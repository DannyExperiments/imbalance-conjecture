# Final manuscript audit status - Version 1.1.0

The priority-corrected manuscript was rebuilt by GitHub Actions, extracted from
the resulting workflow artifact, independently preflighted, rendered, inspected
page by page, and installed as `paper/manuscript.pdf`.

Controlling adjudication:

```text
PRIORITY_CORRECTION_INTEGRATED: PASS
RAOUI_EARLIER_PROOF_CITED: PASS
SCHREIB_EARLIER_FORMALIZATION_CITED: PASS
FIRST_SOLUTION_CLAIM_REMOVED: PASS
HEADLINE_AND_THRESHOLD_NOVELTY_CLAIMS_REMOVED: PASS
ADDITIONAL_RESULT_PRIORITY: UNRESOLVED_FOCUSED_SEARCH_REQUIRED
MATHEMATICAL_PROOF_SCOPE_PRESERVED: PASS
REFERENCES_AND_STATIC_CROSS_REFERENCES: PASS
GITHUB_ACTIONS_BUILD: PASS
ALL_PAGE_VISUAL_INSPECTION: PASS
PUBLIC_SAFE_INSTALLATION: PASS
HUMAN_SPECIALIST_REVIEW: NOT_OBTAINED_NOT_CLAIMED
PRESENT_ARGUMENT_FORMAL_VERIFICATION: NOT_OBTAINED_NOT_CLAIMED
FINAL_VERSION_1_1_MANUSCRIPT_AUDIT: PASS
```

## Exact artifact

- GitHub Actions workflow run: `30757660187`
- Job: `91522528192`
- Artifact ID: `8836452818`
- Artifact ZIP SHA-256: `3fcbad2e1f0db411fcc0f89bdcc2808328d7d924e0f591ed33ce34f15fd38afe`
- PDF SHA-256: `a1d689de2edc61dbbb946e597f1820a972a2ea71371b2ca1be456647a6b48473`
- PDF size: 354,654 bytes
- PDF pages: 15 A4 pages

The final TeX pass had no unresolved citations or references, multiply defined
labels, LaTeX or BibTeX warnings, or overfull or underfull boxes. All 15 pages
were rendered at 150 dpi and inspected. No clipping, overlap, malformed
equation, broken glyph, displaced label, or unreadable reference was found.

## Corrected mathematical and historical scope

The manuscript contains a complete independent proof of the finite-simple
locally-irregular imbalance theorem. It does not claim to be the first proof or
to solve a problem that remained open at the manuscript date. It identifies:

1. A. A. Raoui's earlier complete proof, deposited on 8 June 2026, DOI
   `10.5281/zenodo.20589431`; and
2. James Alexander Schreib's earlier full Lean 4 formalization, deposited on
   25 July 2026, DOI `10.5281/zenodo.21542164`.

The direct threshold-set inequality is retained as the proof engine, without a
claim that its bare nonnegativity is stronger than graphicality or priority
bearing. The profile-sensitive quantitative bounds, equality classification,
and one-equal-edge extension were not found in the two exact prior records.
Their broader novelty remains unresolved pending a refreshed focused search;
absolute priority is not claimed.

## Review and formalization boundary

The mathematical argument and its extensions previously passed an independent
AI adversarial audit. That is not human peer review. No human graph-theory
specialist report has been obtained. Schreib's external Lean development
formalizes the headline theorem but does not kernel-check this manuscript's
different proof architecture, quantitative bounds, equality classification, or
one-equal-edge extension.

This file is the controlling manuscript audit for Version 1.1.0. The unsuffixed
`FINAL_MANUSCRIPT_AUDIT_STATUS.md` and the old build/preflight records are
retained as explicitly superseded Version 2.1 provenance only.
