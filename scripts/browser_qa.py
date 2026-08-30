#!/usr/bin/env python3
"""Run desktop and mobile interaction checks against the prebuilt textbook.

Usage from the repository root:
    python scripts/browser_qa.py

Optional dependencies:
    pip install playwright beautifulsoup4
    playwright install chromium

The script also works with a system Chromium/Chrome executable when present.
It writes browser-qa.json and, unless disabled, QA screenshots under qa-screenshots/.
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import shutil
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"
EXPECTED_REFS = json.loads((REPO / "citation-audit.json").read_text(encoding="utf-8"))["summary"]["published_unique_cited_references"]
CSS = (DOCS / "assets/style.css").read_text(encoding="utf-8")
SITE_JS = (DOCS / "assets/site.js").read_text(encoding="utf-8")
# Make theme testing deterministic and avoid writing local storage during an in-memory render.
SITE_JS = SITE_JS.replace("localStorage.getItem('dpn-theme')", "null").replace(
    "localStorage.setItem('dpn-theme',root.dataset.theme)", "void 0"
)
SEARCH_INDEX = json.loads((DOCS / "search-index.json").read_text(encoding="utf-8"))


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def inline_page(relative_path: str) -> str:
    """Inline local assets so the page can be tested without starting a web server."""
    path = DOCS / relative_path
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for tag in soup.find_all("link", rel="stylesheet"):
        tag.decompose()
    for tag in soup.find_all("script", src=True):
        tag.decompose()
    style = soup.new_tag("style")
    style.string = CSS
    soup.head.append(style)
    for image in soup.find_all("img", src=True):
        src = image["src"]
        if src.startswith(("http:", "https:", "data:")):
            continue
        target = (path.parent / src).resolve()
        if target.exists():
            image["src"] = data_uri(target)
    pre = soup.new_tag("script")
    pre.string = "window.fetch=async()=>({json:async()=>" + json.dumps(SEARCH_INDEX) + "});"
    soup.body.append(pre)
    script = soup.new_tag("script")
    script.string = "(()=>{" + SITE_JS + "})();"
    soup.body.append(script)
    return "<!doctype html>" + str(soup)


def chromium_executable() -> str | None:
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        found = shutil.which(name)
        if found:
            return found
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--screenshots-dir",
        type=Path,
        default=REPO / "qa-screenshots",
        help="Directory for browser-QA screenshots.",
    )
    parser.add_argument("--no-screenshots", action="store_true")
    args = parser.parse_args()
    if not args.no_screenshots:
        args.screenshots_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    console_errors: list[str] = []

    def check(name: str, condition: bool, detail: str = "") -> None:
        results.append({"check": name, "pass": bool(condition), "detail": detail})

    with sync_playwright() as playwright:
        launch_kwargs = {"headless": True, "args": ["--no-sandbox"]}
        executable = chromium_executable()
        if executable:
            launch_kwargs["executable_path"] = executable
        browser = playwright.chromium.launch(**launch_kwargs)
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        page.set_content(inline_page("index.html"), wait_until="load")
        check(
            "home-title",
            page.locator("h1").first.inner_text().strip() == "Decision in the Making",
            page.title(),
        )
        part_count = page.locator("section.part-intro").count()
        check("seven-parts", part_count == 7, str(part_count))
        check(
            "home-reading-map",
            page.locator("figure.flow-figure img").count() == 1
            and page.locator("figure.flow-figure img").evaluate("(i)=>i.complete && i.naturalWidth>0"),
        )
        if not args.no_screenshots:
            page.screenshot(path=str(args.screenshots_dir / "home-desktop.png"), full_page=True)

        page.click("#search-button")
        opened = page.locator("#search-dialog").evaluate("(d)=>d.open")
        check("search-dialog-opens", opened, str(opened))
        if not opened:
            page.locator("#search-dialog").evaluate('(d)=>d.setAttribute("open","")')
        page.locator("#search-input").evaluate(
            '(el)=>{el.value="anchoring";el.dispatchEvent(new Event("input",{bubbles:true}))}'
        )
        page.wait_for_timeout(350)
        result_count = page.locator("#search-results .search-hit").count()
        check("full-text-search", result_count > 0, f"{result_count} results")
        first_result = page.locator("#search-results .search-hit").first.inner_text() if result_count else ""
        check("search-relevance", "anchor" in first_result.lower(), first_result[:160])
        if page.locator("#search-dialog").evaluate("(d)=>d.open"):
            page.locator("#search-dialog").evaluate("(d)=>d.close ? d.close() : d.removeAttribute('open')")
        before = page.locator("html").get_attribute("data-theme")
        page.click("#theme-button")
        after = page.locator("html").get_attribute("data-theme")
        check("dark-mode", before != after and after == "dark", f"{before}->{after}")
        page.click("#theme-button")

        page.set_content(inline_page("start-here.html"), wait_until="load")
        check("start-here", "The organizing logic" in page.locator("main").inner_text())

        page.set_content(inline_page("chapters/10-feeling-and-availability-as-shortcuts.html"), wait_until="load")
        check(
            "chapter-figure-loaded",
            page.locator("main figure img").count() == 1
            and page.locator("main figure img").evaluate("(i)=>i.complete && i.naturalWidth>0"),
        )
        table_count = page.locator("main .table-wrapper table").count()
        check("chapter-table-responsive", table_count >= 1, str(table_count))
        toc_count = page.locator("aside.on-page a").count()
        check("chapter-on-page-toc", toc_count > 5, str(toc_count))
        nav_count = page.locator("nav.page-nav a").count()
        check("chapter-prev-next", nav_count == 2, str(nav_count))
        if not args.no_screenshots:
            page.screenshot(path=str(args.screenshots_dir / "chapter-desktop.png"), full_page=False)

        page.set_content(inline_page("references.html"), wait_until="load")
        reference_count = page.locator("main .reference").count()
        check("reference-count", reference_count == EXPECTED_REFS, f"{reference_count} (expected {EXPECTED_REFS})")
        epub = DOCS / "downloads/Decision_Persuasion_Negotiation_Student_Ebook_Revised.epub"
        check("epub-download", epub.exists() and epub.stat().st_size > 1_000_000, f"{epub.stat().st_size if epub.exists() else 0} bytes")

        mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
        mobile.set_content(inline_page("index.html"), wait_until="load")
        check("mobile-menu-button-visible", mobile.locator(".menu-button").is_visible())
        mobile.click(".menu-button")
        check(
            "mobile-sidebar-opens",
            "open" in (mobile.locator(".sidebar").get_attribute("class") or "")
            and mobile.locator(".sidebar-backdrop").is_visible(),
        )
        mobile.wait_for_timeout(300)
        if not args.no_screenshots:
            mobile.screenshot(path=str(args.screenshots_dir / "home-mobile-menu.png"), full_page=False)
        if mobile.locator(".sidebar-backdrop").is_visible():
            mobile.locator(".sidebar-backdrop").evaluate("(e)=>e.click()")
        check("mobile-sidebar-closes", "open" not in (mobile.locator(".sidebar").get_attribute("class") or ""))
        mobile.close()

        page.set_content(inline_page("complete-book.html"), wait_until="domcontentloaded", timeout=120000)
        complete_text = page.locator("main").inner_text()
        check("complete-book-chapters", all(f"Chapter {number}." in complete_text for number in (1, 10, 20, 30, 35)))
        complete_tables = page.locator("main .table-wrapper table").count()
        check("complete-book-tables-responsive", complete_tables >= 36, str(complete_tables))
        browser.close()

    check("console-errors", len(console_errors) == 0, "; ".join(console_errors[:5]))
    report = {
        "status": "PASS" if all(item["pass"] for item in results) else "FAIL",
        "checks": results,
        "console_errors": console_errors,
    }
    (REPO / "browser-qa.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
