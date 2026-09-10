# Final HTML: independent link and visual review

**Passed.** This review used the final HTML build containing the tested cross-format title anchors and the restored callout anchors. No remaining source correction is requested.

## All-page local-link audit

- All **60 configured HTML pages** are present and match the independent source inventory.
- **7,597 local references** checked: 6,884 hrefs and 713 src references.
- **2,083 actual element-fragment checks** passed against rendered HTML/SVG IDs or legacy named anchors.
- **Zero** missing targets, missing fragments, duplicate IDs, or files changing during the audit.
- 540 external or nonlocal references were deliberately excluded. CSS URL expressions, srcset, JavaScript navigation, external destinations, and the semantics of non-HTML resource fragments are outside this checker.

Machine-readable result and rendered-file SHA-256 snapshot: `final-html-link-audit.json`. Reusable checker: `audit-final-html-links.py`. Its fixture tests cover normalized relative paths, directory indexes, queries, percent-encoded Unicode, base URLs, named anchors, text directives, SVG IDs, external links, and deliberately broken links.

## Independent desktop and phone inspection

Opened the final rendered files in a clean headless Chrome context at **1440 × 1080** and **390 × 844**. Inspected all **25 saved screenshots**, covering the opening prose and a representative figure with its caption and surrounding discussion on each of these six pages:

| Page | Representative figure | Result |
| --- | --- | --- |
| Preface / index | Master decision map | Opening scene and cover wrap correctly; map, return arrow, framing statement, caption, and surrounding prose remain readable. |
| Part I | Three-question reading route | Heading, introductory paragraphs, three nodes, connectors, and follow-up questions remain clearly ordered. |
| Chapter 4 | Predictive-processing diagram | Expectations and signals converge on perception; action/sampling feedback and qualifications are visible. The wide diagram uses deliberate horizontal scrolling on a phone. |
| Chapter 21 | Four-element habit loop | Cue, impulse, action, and outcome form a circle; the dashed learning return and caption retain their meaning at both widths. |
| Chapter 40 | Choice-environment diagnostic map | Five questions fit on a phone without overlap; the caption distinguishes the map from a universal psychological sequence. |
| Appendix F | Research-selection diagram | The research stages, connecting arrows, evidence-status opening, and distinction between failed replication and fabrication remain readable. |

No unloaded image, unintended page-wide horizontal overflow, overlapping figure labels, or hidden opening title was observed. The final captures explicitly wait for page load and reset scroll to the top; this prevents a capture artifact from obscuring a title behind the sticky navigation.

The mobile Chapter 4 figure retains a **900 px** image inside a **331 px** horizontal reading pane. The pane remains inside the text column and pans through its full **569 px** range. Both ends were inspected. This is an intentional reading requirement, not an assertion that the whole diagram fits simultaneously on a phone. The other five sampled diagrams fit the narrow column.

Screenshots: `final-html-independent-screenshots/`. Dimensions, selected image paths, loading status, scroll geometry, and screenshot paths: `final-html-independent-visual-metrics.json`. Reproducer: `audit-final-html-visual.cjs`.

## Cross-format navigation repair

The first actual-HTML audit found 30 broken fragment links. Six vanished callout-title targets now reside on surviving callout DIVs, with distinct title IDs. The 21 chapter-title references retain their original fragments; matching anchors are explicitly excluded from EPUB with `content-visible unless-format="epub"`. The exact repair was first tested in a small Quarto book, confirming one target ID and a resolved link in each output format. The previous bare-QMD approach was rejected because those links remained literal in EPUB.

The Appendix C link from the reading guide now targets its existing ethical-audit anchor, and its route-table heading reads “Suggested route.” All prose was preserved apart from that authorized header change. Exact records: `rendered-fragment-repairs.json`, `cross-format-title-link-repairs.json`, and `title-anchor-cross-format-fixture.json`.

Root independently reports the final EPUB package check passing with zero errors. This worker's destination visual review covers the six HTML pages above; full EPUB visual and broader figure checks belong to root's separate verification.
