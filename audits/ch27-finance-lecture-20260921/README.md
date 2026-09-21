# Chapter 27 lecture integration — 21 September 2026

Request: simplify Figure 27.1 to the existing euro-note photo; begin with rapid responses to news; integrate BE09. Behavioral Finance - election and futures; organize a coherent chapter.

## Reading sequence

1. Earnings puzzle and photo-only €20 question (Figure 27.1).
2. Empirical price discovery: scheduled Fed surprise, continuous election-night updating, and dispersed information after Challenger. September 11 futures provide a brief comparison.
3. The information sets in EMH; distinguish fast response, no abnormal net return, and correct fundamental valuation; costly information.
4. Earnings drift and the size/value/momentum/reversal evidence, including growth versus shareholder returns. Move the existing anomaly comparison into the main text.
5. Joint tests, risk benchmarks, implementation and publication; strict arbitrage versus risky convergence; Palm/3Com and CUBA.
6. Valuation, feedback, historical bubbles, experiments, and diagnostic dashboard. The entire existing span from “How feedback can sustain a price bubble” through the systemic-crisis discussion is unchanged byte-for-byte.
7. Investor behavior, analysis methods, trading costs, diversification, compounding, a decision memo, and exercises.

`slide-coverage.csv` maps all 80 slides, including hidden slides. Repeated tables/figures are consolidated, quotation collages and classroom logistics omitted, and the financial-intermediation productivity series excluded as a separate question. The existing bubble history and experimental evidence remain fully developed.

## Figures and reproducibility

- Figure 27.1 uses `figures/finance-euro-note-found.png` directly. No image generation or photo modification. Its cached source was verified against the current Git-index blob `16736116861f0051b300cb433f2897bc44bf7c77` before restoring the unavailable local bytes. The old composite remains untouched and unused by this chapter.
- `finance-fed-announcement.svg`: `build_figures.py` preserves all 409 move/line segments of the exact lecture's two source-vector paths in `slide11.xml`. It rescales published graphical geometry, not a newly inferred numerical time series. Minute-scale evidence is not used to claim millisecond reaction. Primary source: McKinsey Global Institute (2013), Exhibit 12, p. 25, https://www.mckinsey.com/featured-insights/employment-and-growth/qe-and-ultra-low-interest-rates-distributional-effects-and-risks ; policy verified at https://www.federalreserve.gov/newsevents/pressreleases/monetary20130918a.htm .
- `finance-election-night.svg`: raw Kalshi minute closes and Yahoo ES=F hourly **opens**, aligned in America/New_York time. Data copies in `data/` match the lecture's source SHA-256 hashes. `data/election-plotted.csv` contains every plotted observation. The 0–100-cent probability-contract axis avoids the lecture's zoomed scale. The month panel is omitted to keep the comparison focused; election-night prices already display uncertainty and updating. `numerical-checks.json` records counts, sustained threshold and 2.1047% futures change. First 95-cent close separately confirmed at 23:30 November 5; sustained from 00:51 November 6 through 07:00. The display ends 06:00. News-call comparison verified against AP's own chronology; it is not treated as first public information.
- `finance-challenger-intraday.png`: byte-identical extraction of `ppt/media/image9.png`, Maloney & Mulherin (2003), Figure 1. Caption distinguishes the opening-price graphical baseline from previous-close daily returns and distinguishes NYSE halt from Nasdaq trade. Verified against https://maloney.people.clemson.edu/challenger.pdf .
- `finance-earnings-drift-evidence.png`: byte-identical extraction of `ppt/media/image12.png` from slide 20, the original-looking historical plot rather than the lecture's alternate redraw. Study conclusion verified at https://doi.org/10.1016/0304-405X(82)90003-4 . No curve digitization or manufactured observations.
- Fama–French international result verified against the final published abstract (7.68 percentage points, 1975–1995, 12/13 markets), not the earlier working-paper figure of 7.60. McLean–Pontiff's 97 predictors and 26%/58% declines verified against the published abstract.
- CUBA description checked against Thaler (2016), pp. 1588–1589. The prose uses December 2014 rather than reproducing the source's mistaken December 18 announcement date. It does not assert that the fund's underlying Caribbean holdings could never benefit from changed policy.
- The hypothetical 52-week example explicitly assumes independent equal-probability +80%/-60% outcomes and full reinvestment. Exact arithmetic is in `numerical-checks.json`; it is not empirical IPO data.

Rebuild SVGs using a Python environment with matplotlib:

```
MPLCONFIGDIR=/tmp/ch27-mpl /private/tmp/coopetition-replication-venv/bin/python audits/ch27-finance-lecture-20260921/build_figures.py
```

PNG fallbacks were rendered from the final SVGs using the bundled Node runtime's `sharp`, SVG input density 180. The script adds accessible SVG title/description elements. Direct source images were inspected at native size. A 390px source contact sheet exposed small source-chart labels; the two historical PNGs therefore use the existing `.wide-illustration` class, which provides the book's 800px horizontal reading pane on narrow HTML screens. Existing CSS gives SVGs a 900px pane. EPUB figures support enlargement; native-reader pagination was not inspected.

## Build provenance and limitations

OneDrive timed out on cloud-only source files. A fresh read-only GitHub clone in `/private/tmp/ch27-render-20260921` supplied matching committed bytes for 219 cloud-only source files. Every fallback file matched the current working repository's Git-index blob; there were zero unmatched sources. All 228 accessible current files were overlaid, including the edited chapter and new figures. `build-inputs.json` records this inventory. Current source files in the working repository were preserved.

HTML and EPUB were built sequentially in that isolated copy. Verified generated files were delivered back to docs/ and _epub/ using atomic replacement because in-place writes to cloud-only outputs stalled. Delivered HTML and both EPUB copies match the validated hashes. The browser URL policy rejected the local HTML preview; no alternate browser route was attempted. Verification therefore includes direct figure inspection, HTML/EPUB structural and asset checks, numerical checks, and repository QA, but not a browser screenshot of final layout or native-reader pagination. The first QA was run while the full HTML build was still relocating outputs and reported missing pages plus missing metadata on two new SVGs. Metadata was fixed, builds completed, and final checks rerun; final reports supersede that intermediate result.

No commit, push, or external publication was performed. Final verification details are recorded in `validation.json` and the accompanying QA reports.
