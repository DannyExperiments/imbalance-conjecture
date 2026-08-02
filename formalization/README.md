# Formalization status

This repository contains no completed Lean, Isabelle, Coq, or Aristotle
certificate for its alternative proof, quantitative equality results, or
one-equal-edge extension.

The original Imbalance Conjecture does have an external Lean 4 formalization by
James Alexander Schreib, published on 25 July 2026:
<https://doi.org/10.5281/zenodo.21542164>. The archived source also proves the
relevant Erdős--Gallai inequality for every edge subset. It predates this
repository's formalization attempt and was inspected here, but not freshly
rebuilt.

An Aristotle Stage 1 attempt on 2 August 2026 ended at the platform time limit.
It returned no completed certificate, so no theorem from that run is counted as
formalized. See [`ARISTOTLE_STAGE1_STATUS.md`](ARISTOTLE_STAGE1_STATUS.md).

Any future formalization effort for this repository should target the distinct
quantitative slack, equality classification, or one-equal-edge extension, or
formalize this alternative proof specifically. Reformalizing the bare headline
theorem is no longer a useful priority target.

`ARISTOTLE_STAGE1_PROMPT.md` is preserved as a historical prompt. It predates
the discovery of Schreib's formalization and should not be relaunched unchanged.

Formalization is optional corroboration and does not block public timestamping.
