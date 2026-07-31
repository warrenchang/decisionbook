# Decision, Persuasion, and Negotiation — GitHub-ready online textbook

The student-facing website is already built in `docs/`. Upload the complete repository to GitHub and publish it with GitHub Pages; students can then open the book immediately in a browser.

## Publish with GitHub Pages

1. Create a GitHub repository and upload **all contents of this folder**.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose either:
   - **GitHub Actions** (the included `.github/workflows/pages.yml` deploys `docs/`), or
   - **Deploy from a branch**, select the default branch and `/docs`.
4. Save. GitHub will display the public course address after deployment.

No site generator, package manager, or external web service is required. All links are relative, and `docs/.nojekyll` lets GitHub serve the prebuilt files as-is.

## Preview locally

```bash
python -m http.server 8000 --directory docs
```

Then open the local address shown by Python.

## What students receive

- 35 chapters in seven cumulative parts.
- A **Start Here** guide and seven part-overview pages.
- One accessible conceptual figure per chapter plus a whole-book reading map.
- Responsive HTML tables, full-text search, dark mode, reading progress, mobile navigation, and print styles.
- Chapter-specific reference lists and a master bibliography containing only cited works.
- A complete single-page edition and a downloadable EPUB.

## Repository map

- `docs/` — publishable website; this is what GitHub Pages serves.
- `chapters/` — editable Markdown chapter sources.
- `parts/` and `start-here.md` — editable orientation and transition pages.
- `appendices/` — portable tools and the corrected example index.
- `figures/` — SVG web illustrations and PNG EPUB illustrations.
- `book.md` — combined book source used for the EPUB.
- `CITATION_AUDIT.md` and `citation-audit.json` — reference correspondence audit.
- `STRUCTURE_AND_EDITORIAL_REPORT.md` — rationale for the revised flow.
- `QA_REPORT.md` — structural, citation-correspondence, link, accessibility, and EPUB checks.
- `BROWSER_QA.md` and `browser-qa.json` — desktop/mobile interaction checks in Chromium (added after the browser QA run).

## Editing and release maintenance

The checked-in Markdown files are the canonical editable manuscript; `docs/` is the prebuilt student release. Because the release is already built, no generator is required to deploy it. After editorial changes, update the corresponding HTML release files and run `python scripts/qa_repository.py`. The optional Chromium interaction audit is documented in `scripts/README.md`.

The two DOCX-conversion scripts in `scripts/` are provenance helpers that require the original source documents and reproduce the source-extraction layer. They are not required for deployment, and the finished Markdown, figures, audits, and prebuilt HTML in this repository remain authoritative.

No license has been added. Add the license you want students and other users to follow before making the repository public.
# decisionbook
