# Readings that could strengthen the book

Reviewed 21 September 2026. This is a coverage assessment and proposed incorporation plan; no book chapters were changed.

The strongest additions are four short, connected examples: machine learning as a tool for discovering behavioral patterns; information that increases confidence without improving accuracy; an experiment separating perceived improvement from treatment efficacy; and a method for investigating who benefits from an intervention without reusing the same evidence to discover and confirm the answer. These fit Chapters 42, 15, 5, and the evidence-design appendix respectively. They do not require a new chapter.

## Scope and method

The source folder is `Behavioral Economics/Lecture Notes/Readings` in the SDU OneDrive teaching directory. All 20 documents were inventoried and their text extracted. Six Word/PDF pairs contain versions of the same teaching documents, and two slide decks summarize published chapters. The 643-page *Economics of Artificial Intelligence* volume was screened through its contents and relevant constituent chapters; this was not a close reading of the entire volume.

Comparison used the current `.qmd` sources and chapter order in `_quarto-html.yml`, rather than retired Markdown drafts or generated HTML. Promising passages were checked against existing sections and primary publications. This is a targeted editorial review, not a systematic review of every paper mentioned in the teaching notes. The inventory records source paths, SHA-256 hashes, and page/slide counts in [inventory.json](inventory.json); source documents were not altered.

## Recommended additions, in priority order

### 1. Chapter 42: using machine learning to discover behavioral patterns

**Source:** Camerer, *Artificial Intelligence and Behavioral Economics* (2019), especially section 24.2; Athey, *The Impact of Machine Learning on Economics* (2019), section 21.2.

**What is new:** Chapter 42 already explains descriptive, diagnostic, predictive, and prescriptive analysis, and distinguishes prediction from causal intervention effects. It says less about using new measurements to develop behavioral explanations.

**Suggested treatment:** Add a 250–350-word research box near the analytical-purpose table or tool workbench. Camerer describes bargaining experiments in which the history of offers and concessions adds predictive information beyond the amount available for division. Athey discusses converting text and other unstructured material into research variables. Connect these ideas in a sequence: measure behavior → find a predictive pattern → formulate competing explanations → test them with new data or experimental variation.

**Evidence boundary:** Predictive usefulness does not establish a causal mechanism. Camerer's broader proposals are explicitly speculative; present them as a research agenda. Do not infer that a measured cursor movement reveals a particular emotion. Validate any machine-generated measure against the construct it is meant to represent. [Camerer chapter](https://www.nber.org/books-and-chapters/economics-artificial-intelligence-agenda/artificial-intelligence-and-behavioral-economics); [Athey chapter](https://www.nber.org/books-and-chapters/economics-artificial-intelligence-agenda/impact-machine-learning-economics).

### 2. Chapter 5: feeling improved is not the same as demonstrating improvement

**Source lead:** The reading on priming, subliminal messaging, and positive thinking. **Verified original:** Greenwald, Spangenberg, Pratkanis, and Eskenazi (1991), *Double-Blind Tests of Subliminal Self-Help Audiotapes*.

**What is new:** Chapter 5 distinguishes expectations that change experience, behavior, and physiology. This study provides an especially clear way to show why perceived benefit must be assessed separately from the advertised outcome.

**Design and finding:** Across three replications with 237 participants, actual tape content and the label describing its purpose were varied independently. After a month, the tapes did not produce the memory or self-esteem benefits claimed for their subliminal content. Perceived improvement nevertheless tended to follow the label.

**Suggested treatment:** A 200–250-word case immediately after the discussion of expectancy mechanisms, before the illness-after-a-deadline example. A small 2 × 2 design table could make the separation of content and expectation visible. Link Chapter 13's masked-cue note to this example instead of repeating it.

