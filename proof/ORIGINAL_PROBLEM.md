# Imbalance Conjecture — historical campaign input

> The open-status assumption used when this input was frozen was stale. Raoui's
> earlier proof, DOI `10.5281/zenodo.20589431`, was located on 2 August 2026.
> This file is preserved as the exact problem attacked, not as a current claim
> that the conjecture was open.

Run ID: `imbalance-director-20260801-132101-ultra`  
Problem ID: `OPG-57613`  
Freeze date: 2026-08-01

Let `G` be a finite simple graph. For an edge `e=uv`, define

`imb_G(e) = |deg_G(u)-deg_G(v)|`.

Assume every edge has positive imbalance; equivalently, adjacent vertices of
`G` never have equal degree. Let

`M(G) = { imb_G(e) : e in E(G) }`

be the multiset of the `m=|E(G)|` edge imbalances.

## Conjecture

`M(G)` is graphic: there is a finite simple graph on `m` vertices whose degree
multiset is exactly `M(G)`.

Equivalently, if the imbalances are sorted as

`x_1 >= x_2 >= ... >= x_m > 0`,

then they satisfy all Erdős–Gallai inequalities

`sum_{i<=k} x_i <= k(k-1) + sum_{i>k} min(k,x_i)`

for `1 <= k <= m`, together with even total sum.

## Solve gate

A full solve is exactly one of:

1. an independent complete proof for every finite simple graph under the displayed
   hypothesis, with every Erdős–Gallai or realization step justified; or
2. one explicit finite simple graph `G` satisfying the hypothesis for which
   the exact imbalance sequence fails a named Erdős–Gallai inequality, with a
   replayable certificate.

Finite testing, random testing, a sufficient subclass, or an auxiliary
construction whose feasibility is unproved is not a solve.

## Known source-reported frontier

Kozerenko and Serdiuk (2023), Conjecture 5.5, report exhaustive verification
for graphs on at most 12 vertices. Their Proposition 5.4 refutes a different,
second imbalance conjecture; it does not refute the conjecture frozen here.
