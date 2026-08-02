# Build and validation instructions

## Build status

> The environment record below documents the historical Version 2.1 build.
> The current priority-corrected build is recorded separately in
> `BUILD_LOG_v1.1.0.txt` and `PDF_PREFLIGHT_v1.1.0.txt`.

The Version 2.1 PDF was built without internet access from a fresh temporary directory. The same TeX/BibTeX toolchain used for Version 2 was retained. The
Version 1.1 PDF was subsequently rebuilt by GitHub Actions using TeX Live 2026,
latexmk 4.88, and pdfTeX 1.40.29.

## Actual environment used

```text
Operating system: Linux 6.12.13 x86_64
C library: glibc 2.41
Python: CPython 3.13.5
Python compiler: GCC 14.2.0
NetworkX: 3.6.1 installed; not invoked in the Version 2.1 source repair or build
latexmk: 4.86 (John Collins, 11 Dec. 2024)
pdfTeX: 3.141592653-2.6-1.40.26
TeX distribution: TeX Live 2025/dev/Debian
LaTeX2e: 2024-11-01 patch level 2
BibTeX engine: bibtex8 0.99d-x4.02, release 4.02 (16 Dec. 2023)
g++: 14.2.0 (not invoked for the Version 2.1 repair)
Poppler pdfinfo/pdftotext/pdffonts/pdftoppm: 25.06.0
```

## TeX class and direct package versions loaded

```text
amsart.cls: 2020/05/29 v2.20.6
amsmath: 2024/11/05 v2.17t
amssymb: 2013/01/14 v3.01
mathtools: 2024/10/04 v1.31
microtype: 2025/02/11 v3.2a
enumitem: 2025/02/06 v3.11
booktabs: 2020/01/12 v1.61803398
hyperref: 2024-11-05 v7.01l
geometry: 2020/01/02 v5.9
```

These declarations were read from the actual Version 2.1 `manuscript.log`. No unknown direct package version was filled by inference.

## Required build files

```text
manuscript.tex
references.bib
latexmkrc
```

`latexmkrc` selects PDF mode and `bibtex8`:

```perl
$pdf_mode = 1;
$bibtex = 'bibtex8 %O %B';
$pdf_previewer = 'none';
```

## Clean build procedure

```bash
set -euo pipefail
BUILD_DIR="$(mktemp -d)"
cp manuscript.tex references.bib latexmkrc "$BUILD_DIR/"
cd "$BUILD_DIR"
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

The first invocation runs pdfTeX and `bibtex8` as required. The second invocation must report that all targets are up to date.

## Validation procedure

```bash
pdfinfo manuscript.pdf
pdffonts manuscript.pdf
pdftotext -layout manuscript.pdf manuscript.txt
pdftoppm -png -r 180 manuscript.pdf rendered-page
```

The final log is scanned for undefined citations/references, multiply defined labels, LaTeX/BibTeX warnings, and overfull/underfull boxes. The rendered pages are inspected individually. The source is compared structurally against Version 2 as recorded in `MATHEMATICAL_PRESERVATION.json`.
