# Habit chapter: first editorial revision

Date: September 10, 2026. Baseline Git revision: `d2b381b`.

The user requested a first independent edit to make Chapter 21 more organized, engaging, and free of redundant information. The canonical chapter was revised; this is a local editorial iteration, not a published release or an approved style specification for the remaining chapters.

## Reading the revision

- [Revised chapter](../../docs/chapters/21-habits-wanting-and-self-control.html)
- [Editable source](../../chapters/21-habits-wanting-and-self-control.qmd)
- [Preserved original source](chapter-before.qmd)
- `chapter-changes.diff` records the exact source changes against the preserved original.

The central change is a continuous explanation organized around a fictional student checking a phone while writing. The scene is introduced as an illustration. The chapter follows four questions: what makes a response habitual, how that control develops, why an unrewarding routine can persist, and how to prepare a different response.

## Changes and reasons

| Original feature | Revision | Reason |
| --- | --- | --- |
| Five examples before the main explanation | One opening scene, revisited at each explanatory step and at the close | Gives the reader a concrete puzzle and a reason to continue. |
| Nine substantive top-level sections, with overlapping accounts of habits and context | Four substantive top-level sections | Establishes a progression from mechanism to evidence to application. |
| Extensive lists of possible cues, responses, occupations, and behaviors | A developed phone example, a brief positive walking example, and one managerial application | Makes each example perform a distinct explanatory job. |
| Repeated habit definitions and several presentations of the formation timetable | One definition and one account of the learning curve | Removes repeated explanation while preserving the evidence boundary. |
| Brief stale-popcorn finding buried in the context discussion | A developed study example addressing persistence despite disappointment | Uses an experiment to answer the question the narrative has raised. |
| Model-based/model-free control and neural learning introduced during the main narrative | Two optional research notes at the end | Retains technical material without making it a prerequisite for the practical explanation. |
| Full BRAIN exercise within the main self-control discussion | A short main-text introduction and an optional practice note | Preserves access to the exercise without interrupting the chapter's central argument. |
| Five tables repeating distinctions, examples, and interventions | One compact BRAIN prompt table in the optional note | Avoids restating prose as parallel catalogues. |
| Repeated marshmallow discussion | Removed here; already discussed in Chapter 19 | Avoids duplicating a nearby chapter's teaching example. |
| Brief ego-depletion detour | Removed here; still covered in Chapter 39 | Keeps the chapter focused on habits without changing the book's treatment of the debate. |
| Thorndike/Skinner historical survey and additional named mechanisms | Removed from this chapter | They were not needed to explain the central puzzle. Unused local references were removed and the master bibliography synchronized. |
| Long assignment asking for numerous constructs at once | Four sequential questions and a one-week observation exercise | Makes the task easier to carry out and evaluate. |

Reader-oriented word count, excluding the reference list, YAML, URLs, and attribute markup but including headings and captions: **5,003 → 3,179**, a **36.5% reduction**. This count includes the optional notes. The count uses the same word-token rule for both versions; it is not a raw file-size comparison.

## Scientific distinctions preserved or clarified

- Habit frequency, automaticity, outcome devaluation, and computational model fits remain distinguishable. Goal-directed control is no longer equated with conscious, effortful reasoning.
- Reward or relief can support repetition; reward is not made a necessary condition for every habit performance.
- Habit, motivational wanting, experienced liking, and conscious urges remain distinct. An explicit forecast is not made necessary for every motivational pull.
- The habit-formation range describes modeled times toward a plateau in the fitted cases, including projections beyond observation. It is not a universal timetable or an observed completion date for every participant.
- The missed-opportunity result remains bounded: one omission did not materially disrupt the process in the cited study; it did not strengthen the habit or establish that repeated omissions are harmless. The phrase “no strengthening, but no reset” is retained with that qualification.
- The popcorn account distinguishes measured prior habit strength from manipulated immediate conditions. Neither that study nor the fictional phone example establishes that all repeated actions ignore outcomes.
- The association between self-control and beneficial routines is explicitly distinguished from causal evidence.
- BRAIN remains a classroom mnemonic, not an independently validated treatment. Everyday phone checking is not treated as a diagnosis of addiction.
- The observation exercise is not represented as a controlled test of intervention efficacy.

