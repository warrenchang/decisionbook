"""Check Chapter 27 source coverage and final HTML/EPUB without changing inputs."""
import csv
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from qa_float_references import RenderedFloats, source_inventory

source = ROOT / "chapters/27-markets-mispricing-and-bubbles.qmd"
html = ROOT / "docs/chapters/27-markets-mispricing-and-bubbles.html"
epub = ROOT / "docs/Decision-in-the-Making.epub"
checks = {}
rows = list(csv.DictReader((HERE / "slide-coverage.csv").open()))
checks["63 slides mapped"] = len(rows) == 63 and {int(r["slide"]) for r in rows} == set(range(1, 64)) and all(r["destination"] and r["handling"] for r in rows)
checks["15 hidden slides mapped"] = sum(r["hidden"] == "True" for r in rows) == 15
definitions, _, issues = source_inventory(source, ROOT)
checks["source float references"] = not issues

with zipfile.ZipFile(epub) as z:
    pages = [(name, z.read(name).decode()) for name in z.namelist()
             if name.endswith(".xhtml")]
    chapter_pages = [(name, text) for name, text in pages
                     if 'id="tbl-historical-bubbles"' in text]
checks["unique EPUB chapter"] = len(chapter_pages) == 1
epub_name, epub_text = chapter_pages[0]
required = ["Tulipmania:", "South Sea Bubble:", "Mississippi scheme:",
            "Dot-com innovation", "Thailand, Malaysia, Indonesia",
            "304 traders", "Tucker and Xu (2024)",
            "Flat fundamentals:", "Lottery payoffs and cognitive reflection"]
for fmt, text in [("HTML", html.read_text()), ("EPUB", epub_text)]:
    checks[f"{fmt} required revision content"] = all(s in text for s in required)
    parsed = RenderedFloats(body_is_main=fmt == "EPUB")
    parsed.feed(text)
    local = {unquote(urlsplit(ref).fragment) for ref in parsed.references}
    checks[f"{fmt} all expected floats"] = {d["id"] for d in definitions} <= parsed.floats
    checks[f"{fmt} local prose references"] = not (parsed.floats - local)
    checks[f"{fmt} numbered tables"] = parsed.unnumbered_tables == 0
    checks[f"{fmt} resolved references"] = not parsed.unresolved
    checks[f"{fmt} no raw float references"] = all("@" + d["id"] not in text for d in definitions)

citations = json.loads((ROOT / "citation-audit.json").read_text())
chapter_citations = next(c for c in citations["chapters"] if c["file"] == str(source.relative_to(ROOT)))
checks["chapter citations resolved"] = not chapter_citations["unresolved"]
result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "chapter_reference_count": chapter_citations["reference_count"],
    "epub_chapter": epub_name,
    "sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in [source, html, epub]},
    "scope": "Chapter 27. Separate whole-book QA reports retain any unrelated issues."
}
(HERE / "chapter-validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
