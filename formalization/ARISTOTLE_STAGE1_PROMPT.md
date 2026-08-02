# Aristotle Stage 1 prompt

Formalize the independently audited arbitrary threshold-set theorem from the attached Imbalance Conjecture packet in Lean 4.30.0 and pinned Mathlib commit `c5ea00351c28e24afc9f0f84379aa41082b1188f`.

Let `G` be an arbitrary finite simple graph. For an undirected edge `e = uv`, define

```text
edgeImbalance G e = |G.degree u - G.degree v|.
```

Assume `G` is locally irregular: every adjacent pair has unequal degree. For `S` a finite set of edges, put `k = |S|` and define the integer-valued subset Erdos-Gallai deficit

```text
D_G(S) = k(k-1)
       + sum_{f in E(G) \ S} min(k, edgeImbalance G f)
       - sum_{e in S} edgeImbalance G e.
```

Prove that if `k >= 1` and every edge in `S` has imbalance at least `k`, then `0 <= D_G(S)`.

The kernel proof must include named declarations for:

1. the exact deficit identity;
2. the head-reserve inequality;
3. the local weighted cross-payment bound;
4. the global multiple-use cross-payment bound;
5. multiplicity domination;
6. the `p = 0`, `h = 1`, and `k = 1` boundary profiles.

Requirements:

- Use Mathlib's finite `SimpleGraph` framework in the exported theorem.
- Distinguish degrees in `G` from residual incidences after deleting selected heads.
- Eliminate all division by cross-multiplication and prove sign conditions.
- Prove the unit-imbalance parity bipartition and its quadratic edge bound; do not assume it as an axiom.
- Do not use finite enumeration as proof.
- No `sorry`, `admit`, `unsafe`, custom `axiom`, or unproved custom `opaque` declaration.
- Do not formalize equality classification or the one-equal-edge extension in Stage 1.
- Do not claim the full Imbalance Conjecture unless a kernel-checked Erdos-Gallai sufficiency or equivalent Havel-Hakimi realization theorem is also supplied.

Return one ZIP containing all Lean/Lake source, `lean-toolchain`, `lakefile.lean`, `lake-manifest.json`, README, exact theorem-scope report, clean build log, no-holes scan, `#print axioms` output, manifest, and SHA-256 ledger.

Run and record:

```bash
lake build
lake env lean <axiom-audit-file>
```

A clean Stage 1 threshold theorem is a successful partial formalization. It is not a formal proof of the full conjecture.

