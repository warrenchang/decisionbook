# GitHub upload checklist

1. Create a new GitHub repository.
2. Upload **every file and folder** in this package, including hidden folders such as `.github` and files such as `.nojekyll`.
3. Open **Settings → Pages**.
4. Choose one publishing method:
   - **GitHub Actions:** select GitHub Actions as the source; the included workflow deploys the prebuilt `docs/` folder after each push to `main` or `master`.
   - **Deploy from a branch:** select the default branch and the `/docs` folder.
5. Wait for deployment to finish and open the public Pages address shown by GitHub.
6. Test the home page, **Start Here**, one chapter, search, dark mode, mobile navigation, the complete-book page, references, and the EPUB download.
7. Before later releases, run `python scripts/qa_repository.py` from the repository root and publish only when `QA_REPORT.md` reports **PASS**. For a full interaction check, follow `scripts/README.md` and run `python scripts/browser_qa.py`.
8. The supplied release already passed both the structural QA and desktop/mobile Chromium interaction audit; see `QA_REPORT.md` and `BROWSER_QA.md`.

For a local preview:

```bash
python -m http.server 8000 --directory docs
```
