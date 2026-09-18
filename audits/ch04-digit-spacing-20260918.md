# Figure 4.1 digit spacing — 18 September 2026

Status: REVISED and verified.

Tightened the visible gaps within 12 and 14 to 2.6 SVG units, matching the separation in the central ambiguous mark. Recentered both number groups around their previous visible centers. Character outlines, central-mark clipping, and both central-mark instances are unchanged. Regenerated the PNG fallback from the final SVG.

Verification:

- Compared character definitions and clipping with the original; verified both new gaps arithmetically.
- Inspected SVG rasterizations before and after at 1200 × 500.
- Rebuilt chapter 4 HTML and the full EPUB. Source and HTML SVG/PNG assets match; the packaged EPUB SVG is byte-identical to the source.
- Inspected HTML at 1280 × 720 and 390 × 844, and the extracted EPUB chapter in a browser at 768 × 1024 and 390 × 844. Narrow layouts retain their existing horizontal figure scrolling; checked both number groups and the central mark. EPUB preview used a byte-identical HTML copy of the extracted XHTML with its packaged assets, not a dedicated EPUB reader.
- Book QA passed with zero errors and warnings; EPUB QA passed with zero errors; `git diff --check` passed.
