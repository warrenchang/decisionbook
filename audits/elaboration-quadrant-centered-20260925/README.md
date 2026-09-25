# Centered elaboration quadrant — 25 September 2026

## Revision

- Moved the motivation and ability axes to the middle of the four equal quadrants. Kept Low/High directions and short condition labels; removed the former outside axes and dashed interior dividers.
- Replaced the former Table 30.1 with two paragraphs covering all four combinations and their practical implications. No substantive evidence or references were removed. Preserved `tbl-25-1` as a legacy anchor beside the replacement explanation.
- Updated the caption, alternative text, editable SVG generator, and matching PNG. The caption retains the continuous-dimensions qualification.

## Verification

- Chapter 30 HTML and full EPUB rebuilt successfully.
- Book QA: 0 errors and 0 warnings. EPUB QA: 0 errors. Bibliography: 1,096 references, synchronized.
- Source, HTML, and EPUB float checks: 106 figures and 164 tables, no issues. All remaining tables renumber automatically.
- HTML navigation, search, aliases, and links: 62 pages, 42 chapter entries, 91 aliases, 7,681 local links; no issues.
- SVG containment checked at 780px and 350px. Minimum label size at 350px: 13.46 CSS px; no clipping. Connector geometry passes.
- Figure inspected in generated HTML at 390px and 1280px viewports and in extracted EPUB at 390px and 768px. Central axes, quadrant labels, directions, and outer margins remain readable. Screenshots and geometry are in `visual-qa/`.
- Final HTML SVG/PNG and embedded EPUB SVG match the source assets. The old table anchor and both replacement paragraphs were verified in both editions.
- `git diff --check` passed. No commit or push requested or performed.

Status: **REVISED / verified**. This focused revision supersedes the prior table-plus-figure arrangement recorded in `audits/visual-readability-20260925/`.
