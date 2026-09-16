# Section-heading revision — 16 September 2026

The user identified “Conformity is an outcome, not a mechanism” as misleading and requested revision of similar section titles throughout the book.

Conformity can describe the process of adjusting beliefs, judgments, or behavior toward other people or group expectations. The original heading intended to distinguish observed agreement from the informational or normative influences that produce it, but incorrectly excluded the process meaning. The revised heading is **Why we conform: informational and normative influence**. Chapter 26's definition, learning goal, associated discussion of social proof and information cascades, and concept-index description now use the distinction consistently.

The conceptual check used the [APA Dictionary of Psychology definition of conformity](https://dictionary.apa.org/conformity) and the informational/normative distinction already developed and cited in the chapter (Deutsch and Gerard, 1955). No bibliographic entries were added or changed.

## Scope

- Reviewed the inventory of 1,072 level-two through level-six headings across all 62 configured sources, including all 42 chapters. Recurring labels such as learning goals, practice activities, and references retained their established roles.
- Revised 73 headings across 35 sources to name their topics or conclusions directly, replacing misleading exclusions, vague contrasts, and compressed slogans.
- Updated nine linked heading labels and the conformity description in the concept index: 36 sources changed in this revision overall.
- Preserved the previous, uncommitted prose revision. The compressed source snapshot records the exact state immediately before this heading revision; an exact replay of the three edit logs reproduces every current source.
- Preserved previous public anchors. Existing chapter titles, order, references, figure markup, code, mathematics, and numerical information outside revised headings were retained. The crash heading now explicitly names 1987.
- Rebuilt HTML and EPUB sequentially. No commit or push was performed for this revision.

## Verification

| Check | Result |
| --- | --- |
| Exact edit replay and source preservation | Pass for all 62 sources |
| Revised headings in HTML and EPUB | All 73 present |
| Previous HTML IDs and section links | Preserved; no duplicate HTML IDs |
| Search index | All revised titles present; old title text absent |
| Book QA | 0 errors, 0 warnings |
| Reference synchronization | 967 unique references; unchanged |
| Figure and table references | 115 figures, 151 tables; 0 issues |
| EPUB release checks | Pass |
| Optional mathematics | 29 analysis boxes retained in each edition; no main-chapter text math outside callouts |
| Representative layout | Eight checks across desktop and phone widths passed |

Visual checks covered the Chapter 26 heading and definition in HTML and extracted EPUB XHTML, the revised decision-quality heading in Chapter 1, and a research-callout title in Chapter 6. The desktop and phone Chapter 26 HTML views, Chapter 6 desktop callout, and desktop EPUB view were also inspected directly as images. Native-reader pagination was not tested.

The broader ID check found 14 pre-existing duplicate EPUB callout-wrapper IDs. Each was verified in the preceding committed EPUB (`870e2914810db7cdcaf792306953f493f8871a26`); the heading revision introduced none. They are recorded in `baseline-epub-duplicate-ids.json` and `revision-qa.json` rather than represented as a new regression or silently removed.

## Audit files

- `before-sources.json.gz`, `before-rendered-ids.json`, and `heading-inventory.json`: baseline material.
- `heading-edits.json`, `chapter26-prose-edits.json`, and `index-edits.json`: exact changes.
- `check_revision.py`, `revision-qa.json`, and `source-preservation-qa.json`: reproducible source, heading, anchor, and reading-layer checks.
- `search-qa.json` and `float-qa.json`: search and cross-reference checks.
- `check-layout.cjs`, `layout-qa.json`, and PNG files: representative layout checks.
- `render-html.log` and `render-epub.log`: successful build logs.

The repository-level reports are `QA_REPORT.md`, `qa-report.json`, and `EPUB_QA_REPORT.md`.
