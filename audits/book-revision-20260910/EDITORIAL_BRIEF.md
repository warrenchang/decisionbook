# Editorial brief: whole-book revision

The author's request is to apply the habit chapter's successful revisions to every part introduction, chapter, illustration, and other reader-facing section. The book should be more engaging, easier to follow, less repetitive, and scientifically dependable. This is an authorized substantive revision, not merely an assessment or a sample edit.

## What the habit revision established

1. Begin with a concrete situation that raises a worthwhile question; develop the example before naming several theories.
2. Build an explanatory sequence. Each section should answer a question made meaningful by the preceding one, and each paragraph should have a clear job.
3. Introduce one important distinction at a time, define unfamiliar terms on first use, and replace abstract labels with ordinary language where meaning is preserved.
4. Keep a useful recurring example while allowing other examples when they reveal a different mechanism. Do not impose the same fictional scene or template on every chapter.
5. Remove repeated definitions, catalogues, boilerplate, unnecessary tables, and previews that simply restate the paragraph that follows. Preserve genuinely useful retrieval practice and cross-chapter reminders.
6. Let studies answer the reader's question: explain the comparison, finding, and implication together. Preserve denominators, measured versus manipulated variables, uncertainty, replication status, and generalization limits.
7. Move technical detail to an optional research note when it interrupts the main explanation, while keeping qualifications that change interpretation beside the claim.
8. Vary sentence and paragraph length; avoid chains of short sentences, artificial drama, jargon piles, slogan-like contrasts, and repetitive disclaimers.
9. Give illustrations one clear teaching purpose. Simplify labels and structure; remove redundant nested boxes; distinguish a teaching schematic from an established mechanism or empirical result. Every arrow must say something defensible.
10. End with a useful application or a resolved opening question rather than another summary inventory.

## Scientific and editorial boundaries

Read each owned source completely before deciding its revision. Do not substitute global search-and-replace for an editorial pass. Preserve numerical examples, equations, evidence boundaries, meaningful learning objectives, citations, Quarto IDs, and links unless there is a documented reason to change them. Repair or retain explicit anchors when headings change. Do not remove a canonical cross-referenced concept simply to shorten a chapter; shorten, clarify, or relocate its treatment. Check doubtful, high-consequence, controversial, or temporally unstable claims against primary sources and record the evidence. Do not invent studies, quotations, sources, effect sizes, or verification outcomes.

No reduction quota applies. A paragraph that already works may remain. A source recorded as reviewed must actually be read; a figure recorded as visually passed must actually be inspected. Distinguish newly source-verified claims from claims retained after consistency review. Do not promise that all residual errors have been eliminated.

## Shared-work rules

`inventory.json` assigns source and figure ownership. Edit only owned canonical `.qmd` files and owned figures (including their matching PNG fallbacks). Root owns shared figures, part introductions, front matter, appendices, indexes, CSS, shared QA reports, and final builds. Do not edit `docs/`, retired chapters, legacy `.md`, or previous audit snapshots. Do not run full Quarto builds in workers. You are not alone in the codebase: preserve others' edits and send cross-boundary issues to root. No commits, pushes, external messages, or publication.

## Required record for each worker

Write one report `<owner>-report.md` and structured `<owner>-ledger.json` in this audit directory. For each source, record full-read status, before/after word counts, substantive changes, scientific checks/corrections with source URLs, and any unresolved issue. For each owned figure, record semantic review, source and rendered size inspected, visual status, modifications, and caption/alt consistency. Inspect every owned figure individually and in a contact sheet; render changed SVGs to their PNG fallbacks. Retain intended numerical values and verify geometry. Final destination checks are coordinated by root after all edits.
