#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

required=(
  README.md STATUS.md AI_DISCLOSURE.md PROVENANCE.md MANIFEST.md CITATION.cff
  RELEASE_CHECKLIST.md LICENSE_STATUS.md REPRODUCIBILITY.md
  proof/ORIGINAL_PROBLEM.md
  proof/PROBLEM_AND_PROOF.md
  proof/EXTENSIONS_AND_STRENGTHENINGS.md
  proof/EXTENSIONS_ERRATA.md
  audits/MATHEMATICAL_AUDIT.md
  audits/LITERATURE_PRIORITY_AUDIT.md
  audits/PRIORITY_CORRECTION_2026-08-02.md
  audits/EXTENSION_PRIORITY_SEARCH_2026-08-03.md
  audits/CLAIMS_EVIDENCE_MATRIX.md
  audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md
  audits/FINAL_MANUSCRIPT_AUDIT_STATUS_v1.1.0.md
  auxiliary/README.md
  auxiliary/imbalance_breakthrough_verifier.py
  auxiliary/imbalance_breakthrough_verifier.log
  auxiliary/imbalance_extensions_verifier.py
  auxiliary/imbalance_extensions_verifier.log
  auxiliary/imbalance_independent_referee_checker.py
  auxiliary/imbalance_independent_referee_checker.log
  auxiliary/imbalance_exhaustive_n7.cpp
  auxiliary/imbalance_exhaustive_n7.log
  verification/imbalance_independent_referee_checker.py
  verification/INDEPENDENT_CHECKER_LOG.txt
  verification/imbalance_exhaustive_n7.cpp
  verification/EXHAUSTIVE_N7_LOG.txt
  formalization/README.md
  formalization/ARISTOTLE_STAGE1_STATUS.md
  release/V1.0.0_SUPERSESSION_NOTICE.md
  release/RELEASE_NOTES_v1.1.0.md
  paper/BUILD_LOG_v1.1.0.txt
  paper/PDF_PREFLIGHT_v1.1.0.txt
)

for path in "${required[@]}"; do
  [[ -f "$path" ]] || fail "missing required file: $path"
done

cmp -s auxiliary/imbalance_independent_referee_checker.py \
  verification/imbalance_independent_referee_checker.py \
  || fail "independent Python source differs between auxiliary and verification copies"
cmp -s auxiliary/imbalance_independent_referee_checker.log \
  verification/INDEPENDENT_CHECKER_LOG.txt \
  || fail "independent Python output differs between auxiliary and verification copies"
cmp -s auxiliary/imbalance_exhaustive_n7.cpp \
  verification/imbalance_exhaustive_n7.cpp \
  || fail "independent C++ source differs between auxiliary and verification copies"
cmp -s auxiliary/imbalance_exhaustive_n7.log \
  verification/EXHAUSTIVE_N7_LOG.txt \
  || fail "independent C++ output differs between auxiliary and verification copies"

for forbidden in sources notes paper/candidates paper/drafts handoffs; do
  [[ ! -e "$forbidden" ]] || fail "private-only path present: $forbidden"
done

if rg -n 'sandbox:/|/mnt/data|/Users/|chatgpt\.com/g/' \
  --glob '!SHA256SUMS.txt' \
  --glob '!scripts/verify.sh' .; then
  fail "private or ephemeral path found"
fi

rg -q 'INDEPENDENT_PROOF_AI_AUDIT_PASS_PRIOR_PROOF_IDENTIFIED_PRIORITY_CORRECTED_V1_1_CANDIDATE' STATUS.md \
  || fail "status marker missing"
rg -qi 'independent proof' README.md || fail "independent-proof framing missing"
rg -q '10\.5281/zenodo\.20589431' README.md audits/PRIORITY_CORRECTION_2026-08-02.md \
  || fail "Raoui priority record missing"
rg -q '10\.5281/zenodo\.21542164' README.md formalization/README.md \
  || fail "Schreib formalization record missing"
rg -qi 'Human specialist review.*(has|have) not been obtained' README.md \
  || fail "human-review nonclaim missing"
rg -q 'This repository contains no completed Lean, Isabelle, Coq, or Aristotle' formalization/README.md \
  || fail "repository-scoped formalization boundary missing"
rg -q 'ended at the platform time limit' formalization/ARISTOTLE_STAGE1_STATUS.md \
  || fail "timed-out Aristotle status missing"
rg -q 'FINAL_VERSION_1_1_MANUSCRIPT_AUDIT: PASS' \
  audits/FINAL_MANUSCRIPT_AUDIT_STATUS_v1.1.0.md \
  || fail "current Version 1.1 manuscript audit missing"
rg -q 'a1d689de2edc61dbbb946e597f1820a972a2ea71371b2ca1be456647a6b48473' \
  paper/BUILD_LOG_v1.1.0.txt paper/PDF_PREFLIGHT_v1.1.0.txt \
  audits/FINAL_MANUSCRIPT_AUDIT_STATUS_v1.1.0.md \
  || fail "current Version 1.1 PDF hash record missing"
