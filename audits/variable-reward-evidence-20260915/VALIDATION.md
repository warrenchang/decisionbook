# Validation of Chapter 21 variable-reward addition

Date: 2026-09-15

- HTML and EPUB regenerated with `quarto render --profile html` and `quarto render --profile epub`.
- Master references synchronized with `python3 scripts/sync_references.py` (916 unique references).
- `python3 scripts/qa_quarto_book.py`: PASS, zero errors and zero warnings.
- `python3 scripts/qa_epub_release.py`: PASS, zero errors.
- New anchor, main-text link, four reference entries, and EPUB section content verified.
- Callout opened and inspected at 1440-pixel and 390-pixel viewport widths; no horizontal overflow; monetary amounts preserved.
- Desktop and mobile screenshots visually inspected.
- SHA-256 comparison confirmed that Chapter 21 was the only changed source among pre-existing chapters, appendices, and figures during this edit. Existing Chapter 25 edits were preserved.
- Quarto changed file modes while recreating output files; original tracked modes restored for previously unmodified output files, without changing their contents.
- References retain the book's existing plain DOI presentation.
- No commit or push performed.
