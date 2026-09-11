# Chapter 4: generative AI and predictive processing

## Scope

Added a discussion under `#generative-ai-and-predictive-processing`, one learning objective, and an exploratory Practice Lab extension. Connected the discussion to Figure 4.1, Chapter 42, and the concept index. Existing figure sources were preserved.

## Evidence and boundaries

| Teaching claim | Primary source | Boundary maintained |
| --- | --- | --- |
| Autoregressive text generation estimates the next token from available context and previous output. | Vaswani et al. (2017), *Attention Is All You Need*, model architecture; Brown et al. (2020), *Language Models Are Few-Shot Learners*. | Tokens are not necessarily whole words. Sampling need not choose the most probable token. The next output position is not necessarily a future event. |
| Instructions and examples can change performance without a weight update. | Brown et al. (2020), abstract and discussion of in-context learning. | Ordinary prompting changes current representations; it is distinct from retraining parameters. Performance differs across tasks. |
| Learned structure and present context offer a comparison between LLMs and perceptual inference. | Clark (2013), *Whatever Next?*, together with the computational sources above. | Explicitly a teaching analogy, not evidence for identical brain/model architectures or learning rules. Perception involves sensory and bodily signals and opportunities to act for further evidence. |
| Diffusion can refine an image representation, or a group of video frames, under conditioning information. | Rombach et al. (2022), §§3.1–3.3; Ho et al. (2022), §§2–3.1. | Not all generative models predict pixels or frames sequentially. Video diffusion and autoregressive extension can coexist. |

The bank completions are labeled illustrative, not measured outputs. The managerial example is an application of the analogy, not a reported experiment. The practice exercise uses fixed observations, the same model and settings, fresh conversations, and repetitions; it explicitly does not establish a general causal effect. Plausible generation is distinguished from external verification and validated forecasting.

Primary publication links are included in the chapter bibliography. Author/title/year/venue metadata were checked against official proceedings and published papers; the media page ranges were independently verified. No unverified page ranges were added for the two language-model papers.

## Independent review

The source-verifier agent reviewed the complete new discussion and exercise, finding no material scientific error. Its suggestion to use a fresh conversation with the same model and settings for every trial was incorporated before rendering.

## Release verification

- Full HTML and EPUB renders completed successfully.
- Reference synchronization: 824 unique references; check passed.
- Source/HTML QA: 0 errors, 0 warnings. EPUB release QA: 0 errors; staged and distributed EPUB files match.
- New discussion and Practice Lab inspected visually at HTML widths 1440/390 and EPUB widths 768/390. No clipping or page overflow. EPUB inspection used the packaged XHTML and stylesheet in Chromium; it does not assert identical pagination in every e-reader.
- New discussion text matches between HTML and EPUB. Figure 4.1 and Chapter 42 links resolve in both formats. Chapter 42 and concept-index return links resolve. All four new references are present in both formats.
- Book-wide responsive figure QA: 115 HTML placements and 114 EPUB placements, 0 issues in either format.
- `git diff --check` passed.

The focused output checks are recorded in `ch04-generative-ai-render-checks-20260910.json`. The build logs and visual captures are in `/private/tmp/ch04-generative-ai/`. The existing repository QA scripts reproduce the reference, source/HTML, EPUB package, and responsive-figure checks.
