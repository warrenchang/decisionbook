#!/usr/bin/env python3
"""Read-only audit of local links against rendered HTML files and actual IDs.

Run only after the coordinated final HTML build has completed. The sole persistent
write is the requested JSON report; canonical sources and rendered files are read.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import difflib
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import quote, unquote, urljoin, urlsplit


ORIGIN = "https://local-render-audit.invalid"


class Document(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.ids: Counter[str] = Counter()
        self.names: set[str] = set()
        self.links: list[dict] = []
        self.base: str | None = None
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids[values["id"]] += 1
        if tag == "a" and values.get("name"):
            self.names.add(values["name"])
        if tag == "base":
            if self.base is None and "href" in values:
                self.base = values["href"]
            return
        for attribute in ("href", "xlink:href", "src", "poster"):
            if attribute in values and values[attribute] is not None:
                self.links.append({"tag": tag, "attribute": attribute,
                                   "url": values[attribute], "line": self.getpos()[0]})

    handle_startendtag = handle_starttag


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def configured_sources(config: Path) -> list[str]:
    # The checked-in profile uses plain QMD paths for every chapter, part, and
    # appendix. Reject duplicates; the independent inventory check detects a
    # syntax change that this deliberately small reader would otherwise miss.
    sources = re.findall(r"^\s*-\s*(?:part:\s*)?([^\s#]+\.qmd)\s*(?:#.*)?$",
                         config.read_text(), flags=re.M)
    if not sources or len(sources) != len(set(sources)):
        raise ValueError("Expected a nonempty, unique list of configured QMD sources")
    return sources


def audit(render_root: Path, html_sources: list[str]) -> dict:
    render_root = render_root.resolve()
    documents: dict[Path, Document] = {}
    initial_hashes: dict[Path, str] = {}
    issues: list[dict] = []
    counts: Counter[str] = Counter()
    non_html_fragments: list[dict] = []

    def relative(path: Path) -> str:
        try:
            return path.relative_to(render_root).as_posix()
        except ValueError:
            return str(path)

    def document(path: Path) -> Document:
        if path not in documents:
            raw = path.read_bytes()
            initial_hashes[path] = hashlib.sha256(raw).hexdigest()
            documents[path] = Document(raw.decode("utf-8"))
        return documents[path]

    for source_name in html_sources:
        source = render_root / source_name
        if not source.is_file():
            issues.append({"kind": "missing_configured_html", "source": source_name})
            continue
        counts["configured_html_present"] += 1
        doc = document(source)
        page_url = ORIGIN + "/" + quote(source_name, safe="/")
        base_url = urljoin(page_url, doc.base) if doc.base is not None else page_url
        for link in doc.links:
            counts["references_seen"] += 1
            raw_url = link["url"].strip()
            target_url = urlsplit(urljoin(base_url, raw_url))
            if target_url.scheme != "https" or target_url.netloc != urlsplit(ORIGIN).netloc:
                counts["external_or_nonlocal_skipped"] += 1
                continue
            counts["local_references_checked"] += 1
            counts["local_" + link["attribute"]] += 1
            decoded_path = unquote(target_url.path)
            target = (render_root / decoded_path.lstrip("/")).resolve()
            if not target.is_relative_to(render_root):
                issues.append({"kind": "outside_output_root", "source": source_name,
                               **link, "target": str(target)})
                continue
            if decoded_path.endswith("/") or target.is_dir():
                target /= "index.html"
            entry = {"source": source_name, **link, "target": relative(target)}
            if not target.is_file():
                issues.append({"kind": "missing_local_file", **entry})
                continue
            # Browser text-fragment directives are not element IDs. Preserve and
            # validate an ordinary fragment preceding a text directive, if any.
            fragment = unquote(target_url.fragment.split(":~:", 1)[0])
            if not fragment:
                continue
            if target.suffix.lower() not in {".html", ".htm", ".xhtml", ".svg"}:
                non_html_fragments.append({**entry, "fragment": fragment})
                continue
            if target.suffix.lower() == ".svg" and fragment.startswith("svgView("):
                counts["svg_view_fragments_skipped"] += 1
                continue
            target_doc = document(target)
            counts["local_element_fragments_checked"] += 1
            anchors = target_doc.ids.keys() | target_doc.names
            if fragment not in anchors and not (target.suffix.lower() != ".svg" and fragment.lower() == "top"):
                issues.append({"kind": "missing_local_fragment", **entry,
                               "fragment": fragment,
                               "nearby_ids": difflib.get_close_matches(fragment, anchors, n=4, cutoff=.55)})

    duplicate_ids = [{"file": relative(path), "id": key, "count": number}
                     for path, doc in sorted(documents.items())
                     for key, number in doc.ids.items() if number > 1]
    changed_files = [relative(path) for path, old in initial_hashes.items()
                     if not path.is_file() or sha(path) != old]
    return {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "render_root": str(render_root),
        "scope": "All href/xlink:href/src/poster attributes in configured rendered HTML; actual IDs and legacy named anchors in local HTML/SVG targets. External URLs skipped. CSS url(), srcset, JavaScript navigation, and external resources are outside this link audit.",
        "configured_html_count": len(html_sources),
        "counts": dict(counts),
        "parsed_target_files": len(documents),
        "missing_or_invalid_links": issues,
        "duplicate_ids": duplicate_ids,
        "non_html_fragments_not_interpreted": non_html_fragments,
        "files_changed_during_audit": changed_files,
        "rendered_html_snapshot": [
            {"path": relative(path), "sha256": initial_hashes[path],
             "mtime_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()}
            for path in sorted(initial_hashes) if path.is_file()
        ],
        "passed": not issues and not duplicate_ids and not changed_files,
    }


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="decision-html-links-") as folder:
        root = Path(folder)
        (root / "chapters").mkdir()
        (root / "index.html").write_text('<h1 id="home">Home</h1><a href="chapters/test.html#caf%C3%A9">go</a>')
        (root / "chapters/test.html").write_text('''<h1 id="café">Chapter</h1>
<a href="../#home">home</a><a href="./test.html?view=1#caf%C3%A9">same</a>
<a href="#top">top</a><a href="#:~:text=Chapter">text</a><a name="old"></a>
<a href="#old">legacy</a><a href="https://example.com/missing#none">external</a>
<a href="mailto:example@example.com">mail</a><img src="../sample%20image.png">
<a href="../icon.svg#mark">svg</a><a href="../reading.pdf#page=2">pdf</a>''')
        (root / "sample image.png").write_bytes(b"fixture")
        (root / "reading.pdf").write_bytes(b"fixture")
        (root / "icon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><path id="mark"/></svg>')
        result = audit(root, ["index.html", "chapters/test.html"])
        assert result["passed"], result
        assert result["counts"]["external_or_nonlocal_skipped"] == 2
        assert len(result["non_html_fragments_not_interpreted"]) == 1
        with (root / "chapters/test.html").open("a") as handle:
            handle.write('<a href="../lost.html">missing</a><a href="../index.html#absent">bad fragment</a><p id="café">duplicate</p>')
        result = audit(root, ["index.html", "chapters/test.html", "not-built.html"])
        assert not result["passed"]
        assert {entry["kind"] for entry in result["missing_or_invalid_links"]} == {
            "missing_local_file", "missing_local_fragment", "missing_configured_html"}
        assert len(result["duplicate_ids"]) == 1
        (root / "base.html").write_text('<base href="chapters/"><a href="test.html#old">base</a>')
        assert not audit(root, ["base.html"])["missing_or_invalid_links"]
    print("Self-test passed: relative and directory paths, percent encoding, queries, Unicode IDs, named anchors, base URLs, SVG IDs, text fragments, external URLs, missing files/fragments, and duplicate IDs.")


def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", type=Path, default=repo)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("final-html-link-audit.json"))
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    config = args.root / "_quarto-html.yml"
    sources = configured_sources(config)
    inventory = json.loads((args.root / "audits/book-revision-20260910/inventory.json").read_text())
    inventoried = {entry["path"] for entry in inventory["sources"]}
    if set(sources) != inventoried:
        raise ValueError(f"Configuration/inventory mismatch: config-only {set(sources)-inventoried}; inventory-only {inventoried-set(sources)}")
    result = audit(args.root / "docs", [str(Path(name).with_suffix(".html")) for name in sources])
    result["configuration"] = {"path": str(config), "sha256": sha(config),
                               "sources_match_inventory": True}
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"report": str(args.output), "passed": result["passed"],
                      "configured_html": result["configured_html_count"],
                      "counts": result["counts"],
                      "issues": len(result["missing_or_invalid_links"]),
                      "duplicate_ids": len(result["duplicate_ids"]),
                      "changed_files": len(result["files_changed_during_audit"])}))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
