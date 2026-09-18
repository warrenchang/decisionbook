# Part VI lecture integration — 18 September 2026

This revision expands Chapters 35–38 using the three supplied 2022 lecture PDFs and four inline screenshots. The four-chapter progression remains foundations → claiming value → creating value → designing and implementing agreements. Existing chapter titles, epigraphs, explicit anchors, and figures are retained.

## What changed

| Chapter | Principal additions |
| --- | --- |
| 35: Negotiation as Joint Decision Design | Everyday interdependence; economic and relational outcomes; high-road/low-road and thumb-wrestling demonstrations; soft/hard/principled approaches; additional skilled-negotiator observations; public audiences and face; individualism/collectivism and power-distance comparisons connected to concrete questions. |
| 36: Distributive Negotiation | Copenhagen and Tom job examples; dream-house reservation value; BATNA improvement and expiry; chilling effects; Chandler/Einstein and campaign-photograph cases; precise and range offers; five range-offer forms; numerical concession and midpoint examples; real-estate debrief. |
| 37: Integrative Negotiation | Vietnamese prunes and processing conditions; unusable compromise example; concrete Camp David framework terms; two-sided preparation; five sources of useful differences; iterative search, agreement and exit decisions. |
| 38: Designing Better Agreements | Full service menu with a test of MESO equivalence; construction incentives; royalties/TV/agent examples; complete MPharm A–E analysis; effort, liquidity and risk; cultural meeting and commitment protocols; mediation/conventional/final-offer arbitration; post-settlement invitation and procedure; advanced seminar exercise. |

The Part VI introduction now previews these examples and connects culture, bargaining and implementation. Ten works were added to the master reference union; synchronization removed none of the existing entries. Additional already-cited works were reused in chapter-local reference lists.

New algebra is in two optional **Mathematical analysis** boxes. The main text gives the reasoning and decisions in words. The boxes use short equations and line breaks for phone readability.

## Coverage and evidence

[Coverage ledger](coverage.md) accounts for all **98 PDF pages and four screenshots**, including repeated material, polls, media prompts, unsupported numerical claims, and corrections. It records the source checks and the reasons for reframing or omitting particular claims. Source facts are distinguished from illustrative assumptions and from simplified classroom adaptations.

The supplied PDFs were read by page-labeled text extraction, with rendered inspection of quantitative, diagrammatic and poll slides. The four screenshots were read directly from the user's inline attachments; the temporary image paths were no longer readable when the final inventory was recorded. No poll results, missing role briefs, film transcripts, scientific evidence, or verification outcomes were invented.

Primary checks concern original papers, author-hosted papers, official institutional sources and the reported anecdote sources. The scholarly matcher checks author/year correspondence; it does not substitute for these claim checks. Culture is presented as a set of possible orientations to investigate, rather than a diagnosis from nationality. Mediation is not assigned a universal success rate or a gendered model of justice. General arbitration is distinguished from final-offer selection.

## Verification records

Final result: **PASS** — 35 integration checks; 48 selected-element layout checks; 984 synchronized master references; no unresolved author–year citations; no Quarto source errors or warnings; no source/HTML/EPUB float-reference issues; and no final EPUB release errors. The final EPUB contains the revised market-research heading and the multiline MPharm calculation. Numerical text and phone equation screenshots were inspected after the final rebuild. File hashes are recorded in `final-artifact-hashes.json`.

- `integration-qa.json`: reservation values, all five MPharm packages, common-probability transfer cancellation, state-dependent incentives, illustrative MESO margins, complete slide-page accounting, source-PDF hashes, title/epigraph/anchor preservation and mathematical-box placement.
- `quarto-qa.log`: canonical source, bibliography, link and structural checks.
- `float-qa.json`: source/HTML/EPUB figure and table references.
- `epub-release-qa.log`: final EPUB package, navigation and release checks.
- `layout-qa.json`, `layout-qa.log`, and `screenshots/`: 12 selected new or expanded elements in HTML and extracted EPUB at 1440px and 390px, including expanded math. Wide HTML tables use the book's existing horizontal scrolling; checks exercise the scroll endpoint. EPUB inspection uses Chrome's XHTML/MathML rendering, not native-reader pagination.
- `render-html.log`, `render-html-ch36-final.log`, `render-html-ch38-final.log`, `render-epub-final.log`: sequential render logs. The two chapter rerenders incorporate the final equation-layout improvements.

Reproduce the integration checks from the repository root:

```sh
python3 audits/part-vi-lecture-integration-20260918/verify-integration.py
python3 scripts/sync_references.py --check
python3 scripts/qa_quarto_book.py
python3 scripts/qa_epub_release.py
python3 scripts/qa_float_references.py --rendered
```

For visual reproduction, extract the final EPUB to a temporary directory and run `check-layout.cjs` with that directory as its first argument, using Node with Playwright available and the configured Chrome executable. Always run HTML and EPUB builds sequentially.

## Workspace scope

Published source changes are confined to Part VI, Chapters 35–38, and the added master references. The publication files were rebuilt in an isolated directory from commit `4986f2b8605223ae7d32efb7f810c0dbca934342` plus this revision. Unrelated chapter, theme, and figure edits remain in the original workspace. The master bibliography in this publication build contains 984 works; the earlier combined editing workspace contained 994. The archived baseline retains only the Part VI source files. The `publish-*` logs record checks of the isolated publication build, and `final-artifact-hashes.json` identifies its files.
