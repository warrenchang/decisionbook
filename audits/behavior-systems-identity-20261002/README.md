# Behavior systems and identity revision

Request: develop scientifically accurate coverage of reducing reliance on willpower, arranging a habit loop, starting small, and motivating change through identity, including “I don't smoke” versus “I am a nonsmoker.”

## Placement and editorial decisions

- Chapter 39 is the primary practical home. Added a repeatable writing procedure; made the existing small-start and anchor discussion visible in the main text; developed identity, the smoking example, and its evidence; updated the learning goals, techniques table, and practice lab.
- Chapter 29 explains identity as beliefs and expectations about the self, with a school intervention and longitudinal smoking evidence. “Internal model” describes psychological representations, not a tested neural mechanism.
- Chapter 21 links the habit mechanism to the procedure and identity discussion without repeating either.
- The procedure is a teaching synthesis of existing concepts, not a separately validated intervention. Deliberate planning and effort still matter. A reliable routine, a checklist, and automation do not necessarily imply habitual automaticity.
- Starting small concerns initiating useful action. The text retains the need to develop skills, increase useful work, and evaluate substantive outcomes. It does not promise a fixed habit-formation deadline or an effect from celebration alone.
- Both smoking statements can express commitment. No direct test of those exact two sentences was located; the book does not rank them by demonstrated efficacy. The studies below concern identities and broader interventions, not that grammatical contrast. No claims from the separate “I don't” versus “I can't” literature were imported.

## Evidence and claim checks

Verified against publisher pages, original articles, or author/institutional copies on 2026-10-02. New bibliography entries are in the relevant chapters and synchronized master references.

| Source | Design and result relevant here | Boundary and use |
| --- | --- | --- |
| Duckworth, A. L., Gendler, T. S., & Gross, J. J. (2016). Situational strategies for self-control. *Perspectives on Psychological Science, 11*(1), 35–55. [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4736542/); DOI 10.1177/1745691615623247. | Conceptual review of intervening before an impulse develops, including selecting and changing situations. | Supports broadening self-control beyond resistance. Does not establish that every environmental arrangement outperforms every effortful strategy. Already cited in the book. |
| Wood, W., & Rünger, D. (2016). Psychology of habit. *Annual Review of Psychology, 67*, 289–314. [Publisher](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-122414-033417). | Review of repeated responses in recurring contexts, automaticity, and interaction with deliberate goal pursuit. | Supports the cue–response account. The writing example distinguishes habitual initiation from deliberative evaluation. Already cited. |
| Oyserman, D. (2009). Identity-based motivation: Implications for action-readiness, procedural-readiness, and consumer behavior. *Journal of Consumer Psychology, 19*(3), 250–260. [DOI](https://doi.org/10.1016/j.jcps.2009.05.008); author copy at USC inspected. | Identity-based motivation account: situations cue identities and their meanings, influencing readiness to act and interpretations of difficulty. | Mechanistic framework, not proof that self-labels reliably change behavior. Already cited. |
| Oyserman, D., Bybee, D., & Terry, K. (2006). Possible selves and academic outcomes: How and when possible selves impel action. *Journal of Personality and Social Psychology, 91*(1), 188–204. [Original article](https://sparq.stanford.edu/sites/g/files/sbiybj19021/files/media/file/oyserman_byeee_terry_2006.pdf); DOI 10.1037/0022-3514.91.1.188. | Randomized school program; 264 consenting eighth graders in three Detroit schools. Future-self work, practical strategies, and interpretation of difficulty versus regular electives; grades and attendance improved over the two school years examined. | Bundled program, specific population; cannot isolate identity wording. Randomization, school-record outcomes, and follow-up checked in the full article. |
| Meijer, E., van den Putte, B., Gebhardt, W. A., van Laar, C., Bakk, Z., Dijkstra, A., Fong, G. T., West, R., & Willemsen, M. C. (2018a). A longitudinal study into the reciprocal effects of identities and smoking behaviour: Findings from the ITC Netherlands Survey. *Social Science & Medicine, 200*, 249–257. [Original article](https://pure.uva.nl/ws/files/33475253/A_longitudinal_study_into_the_reciprocal_effects_of_identities_and_smoking_behaviour.pdf); DOI 10.1016/j.socscimed.2017.12.006. | Cross-lagged observational models; main identity/behavior model N = 1,036. Quitter identity predicted later quit success, and quit success predicted later identity. | Reciprocal prediction is not causal identification. Complete-case selection and partially overlapping cross-validation samples constrain inference. |
| Meijer, E., Gebhardt, W. A., van Laar, C., van den Putte, B., & Evers, A. W. M. (2018b). Strengthening quitter self-identity: An experimental study. *Psychology & Health, 33*(10), 1229–1250. [Publisher article](https://www.tandfonline.com/doi/abs/10.1080/08870446.2018.1478976); [PDF](https://www.tandfonline.com/doi/pdf/10.1080/08870446.2018.1478976); DOI 10.1080/08870446.2018.1478976. | Randomized 2 × 3 writing/expected-support experiment. Analysis included 339 daily smokers completing initial pre/post measures. Weak identity effect; no significant effect on immediate quit intention or smoking outcomes at one/six months. | Null results do not prove all identity interventions ineffective. Expected-support vignettes are not delivered social support. Publisher-indexed article and PDF text inspected; direct HTML open returned 403. |
| van Vliet, M. H. M., Penfornis, K. M., Gebhardt, W. A., von Haeseler, E. F., Chavannes, N. H., Versluis, A., & Meijer, E. (2026). The effect of identity-related interventions on physical activity- and smoking-related identities and behavior: A mixed-methods systematic review. *Systematic Reviews, 15*, 106. [Publisher article](https://link.springer.com/article/10.1186/s13643-026-03103-2). | Nineteen reports describing 20 studies; varied intervention designs, with positive and null findings. | Narrative synthesis; more physical-activity than smoking research. Publication in 2026 is not evidence of comprehensive coverage of studies published through 2026. Used to contextualize, not generalize from, one smoking experiment. |

The two Meijer papers are distinguished consistently as 2018a (longitudinal) and 2018b (experimental) in this book.

## Verification

Completed 2026-10-03:

- Full HTML render succeeded. Chapter 29 was rendered again after refining the transition into the preschool example.
- Full EPUB render succeeded; `python3 scripts/qa_epub_release.py` reported 0 errors. Native e-reader layout was not separately inspected.
- `python3 scripts/sync_references.py --check`: 1,271 unique references, synchronized.
- `python3 scripts/qa_quarto_book.py`: 0 errors and 0 warnings; citation audit reported no unresolved author–year citations.
- Rendered float-reference check: 69 sources, 108 figures, 169 tables, 0 issues. See `float-reference-qa.json`.
- HTML/EPUB text and anchor checks: 24 checks, 0 failures. See `content-qa.json`.
- Browser inspection: the procedure at 1280 × 720; small-start and identity text at 390 × 844; Chapter 39 → Chapter 29 link opened the new passage. Both chapters' page widths matched the 390-pixel viewport without horizontal page overflow.
- Preserved the tracked executable mode on `docs/parts/part-1.html` after rendering. `git diff --check` passed.
- No commit or push performed.
