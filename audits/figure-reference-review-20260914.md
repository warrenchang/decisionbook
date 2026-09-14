# Figure 9.1 and book-wide table/figure references

## Figure 9.1

Replaced [the project image](../figures/affect-panda-sea-star.png) with an original AI-generated editorial illustration using the built-in image tool. The panda cub rests its tilted head against a tree fork and hugs the branch. Purple and orange ochre sea stars have thick, irregular arms and textured surfaces, guided by the user's two photographic references. The subjects retain equal space in the composition.

The chapter now explicitly refers to Figure 9.1 and asks readers to identify the features that first draw their concern. It separates that response from evidence about conservation outcomes. The allocation exercise remains hypothetical; the image is not presented as evidence that either species deserves more funding. Updated its caption and alternative text, including the image's generated status.

The complete generation prompt, method, and primary anatomy source are in the [prompt record](figure-reference-review-20260914-image-prompt.md). The original generated file is retained; the selected image is saved at the book's existing asset path. Its source, HTML copy, and renamed EPUB image match byte-for-byte: [published-image verification](figure-reference-review-20260914-published-image.json).

## Reference and discussion review

Read every teaching table and figure in the 62 configured sources, covering the preface, reading guide, seven part introductions, all 42 chapters, and appendices. The final inventory contains **116 figures and 146 tables**. All 262 have a numbered reference and meaningful discussion in the same source where they appear.

- Added missing local references to 199 existing numbered items, usually by integrating the reference into an existing explanation.
- Numbered three previously unnumbered items: the focused reading-route table, the portable decision-journal table, and the hollow-face animation.
- Reviewed and, where needed, improved the discussion of the other 60 items. The prose tells readers what to compare, infer, notice, or do, rather than merely saying “see below.”

The animation's reference shares its HTML-only condition. EPUB retains the original-video link and viewing instructions without an unresolved numbered reference. Three legacy anchors for removed tables remain as link destinations, but are not counted as current tables. The cover and author portrait are not numbered teaching figures.

Existing identifiers, table contents—including the raw HTML table—and all bibliographic entries were preserved across all 62 sources. The master bibliography still contains 884 entries. [Preservation record](figure-reference-review-20260914-preservation.json).

Independent readings of changed sentences caught and resolved unclear antecedents in Part II and Chapter 33, two precision issues in Chapter 27, and an awkward figure introduction in Chapter 36. No outstanding issue remains in these reviews: [front matter, appendices, and image](figure-reference-review-20260914-independent.md), [Chapters 15–28](figure-reference-review-20260914-middle-independent.md), and [Chapters 1–14 and 29–42](figure-reference-review-20260914-chapters-independent.md). The [complete ledger](figure-reference-review-20260914-ledger.json) records each item and its final discussion.

## Durable rule and verification

Added **Connect every table and figure to the argument** to the [editing guide](../QUARTO_EDITING_GUIDE.md). The new [reference-coverage checker](../scripts/qa_float_references.py) checks identifiers, local body references, unnumbered teaching tables, and rendered links. Its HTML/source check is integrated into the regular book QA. Captions, alternative text, table cells, and code examples do not count as body discussion. Editorial review remains necessary to judge explanatory quality.

Rebuilt the full HTML book and final EPUB; re-rendered the four pages affected by independent copyediting. Final checks passed:

- **HTML:** 262 numbered items have local prose links; 118 image placements load at desktop and phone widths without reported layout issues. All 2,573 main-content internal links and 685 search entries resolve.
- **EPUB:** all 261 included numbered items have local prose links; 116 image placements load at tablet and phone widths. The sole omitted teaching figure is the HTML-only animation. No unresolved reference remains.
- **Figure 9.1:** inspected individually at native size and in desktop/phone HTML and tablet/phone EPUB; correct numbering, complete image, matching alternative text, and caption below the image.
- **Book and release checks:** zero errors and warnings in book QA; zero EPUB release errors. All existing table data, source IDs, and bibliographic entries remain intact.

Evidence: [combined reference QA](figure-reference-review-20260914-final-qa.json), [HTML visual QA](figure-reference-review-20260914-rendered-figure-qa.json), [EPUB visual QA](figure-reference-review-20260914-rendered-epub-figure-qa.json), [navigation](figure-reference-review-20260914-navigation.json), [HTML Figure 9.1](figure-reference-review-20260914-html-figure-9-1.json), [EPUB Figure 9.1](figure-reference-review-20260914-epub-figure-9-1.json), and [animation](figure-reference-review-20260914-html-animation.json).

EPUB layout was checked through the final packaged XHTML in Chromium, not in every commercial reader. This pass changes the single requested raster illustration and the prose connections; it does not redesign the other figures. Existing user changes were preserved. No commit or push was performed.
