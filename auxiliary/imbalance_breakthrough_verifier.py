#!/usr/bin/env python3
"""Independent exact checks accompanying the Imbalance Conjecture proof.

The proof itself is symbolic and does not depend on these finite checks.
This script verifies:
  1. the literal 13-vertex residual counterpacket outside first-failure scope;
  2. the head-reserve and weighted-residual inequalities on every unlabeled
     graph in the NetworkX graph atlas (orders <= 7), for every boundary-tie
     choice of a top-k set;
  3. the same checks on all locally irregular nonisomorphic trees through
     order 16;
  4. the final multiplicity inequality on all integer head profiles k <= 50.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb, floor
import networkx as nx


def locally_irregular(G: nx.Graph) -> bool:
    d = dict(G.degree())
    return all(d[u] != d[v] for u, v in G.edges())


def eg_deficit(seq: list[int], k: int) -> int:
    return k * (k - 1) + sum(min(k, x) for x in seq[k:]) - sum(seq[:k])


def oriented_edges(G: nx.Graph):
    d = dict(G.degree())
    out = []
    for idx, (a, b) in enumerate(G.edges()):
        if d[a] > d[b]:
            u, v = a, b
        else:
            u, v = b, a
        out.append((d[u] - d[v], idx, u, v))
    return sorted(out, key=lambda e: (-e[0], e[1]))


def all_top_sets(G: nx.Graph, k: int):
    es = oriented_edges(G)
    threshold = es[k - 1][0]
    mandatory = [e for e in es if e[0] > threshold]
    tied = [e for e in es if e[0] == threshold]
    need = k - len(mandatory)
    for choice in combinations(tied, need):
        yield mandatory + list(choice), [e[0] for e in es]


def packet_data(G: nx.Graph, S, k: int):
    d = dict(G.degree())
    s = Counter(e[2] for e in S)
    U = set(s)
    h = len(U)
    p = k - h
    H = set(G) - U

    q = {}
    Q = 0
    for z in H:
        qz = sum(max(0, s[u] - abs(d[u] - d[z])) for u in G.neighbors(z) if u in U)
        q[z] = qz
        Q += qz

    TV = sum(
        min(k, abs(d[x] - d[y]))
        for x, y in G.edges()
        if x in H and y in H
    )
    psi = sum(
        2 * s[u] * s[v] - s[u] - s[v] + 1
        for u, v in combinations(U, 2)
    )
    es = [s[u] - 1 for u in U]
    collision_numerator = sum(e * (k - e) ** 2 for e in es)
    weights = sorted((abs(d[x] - d[y]) for x, y in G.edges()), reverse=True)
    delta = eg_deficit(weights, k)
    return d, s, U, h, p, q, Q, TV, psi, collision_numerator, weights, delta


def check_threshold_case(G: nx.Graph, S, k: int):
    d, s, U, h, p, q, Q, TV, psi, C, weights, delta = packet_data(G, S, k)
    assert delta >= TV - Q + psi, ("head reserve", G.edges(), k)
    if p > 0:
        assert 4 * p * (Q - TV) <= C, ("weighted residual", G.edges(), k)
    if h >= 2 and p > 0:
        assert C < 4 * p * psi, ("multiplicity dominance", G.edges(), k)
    assert delta >= 0, ("top-threshold conclusion", G.edges(), k)


def verify_counterpacket():
    G = nx.Graph()
    G.add_edges_from([
        ("u", "z"), ("u", "x"), ("u", "y"),
        ("u", "a1"), ("u", "a2"), ("u", "a3"),
        ("v", "z"), ("v", "x"), ("v", "y"),
        ("v", "b"), ("v", "p"), ("v", "q"),
        ("w", "z"), ("w", "x"), ("w", "y"),
        ("w", "c"), ("w", "p"), ("w", "q"),
        ("z", "x"), ("z", "y"),
    ])
    d = dict(G.degree())
    assert locally_irregular(G)
    weights = sorted((abs(d[x] - d[y]) for x, y in G.edges()), reverse=True)
    assert Counter(weights) == Counter({5: 5, 4: 4, 2: 6, 1: 5})
    S = [e for e in oriented_edges(G) if e[0] == 5]
    data = packet_data(G, S, 5)
    _, s, U, h, p, q, Q, TV, psi, C, weights, delta = data
    assert s == Counter({"u": 3, "v": 1, "w": 1})
    assert q["z"] == 2 and q["x"] == 1 and q["y"] == 1
    assert Q == 4 and TV == 2
    deficits = [eg_deficit(weights, k) for k in range(1, len(weights) + 1)]
    assert min(deficits) == 14
    return d, weights, deficits, Q, TV, psi, C, delta


@lru_cache(None)
def partitions(n: int, max_part: int):
    if n == 0:
        return ((),)
    ans = []
    for a in range(min(n, max_part), 0, -1):
        for rest in partitions(n - a, a):
            ans.append((a,) + rest)
    return tuple(ans)


def profile_psi(es):
    h = len(es)
    p = sum(es)
    s2 = sum(e * e for e in es)
    return p * p - s2 + (h - 1) * p + h * (h - 1) // 2


def verify_profiles(kmax: int = 50):
    checked = 0
    smallest_gap = None
    smallest_profile = None
    for k in range(3, kmax + 1):
        for h in range(2, k):
            p = k - h
            for pos in partitions(p, p):
                if len(pos) > h:
                    continue
                es = pos + (0,) * (h - len(pos))
                psi = profile_psi(es)
                C = sum(e * (k - e) ** 2 for e in es)
                gap = 4 * p * psi - C
                assert gap > 0, (k, h, es, gap)
                checked += 1
                if smallest_gap is None or gap < smallest_gap:
                    smallest_gap = gap
                    smallest_profile = (k, h, es)
    return checked, smallest_gap, smallest_profile


def audit_graph_family(graphs):
    graph_count = 0
    threshold_cases = 0
    tie_choices = 0
    for G in graphs:
        if G.number_of_edges() == 0 or not locally_irregular(G):
            continue
        graph_count += 1
        m = G.number_of_edges()
        for k in range(2, m + 1):
            for S, weights in all_top_sets(G, k):
                tie_choices += 1
                if weights[k - 1] < k:
                    continue
                threshold_cases += 1
                check_threshold_case(G, S, k)
    return graph_count, threshold_cases, tie_choices


def main():
    d, weights, deficits, Q, TV, psi, C, delta = verify_counterpacket()
    print("COUNTERPACKET_OK")
    print("degrees=", dict(sorted(d.items())))
    print("weights=", weights)
    print("EG_deficits=", deficits)
    print(f"k=5: TV={TV}, Q={Q}, residual_gap={TV-Q}, Psi={psi}, Delta_5={delta}")

    atlas_result = audit_graph_family(nx.graph_atlas_g())
    print("ATLAS_OK", atlas_result, "(graphs, threshold cases, tie choices)")

    def trees_through_16():
        for n in range(2, 17):
            if n == 2:
                yield nx.path_graph(2)
            else:
                yield from nx.nonisomorphic_trees(n)

    tree_result = audit_graph_family(trees_through_16())
    print("TREES_OK", tree_result, "(graphs, threshold cases, tie choices)")

    profile_result = verify_profiles(50)
    print("PROFILES_OK", profile_result, "(profiles, smallest gap, profile)")


if __name__ == "__main__":
    main()
