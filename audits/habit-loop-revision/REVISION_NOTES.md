# Habit-loop revision, 10 September 2026

The author requested four simple elements in a circular layout, with learning shown as feedback and no nested box inside the response-tendency element.

The revised teaching diagram uses **Cue → Impulse → Action → Outcome**, with a dashed **Learning** arrow returning from outcome to cue. The circle represents repeated encounters: it does not claim that an outcome physically creates or changes the next cue. Learning through repetition changes how readily the cue retrieves the action. The caption states this interpretation explicitly.

“Impulse” is an accessible label for readiness to act, not a claim that conscious desire mediates every habitual response. The figure includes this qualification in a single unboxed note, and the chapter illustrates it with the student's hand moving before he notices. “Outcome” allows reward, relief, disappointment, or no interesting reward; it avoids suggesting that each performance must be rewarded. The four elements are an explanatory diagram, not a separately validated four-stage theory of habit.

Scientific basis checked against author-hosted publications:

- Wood, W., & Neal, D. T. (2007). *A new look at habits and the habit–goal interface*. Psychological Review, 114(4), 843–863. https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.neal_.2007psychrev_a_new_look_at_habits_and_the_interface_between_habits_and_goals.pdf
- Wood, W., & Rünger, D. (2016). *Psychology of habit*. Annual Review of Psychology, 67, 289–314. https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/wood.runger.2016.pdf

Both sources support learning context–response associations through repetition. They do not establish the four labels as obligatory independent stages. The distinctions between repetition-based habit learning, current outcome value, and consciously experienced wanting remain in the chapter.

Files changed for this revision:

- `figures/habit-loop.svg` and its PNG fallback: four equal cards, circular arcs, larger labels, one dashed feedback arrow, no nested card.
- `chapters/21-habits-wanting-and-self-control.qmd`: example, caption, alternative text, and explanation aligned with the figure.
- `appendices/appendix-c-portable-course-tools.qmd`: the behavior-redesign canvas uses the same four labels and treats learning as feedback.
- `quarto-custom.scss`: allow this compact figure to fit a narrow screen instead of forcing the horizontal scrolling used for wide diagrams.

`chapter-before.qmd`, `habit-loop-before.svg`, and `habit-loop-before.png` preserve the state immediately before this revision. Earlier chapter revisions remain in `audits/habits-first-round/`. The diff here records only this revision; earlier revision records retain their original scope.

Verification outputs are recorded in `render-verification.json` and `verification.json`. The screenshots show the figure and its caption in HTML and extracted EPUB content at desktop and phone widths; this is browser rendering of EPUB content, not a guarantee of identical rendering in every EPUB reader.
