# Quality-assurance report

**Release status: PASS**

This report was produced by `scripts/qa_repository.py`. A PASS means that the automated release checks found no broken internal links, unresolved bibliography correspondence, missing required chapter sections, inaccessible chapter figures, or invalid EPUB container structure.

## Release summary

| Check | Result |
|---|---:|
| Rendered chapters | 35 |
| Editable Markdown chapters | 35 |
| Appendices | 2 |
| Chapter body words, excluding reference lists | 114,250 |
| Average chapter length | 3,264 words |
| Shortest / longest chapter | 1,127 / 6,002 words |
| Chapter diagrams / unique assignments | 35 / 35 |
| Responsive chapter tables | 36 |
| Global bibliography entries | 453 |
| Chapter references absent from global bibliography | 0 |
| Global references absent from chapter lists | 0 |
| Duplicate global references | 0 |
| Internal links checked | 3,247 |
| Broken paths / broken fragments | 0 / 0 |
| Images missing alternative text | 0 |
| Tables lacking headers / responsive wrappers | 0 / 0 |
| Pages with duplicate IDs | 0 |
| Search-index entries | 46 |
| EPUB ZIP integrity | Pass |
| EPUB mimetype and package structure | Pass |
| Release-blocking errors | 0 |
| Non-blocking warnings | 0 |

## What was checked

- Sequential chapter numbering and parity between editable Markdown and rendered HTML.
- Presence of learning goals, key ideas, study-and-practice material, and chapter-specific references in every chapter.
- Correct previous/next chapter navigation after the structural reordering.
- Local paths and fragment identifiers across the complete prebuilt site.
- Alternative text, captions, file existence, table headers, responsive overflow behavior, duplicate IDs, and heading hierarchy.
- Exact set equality between the union of chapter reference lists and the global bibliography.
- Machine-readable citation-audit status, search-index integrity, GitHub Pages deployment files, and EPUB container validity.

## Citation scope

The citation checks establish author–year/bibliography correspondence and ensure that the published reference list contains only works represented in chapter reference lists. They do not independently reproduce every study or establish that every source supports every clause at systematic-review depth. That remains a scholarly editorial judgment, particularly for contested or context-sensitive effects.

## Issues

No automated issues were found.
