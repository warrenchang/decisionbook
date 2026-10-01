# Figure-caption review — 30 September 2026

Reviewed all 108 figure captions in the 69 configured book sources. Revised 28 captions across 19 sources to remove redundant descriptions of visible lines, colors, panel arrangements, and labeled values. The requested sentence in Figure 15.2 is removed. The editing guide now records this caption rule.

The review preserves interpretive claims and details that cannot be inferred visually: study populations and comparisons, units and denominators, error-bar definitions, fitting methods, unlabelled reference-line meanings, schematic/simulated status, and sources. Alternative text, figure assets, data, identifiers, and surrounding prose are unchanged. The ledger records every caption and the before/after text of each revision; `PASS` means no caption change was needed, not a complete visual or scientific re-audit of the figure.

## Verification

- Full HTML and EPUB builds completed. An initial book-QA run overlapped HTML regeneration and found temporarily missing generated files; after the render completed, book QA passed with 0 errors and 0 warnings.
- Source, HTML, and extracted EPUB float-reference QA passed: 69 sources, 108 figures, 169 tables, 0 issues. See `float-reference-qa.json`.
- All 108 HTML captions and 107 EPUB captions are present. The hollow-face animation retains its existing HTML-only publication condition. All 28 revised captions match the final text in both editions; see `rendered-caption-qa.json`.
- EPUB release QA passed with 0 errors. EPUB checks were structural/textual; no native EPUB-reader visual inspection is claimed.
- Reviewed static figure contact sheets, source labels where needed, and the Challenger figure separately. Browser inspection covered Figure 15.2 at desktop (1280 × 720) and phone (390 × 844) widths, Figure 21.2 at phone width, and Figure 27.7 at desktop width. Captions wrap without clipping; the habit threshold and trading-classification details remain readable. Temporary viewport changes were reset and the review tab closed.
- Verified that all 19 manuscript-file diffs consist only of the reviewed caption replacements; no figure assets or alternative text changed. `git diff --check` passed. Restored the existing executable mode of `docs/parts/part-1.html` after the full render.

No commit or push performed.
