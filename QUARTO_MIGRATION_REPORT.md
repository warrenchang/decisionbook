# Quarto Migration Report

## Changes completed

- Added `_quarto.yml` with the seven-part, 35-chapter book structure.
- Converted canonical manuscript files from `.md` to `.qmd`.
- Added `index.qmd`, `references.qmd`, and `about.qmd`.
- Converted legacy HTML callout boxes to native Quarto/Pandoc fenced callouts.
- Converted chapter illustrations to native Quarto figure syntax with unique figure IDs and alt text.
- Converted the 36 manually numbered table captions to Quarto table captions with unique IDs.
- Replaced part-page HTML chapter cards with editable Markdown links.
- Added `quarto-custom.scss` for textbook typography, figures, references, callouts, and responsive layout.
- Added `preview-book.sh`, `render-book.sh`, and `QUARTO_EDITING_GUIDE.md`.
- Removed the old static Pages workflow that generated failure notifications.
- Preserved the previous static website in `docs/` as a fallback until the first `quarto render`.
- Moved legacy build and QA scripts and reports to `legacy-static-build/`.
- Added an editable draw.io master for the decision-loop figure under `figures-src/`.

## Validation completed

- All 47 `.qmd` files parse successfully with Pandoc.
- Every file listed in `_quarto.yml` exists.
- All local `.qmd` links and figure paths resolve.
- Figure and table IDs are unique.
- No legacy `<aside>`, `<figure>`, or reference `<div>` blocks remain in the `.qmd` sources.

## First local build

Install Quarto, then run:

```bash
quarto preview
```

After inspection, rebuild all publishing files with:

```bash
quarto render
```

The first Quarto render will replace the fallback custom static site in `docs/` with the generated Quarto book.
