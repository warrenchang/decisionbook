# Book-wide removal of redundant qualifications

Baseline: `870e2914810db7cdcaf792306953f493f8871a26`.

Reviewed all 62 configured sources, including the 42 chapters, front matter, part introductions, and appendices. The revision removes repeated denominators, warnings against claims a passage never made, duplicate qualifications, and explanations already supplied by the preceding sentence. Qualifications that change the scientific interpretation remain.

The edit log records 181 sentence, phrase, and transition edits across 42 source files (37 chapters), reducing the source text by approximately 2,400 words. Chapter 26's Asch example now ends with the reported result and citation. Similar edits cover the robot-image study, jam display, vaccination prompt, hypothetical calculations, narrative examples, and repeated cautions about universal effects.

## Verification

- `editorial-qa.json`: exact replay of the edit log from the baseline matches the final sources; no distinct numeric value was lost from any source; displayed equations are unchanged.
- `source-preservation-qa.json`: all reference blocks, authored explicit anchors, and Python examples retained.
- `reading-layers-qa.json`: all 62 HTML sources and 42 EPUB chapters checked; 29 mathematical analysis boxes retained; no main-text chapter mathematics outside optional callouts.
- `qa-quarto.log`: 0 errors and 0 warnings.
- `qa-epub.log`: release package and internal navigation pass.
- `final-floats.json`: 115 figures and 151 tables; no reference issues.
- `layout-qa.json`: revised passages in three HTML chapters and two extracted EPUB chapters pass at 1440 px and 390 px. Screenshots were inspected for paragraph flow, legibility, and wrapping.
- `python3 scripts/sync_references.py --check`: 967 unique chapter-and-appendix references retained.

HTML was rebuilt before EPUB, sequentially:

```sh
quarto render --profile html
quarto render --profile epub
python3 scripts/qa_quarto_book.py
python3 scripts/sync_references.py --check
python3 scripts/qa_epub_release.py
python3 audits/book-redundant-hedging-20260916/check_reading_layers.py
```

`check-layout.cjs` uses Playwright and the installed Chrome. Its EPUB targets point to an extraction of the rebuilt EPUB in `/private/tmp/book-redundant-hedging-epub-20260916`; re-extract that file there before repeating the browser check. EPUB visual inspection used Chromium's XHTML rendering, not native-reader pagination. External embeds were blocked for this prose-layout check.

## Resolved verification findings

The initial layout harness passed a viewport option to `BrowserContext.newPage`, which does not set a per-page viewport. The final harness explicitly calls `setViewportSize` and verifies the actual viewport width; all ten corrected checks pass. The initial results are retained as `initial-layout-qa.json`.

Chapter 13's sole footnote repeated the preceding explanation of masked priming. Removing its call and definition also removed Quarto's automatic `footnotes` section. The anchor audit now records this intentional generated-heading removal and verifies that no authored heading or incoming source link was lost. Initial and final anchor-check results are retained separately.

No commit or push was made for this revision.
