# Reward anticipation, effort, and near misses — 14 September 2026

## Coverage and editorial decisions

The baseline manuscript already distinguished wanting from liking and contained a collapsed reward-prediction-error note in Chapter 21. It did not develop the uncertain-reward or gambling near-miss examples, or the distinction between obtaining a reward through effort and consuming it. Chapters 16 and 19 already covered ambiguity and delayed choice behaviorally; Chapter 39 already treated digital engagement and user agency.

Added two connected main-text sections in Chapter 21, a measurement-focused Research Lens there, short Research Lenses in Chapters 16 and 19, a substantive cross-link in Chapter 39, and concept-index entries. The previous prediction-error note now complements the main explanation rather than repeating its definition. Eight published references were added; previous references were retained and the affected lists sorted alphabetically. No unpublished lecture slides are cited.

The supplied prose was treated as a lead to investigate. The attached curve was not adopted as measured evidence. In particular, the classic uncertainty experiment recorded dopamine-neuron firing during Pavlovian waiting, not a universal quantity of dopamine released during work. Baseline activity is not zero dopamine. No claim about depression or anxiety being caused by a single reduction in dopamine was added; those clinical claims require a separate, more differentiated account. The proposed all-or-none lever-pressing claim was replaced with a directly documented effort-allocation experiment. No inference about the fictional student's dopamine levels is made.

## Claim-to-source matrix

Full author lists and publication details are recorded in the affected chapters and the synchronized reference list. The links below identify the evidence consulted. Sample sizes are stated only where verified.

| Source | Design and measurement | Supported contribution | Boundary and editorial use |
| --- | --- | --- | --- |
| [Schultz, Dayan, & Montague (1997)](https://pubmed.ncbi.nlm.nih.gov/9054347/) | Primate neuronal recordings synthesized with reward-learning models. | Predictive cue responses, unexpected reward responses, and omission-related dips. | Firing responses are not pleasure measurements; promoted existing explanation into Chapter 21's main text. |
| [Salamone et al. (1991)](https://pubmed.ncbi.nlm.nih.gov/1780422/) | Food-deprived rats; lever-pressing for preferred pellets versus freely available chow; systemic and local dopamine manipulations. | Reduced lever pressing with increased chow consumption. | Identifies altered response allocation, not loss of all appetite, pleasure, or action; added to Chapter 21. |
| [Mohebi et al. (2019)](https://www.nature.com/articles/s41586-019-1235-y) | Compared identified dopamine-cell firing with accumbens dopamine release in the same task. | Reward-expectation-linked release changes without corresponding changes in recorded cell spiking. | Distinguishes measurement and functional timescales; added to Chapter 21. |
| [Fiorillo, Tobler, & Schultz (2003)](https://www.hms.harvard.edu/bss/neuro/bornlab/nb204/final_exam/FiorilloSchultz2003.pdf) | Two monkeys; visual cues; liquid reward after two seconds; probabilities 0, .25, .5, .75, 1. | Waiting-period activation greatest at .5; cue responses increase with reward probability. | This is not a universal optimum for motivation or addiction. Main text and research note preserve that distinction. |
| [Clark et al. (2009)](https://motivation.site.wesleyan.edu/files/2016/06/Clark-2009-Neuron1.pdf) | Two-reel slot-machine task; behavioral experiment n=40; subjective ratings, plus a separate fMRI experiment; manipulated choice of play icon. | Near misses less pleasant than full misses but increased desire to continue on participant-chosen trials. | Reported desire is distinct from measured long-term persistence or addiction. Added to Chapter 21 with the personal-control condition. |
| [Habib & Dixon (2010)](https://pubmed.ncbi.nlm.nih.gov/21119848/) | fMRI; 11 pathological and 11 nonpathological gamblers. | Greater overlap of near-miss and win responses in the pathological group. | Blood-oxygenation contrasts do not directly measure dopamine; observational group difference. Added to Research Lens. |
| [Sescousse et al. (2016)](https://www.nature.com/articles/npp201643) | 22 pathological gamblers, 22 controls; fMRI; double-blind counterbalanced placebo versus sulpiride. | Amplified striatal near-miss responses in gamblers; no reliable drug modulation of those responses. | Retained the null pharmacological result; dopamine mechanism remains unresolved. |
| [Hsu et al. (2005)](https://stanford.edu/~knutson/bad/hsu05.pdf) | Human fMRI comparisons of risk and ambiguity, plus lesion study; main fMRI n=16. | Ambiguity associated with greater amygdala/OFC and lower striatal responses. | Neither a direct dopamine assay nor a study establishing addiction; added to Chapter 16 and linked from Chapter 21. |
| [Kable & Glimcher (2007)](https://www.nature.com/articles/nn2007) | Human intertemporal monetary choice and fMRI. | Delayed-reward subjective value tracked in ventral striatum and cortical regions. | Challenges an exclusive impulsive-versus-patient regional split; no direct dopamine measure. Added to Chapter 19. |

The strongest transferable implication is to distinguish what prompts pursuit, how much effort it requires, what the outcome feels like, and whether the next attempt is actually more likely to succeed. The animal, imaging, and behavioral findings answer different parts of that question.

## Verification

Completed a full HTML build, followed by focused renders after the final wording and note-anchor refinements, and a full EPUB build. The source/book QA check reports zero errors and zero warnings. Reference synchronization passes with 895 unique entries. EPUB release QA reports zero errors. Source, HTML, and EPUB float-reference coverage passes for all 116 figures and 147 tables.

All eight added references have verified publication identifiers; the original chapter reference entries remain present. The affected chapter reference lists are alphabetically ordered. A baseline comparison confirms that all figure captions, alternative text, and table rows from the start of this turn are unchanged, including the previous Figure 21.2 and 21.5 simplifications.

Chromium reading checks pass for the five new section/note anchors at 1440-pixel and 390-pixel widths in both HTML and extracted EPUB content (10 checks per edition). Desktop and phone captures were visually inspected. The final EPUB contains exactly one occurrence of each new anchor. The research notes use separate neutral wrappers to avoid duplicate identifiers from EPUB callout rendering. These checks cover the packaged EPUB content in a browser, not every native e-reader application.

The accompanying preservation, reading, and EPUB-anchor JSON files record these checks. No commit or push was performed for this request.
