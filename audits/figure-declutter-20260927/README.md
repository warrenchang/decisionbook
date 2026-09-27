# Figure text review — 27 September 2026

Reviewed every numbered figure in the configured book: **108 reviewed, 29 revised, 79 retained, 0 blocked**. The cover and author portrait were also inspected and retained. Legacy figures outside the configured book were not changed.

Figure 26.1 now shows only the target and comparison panels, their lines, and essential labels. Removed the question heading, “170 units,” red endpoint marks, and pink follow-up box. The question and imagined unanimous answer are in the caption and adjacent prose. All four line coordinates are unchanged.

Across the book, removed redundant explanatory sidebars, general advice panels, repeated titles, and interpretation footers. Retained concepts, task-defining prompts, axes, condition labels, values, uncertainty qualifications, and legends. Captions and alt text were updated where their descriptions changed. The editing guide now records this convention.

| Scope | Reviewed | Revised | Retained |
| --- | ---: | ---: | ---: |
| Chapters 1–14 | 35 | 7 | 28 |
| Chapters 15–28, excluding 26 | 31 | 10 | 21 |
| Chapters 29–42 | 29 | 5 | 24 |
| Front matter, Chapter 26, appendices | 13 | 7 | 6 |

## Verification

- Complete HTML and EPUB builds completed sequentially; render logs are included here.
- Book QA: zero errors and zero warnings. EPUB QA: zero errors.
- Float coverage: 62 configured sources, 108 figures and 164 tables, with zero source, HTML or EPUB reference issues.
- Bibliography union: 1,189 unique chapter-and-appendix references, check passed.
- All 29 revised SVGs match the assets in final HTML and EPUB exactly; every corresponding HTML PNG matches its canonical fallback.
- All 26 guarded generator records pass hash, patch replay, no-op and drift-rejection checks. Six isolated generator outputs reproduce the canonical SVG byte for byte. Music Lab, participant-flow and model-underdetermination generators were also checked separately.
- All 2,000 simulation records and all simulation metadata reproduce exactly. Empirical plot geometry is preserved. The model-underdetermination metadata changes only its minimum retained label-size calculation after removal of a footer.
- An independent second review of the seven root-owned revisions found no missing scientific qualification, altered data or stale alt text.
- `git diff --check` passes.

Every figure received visual review through contact sheets or individual renders, as specified in its ledger. Revised vectors were inspected individually at source or large reading size and narrow reading size. Final HTML and extracted EPUB content were sampled in the browser at desktop and 390-pixel widths. Wide figures retain the book’s existing horizontal reading panes. EPUB browser checks do not represent every native e-reader.

## Records

- `combined-ledger.json`: decisions and checks for all 108 numbered figures.
- `early-ledger.json`, `middle-ledger.json`, `late-ledger.json`, `root-ledger.json`: detailed reviews and provenance.
- `root-independent-review.json`: independent scientific/semantic review.
- `generator-verification.json` and `verify_generators.py`: exact generator checks. Use Matplotlib 3.11.1 for the recorded simulation SVG.
- `published-asset-verification.json`: final edition asset hashes.
- `png-verification.json`: decoded pixel comparisons using each figure’s production density and background settings.
- `destination-visual-review.json`: browser observations and limits.
- `float-reference-final.json`: full source/HTML/EPUB float coverage.

Earlier Chapter 7 face illustrations and the separate Chapter 12 framing revision were preserved. This review did not commit or push changes.
