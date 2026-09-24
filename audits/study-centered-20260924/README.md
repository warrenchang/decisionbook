# Study-centered revision · 24 September 2026

Reviewed all 42 chapters, seven part openers, seven appendices, and front/end matter. Revised 27 chapters and nine other canonical sources. The remaining chapters already led with substantive evidence or formal analysis and were retained after review. This pass builds on the earlier social-influence revision already present in the working tree; `baseline.json` identifies that starting state.

## Editorial changes

The main argument now more consistently proceeds from a question to a study's comparison, finding, interpretation, and limits before drawing a practical lesson. The revisions expand what participants actually did and what the results distinguish, rather than adding citations to unsupported advice.

- Developed experiments on information seeking, divided attention, perception, expectations, expertise, attribution, familiarity, diagnostic reasoning, coordination, culture, persuasion, communication, and negotiation.
- Brought empirical comparisons ahead of practical frameworks in Chapters 5, 30–32, and 39–41. In behavior design, the successful vaccination-planning intervention is paired with the gym-planning null result so that a useful technique does not become a universal prescription.
- Shortened repetitive recommendations, especially in the habit chapter. Longer practical recipes remain available as optional material. Worksheets and mnemonics are identified as teaching or drafting aids where they have not themselves been validated.
- Preserved formal game theory, normative decision analysis, methodological explanation, the approved preface scene, important concepts, and existing scientific qualifications. A formal benchmark does not require experimental validation to serve its stated mathematical purpose.
- Replaced a generic story-processing figure in the reading path with an actual donation experiment. Its old asset and legacy anchor remain available.

## Four new study figures

| Figure | What readers can see | Scientific qualification |
| --- | --- | --- |
| 3.1 · Laptop distraction | Test performance when using a laptop for unrelated tasks, and when seeing others multitask | Separate experiments; reported means, with standard errors derived from rounded published standard deviations |
| 15.2 · Confidence and accuracy | Confidence rises across information stages without a corresponding accuracy gain | One case, 32 judges; lines connect reported means, with no invented uncertainty bands |
| 31.1 · Stories and statistics | Donations to an identifiable child, statistical information, and their combination | Giving is the measured outcome; the two lower means were not statistically distinguished |
| 39.1 · Vaccination plans | Reminder-only versus date-and-time planning prompts | Raw rates and their difference are distinguished from the covariate-adjusted estimate |

All four have captions, alternative text, and discussion in the chapter. Values, denominators, source URLs, and transformations are recorded in [figure-data.json](figure-data.json). The reproducible generator is [build_study_centered_figures.py](../../scripts/build_study_centered_figures.py).

## Coverage and preservation

- [Chapters 1–14](chapters-01-14.md), [15–29](chapters-15-29.md), and [30–42](chapters-30-42.md): chapter-by-chapter changes and reasons for retaining other material.
- [Front matter, parts, and appendices](front-and-end-matter.md): disposition of the other twenty configured sources.
- [Independent scientific review](independent-scientific-review.md): a separate fact check of seven priority descriptions and all four plotted datasets. One wording correction was implemented: a nonsignificant interaction is not proof of independence.
- [Preservation record](preservation.json): no existing reference entries removed in this pass; ten chapter reference entries added, representing nine new unique sources in the master bibliography. Net chapter length increased by 934 whitespace-delimited words, including references, while redundant advice was reduced.
- [Complete canonical-source diff](revision.diff): compares against this turn's saved working tree, not against an older commit that would conflate earlier changes.

This is a book-wide editorial and evidence-grounding review, with primary-source verification of newly developed claims and targeted independent checking. It is not a fresh systematic review of every historical citation. The independent-review record identifies its access limitations.

## Validation

Full HTML and EPUB builds, source/reference checks, local HTML links, rendered figure/table references, and EPUB packaging checks are recorded in [validation.json](validation.json). Visual checks are documented in [visual-qa/README.md](visual-qa/README.md).

No commit or push was performed.
