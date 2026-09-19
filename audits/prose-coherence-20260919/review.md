# Prose coherence review — 19 September 2026

Reviewed the 62 configured sources, including all 42 chapters, the reading guides, part introductions, and appendices. Edited 38 chapters and five appendices, with a net reduction of 2,156 words. This pass builds on the earlier heading consolidation and preserves those revisions.

## Editorial decisions

Removed detached methodological asides, obvious restatements, generic cautions, editorial previews, and sentences explaining what an immediately preceding example already makes clear. Each candidate was considered in context rather than removed by a global text rule. The review included targeted searches and a separate pass over short standalone paragraphs.

Examples include the reminder that explicitly separate experimental groups were not the same individuals; a reminder that a stated forecast was not a later measurement; and repeated statements that familiar evidence could not prove an unrelated stronger claim. Reworked a few sentences to state the relevant comparison directly. Integrated comparison-group and sample details beside the studies they describe, and removed resulting repetitions.

Retained qualifications that materially determine interpretation, including disputed or retracted findings, measurement distinctions where a claim depends on them, model assumptions, uncertain estimates, and alternative explanations developed as part of the argument. No studies, tables, figures, or bibliography entries were removed. No new empirical claims or sources were added.

## Verification

- Full HTML and EPUB builds completed.
- Book QA: zero errors and zero warnings.
- Reference synchronization: 1,028 unique references; passed.
- EPUB release QA: zero errors.
- All 62 sources retain their headings, anchors, figures, tables, reference lists, and distinct citation years relative to the start-of-pass snapshot.
- Ninety-six exact deleted sentences or passages checked absent from HTML, EPUB, and the search index. Other edits condense or reconnect retained text.
- All 235 link targets affected by the earlier heading pass still resolve in HTML and EPUB.
- Float checks cover 116 figures and 166 tables, with zero issues.
- Git whitespace check passed. No commit or push performed.

`prose-only.diff` shows the final changes relative to the start of this pass, separate from the earlier heading edits. `edits.json` records the editorial sequence, including subsequent refinements. `preservation-qa.json` and `rendered-removals-qa.json` record the checks.
