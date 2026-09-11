# Master decision map: scientific review and integration

## Assessment

The diagram is defensible as the author's organizing framework for examining a decision. It is not an empirically validated seven-stage psychological model, a neural architecture, or a complete causal graph. The five feedback arrows represent possible revisions to how decision functions are carried out; they do not assert that every outcome updates every function, that all updates are conscious, or that learning guarantees improvement.

The review draft needed clearer scope for its missing arrow to context. The integrated figure labels its starting input **Current context & information**. This identifies what is available for a particular decision; it does not assert that context and information remain unchanged across decisions. Learning can alter future information seeking, and action can change future circumstances. The preface and Chapter 1 state this explicitly. The shared feedback path remains directed to interpretation, option construction, prediction, valuation, and choice/implementation.

Prediction and valuation remain separate functions. Revising the importance attached to a consequence is possible, but observations alone do not determine whose interests should count. Chapter 1 makes that distinction explicit. The footer states that functions can overlap or recur; the accompanying discussion treats the downward route as an organizing sequence rather than a mandatory temporal order.

## Sources and limits

- Payne, Bettman, and Johnson (1993), *The Adaptive Decision Maker*, publisher's Chapter 4 summary: https://www.cambridge.org/core/books/abs/adaptive-decision-maker/studying-contingent-decisions-an-integrated-methodology/10711D0BA4975767F1776F6D810DEAEC. The authors discuss multiple strategies and adaptation to decision tasks, effort, and accuracy. This supports caution about portraying a single compulsory sequence; it does not validate the book's particular boxes or arrows. The summary was checked, not the entire book.
- Denrell and March (2001), *Adaptation as Information Restriction: The Hot Stove Effect*, original publisher abstract and bibliographic record: https://pubsonline.informs.org/doi/10.1287/orsc.12.5.523.10092. Their modeling account shows how reproducing apparent success can restrict sampling and sustain mistaken rejection of risky or novel options. It supports the qualifications that learning affects future information and can preserve error. Added to Chapter 1's reference list using the exact entry already in the master bibliography; no new unique reference or deletion.
- Sutton and Barto (2018), *Reinforcement Learning: An Introduction*, second-edition publisher description: https://mitpress.mit.edu/9780262039246/reinforcement-learning/. The agent–environment learning framework supplies a relevant comparison, not an identification of human decision-making with one reinforcement-learning algorithm. Attempts to open the author-hosted full PDF timed out; this review does not claim a fresh full-book reading. No additional in-text claim relies on uninspected passages.

## Changes incorporated

- Updated `scripts/build_master_loop_figures.py` so the canonical SVG is reproducible.
- Replaced `figures/master-loop.svg` and its PNG fallback with the corrected five-target feedback diagram.
- Revised the preface figure caption, alternative text, and discussion, retaining the hiring-committee example.
- Updated the reader's guide and Chapter 1 to explain feedback targets, future context/information, and the limits of learning from rewards.
- Retained the part reading maps, which depict reading order rather than this feedback network. The old unreferenced portrait/interlude assets are outside the canonical placements of this diagram.

Verification results and figure placement checks are recorded in this folder. The preceding review draft is preserved separately as a historical artifact.
