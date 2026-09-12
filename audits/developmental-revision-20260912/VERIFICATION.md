# Final verification — 12 September 2026

**Local revised edition: PASS for the checks below.** No commit or push performed.

| Check | Result |
| --- | --- |
| HTML and EPUB builds | Successful; 61 configured source documents, including all 42 chapters |
| Source, figures, citations, required learning sections | 0 errors; 0 warnings |
| Master bibliography | 849 distinct works; synchronized; all source lists and master correctly ordered |
| Reference preservation | 11 works added; none deleted; three Chapter 6 entries retained in Appendix B |
| Legacy anchors and review files | No original explicit anchor lost; six supplied review files match baseline hashes |
| Rendered HTML local links | 8,036 references and 2,901 element fragments checked; no missing targets or duplicate IDs |
| HTML geometry and image loading | 118 placements across 61 pages at 1440 and 390 pixels; 0 issues |
| Focused compact-figure review | All eleven diagrams at both widths; 22 captures inspected; mobile non-title type at least 12.15 CSS pixels |
| Main comparison sections | Six sections visible by default at both widths |
| Portable Tools | All 30 tools display their correct level and category color at both widths |
| EPUB package and content | ZIP, manifest, 42-chapter navigation, mathematics, image alternatives, freshness, and all internal links pass |
| EPUB geometry and image loading | 116 placements across 63 XHTML documents at 768 and 390 pixels; 0 issues |
| Independent EPUB visual review | Twelve captures covering six revised figures inspected; no clipping or caption contradiction |
| SVG reproducibility | All eleven final generator outputs reproduced byte-identically in memory |
| Source/output visual assets | All 117 distinct rendered assets match their retained source bytes |
| Diff hygiene | `git diff --check` passed; incidental generated whitespace and file-mode changes normalized |

The source QA counts 115 unique figures recognized from canonical source markup. The rendered inventory is broader: it includes the generated cover and raw media presentation and resolves 117 unique assets in 118 placements. The source supported placement count is 116 Markdown images, one raw HTML GIF, and the automatic preface cover. EPUB handles cover/media differently; its rendered content count is 116. These are different defined inventories, not missing figures.

The figure ledger states the actual review scope per asset. Eleven priority SVGs were recomposed; the calibration chart was corrected. Other wide SVGs retain contained horizontal reading panes. Neither the mechanical checks nor the contact-sheet pass certify an exhaustive new scientific review of every retained illustration. Extracted EPUB XHTML was rendered in Chromium; native Books and other EPUB readers were not separately tested.

## Delivered files

- Website entry: `docs/index.html`
- Downloadable and staged EPUB: `docs/Decision-in-the-Making.epub` and `_epub/Decision-in-the-Making.epub` (identical bytes; 14.62 MiB)
- EPUB SHA-256: `cf4f48165e29fc2af4ac564e6fb8117c0bd41b921708fced3df3e75b938e76e1`
- Revision summary: `REVISION-SUMMARY.md`
- Complete final source/artifact hashes and embedded check results: `final-verification.json`
- Per-figure disposition and source/output hashes: `figure-ledger.md` and `.json`

The final full HTML build was followed by a Chapter 39-only render for the evidence-map link. Full package/link checks were run on the finished files. The last full HTML geometry run preceded that link-only correction; its figure/body layout was unchanged. The focused figure captures precede the invisible chapter-entry anchors, which add no displayed text. Final EPUB geometry was rerun on the released package.

## Reproduction

Run `python3 scripts/sync_references.py --check`, `python3 -m doctest scripts/sync_references.py`, `quarto render --profile html`, and `quarto render --profile epub`. The post-render script copies the staged EPUB beside the website. Run `python3 scripts/qa_quarto_book.py` and `python3 scripts/qa_epub_release.py`.

Browser checks use `scripts/qa_rendered_figures.cjs`, `scripts/qa_rendered_epub_figures.cjs`, and this directory's `qa-reading-route.cjs` with Node, Playwright, and local Chrome. The EPUB checker takes an extracted `EPUB/` directory and a screenshot output directory. The HTML link audit uses the `configured_sources` and `audit` functions in `audits/book-revision-20260910/audit-final-html-links.py`; the final result is `html-links.json`.

The retained `audit-revision.py` regenerates source/link metrics; `record-final-verification.py` collects finished output hashes and report snapshots. Chapter reports supply primary-source links, numerical checks, and preservation decisions. `INTEGRATION-NOTES.md` records defects discovered and resolved during validation.
