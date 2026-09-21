# Figure 27.4: compact legend and vertical axis label

The four company legends now share one row. The price-change label is beside the y-axis, rotated 90 degrees, and the figure height decreases from 6 to 5 inches at the same width. The plotting area retains nearly its previous height.

The change is reproduced in `scripts/build_finance_news_figures.py`. Every one of the 897 source markers was checked against the revised SVG axes transformation. The source coordinates, company markers, colors, scales, and trading gaps are unchanged. The other news figures and extraction files retain their previous hashes.

The high-resolution PNG fallback was regenerated from the final SVG with Sharp, using input density 72 and output width 3780 pixels; the output is 3780 by 2250 pixels. Inspection images at 800 and 390 pixels are retained here. The 800-pixel reading size has a single legend row, readable text, and no clipping. The narrow overview is small; the existing HTML and EPUB rules retain an 800-pixel horizontal reading pane for this figure.

HTML and EPUB were rebuilt. Their Figure 27.4 assets match the final source files. Book QA passed with zero errors and warnings, and EPUB QA passed with zero errors. Structural and asset checks supplement the image inspection; no new browser screenshot or native EPUB-reader pagination check is claimed.

Numerical checks, asset hashes, and the EPUB image location are recorded in `validation.json`.
