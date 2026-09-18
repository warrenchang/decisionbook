# Predictive learning and metacognition: evidence and editorial review

Date: 18 September 2026. Scope: Chapters 4 and 8, their bibliography, and relevant concept-index entries. The saved chapter baselines include the already completed Jennings Research Lens change. No source lecture notes were altered.

## Placement and scientific decisions

- Chapter 4: expand the existing AI Research Lens, retaining the bank example, in-context learning, image/video diffusion, and framing exercise. Explain generative models, attention, current-state inference versus enduring learning, and age differences before the practical evidence-seeking discussion.
- Chapter 8: add metacognitive monitoring and control between the costs of deliberation and the training of automatic responses. Place AI reasoning in its own collapsible Research Lens immediately after the human account. The main narrative remains continuous when either lens is closed.
- A generative model connects hidden causes with expected observations; its predictions need not concern future events. Attention and prediction interact. The precision account of attention is a theoretical model, not a demonstrated complete architecture of the brain.
- Distinguish model parameters from the influence assigned to current evidence. Changes in an estimated state need not entail lasting parameter learning. Standard fixed-parameter LLM inference can still support adaptation within context; subsequent training can change parameters.
- Replace the proposed monotonic age rule with specific evidence about causal expectations, uncertainty-sensitive updating, and retained learning. The studies do not establish that one global weight on sensory input decreases with age.
- Distinguish predictive-processing theory from dual-process classifications. Metacognitive monitoring can motivate controlled inspection; it does not require a separate inner observer.
- AI reasoning can use generated intermediate context, learned checking strategies, or an explicit search procedure. A separate self-prompting controller is design-dependent. Neither extended output nor a reasoning label demonstrates consciousness, psychological System 2, or reliable correction.

## Claim-to-source matrix

Full verified bibliographic entries are in the relevant chapters and the synchronized master bibliography. Links below lead to primary papers or author/institutional copies. Existing sources support the theoretical framing; eight references were newly added.

| Source | Design or evidence type | Finding or function used | Boundary retained | Placement |
| --- | --- | --- | --- | --- |
| [Rao & Ballard (1999)](https://doi.org/10.1038/4580); [Friston (2010)](https://doi.org/10.1038/nrn2787) | Computational account of visual processing; theoretical synthesis | Generative predictions, perceptual inference, learning, and control | Proposed computational accounts; no claim that every perceptual or reflective process has a uniquely established implementation | Ch. 4; Friston also added to Ch. 8's local bibliography |
| [Feldman & Friston (2010)](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2010.00215/full) | Computational theory and simulations of attention | Attention can be modeled through precision assignment | Precision and attention are not universally interchangeable | Ch. 4 |
| Brown et al. (2020), existing official NeurIPS reference | LLM benchmark experiments with examples in the prompt | In-context adaptation with fixed parameters | Does not imply that a normal prompt retrains the model or that all AI systems have fixed parameters forever | Ch. 4 |
| [Lucas et al. (2014)](https://cocosci.princeton.edu/papers/WhenChildrenAreBetter.pdf) | Experiments comparing adults with children aged four and five; causal generalization tasks | Children more readily generalized an unusual conjunctive causal relationship | Specific task and kind of prior; no general child superiority or monotonic lifespan trajectory | Ch. 4 |
| [Nassar et al. (2016)](https://www.nature.com/articles/ncomms11609.pdf) | Behavioral age comparison and computational analysis of a changing prediction task; 57 participants per age group in reported regressions | Older adults showed weaker uncertainty-dependent adjustments; both groups learned more after surprise | Behavioral/model result, not direct measurement of neural parameters; group comparison, not longitudinal aging | Ch. 4 |
| [Boyke et al. (2008)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6670504/) | Older adults trained in juggling; structural MRI | Skill acquisition and associated regional structural changes | MRI findings do not directly measure a predictive model's parameters; acquisition does not imply youthful proficiency | Ch. 4 |
| [Desender, Boldt, & Yeung (2018)](https://discovery.ucl.ac.uk/id/eprint/10076911/) | Perceptual task manipulating evidence strength and variability; initial study and preregistered replication | Information seeking differed with confidence even at matched accuracy | Does not imply confidence is always calibrated or establish one universal mechanism for monitoring | Ch. 8 |
| [Wei et al. (2022)](https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) | Prompting experiments on reasoning benchmarks | Intermediate worked steps can improve performance | Benchmark and model dependence; no assurance of truth or awareness | Ch. 8 AI lens |
| [Guo et al. (2025)](https://www.nature.com/articles/s41586-025-09422-z) | Reinforcement-learning experiments in the DeepSeek-R1 research | Learned reasoning behavior includes checking and revising intermediate work | Describes the reported research; does not claim every deployed reasoning model uses its training pipeline or that the whole R1 pipeline excludes supervised learning | Ch. 8 AI lens |
| [Yao et al. (2023)](https://proceedings.neurips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract.html) | Tree of Thoughts search framework tested on planning/search tasks | Repeated model calls generate and evaluate candidate steps; search can backtrack | An explicit architecture, not a description of all reasoning modes | Ch. 8 AI lens |
| [Huang et al. (2024)](https://arxiv.org/abs/2310.01798), ICLR publication linked in bibliography | Experiments on intrinsic self-correction without external feedback | Revision sometimes reduced accuracy in tested systems/tasks | The title is not adopted as a universal current claim that LLMs cannot self-correct; positive training evidence is discussed alongside it | Ch. 8 AI lens |

## Preservation and coherence checks

- Preserved the opening perception exercise and later reveal, visual demonstrations, Jennings case and stable anchor, active-inference lens, bodily-regulation material, diffusion discussion, and chapter practice activities.
- Preserved the bat-and-ball opening, expert engineer example, Stroop exercise, practice/feedback section, emotion section, and comparison table.
- New cross-links connect the Chapter 4 learning discussion, Chapter 8 metacognition and AI lens, and Chapter 42's existing AI workflow.
- New and edited AI callouts use a plain outer anchor wrapper so HTML and EPUB can retain stable, unique link targets.
- No new mathematical expressions were introduced.

## Validation

- Full HTML and EPUB renders completed sequentially. A final EPUB rebuild followed the last source whitespace cleanup; the released and staged files match and pass the source-freshness check.
- `python3 scripts/sync_references.py --check`: 1,007 unique references, synchronized.
- `python3 scripts/qa_quarto_book.py`: zero errors and zero warnings; no unresolved author–year citations.
- `python3 scripts/qa_epub_release.py`: zero errors, including all internal content links, packaged XHTML, figures, and navigation.
- `python3 scripts/qa_float_references.py --rendered --epub-dir /private/tmp/predictive-metacognition-final-epub`: 62 sources, 117 figure labels, 165 table labels, zero issues.
- `check-content.py`: existing references and figures retained in both chapters; HTML IDs unique and local chapter links resolve; the two revised/new AI lenses, Jennings lens, and metacognition section have unique EPUB targets with their text present. Research Lens contents remain expanded in EPUB.
- `check-lenses.cjs`: all three relevant lenses start closed and open/close by mouse click at 1,280 px and 390 px; no page-width overflow. This check does not certify keyboard accessibility.
- Visually reviewed the expanded Chapter 4 lens at desktop and phone widths, the expanded Chapter 8 lens on phone, and its collapsed desktop transition into practice and learning. Titles, text wrapping, padding, and the main narrative remain readable. PNG evidence and JSON results accompany this record.
- `git diff --check`: pass.
- Source changes and generated publications are ready for review; no commit or push was performed.
