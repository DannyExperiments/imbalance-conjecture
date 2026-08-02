# Source-to-manuscript comparison

## Immutable baseline

The Version 2 archive was verified before use:

```text
SHA-256: b311713693c8b82411795dbff09c43c541692ca7d16db2dcb896b990b1b02d1d
Internal checksum ledger: PASS
Archive integrity test: PASS
```

Version 2.1 is a separate derivative. The baseline was not edited in place and is not embedded in this package.

## Bibliographic reconciliation

| Record | Version 2.1 active form | Manuscript treatment |
|---|---|---|
| 2013 MathOverflow question | Sergiy Kozerenko, “Graphs with graphic imbalance sequences,” question 140819, August 30, 2013 | Origin identified on the opening page; exact title appears in the bibliography |
| Kozerenko--Skochko (2014) | *Algebra and Discrete Mathematics* 18(1), 97--108 | Published formulation, proved classes, and order-nine verification stated without expansion |
| Kozerenko (2019) | *Journal of Advanced Mathematical Studies* 12(1), 50--62 | Multigraph-target theorem explicitly distinguished from the present simple-graph conclusion |
| Kozerenko--Serdiuk | *Opuscula Mathematica* 43(1) (2023), 81--100; published online December 30, 2022 | Conjecture 5.5 and verification through source order 12 retained |

The arbitrary-subset Erdős--Gallai criterion and strong/reduced-index reductions remain described as prior degree-sequence machinery. The source-graph threshold theorem is distinguished as the new imbalance-specific forcing statement. Labeled realization, complete-graph b-factor language, the signed oriented incidence equation, transferred degree-sequence inequalities, and the locally irregular decomposition observation remain described as standard reformulations or immediate consequences.

## Residual source limitations

The manuscript uses the required five-gap statement exactly:

> Residual source gaps include an ambiguous inaccessible 2025 Serdiuk listing, an unidentified AI-summary/search snippet, one Scholar-indexed citation to the 2014 paper that could not be independently identified, incomplete subscription-database coverage, and possible unindexed or unpublished work.

The qualified novelty statement remains unchanged: apparently new with moderate novelty confidence; absolute historical priority is not claimed.

## Mathematical source comparison

A structural source comparison was performed between the immutable Version 2 TeX and Version 2.1.

| Audited item | Version 2 | Version 2.1 | Result |
|---|---:|---:|---|
| Labeled display environments | 79 | 79 | Exact contents and labels preserved |
| Lemma statements | 4 | 4 | Byte-identical |
| Corollary statements | 3 | 3 | Byte-identical |
| Theorem statements/scopes | 5 | 5 | Byte-identical |
| Mathematical labels | 100 unique | 100 unique | Same order; no duplicates |
| Proof environments | 11 | 11 | Byte-identical |
| Proof paragraphs | 38 | 38 | Byte-identical |

All load-bearing inequalities, all boundary cases, the threshold-equality classification, the corrected zero-edge inequalities, and the one-equal-edge extension are therefore unchanged. The preserved repairs include the empty-source boundary, active sets for every selected head, the `r=0` boundary, the explicit `h=2` algebraic subcase, allowance for an empty active set, and the phrase “signed oriented incidence matrix.”

The machine-readable comparison is `MATHEMATICAL_PRESERVATION.json`.

## Render comparison

Both PDFs have 15 A4 pages. At 180 dpi, pages 3--14 are pixel-identical. Differences occur only on pages 1, 2, and 15, precisely where the corrected page range, five-gap sentence, and bibliography entries render. No mathematical page changed.

## Source-conflict disposition

No unresolved source conflict required a theorem change or narrower mathematical wording. The only unresolved matters are the five documented literature-coverage gaps. Human specialist review and proof-assistant verification have not been obtained.
