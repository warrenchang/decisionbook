# Figure 37.2 revision

Request: make the figure more visually appealing, give the axes the same scale,
and make it closer to the lecture illustration.

Reference: `07. Integrative Negotiation.pdf`, PDF page 7 (slide 6), supplied by
the author. The original PDF was read without modification.

The revised figure adopts the lecture's continuous schematic frontier,
northeast value-creation arrow, and two-way value-claiming annotation. It
replaces the previous illustrative discrete menu, rather than smoothing
observations. The caption, alternative text, and adjacent paragraph now explain
that schematic. The separate four-package numerical example remains intact.

Both scores span 0–100 over 520 SVG units (5.2 pixels per score unit); the axis
extensions also have equal lengths. Scores are separately normalized for the
two parties, so matching graphic scales do not establish interpersonal welfare
comparability. The chapter retains that distinction in its existing footnote.
No new empirical claim or data series was introduced.

Canonical builder: `scripts/build_pareto_figure.py`. Both historical DOCX
conversion scripts now call and retain this same builder. They were compiled
but their full conversion pipelines were not run.

Regeneration:

```sh
python3 scripts/build_pareto_figure.py
node scripts/render_svg_png_fallbacks.cjs figures/pareto.svg
quarto render --profile html
quarto render --profile epub
```

The two publication builds must run sequentially. The Node renderer requires
Playwright and a supported local Chrome/Chromium installation.

Verification records:

- `geometry-check.json`: equal scales and axis lengths, correct directions for
  both arrows, connector attachment, and deterministic SVG regeneration.
- `float-source-qa.json`: all source figures and tables retain body references.
- `check-layout.cjs`: reproducible checks and screenshots of the source at 760
  and 340 pixels, plus the actual HTML and extracted EPUB chapter figures at
  desktop and phone widths. Screenshots accompany `layout-check.json`.
- `pareto-before.svg` and `section-before.txt`: the prior figure and local text.

The EPUB visual check uses its extracted XHTML and packaged image in Chrome;
it does not claim testing of pagination in every EPUB reader.

Completed checks: full HTML and EPUB builds succeeded in sequence. Book QA
reported zero errors and zero warnings; EPUB QA reported zero errors; source,
HTML, and EPUB float-reference checks reported zero issues. The packaged EPUB
SVG and the HTML SVG/PNG match the canonical figure bytes. Visual inspection
confirmed clear labels and unclipped arrowheads at native, desktop, and phone
sizes. The smallest figure text is approximately 12.2 CSS pixels in the HTML
phone layout and 13.8 pixels in the EPUB phone layout.

This revision did not stage, commit, or push files.
