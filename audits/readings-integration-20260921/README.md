# Readings incorporated into the book

Implemented 21 September 2026 following approval of the four priority additions in `audits/readings-coverage-20260921/recommendations.md`.

| Location | Addition |
| --- | --- |
| Chapter 5 | Greenwald et al.'s blinded subliminal-tape study, distinguishing advertised content, measured change, and perceived improvement. |
| Chapter 13 | Link from masked-cue processing to the Chapter 5 experiment. |
| Chapter 15 | Oskamp's case-history study, the separate changes in confidence and accuracy, and a link to Chapter 42's independent testing principle. |
| Chapter 42 | Research lens on using bargaining-process records and unstructured measurements to discover predictive behavioral patterns; link from intervention benefits to the new methods note. |
| Appendix D, Running an Experimental Study | Research lens on honest subgroup estimation, independent discovery and estimation samples, group-average effects, and limitations. |

Five verified references were added: Greenwald et al. (1991), Oskamp (1965), Camerer (2019), Athey (2019), and Athey and Imbens (2016). The master reference list contains 1,069 unique works. Optional priming and positive-self-statement candidates remain outside this implementation.

## Scientific review

The source checks and independent review found no actionable defects. The text preserves these boundaries:

- The tape study's 237 participants completed both assessments. General pre/post gains do not establish a causal placebo effect. One replication included additional conditions, so no uniform 2 × 2 design table was added.
- Oskamp's confidence means rose from 33.2% to 52.8%; accuracy changed from 26.0% to 27.8%, without a significant first-to-final improvement. The small, single-case study does not establish that additional information is generally harmful.
- Camerer's bargaining results concern held-out prediction, not identified psychological mechanisms. The source's reversed conditional probabilities in its ROC explanation were not reproduced.
- Honest subgroup estimation concerns conditional group-average effects. Separate data reduce a source of selection bias but cost precision and do not repair an invalid causal design or establish individual effects.

## Build and verification

Completed full HTML and EPUB builds with `quarto render --profile html` and `quarto render --profile epub`. Build logs are retained here.

- `scripts/sync_references.py --check`: pass, 1,069 unique references.
- `scripts/qa_quarto_book.py`: pass, zero errors and zero warnings.
- `scripts/qa_epub_release.py`: pass, zero errors.
- `scripts/qa_float_references.py --rendered --epub-dir /tmp/readings-integration-epub-20260921/EPUB`: pass, zero issues.
- Targeted delivery checks: new passages present in HTML and EPUB; three new anchors unique; corresponding HTML search entries present. See `html-delivery.json` and `delivery-validation.json`.
- Whitespace check passed for the edited sources and master bibliography. Existing whitespace in earlier generated finance SVG changes was outside this task.

Review included the prose in context and the generated callout structure. No new browser screenshots were taken for these text additions.

The before copies and `source-before.json` preserve the starting state. Concurrent edits to Chapters 21 and 39 appeared during final verification; they were left intact and are recorded separately in `delivery-validation.json`. The temporary staged EPUB disappeared during that concurrent activity, so final checks used the stable canonical release in `docs/Decision-in-the-Making.epub`. The latest combined release passed the checks above. No source readings were edited and no commit or push was performed.