**Evidence boundary:** Keep the conclusion about these tested products and outcomes. General before/after gains do not by themselves identify a causal placebo effect, because practice and other changes can contribute. This finding does not imply that all expectancy effects are illusory. [Original paper and verified metadata](https://journals.sagepub.com/doi/10.1111/j.1467-9280.1991.tb00112.x).

### 3. Chapter 15: more information can increase confidence faster than accuracy

**Source lead:** Camerer's section 24.3.3. **Verified original:** Oskamp (1965), *Overconfidence in Case-Study Judgments*.

**What is new:** Chapter 15 already distinguishes overestimation, overplacement, and overprecision. A concrete study would explain why gathering more detail is not automatically a remedy.

**Design and finding:** Thirty-two judges, including eight clinical psychologists, received one person's case history in four stages and repeatedly answered 25 questions. Confidence increased significantly as information accumulated; accuracy did not improve significantly.

**Suggested treatment:** About 200 words after the three-forms table and before the calibration activity. Ask readers to distinguish information that makes a case feel familiar from information that improves prediction. Cross-reference Chapter 42's untouched test-set principle.

**Evidence boundary:** This was a small study using one case, not a general demonstration that additional information is harmful. Camerer's analogy between human judgment and overfitted machine learning is a hypothesis, not an established account of how the brain computes confidence. [Original article](https://faculty.fortlewis.edu/burke_b/Senior/BLINK%20replication/Overconfidence.pdf); [publication record](https://pubmed.ncbi.nlm.nih.gov/14303514/).

### 4. Evidence-design appendix, with a short Chapter 42 link: discovering who benefits

**Source:** Athey (2019), section 21.4.2, and Athey and Imbens (2016), *Recursive Partitioning for Heterogeneous Causal Effects*.

**What is new:** Chapter 42 already has the student-outreach example showing why dropout risk and intervention benefit can rank groups differently. The evidence-design appendix covers multiplicity and preregistration. The missing bridge is how exploratory subgroup discovery can be followed by defensible estimation.

**Suggested treatment:** Add a 150–250-word optional methods box after the appendix's multiplicity discussion. Explain an “honest” split: use one sample to discover promising group definitions and a separate sample to estimate their treatment effects. Add only a short link from Chapter 42's existing outreach example.

**Evidence boundary:** This is a methodological contribution supported by simulations, not an empirical demonstration that a particular outreach policy works. Splitting data costs precision and does not repair confounding, poor measurement, or a weak intervention. Estimated subgroup averages do not reveal each person's individual causal effect. [Athey and Imbens, PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC4941430/).

## Smaller or conditional additions

- **Prediction and valuation:** Agrawal, Gans, and Goldfarb's chapter is already cited and substantially incorporated in Chapter 42. A short qualification could explain that their model does not imply that better prediction always raises the value of human judgment: the relationship depends on the cost of learning payoffs and on automation. Keep the book's established distinction between their technical use of “judgment” and the book's broader terminology. The relevant discussion is in sections 3.4.4–3.6 of the local published chapter.
- **Personalization and exploitation:** Camerer's concern that AI can either help or exploit consumers would make a useful cross-reference from Chapter 42 to Chapter 40. Chapter 40 already explains recommendation systems, platform metrics, personalization, and dark patterns; another full discussion would repeat it.
- **Positive self-statements:** Wood, Perunovic, and Lee (2009) could supply a brief contrast between repeating a favorable statement and having an actionable, credible expectation in Chapter 5. Their two experiments found different immediate responses by self-esteem; this should not become a general clinical claim or be conflated with values-affirmation interventions. Primary bibliographic details and abstract were checked, but cumulative evidence has not been reviewed. [Original publication](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2009.02370.x).
- **Health-goal cues:** Papies and colleagues (2014) offer a possible Chapter 13/39 example involving recipe flyers and actual shopping receipts. The stimuli were visible; do not call them subliminal. The paper is a candidate for a bounded case, not sufficient support for a general prescription that subtle cues reliably activate goals without awareness. A fuller check of the study and later evidence should precede incorporation. [Original publication](https://www.nature.com/articles/ijo2013136).

## Coverage of the source collection

Word/PDF versions are grouped below; the inventory preserves all individual files.

| Reading or group | Current coverage | Recommended use |
| --- | --- | --- |
| *AI and Behavioral Economics* | AI assistance is covered; behavioral discovery and the overfitting analogy are largely absent. | Priorities 1 and 3; brief link to Chapter 40. |
| *Impact of ML on Economics* | Prediction/causation, tool selection, intervention benefits, and validation already appear in Chapter 42. | Measurement example in priority 1; subgroup-estimation box in priority 4. |
| *Impact_ML_on_Econ_Summary* slides | Derivative of the Athey chapter. | Use for teaching sequence; cite the published chapter. |
| *Prediction, Judgment and Complexity* | Core argument and terminology already appear in Chapter 42. | Short qualification about conditional complementarity, if needed. |
| *Prediction_Judgment_Complexity_Summary* slides | Derivative of the preceding chapter. | No separate evidentiary contribution. |
| *The Economics of Artificial Intelligence: An Agenda* | Contains the three published chapters above plus broader work on growth, labor, industrial organization, and regulation. | Background reference; its contents alone do not justify expanding this decision-making book into an AI-economics survey. |
| *From Perception to Choice: Understanding the Dimensions of Decision Making* | Its broad dimensions are distributed across the existing book. | Background synthesis; check individual original studies if a particular example is selected. No new organizing framework is needed. |
| *Choosing the Right Research Question in Behavioral Economics* | Evidence-design appendix already covers focused questions, constructs, estimands, feasibility, and comparisons. | At most reuse a strong exercise; avoid duplicating the methods discussion. |
| *Formulating a Strong Research Question for a Behavioral Economics Literature Review* | Dedicated literature-review appendix already covers question formation, searching, comparing evidence, and synthesis. | Largely incorporated in substance. Course-specific rubrics belong in course materials. |
| *Experimental Studies and Replication Failures Across Disciplines* | Evidence-breakdown appendix already provides an extensive, qualified evidence-status map. | Treat as a list of leads; do not import its claims or bibliography wholesale. |
| *Goal Setting and Priming Effects on Behavior* | Chapter 39 already covers goal specificity, learning goals, implementation intentions, WOOP, and limitations. Chapter 13 distinguishes kinds of priming. | Health-cue example is optional, subject to further evidence review. |
| *Priming, Subliminal Messaging, and Positive Thinking* | Much overlaps Chapters 5, 13, 39, the literature-review appendix, and the evidence-status appendix. | Priority 2 is a clear addition; positive self-statements are optional. |
| Instructor notes: *Literature* | Two anchoring references; Chapter 11 and the evidence apparatus already discuss anchoring. | Bibliographic lead list, not a new section. |
| Instructor notes: *Replication Crisis References* | Many listed topics already appear in the evidence-status appendix. | Verify selected references individually; broad annotations do not establish a study's replication status. |

## Source corrections and boundaries

The teaching drafts should be treated as leads to evidence. One concrete error is the subliminal-tape citation: the review lists a different title and *Journal of Applied Psychology, 76*, 119–127. The verified Greenwald et al. paper is *Psychological Science, 2*(2), 119–122, DOI [10.1111/j.1467-9280.1991.tb00112.x](https://doi.org/10.1111/j.1467-9280.1991.tb00112.x). The cross-discipline replication draft also contains an unfinished “Registered Replication Report ().” reference. The instructor list attaches broad replication-crisis claims without consistently naming the corresponding replication evidence.

The draft's facial-feedback account should also not replace the book's more careful distinction between the original pen-in-mouth procedure and other ways of inducing smiles. Likewise, theoretical plausibility, a field setting, or repeated citation does not by itself establish that a priming effect is dependable.

The suggested incorporation is deliberately selective: add examples that do new explanatory work, use links where concepts already have a home, and retain the book's current evidence qualifications. No raw reading, book source, reference list, HTML, or EPUB was modified during this assessment.
