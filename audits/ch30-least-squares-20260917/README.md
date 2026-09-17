# Figure 30.1: fit each prescribed shape by least squares

The user requested curves that minimize squared errors and sit more naturally among the observations. This revision supersedes the illustrative curve placements documented in `../ch30-same-evidence-20260917/`.

All 32 synthetic observations, their order, panel layout, colors, labels, and axis limits are preserved. For each of the three previously specified trend shapes, the generator now minimizes the sum of squared vertical residuals in `y = a + b*g(x)` over the intercept `a` and amplitude `b`:

- Steady: `g(x) = x`.
- Accelerating: `g(x) = x**2`.
- Tapering: `g(x) = 1-exp(-x/3.5)`. The time scale of 3.5 is retained from the original illustration and held fixed. The old normalization is absorbed into the fitted amplitude.

These are global least-squares minima for the two free coefficients within each prescribed form, not an unconstrained search over curvature or all possible trend models. Curves are drawn over the observed x range, 0.5–9.7. No observations were changed to balance the signs of residuals.

| Form | Squared error before | Squared error after | Above / below |
| --- | ---: | ---: | ---: |
| Steady | 7,560.54 | 6,864.78 | 16 / 16 |
| Accelerating | 7,290.89 | 6,512.74 | 16 / 16 |
| Tapering | 14,136.31 | 8,447.63 | 17 / 15 |

With a fitted intercept, signed residuals sum to zero up to floating-point precision. Least squares does not require equal counts above and below. The chapter caption and a methodological footnote now state the fitting criterion, fixed shapes, and unequal goodness of fit.

Verification: independently reproduced all coefficients and residual sums of squares with NumPy's `linalg.lstsq`; checked the normal equations, lower squared errors, and unchanged coordinates. See `fit-verification.json`. Regeneration gives byte-identical SVG and JSON. The PNG fallback was refreshed from the final SVG. A native browser check found 32 points in each panel and no text outside the 760 × 800 SVG canvas.

Method reference: [NIST least-squares criterion](https://itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm). The objective is also directly implemented and checked in `scripts/build_model_interpretation_figure.py`.

No commit, push, or external publication was performed.

Final checks: HTML and EPUB rebuilt successfully; book QA passed with zero errors and warnings; EPUB QA passed with zero errors. The final figure and caption were inspected in HTML at desktop/390px widths and extracted EPUB content at 768px/390px widths, with no clipping or page overflow. EPUB inspection used a byte-identical HTML copy of the XHTML with packaged styles and SVG, not a dedicated e-reader. The packaged SVG matches the source exactly. See `verification.json` and `output-hashes.json`.
