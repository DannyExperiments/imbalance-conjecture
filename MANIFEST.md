# Manifest

This directory is the sanitized public research surface. The separate private evidence warehouse remains the authoritative archive for raw model returns, task receipts, nested ZIPs, and immutable audit packets.

## Public files

- `README.md`, `STATUS.md`: exact theorem and release status.
- `AI_DISCLOSURE.md`, `PROVENANCE.md`: authorship, AI contribution, evidence chronology, and nonclaims.
- `REPRODUCIBILITY.md`, `scripts/verify.sh`, `.github/workflows/`: offline
  verification instructions plus GitHub-hosted repository and PDF replay.
- `proof/ORIGINAL_PROBLEM.md`: exact problem statement and original-source context.
- `proof/PROBLEM_AND_PROOF.md`: complete corrected ordinary proof return.
- `proof/EXTENSIONS_AND_STRENGTHENINGS.md`, `proof/EXTENSIONS_ERRATA.md`: audited quantitative and extension scope and correction sheet.
- `audits/`: curated mathematical, literature, and claims-evidence adjudications.
- `verification/`: independent dependency-free Python and exhaustive C++ corroboration with frozen logs.
- `auxiliary/`: the four non-load-bearing programs and captured outputs
  referenced by the manuscript, including the two independent lanes mirrored
  under `verification/`.
- `formalization/`: external Schreib-formalization notice and the historical
  local Aristotle attempt.
- `audits/PRIORITY_CORRECTION_2026-08-02.md`: controlling priority correction.
- `release/V1.0.0_SUPERSESSION_NOTICE.md`: reason the original release must not
  receive the paper DOI.
- `paper/`: priority-corrected manuscript source and PDF, checked-in `latexmkrc`,
  and clearly marked historical Version 2/2.1 build, preflight, preservation,
  text-scan, render-diff, changelog, and exact-comparison records.
- `release/`: release notes and final release hashes once frozen.
- `CITATION.cff`: release citation metadata naming DannyExperiments as the
  conventional author.

## Excluded private material

The public repository excludes raw ChatGPT task URLs, sandbox links, absolute
local paths, nested private ZIPs, mutable campaign ledgers, and third-party
PDFs. Their hashes and conclusions are preserved in `PROVENANCE.md` and in the
private evidence warehouse. The Version 2.1 final-manuscript audit is recorded
in `audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md` as historical evidence, not current
release approval.
