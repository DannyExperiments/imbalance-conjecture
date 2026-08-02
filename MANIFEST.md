# Manifest

This directory is the sanitized public research surface. The separate private evidence warehouse remains the authoritative archive for raw model returns, task receipts, nested ZIPs, and immutable audit packets.

## Public files

- `README.md`, `STATUS.md`: exact theorem and release status.
- `AI_DISCLOSURE.md`, `PROVENANCE.md`: authorship, AI contribution, evidence chronology, and nonclaims.
- `REPRODUCIBILITY.md`, `scripts/verify.sh`, `.github/workflows/`: offline
  verification instructions plus GitHub-hosted repository and PDF replay.
- `proof/ORIGINAL_PROBLEM.md`: exact problem statement and original-source context.
- `proof/PROBLEM_AND_PROOF.md`: complete corrected ordinary proof return.
- `proof/EXTENSIONS_AND_STRENGTHENINGS.md`, `proof/EXTENSIONS_ERRATA.md`: audited strengthened scope and correction sheet.
- `audits/`: curated mathematical, literature, and claims-evidence adjudications.
- `verification/`: independent dependency-free Python and exhaustive C++ corroboration with frozen logs.
- `auxiliary/`: the four non-load-bearing programs and captured outputs
  referenced by the manuscript, including the two independent lanes mirrored
  under `verification/`.
- `formalization/`: current nonformalization boundary and staged Aristotle prompt.
- `paper/`: canonical post-literature Version 2.1 manuscript, checked-in
  `latexmkrc`, and public-safe
  build, preflight, Version 2-to-2.1 preservation, text-scan, render-diff,
  changelog, and exact-comparison records.
- `release/`: release notes and final release hashes once frozen.
- `CITATION.cff`: release citation metadata naming DannyExperiments as the
  conventional author.

## Excluded private material

The public candidate excludes raw ChatGPT task URLs, sandbox links, absolute
local paths, nested private ZIPs, mutable campaign ledgers, and third-party
PDFs. Their hashes and conclusions are preserved in `PROVENANCE.md` and in the
private evidence warehouse. The completed Version 2.1 final-manuscript audit is
recorded in `audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md`.
