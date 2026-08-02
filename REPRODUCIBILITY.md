# Reproducibility

The same public gate is replayed on GitHub Actions, and a separate PDF
workflow rebuilds the manuscript from its TeX, bibliography, and checked-in
`latexmkrc`. Workflow logs are linked by the status badges at the top of the
repository README.

## One-command check

```bash
bash scripts/verify.sh
```

The script:

1. verifies the public checksum ledger when present;
2. rejects private-only directories, absolute local paths, sandbox links, and ChatGPT project URLs;
3. checks the exact status and authorship/nonclaim language;
4. checks that no manuscript author command is present;
5. runs the dependency-free Python checker and compares its terminal success marker;
6. compiles the C++20 checker with warnings enabled, runs it, and compares its exact output;
7. checks the installed canonical manuscript files; and
8. runs `git diff --check` when executed inside a Git checkout.

No dependency installation or network access occurs.

## Independent checker scopes

The Python checker covers exhaustive labeled graphs through five vertices, two bipartite universes, random graphs, threshold subsets, equality cases, zero-correction regimes, target uniqueness, and 1,295,871 head profiles through `k = 50`.

The C++20 checker exhausts all `2^21 = 2,097,152` labeled graphs on seven vertices. Its recorded output includes 3,162,929 qualifying threshold sets and no failed assertion.

These runs are corroborating evidence. The written proof is load-bearing.

The manuscript's broader four-program record is preserved under `auxiliary/`.
The two NetworkX lanes there are archival and are not executed by the release
gate; no dependency installation is performed. The dependency-free Python and
C++20 files mirrored under `verification/` are the independently replayed
lanes used by `scripts/verify.sh`.

## Manuscript build

The post-literature Version 2.1 manuscript is installed with its clean build
log, exact tool versions, PDF preflight, Version 2-to-2.1 mathematical
preservation record, render comparison, changelog, and source-comparison record.
Run the release gate with `REQUIRE_RELEASE_PAPER=1`; it rejects an incomplete
canonical manuscript set. The independent final-manuscript audit is separate
from file integrity and passes for the installed Version 2.1 files.
