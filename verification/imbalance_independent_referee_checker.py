#!/usr/bin/env python3
"""Dependency-free adversarial checker for the Imbalance Conjecture packet.

No NetworkX or third-party package is used.  Exact integer arithmetic only.

Complete finite universes checked by default:
  * every labeled simple graph on 0..5 vertices;
  * every labeled bipartite graph on fixed sides 2+6 and 3+4;
  * all qualifying threshold subsets in those universes;
  * every top-set choice across every boundary tie;
  * all zero-edge correction inequalities (Z1)--(Z8);
  * all source equality classifications;
  * target uniqueness for the two claimed target families through 6 vertices.

It also performs deterministic random tests on general, bipartite, multipartite,
disconnected, star, and subdivided-star families.  The random lane is evidence,
not exhaustive coverage.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
import hashlib
import json
import math
import random
import sys
from typing import Iterable, Iterator, Sequence


@dataclass
class Stats:
    graphs: int = 0
    graphs_nonempty: int = 0
    locally_irregular: int = 0
    at_most_one_zero: int = 0
    exactly_one_zero: int = 0
    threshold_sets_li: int = 0
    threshold_sets_zero: int = 0
    top_sets_li: int = 0
    top_tie_sets_li: int = 0
    identities_2: int = 0
    inequalities_3: int = 0
    inequalities_5: int = 0
    inequalities_11: int = 0
    inequalities_12: int = 0
    inequalities_13: int = 0
    inequalities_19: int = 0
    zero_z4: int = 0
    zero_z5: int = 0
    zero_z6: int = 0
    zero_z7: int = 0
    zero_z8: int = 0
    zero_final: int = 0
    equality_cases: int = 0
    one_zero_top_sets: int = 0
    one_zero_exception_21: int = 0
    one_zero_single_head: int = 0
    r0_repairs: int = 0
    random_graphs: int = 0
    random_threshold_sets: int = 0


STATS = Stats()
MINIMA: dict[str, tuple[int, object]] = {}


def update_min(name: str, value: int, witness: object) -> None:
    old = MINIMA.get(name)
    if old is None or value < old[0]:
        MINIMA[name] = (value, witness)


def fail(kind: str, packet: dict) -> None:
    print("CERTIFIED_COUNTEREXAMPLE", kind)
    print(json.dumps(packet, sort_keys=True, indent=2))
    raise AssertionError(kind)


def all_pairs(n: int) -> list[tuple[int, int]]:
    return [(u, v) for u in range(n) for v in range(u + 1, n)]


def graph_from_mask(n: int, pairs: Sequence[tuple[int, int]], mask: int) -> list[tuple[int, int]]:
    return [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]


def graph_data(n: int, edges: Sequence[tuple[int, int]]):
    deg = [0] * n
    adj = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    weights = [abs(deg[u] - deg[v]) for u, v in edges]
    return deg, adj, weights


def eg_deficits(seq: Sequence[int]) -> list[int]:
    x = sorted(seq, reverse=True)
    return [
        k * (k - 1) + sum(min(k, z) for z in x[k:]) - sum(x[:k])
        for k in range(1, len(x) + 1)
    ]


def is_graphical(seq: Sequence[int]) -> bool:
    m = len(seq)
    if sum(seq) & 1:
        return False
    if any(d < 0 or d >= m for d in seq):
        return False
    return all(d >= 0 for d in eg_deficits(seq))


def subset_deficit(weights: Sequence[int], S: Sequence[int], k: int) -> int:
    ss = set(S)
    return k * (k - 1) + sum(min(k, w) for i, w in enumerate(weights) if i not in ss) - sum(weights[i] for i in S)


def top_sets(weights: Sequence[int], k: int) -> Iterator[tuple[int, ...]]:
    if not (1 <= k <= len(weights)):
        return
    order_values = sorted(weights, reverse=True)
    t = order_values[k - 1]
    mandatory = [i for i, w in enumerate(weights) if w > t]
    boundary = [i for i, w in enumerate(weights) if w == t]
    need = k - len(mandatory)
    for c in combinations(boundary, need):
        yield tuple(sorted(mandatory + list(c)))


def qualifying_sets(weights: Sequence[int], k: int) -> Iterator[tuple[int, ...]]:
    eligible = [i for i, w in enumerate(weights) if w >= k]
    if len(eligible) >= k:
        yield from combinations(eligible, k)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def profile_bound(h: int, p: int) -> int:
    if 2 * h >= 3 * p:
        return ceil_div(3 * p * p + (2 * h - 4) * p + h * (h - 2), 4)
    return ceil_div(4 * (h - 1) * p + h * (h - 2), 4)


def strip_active(n: int, deg: Sequence[int]) -> list[int]:
    return [v for v in range(n) if deg[v] > 0]


def is_source_star(n: int, edges: Sequence[tuple[int, int]], deg: Sequence[int]) -> bool:
    active = strip_active(n, deg)
    if len(active) < 2:
        return False
    aset = set(active)
    eactive = [(u, v) for u, v in edges if u in aset and v in aset]
    ds = sorted((deg[v] for v in active), reverse=True)
    return len(eactive) == len(active) - 1 and ds == [len(active) - 1] + [1] * (len(active) - 1)


def subdivided_star_direct_edges(n: int, edges: Sequence[tuple[int, int]], deg: Sequence[int], k: int):
    active = strip_active(n, deg)
    if len(active) != k + 3 or len(edges) != k + 2:
        return None
    centers = [v for v in active if deg[v] == k + 1]
    mids = [v for v in active if deg[v] == 2]
    leaves = [v for v in active if deg[v] == 1]
    if len(centers) != 1 or len(mids) != 1 or len(leaves) != k + 1:
        return None
    c, m = centers[0], mids[0]
    eset = {tuple(sorted(e)) for e in edges}
    if tuple(sorted((c, m))) not in eset:
        return None
    mid_leaves = [x for x in leaves if tuple(sorted((m, x))) in eset]
    direct = [x for x in leaves if tuple(sorted((c, x))) in eset]
    if len(mid_leaves) != 1 or len(direct) != k:
        return None
    expected = {tuple(sorted((c, m))), tuple(sorted((m, mid_leaves[0])))} | {
        tuple(sorted((c, x))) for x in direct
    }
    if eset != expected:
        return None
    return {next(i for i, e in enumerate(edges) if tuple(sorted(e)) == tuple(sorted((c, x)))) for x in direct}


def equality_classified(n: int, edges, deg, S: Sequence[int], k: int) -> bool:
    if k == 1:
        return is_source_star(n, edges, deg)
    if is_source_star(n, edges, deg):
        return len(edges) >= k + 1
    direct = subdivided_star_direct_edges(n, edges, deg, k)
    return direct is not None and set(S) == direct


def oriented_edge(edge: tuple[int, int], deg: Sequence[int]) -> tuple[int, int]:
    u, v = edge
    if deg[u] > deg[v]:
        return u, v
    if deg[v] > deg[u]:
        return v, u
    raise ValueError("zero edge cannot be selected")


def metric_packet(n: int, edges: Sequence[tuple[int, int]], deg: Sequence[int], weights: Sequence[int], S: Sequence[int], k: int):
    selected = set(S)
    s = [0] * n
    ell = [0] * n
    oriented_selected = []
    for i in S:
        h, l = oriented_edge(edges[i], deg)
        s[h] += 1
        ell[l] += 1
        oriented_selected.append((i, h, l, weights[i]))
    U = [v for v in range(n) if s[v] > 0]
    Uset = set(U)
    H = [v for v in range(n) if v not in Uset]
    Hset = set(H)
    h = len(U)
    p = k - h
    eprof = {u: s[u] - 1 for u in U}
    pf = [s[u] + s[v] for u, v in edges]
    B = sum(ell[v] * (deg[v] - 1) for v in range(n))
    P = sum(k - pf[i] for i in S)
    psi = sum(2 * s[u] * s[v] - s[u] - s[v] + 1 for u, v in combinations(U, 2))
    D = subset_deficit(weights, S, k)
    identity_rhs = B + sum(min(k, weights[i]) - pf[i] for i in range(len(edges)))
    TV = sum(min(k, weights[i]) for i, (x, y) in enumerate(edges) if x in Hset and y in Hset)
    dH = [0] * n
    for x, y in edges:
        if x in Hset and y in Hset:
            dH[x] += 1
            dH[y] += 1
    by_head = {}
    Q = 0
    eset = {tuple(sorted(e)) for e in edges}
    for u in U:
        qmap = {}
        for z in H:
            if (min(u, z), max(u, z)) not in eset:
                continue
            q = max(0, s[u] - abs(deg[u] - deg[z]))
            if q > 0:
                qmap[z] = q
        A = set(qmap)
        Qu = sum(qmap.values())
        Q += Qu
        Wu = sum(min(k, weights[i]) for i, (x, y) in enumerate(edges)
                 if x in Hset and y in Hset and (x in A or y in A))
        E1 = sum(1 for i, (x, y) in enumerate(edges)
                 if x in A and y in A and weights[i] == 1)
        zeta = sum((1 if x in A else 0) + (1 if y in A else 0)
                   for i, (x, y) in enumerate(edges)
                   if x in Hset and y in Hset and weights[i] == 0)
        t = sum(1 for z in A if deg[z] == deg[u])
        by_head[u] = {
            "qmap": qmap, "A": A, "Q": Qu, "W": Wu, "E1": E1,
            "zeta": zeta, "t": t, "n": len(A), "e": eprof[u],
            "a": deg[u] - k - 1,
        }
    ZUU = sum(1 for i, (x, y) in enumerate(edges) if x in Uset and y in Uset and weights[i] == 0)
    ZUH = sum(1 for i, (x, y) in enumerate(edges) if ((x in Uset) ^ (y in Uset)) and weights[i] == 0)
    ZH = sum(1 for i, (x, y) in enumerate(edges) if x in Hset and y in Hset and weights[i] == 0)
    C = sum(eprof[u] * (k - eprof[u]) ** 2 for u in U)
    return {
        "selected": selected, "oriented_selected": oriented_selected,
        "s": s, "ell": ell, "U": U, "H": H, "h": h, "p": p,
        "eprof": eprof, "pf": pf, "B": B, "P": P, "psi": psi,
        "D": D, "identity_rhs": identity_rhs, "TV": TV, "Q": Q,
        "dH": dH, "by_head": by_head, "ZUU": ZUU, "ZUH": ZUH,
        "ZH": ZH, "C": C,
    }


def base_packet(n, edges, deg, weights, S=None, k=None):
    oriented = []
    for i, (u, v) in enumerate(edges):
        if deg[u] > deg[v]:
            oriented.append((i, u, v, weights[i]))
        elif deg[v] > deg[u]:
            oriented.append((i, v, u, weights[i]))
        else:
            oriented.append((i, u, v, 0))
    seq = sorted(weights, reverse=True)
    packet = {
        "vertices": list(range(n)), "edges": [list(e) for e in edges],
        "degrees": deg, "oriented_edges": [list(x) for x in oriented],
        "weights_sorted": seq, "eg_deficits": eg_deficits(seq),
    }
    if S is not None:
        packet["k"] = k
        packet["S_indices"] = list(S)
        packet["S_edges"] = [list(edges[i]) for i in S]
    return packet


def check_li_threshold_set(n, edges, deg, weights, S, k, lane: str):
    STATS.threshold_sets_li += 1
    if lane == "random":
        STATS.random_threshold_sets += 1
    M = metric_packet(n, edges, deg, weights, S, k)
    packet = base_packet(n, edges, deg, weights, S, k)
    packet.update({key: val for key, val in M.items() if key not in {"selected", "by_head"}})
    packet["by_head"] = {str(u): {kk: (sorted(vv) if isinstance(vv, set) else vv) for kk, vv in d.items()} for u, d in M["by_head"].items()}

    STATS.identities_2 += 1
    if M["D"] != M["identity_rhs"]:
        fail("(2)", packet | {"lhs": M["D"], "rhs": M["identity_rhs"]})

    pair_rhs = 2 * sum(M["s"][u] * M["s"][v] for u, v in combinations(M["U"], 2))
    STATS.inequalities_3 += 1
    update_min("(3)", M["B"] + M["P"] - pair_rhs, packet)
    if M["B"] + M["P"] < pair_rhs:
        fail("(3)", packet | {"lhs": M["B"] + M["P"], "rhs": pair_rhs})

    STATS.inequalities_5 += 1
    rhs5 = M["TV"] - M["Q"] + M["psi"]
    update_min("(5)", M["D"] - rhs5, packet)
    if M["D"] < rhs5:
        fail("(5)", packet | {"lhs": M["D"], "rhs": rhs5})

    for u, R in M["by_head"].items():
        e = R["e"]
        if e == 0:
            if R["A"] or R["Q"]:
                fail("e=0 active in locally irregular graph", packet)
            continue
        a, nn, Qu, Wu = R["a"], R["n"], R["Q"], R["W"]
        if a < 0:
            fail("(6) a<0", packet | {"u": u, "a": a})
        # Every active edge is unselected, (7), and (8).
        if nn > deg[u] - M["s"][u] or nn > k - e + a:
            fail("(7)", packet | {"u": u, "n": nn, "bound": k - e + a})
        for z, q in R["qmap"].items():
            edge_id = next(i for i, xy in enumerate(edges) if tuple(sorted(xy)) == tuple(sorted((u, z))))
            if edge_id in M["selected"]:
                fail("active edge selected", packet | {"u": u, "z": z})
            j = abs(deg[u] - deg[z])
            if not (1 <= j <= e and q == e + 1 - j):
                fail("active q formula", packet | {"u": u, "z": z, "j": j, "q": q, "e": e})
            bound8 = q + M["p"] - e + a
            if M["dH"][z] < bound8:
                fail("(8)", packet | {"u": u, "z": z, "dH": M["dH"][z], "rhs": bound8})
            if deg[z] > deg[u] and M["dH"][z] < bound8 + 2 * j:
                fail("(8) high-sign sharpening", packet | {"u": u, "z": z})
        sumd = sum(M["dH"][z] for z in R["A"])
        if Wu < sumd - R["E1"]:
            fail("(9)", packet | {"u": u, "W": Wu, "sumd": sumd, "E1": R["E1"]})
        if R["E1"] > (nn * nn) // 4:
            fail("(10)", packet | {"u": u, "E1": R["E1"], "bound": nn * nn // 4})
        lhs11 = M["p"] * Qu - e * Wu
        rhs11a = e * R["E1"] - e * a * nn - (M["p"] - e) * sum(e - q for q in R["qmap"].values())
        rhs11 = e * ((nn * nn) // 4 - a * nn)
        STATS.inequalities_11 += 1
        update_min("(11a)", rhs11a - lhs11, packet)
        update_min("(11)", rhs11 - lhs11, packet)
        if lhs11 > rhs11a or rhs11a > rhs11:
            fail("(11)", packet | {"u": u, "lhs": lhs11, "middle": rhs11a, "rhs": rhs11})
        STATS.inequalities_12 += 1
        margin12 = e * (k - e) ** 2 - 4 * lhs11
        update_min("(12)x4", margin12, packet)
        if margin12 < 0:
            fail("(12)", packet | {"u": u, "lhs_x4": 4 * lhs11, "rhs_x4": e * (k - e) ** 2})

    if M["p"] > 0:
        STATS.inequalities_13 += 1
        margin13 = M["C"] - 4 * M["p"] * (M["Q"] - M["TV"])
        update_min("(13)x4", margin13, packet)
        if margin13 < 0:
            fail("(13)", packet | {"lhs_x4": 4 * M["p"] * (M["Q"] - M["TV"]), "rhs_x4": M["C"]})
    if M["h"] >= 2 and M["p"] > 0:
        STATS.inequalities_19 += 1
        margin19 = 4 * M["p"] * M["psi"] - M["C"]
        update_min("(19)", margin19, packet)
        if margin19 <= 0:
            fail("(19)", packet | {"lhs": 4 * M["p"] * M["psi"], "rhs": M["C"]})

    if M["D"] < 0:
        fail("threshold-set theorem", packet | {"D": M["D"]})
    if M["D"] == 0:
        STATS.equality_cases += 1
        if not equality_classified(n, edges, deg, S, k):
            fail("threshold equality classification", packet)


def check_zero_threshold_set(n, edges, deg, weights, S, k):
    STATS.threshold_sets_zero += 1
    M = metric_packet(n, edges, deg, weights, S, k)
    packet = base_packet(n, edges, deg, weights, S, k)
    packet.update({key: val for key, val in M.items() if key not in {"selected", "by_head"}})
    packet["by_head"] = {str(u): {kk: (sorted(vv) if isinstance(vv, set) else vv) for kk, vv in d.items()} for u, d in M["by_head"].items()}

    if M["D"] != M["identity_rhs"]:
        fail("zero (2)", packet)
    rhs4 = M["TV"] - M["Q"] + M["psi"] - M["ZUU"]
    STATS.zero_z4 += 1
    update_min("Z4", M["D"] - rhs4, packet)
    if M["D"] < rhs4:
        fail("Z4", packet | {"lhs": M["D"], "rhs": rhs4})

    for u, R in M["by_head"].items():
        e, nn, a = R["e"], R["n"], R["a"]
        if a < 0:
            fail("zero a<0", packet | {"u": u})
        # Degree estimate including zero j=0.
        for z, q in R["qmap"].items():
            bound = q + M["p"] - e + a
            if M["dH"][z] < bound:
                fail("zero degree estimate", packet | {"u": u, "z": z, "lhs": M["dH"][z], "rhs": bound})
        sumd = sum(M["dH"][z] for z in R["A"])
        STATS.zero_z5 += 1
        if R["W"] < sumd - R["E1"] - R["zeta"]:
            fail("Z5", packet | {"u": u, "lhs": R["W"], "rhs": sumd - R["E1"] - R["zeta"]})
        STATS.zero_z6 += 1
        if R["Q"] - e * nn > R["t"]:
            fail("Z6", packet | {"u": u, "lhs": R["Q"] - e * nn, "rhs": R["t"]})
        STATS.zero_z7 += 1
        lhs7 = 4 * (M["p"] * R["Q"] - e * R["W"])
        rhs7 = e * (k - e) ** 2 + 4 * e * R["zeta"] + 4 * (M["p"] - e) * R["t"]
        update_min("Z7x4", rhs7 - lhs7, packet)
        if lhs7 > rhs7:
            fail("Z7", packet | {"u": u, "lhs_x4": lhs7, "rhs_x4": rhs7})

    if M["p"] > 0:
        STATS.zero_z8 += 1
        lhs8 = 4 * M["p"] * (M["Q"] - M["TV"])
        rhs8 = M["C"] + 8 * M["p"] * M["ZH"] + 4 * M["p"] * M["ZUH"]
        update_min("Z8x4", rhs8 - lhs8, packet)
        if lhs8 > rhs8:
            fail("Z8", packet | {"lhs_x4": lhs8, "rhs_x4": rhs8})

    STATS.zero_final += 1
    if M["h"] == k:
        rhs = math.comb(k, 2) - M["ZUU"] - M["ZUH"]
        name = "Z1"
    elif M["h"] == 1:
        rhs = M["B"] - 2 * M["ZH"]
        name = "Z3"
    else:
        rhs = profile_bound(M["h"], M["p"]) - M["ZUU"] - M["ZUH"] - 2 * M["ZH"]
        name = "Z2"
    update_min(name, M["D"] - rhs, packet)
    if M["D"] < rhs:
        fail(name, packet | {"lhs": M["D"], "rhs": rhs})


def check_one_zero_details(n, edges, deg, weights):
    positive = sorted((w for w in weights if w > 0), reverse=True)
    r = len(positive)
    if r == 0:
        # Exactly one zero edge was assumed by caller.
        if len(edges) != 1 or sorted(weights, reverse=True) != [0] or not is_graphical([0]):
            fail("r=0 repair", base_packet(n, edges, deg, weights))
        STATS.r0_repairs += 1
        return
    if positive[0] > r - 1:
        fail("one-zero k=1", base_packet(n, edges, deg, weights) | {"r": r, "y1": positive[0]})
    # Select top positive edge sets at every top-threshold index.
    positive_ids = [i for i, w in enumerate(weights) if w > 0]
    pos_weights = [weights[i] for i in positive_ids]
    for k in range(2, r + 1):
        if sorted(pos_weights, reverse=True)[k - 1] < k:
            continue
        for localS in top_sets(pos_weights, k):
            S = tuple(positive_ids[i] for i in localS)
            STATS.one_zero_top_sets += 1
            M = metric_packet(n, edges, deg, weights, S, k)
            if M["D"] < 0:
                fail("one-equal-edge extension", base_packet(n, edges, deg, weights, S, k) | {"D": M["D"]})
            zero_i = weights.index(0)
            zx, zy = edges[zero_i]
            zero_in_H = zx in set(M["H"]) and zy in set(M["H"])
            if M["h"] == 2 and M["p"] == 1 and zero_in_H:
                STATS.one_zero_exception_21 += 1
                if M["Q"] - M["TV"] > 2:
                    fail("one-zero exceptional (h,p)=(2,1)", base_packet(n, edges, deg, weights, S, k) | {"Q": M["Q"], "TV": M["TV"]})
            if M["h"] == 1 and zero_in_H:
                STATS.one_zero_single_head += 1
                u = M["U"][0]
                R = M["by_head"][u]
                a, nn = R["a"], R["n"]
                if a >= 1 and R["E1"] + R["zeta"] > a * nn:
                    fail("one-zero single-head a>=1", base_packet(n, edges, deg, weights, S, k) | {"a": a, "n": nn, "E1": R["E1"], "zeta": R["zeta"]})
                if a == 0 and nn == 1 and M["B"] == 0 and R["zeta"] > 0 and M["TV"] < M["Q"]:
                    fail("one-zero single-head a=0", base_packet(n, edges, deg, weights, S, k) | {"TV": M["TV"], "Q": M["Q"]})


def sampled_qualifying_sets(weights: Sequence[int], min_k: int, cap: int | None, rng: random.Random | None):
    specs=[]
    total=0
    for k in range(min_k, len(weights)+1):
        eligible=tuple(i for i,w in enumerate(weights) if w>=k)
        if len(eligible)>=k:
            c=math.comb(len(eligible),k)
            specs.append((k,eligible,c))
            total+=c
    if cap is None or total<=cap:
        for k,eligible,_ in specs:
            for S in combinations(eligible,k):
                yield k,S
        return
    assert rng is not None
    chosen=set()
    # Cover every qualifying k at least once where the cap allows.
    for k,eligible,_ in specs:
        if len(chosen)>=cap:
            break
        chosen.add((k,tuple(eligible[:k])))
    attempts=0
    while len(chosen)<cap and attempts<50*cap+1000:
        attempts+=1
        k,eligible,_=rng.choice(specs)
        S=tuple(sorted(rng.sample(eligible,k)))
        chosen.add((k,S))
    for item in sorted(chosen):
        yield item


def sampled_top_sets(weights: Sequence[int], k: int, cap: int | None, rng: random.Random | None):
    order_values=sorted(weights,reverse=True)
    t=order_values[k-1]
    mandatory=tuple(i for i,w in enumerate(weights) if w>t)
    boundary=tuple(i for i,w in enumerate(weights) if w==t)
    need=k-len(mandatory)
    count=math.comb(len(boundary),need)
    if cap is None or count<=cap:
        yield from top_sets(weights,k)
        return
    assert rng is not None
    chosen={tuple(sorted(mandatory+boundary[:need]))}
    attempts=0
    while len(chosen)<cap and attempts<50*cap+1000:
        attempts+=1
        chosen.add(tuple(sorted(mandatory+tuple(rng.sample(boundary,need)))))
    yield from sorted(chosen)

def check_graph(n: int, edges: Sequence[tuple[int, int]], lane: str = "exact", subset_cap: int | None = None, rng: random.Random | None = None):
    STATS.graphs += 1
    if lane == "random":
        STATS.random_graphs += 1
    if edges:
        STATS.graphs_nonempty += 1
    deg, adj, weights = graph_data(n, edges)
    zeros = sum(w == 0 for w in weights)
    li = zeros == 0
    if li and edges:
        STATS.locally_irregular += 1
        seq = sorted(weights, reverse=True)
        if not is_graphical(seq):
            fail("final theorem", base_packet(n, edges, deg, weights))
        # Top-threshold ties, independently of arbitrary qualifying subsets.
        for k in range(1, len(edges) + 1):
            sw = sorted(weights, reverse=True)
            if sw[k - 1] < k:
                continue
            top_cap = None if subset_cap is None else min(50, subset_cap)
            for S in sampled_top_sets(weights, k, top_cap, rng):
                STATS.top_sets_li += 1
                boundary = sw.count(sw[k - 1]) > sum(1 for w in sw[:k] if w == sw[k - 1])
                if boundary:
                    STATS.top_tie_sets_li += 1
                D = subset_deficit(weights, S, k)
                if D != eg_deficits(sw)[k - 1]:
                    fail("top tie deficit mismatch", base_packet(n, edges, deg, weights, S, k))
                if D < 0:
                    fail("k=1 threshold", base_packet(n, edges, deg, weights, S, k))
        # Every arbitrary threshold set. Avoid duplicate rechecking top sets only by design;
        # duplicate checks are useful as independent enumeration-path consistency.
        for k, S in sampled_qualifying_sets(weights, 1, subset_cap, rng):
            if k == 1:
                D = subset_deficit(weights, S, k)
                if D < 0:
                    fail("arbitrary threshold k=1", base_packet(n, edges, deg, weights, S, k))
                if D == 0 and not equality_classified(n, edges, deg, S, k):
                    fail("k=1 equality classification", base_packet(n, edges, deg, weights, S, k))
            else:
                check_li_threshold_set(n, edges, deg, weights, S, k, lane)

    if zeros <= 1:
        STATS.at_most_one_zero += 1
        seq = sorted(weights, reverse=True)
        if not is_graphical(seq):
            fail("one-equal-edge theorem", base_packet(n, edges, deg, weights))
        if zeros == 1:
            STATS.exactly_one_zero += 1
            check_one_zero_details(n, edges, deg, weights)

    # Zero-edge correction for every arbitrary graph and qualifying k>=2 subset.
    for k, S in sampled_qualifying_sets(weights, 2, subset_cap, rng):
        check_zero_threshold_set(n, edges, deg, weights, S, k)


def exhaustive_labeled(max_n: int = 6):
    for n in range(max_n + 1):
        pairs = all_pairs(n)
        for mask in range(1 << len(pairs)):
            check_graph(n, graph_from_mask(n, pairs, mask))
        print(f"EXHAUSTIVE_LABELED_DONE n={n} graphs={1 << len(pairs)}")


def exhaustive_bipartite(a: int, b: int):
    n = a + b
    pairs = [(u, a + v) for u in range(a) for v in range(b)]
    for mask in range(1 << len(pairs)):
        check_graph(n, graph_from_mask(n, pairs, mask))
    print(f"EXHAUSTIVE_BIPARTITE_DONE sides={a}+{b} graphs={1 << len(pairs)}")


def complete_multipartite(parts: Sequence[int]) -> tuple[int, list[tuple[int, int]]]:
    starts = []
    s = 0
    for p in parts:
        starts.append(range(s, s + p))
        s += p
    edges = []
    for i in range(len(starts)):
        for j in range(i + 1, len(starts)):
            edges.extend((u, v) for u in starts[i] for v in starts[j])
    return s, edges


def deterministic_structural_tests():
    # Exact named equality families and disconnected variants.
    for t in range(2, 21):
        n = t + 1
        edges = [(0, v) for v in range(1, n)]
        check_graph(n, edges, lane="random", subset_cap=200, rng=random.Random(t))
        # Add isolates and a disjoint small path/cycle when local irregularity permits;
        # the all-purpose checker handles zero edges as well.
        check_graph(n + 3, edges, lane="random", subset_cap=200, rng=random.Random(1000 + t))
    for k in range(2, 15):
        # center 0, middle 1, terminal 2, direct leaves 3..k+2
        n = k + 3
        edges = [(0, 1), (1, 2)] + [(0, v) for v in range(3, n)]
        check_graph(n, edges, lane="random", subset_cap=200, rng=random.Random(2000 + k))
    # Complete multipartite and disconnected unions.
    for parts in ([1, 2], [1, 3], [2, 3], [1, 2, 4], [1, 3, 5], [2, 3, 7], [1, 2, 3, 5]):
        n, edges = complete_multipartite(parts)
        check_graph(n, edges, lane="random", subset_cap=200, rng=random.Random(sum(parts)))


def random_tests(count: int = 500):
    rng = random.Random(0x1BA1A9CE)
    for i in range(count):
        mode = i % 5
        if mode == 0:
            n = rng.randrange(7, 15)
            edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < rng.uniform(0.05, 0.95)]
        elif mode == 1:
            a = rng.randrange(2, 7); b = rng.randrange(3, 12); n = a + b
            p = rng.uniform(0.03, 0.97)
            edges = [(u, a + v) for u in range(a) for v in range(b) if rng.random() < p]
        elif mode == 2:
            # Random independent-class blowup.
            r = rng.randrange(2, 7)
            parts = [rng.randrange(1, 5) for _ in range(r)]
            n = sum(parts)
            ranges=[]; s=0
            for p0 in parts: ranges.append(range(s,s+p0)); s+=p0
            edges=[]
            for x in range(r):
                for y in range(x+1,r):
                    if rng.random()<0.5:
                        edges.extend((u,v) for u in ranges[x] for v in ranges[y])
        elif mode == 3:
            # Disjoint union of two independently random graphs.
            a = rng.randrange(2, 8); b = rng.randrange(2, 8); n = a+b
            edges=[]
            for off,size in ((0,a),(a,b)):
                p=rng.uniform(0.08,0.92)
                edges.extend((off+u,off+v) for u in range(size) for v in range(u+1,size) if rng.random()<p)
        else:
            # Random tree via Prüfer sequence.
            n = rng.randrange(3, 16)
            pr = [rng.randrange(n) for _ in range(n-2)]
            d=[1]*n
            for x in pr:d[x]+=1
            leaves={i for i,x in enumerate(d) if x==1}; edges=[]
            for x in pr:
                leaf=min(leaves); leaves.remove(leaf); edges.append((min(leaf,x),max(leaf,x)))
                d[leaf]-=1;d[x]-=1
                if d[x]==1:leaves.add(x)
            x,y=sorted(leaves);edges.append((x,y))
        check_graph(n, sorted(set(tuple(sorted(e)) for e in edges)), lane="random", subset_cap=20, rng=rng)
    print(f"RANDOM_DONE graphs={count}")


def profile_exhaustive(kmax: int = 100):
    count = 0
    min_gap = None
    witness = None
    def parts(total: int, maxpart: int, length: int, prefix=()):
        if length == 0:
            if total == 0:
                yield prefix
            return
        for x in range(min(maxpart, total), -1, -1):
            yield from parts(total-x, x, length-1, prefix+(x,))
    for k in range(3, kmax+1):
        for h in range(2,k):
            p=k-h
            for es in parts(p,p,h):
                psi=sum(2*(es[i]+1)*(es[j]+1)-(es[i]+1)-(es[j]+1)+1 for i in range(h) for j in range(i+1,h))
                C=sum(e*(k-e)**2 for e in es)
                gap=4*p*psi-C
                count+=1
                if min_gap is None or gap<min_gap:
                    min_gap=gap;witness=(k,h,es,psi,C)
                if gap<4*p or gap<=0:
                    fail("profile (19)/(B)", {"k":k,"h":h,"p":p,"es":es,"psi":psi,"C":C,"gap":gap})
                L=profile_bound(h,p)
                if ceil_div(gap,4*p)<L:
                    fail("PB", {"k":k,"h":h,"p":p,"es":es,"gap":gap,"L":L})
    print(f"PROFILE_EXHAUSTIVE_DONE kmax={kmax} profiles={count} min_gap={min_gap} witness={witness}")


def target_uniqueness(max_vertices: int = 7):
    counts = Counter()
    for n in range(1, max_vertices+1):
        pairs=all_pairs(n)
        for mask in range(1<<len(pairs)):
            edges=graph_from_mask(n,pairs,mask)
            deg,_,_=graph_data(n,edges)
            seq=tuple(sorted(deg,reverse=True))
            if seq == (n-1,)*(n):
                if len(edges)!=math.comb(n,2):
                    fail("target uniqueness complete", {"n":n,"edges":edges,"degrees":deg})
                counts[("complete",n)]+=1
            k=n-2
            if k>=2 and seq == tuple([k]*k+[k-1,1]):
                top=[v for v,d in enumerate(deg) if d==k]
                tails=[v for v,d in enumerate(deg) if d!=k]
                eset=set(edges)
                if len(top)!=k or len(tails)!=2:
                    fail("target uniqueness partition", {"n":n,"edges":edges,"degrees":deg})
                if any(tuple(sorted((u,v))) not in eset for u,v in combinations(top,2)):
                    fail("target uniqueness clique", {"n":n,"edges":edges,"degrees":deg})
                if tuple(sorted(tails)) in eset:
                    fail("target uniqueness tail edge", {"n":n,"edges":edges,"degrees":deg})
                neigh=[{u for u in top if tuple(sorted((u,t))) in eset} for t in tails]
                if neigh[0]&neigh[1] or neigh[0]|neigh[1]!=set(top) or sorted(map(len,neigh))!=[1,k-1]:
                    fail("target uniqueness neighborhoods", {"n":n,"edges":edges,"degrees":deg,"neigh":[sorted(x) for x in neigh]})
                counts[("critical",k)]+=1
    print("TARGET_UNIQUENESS_DONE", dict(counts))


def main():
    exhaustive_labeled(5)
    exhaustive_bipartite(2, 6)
    exhaustive_bipartite(3, 4)
    deterministic_structural_tests()
    random_tests(500)
    profile_exhaustive(50)
    target_uniqueness(6)
    payload={"stats":STATS.__dict__,"minima":{k:{"value":v[0]} for k,v in sorted(MINIMA.items())}}
    print("ALL_INDEPENDENT_CHECKS_PASS")
    print(json.dumps(payload,sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
