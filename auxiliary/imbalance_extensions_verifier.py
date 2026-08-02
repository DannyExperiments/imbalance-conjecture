#!/usr/bin/env python3
"""Independent finite checks for the quantitative Imbalance results.

These checks are not proofs. They verify:
  * the profile-dependent bound and 4 p Psi - C >= 4 p through k=50;
  * the arbitrary threshold-set inequality for every qualifying edge subset
    in every locally irregular graph in the NetworkX graph atlas;
  * the threshold equality classification (including k=1) on that search;
  * the sorted equality classification for every locally irregular
    nonisomorphic tree through order 16;
  * the two converse sequence formulas and uniqueness of their small target
    realizations within the graph atlas;
  * the zero-edge correction bounds on every qualifying subset in every
    graph in the atlas;
  * graphicality for every atlas graph with at most one zero-imbalance edge.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
import networkx as nx


def locally_irregular(G: nx.Graph) -> bool:
    d = dict(G.degree())
    return all(d[u] != d[v] for u, v in G.edges())


def edge_weights(G: nx.Graph) -> dict[tuple, int]:
    d = dict(G.degree())
    return {tuple(sorted((u, v), key=repr)): abs(d[u] - d[v]) for u, v in G.edges()}


def imbalance_sequence(G: nx.Graph) -> list[int]:
    return sorted(edge_weights(G).values(), reverse=True)


def eg_deficit(seq: list[int], k: int) -> int:
    return k * (k - 1) + sum(min(k, x) for x in seq[k:]) - sum(seq[:k])


def subset_deficit(weights: dict[tuple, int], S: tuple[tuple, ...], k: int) -> int:
    selected = set(S)
    return (
        k * (k - 1)
        + sum(min(k, w) for e, w in weights.items() if e not in selected)
        - sum(weights[e] for e in selected)
    )


@lru_cache(None)
def partitions(n: int, cap: int):
    if n == 0:
        return ((),)
    out = []
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            out.append((first,) + rest)
    return tuple(out)


def profile_psi(es: tuple[int, ...]) -> int:
    h = len(es)
    p = sum(es)
    s2 = sum(e * e for e in es)
    return p * p - s2 + (h - 1) * p + h * (h - 1) // 2


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def profile_bound(h: int, p: int) -> int:
    if 2 * h >= 3 * p:
        num = 3 * p * p + (2 * h - 4) * p + h * (h - 2)
    else:
        num = 4 * (h - 1) * p + h * (h - 2)
    return ceil_div(num, 4)


def check_profiles(kmax: int = 50):
    checked = 0
    minimum_margin = None
    witness = None
    for k in range(3, kmax + 1):
        for h in range(2, k):
            p = k - h
            for positive in partitions(p, p):
                if len(positive) > h:
                    continue
                es = positive + (0,) * (h - len(positive))
                psi = profile_psi(es)
                C = sum(e * (k - e) ** 2 for e in es)
                gap = 4 * p * psi - C
                assert gap >= 4 * p, (k, h, es, gap, 4 * p)
                assert ceil_div(gap, 4 * p) >= profile_bound(h, p), (
                    k, h, es, gap, profile_bound(h, p)
                )
                checked += 1
                margin = gap - 4 * p
                if minimum_margin is None or margin < minimum_margin:
                    minimum_margin = margin
                    witness = (k, h, es, gap)
    return checked, minimum_margin, witness


def strip_isolates(G: nx.Graph) -> nx.Graph:
    H = G.copy()
    H.remove_nodes_from(list(nx.isolates(H)))
    return H


def is_star_graph(G: nx.Graph) -> bool:
    H = strip_isolates(G)
    if H.number_of_nodes() < 2 or not nx.is_connected(H):
        return False
    n = H.number_of_nodes()
    ds = sorted((d for _, d in H.degree()), reverse=True)
    return ds == [n - 1] + [1] * (n - 1)


def is_star_case(G: nx.Graph, k: int) -> bool:
    H = strip_isolates(G)
    return is_star_graph(G) and H.number_of_edges() >= k + 1


def is_subdivided_star_case(G: nx.Graph, k: int) -> bool:
    H = strip_isolates(G)
    if not nx.is_tree(H) or H.number_of_nodes() != k + 3:
        return False
    ds = sorted((d for _, d in H.degree()), reverse=True)
    return ds == [k + 1, 2] + [1] * (k + 1)


def selected_is_direct_leaf_set(G: nx.Graph, S: tuple[tuple, ...], k: int) -> bool:
    H = strip_isolates(G)
    centers = [v for v, d in H.degree() if d == k + 1]
    if len(centers) != 1:
        return False
    u = centers[0]
    expected = {
        tuple(sorted((u, v), key=repr))
        for v in H.neighbors(u)
        if H.degree(v) == 1
    }
    return len(expected) == k and set(S) == expected


def audit_threshold_subsets(graphs):
    locally_irregular_count = 0
    subset_count = 0
    equality_count = 0
    nontop_count = 0
    for G in graphs:
        if G.number_of_edges() == 0 or not locally_irregular(G):
            continue
        locally_irregular_count += 1
        weights = edge_weights(G)
        ordered = sorted(weights.values(), reverse=True)
        m = len(weights)
        for k in range(1, m + 1):
            eligible = [e for e, w in weights.items() if w >= k]
            if len(eligible) < k:
                continue
            top_sum = sum(ordered[:k])
            for S in combinations(eligible, k):
                subset_count += 1
                D = subset_deficit(weights, S, k)
                assert D >= 0, (list(G.edges()), dict(G.degree()), weights, k, S, D)
                if sum(weights[e] for e in S) < top_sum:
                    nontop_count += 1
                if D == 0:
                    equality_count += 1
                    if k == 1:
                        assert is_star_graph(G), (list(G.edges()), dict(G.degree()), k, S)
                    else:
                        ok = is_star_case(G, k) or (
                            is_subdivided_star_case(G, k)
                            and selected_is_direct_leaf_set(G, S, k)
                        )
                        assert ok, (list(G.edges()), dict(G.degree()), weights, k, S)
    return locally_irregular_count, subset_count, nontop_count, equality_count


def audit_sorted_family(graphs):
    locally_irregular_count = 0
    equality_count = 0
    for G in graphs:
        if G.number_of_edges() == 0 or not locally_irregular(G):
            continue
        locally_irregular_count += 1
        seq = imbalance_sequence(G)
        for k in range(2, len(seq) + 1):
            if seq[k - 1] >= k and eg_deficit(seq, k) == 0:
                equality_count += 1
                assert is_star_case(G, k) or is_subdivided_star_case(G, k), (
                    list(G.nodes()), list(G.edges()), dict(G.degree()), seq, k
                )
    return locally_irregular_count, equality_count



def zero_correction_lower_bound(
    G: nx.Graph,
    weights: dict[tuple, int],
    S: tuple[tuple, ...],
    k: int,
) -> tuple[int, tuple]:
    d = dict(G.degree())
    s_head: dict[object, int] = {}
    selected_lows = []
    for x, y in S:
        assert d[x] != d[y] and weights[(x, y)] >= k
        if d[x] > d[y]:
            head, low = x, y
        else:
            head, low = y, x
        s_head[head] = s_head.get(head, 0) + 1
        selected_lows.append(low)

    U = set(s_head)
    h = len(U)
    p = k - h
    z_uu = z_uh = z_h = 0
    for (x, y), w in weights.items():
        if w != 0:
            continue
        xu, yu = x in U, y in U
        if xu and yu:
            z_uu += 1
        elif xu or yu:
            z_uh += 1
        else:
            z_h += 1

    if h == k:
        lower = k * (k - 1) // 2 - z_uu - z_uh
    elif h == 1:
        B = sum(d[v] - 1 for v in selected_lows)
        lower = B - 2 * z_h
    else:
        lower = profile_bound(h, p) - z_uu - z_uh - 2 * z_h
    return lower, (h, p, z_uu, z_uh, z_h, s_head, tuple(selected_lows))


def audit_zero_corrections(graphs):
    graph_count = subset_count = 0
    minimum_margin = None
    witness = None
    for G in graphs:
        if G.number_of_edges() == 0:
            continue
        graph_count += 1
        weights = edge_weights(G)
        m = len(weights)
        for k in range(2, m + 1):
            eligible = [e for e, w in weights.items() if w >= k]
            if len(eligible) < k:
                continue
            for S in combinations(eligible, k):
                subset_count += 1
                D = subset_deficit(weights, S, k)
                lower, metadata = zero_correction_lower_bound(G, weights, S, k)
                assert D >= lower, (
                    list(G.edges()), dict(G.degree()), weights, k, S, D, lower, metadata
                )
                margin = D - lower
                if minimum_margin is None or margin < minimum_margin:
                    minimum_margin = margin
                    witness = (k, S, D, lower, metadata)
    return graph_count, subset_count, minimum_margin, witness


def audit_one_zero_graphs(graphs):
    checked = exact_one = 0
    for G in graphs:
        if G.number_of_edges() == 0:
            continue
        seq = imbalance_sequence(G)
        zero_count = seq.count(0)
        if zero_count > 1:
            continue
        checked += 1
        exact_one += zero_count == 1
        assert nx.is_graphical(seq, method="eg"), (
            list(G.edges()), dict(G.degree()), seq, zero_count
        )
    return checked, exact_one


def trees_through_16():
    for n in range(2, 17):
        if n == 2:
            yield nx.path_graph(2)
        else:
            yield from nx.nonisomorphic_trees(n)


def check_converse_formulas(kmax: int = 100):
    for t in range(2, kmax + 2):
        G = nx.star_graph(t)  # K_{1,t}
        seq = imbalance_sequence(G)
        assert seq == [t - 1] * t
        # k=1 equality and all k<=t-1 threshold equalities.
        weights = edge_weights(G)
        edges = tuple(weights)
        assert subset_deficit(weights, (edges[0],), 1) == 0
        for k in range(2, t):
            assert seq[k - 1] >= k
            assert eg_deficit(seq, k) == 0
            assert subset_deficit(weights, edges[:k], k) == 0
    for k in range(2, kmax + 1):
        G = nx.Graph()
        u = "u"
        direct = []
        for i in range(k):
            e = tuple(sorted((u, f"l{i}"), key=repr))
            direct.append(e)
            G.add_edge(*e)
        G.add_edge(u, "z")
        G.add_edge("z", "y")
        assert locally_irregular(G)
        seq = imbalance_sequence(G)
        assert seq == [k] * k + [k - 1, 1]
        assert eg_deficit(seq, k) == 0
        assert subset_deficit(edge_weights(G), tuple(direct), k) == 0


def check_small_target_uniqueness():
    atlas = nx.graph_atlas_g()
    by_seq: dict[tuple[int, ...], list[nx.Graph]] = {}
    for H in atlas:
        seq = tuple(sorted((d for _, d in H.degree()), reverse=True))
        by_seq.setdefault(seq, []).append(H)
    checks = 0
    # Atlas has graphs through seven vertices, so t<=7 and k+2<=7.
    for t in range(2, 8):
        seq = (t - 1,) * t
        candidates = by_seq.get(seq, [])
        assert len(candidates) == 1 and nx.is_isomorphic(candidates[0], nx.complete_graph(t))
        checks += 1
    for k in range(2, 6):
        seq = tuple([k] * k + [k - 1, 1])
        candidates = by_seq.get(seq, [])
        assert len(candidates) == 1, (k, len(candidates))
        checks += 1
    return checks


def main():
    print("PROFILE_STRENGTHENING_OK", check_profiles())
    atlas = nx.graph_atlas_g()
    print("ATLAS_THRESHOLD_SUBSETS_OK", audit_threshold_subsets(atlas))
    print("ATLAS_ZERO_CORRECTIONS_OK", audit_zero_corrections(atlas))
    print("ATLAS_ONE_ZERO_GRAPHICAL_OK", audit_one_zero_graphs(atlas))
    print("TREE_SORTED_EQUALITY_OK", audit_sorted_family(trees_through_16()))
    check_converse_formulas()
    print("CONVERSE_FORMULAS_OK")
    print("SMALL_TARGET_UNIQUENESS_OK", check_small_target_uniqueness())


if __name__ == "__main__":
    main()
