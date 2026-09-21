# Quarto Editing and Publishing Guide

The repository is now a Quarto book project. The `.qmd` files are the canonical source; `docs/` is generated output. Do not routinely edit generated HTML files.

## Book-specific presentation requirements

The following requirements apply to *Decision in the Making*. They are project conventions, not general writing-style rules.

### Examples adapted from teaching materials

- Present each example directly, without phrases such as “the lecture’s example,” “as shown in the slides,” or “the course’s comparison.” Make the explanation self-contained and refer only to figures readers can see in the book. Retain scholarly citations and qualifications needed to interpret the evidence; keep the provenance of teaching materials in project records.

### Personal stories and cultural examples

- Write the author's experiences in first person in consistently labeled, normally expanded note boxes headed “From my experience: …”. Prefer “personal story” or “personal experience” to the vague “personal illustration.” Place the story beside the mechanism it helps the reader understand.
- Preserve supplied events, setting, uncertainty, and sequence while polishing the language. Do not invent dialogue, motives, reactions, actions, or outcomes. Distinguish a response the author gave at the time from what they now think they could have said; identify hypothetical alternatives explicitly.
- End with a short implication earned by the episode, without retelling its lesson in several forms. Use the story to illustrate a concept, not to establish a scientific or population-level claim.
- Scope cultural observations to the people and settings described. One colleague's reaction is not a national trait; a restaurant observation is not a national frequency estimate. Separate observations from proposed explanations, especially when connecting food, sleep, institutions, and behavior.
- When a personal story spans topics, give it one developed home and cross-reference it elsewhere. Do not repeat the full anecdote to populate several chapters.

Use the existing Quarto style. Put an anchor before a new callout when it needs a link; assigning the ID directly to the callout can duplicate it in the EPUB wrapper:

```markdown
[]{#personal-story-short-name}

::: {.callout-note .personal-example icon=false}
## From my experience: a descriptive title

The author's story and its implication.
:::
```

### Supplementary mathematics

- Minimize mathematics in the main reading path. Explain the intuition and decision consequence in ordinary language; put derivations and substantial formal analysis in a clearly titled, foldable “Mathematical analysis” box or an appropriate appendix. Keep simple quantities when they help, and spell out expressions such as “one billion” when notation adds no value.

## Install

1. Install Quarto from <https://quarto.org/docs/download/>.
2. Install the official **Quarto** extension in VS Code.
3. Open the repository folder in VS Code and trust the workspace.
4. Confirm installation:

```bash
quarto --version
quarto check
```

## Edit with live preview

From the repository root, run:

```bash
quarto preview
```

Open a chapter such as `chapters/01-how-decisions-should-be-made-and-how-they-actually-are.qmd`. Use **Visual** mode for word-processor-like editing or **Source** mode for precise Markdown editing. Save the file; the browser preview updates automatically.

## Rebuild all publishing files

```bash
quarto render
```

This rebuilds the complete HTML book in `docs/`. GitHub Pages should be configured to publish `main` / `docs`.

## Publish

```bash
git add .
git commit -m "Revise textbook"
git push origin main
```

## Reorder appendices

Appendix letters follow the order in `_quarto-html.yml` and `_quarto-epub.yml`, not the letters in historical filenames. When the order changes, update both profiles, reader-facing appendix labels and ranges, and the expected order in the publication checks. Preserve filenames and anchors so saved links still resolve. Rebuild both editions and check that headings, navigation, figure and table numbers, and labeled links agree with the new order.

## Edit a figure

Keep an editable source such as `figures-src/decision-loop.drawio`, export it as `figures/decision-loop.svg`, and run `quarto render`. The same filename lets the chapter update without changing its source.

### Keep the figure informative

Keep visible text to what readers need to interpret the graphic: panel labels, concepts, axes, units, conditions, legends, and necessary task instructions. Put repeated figure titles, subtitles, source lines, explanatory footers, and interpretation in the caption or adjacent prose. After moving text, update alternative text so it does not describe a note or panel that is no longer visible.

Before deleting text, identify what a reader should learn from the illustration. Read the image without the surrounding chapter and check that it supplies the information needed for that purpose:

