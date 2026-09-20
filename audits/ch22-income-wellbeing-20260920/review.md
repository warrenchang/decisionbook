# Chapter 22: income and well-being

Revised the income section and Figure 22.2 to distinguish life evaluation from emotional well-being, both measured through self-reports. Explained that the 2010–2021 disagreement concerned the income pattern of emotional well-being, and that the 2023 collaboration reconciled it through measurement ceilings and differences across the happiness distribution. Retained the 2024 reanalysis with its actual estimated threshold. Removed the two requested closing sentences and shortened the caption.

The figure now uses the requested author–year headings, full measure labels, and consistent 22-unit text (20-unit axis labels). The 2010 evaluation and 2021 average-experience lines are straight on the schematic log-income axes. All curves remain schematic. The canonical SVG is explicitly protected as hand-maintained in `scripts/build_new_chapter_figures.py`; its historical builder is not an active source. Regenerated the PNG from the final SVG using the standard browser renderer.

Primary sources checked:

- Kahneman and Deaton (2010): https://doi.org/10.1073/pnas.1011492107
- Killingsworth (2021): https://pmc.ncbi.nlm.nih.gov/articles/PMC7848527/
- Killingsworth, Kahneman, and Mellers (2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10013834/
- Bennedsen (2024): https://doi.org/10.1016/j.econlet.2024.111730

Verification:

- Affected HTML and complete EPUB rendered successfully.
- Source QA: zero errors or warnings; reference check: 1,038 unique references; EPUB QA: zero errors; rendered float-reference check: zero issues.
- SVG text-bounds check: all 11 text elements contained within their panels. Inspected the final PNG and rendered HTML at 1,400- and 390-pixel viewports. The figure displays at 820 pixels on desktop and 900 pixels inside the existing phone scroll pane; no page overflow.
- Inspected the extracted EPUB in a browser at a 390-pixel viewport; image loaded and the existing scroll pane preserved readable labels. Also checked image loading at 900 pixels. This is browser inspection of the EPUB content, not a device-specific e-reader test.
- Verified the EPUB embeds the final SVG, HTML assets match the canonical SVG/PNG, and removed phrases are absent from the chapter source, HTML, and search index. Figure numbering remains 22.2. `git diff --check` passed.