## Source checks during this revision

These checks targeted the central explanations and retained numerical claims; they are not a new systematic literature review or a claim that every book citation was independently reverified.

- [Wood and Neal (2007), author-hosted paper](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf): habit/context and goal-control distinctions; retained epigraph source.
- [Wood and Rünger (2016), author-hosted review](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.runger.2016.pdf): context, repetition, and the relationship between habits and goals.
- [Lally et al. (2010), publisher abstract](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674) and [indexed paper copy](https://transformationweightcontrol.com/wp-content/uploads/2024/12/Lally-2010-How-Habits-are-Formed.pdf): range, fitted-case median, and single missed opportunity. The indexed paper text was available; direct full-PDF fetching failed during this turn. The detailed omission statistics were removed from the chapter rather than newly reverified or reinterpreted.
- [Neal et al. (2011), author-hosted paper](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/neal.wood_.wu_.kurlander.2011.the_pull_of_the_past.pdf): fresh versus stale popcorn, context, and nondominant-hand manipulation.
- [Galla and Duckworth (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4731333/): beneficial routines and the stated nonexperimental limitation. Indexed article text was available; a later direct open encountered a browser challenge.
- [Duckworth et al. (2016)](https://pmc.ncbi.nlm.nih.gov/articles/4736542/): situation selection/modification and timing of intervention.
- [Schultz et al. (1997), author page](https://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.html), [Berridge and Robinson (1998)](https://pubmed.ncbi.nlm.nih.gov/9858756), and [Koob and Volkow (2016)](https://pubmed.ncbi.nlm.nih.gov/27475769/): retained learning, wanting/liking, and clinical boundaries checked against accessible source summaries.

## Figures and generated files

All five original figure topics are retained. Captions and alternative text now identify schematic versus observed content and describe the role of each image in the revised explanation. The reward-prediction-error and urge figures are in optional notes.

Visual inspection also led to small geometry corrections in four editable figures: the habit-loop return arrow now reaches the response box; the wanting/liking return connector starts at the box boundary; the separate application heading in the prediction-error figure wraps within its available space; and the urge-observation markers lie on the existing illustrative curve. Corresponding PNG fallbacks were regenerated. These corrections do not change data, the curve, or the relationships represented.

The full local HTML/EPUB builds also refresh generated copies from existing canonical sources. The initial checkout was clean, but some committed HTML captions and copied figures differed from those sources. Such generated-file synchronization is distinct from new edits to other chapters: their canonical prose was not rewritten in this task. File permission changes caused by rendering are normalized back to their original Git modes.

## Verification

Final build and inspection results are recorded in `verification.json` and the repository's `QA_REPORT.md` and `EPUB_QA_REPORT.md`. Browser inspection covers this chapter at 1,440 px and 390 px widths. EPUB inspection uses extracted XHTML in Chromium, rather than asserting identical behavior in every e-reader.

At narrow HTML widths, the existing design provides horizontal scrolling within wide figures; page text itself does not overflow. The EPUB scales wide diagrams to the page, making their internal text small on a phone. The adjacent explanations and alternative text remain available, but comfortable inspection of those diagrams requires zoom or a larger reader. This preexisting EPUB design limitation is not treated as a visual pass at phone size.

## Useful feedback for the next editorial pass

The opening, the popcorn study, and the change-plan section are the most informative places to judge whether this direction matches the intended voice. Comments can identify a passage and state whether the preference applies to this chapter or to the whole book. This first revision is a concrete example for that discussion; its structure should not automatically be imposed on every chapter.
