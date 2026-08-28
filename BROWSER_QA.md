# Browser interaction report

**Release status: PASS**

The prebuilt site was exercised in headless Chromium at desktop and mobile viewport sizes. The browser audit used the actual site JavaScript, stylesheet, search index, HTML pages, figures, and EPUB contained in this release.

| Interaction or page | Result |
|---|---:|
| Home page title and seven-part map | Pass |
| Whole-book reading-map figure | Pass |
| Search dialog opens | Pass |
| Full-text search returns relevant results for “anchoring” | Pass |
| Light/dark theme toggle | Pass |
| Preface page | Pass |
| Chapter figure loads | Pass |
| Chapter table is in a responsive wrapper | Pass |
| On-page table of contents | Pass |
| Previous/next chapter navigation | Pass |
| Master bibliography contains 477 entries | Pass |
| EPUB download exists and is nonempty | Pass |
| Mobile menu opens and closes at 390 × 844 | Pass |
| Complete-book page contains Chapters 1, 10, 20, 30, and 35 | Pass |
| Complete-book page contains all 36 responsive tables | Pass |
| Browser console errors | 0 |

The machine-readable results are in `browser-qa.json`. The reproducible audit is `scripts/browser_qa.py`.
