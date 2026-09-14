# Figure text and F.2 alignment review — 14 September 2026

## Outcome

Reviewed all 117 unique visual assets used by the configured book: 109 SVGs, six still images, the inline hollow-face animation, and the cover. Revised 106 diagrams; 11 assets required no change. All 109 SVGs have current PNG companions. The HTML and EPUB editions were rebuilt.

F.2 now aligns the evaluation sample and random assignment at x=240. Treatment and control centers are x=125 and x=355, giving equal 115-unit branches. Both group boxes remain 200×102 at y=718. External and internal validity remain unboxed annotations, separated from the study procedures.

Removed repeated outer titles, recap banners, footers, and duplicate panel explanations. Retained essential node/panel labels, task instructions, axes, values, denominators, source information, and scientific qualifications. Caption/body context supplies explanations removed from the graphics; unique data were not deleted merely because they appeared above or below a diagram. Chapter 1's original illustration topology is retained.

Fourteen QMD sources changed only in their figure alternative text, to remove references to deleted visual panels and notes. A comparison against the start-of-turn snapshot confirms all other prose, tables, and references are unchanged by this turn. Accessible SVG titles/descriptions remain present. The cover, personal photographs, object illustrations, and animation contain no redundant editorial overlays.

## Verification

- All 109 SVGs parsed and passed connector attachment/proportion and browser text-bound checks; no duplicate SVG IDs or text beyond final viewBoxes.
- All vector figures inspected individually at native size, then on final contact sheets. Root-owned seven diagrams received an additional independent review. F.2 also passed box-padding, validity-label gap, and exact symmetry checks.
- HTML: 62 configured pages; 118 visual placements checked at desktop 1440px and phone 390px; zero layout/loading issues.
- EPUB: 116 figure placements checked at 768px and 390px; zero layout/loading issues. F.2 has its correct number, caption below the image, and no horizontal overflow in both formats.
- Source/publication QA: zero errors and warnings. EPUB release QA: zero errors. Navigation: 2,364 main internal links and 685 search entries resolve; appendix labels and order are consistent.
- All 117 HTML image assets and 116 EPUB assets match their final source or PNG fallback by exact hash. The hollow-face animation remains HTML-only under the existing source condition; its explanation and source link remain in EPUB.
- Seven root generators reproduce their final SVGs byte-for-byte. The 23 active generated outputs in the other figure builders reproduce the reviewed SVGs, are idempotent, and reject unreviewed input drift. Transparent guarded patches preserve earlier reviewed wrapping/layout changes. Legacy conversion scripts and six designated hand-maintained assets remain outside that generator update.

The narrow-layout checks preserve existing deliberate horizontal reading panes for wide figures. They verify loading and containment, not universal phone reflow. Individual native inspection and representative destination screenshots supplement those automated screens.

## Records

- `figure-text-review-20260914-ledger.json`: every asset, exact removed text, status, final hashes, and verification notes.
- `figure-text-review-20260914-early.md`, `-middle.md`, `-late.md`: individual review ledgers.
- `figure-text-review-20260914-root-independent.md`: independent semantic and visual check of F.2 and the appendix/master diagrams.
- `figure-text-review-20260914-bounds.json`: all SVG text bounds and F.2 geometry.
- `figure-text-review-20260914-prose-preservation.json`: QMD changes restricted to alternative text.
- `figure-text-review-20260914-published-assets.json`, `-navigation.json`, `-html-destination.json`, `-epub-destination.json`: publication checks.
- `figure-text-review-20260914-root-generators.json` and `-generator-cleanup.json`: generator reproduction checks.

Existing uncommitted work was preserved. No commit or push was made.
