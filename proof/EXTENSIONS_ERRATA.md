# Errata and clarifications for `IMBALANCE_EXTENSIONS_2026-08-01.md`

This errata sheet records the local repairs identified by the independent no-internet adversarial referee. None changes a theorem statement, a numerical bound, or the substantive argument.

## E1. Empty source graph

Before introducing a positive imbalance list in the proof of the main Imbalance Conjecture, dispose of the empty graph:

> If `E(G)=∅`, the imbalance sequence is empty and hence graphical. Assume thereafter that `m=|E(G)|≥1`.

The reconciled manuscript includes this boundary case at the start of the proof of the main theorem.

## E2. Active sets in the zero-edge correction argument

In the zero-edge correction proof, the active set must be defined for **every** selected head `u∈U`, not only for a repeated head:

```text
A_u = {z∈V(H): uz∈E(G), q_{u,z}>0}.
```

When `e_u=s_u-1=0`, a positive edge cannot be active, but a zero `U-H` edge can be active and must be included. The reconciled manuscript states this explicitly before defining `t_u` and `ζ_u`.

## E3. The `r=0` boundary in the one-equal-edge theorem

If the graph has exactly one zero-imbalance edge and no positive imbalances, then it has exactly one edge; its only non-isolated component is `K_2`, and its full imbalance sequence is `(0)`, which is graphical. Only after this case is removed may one assume `r≥1` and introduce `y_1`.

The reconciled manuscript includes this case before the positive sequence is defined.

## E4. Explicit `h=2`, `2h<3p` quantitative line

In the proof of the sharpening `4pΨ-C≥4p`, explicitly record that for `h=2` and `2h<3p`, one has `p≥2`, and the second profile lower bound gives

```text
4pΨ-C ≥ 4p^2 ≥ 4p.
```

The reconciled manuscript now displays this inequality.

## E5. Incidence-matrix terminology

The incidence matrix in the reformulation is the **signed oriented vertex-edge incidence matrix**. The reconciled manuscript already uses this terminology.

## E6. Empty active set in the single-head boundary

The single-head estimate also covers `A_u=∅`; no nonempty active-set assumption is used. The reconciled manuscript now says this explicitly.

## Status

The independent referee found no false mathematical inference after these local repairs and determined that the following claims survive:

- the arbitrary threshold-set theorem;
- the Imbalance Conjecture;
- the quantitative slack theorem;
- the complete equality classification;
- the zero-edge correction lemma;
- the one-equal-edge extension.

Historical priority and publication status remain outside the scope of that no-internet audit and are still pending the separate literature review.
