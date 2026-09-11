# Chapter 4: traffic-light color and duck–rabbit examples

## Artwork and teaching scope

Two new SVGs and matching PNG fallbacks were constructed from scratch. Neither attached illustration was embedded or traced. The traffic signal has new geometry, texture, and surroundings. The ambiguous animal uses a new smooth contour with the historical orientation reversed: duck right, rabbit left. The animal artwork has no visible labels or Easter cues that preselect a response.

The traffic drawing defines one opaque achromatic lens symbol and uses it twice. The PNG's central 121 × 121 target regions were compared: 14,641 identical RGB triplets, maximum difference 0, and R = G = B throughout. An initial gradient introduced one-level raster-rounding differences and was replaced with a uniform gray base before final rendering. Antialiased edges blending with the surroundings are excluded from the interior comparison.

Independent visual inspection found the traffic target subtly warmer in context, not unmistakably red. The text therefore says “may look warmer or reddish,” acknowledges variation, and does not imply a universal perceptual effect or measured effect size. Color constancy is connected to the demonstration without treating illumination inference as its sole mechanism. The duck–rabbit supports both named interpretations; it is explicitly distinguished from the stimuli used in the cited studies.

## Source verification

| Source | Evidence used | Limit |
| --- | --- | --- |
| Bloj, Kersten, & Hurlbert (1999), DOI 10.1038/47245 | Perceived card folding changes color appearance, consistent with interpretation of mutual illumination. | Primary experiment does not test traffic lights. |
| Foster (2011), DOI 10.1016/j.visres.2010.09.006 | Review of color constancy, including adaptation, scene relations and illumination information. | Does not require a separate mandatory illuminant-estimation stage. |
| Shevell & Kingdom (2008), DOI 10.1146/annurev.psych.59.103006.093619 | Contextual influences on color in complex scenes. | General support; the new drawing does not isolate contrast, adaptation or scene interpretation. |
| Brugger & Brugger (1993), DOI 10.2466/pms.1993.76.2.577 | Rabbit naming predominated among 265 Easter visitors; bird naming among 276 October visitors at Zurich Zoo. | Different observational samples, not a randomized seasonal-cue intervention. |
| Dudda et al. (2026), DOI 10.1515/edu-2025-0134 | Around Easter, 157/179 analyzable responses named a bird and 22 a rabbit. | No October group; timing and collection procedures differed. Does not establish absence of any seasonal difference. |

The Dudda paper was published April 30, 2026. Publisher metadata and the author-uploaded published full text were checked. Its finding is described as failure to reproduce rabbit predominance, not a direct repeat of the seasonal comparison. An independent source verifier reviewed the final prose, captions and all five bibliographic entries and found no material scientific issue.

## Release verification

- Full HTML and EPUB renders completed successfully.
- Reference synchronization passed with 829 unique references. Source/HTML QA passed with 0 errors and 0 warnings; EPUB release QA passed with 0 errors.
- Both new illustrations and captions were visually inspected in HTML at 1440/390 pixels and packaged EPUB XHTML at 768/390 pixels: 8 figure placements, 0 issues. Essential traffic-panel labels remain above 12 CSS pixels; neither new figure requires horizontal scrolling.
- Numbering verified: traffic context is Figure 4.3, duck–rabbit Figure 4.4, and the existing predictive-processing diagram Figure 4.5. Five new references appear in both formats.
- Both SVGs parse with unique internal IDs. HTML copies match the final source SVGs and PNG fallbacks. Staged and distributed EPUB files match.
- Whole-book responsive figure checks: 117 HTML placements and 116 EPUB placements; 0 issues in either format.
- Final `git diff --check` passed. Existing user edits and untracked files were preserved; no commit or push was performed.

Focused checks are recorded in `ch04-context-examples-checks-20260910.json`; temporary build logs and visual captures are in `/private/tmp/ch04-context-examples/`. EPUB visual inspection used Chromium with the packaged stylesheet, not an assertion of identical pagination in every e-reader.
