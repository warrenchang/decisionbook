# Personal stories and note boxes

## Scope

Reviewed first-person candidates across all 62 configured book sources, separating author experiences from quotations, imagined dialogue, exercises, and generic first-person explanations. Revised six chapters. Existing anecdotes concern bodily urgency (4), the author's daughter counting (8), a fall reinterpreted as a somersault (12), a holiday price increase (17), and breakfast choices (40). Added the user's amusement-park account in Chapter 12 and cola-replacement account in Chapter 21. All seven stories use expanded note boxes with titles beginning “From my experience”.

## Editorial decisions

- The park account now uses five minutes and includes the daughter's occasional reminder to leave. Chapter 40 links to the full account rather than repeating the former ten-minute version. The framing discussion connects genuine choice, autonomy, and carrying out a self-chosen plan, while distinguishing choice over timing from choice over departure.
- The general autonomy explanation is supported by the book's existing Deci and Ryan (2000) reference, also added to Chapter 12's bibliography. Verified against the authors' PDF, especially pp. 234 and 238: https://www.selfdeterminationtheory.org/SDT/documents/2000_DeciRyan_PIWhatWhy.pdf. The story remains a personal observation rather than a demonstration of a particular mechanism.
- The cola account reports drowsiness and heavy meals as cues, access as friction, sparkling water as an experienced replacement, and a push-up as a proposed response whose feasibility depends on context. It expresses the author's wish to reduce cola without inserting a general medical claim about all zero-sugar drinks.
- Kept the daughter-counting photograph inside its personal-experience box. Preserved figures, captions, existing anchor identifiers, and relevant surrounding research. Left quotations and hypothetical examples in their original roles.

## Verification

- Full HTML and EPUB builds completed successfully.
- Book QA: 0 errors, 0 warnings. Reference synchronization: 1,028 unique references, passed. EPUB release QA: 0 errors, including internal links.
- Browser checks passed for all seven expanded note boxes across six chapters at 1,280 px and 390 px: correct labels, loaded images, and no horizontal overflow. Visually reviewed the park story on mobile, cola story on desktop, and counting photograph on mobile.
- Verified all seven personal-story boxes in EPUB; new story text appears in search; superseded ten-minute wording and the old “personal illustration” title are absent.
- Corrected two assumptions in the one-off browser audit: use canonical pages rather than redirects, and allow Quarto's hidden accessibility label “Note”. Neither required changes to the book.
- Removed unrelated generated attribute-order and file-mode churn after confirming identical HTML structure/content or identical file bytes.
- No commit or push performed.
