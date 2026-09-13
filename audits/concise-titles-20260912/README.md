# Concise chapter titles — 12 September 2026

Applied the requested titles for Chapters 3–6 and 9. Chapter 11 uses **Anchors, Halos, and Decoys**, naming its three principal mechanisms. Each retains one italic subtitle, using the earlier descriptive phrase.

| Chapter | Title | Subtitle |
| --- | --- | --- |
| 3 | Limited Attention | What Becomes Evidence? |
| 4 | The Predictive Mind | Perception Is Inference |
| 5 | Expectations | When Predictions Become Causes |
| 6 | Valuation | How Options Become Worth Choosing |
| 9 | Availability, Affect, and Representativeness | What Feels Likely |
| 11 | Anchors, Halos, and Decoys | When Context Rewrites Comparison |

The six former section IDs are explicitly retained on the H1s. Filenames and chapter-start anchors are unchanged. Three chapter-name links now use the new titles. Chapter discussions and references were preserved.

Verification: HTML and EPUB rebuilt; all 42 chapter titles and single-subtitle openings checked; sidebar labels and the six changed EPUB contents entries verified. Source QA, bibliography synchronization, HTML links (8,020 local references), and EPUB package/internal links all passed. Desktop and phone previews inspected for Chapters 9 and 11. The EPUB visual check uses packaged XHTML in Chromium. `git diff --check` passed.

The reusable check script follows the earlier opening audit, overriding its six expected titles and subtitles from changes.json. It uses the existing HTML build and an extracted EPUB under OPENING_CHECK_TEMP. It requires Playwright and local Chrome. No commit or push was performed for this title revision.
