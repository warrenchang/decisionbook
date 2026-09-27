"""Check source preservation and presence of the Behave additions in both editions.

Run from any directory after rendering HTML and EPUB. Full release checks remain
in scripts/qa_quarto_book.py, qa_epub_release.py, and qa_float_references.py.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parent.parent
ANCHORS = {
    "chapters/01-understanding-decision-making.qmd": ["a-decision-has-a-history"],
    "chapters/06-valuation.qmd": ["reappraisal-and-emotional-learning", "hormones-and-social-context"],
    "chapters/07-rationalization.qmd": ["dehumanization-and-moral-disengagement"],
    "chapters/08-intuition-and-deliberation.qmd": ["moral-intuition-and-reasoning"],
    "chapters/20-intertemporal-decision-making.qmd": ["development-and-peer-context", "childhood-conditions-and-development"],
    "chapters/25-cooperation-and-social-preferences.qmd": ["sacred-values-and-material-tradeoffs", "early-social-evaluation-and-replication"],
    "chapters/29-culture-and-identity.qmd": ["how-livelihoods-can-shape-cultural-learning", "stereotypes-of-warmth-and-competence", "rank-control-and-stress", "a-social-climate-can-outlast-its-founders"],
    "chapters/34-connection.qmd": ["empathy-compassion-and-personal-distress"],
    "appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd": ["genes-develop-in-environments", "heritability-describes-variation", "experience-and-gene-regulation", "kinship-and-social-group-markers", "neural-preparation-and-conscious-choice"],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class HtmlIDs(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = Counter()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if "id" in dict(attrs):
            self.ids[dict(attrs)["id"]] += 1


errors, records = [], []
epub_path = ROOT / "docs/Decision-in-the-Making.epub"
epub_ids = Counter()
with ZipFile(epub_path) as archive:
    for name in archive.namelist():
        if name.endswith(".xhtml"):
            doc = ET.fromstring(archive.read(name))
            epub_ids.update(e.attrib["id"] for e in doc.iter() if "id" in e.attrib)

for name, anchors in ANCHORS.items():
    source = ROOT / name
    text = source.read_text()
    html = ROOT / "docs" / Path(name).with_suffix(".html")
    html_ids = HtmlIDs(html.read_text()).ids
    baseline = ROOT / "tmp/behave-20260927/before" / name
    old_ids = set(re.findall(r"\{[^}\n]*#([A-Za-z][\w:.-]*)", baseline.read_text())) if baseline.exists() else None
    new_ids = set(re.findall(r"\{[^}\n]*#([A-Za-z][\w:.-]*)", text))
    removed = sorted(old_ids - new_ids) if old_ids is not None else None
    if removed:
        errors.append(f"Removed old anchors in {name}: {removed}")
    for anchor in anchors:
        if anchor not in new_ids or html_ids[anchor] != 1 or epub_ids[anchor] != 1:
            errors.append(f"Anchor {anchor}: source={anchor in new_ids}, HTML={html_ids[anchor]}, EPUB={epub_ids[anchor]}")
    records.append({"source": name, "source_sha256": sha(source), "html_sha256": sha(html), "new_anchors": anchors, "removed_baseline_anchors": removed})

fly_name = "chapters/08-intuition-and-deliberation.qmd"
fly_before = ROOT / "tmp/behave-20260927/before" / fly_name
fly_preserved = None
if fly_before.exists():
    pattern = r"\[\]\{#implicit-knowledge-and-learned-intuition\}.*?(?=\n## )"
    old = re.search(pattern, fly_before.read_text(), re.S).group()
    current = re.search(pattern, (ROOT / fly_name).read_text(), re.S).group()
    fly_preserved = old == current
    if not fly_preserved:
        errors.append("Prior implicit-knowledge passage changed")

manifest = json.loads((AUDIT / "source-manifest.json").read_text())
source_checks = []
for source in manifest["sources"]:
    path = Path(source["source"])
    unchanged = sha(path) == source["sha256"] if path.exists() else None
    source_checks.append({"id": source["id"], "sha256_unchanged": unchanged})
    if unchanged is False:
        errors.append(f"Supplied PDF changed: {source['id']}")

report = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "FAIL" if errors else "PASS",
    "scope": "19 Behave anchors across nine edited chapter/appendix sources; original PDFs and baseline anchors when locally available. Concurrent unrelated edits are not attributed to this integration.",
    "source_count": len(source_checks), "new_anchor_count": sum(map(len, ANCHORS.values())),
    "original_pdf_checks": source_checks,
    "prior_implicit_knowledge_passage_unchanged": fly_preserved,
    "sources_and_outputs": records,
    "epub_sha256": sha(epub_path), "errors": errors,
}
(AUDIT / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": report["status"], "new_anchors": report["new_anchor_count"], "original_PDFs_unchanged": sum(x["sha256_unchanged"] is True for x in source_checks), "errors": errors}, indent=2))
raise SystemExit(bool(errors))