- Name the central concepts using standard terms, with a short definition or concrete example where the term alone is insufficient.
- Show the actual distinction, mechanism, comparison, or task. A generic question such as “Who was observed?” cannot replace the term **attrition** and an explanation of missing outcomes.
- Identify comparison groups, experimental conditions, units, denominators, abbreviations, and hypothetical or schematic assumptions needed to interpret the visual.
- Retain qualifications that prevent an incorrect inference. A compact diagram must not imply that intention-to-treat analysis automatically resolves attrition or spillovers, for example.
- Remove repeated slogans and decorative headings only when the remaining figure still teaches its intended point. Meaningful labels are not redundant merely because the chapter also explains them.
- Keep captions and alternative text focused on what readers should understand. Omit generic production notes about how an image was made or redrawn; retain production provenance in the project records. Preserve scholarly source citations, required credits and licenses, and distinctions between hypothetical illustrations, simulations, and observed results.

A planning-question diagram, an activity, and a research-results plot serve different purposes. Preserve the task instructions needed for an activity without adding a visible answer banner; give alternative text equivalent access to the displayed information. Photographs should retain their illustrative role without implying evidence for an unobserved mechanism.

After changing a figure, update its alternative text and caption, regenerate its PNG from the final SVG, and inspect the image at native and narrow reading sizes. Update its generator as well. Covered generators use `scripts/reviewed_figure_cleanup.json` to preserve reviewed edits and deliberately reject unreviewed changes in generator output; refresh those exact patches after a new review rather than bypassing the guard.

### Style for empirical plots

Place y-axis titles vertically alongside their axes throughout the book, with enough margin for the tick labels. Keep category names, tick labels, panel titles, and legends in their appropriate readable orientation; these are not y-axis titles.

Use the Chapter 27 news and earnings plots as the style reference for comparable empirical charts: white background, navy text, muted axes, light horizontal grid lines, and the book's blue/teal palette with restrained additional colors when groups need them. Use consistent sans-serif typography, readable axis units, sparse time ticks, and direct labels or a compact legend. Keep event labels brief and put the interpretation and scholarly source in the caption or surrounding prose.

`scripts/build_finance_news_figures.py` provides the current reusable plotting settings and builds Figures 27.2–27.4. Match Figure 27.5's treatment when adding comparable figures. Preserve the scientific form of the evidence: points stay points, trading gaps stay gaps, and published irregularities should not become fitted smooth curves. Label approximate tracing when original numerical data are unavailable, and keep source geometry or extracted coordinates with provenance for reproduction.

### Connect every table and figure to the argument

Every teaching table and figure must have a stable identifier and an explicit numbered reference in the surrounding prose of the chapter, appendix, or part opener where it appears. Use `@fig-...` and `@tbl-...` so numbering and links remain correct when the book changes. A caption, alternative text, or reference from another chapter does not replace this local discussion.

Tell readers what to notice, compare, infer, or do with the material and how it advances the explanation. Integrate the reference into an existing substantive sentence where possible; avoid adding a repeated summary or a sentence that only says “see the table below.” For a prediction activity, identify the task before the image and discuss its interpretation afterward without revealing the answer prematurely.

Give previously unnumbered teaching tables and illustrations a caption and identifier. Preserve existing identifiers even when their names contain old chapter numbers. Retain legacy anchors for removed material, but do not treat them as current tables or figures. Covers and author portraits serve a different purpose and do not need numbered discussion. Keep references to format-specific media inside the same publication condition, so another edition cannot acquire a broken reference.

Before delivery, check both that every current table and figure has a body reference and that the accompanying discussion explains its purpose. An automatic reference count can check coverage; it cannot establish that the discussion is useful.

Run `python3 scripts/qa_float_references.py` for source coverage. After the HTML build, add `--rendered` to check the displayed floats and their local prose links. After extracting the final EPUB, add `--epub-dir /path/to/extracted/EPUB` to check that edition too. Follow the coverage check with a reading of the discussion in context.

## Important

- Edit `.qmd`, not `docs/*.html`.
- Do not edit `docs/search.json` or Quarto-generated navigation.
- Run a full `quarto render` before publishing.
- Build the EPUB with `quarto render --profile epub`. The normalized release is copied to `docs/Decision-in-the-Making.epub` without adding a download button to the HTML book.
