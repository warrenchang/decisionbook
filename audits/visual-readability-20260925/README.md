# Visual readability revision — 25 September 2026

Reviewed all 42 chapters and the complete 62-source canonical reading route for places where a graphic would reveal a relationship, experimental comparison, or calculation more clearly. This was a book-wide **source-level opportunity review**, followed by full visual QA of the four selected additions. It was not a fresh visual certification of every retained figure.

## Implemented

| Location | Addition | What the visual contributes |
| --- | --- | --- |
| Chapter 30, Figure 30.2 / Table 30.1 | Motivation–ability quadrant | Separates willingness to evaluate a message from knowledge, time, and attention. The table retains practical implications. Continuous dimensions, not fixed audience types. |
| Chapter 22, Figure 22.2 | Cold-water protocol timelines | Makes the identical first minute and added, less unpleasant ending visible. Timing and the published 22/32 repeat-choice result; no invented pain trajectory. |
| Chapter 24, Figure 24.1 / Table 24.3 | Expected payoff against belief | Derives the 61.5% switching threshold from the chapter's declared stag-hunt payoffs. Illustrative calculation, not observed behavior. |
| Chapter 38, Figure 38.1 | Payoffs with and without approval | Shows why two apparently attractive contract packages create different financial incentives. Hypothetical state payoffs, before effort costs. |

Each figure has a concise caption, descriptive alt text, local prose discussion, editable generator, and PNG companion generated from its final SVG. Existing studies, references, tables, and figures were retained. Only Chapters 22, 24, 30, and 38 changed in this pass; see `source-changes.patch`, compared with the working tree at the start of the task rather than HEAD. Earlier title/file revisions were preserved.

The chapter-by-chapter decisions, including deferred candidates and their reasons, are in `review-01-14.md`, `review-15-29.md`, and `review-31-end.md`. Chapter 30 received an independent semantic and native-image review in `review-ch30-independent.md`; its suggested “less motivated” wording was incorporated.

## Verification

- Full HTML and EPUB builds completed. Chapter 30 HTML was refreshed after correcting arrowhead proportions. The final EPUB's four embedded SVGs match the final source assets byte for byte (`epub-asset-provenance.json`).
- Book QA: **0 errors, 0 warnings**. EPUB QA: **0 errors**.
- Float QA: **106 figures and 165 tables**, all with local prose references in source, HTML, and EPUB; **0 issues**.
- Bibliography synchronization: **1,096 unique references**, pass.
- HTML validation: **62 pages, 42 chapter navigation/search entries, 91 redirect aliases, 7,682 local links**, **0 issues**.
- New SVGs parse; label-containment checks at native 760px and narrow 350px passed. Minimum label size at 350px is **12.89 CSS px**. Final arrowhead-to-stroke proportions pass the repository validator.
- All four figures inspected individually at native and narrow sizes. Generated HTML inspected at 390px and 1280px viewports; extracted EPUB inspected at 390px and 768px. Desktop contact sheets retained. No clipping or horizontal figure scrolling at the inspected phone width. These are offline browser renderings, not tests of every EPUB application.
- The EPUB uses the SVGs directly. Companion PNGs were generated and inspected separately; no claim is made that the EPUB embeds a raster fallback.
- `git diff --check` passed.

## Figure verification ledger

| Figure | Status | Destination sizes inspected | Result |
| --- | --- | --- | --- |
| `elaboration-quadrant` | REVISED | SVG 760/350px; HTML 390/1280px; EPUB 390/768px | Axes, four labels, scientific boundary, and corrected arrowheads pass. |
| `cold-water-better-ending` | REVISED | SVG 760/350px; HTML 390/1280px; EPUB 390/768px | Shared interval, warming extension, duration scale, and reported choice clearly distinguished. |
| `stag-hunt-belief-payoffs` | REVISED | SVG 760/350px; HTML 390/1280px; EPUB 390/768px | Lines, crossing, labels, and units pass; arithmetic asserted in generator. |
| `contract-state-payoffs` | REVISED | SVG 760/350px; HTML 390/1280px; EPUB 390/768px | Common scale, state labels, and direct values pass; arithmetic recorded separately. |

`final-image-inventory.json` records all source image figures, including retained assets. `audits/float-reference-qa.json` also inventories the inline figure and all table floats. Retained figures received source-level consideration, not new visual PASS labels.

The HTML screenshot renderer disables scripts and networking; the inline fraction in Figure 24.1's caption consequently appears as a MathJax placeholder there. It is encoded correctly in generated HTML and displays as a fraction in EPUB. This does not affect the SVG chart.
