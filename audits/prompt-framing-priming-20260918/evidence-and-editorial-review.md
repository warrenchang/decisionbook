# Prompts, framing, and priming

Date: 18 September 2026. Scope: the existing Chapter 4 AI Research Lens, its exercise and references, and relevant concept-index entries. The baseline preserves the prior learning/metacognition revision and Jennings callout.

## Editorial placement

The new subsection follows the explanation of generative model families and precedes the existing workplace-question example. It distinguishes framing the present decision from the influence of preceding material, then explains why explicit instructions and new evidence are separate explanations for prompt sensitivity. The workplace example illustrates a presupposition; it is not presented as an equivalence-framing experiment. An expanded exercise separates two comparisons rather than changing framing and preceding context simultaneously. Cross-links lead to the existing framing and accessibility chapters; those chapters were not otherwise rewritten.

## Evidence matrix

| Verified primary source | Design/context and measure | Result used | Scientific boundary |
| --- | --- | --- | --- |
| Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *PNAS, 120*(6), e2218523120. [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9963545/); [DOI](https://doi.org/10.1073/pnas.2218523120) | Psychological tasks administered to GPT-3; gain/loss framing contrasts used equivalent gamble problems, counterbalanced option order, and choice probabilities | Framing was among the effects found in the tested GPT-3 system | An observed effect in a particular model and design; neither universal across LLMs nor evidence of shared subjective experience. No new model experiment was run for this revision. |
| Sinclair, A., Jumelet, J., Zuidema, W., & Fernández, R. (2022). Structural persistence in language models: Priming as a window into abstract language representations. *Transactions of the Association for Computational Linguistics, 10*, 1031–1050. [Paper and metadata](https://aclanthology.org/2022.tacl-1.60/); DOI 10.1162/tacl_a_00504 | Controlled Prime-LM sentence corpus and conditional sentence-probability comparisons in neural language models | Transformer models showed structural persistence after a prime, modulated by semantic information | Supports a measured linguistic priming effect; does not by itself establish broader social or behavioral priming, or identical human and machine memory mechanisms. |
| Jumelet, J., Zuidema, W., & Sinclair, A. (2024). Do language models exhibit human-like structural priming effects? In *Findings of the Association for Computational Linguistics: ACL 2024* (pp. 14727–14742). [Paper and metadata](https://aclanthology.org/2024.findings-acl.877/); DOI 10.18653/v1/2024.findings-acl.877 | Analyses of linguistic factors affecting sentence/token predictions in a structural-priming paradigm | Frequency and lexical dependence influenced priming strength | The book uses these specific moderators, not a claim that all properties of human priming transfer to all language models. |

## Interpretation decisions

- Framing: changes to the representation of a problem. The stronger equivalence-framing test holds outcomes, options, and objectives fixed.
- Priming: the influence of preceding material on subsequent processing or response. Conditional-probability evidence supports structural priming in tested language models.
- Do not treat every prompt response as a cognitive bias. Following a format instruction, inferring a demonstrated task, or using new facts may correctly change an answer.
- A workplace cue about employee loyalty is identified as a hypothesis that needs its own test; structural-priming findings do not establish that proposed effect.
- The exercise requires separate manipulations, unchanged task facts, fresh contexts, fixed model/settings, varied condition order, and repeated runs. It is a teaching demonstration, not a reported experiment or a validated debiasing intervention.

## Validation

- Canonical source QA: zero errors and zero warnings; all earlier chapter references and figures retained.
- Bibliography synchronization: 1,010 unique references; three new verified sources for this addition.
- HTML and EPUB rebuilt sequentially. The final wording was rendered and the final EPUB passes freshness and staged/release equality checks.
- EPUB release QA: zero errors. Targeted checks confirm the new subsection, final wording, three citations, and revised exercise are packaged with a unique anchor.
- HTML: all Chapter 4 local content links resolve and IDs are unique. The search index includes the final discussion and retains the prior Chapter 8 metacognition section.
- Browser checks at 1,280 px and 390 px: the Research Lens starts closed, opens and closes, displays the new material and cross-links, and has no horizontal overflow. Desktop and phone layouts were visually reviewed; screenshots and JSON checks accompany this record. Keyboard accessibility was not assessed.
- Figure/table reference QA across 62 sources and both rendered formats: 117 figure labels, 165 table labels, zero issues; report saved in this audit folder.
- `git diff --check`: pass. No commit or push performed.
