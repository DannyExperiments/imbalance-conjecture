# The Imbalance Conjecture

[![Repository verification](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/verify.yml)
[![PDF build](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/pdf.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/imbalance-conjecture/actions/workflows/pdf.yml)

[Paper (PDF)](paper/manuscript.pdf) ·
[Complete proof](proof/PROBLEM_AND_PROOF.md) ·
[Mathematical audit](audits/MATHEMATICAL_AUDIT.md) ·
[Literature audit](audits/LITERATURE_PRIORITY_AUDIT.md) ·
[Independent checkers](verification/README.md) ·
[Release notes](release/RELEASE_NOTES_v1.0.0.md) ·
[Reproduce](REPRODUCIBILITY.md)

This repository gives a complete proof of the Imbalance Conjecture, together
with a stronger threshold-set theorem, an equality classification, and a
one-equal-edge extension.

## The problem

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

## Result

The answer is affirmative.

> **Imbalance Conjecture.** Let `G` be a finite simple graph. If `d_G(u) != d_G(v)` for every edge `uv`, then
>
> \[
> \{\lvert d_G(u)-d_G(v)\rvert:uv\in E(G)\}
> \]
>
> with multiplicity is the degree multiset of a finite simple graph.

The proof establishes a stronger arbitrary threshold-set theorem. If `S` is any `k`-edge subset and every edge in `S` has imbalance at least `k`, then `S` satisfies its subset Erdos-Gallai inequality. This implies the sorted top-threshold theorem and rules out a first failed Erdos-Gallai index.

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
| Ordinary proof | Complete |
| Independent adversarial mathematical audit | Pass; high confidence |
| Independent finite corroboration | Pass; non-load-bearing |
| Literature and current-open-status audit | Complete through August 1, 2026 |
| Novelty | Apparently new; moderate confidence |
| Human specialist review | Not obtained; not claimed |
| Lean/Aristotle | No completed certificate; Stage 1 prompt prepared |
| Canonical post-literature manuscript | Version 2.1 installed; final manuscript audit passed |

The documented literature search found no retrievable earlier complete finite-simple-graph solution. It did identify narrow residual source gaps, so this repository does not claim absolute historical priority or a certified first proof.

The problem was identified for investigation through
[UnsolvedMath v1.2.0](https://huggingface.co/datasets/ulamai/UnsolvedMath),
curated by UnsolvedMath Contributors and released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). UnsolvedMath
provided discovery and indexing only; the MathOverflow question and primary
papers, not the dataset, are the authorities for the statement and status used
here.

## Repository map

- [`proof/`](proof/) preserves the complete corrected proof return.
- [`paper/`](paper/) contains the canonical post-literature Version 2.1 TeX,
  bibliography, PDF, and public-safe build/comparison records.
- [`audits/`](audits/) records the mathematical and literature adjudications.
- [`verification/`](verification/) contains independent dependency-free Python and exhaustive C++ corroboration.
- [`auxiliary/`](auxiliary/) contains all four non-load-bearing programs and
  captured outputs referenced by the manuscript.
- [`formalization/`](formalization/) records the exact current nonformalization boundary and staged Aristotle prompt.
- [`audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md`](audits/FINAL_MANUSCRIPT_AUDIT_STATUS.md)
  records the completed independent Version 2.1 audit and public-release approval.
- [`scripts/verify.sh`](scripts/verify.sh) validates the sanitized release surface and replays the independent checkers.

## Verification

The default verification path installs nothing:

```bash
bash scripts/verify.sh
```

The universal proof is symbolic. The finite programs are regression and falsification evidence only.

## Authorship and AI disclosure

DannyExperiments initiated and directed the investigation, selected the validation requirements, curated and validated the artifacts, and is the human curator and conventional manuscript author of this project. OpenAI GPT-5.6 Pro generated the ordinary-language proof, strengthened results, and initial manuscript. OpenAI Codex coordinated audit and provenance work and prepared the repository and reproducibility infrastructure. No AI system is listed as an author.

See [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md) and [`PROVENANCE.md`](PROVENANCE.md). No repository-wide reuse license is granted.

Human specialist review and proof-assistant verification have not been obtained and are not claimed. The repository records a solver-authored proposed solution, not journal acceptance or human peer review.
