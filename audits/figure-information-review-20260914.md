# Figure information review — 14 September 2026

## Result and scope

Reviewed all 117 unique visual assets used by the 62 configured book sources: 109 SVG diagrams and eight raster or animated assets, including the cover. Revised 46 diagrams; 71 assets already communicate their intended concept, activity, result, or illustrative purpose. This review follows the earlier redundancy cleanup and corrects places where useful information was lost or was never explicit enough.

The governing distinction is between repeated decoration and necessary explanation. A figure needs the terms, conditions, quantities, and relationships that let readers understand its central point independently of the chapter prose. An activity may invite a prediction without displaying its answer; a photograph need not become a conceptual diagram. All assets have an individual disposition in the [review ledger](figure-information-review-20260914-ledger.json).

## Figure F.3

Replaced the generic participant-flow questions with three separate, named mechanisms and a fourth analysis panel:

- **Noncompliance:** treatment assigned versus treatment received; both treatment nonreceipt and control crossover are explicit.
- **Attrition:** randomized participants versus participants observed; the diagram explains missing outcomes and the possibility of losing comparability.
- **Spillovers (interference):** one person's treatment can affect another person's outcome, including across treatment and control groups.
- **Intention-to-treat (ITT):** compare outcomes by original assignment; this alone does not resolve attrition or spillovers.

The three threats are not connected as a mandatory sequence. The visible explanations retain conditional language where the scientific conclusion is conditional. Updated the caption, alternative text, and accompanying paragraph in the physical Appendix E source, which publishes as Appendix F. The distinction between these threats agrees with J-PAL's [elements of randomized evaluation](https://www.povertyactionlab.org/resource/elements-randomized-evaluation) and [implementation monitoring guidance](https://www.povertyactionlab.org/resource/implementation-monitoring). A separate reviewer checked the scientific distinctions and inspected the final individual render: [independent review](figure-information-review-20260914-root-independent.md).

The 760-unit-wide design uses text of at least 28 units, equivalent to approximately 12.2 pixels at a 330-pixel image width. Native and phone inspection found no clipping or text outside its panels. The final HTML and EPUB phone views were inspected individually; all four concepts are readable inside the illustration.

## Repairs elsewhere

The 45 other revisions restore or clarify conventional terms, comparison conditions, measurement labels, instructions, or short explanations. Examples include attribute substitution and confirmation bias; regression to the mean and reward prediction errors; the 0–100, two-thirds-of-the-mean guessing task; visible versus hidden download counts in Music Lab; the meaning of Schelling's neighborhood-share statistic; grounding in communication; BATNA and reservation values; equivalent simultaneous offers; and the hypothetical loss definitions in the AI examples. Per-asset explanations appear in the [early](figure-information-review-20260914-early.md), [middle](figure-information-review-20260914-middle.md), and [late](figure-information-review-20260914-late.md) review notes.

Numerical results and simulation parameters were preserved. The Schelling reconstruction reproduced the displayed moves and mean neighbor shares, with all 759 circle attribute sets unchanged. The original Chapter 1 illustration structure was preserved. Figure F.2 retains treatment and control centers 115 units to either side of random assignment's center.

Added the **Keep the figure informative** standard to [the book editing guide](../QUARTO_EDITING_GUIDE.md), including requirements for essential terminology, units, conditions, scientific qualifications, accessibility, and final rendering. Generator instructions were synchronized so regeneration retains the reviewed labels. All 23 outputs governed by the cleanup manifest match their canonical SVGs exactly; application is idempotent and rejects unreviewed input changes. Six hand-maintained outputs remain protected. The revised methods and Schelling outputs were also reproduced independently.

## Verification

- All 109 SVGs pass connector checks and the final text/viewBox and duplicate-identifier screen. Revised figures were inspected individually at native size, followed by a review of all ten final contact sheets.
- Regenerated the 46 revised SVGs' PNG fallbacks and rebuilt HTML and EPUB sequentially.
- Book source/rendered QA: zero errors and zero warnings. Reference synchronization check: 884 entries.
- HTML: 118 image placements load across 62 pages at 1440 and 390 pixels; zero reported figure-layout issues. Navigation check: 2,364 main-content internal links, 685 search entries, and 126 appendix-labeled links; zero issues.
- EPUB: 116 image placements load across 64 XHTML documents at 768 and 390 pixels; zero reported issues. EPUB release QA: zero errors.
- F.3 retains its correct number, full alternative text, and caption below the illustration in both editions; no page overflow at the checked widths.
- Final publication byte checks are recorded in the [published-assets report](figure-information-review-20260914-published-assets.json), covering all 117 HTML assets and the 116 expected EPUB assets. The hollow-face GIF retains its existing HTML-only condition.

Persistent evidence: [SVG bounds and F.2 symmetry](figure-information-review-20260914-bounds.json), [F.3 text size and padding](figure-information-review-20260914-f3-bounds.json), [generators](figure-information-review-20260914-generators.json), [HTML figures](figure-information-review-20260914-rendered-figure-qa.json), [EPUB figures](figure-information-review-20260914-rendered-epub-figure-qa.json), [HTML F.3](figure-information-review-20260914-html-f3.json), [EPUB F.3](figure-information-review-20260914-epub-f3.json), and [navigation](figure-information-review-20260914-navigation.json). General checks are in [QA_REPORT.md](../QA_REPORT.md) and [EPUB_QA_REPORT.md](../EPUB_QA_REPORT.md).

These checks establish the reviewed information and tested rendering, not a claim that every complex landscape figure now reflows into a phone-sized portrait. Existing deliberate reading panes remain. EPUB layout was inspected in Chromium using the final packaged XHTML, not in every commercial e-reader. Existing user work was preserved; no commit or push was performed.
