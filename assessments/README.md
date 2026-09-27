# Book practice questions

The blueprint in `blueprint.json` fixes coverage before item drafting: five questions for each of 42 numbered chapters and ten for each of seven parts (280 questions). Chapter sets focus on their own learning goals. Part reviews revisit every chapter in the part through new applications and comparisons. Appendices are reference material and do not receive separate sets.

All items use five alternatives and one best answer, following the short scenarios, conceptual distinctions, and explicit calculations used in the Behavioral Economics exams. The questions are newly written; restricted exam questions are not reproduced here.

## Blueprint and authoring

Most chapters have two easy, two medium, and one hard item. Chapters 1, 21, 22, and 34 have two easy and three medium items following the answer-cue review. Each part has two easy, six medium, and two hard items: 98 easy, 130 medium, and 52 hard overall (35.0%, 46.4%, 18.6%). These are intended difficulty levels, not estimates from student response data. Most items require application or analysis. Every chapter has equal question weight; each item receives one point in its set.

Canonical items live in `bank/part-N.md`. Each heading records ID, topic/objective, intended difficulty, cognitive level, and source chapter numbers. The stem supplies all assumptions. Exactly one `+` choice is correct; four `-` choices represent plausible errors. The text after ` | ` explains each option. Correct-first authoring is only an editing convention: the generator reproducibly shuffles all alternatives before publication.

Run `python3 scripts/build_practice.py` after edits; `--check` detects stale generated includes. Run `python3 scripts/qa_practice.py` to check counts, tags, keys, duplicates, answer positions, length cues, and rendered HTML/EPUB when present. Independent assessment review is required before release. No response data are collected or sent anywhere.

## Reader experience

Each chapter ends with a five-question practice set before its references. Each part ends with a separate ten-question review page. In HTML readers answer the whole set, then select **Check answers** to reveal the score, correct choices, and explanations for every alternative. **Try again** starts a fresh attempt. The EPUB presents questions first and a linked answer section afterward so readers can finish before checking. Without JavaScript, the web book offers a collapsed answer key for the same self-check workflow.
