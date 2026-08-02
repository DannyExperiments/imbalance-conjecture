# Provenance

## Problem record

- Sergiy Kozerenko, ["Graphs with graphic imbalance sequences"](https://mathoverflow.net/questions/140819/graphs-with-graphic-imbalance-sequences), MathOverflow question 140819, August 30, 2013.
- Sergiy Kozerenko and Volodymyr Skochko, ["On graphs with graphic imbalance sequences"](https://doi.org/10.12958/adm135), *Algebra and Discrete Mathematics* 18(1) (2014), 97-108.
- Sergiy Kozerenko and Andrii Serdiuk, ["New results on imbalance graphic graphs"](https://doi.org/10.7494/OpMath.2023.43.1.81), *Opuscula Mathematica* 43(1) (2023), 81-100; published online December 30, 2022; Conjecture 5.5.

## Discovery route

The project identified the Imbalance Conjecture for investigation through
[UnsolvedMath v1.2.0](https://huggingface.co/datasets/ulamai/UnsolvedMath), a
dataset curated by UnsolvedMath Contributors and released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The dataset supplied
discovery and indexing, not the proof. Its record was not used as the authority
for the theorem statement or current status; those were checked against the
MathOverflow question and primary literature listed above.

## Frozen private evidence

The source-return warehouse is preserved separately from this sanitized release surface. The controlling frozen manuscript archive is:

```text
THE_IMBALANCE_CONJECTURE_PRIVATE_MANUSCRIPT_AUDIT_RECONCILED_2026-08-02.zip
SHA-256 f995ec1020c813b6c02b07990931a0e5012a2041cd4a79a10f376fc024accef5
```

The archive contains the corrected TeX/PDF, independent referee report, dependency-free Python checker, exhaustive C++ checker, logs, errata, manifests, and checksums. It remains immutable even though its manuscript predates the completed literature audit.

Additional controlling hashes:

| Artifact | SHA-256 |
|---|---|
| External adversarial referee report | `12a2ff82037ae3dd30b0506ae611ba65ecceefb30a70e0dcaff4cd26c6394c75` |
| Audit adjudication | `fc968e253ede1ea3e3abe42d09cd6b6a76af476ffc42e66531e2f43da385179f` |
| Independent novelty/status audit | `0188e66d5dc5335b8b939f624caed24512f51a5a2e138a2308ce42d1a4219da1` |
| Frozen candidate TeX | `109c6e15ba114192e95824ba1b1c09013142bab0297263656c2f3ec3f0f39fbf` |
| Frozen candidate PDF | `f5afa97d49c20a1e30c1605fcfe7af2fc1d94bfa1812dbd2c1965e1fb96250cb` |

## Audit chronology

1. The original proof and research packet were frozen on August 1, 2026.
2. A separate adversarial AI referee reconstructed the main proof and extensions.
3. Six local clarifications and boundary repairs were incorporated into the audit-reconciled candidate.
4. The independent Python checker and exhaustive seven-vertex C++ checker were freshly replayed.
5. A separate internet-enabled literature audit checked the open status, closest prior results, forward citations, and extension novelty through August 1, 2026.
6. A distinct post-literature Version 2 manuscript package was produced and
   installed on the sanitized release worktree without substituting for the
   immutable predecessor. Its archive SHA-256 is
   `b311713693c8b82411795dbff09c43c541692ca7d16db2dcb896b990b1b02d1d`,
   and its PDF SHA-256 is
   `4c7ae205fa07839ff200ff7ecb407471da1d9b55862a0a39f2c5ae143ff00016`.
7. Package integrity, clean-build records, exact source comparison, and visual
   inspection records accompany Version 2. A later independent final-manuscript
   audit passed all mathematical, artifact, reference, disclosure, and visual
   checks but found one omitted residual-source-gap item and two stale primary-
   source details.
8. Version 2.1 was produced as a separate provenance-only derivative. Its
   archive SHA-256 is
   `7dd54873d651654f3508d977d7660260fd053c301181da0a525ae3337ceaa638`.
   The archive and complete internal checksum ledger passed. Its installed
   TeX, PDF, and bibliography hashes are, respectively,
   `6ba7493f5f7d54288582e102c5a309d0fadb6c73a00b290f95fcc87deb55ce59`,
   `d7282af267d46969f0847e88d00fa89e2b1c6bd06cc1afa29a8b2332d7dcccac`,
   and `f0de679a60a486885ece83e44c7f1f854680ffd594180c73b5322cf412e3bbf2`.
9. Independent reconciliation confirmed that Version 2.1 changes only the
   exact MathOverflow title, the authoritative 2023 page range, the complete
   five-gap disclosure, and consequential build/comparison records. All 79
   labeled displays, four lemmas, three corollaries, five theorem scopes, 100
   mathematical labels, 11 proof environments, and 38 proof paragraphs are
   preserved. All 15 rendered pages passed visual inspection, with pages 3--14
   pixel-identical to Version 2 at 180 dpi. The final-manuscript audit passes.

## Contribution boundary

DannyExperiments is the human curator and conventional manuscript author. GPT-5.6 Pro generated the ordinary proof and initial manuscript. Codex coordinated auditing, provenance, repository integration, and reproducibility. No AI system is an author, and no claim of unaided human discovery is made.

Public posting will establish a public timestamp for the posted files. It will not by itself establish historical priority, peer review, or journal acceptance.
