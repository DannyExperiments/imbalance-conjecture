# Quantitative Erdős–Gallai Deficits for Edge-Imbalance Multisets

[![Repository verification](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/verify.yml)
[![PDF build](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/pdf.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/pdf.yml)

[Paper (PDF)](paper/manuscript.pdf) ·
[Independent proof](proof/PROBLEM_AND_PROOF.md) ·
[Priority correction](audits/PRIORITY_CORRECTION_2026-08-02.md) ·
[Mathematical audit](audits/MATHEMATICAL_AUDIT.md) ·
[Independent checkers](verification/README.md) ·
[Reproduce](REPRODUCIBILITY.md)

This repository gives a later independent proof of the Imbalance Conjecture and
develops quantitative deficit bounds, a complete threshold-equality
classification, and an extension allowing one equal-degree edge.

> **Priority correction (2 August 2026).** A. A. Raoui's preprint
> [“The Imbalance Conjecture”](https://doi.org/10.5281/zenodo.20589431),
> deposited on 8 June 2026, contains an earlier proof of exactly the same
> finite-simple locally-irregular theorem. James Alexander Schreib subsequently
> released a [Lean 4 formalization](https://doi.org/10.5281/zenodo.21542164)
> on 25 July 2026, including the relevant Erdős--Gallai inequality for every
> edge subset. Accordingly, this repository claims neither a first solution nor
> priority for its threshold-set statement. Its proof architecture is different.
> The quantitative slack, equality classification, and one-equal-edge extension
> were not found in those two records; broader novelty has not been established
> and requires a refreshed focused search. See the
> [full correction record](audits/PRIORITY_CORRECTION_2026-08-02.md).

## The historical problem

For an edge `uv` of a finite simple graph `G`, define

\[
\operatorname{imb}_G(uv)=\lvert d_G(u)-d_G(v)\rvert.
\]

If adjacent vertices of `G` always have unequal degrees, must the multiset of edge imbalances be the degree multiset of a finite simple graph?

Sergiy Kozerenko posed the question in
[MathOverflow question 140819](https://mathoverflow.net/questions/140819/graphs-with-graphic-imbalance-sequences)
on August 30, 2013. Kozerenko and Volodymyr Skochko published the conjecture
in 2014. Kozerenko and Andrii Serdiuk restated it as Conjecture 5.5 in work
published online on December 30, 2022 and assigned bibliographic year 2023.

## Results in this repository

Raoui had already established that the answer is affirmative. The theorem below
is reproved here by an independent argument.

> **Imbalance theorem (formerly the Imbalance Conjecture).** Let `G` be a finite simple graph. If `d_G(u) != d_G(v)` for every edge `uv`, then
>
> \[
> \{\lvert d_G(u)-d_G(v)\rvert:uv\in E(G)\}
> \]
>
> with multiplicity is the degree multiset of a finite simple graph.

As its proof engine, the argument first establishes a threshold-set lemma: if
`S` is any `k`-edge subset and every edge in `S` has imbalance at least `k`,
then `S` satisfies its subset Erdős--Gallai inequality. This is not claimed as
a stronger consequence than graphicality, since every graphical sequence
satisfies the corresponding inequality for every subset. Its role is that the
lemma is proved directly and then rules out a first failed Erdős--Gallai index.

The audited scope also includes:

- profile-dependent positive slack;
- classification of equality in the threshold theorem by stars and once-subdivided stars;
- rigidity of the corresponding target realizations;
- exact zero-edge correction inequalities; and
- graphicality of the full edge-imbalance multiset when at most one source edge joins equal-degree vertices.

The labeled realization, complete-graph b-factor formulation, signed-incidence equation, transferred degree-sequence inequalities, and locally irregular decomposition observation are standard reformulations or immediate consequences, not separately claimed breakthroughs.

## Verification and scope

| Gate | Status |
|---|---|
| Independent ordinary proof | Complete |
| Independent AI adversarial mathematical audit | Pass; high confidence |
| Independent finite corroboration | Pass; non-load-bearing |
| Literature and priority record | Corrected 2 August 2026; the earlier audit is superseded |
| Headline priority | Earlier proof by Raoui; no first-solution claim here |
| Additional results | Slack/equality/one-equal-edge results absent from Raoui and Schreib; broader priority review incomplete |
| Human specialist review | Not obtained; not claimed |
| Formalization | Published Lean 4 formalization by Schreib; source inspected but not rebuilt here. This repository's alternative argument and extensions are not kernel checked |
| Manuscript | Priority-corrected Version 1.1 release candidate |

The original literature search missed Raoui's June 2026 preprint and Schreib's
July 2026 formalization. The repository therefore makes no priority claim for
the headline theorem or the threshold-set statement. The existing `v1.0.0`
release is retained only as a historical snapshot and is superseded for
citation and DOI purposes.

The problem was identified for investigation through
[UnsolvedMath v1.2.0](https://huggingface.co/datasets/ulamai/UnsolvedMath),
curated by UnsolvedMath Contributors and released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). UnsolvedMath
provided discovery and indexing only; the MathOverflow question and primary
papers, not the dataset, are the authorities for the statement and status used
here.

## Repository map

- [`proof/`](proof/) preserves the complete corrected proof return.
- [`paper/`](paper/) contains the priority-corrected manuscript source,
  bibliography, PDF, and historical build/comparison records.
- [`audits/`](audits/) records the mathematical and literature adjudications.
- [`verification/`](verification/) contains independent dependency-free Python and exhaustive C++ corroboration.
- [`auxiliary/`](auxiliary/) contains all four non-load-bearing programs and
  captured outputs referenced by the manuscript.
- [`formalization/`](formalization/) distinguishes Schreib's external Lean
  formalization from the unformalized alternative proof and extensions here.
- [`audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md`](audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md)
  records the historical Version 2.1 audit; its release approval is superseded
  by the priority correction.
- [`scripts/verify.sh`](scripts/verify.sh) validates the sanitized release surface and replays the independent checkers.

## Verification

The default verification path installs nothing:

```bash
bash scripts/verify.sh
```

The universal proof is symbolic. The finite programs are regression and falsification evidence only.

## Authorship and AI disclosure

DannyExperiments initiated and directed the investigation, selected the validation requirements, curated and validated the artifacts, and is the human curator and conventional manuscript author of this project. OpenAI GPT-5.6 Pro generated the ordinary-language proof, quantitative and extension results, and initial manuscript. OpenAI Codex coordinated audit and provenance work and prepared the repository and reproducibility infrastructure. No AI system is listed as an author.

See [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md) and [`PROVENANCE.md`](PROVENANCE.md). No repository-wide reuse license is granted.

Human specialist review has not been obtained. The repository records an
AI-generated, human-curated independent proof and extensions, not journal
acceptance or a first solution of the conjecture.
