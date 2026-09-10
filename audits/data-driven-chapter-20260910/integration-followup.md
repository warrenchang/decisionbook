# Chapter 42 integration follow-up — September 10, 2026

The author requested removal of the separate AI architecture and a clearer explanation of the final chapter's significance and connections to the rest of the book.

## Editorial changes

- Removed the original Figure 42.1 placement. Chapter 42 now links to the existing normative decision loop, Figure 1.1, in its prediction/valuation discussion and closing synthesis. Figure 1.1 itself is unchanged.
- Added “Why this is the final chapter,” connecting attention and framing, prediction and calibration, valuation and well-being, authority and negotiation, and design and learning to AI-supported decisions.
- Strengthened the Chapter 41 transition and book-closing hiring example. Added focused forward links in Chapters 1, 6, and 15 and revised the Preface and Part VII introduction.
- Retained the two numerical illustrations, now Figures 42.1 and 42.2. Removed the withdrawn architecture from the active figure generator and responsive-style exceptions. Its original assets and initial review screenshots remain as earlier-draft records, without a reader-facing placement.
- A separate reviewer checked the new connections and the normative/descriptive distinction. The final prose explicitly calls Figure 1.1 a normative framework and includes implementation between choice and outcomes. No new empirical findings or citations were introduced.

## Verification

- Full HTML and EPUB builds completed; Chapter 42 HTML was refreshed after the final wording adjustment.
- Source/HTML QA: zero errors and zero warnings. EPUB package, numbering, internal links, freshness, and staged/released-copy checks: zero errors.
- Reference synchronization: 820 unique chapter-and-appendix references; unchanged by this revision.
- Both remaining numerical SVGs reproduce byte-for-byte from the revised generator.
- Full responsive figure audits: 115 HTML placements and 114 EPUB placements, each tested at two viewport widths, with zero issues. The stale HTML count guard was updated after checking the configured source inventory: 114 Markdown image declarations plus the HTML cover.
- Targeted Chapter 42 checks at HTML 1440/390 and EPUB 768/390 pixels confirmed two illustrations, correct 42.1/42.2 numbering, removal of the prior diagram, no page overflow, and two references resolving to the original Figure 1.1. Navigation to that shared destination was tested in both formats. Screenshots and measurements are in `rendered-integration/`.
- The new explanatory section, closing section, surviving figures, and shared figure destination were visually inspected. EPUB inspection used the extracted book with its packaged CSS; reader-specific implementations can differ.
- `git diff --check` passed. Existing user changes and obsolete generated-figure deletions were preserved. No commit, push, or publication was performed.