actual_pdf_hash="$(shasum -a 256 paper/manuscript.pdf | awk '{print $1}')"
[[ "$actual_pdf_hash" == "a1d689de2edc61dbbb946e597f1820a972a2ea71371b2ca1be456647a6b48473" ]] \
  || fail "paper/manuscript.pdf is not the audited Version 1.1 artifact"

if [[ -f paper/manuscript.tex ]]; then
  rg -n '\\author\s*\{' paper/manuscript.tex && fail "manuscript must not contain an author command"
  rg -Fq '\cite{Raoui2026}' paper/manuscript.tex \
    || fail "Raoui citation missing from manuscript"
  rg -Fq '\cite{Schreib2026}' paper/manuscript.tex \
    || fail "Schreib citation missing from manuscript"
  rg -q 'doi[[:space:]]*=.*10\.5281/zenodo\.20589431' paper/references.bib \
    || fail "Raoui DOI missing from bibliography"
  rg -q 'doi[[:space:]]*=.*10\.5281/zenodo\.21542164' paper/references.bib \
    || fail "Schreib DOI missing from bibliography"
  if rg -n -i 'no retrievable earlier complete solution|threshold-set strengthening|main and strengthened results are therefore apparently new' \
      paper/manuscript.tex; then
    fail "superseded priority language remains in active manuscript"
  fi
  rg -q 'pp\.~81--100' paper/manuscript.tex \
    || fail "authoritative 2023 page range missing from manuscript"
  rg -q 'title[[:space:]]*=.*Graphs with graphic imbalance sequences' paper/references.bib \
    || fail "exact MathOverflow title missing from bibliography"
  rg -q 'pages[[:space:]]*=.*81--100' paper/references.bib \
    || fail "authoritative 2023 bibliography page range missing"
  ! rg -q 'pp\.~81--96|Residual source gaps comprise' paper/manuscript.tex \
    || fail "superseded Version 2 source wording remains"
fi

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

python3 verification/imbalance_independent_referee_checker.py > "$tmp_dir/python.log"
cmp -s "$tmp_dir/python.log" verification/INDEPENDENT_CHECKER_LOG.txt \
  || fail "independent Python output differs from frozen log"

c++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  verification/imbalance_exhaustive_n7.cpp \
  -o "$tmp_dir/imbalance_exhaustive_n7" 2> "$tmp_dir/cxx.log"
[[ ! -s "$tmp_dir/cxx.log" ]] || fail "C++ compilation produced diagnostics"
"$tmp_dir/imbalance_exhaustive_n7" > "$tmp_dir/n7.log"
cmp -s "$tmp_dir/n7.log" verification/EXHAUSTIVE_N7_LOG.txt \
  || fail "exhaustive C++ output differs from frozen log"

if [[ -f SHA256SUMS.txt ]]; then
  shasum -a 256 -c SHA256SUMS.txt
fi

if [[ "${REQUIRE_RELEASE_PAPER:-0}" == "1" ]]; then
  [[ -f paper/manuscript.tex ]] || fail "release manuscript TeX missing"
  [[ -f paper/manuscript.pdf ]] || fail "release manuscript PDF missing"
  [[ -f paper/references.bib ]] || fail "release bibliography missing"
  [[ -f paper/latexmkrc ]] || fail "release latexmk configuration missing"
  [[ -f paper/BUILD_LOG.txt ]] || fail "release build log missing"
  [[ -f paper/PDF_PREFLIGHT.txt ]] || fail "release PDF preflight missing"
  [[ -f paper/V2_CHANGELOG.md ]] || fail "release manuscript changelog missing"
  [[ -f paper/V2_TO_V2_1_CHANGELOG.md ]] || fail "Version 2-to-2.1 changelog missing"
  [[ -f paper/PRIORITY_CORRECTION_CHANGELOG.md ]] || fail "priority-correction changelog missing"
  [[ -f paper/BUILD_LOG_v1.1.0.txt ]] || fail "Version 1.1 build log missing"
  [[ -f paper/PDF_PREFLIGHT_v1.1.0.txt ]] || fail "Version 1.1 PDF preflight missing"
  [[ -f audits/FINAL_MANUSCRIPT_AUDIT_STATUS_v1.1.0.md ]] \
    || fail "Version 1.1 final manuscript audit missing"
  [[ -f paper/SOURCE_TO_MANUSCRIPT_COMPARISON.md ]] || fail "release source comparison missing"
  [[ -f paper/MATHEMATICAL_PRESERVATION_V2_TO_V2_1.json ]] \
    || fail "Version 2-to-2.1 mathematical preservation record missing"
  [[ -f paper/PDF_RENDER_DIFF_SUMMARY_V2_TO_V2_1.json ]] \
    || fail "Version 2-to-2.1 render comparison missing"
  [[ -f paper/PDF_TEXT_REFERENCE_SCAN_V2_1.txt ]] \
    || fail "Version 2.1 PDF text/reference scan missing"
  rg -q 'Superseded for current release approval' audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md \
    || fail "historical manuscript audit is not marked superseded"
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git diff --check
fi

echo "Public repository integrity and disclosure checks passed."
