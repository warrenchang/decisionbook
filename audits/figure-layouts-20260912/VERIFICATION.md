# Chapter 1 restoration and Figure 2.1 phone layout

Date: 2026-09-12

- Figures 1.1 and 1.2: restored the SVGs and PNGs byte-for-byte from commit `227f62e`. Captions and explanatory prose remain compatible. Their original landscape layouts use contained horizontal scrolling on small screens.
- Figure 2.1: preserved the four decision-building questions, enlarged supporting text to 30 SVG pixels, wrapped headings, and used a 760 × 1190 portrait canvas. Supporting wording makes opportunity cost and information value explicit. The footer notes that earlier steps can be revisited.
- Removed the Chapter 1 redraws from the compact-figure generator so regeneration preserves the restored originals. The general text normalizer already excludes them. The generator now owns Figure 2.1; its other nine outputs were unchanged.
- Rebuilt the full HTML book and downloadable EPUB. All six HTML figure assets match their sources; all three final SVGs are embedded in the EPUB.

## Verification

- Canonical source and HTML QA: PASS, 0 errors and 0 warnings.
- Rendered HTML: all 118 figure placements passed at desktop and 390-pixel widths.
- EPUB package QA: PASS. Rendered EPUB: all 116 figure placements loaded at 768- and 390-pixel widths with no reported page overflow.
- Figure 2.1 fits without horizontal scrolling at 390 pixels: minimum text size 13.02 pixels in HTML and 14.76 pixels in EPUB.
- Figure 2.1 SVG text geometry: no overlapping text blocks or text outside the canvas. Arrow endpoints attach to the four box boundaries.
- Visually inspected both restored Chapter 1 figures in HTML and EPUB and Figure 2.1 at phone width in both formats. SVG and PNG appearance also inspected.
- `git diff --check`: passed.

The EPUB visual check uses Chromium rendering of packaged XHTML, not a native EPUB reader. Screenshots and exact asset hashes accompany this record. No commit or push was performed for this change.
