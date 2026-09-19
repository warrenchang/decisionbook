# Book-wide section hierarchy revision — 19 September 2026

## Result

Reviewed all **62 configured source documents**: 42 chapters, seven appendices, seven part introductions, and six front/back-matter sources. Revised **31 chapters and two appendices**, plus relevant concept-index display labels. Consolidated **59 headings** and corrected additional heading levels and titles. The review preserved developed conceptual distinctions and useful technical/reference navigation.

The valuation chapter now discusses music and cultural objects within **Experience and social meaning shape value**. The music-sales neuroforecasting study appears in the neuroscience research lens, where its predictive interpretation belongs. Waiting-cost effects now develop the broader account of changing motives.

Other substantive improvements include organizing mental accounting around its four operations; placing the four narrative mechanisms under their umbrella section; keeping ordinary plans outside the commitment-device subsection; and integrating brief cases, practical checks, and worked examples with the arguments they support.

## Review record

- [Chapters 1–10 and front matter](review-01-10-and-frontmatter.md)
- [Chapters 11–22](review-11-22.md)
- [Chapters 23–32](review-23-32.md)
- [Chapters 33–42](review-33-42.md)
- [Seven appendices](review-appendices.md)
- [Independent preservation review](preservation-review.md)

Sources were compared with the task-start snapshot, which includes the prior turn's uncommitted context/mood-memory revisions. Those earlier changes are preserved. Descriptive concept-index labels for Bennett and Sapolsky remain valid descriptions of their retained passages; their existing targets are preserved.

## Verification

- Full HTML and EPUB builds completed successfully, without warnings or errors.
- Source QA: **0 errors, 0 warnings**.
- Master bibliography check: **1,036 unique references**, unchanged by this task.
- EPUB release QA: **0 errors**.
- All **816 previous rendered heading IDs** remain valid, including headings converted to passage anchors. No duplicate rendered IDs.
- Across all 42 chapters, independent comparisons preserve **1,059 reference blocks, 88 figure declarations, 131 table blocks/captions, 34 footnotes, 7,898 numeric tokens, and 2,093 citation groups**. Counts include repeated chapter-level bibliography entries. Numeric comparisons exclude heading numbers, link targets, and anchors.
- All substantive appendix text is unchanged after stripping headings and standalone anchors.
- Float-reference QA covers **96 figures and 166 tables** across all 62 configured sources and the final HTML/EPUB; **0 issues**.
- Desktop and phone valuation screenshots were inspected, along with desktop mental-accounting and narrative-mechanism pages. Text and heading hierarchy render correctly; none of the inspected viewports has horizontal overflow.
- `git diff --check` passes. Incidental generated-file permission changes were restored to tracked modes.

Reproducible checks and outputs: `verify_hierarchy.py`, `rendered-hierarchy-qa.json`, `check_layout.js`, `layout-qa.json`, `float-qa.json`, and the preservation-review JSON. The preservation audit checks retained evidence and consequential changes; it does not claim to re-verify every pre-existing scientific claim in the book.

No commit or push was performed.
