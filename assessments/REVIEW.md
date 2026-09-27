# Assessment review record

Reviewed 27 September 2026.

## Scope and review

The book contains 280 newly authored single-best-answer items: 210 chapter questions and 70 part-review questions. Each has five alternatives, an explanation for every alternative, a topic/objective tag, an intended difficulty, a cognitive-level tag, and source chapter references. Questions extending the Chapter 2 information-value discussion also link to Appendix A.

The 2025 Behavioral Economics ordinary exam and the 2026 40-question sample exam were inspected privately for format and task style. Their restricted files and exam questions were not copied into this repository.

Independent read-only assessment auditors reviewed all 280 drafts against the chapter sources, then reviewed all 280 revised items. Follow-up checks accepted the revised first two parts, including the response-task item replacing the only lexical near-duplicate. Four initial one-best-answer assumption problems were corrected: expected rather than merely possible regression (C15.03), exhaustive success/failure outcomes (P02.05), and expected-payoff assumptions in mixed equilibrium and risk dominance (C24.05, P04.09).

Final review corrections covered reference dependence versus loss aversion, adverse-selection mechanisms, self-contained prediction terminology, information costs, and one contingent-contract distractor rationale. All reported substantive correctness, ambiguity, and source-support issues were resolved. Review suggestions also strengthened distractors, shortened conspicuous correct options, replaced repeated scenarios, and restored missing learning-goal coverage.

## Follow-up review of answer cues

The author's concern about Chapter 1, Question 5 prompted a fresh read-only audit of all 280 questions. Three independent assessment auditors covered parts 1–2 (95 items), parts 3–4 (90 items), and parts 5–7 (95 items). They examined whether the stem supplied the answer, whether alternatives were plausible and parallel, whether more than one answer was defensible, and whether questions leaked answers to one another. Seventy-five questions were revised; all 75 received follow-up acceptance after the identified corrections. The remaining 205 were accepted without wording changes in this pass.

C01.05 now asks readers to identify evidence against description invariance instead of repeating an observed description effect. Other changes remove conclusion-bearing stem clauses, replace implausible distractors with relevant misconceptions, and ask readers to apply concepts, choose diagnostic comparisons, or distinguish intermediate measures from intended outcomes. Necessary assumptions for probability, payoff, causality, and timing remain explicit. Basic concept-recognition questions remain appropriate in these formative sets.

Final corrections clarified reported experience (C05.02), the prisoner's-dilemma comparison (C25.01), the cancellation-based sales measure (P06.07), and the human-versus-AI forecast comparator (P07.04). C01.05, C21.05, C22.05, and C34.05 were reclassified as medium rather than artificially retaining their original hard labels. No question IDs or correct-answer positions changed. `cue-review-20260927.json` records the revised IDs and final bank fingerprints; `qa-report.json` records automated checks, which supplement rather than replace the independent judgment of item quality.

## Follow-up clarification of descriptive research

After the answer-cue review, the author questioned whether asking why a behavior occurs is descriptive or prescriptive. Chapter 1 now distinguishes the broad descriptive tradition in decision science, which includes explanation and prediction, from narrower methodological classifications of descriptive and explanatory research. It explains why identifying a cause can inform a prescription without determining which change is desirable. The supporting reference is Bell, Raiffa, and Tversky (1988), chapter DOI 10.1017/CBO9780511598951.003, verified against the publisher's record.

C01.01 now classifies two explicit tasks: measuring observed pension choices and developing practical support for better choices. Its five alternatives are parallel pairs of perspectives. A read-only assessment auditor accepted the item and the chapter clarification with no required corrections. The original key position (B), easy difficulty, and understanding objective remain unchanged. This is one additional revision after the 75-item pass above; it does not claim a second review of all 280 items. The final HTML and EPUB pass the 280-item synchronization checks, the book and EPUB checks, and the updated reference checks. The browser check confirmed the new item, its expanded rationale, scoring, and retry.

## Interpretation

The difficulty mix is an editorial estimate, not an estimate from student performance data. Following the cue review, the bank contains 98 easy, 130 medium, and 52 hard questions; four revised questions were reclassified from hard to medium to match their revised tasks. These are formative sets: some ideas recur in new situations across chapter and part reviews. The existing Practice Labs remain the assessment of producing a plan, message, decision record, or agreement; recognizing a good plan in an MCQ is not equivalent to constructing one.

## Reproducible checks

`python3 scripts/build_practice.py --check` checks synchronization. `python3 scripts/qa_practice.py --rendered` checks all source counts, labels, keys, rationales, answer distribution, length cues, lexical duplicates, HTML question/key associations, and EPUB question/answer content. `assessments/qa-report.json` records the latest results. The full book and EPUB checks cover links, numbering, navigation, references, and figures.

Published alternatives use a stable per-item shuffle. The correct-first order in the human-readable source is an editing convention, not the reader-facing order.

## Source-bank fingerprints

| Bank | SHA-256 |
| --- | --- |
| part-1.md | `f6f4b3fcbd19042853a3ff7fa72161c3cb2049f0f8dc5fb93910e39c2b76ad9c` |
| part-2.md | `2b236663df3531f3f972db8a1d5241dee9a1b8fbc23f19146a0a6b12d6a0f347` |
| part-3.md | `f0b506e315a65e07f277a7ad7cedc9c9b6bae37127e98aafde8eadedca374a7c` |
| part-4.md | `cbf56d283db6d8afce0763039d35fe94a809172dc90109be993828dae16f6031` |
| part-5.md | `d145cb3bb1e793afd837e05c079d2a0b188f45bc3666cb0eb373cdc331c85d51` |
| part-6.md | `453fc026b5e0a0f99a7aa189d554b89bcfeb38165988e9ac147c773b2e407fde` |
| part-7.md | `9fdf355ae3f8632331c1e917b35af40da214d2140342f15da3fceab706628229` |

## Reader-flow verification

`ui-checks.json` records the observed browser checks: incomplete sets cannot be submitted; answers remain hidden before submission; mixed and all-correct attempts score correctly; retry clears the attempt; keyboard controls work; and the 390-pixel layout has no horizontal overflow. The EPUB package contains all 280 static questions and 49 answer sections, with valid navigation and links. Its extracted XHTML was visually checked, with same-document link extensions adapted only in the temporary browser preview.

The follow-up cue revision was also checked in the rendered Chapter 1 practice set: the revised question and explanation appear correctly, an all-correct attempt scores 5/5, and retry clears the selections and hides the key. `cue-review-ui-20260927.json` records this targeted check.
