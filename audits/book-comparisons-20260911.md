# Book comparison-context revision — 11 September 2026

The Flint opening now puts the model-guided hit rate of about **80%** beside **15%** under the changed priorities. The later discussion gives the recovery to about **70%** after targeting resumed. A footnote explains the denominator and successive programme phases.

Reviewed **all 42 chapters and all 19 other configured book components**. Corrected **35 passage groups across 20 chapters, the evidence-reading guide, and Appendix F**; net addition **566 words**. The changes name missing controls, align the compared outcome, or add verified paired values. Examples include retirement allocations, investor returns, park signs, AI inference prices, mammography screening, physician reasoning, and the watched-eyes caption and figure label. Existing ABT revisions were preserved.

Added a concise comparator rule to the general, paper, and referee writing skills. It applies to numerical/performance claims carrying the argument, requires meaningful aligned comparisons, and avoids invented benchmarks.

## Verification

- Full HTML render and EPUB render completed successfully. A final Chapter 42 HTML render incorporated the independent review's “per case” clarification.
- Book QA: **0 errors, 0 warnings**. EPUB QA: **0 errors**.
- Reference synchronization: **834 unique entries**, current.
- All **61** canonical HTML pages passed local link/anchor checks.
- All **37 revised prose lines** passed source-to-HTML/EPUB text checks; **18 targeted numeric/currency checks** passed in both editions.
- Headings, identifiers, display equations, tables, existing footnotes, reference blocks, and link targets were preserved. Intentional additions are documented in the checks file.
- Updated watched-eyes SVG/PNG match their HTML copies. EPUB embeds the final SVG byte-for-byte; its PNG fallback was regenerated and inspected offline.
- Frozen source hashes remained unchanged through final verification. Staged and released EPUB files match. `git diff --check` passes.
- Independent review verified the new Chapter 42 comparisons and all three skill updates. Its one observation-unit clarification was applied and rechecked.

The output checks used source, HTML text, and EPUB package inspection. No live browser or EPUB-reader visual inspection is claimed. Updated sources and both editions are local; this pass did not commit or push.

Detailed coverage and primary-source checks: [review ledger](book-comparisons-20260911-review.md). Machine-readable results and final hashes: [checks](book-comparisons-20260911-checks.json).
