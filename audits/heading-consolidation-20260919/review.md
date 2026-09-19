# Heading consolidation — 19 September 2026

Reviewed the 62 configured book sources, including all 42 chapters. Consolidated 189 narrative headings in 38 chapters, two reading guides, and three appendices. The narrative-heading inventory fell from 732 to 543 (25.8%). Retained headings for substantial topics, exercises, research and mathematical boxes, and reference tables/tools where they serve a distinct navigation purpose.

The three named Chapter 13 headings now sit within “Repetition can become liking and truth.” Their discussions and link targets remain. Broadened umbrella headings where needed; flattened the additional example hierarchy in Chapter 1; moved the Chapter 35 predictable-errors paragraph before the culture discussion and moved two section starts to include their introductory paragraphs.

Compared all non-heading, non-anchor source lines with a snapshot taken at the beginning of this pass. Substantive text, citations, tables, figures, and exercises are preserved. One Chapter 13 transition was reworded to connect flavor familiarity directly to the preceding example. Earlier uncommitted removals of three Chapter 13 asides are preserved.

## Verification

- Full HTML and EPUB builds completed; Chapter 1 received a final targeted HTML render after removal of inconsistent example numbering.
- Book QA: zero errors and zero warnings.
- Reference synchronization: 1,028 unique references; passed.
- EPUB release QA: zero errors.
- All 235 affected heading targets remain in HTML and EPUB. The 189 merged headings are absent from HTML headings and contents entries.
- Browser checks passed at 1,280px and 390px: Chapter 13 discussions remain together in the main text with no horizontal overflow; Chapter 35 passages belong to the intended sections.
- Chapter 13 desktop and mobile section captures visually reviewed. Fixed navigation is suppressed only in the screenshot capture to prevent overlap in the long image.
- Git whitespace check passed. No commit or push performed.

The detailed change manifest is `changes.json`; original narrative-heading inventory is `inventory.json`; checks are recorded in `source-conservation.json`, `anchor-qa.json`, and `browser-qa.json`.
