# Section hierarchy review: configured appendices

Reviewed the seven appendices listed in `_quarto-html.yml`, including their main-text prose, worked examples, research and activity boxes, mathematical sections, and navigation tables. Retired Markdown appendices were excluded. Technical distinctions and reusable tools need navigational headings even when shorter than an ordinary chapter section; these were not flattened mechanically.

| Configured appendix | Decision and rationale |
| --- | --- |
| A — Rational Choice and Decision Analysis | Unchanged. Main sections introduce distinct formal objects or analytical operations. The probability, weight, and joint-sensitivity subsections distinguish different calculations, so their separate headings are useful in this reference appendix. Job-offer examples are already integrated. |
| B — Evolutionary Explanations of Value, Choice, and Rationality | Integrated “Optimally irrational?” into “Rationality has more than one benchmark,” retaining `optimally-irrational`. The book discussion and evaluation checklist apply the distinctions just developed; the existing transition already establishes that relationship. Removed the redundant child headings “Sapolsky's backward clock” and “Bennett's five proposed breakthroughs” from research boxes already titled “Causes across timescales” and “A proposed history of cognitive capacities.” Retained `sapolsky-turtles` and `bennett-five-breakthroughs`. All discussion, table content, and qualifications remain. |
| C — Conducting and Writing a Literature Review | Unchanged. Main headings follow the review workflow. The retirement-saving example is already a collapsible supporting research box after the practice plan, not a main section competing with search, synthesis, or writing. Its title remains useful for identifying the transfer example. |
| D — Running an Experimental Study | Demoted “Worked study: from question to report” from a main section to a subsection under “The one-page evidence design card,” preserving its original generated ID as explicit `worked-study-from-question-to-report`. It is a developed application of that record, with a complete declared design, code box, estimate, and interpretation. The numbered methodological steps remain useful navigation within the five phases. The short practice activity is already boxed under “Study and practice,” so it remains there. |
| E — When Evidence Breaks | Unchanged. Main sections separate the mechanisms affecting research credibility. The empirical cases already develop those mechanisms within the prose. The final evidence-status map is a substantial reference resource with two meaningful classifications; its headings are useful navigation. The practice activity is already a subordinate activity box. |
| F — Portable Tools | Unchanged. Main sections group tools by the task they serve; individual tools are already boxed and linked from the tool-selection tables. Their short labels are necessary for finding and using the worksheets, not elevated examples in an expository chapter. |
| G — Index of Major Examples | Unchanged. Recurring cases, the extended example index, and linked videos are distinct lookup resources. Case names belong in this index. |

## Preservation and checks

- Three redundant/book-example subheadings integrated; one main worked-example heading demoted.
- Checked original IDs against `rendered-heading-baseline.json`; retained every existing explicit anchor.
- Compared all seven files with `source-baseline.json` after removing heading lines and standalone anchor lines: all substantive text is identical. Equations, code, studies, numerical results, references, table content, captions, and figures are therefore preserved.
- Reread the affected passages with their surrounding material. Existing transitions remain coherent without the redundant headings.
- `git diff --check -- appendices/*.qmd` passed.
- Rendering and shared QA remain with the root agent. No render, commit, or push performed.

## Display labels for root review

Incoming links still resolve. Two labels in `concept-index.qmd` reproduce removed research-box child headings: line 121 names “Appendix B, Bennett's five proposed breakthroughs”; line 775 names “Appendix B, Sapolsky's backward clock.” To align labels with the visible box titles, the root agent can use “Appendix B, A proposed history of cognitive capacities” and “Appendix B, Causes across timescales,” respectively. No change to the targets is needed. The worked-study title itself is unchanged.
