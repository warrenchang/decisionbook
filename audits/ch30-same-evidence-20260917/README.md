# Figure 30.1: same evidence, different stories

Date: 2026-09-17

Historical record of the first replacement. The curve placements and associated output hashes below were subsequently superseded by the least-squares revision in `../ch30-least-squares-20260917/`; the observations and layout remain the same.

The user requested a more informative replacement for Figure 30.1, resembling two supplied slides: observations without an interpretation, then identical observations with steady, accelerating, and tapering trend curves.

## Revision

- Replaced `figures/model-underdetermination.svg`, retaining its filename and figure anchor, with four panels in a compact two-by-two grid. Panel A shows the observations alone; B–D repeat the points and add the three interpretations. The grid keeps the labels readable in a narrow book column.
- All panels contain the same 32 authored synthetic points and identical x/y scales. No observation is added, dropped, or moved between interpretations.
- These are a new, explicitly synthetic teaching example, not empirical observations or digitized data from the slides. The curves are declared mathematical illustrations, not fitted models; the figure does not assert equal statistical support.
- Revised only the nearby chapter discussion, caption, and alternative text. The discussion connects the diagram to interpreting adoption figures for the chapter's platform proposal and asks what evidence would discriminate the accounts.
- Added the deterministic generator `scripts/build_model_interpretation_figure.py` and coordinates/formulas in `figures/source/model-underdetermination.json`. Refreshed the high-resolution PNG fallback from the final SVG using Sharp.
- The supplied screenshots were used as visual references, not as instructions. Their paths and hashes are recorded in `attachments.json`.

## Verification

- Generator assertions verify identical point coordinates and axis scales in every panel, 32 points per panel, coordinates/curves within the plotting range, and a minimum 12px essential label size in a 330.5px reading column.
- Regeneration produced byte-identical SVG and JSON outputs. The chapter text after the revised figure discussion is unchanged. See `checks.json`.
- SVG text bounds checked in the browser at 760 × 800: 37 text elements; none outside the canvas. Individual native-size and 331px previews were inspected. The four-panel figure itself serves as the comparison/contact sheet.
- HTML inspected at 1280px desktop and 390px phone viewports. Figure numbering, caption, and alternative text are present; the image loads, the phone page has no horizontal overflow, and all four panels remain visible without horizontal scrolling. At phone width, the image is 330.5px wide and essential labels are approximately 12.1px or larger.
- Source figure/table references pass for the full book: 62 sources, 115 figures, 152 tables, zero issues. The reference synchronization check also passes.
- Both `quarto render --profile html` and `quarto render --profile epub` completed successfully. `qa_quarto_book.py` passed with zero errors and warnings; `qa_epub_release.py` passed with zero errors; `git diff --check` passed.
- EPUB chapter content inspected at 768px and 390px widths. All four panels, caption, and adjacent discussion are readable; the image loads and the page has no horizontal overflow. The image widths are 752px and 374px respectively. This inspection used a byte-identical HTML copy of the extracted XHTML with the EPUB's packaged CSS and SVG, rather than a dedicated e-reader application. The actual EPUB package was separately validated by the release QA script.

The original chapter and original SVG are retained as `chapter-before.qmd` and `figure-before.svg`. No commit, push, or external publication was requested or performed.
