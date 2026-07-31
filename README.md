# Quarto part-navigation fix

Replace the corresponding files in the root of the Quarto textbook project:

- `_quarto.yml`
- `quarto-custom.scss`
- `parts/part-1.qmd` through `parts/part-7.qmd`

Then stop any active preview, run `quarto render`, start `quarto preview`, and hard-refresh the browser.

The changes:

- add explicit title metadata to every part page;
- prevent part overview pages from consuming chapter numbers;
- set a docked, lightly shaded sidebar with part-level collapsing;
- strengthen part headings, spacing, hover states, and the active-page indicator.
