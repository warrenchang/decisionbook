# Chapter 27 news examples and plot style — 21 September 2026

Request: restyle Figure 27.4, keep comparable plots consistent with the book, and replace the election-night example with September 11 futures evidence.

## Delivered scope

- Figure 27.2 (Fed): original 409 vector segments preserved; horizontal outcome label, matching book typography, muted axes and event marker.
- Figure 27.3: September 11 futures replaces election night. The introduction, explanation, exercise and references follow the new case. Old election assets/data remain intact; old fragment IDs are retained as invisible legacy anchors.
- Figure 27.4 (Challenger): all 897 published vector markers replotted; distinguish firms by both color and shape. The original price/opening-price ratios are expressed as percentage changes, exactly `100 × (ratio − 1)`. This makes the unit clearer without changing the underlying comparison. No lines span gaps in trades.
- Figure 27.5 remains unchanged. The other plots match its navy/blue/teal palette, simple sans-serif type, light axes/grid, and restrained in-figure text. An empirical-plot convention is added to `QUARTO_EDITING_GUIDE.md`.
- All chapter text from “What market efficiency…” through the end of the substantive chapter is unchanged, except the requested news-timing exercise. Election-only Associated Press/Kalshi/Yahoo references are removed and the 9/11 Commission report added; the master references are synchronized.

## Source and accuracy

### Challenger

Primary source: Maloney & Mulherin (2003), *Journal of Corporate Finance*, 9, 453–479, Figure 1, printed p. 458. Author-hosted PDF: https://maloney.people.clemson.edu/challenger.pdf . Its SHA-256 is `5dce53e551f377895546821b29d6d718353fc290838b237e9d8118dc24c217ed`.

`extract_challenger.py` reads every plot marker from the original PDF vector objects on zero-based page 5. The source frame locates hour 11–17 and ratio 0.86–1.02. Four path types identify the circle, diamond, triangle and square markers. All source markers, including repeated/overlapping ones, are retained: Lockheed 225; Martin Marietta 167; Rockwell 232; Morton Thiokol 273. This is reproduction of published graphical coordinates, not access to the original Francis Emory Fitch transaction records. The extracted coordinates and calibration are saved in `challenger-vector-points.csv` and `challenger-extraction.json`.

The source paper's Table 2 and note 8 verify the distinction between the NYSE halt (11:52–12:44) and the Nasdaq trade at 12:36. The source markers reproduce the gap. The caption explains the opening-price denominator; the daily returns in the main text continue to use the previous day's close.

### September 11

The immutable input is `audits/ch27-finance-lecture-20260921/image6.tiff`, SHA-256 `c3ce9ecc2a744b7c4a22657d20fc7267bb6cbd801476aa9a097efde635d38bf8`, extracted from slide 12 of the supplied lecture and attributed there to Siegel (2008), Figure 13-1. The plot is an **approximate trace of the published image**, disclosed in the caption and alt text. Original numerical price observations were not obtained.

The generator thresholds the price stroke separately from the lighter grid and masks the source annotations. It joins touching dark runs in adjacent columns. Narrow vertical runs are retained explicitly, preserving the extreme fluctuations instead of reducing them to averages or fitted curves. Source tick calibration: x94–1710 = 08:43–09:15; y17–1005 = 1,105–1,060 index points. No curve smoothing or artificial price observations are introduced. All retained source-ink pixels are within one source pixel of the plotted geometry. `september11-digitized-geometry.csv` holds drawing segments, not a reconstructed dataset for statistical analysis; `september11-extraction.json` records the method and calibration.

Impact times (08:46, 09:03 US Eastern) were verified against the 9/11 Commission's Chapter 9: https://9-11commission.gov/report/911Report_Ch9.htm . They identify events rather than an exact instant at which every trader learned the news. The text distinguishes the initial uncertain interpretation from the broader meaning of the second impact, and does not assert millisecond response or isolate a causal economic channel.

### Fed

The existing lecture's `slide11.xml` still supplies the original two vector paths; all 409 source segments are rescaled by the same mapping as the earlier plot. No price values are inferred from the vertical dimension. The original opening and closing labels and the announcement marker are preserved. Only presentation changes.

## Reproduction and checks

Generate the SVGs using the current shared builder:

```sh
MPLCONFIGDIR=/tmp/ch27-figure-mpl /tmp/ch27-figure-venv/bin/python scripts/build_finance_news_figures.py
NODE_PATH=/Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules /Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node audits/ch27-news-figures-20260921/render_fallbacks.cjs
```

If recovering Challenger coordinates from the downloaded paper, use `extract_challenger.py /path/to/challenger.pdf` with PyMuPDF. The renderer requires NumPy, Pillow and Matplotlib; the pixel-fidelity screen additionally uses SciPy. The PNG fallbacks and 800/390px inspection images are generated from final SVGs with Sharp.

Direct inspection covers the source charts, all three final plots at 800px, dense/new plots at native size, and new plots at 390px. The figure labels are readable at the ordinary desktop width; narrow HTML uses the book's existing 900px SVG reading pane. EPUB supports image enlargement. A prior browser policy blocked local-file previews, so no alternate browser route was attempted; no fresh browser screenshot or native EPUB reader pagination is claimed.

HTML Chapter 27, the HTML references page, and the EPUB are rendered sequentially. Delivery checks verify current image bytes, numbering 27.2–27.5, captions/alt text, removal of reader-facing election material, the preserved Figure 27.5 hash, and matching staged/delivered EPUBs. Repository checks and hashes are recorded in `validation.json` and adjacent QA logs. No commit or push is performed.
