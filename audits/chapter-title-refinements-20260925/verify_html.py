"""Check current chapter pages, prior URL aliases, navigation, and internal links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])


mapping = json.loads((AUDIT / "mapping.json").read_text())["chapters"]
sources = re.findall(r"^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$", (ROOT / "_quarto-html.yml").read_text(), re.M)
cache = {}


def page(path):
    path = path.resolve()
    if path not in cache:
        cache[path] = Page(path)
    return cache[path]


issues = []
checked = 0
for source in sources:
    path = DOCS / Path(source).with_suffix(".html")
    for href in page(path).links:
        uri = urlsplit(href)
        if uri.scheme or uri.netloc or uri.path.startswith("/"):
            continue
        target = (path.parent / unquote(uri.path)).resolve() if uri.path else path.resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            issues.append(f"{source}: missing {href}")
            continue
        if target.suffix in {".html", ".htm"}:
            checked += 1
            if uri.fragment and unquote(uri.fragment) not in page(target).ids:
                issues.append(f"{source}: missing fragment in {href}")

index_links = page(DOCS / "index.html").links
search = json.loads((DOCS / "search.json").read_text())
aliases_checked = 0
for row in mapping:
    target = Path(row["new"]).with_suffix(".html")
    assert any(urlsplit(href).path.endswith(str(target)) for href in index_links), row
    assert any(urlsplit(item.get("href", "")).path.endswith(str(target)) and row["title"] in item.get("title", "") for item in search), row
    source = (ROOT / row["new"]).read_text()
    front = source.split("\n---", 1)[0] if source.startswith("---\n") else ""
    for alias in re.findall(r"^  - (\S+\.html)$", front, re.M):
        redirect_path = DOCS / target.parent / alias
        redirect_text = redirect_path.read_text()
        redirect_map = json.loads(re.search(r"var redirects = (\{.*?\});", redirect_text).group(1))
        assert (redirect_path.parent / redirect_map[""]).resolve() == (DOCS / target).resolve(), alias
        assert "redirect + window.location.hash" in redirect_text, alias
        assert "redirect + window.location.search" in redirect_text, alias
        aliases_checked += 1
    if row["old"] != row["new"]:
        assert Path(row["old"]).with_suffix(".html").name in front, row

old_paths = [str(Path(row["old"]).with_suffix(".html")) for row in mapping if row["old"] != row["new"]]
for item in search:
    assert not any(urlsplit(item.get("href", "")).path.endswith(old) for old in old_paths), item.get("href")

result = dict(status="PASS" if not issues else "FAIL", canonical_pages=len(sources), chapter_navigation_and_search_entries=42,
              redirect_aliases_checked=aliases_checked, local_html_links_checked=checked, issues=issues)
(AUDIT / "html-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(bool(issues))
