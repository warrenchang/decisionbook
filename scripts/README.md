# Build and quality-assurance scripts

The checked-in QMD files are the canonical book source. The prebuilt `docs/` directory is the student-facing HTML release.

## Release checks

First synchronize the master bibliography and render the Quarto book:

```bash
python3 scripts/sync_references.py
quarto render
```

Then run the canonical source-and-output audit:

```bash
python3 scripts/qa_quarto_book.py
```

The command rewrites `QA_REPORT.md`, `qa-report.json`, `CITATION_AUDIT.md`, and `citation-audit.json`. It checks the 38-chapter order, required learning sections, source/render parity, references, author–year correspondence, links, alternative text, SVG metadata, duplicate IDs, and diagram connectors. Publish only when the report says **PASS**.

For a labeled visual-review set, use the bundled artifact Python runtime (or any Python with Pillow):

```bash
python3 scripts/render_figure_contact_sheets.py
```

## Lecture-slide image coverage

Generate the occurrence-level raw inventory directly from the eight editable PowerPoint packages:

```bash
python3 scripts/audit_pptx_images.py "/path/to/Slides 2026" --out-dir audits/slide-images-raw
```

The inventory includes hidden slides, embedded or linked images, native chart/diagram objects, media hashes, duplicate groups, object metadata, dimensions, and crop data. It is deliberately rights-neutral. After editorial review, `audits/slide-images-reviewed.csv` gives each occurrence a pedagogical role, provenance assessment, rights status, treatment, destination, and completion state.

Validate exact occurrence coverage and rights/treatment consistency with:

```bash
python3 scripts/qa_slide_image_coverage.py
```

The older `qa_repository.py` audits the earlier hand-built static release and is retained only for historical reproducibility.

The optional browser-interaction audit checks search, dark mode, responsive navigation, figures, tables, chapter navigation, the references page, the complete-book page, and the EPUB:

```bash
pip install playwright beautifulsoup4
playwright install chromium
python scripts/browser_qa.py
```

It rewrites `browser-qa.json` and stores screenshots under `qa-screenshots/`.

## Source-conversion provenance

`base_docx_conversion.py` and `source_conversion_pipeline.py` preserve the original DOCX-to-Markdown extraction logic. They require the original source files at the paths named inside the scripts and reproduce an earlier conversion layer, not every subsequent editorial revision in this release. The finished Markdown chapters, part pages, appendices, figures, citation audit, and prebuilt HTML are therefore the authoritative release assets.
