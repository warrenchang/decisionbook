# Build and quality-assurance scripts

The checked-in Markdown files and the prebuilt `docs/` website are the canonical release sources. A student-facing deployment does **not** need Python, Pandoc, Node, Quarto, or any other generator.

## Release checks

Run the structural release audit from the repository root:

```bash
python scripts/qa_repository.py
```

The command rewrites `QA_REPORT.md` and `qa-report.json`. Publish only when the report says **PASS**.

The optional browser-interaction audit checks search, dark mode, responsive navigation, figures, tables, chapter navigation, the references page, the complete-book page, and the EPUB:

```bash
pip install playwright beautifulsoup4
playwright install chromium
python scripts/browser_qa.py
```

It rewrites `browser-qa.json` and stores screenshots under `qa-screenshots/`.

## Source-conversion provenance

`base_docx_conversion.py` and `source_conversion_pipeline.py` preserve the original DOCX-to-Markdown extraction logic. They require the original source files at the paths named inside the scripts and reproduce an earlier conversion layer, not every subsequent editorial revision in this release. The finished Markdown chapters, part pages, appendices, figures, citation audit, and prebuilt HTML are therefore the authoritative release assets.
