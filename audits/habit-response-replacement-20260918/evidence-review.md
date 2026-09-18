# Replacing a habitual response to a cue

Date: 2026-09-18. Scope: Chapter 21, a transfer paragraph in Chapter 39, the habit index entry, references, and generated HTML/EPUB. Pre-edit snapshots preserve the existing revisions.

## Placement and teaching decisions

The expanded main-text section, **Give a familiar cue a new response**, follows identifying cues and precedes allowing and observing urges. It uses the chapter's bedtime-scrolling example throughout. The earlier heading anchor remains available.

The five steps distinguish identifying the actual cue, specifying an action, preparing access, checking the function of the alternative, and repeating it in context. The example separates starting a replacement routine at bedtime from stopping scrolling already underway. BRAIN now leads explicitly to the prepared replacement. The practice lab rehearses the same sequence; Chapter 39 transfers it to the laptop/inbox example.

The text does not assume a single reward behind every habit or require an identical reward for the replacement. Nor does forming a plan establish that a new habit has been learned. The existing discussion of gradual automaticity, continued availability of old responses, and recovery after a lapse remains intact.

## Source verification

- **Adriaanse et al. (2011), DOI 10.1177/0146167211399102.** Bibliographic details checked against the [university record](https://research-portal.uu.nl/en/publications/breaking-habits-with-implementation-intentions-a-test-of-underlyi/) and the [author-hosted paper](https://bpb-us-e1.wpmucdn.com/wp.nyu.edu/dist/c/6235/files/2019/02/adriaanse-et-al-2011-breaking-habits-with-implementation-intentions.pdf). The three experiments used primed lexical decisions to assess accessibility of familiar versus alternative options. The chapter describes the reduced accessibility advantage, without treating that laboratory measure as demonstrated long-term habit replacement.
- **Wood and Rünger (2016), DOI 10.1146/annurev-psych-122414-033417.** Existing chapter reference. Checked the [author-hosted review](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.runger.2016.pdf), especially its intervention discussion: strong habits can resist planning alone; cue/context changes and response convenience matter. The chapter combines planning with preparation and repetition rather than relying on intention alone.
- **Gollwitzer (1999).** Reused the book's existing reference for the situation–response structure of implementation intentions. No new numerical efficacy claim was added.
- **Lally et al. (2010).** Reused the chapter's existing habit-formation study for repeated action in a consistent context and increasing automaticity. The new passage uses no universal timetable or fixed repetition threshold.

The student and manager examples are teaching applications, not descriptions of participants in these studies. No commit or push is part of this request.

## Verification

- Source QA passed with zero errors and warnings; the master reference check passed with 1,019 unique references. Chapter 21 adds the new Adriaanse reference and reuses the existing Gollwitzer reference. All earlier references and figure/table IDs in both chapters were preserved.
- Full HTML and EPUB renders completed sequentially. EPUB release QA passed with zero errors.
- Browser checks passed at 1,280- and 390-pixel widths for both chapters: visible main-text sections, working reciprocal links, no horizontal page overflow, and the retained old Chapter 21 anchor. Desktop screenshots and the Chapter 21 mobile viewport were inspected. Mobile screenshots use the viewport to avoid the fixed navigation bar crossing a tall section capture.
- Float-reference QA passed for 62 sources, 117 figures, and 165 tables, with zero issues.
- The new text is in the search index and EPUB. An initial content-check assumption that EPUB filenames retained source names was corrected: Quarto uses numbered package filenames. The final anchor-based checks passed and their actual locations are recorded in `content-checks.json`.
- Removed render-only attribute-order changes in Chapters 3 and 37 after confirming equality of parsed HTML events with sorted attributes. Both files were clean before this revision.
- `git diff --check` passed. Final EPUB SHA-256: `36f13cad6cffb050c41fbd3fb17c011b48f1061a55e434307ec07b8c3cc5f825`.
