# Release checklist

## Complete

- [x] Corrected complete ordinary proof preserved.
- [x] Independent adversarial mathematical audit passed.
- [x] All six audit clarifications incorporated in the frozen candidate.
- [x] Dependency-free Python checker replayed successfully.
- [x] Exhaustive C++20 checker replayed successfully over all labeled seven-vertex graphs.
- [x] Current-open-status and novelty literature audit completed through August 1, 2026.
- [x] Public/private repository separation established.
- [x] Authorship and AI-contribution convention fixed.

## Required before public push

- [x] Produce post-literature Version 2 TeX, bibliography, and PDF without
      changing the audited mathematics.
- [x] Include the producer's exact Version 2 comparison against the frozen
      proof, errata, and adversarial audit.
- [x] Reconcile the documented historical and novelty statements with the
      literature report in Version 2.
- [x] Preserve the clean-build, citation/reference, warning, and metadata
      records supplied with Version 2.
- [x] Preserve the all-page visual-inspection and PDF preflight records.
- [x] Install the public-safe Version 2 manuscript files under `paper/`.
- [x] Freeze an independent final-manuscript audit of the installed Version 2.
- [x] Produce and re-audit Version 2.1 with the omitted unresolved 2014-citation
      gap disclosed; update its changelog/comparison record and rebuild TeX/PDF.
- [x] The owner reclassified pre-release contact with Kozerenko and Serdiuk as
      optional post-timestamp outreach; no outreach or endorsement is claimed.
- [x] Regenerate and verify `SHA256SUMS.txt` after every release-tree change.
- [x] Run `REQUIRE_RELEASE_PAPER=1 bash scripts/verify.sh` on the exact final
      tree.
- [ ] Make one coherent release commit and annotated tag.

## Explicit nonclaims

- [x] Human specialist review was not obtained.
- [x] Absolute historical priority is not claimed.
- [x] No proof-assistant verification is claimed.
- [x] Public visibility will not be described as peer review or publication acceptance.

Formalization is valuable but is not a prerequisite for public timestamping.
