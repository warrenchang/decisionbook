# Quarto Editing and Publishing Guide

The repository is now a Quarto book project. The `.qmd` files are the canonical source; `docs/` is generated output. Do not routinely edit generated HTML files.

## Install

1. Install Quarto from <https://quarto.org/docs/download/>.
2. Install the official **Quarto** extension in VS Code.
3. Open the repository folder in VS Code and trust the workspace.
4. Confirm installation:

```bash
quarto --version
quarto check
```

## Edit with live preview

From the repository root, run:

```bash
quarto preview
```

Open a chapter such as `chapters/01-decision-making-is-a-process-not-a-moment.qmd`. Use **Visual** mode for word-processor-like editing or **Source** mode for precise Markdown editing. Save the file; the browser preview updates automatically.

## Rebuild all publishing files

```bash
quarto render
```

This rebuilds the complete HTML book in `docs/`. GitHub Pages should be configured to publish `main` / `docs`.

## Publish

```bash
git add .
git commit -m "Revise textbook"
git push origin main
```

## Edit a figure

Keep an editable source such as `figures-src/decision-loop.drawio`, export it as `figures/decision-loop.svg`, and run `quarto render`. The same filename lets the chapter update without changing its source.

## Important

- Edit `.qmd`, not `docs/*.html`.
- Do not edit `docs/search.json` or Quarto-generated navigation.
- Run a full `quarto render` before publishing.
- The EPUB download is intentionally not configured. Add an `epub:` format and `book: downloads: [epub]` only when an EPUB is desired.
