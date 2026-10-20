# Founder stories in the rationalization chapter

## Request and placement

Integrated the discussion in the user's two screenshots, dated 2026-10-20 at 15:49:27 and 15:49:31, into Chapter 7. The screenshots supplied teaching content, not operational instructions. Original attachments were left unchanged.

- Primary home: “Reading a founder's story,” within “Organizations have narrators too.” The following escalation-of-commitment discussion now has its own subordinate heading.
- Chapter 31 links back from its discussion of causal stories and causal evidence.
- Added a learning goal and a missing-comparison question to the existing rationalization detector. Existing figures and practice questions were retained.

## Coverage and evidence

The four features organize the supplied teaching points; they are not attributed to Gartner as a published four-part taxonomy.

| Supplied point | Integration and evidence | Scope |
| --- | --- | --- |
| Entrepreneurial narrative and imagination | Gartner (2007): narrative analysis examines situated accounts and imagined ventures. The toy-store classroom account grounds the discussion. | Conceptual introduction to a special issue, not a causal experiment. Narrative evidence retains analytical and constructive value. |
| Told backward | Known success can reshape the account of earlier uncertainty; Fischhoff (1975) supplies the hindsight mechanism. | General judgment evidence applied to founder accounts, not a study of founders. |
| Told by survivors | Visible founders exclude failed and unobserved attempts; Denrell (2003) explains misleading learning from selected survivors. | Selection can create a misleading association; the passage does not claim that persistence or risk-taking always lacks value. |
| Told to a template | Audience expectations shape what is made comprehensible and credible. Martens et al. (2007) connects narrative features to IPO resource acquisition and valuation. | Observational associations; no causal effect of wording is claimed. The book avoids sample counts and exact coefficients from the publicly available manuscript. |
| Told with gaps | The account may omit family finance, coworkers, credit, prior attempts, timing, or luck. The interview questions restore these possible contributions. | Questions for analysis, not allegations about a named founder or proof of deliberate concealment. |
| Value of the story | Compare versions, dates, audiences, contemporary records, other participants, and ventures with different outcomes. | Separates accounts of meaning and possibility from evidence about the causes of success. Stories can also precede outcomes and help organize cooperation. |

## Verified sources

Checked on 2026-10-20 against original articles, publisher metadata, and public author copies:

- Gartner, W. B. (2007). Entrepreneurial narrative and a science of the imagination. *Journal of Business Venturing, 22*(5), 613–627. [DOI](https://doi.org/10.1016/j.jbusvent.2006.10.003). [Author-uploaded full text](https://www.researchgate.net/publication/223828503_Entrepreneurial_Narrative_and_a_Science_of_Imagination). Relevant passages: pp. 613–614, 618–619, and the discussion of imagination. Publisher full text did not open through the search tool; the author copy supplied the inspected text.
- Fischhoff, B. (1975). Hindsight is not equal to foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology: Human Perception and Performance, 1*(3), 288–299. [DOI](https://doi.org/10.1037/0096-1523.1.3.288). [Original article at MIT](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Behavioral_Decision_Theory/Fischhoff_1975_Hindsight_is_not_equal_to_foresight.pdf). Already in the master bibliography; added to Chapter 7's references.
- Denrell, J. (2003). Vicarious learning, undersampling of failure, and the myths of management. *Organization Science, 14*(3), 227–243. [Publisher](https://pubsonline.informs.org/doi/10.1287/orsc.14.2.227.15164). Abstract and metadata support the selection argument. The DOI contains `14.2` although the article is in issue 3; preserved the publisher's DOI.
- Martens, M. L., Jennings, J. E., & Jennings, P. D. (2007). Do the stories they tell get them the money they need? The role of entrepreneurial narratives in resource acquisition. *Academy of Management Journal, 50*(5), 1107–1132. [DOI](https://doi.org/10.5465/amj.2007.27169488). [Author-uploaded manuscript](https://www.researchgate.net/publication/228388750_Do_the_Stories_They_Tell_Get_Them_the_Money_They_Need_The_Role_of_Entrepreneurial_Narratives_in_Resource_Acquisition). Inspected methods/results: 1996–2000 IPO prospectuses, firm-resource controls, mixed results across narrative features, and OLS associations. Three industries were semiconductors, biotechnology, and internet content providers.

Lounsbury and Glynn (2001), DOI 10.1002/smj.188, was also checked as background theory on legitimacy and resources. The book uses the developed Martens evidence rather than adding another citation with the same explanatory job.

## Verification

- Full HTML and EPUB renders completed. Chapter 7 HTML and the EPUB were refreshed after refining one sentence about what a narrative's wording reveals.
- `python3 scripts/qa_quarto_book.py`: 0 errors, 0 warnings.
- `python3 scripts/sync_references.py --check`: 1,283 unique master references, synchronized with the current chapters and appendices, including existing user revisions.
- `python3 scripts/qa_epub_release.py`: 0 errors on the final EPUB. Native e-reader layout was not separately inspected.
- Rendered float-reference check: 69 sources, 108 figures, 171 tables, 0 issues. See `float-reference-qa.json`.
- Inspected the new section at desktop width and the four features plus detector table at 390 × 844. The chapter's page width matched the 390-pixel viewport without horizontal overflow.
- Both cross-reference URLs and target anchors were checked; the Chapter 31 destination was opened directly and its backlink inspected. Automated link clicks did not trigger navigation in the in-app preview, so a successful click interaction is not claimed.
- Final EPUB inspection confirmed one founder-story section, all four list items, the Gartner discussion, and the final wording. See `content-qa.json`.
- Preserved existing user edits and pre-render file modes. `git diff --check` passed. No commit or push performed.
