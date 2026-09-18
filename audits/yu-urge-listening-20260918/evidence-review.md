# Yu, urges, and listening before problem-solving

Date: 2026-09-18. Scope: Chapters 21 and 34, the verified-understanding index entry, references, and generated HTML/EPUB. Existing uncommitted work was preserved. Baselines in this directory record the chapter state after the earlier BRAIN revision and before this addition.

## Placement and interpretation

- Chapter 21 introduces the traditional Gun–Yu contrast after acceptance and urge surfing, immediately before the BRAIN practice. It connects allowing a feeling with choosing where one's action goes. It does not claim that dams never work, that Yu's story is established engineering history, or that allowing an urge guarantees its disappearance.
- Chapter 34 develops the analogy within the existing section on verified understanding. It retains the project-manager case and uses the colleague's correction to move from an inaccurate interpretation to a checked account of event, felt impact, and concern.
- The bridge to problem-solving depends on sufficient shared understanding, not complete calm, agreement, or compulsory emotional disclosure. Fairness, dignity, and trust are presented as substantive parts of the problem.
- The later section Support without trapping attention makes the limit of the water metaphor explicit: emotion need not be discharged as if it were accumulated fluid. The added anger experiment supports distinguishing listening from ruminative venting; the existing co-rumination discussion remains intact.
- The existing conflict observer prompt now asks for confirmation or correction of the felt impact and concern before evaluating the proposed solution.

## Primary-source checks

| Reference | Verified source/design | Supported use | Boundary |
| --- | --- | --- | --- |
| Legge, J. (Trans.). (1879). *The sacred books of China: The texts of Confucianism*, Part I, Sacred Books of the East vol. 3 | [Title page](https://sacred-texts.com/book/the-shu-king-shih-king-and-hsiao-king/shell/title-page) confirms translator, date, and volume. [The Yî and Kî](https://sacred-texts.com/book/the-shu-king-shih-king-and-hsiao-king/shell/book-iv-the-yi-and-ki), pp. 57–58, describes Yu opening passages, deepening channels, and conducting water toward the seas. [The Great Plan](https://www.sacred-texts.com/cfu/sbe03/sbe03031.htm), pp. 139–140, describes Gun's damming and failure, followed by his son Yu. | A traditional narrative illustrating the change from blocking to providing a route. | These are literary accounts, not contemporary documentation of Yu's actions or evidence for a psychological mechanism. Modern pinyin Gun/Yu replaces Legge's Khwăn/Yü spelling in the chapter. |
| Weger, H., Jr., Castle Bell, G., Minei, E. M., & Robinson, M. C. (2014). *The relative effectiveness of active listening in initial interactions*. International Journal of Listening, 28(1), 13–31. DOI 10.1080/10904018.2013.813234 | [Publisher text and abstract](https://doi.org/10.1080/10904018.2013.813234): 115 participants interacting with 10 trained confederates using active listening, advice, or simple acknowledgments. | Active-listening recipients reported feeling more understood than recipients in either comparison condition. | Does not establish that every emotional conflict needs the same sequence, that listening guarantees resolution, or that active listening was superior to advice on all outcomes. The chapter identifies initial encounters explicitly. |
| Bushman, B. J. (2002). *Does venting anger feed or extinguish the flame? Catharsis, rumination, distraction, anger, and aggressive responding*. Personality and Social Psychology Bulletin, 28(6), 724–731. DOI 10.1177/0146167202289002 | [Original paper on the author's university site](https://websites.umich.edu/~bbushman/PSPB02.pdf): randomized rumination-plus-punching, distraction-plus-punching, or quiet control after insulting essay feedback. Final analyzed sample: 600. The supposed other participant did not exist. | Rumination-plus-punching produced greater reported anger and more punitive noise choices than quiet control. Noise intensity and duration were standardized and combined; both showed the same result pattern. | The main text describes a supposed provocateur and choices of punishment, not harm delivered to a real opponent. It does not equate talking about a concern with aggressive venting or claim that emotional expression generally worsens distress. |

The publisher's main page/PDF intermittently returned a 403 for Weger et al.; the publisher's indexed full text, abstract, and bibliographic header were available. Claims are limited to the directly available design and outcome statements. The Chinese Text Project pages also intermittently failed to open; the final historical citation uses the accessible Legge translation and its stated page numbers.

## Verification record

Three references were added to the synchronized master bibliography (1,018 unique references). Existing references and all figure/table IDs in both chapters were preserved.

- Final source and reference checks: zero errors and warnings; `git diff --check` passed.
- HTML and EPUB renders completed sequentially. After removing one repeated sentence in the Yu introduction, Chapter 21 HTML and the complete EPUB were rendered again.
- `check-browser.cjs` passed for both chapters at 1,280- and 390-pixel widths. The new main-text passages are visible, both cross-chapter links resolve, and there is no horizontal page overflow. Saved screenshots were reviewed, including the Yu-to-BRAIN transition and the mobile listening passage.
- `python3 scripts/qa_epub_release.py`: passed with zero errors, including source freshness and link checks.
- `python3 scripts/qa_float_references.py --rendered --epub-dir /private/tmp/decision-book-yu-epub-final --output audits/yu-urge-listening-20260918/float-reference-qa.json`: passed for 62 sources, 117 figures, and 165 tables, with zero issues.
- `content-checks.json` confirms final EPUB/search text, preserved references and float IDs, and unique required anchors. Both principal sections are outside collapsed material.
- Removed unrelated HTML attribute-order changes in Chapters 3, 28, and 37 only after verifying equivalence of parsed HTML events with sorted attributes. These files were clean at the start of this revision.
- Final EPUB SHA-256: `8014609e5368f02b5d5027cfa7c8c8c1b5454a97130dca3e8620248db6bb174a`.

No commit or push was performed.
