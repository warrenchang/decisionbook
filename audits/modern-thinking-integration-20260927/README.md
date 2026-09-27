# Modern Thinking Tools: integration into Decision in the Making

Completed 27 September 2026.

All 100 supplied topic summaries and their reference leads were mapped against the current book. Relevant source-PDF passages and primary studies informed additions in **20 chapters**, with **51 new bibliographic works**, 19 new concept-index entries, and three expanded entries. These 51 works include empirical studies, theoretical papers, reviews, and one published correction; the count is not 51 independent experiments.

## Where the book was enriched

| Chapters | Added discussion and research examples |
|---|---|
| [2](../../chapters/02-structuring-a-decision.qmd), [3](../../chapters/03-limited-attention.qmd) | Artists discovering a problem before solving it; expert entrepreneurs building options from available means; costly efforts to keep doors open; news emphasis and the public agenda. |
| [8](../../chapters/08-intuition-and-deliberation.qmd), [13](../../chapters/13-priming-fluency-and-familiarity.qmd) | Experts classify physics problems by principles; worked examples, self-explanation, and deliberate practice; why retrieving information can improve delayed retention despite feeling harder than rereading. |
| [16](../../chapters/16-risk-and-uncertainty.qmd), [18](../../chapters/18-decisions-from-experience.qmd), [27](../../chapters/27-markets-mispricing-and-bubbles.qmd) | Favorable odds and appropriate stake size; the horizon experiment on exploration; exploration before creative hot streaks; highly skewed stock-market wealth creation. Kelly mathematics remains in a foldable box. |
| [21](../../chapters/21-habits-wanting-and-self-control.qmd), [22](../../chapters/22-deciding-for-a-better-life.qmd), [39](../../chapters/39-behavior-design.qmd) | Own-name self-talk and emotional distance; discretionary time and purpose; when demanding happiness undermines it; cultural differences in happiness pursuit; internalizing the reason for an uninteresting activity. |
| [23](../../chapters/23-strategic-interdependence.qmd), [25](../../chapters/25-cooperation-and-social-preferences.qmd), [40](../../chapters/40-choice-architecture.qmd) | Safelite performance pay, garment-production teams, hidden quality, signaling, and anticipated rescue; Swiss pasture governance and common-pool experiments; how landlords responded to a rent-control expansion. |
| [28](../../chapters/28-social-influence.qmd), [29](../../chapters/29-culture-and-identity.qmd), [34](../../chapters/34-connection.qmd) | Unequal burdens of volunteering for low-promotability work; local academic rank and later choices; network bridges, cross-income friendship, and neighborhood opportunity. |
| [37](../../chapters/37-integrative-negotiation.qmd), [38](../../chapters/38-designing-better-agreements.qmd) | Shared objects that connect people with different purposes; incentives that divert effort toward what is easiest to measure; transferring negotiation principles by comparing cases; bounded discretion during implementation. |
| [41](../../chapters/41-decision-hygiene.qmd), [42](../../chapters/42-deciding-with-data-and-ai.qmd) | Promotion based on the wrong performance measure; surgeon familiarity with hospitals; systems approaches to error; trophy-fish photographs and shifting baselines; corrected debiasing evidence; college-selection comparisons; proxy optimization, goal misgeneralization, automation and new tasks, and a designed AI tutoring experiment. |

Most additions develop existing sections. The examples explain what participants did, what the evidence showed, and why it matters to the chapter's decision problem. Theory, observational evidence, experiments, and practical applications remain distinguishable.

## Coverage and evidence record

- [Complete 100-topic coverage table](coverage.csv)
- [Topics 001–034](topics-001-034.md)
- [Topics 035–067](topics-035-067.md)
- [Topics 068–100](topics-068-100.md)
- [Additional source checks and exclusions](additional-evidence.md)
- [The 51 added reference entries](added-references.json)
- [Source inventory and hashes](source-manifest.json)
- [Integration counts](integration-counts.json)

Already-developed material—such as common knowledge, sunk costs, focusing illusion, Bayesian updating, WOOP, framing, and predictive processing—was retained rather than repeated. Course-specific taxonomies, duplicate anecdotes, unsupported extensions, and specialist detours were excluded with reasons in the topic ledgers. All coordinated handoffs in those ledgers were resolved in the chapter additions above.

The supplied PDF has 2,170 pages. The reference file contains 950 original numbered notes, not 950 distinct research papers. The review maps every guide topic and its reference leads, with targeted checks of original passages and primary research; it is not an independent verification of every note, reader comment, or citation in the compilation. Topic 060 belongs to a different PDF according to the supplied guide, so its named studies were checked directly. All three supplied source files retain their original hashes. Full source text and source graphics were not copied into the repository.

## Verification

Independent read-only review checked the chapter additions for scientific accuracy, narrative placement, redundant caveats, and omitted central mechanisms. Two substantive wording issues were corrected: the definition of moral hazard and the description of sanctioning opportunities in Ostrom's laboratory evidence. A final review passed the agenda-setting, academic-rank, and AI-tutoring additions. Repeated prose following the tutoring comparison was consolidated.

- Full HTML render completed for all 62 configured sources; Chapter 42 was refreshed after final prose consolidation.
- Full EPUB render completed and the released EPUB matches the staged artifact.
- `qa_quarto_book.py`: **PASS**, zero errors and zero warnings; all 42 chapters present; zero unresolved author–year citations.
- `qa_float_references.py --rendered`: **PASS**, 62 sources, 108 figures, 164 tables, zero issues.
- `qa_epub_release.py`: **PASS**, zero errors.
- `sync_references.py --check`: **PASS**, exact union of 1,189 chapter-and-appendix references.
- All 51 added references are present in both their rendered HTML chapters and the EPUB; the final consolidated Chapter 42 prose appears in both formats. See [rendered-content-checks.json](rendered-content-checks.json).
- Desktop and phone checks passed for eight representative chapters (16 page/viewport checks), including opening the Kelly mathematics box. Three screenshots were visually inspected for typography, formula fit, and prose flow. See [visual-qa.json](visual-qa.json).
- All 100 topics have exactly one coverage row; all supplied source hashes remain unchanged.
- `git diff --check`: **PASS**.


The working tree already contained other authorized revisions when this task began. Those edits were preserved. No commit or push was made for this task.
