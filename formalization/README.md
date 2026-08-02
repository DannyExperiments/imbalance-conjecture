# Formalization status

No completed Lean, Isabelle, Coq, or Aristotle certificate is banked for the Imbalance Conjecture.

An Aristotle Stage 1 attempt on 2 August 2026 ended at the platform time limit.
It returned no completed certificate, so no theorem from that run is counted as
formalized. See [`ARISTOTLE_STAGE1_STATUS.md`](ARISTOTLE_STAGE1_STATUS.md).

The right first target is the arbitrary threshold-set theorem, not the equality or one-zero extensions. The main new obstacle beyond that theorem is that the pinned Mathlib 4.30.0 source inspected for this campaign does not contain an Erdos-Gallai or Havel-Hakimi realization theorem. A full kernel-checked solution therefore requires both the new threshold proof and a formal graphical-sequence realization theorem.

`ARISTOTLE_STAGE1_PROMPT.md` requests only the threshold theorem and prohibits labeling a partial result as a formal proof of the full conjecture.

Formalization is optional corroboration and does not block public timestamping.
