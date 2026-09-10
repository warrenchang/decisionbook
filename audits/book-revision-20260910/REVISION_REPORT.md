# Whole-book editorial revision — 10 September 2026

The habit chapter established the editorial direction: start with an ordinary situation that raises a question, develop the explanation before introducing more terminology, vary the sentence rhythm, and make each paragraph and figure earn its place. This pass applies those principles across the canonical book.

## What changed

- **Stronger narrative openings.** Chapters begin with a decision, puzzle, experiment, or interaction that gives the reader a reason to continue. Recurring examples carry explanations forward where useful; the book does not force every chapter into one identical story template.
- **A clearer order of explanation.** New terms arrive when they answer an established question. Sections distinguish observation, interpretation, prediction, valuation, and causal explanation without repeatedly restating the whole framework.
- **Less repetition.** Removed overlapping definitions, inventories of mechanisms, repeated loop-location boxes, duplicated warnings, and routine closing checklists. Retained meaningful learning goals, practice tasks, cross-chapter reminders, equations, and necessary qualifications.
- **A more manageable reading path.** Moved useful technical extensions and long research catalogues into optional notes. Qualifications that change the interpretation of a result remain beside the claim.
- **More natural prose.** Developed examples in connected paragraphs, replaced ambiguous abstractions with specific descriptions, and varied sentence length rather than relying on strings of short sentences.
- **Simpler illustrations.** Reduced redundant labels and nested boxes, clarified arrow meanings, separated reading routes from causal models, and distinguished teaching schematics from empirical findings. Corrected quantitative diagrams where needed and regenerated the affected PNG fallbacks.
- **More dependable evidence.** Corrected model assumptions, numerical labels, overextended study interpretations, bibliographic inconsistencies, and current evidence-status notices. Fictional examples are identified as illustrations.

## Coverage and scale

The review covered all **41 chapters, seven part introductions, six appendices, the preface, reading and evidence guides, concept index, About page, and consolidated references**. All 59 authored sources were read completely; the 60th source is the generated bibliography, checked against the deduplicated union of the local reference blocks.

The already calibrated habit chapter was reviewed and retained, with navigation repairs. The other 40 chapters received substantive editorial changes. All **112 unique illustrations, including the cover**, received individual and contact-sheet inspection; **60 were revised**, and 52 were retained after review.

Approximate chapter text declined from **158,303 to 129,795 words**, an **18.0% reduction**. The same counting method was applied to the saved baseline and final sources. This includes optional notes, captions, tables, and equations, and excludes YAML, local reference sections, fenced code, HTML tags, and URLs. Moving technical material into optional notes additionally reduces the main reading path without deleting that material. No reduction quota was imposed.

The [final coverage record](final-coverage.json) contains file-level review coverage, final hashes, and before/after counts. Worker ledgers preserve their handoff state; this final record includes subsequent integration and navigation repairs.

## Consequential scientific corrections

- **Deadline evidence:** Chapter 19 and Appendix F now report the official **2 September 2026 retraction of Ariely and Wertenbroch (2002)** and distinguish that notice from the negligible-effects replication. The original paper no longer supports a deadline-spacing prescription.
- **Moral reminders:** Chapter 7 and Appendix F distinguish the 2024 expression of concern from a retraction or a finding of fraud; corrected the replication authors and kept the replication result separate from research-integrity concerns.
- **Evidence-status map:** Independently checked all 20 Appendix F entries against primary papers, official notices, author repositories, or primary institutional abstracts. Narrowed the Macbeth replication to the task actually tested; qualified the Many Smiles pen task, marshmallow attenuation, ego-depletion estimates, and money-priming comparisons. Removed an opportunity-cost participant count because the source reports conflicting totals.
- **Formal and quantitative claims:** Clarified considered versus feasible alternatives, utility assumptions and units, weak versus strict Jensen inequalities, loss-aversion conditions, and probability-weighting restrictions. Corrected median/mean labels in the mental-accounting evidence and uncrossed schematic income-quantile curves.
- **Causal interpretation:** Distinguished placebo-group change from an identified placebo effect, an information-throughput comparison from measured attention loss, and fictional outcomes from study results. Choice-overload moderators now distinguish an effort-minimizing goal from uncertain preferences.

Sources and exact verification scope are recorded in the [chapters 1–14 report](chapters_01_14-report.md), [chapters 15–28 report](chapters_15_28-report.md), [chapters 29–41 report](chapters_29_41-report.md), [independent Appendix A/E/F review](appendices-a-e-f-independent-scientific-review.md), and [cross-book evidence consistency check](final-evidence-consistency-check.md). This is a complete editorial and consistency pass with targeted primary-source verification, not a systematic review of every cited literature or an independent reconstruction of every published dataset.

## Reproduction and publication checks

The clinic-reminder simulation, Schelling teaching run, and publication-selection simulation reproduce from their declared inputs. The selection example still contains the same 2,000 estimates and 328 selected studies; the raw simulated CSV and JSON are byte-for-byte unchanged. Both histogram panels now use common quantitative scales and explicit within-panel denominators. See [calculation checks](simulation-checks.json) and the [independent reproduction](appendices-a-e-f-calculation-check.json).

Source checks cover canonical membership, required learning sections, images and alternative text, SVG metadata and PNG fallbacks, connector geometry, cross-reference IDs, local links, and the exact bibliography union. The consolidated bibliography contains **798 unique records**.

The HTML and EPUB were rebuilt from the revised sources. Destination checks inspect every configured page and illustration at desktop/tablet and phone widths. Wide diagrams use contained horizontal reading panes on narrow screens; compact diagrams fit the screen. Browser checks of extracted EPUB XHTML do not establish identical behavior in every reading application.

Final results are recorded in [source QA](../../QA_REPORT.md), [EPUB release QA](../../EPUB_QA_REPORT.md), [HTML figure QA](../rendered-figure-qa.json), [EPUB figure QA](../rendered-epub-figure-qa.json), and the [actual HTML link audit](final-html-link-audit.json). All final checks pass: source QA, EPUB package and navigation, all HTML/EPUB figure placements, and 7,597 local HTML references including 2,083 fragment targets. The [independent HTML review](final-html-independent-review.md) inspected 25 final desktop/mobile screenshots. Representative destination screenshots and individual/contact-sheet figure records are retained in this audit directory.

## Reviewing this pass

- Read the [rebuilt book](../../docs/index.html) or [EPUB](../../docs/Decision-in-the-Making.epub).
- Review source changes in the working-tree diff. The baseline commit is `d0a1f75d5b6584cf738c0a6de94290b0b70dab36`; [before.zip](before.zip) preserves the original canonical sources and referenced assets.
- Use the [editorial brief](EDITORIAL_BRIEF.md) to distinguish a book-wide preference from a local exception. For further comments, identify the passage, describe the reading problem, and state the desired change; mark successful passages **KEEP** when their treatment should be preserved.

The canonical `.qmd` and SVG sources remain the editing sources. Generated HTML, EPUB, and PNG fallbacks provide the reviewable publication outputs.
