# Qualification cleanup — 10 September 2026

Reviewed all 42 chapters, six appendices, and the remaining configured front matter, Part introductions, and reference/index/about pages: 61 source files in total. The review covered main prose, callouts, table text, figure captions, alternative text, and the wording inside all 109 active SVGs. Five raster illustrations and the cover were also checked.

Removed generic qualifications, repeated warnings, and obvious limits following results. The specific Chapter 42 sentence about the 280-fold cost reduction is gone; the benchmark, dates, and source remain in the result sentence. Important scope details now appear in 37 concise new footnotes. The final pass changes 54 QMD files and removes approximately 10,700 words net.

Preserved reported results, numerical comparisons, null and mixed findings, integrity notices, mathematical assumptions needed to use the models, and all original reference blocks. Independent reviewers checked the chapter groups, the formal-analysis appendix, and the figure changes. Four reused heading anchors were given unique chapter IDs; the concept-index links and renamed Appendix F heading anchor were checked in rendered output.

Updated 62 SVGs and regenerated their PNG companions with Quarto 1.10.18 for book output and Sharp 0.35.4/libvips 8.18.6 for offline rasterization. Removed empty footer boxes and closed the resulting layout gaps. Final data marks and parameter values were independently checked against the pre-edit snapshot. PNGs use a white background and a two-times raster scale. Formatting-only SVG cleanup was verified to produce identical raster bytes.

## Verification

| Check | Result |
| --- | --- |
| Full HTML and EPUB builds | PASS |
| Canonical source/HTML QA | PASS: 0 errors, 0 warnings |
| Master reference synchronization | PASS: 834 unique references |
| Original reference blocks and footnote resolution | PASS |
| Internal links and anchors across 61 HTML pages | PASS |
| Final SVG and PNG copies in HTML output | PASS: 62 pairs |
| EPUB release/package QA | PASS: 0 errors |
| Current edited figure assets packaged in EPUB | PASS: 62 of 62 |
| SVG parsing and identifier checks | PASS: all 109 active SVGs |
| Offline visual review | 62 revised figures; changed layouts inspected individually |
| Final whitespace check | PASS |
| Interactive HTML/EPUB browser preview | BLOCKED by local browser URL policy |

The browser restriction was respected. Offline artifact inspection and structural release checks were completed; no new browser-based destination review is claimed.

The canonical outputs are `docs/index.html` and `docs/Decision-in-the-Making.epub`. Existing unrelated user changes were preserved. No commit, push, or publication was performed.

Detailed records: `book-qualifications-20260910-source-review.md`, `book-qualifications-20260910-figures.json`, and `book-qualifications-20260910-checks.json`. Temporary before/after comparisons, render logs, and previews are under `/private/tmp/book-qualifications/`.
