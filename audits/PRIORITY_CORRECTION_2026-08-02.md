# Priority correction — 2 August 2026

## Corrected conclusion

The headline theorem in this repository was proved earlier by A. A. Raoui in
*The Imbalance Conjecture*, deposited on 8 June 2026:

- version DOI: <https://doi.org/10.5281/zenodo.20589431>;
- concept DOI: <https://doi.org/10.5281/zenodo.20589430>;
- inspected PDF SHA-256:
  `0ee974129acffe65e4ea82778b6dbbeb4bd0e7abead8f16bc8819862fd42a594`.

The five-page preprint states and proves the same theorem: the edge-imbalance
multiset of every finite simple locally irregular graph is graphical. Two
independent AI audit lanes read the complete paper and found its proof valid
with high confidence.

James Alexander Schreib later released *Lean 4 Formalization of the Imbalance
Conjecture* on 25 July 2026:

- version DOI: <https://doi.org/10.5281/zenodo.21542164>;
- concept DOI: <https://doi.org/10.5281/zenodo.21542163>;
- inspected source-archive SHA-256:
  `9d768f7a700f7923ef419e9ae17dce59a5e450c0a0a9a6091368b5ed74b17486`.

The inspected Lean source contains no `sorry`, `admit`, project axiom, or
`unsafe` declaration. It formalizes the headline theorem and the relevant
Erdős--Gallai inequality for every edge subset. The archive was inspected but
was not rebuilt in this repository.

## Consequences for this project

1. This repository contains a later independent proof, not the first solution.
2. The threshold-set nonnegativity theorem is a proof engine here, not a
   stronger or priority-bearing conclusion. Graphicality already implies the
   corresponding inequality for every subset, and Schreib formalizes that
   all-subset statement.
3. The proof architecture here is materially different from Raoui's:
   first-failed-index reduction, an exact deficit identity, a head reserve,
   weighted residual collision bounds, and multiplicity-profile algebra.
4. The quantitative profile slack, complete threshold-equality classification,
   and one-equal-edge extension were not found in the two records above.
   Broader novelty is not certified and requires a refreshed focused search.
5. The external Lean work verifies the original conjecture, not this
   repository's alternative proof, equality classification, or one-equal-edge
   extension.

## Version handling

The public `v1.0.0` tag and assets are preserved as historical evidence. They
predate this correction and contain an incorrect literature conclusion, so they
must not receive the paper DOI or be used for a priority claim. The corrected
paper and metadata are being prepared as `v1.1.0`.

## Process correction

Future open-problem campaigns must search exact titles, theorem statements,
authors, Zenodo/DataCite, arXiv, formalization repositories, and DOI registries
before discovery work is classified as a new solve. The search must be repeated
immediately before public release and DOI deposit.

This correction changes priority and presentation, not the validity of the
independently audited mathematical argument in this repository.
