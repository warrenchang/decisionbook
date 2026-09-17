# Subsequent axis cleanup — 2026-09-17

Removed the axis titles, tick marks, and numerical tick labels from Figure 30.1. Retained the four panel headings, plain axis lines, and the shared-observations note. Compacted the layout to 760 × 676 and used the freed space for wider plots. Every panel uses the same coordinate transformation. The caption and alternative text explain that the horizontal dimension is time and the vertical dimension is a synthetic outcome.

Verified exact equality of all per-panel data, fitted coefficients, residuals, and numerical scale limits against the immediately preceding source JSON. Five text elements remain; none extends outside the SVG canvas. Refreshed the PNG from the final SVG. HTML and packaged EPUB SVG bytes match the source, as does the HTML PNG fallback.

Inspected the native PNG and final HTML at 1280px/390px, plus extracted EPUB content at 768px/390px. No label clipping or horizontal page overflow was observed. EPUB browser inspection used a byte-identical HTML copy of the packaged XHTML with its CSS and SVG, not a dedicated e-reader. Targeted HTML render and full EPUB render succeeded; book QA passed with zero errors and warnings; EPUB QA passed with zero errors. No commit or push was performed.

This presentation update supersedes the earlier geometry and output hashes; the least-squares verification remains applicable.
