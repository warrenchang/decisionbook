# Figure information-value review — 19 September 2026

Scope: all 116 Markdown image placements in the configured book sources (including the author portrait). `PASS` in the ledger means retained after an editorial information-value review; it is not a claim that every unchanged figure received a fresh scientific or pixel-by-pixel audit.

- 21 placements removed: 13 chapter diagrams, seven part-opening question diagrams, and the repeated Part VII questions in Chapter 41. Their material remains in prose or existing tables. Original assets remain available, and former figure anchors remain as link targets.
- Figure 26.4 redesigned with illustrative song menus. Both experiments used 48 songs. Experiment 1 used random grids in both conditions, displaying download counts only under social influence. Experiment 2 used random ordering for independent choice and descending download counts for social influence. Six invented songs and counts demonstrate the contrast without claiming to reproduce the original interface.
- 94 placements retained unchanged, including perceptual demonstrations, photographs, data comparisons, and diagrams with useful relationships or sequences.

## Evidence and inspection

Music Lab protocol: Salganik, Dodds, and Watts (2006), original supporting materials, pp. 2–3 and Figures S2–S3: https://www.princeton.edu/~mjs3/salganik_dodds_watts06_som.pdf . Existing chapter citation retained; original sample and analysis details moved from the old figure to a footnote.

The editorial review inspected ten contact sheets and source captions/labels. All 107 unique SVG assets in the original inventory were rendered in Chromium at their native dimensions, with transformed text bounding boxes checked against the canvas; no out-of-canvas text flags remained. This screen cannot certify connector geometry or readability. The redesigned Music Lab figure was additionally inspected individually and in the rendered destinations.

`before-inventory.json` records the starting source inventory. `removed-figures.json` records each removal. `figure-ledger.json` records each editorial decision. `svg-render-screen.json` records native dimensions and bounds checks. Final destination sizes, image loading, overflow, and removed-image checks are recorded by `destination-qa.cjs` in `destination-qa.json`; its screenshots cover the changed Music Lab figure at desktop and phone widths in HTML and EPUB.

Source build: `python3 scripts/build_music_lab_figure.py`. Regenerate its PNG from the final SVG in Chromium (device scale factor 2 for a 1280 × 2180 companion). Rebuild book outputs sequentially with `quarto render --profile html` and `quarto render --profile epub`.

## Final checks

Both full builds passed. Source QA reported zero errors and warnings; the reference index contains 1,028 entries. EPUB package/navigation QA passed. Float-reference checks covered 62 sources, 95 figures and 166 tables, with zero issues. Browser checks covered 252 HTML/EPUB page-and-viewport combinations with no broken images or page-overflow flags. The Music Lab figure was visually inspected in all four destination screenshots; essential labels render at approximately 12 px or larger. All 21 former figure anchors occur once in both HTML and EPUB. `git diff --check` passed.

## Follow-up: former Figure 3.3

At the user’s request, the sensory-worlds image was restored as a newly illustrated four-panel figure on 19 September. The original SVG remains available in the review gallery. With the earlier throughput cards still removed, Quarto numbers the replacement Figure 3.2. Twenty placements from the initial removal set remain removed; the original inventory and QA files above document the earlier snapshot. See `../sensory-worlds-illustration-20260919/` for the new figure’s source verification and display checks.
