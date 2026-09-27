# Assessment review record

Reviewed 27 September 2026.

## Scope and review

The book contains 280 newly authored single-best-answer items: 210 chapter questions and 70 part-review questions. Each has five alternatives, an explanation for every alternative, a topic/objective tag, an intended difficulty, a cognitive-level tag, and source chapter references. Questions extending the Chapter 2 information-value discussion also link to Appendix A.

The 2025 Behavioral Economics ordinary exam and the 2026 40-question sample exam were inspected privately for format and task style. Their restricted files and exam questions were not copied into this repository.

Independent read-only assessment auditors reviewed all 280 drafts against the chapter sources, then reviewed all 280 revised items. Follow-up checks accepted the revised first two parts, including the response-task item replacing the only lexical near-duplicate. Four initial one-best-answer assumption problems were corrected: expected rather than merely possible regression (C15.03), exhaustive success/failure outcomes (P02.05), and expected-payoff assumptions in mixed equilibrium and risk dominance (C24.05, P04.09).

Final review corrections covered reference dependence versus loss aversion, adverse-selection mechanisms, self-contained prediction terminology, information costs, and one contingent-contract distractor rationale. All reported substantive correctness, ambiguity, and source-support issues were resolved. Review suggestions also strengthened distractors, shortened conspicuous correct options, replaced repeated scenarios, and restored missing learning-goal coverage.

## Interpretation

The difficulty mix is a design target (35% easy, 45% medium, 20% hard), not an estimate from student performance data. These are formative sets: some ideas recur in new situations across chapter and part reviews. The existing Practice Labs remain the assessment of producing a plan, message, decision record, or agreement; recognizing a good plan in an MCQ is not equivalent to constructing one.

## Reproducible checks

`python3 scripts/build_practice.py --check` checks synchronization. `python3 scripts/qa_practice.py --rendered` checks all source counts, labels, keys, rationales, answer distribution, length cues, lexical duplicates, HTML question/key associations, and EPUB question/answer content. `assessments/qa-report.json` records the latest results. The full book and EPUB checks cover links, numbering, navigation, references, and figures.

Published alternatives use a stable per-item shuffle. The correct-first order in the human-readable source is an editing convention, not the reader-facing order.

## Source-bank fingerprints

| Bank | SHA-256 |
| --- | --- |
| part-1.md | `becb925f392e8acf226f4182cbc8c21889631fcb254d78ce7c2f32f7b38f2fd6` |
| part-2.md | `08dd0705762d496641b4951c40614ad230a0ba2fb860c4cceb51221df60c3c23` |
| part-3.md | `1b467c730e1894941c208abd618d8b5b9dc7ccf9de881e7564f0e3e68d3d385d` |
| part-4.md | `aee210d9aade6cdc957a69fa4071e52d6479b9f19f94676d16ccfe1693c85829` |
| part-5.md | `90359544fd11e05e4bad735a62381c0441a38260d2fd54440a069f5214503d71` |
| part-6.md | `2082a1ca5987308e5721a593360fc68111d9120b502b22bd39e5391bea1b7f24` |
| part-7.md | `ce4c6e7e2904a5c4c7b24d42077d311d137b247aa39dc9911c02aad8d18518f2` |

## Reader-flow verification

`ui-checks.json` records the observed browser checks: incomplete sets cannot be submitted; answers remain hidden before submission; mixed and all-correct attempts score correctly; retry clears the attempt; keyboard controls work; and the 390-pixel layout has no horizontal overflow. The EPUB package contains all 280 static questions and 49 answer sections, with valid navigation and links. Its extracted XHTML was visually checked, with same-document link extensions adapted only in the temporary browser preview.
