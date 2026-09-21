# Book-wide y-axis title placement — 21 September 2026

The user requested vertical y-axis titles for all plots throughout the book. The inventory covers all 99 distinct figure assets referenced by the canonical book configuration. Seven figures required nine title changes. Other plots already used vertical titles or had no separate y-axis title. Category labels, panel titles, legends, x-axis labels, and the intentionally unlabeled Chapter 30 plots retain their meaning and orientation.

## Changes

- Finance: moved the Fed, September 11 futures, and earnings-drift measures from plot headers to vertical y-axis titles, with suitable left margins and shorter canvases. Updated both generators.
- Framing: placed both dependent measures beside the axes, retaining sample information above each panel. Percent units appear in the second y-axis title, so its tick labels now show numbers without repeated percent signs.
- Prospect theory: rotated both conceptual y-axis titles beside their existing axes.
- Culture and communication: moved the cortisol and accuracy measures beside the y-axis. The tone-decoding panel keeps its subject heading.
- Added the convention to QUARTO_EDITING_GUIDE.md.

## Verification

See inventory.csv for the complete scope ledger and validation.json for source/output hashes. Source and extracted data hashes match their pre-edit values. All non-text geometry in the four hand-maintained SVGs is unchanged. The generated plots use the same source paths/coordinates; only title placement, margins, and canvas dimensions changed. The already-correct Challenger SVG also remained byte-identical.

All seven revised figures were visually inspected at 900px and 390px widths. No labels are clipped or collide; dense multi-panel text remains small at phone width and can require zoom. These checks inspect rendered image assets, not a live browser or native EPUB reader. Publication build and package checks are recorded separately in publication-checks.json.
