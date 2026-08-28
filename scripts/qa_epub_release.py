#!/usr/bin/env python3
"""Validate the canonical EPUB release and write a concise QA report."""

from __future__ import annotations

import hashlib
import posixpath
import re
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
EPUB = ROOT / "docs" / "Decision-Persuasion-and-Negotiation.epub"
STAGED_EPUB = ROOT / "_epub" / EPUB.name
REPORT = ROOT / "EPUB_QA_REPORT.md"

XHTML = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
CONTAINER = "urn:oasis:names:tc:opendocument:xmlns:container"

EXPECTED_PARTS = [
    "Part I. The Decision-Making Process",
    "Part II. Attention, Prediction, and Expectation",
    "Part III. Heuristics, Biases, and Probability Judgment",
    "Part IV. Risk, Experience, Time, and Self-Control",
    "Part V. Money, Finance, and Well-Being",
    "Part VI. Strategic and Social Decisions",
    "Part VII. Influence and Persuasion",
    "Part VIII. Communication and Connection",
    "Part IX. Negotiation",
    "Part X. Behavior and Decision Design",
]

REQUIRED_CONTENT = [
    "Probability Judgment",
    "Risky Decision-Making",
    "Prospect Theory",
    "Decisions from Experience",
    "Intertemporal Decision-Making",
    "Mental Accounting",
    "Behavioral Finance",
    "Asset Bubbles",
    "Subjective Well-Being",
    "Strategic Interdependence",
    "Behavioral Game Theory",
    "panda",
    "monkey",
    "banana",
    "33.1%",
    "25.4%",
    "36.5%",
    "Replication Crisis",
    "Publication Bias",
    "Underpowered Studies",
    "Data Fabrication",
    "Registered Reports",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_text(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def main() -> int:
    errors: list[str] = []
    checks: list[tuple[str, str]] = []

    def check(label: str, condition: bool, detail: str = "") -> None:
        checks.append((label, "PASS" if condition else "FAIL"))
        if not condition:
            errors.append(f"{label}: {detail or 'check failed'}")

    check("Canonical EPUB exists", EPUB.is_file(), str(EPUB))
    if not EPUB.is_file():
        REPORT.write_text("# EPUB QA report\n\n**Release status: FAIL**\n\nCanonical EPUB is missing.\n", encoding="utf-8")
        return 1

    if STAGED_EPUB.is_file():
        check("Staged and released EPUBs match", sha256(STAGED_EPUB) == sha256(EPUB))

    with zipfile.ZipFile(EPUB) as archive:
        members = archive.infolist()
        names = {member.filename for member in members}
        check("ZIP integrity", archive.testzip() is None)
        check(
            "EPUB mimetype is first and uncompressed",
            bool(members)
            and members[0].filename == "mimetype"
            and members[0].compress_type == zipfile.ZIP_STORED
            and archive.read("mimetype") == b"application/epub+zip",
        )

        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find(f".//{{{CONTAINER}}}rootfile")
        opf_path = rootfile.get("full-path", "") if rootfile is not None else ""
        check("Container identifies package document", bool(opf_path) and opf_path in names, opf_path)

        package = ET.fromstring(archive.read(opf_path))
        manifest_items = package.findall(f".//{{{OPF}}}manifest/{{{OPF}}}item")
        manifest = {item.get("id", ""): item for item in manifest_items}
        opf_dir = posixpath.dirname(opf_path)
        manifest_paths = {
            item_id: posixpath.normpath(posixpath.join(opf_dir, item.get("href", "")))
            for item_id, item in manifest.items()
        }
        missing_manifest = sorted(path for path in manifest_paths.values() if path not in names)
        check("Every manifest resource exists", not missing_manifest, ", ".join(missing_manifest[:5]))

        spine_refs = [item.get("idref", "") for item in package.findall(f".//{{{OPF}}}spine/{{{OPF}}}itemref")]
        missing_spine = [item_id for item_id in spine_refs if item_id not in manifest]
        check("Every spine reference resolves", not missing_spine, ", ".join(missing_spine[:5]))

        nav_items = [item for item in manifest_items if "nav" in item.get("properties", "").split()]
        check("One navigation document is declared", len(nav_items) == 1, str(len(nav_items)))
        nav_path = posixpath.normpath(posixpath.join(opf_dir, nav_items[0].get("href", "")))
        nav_bytes = archive.read(nav_path)
        nav_text = nav_bytes.decode("utf-8")
        nav_root = ET.fromstring(nav_bytes)
        toc = next(
            (
                element
                for element in nav_root.findall(f".//{{{XHTML}}}nav")
                if element.get(f"{{{EPUB_NS}}}type") == "toc"
            ),
            None,
        )
        check("Navigation contains a table of contents", toc is not None)
        toc_list = toc.find(f"{{{XHTML}}}ol") if toc is not None else None
        top_items = toc_list.findall(f"{{{XHTML}}}li") if toc_list is not None else []
        check("Navigation has 65 top-level book items", len(top_items) == 65, str(len(top_items)))

        labels: list[str] = []
        missing_targets: list[str] = []
        for item in top_items:
            anchor = item.find(f"{{{XHTML}}}a")
            if anchor is None:
                continue
            labels.append(normalized_text(anchor))
            href = anchor.get("href", "").split("#", 1)[0]
            target = posixpath.normpath(posixpath.join(posixpath.dirname(nav_path), href))
            if href and target not in names:
                missing_targets.append(target)
        check("Every top-level navigation target exists", not missing_targets, ", ".join(missing_targets[:5]))

        positions = [labels.index(part) if part in labels else -1 for part in EXPECTED_PARTS]
        check("All ten Part titles appear in order", all(position >= 0 for position in positions) and positions == sorted(positions))

        chapter_numbers = [
            int(value)
            for value in re.findall(r'<span class="header-section-number">(\d+)</span>', nav_text)
        ]
        check("Chapters are numbered 1 through 48", chapter_numbers == list(range(1, 49)), str(chapter_numbers))
        check(
            "Appendices A, B, C, and D are present",
            all(any(label.startswith(f"Appendix {letter}") for label in labels) for letter in "ABCD"),
        )

        publication_date = package.findtext(f".//{{{DC}}}date", default="")
        check("Compilation date is current", publication_date == date.today().isoformat(), publication_date)

        chapter_files = sorted(name for name in names if re.fullmatch(r"EPUB/text/ch\d{3}\.xhtml", name))
        media_files = sorted(name for name in names if name.startswith("EPUB/media/"))
        check("All 65 source documents are packaged", len(chapter_files) == 65, str(len(chapter_files)))
        check("Book figures and cover are packaged", len(media_files) >= 71, str(len(media_files)))

        searchable = "\n".join(
            archive.read(name).decode("utf-8", "ignore")
            for name in sorted(names)
            if name.endswith((".xhtml", ".svg", ".opf"))
        )
        for phrase in REQUIRED_CONTENT:
            check(f"Required content: {phrase}", phrase.lower() in searchable.lower())
        for phrase in ("Start Here", "Start reading", "Browse references"):
            check(f"Removed reader text: {phrase}", phrase.lower() not in searchable.lower())
        check("Removed acronym from reader package", re.search(r"\bDPN\b", searchable, flags=re.IGNORECASE) is None)
        check("Behavioral Economics is italicized in About", "<em>Behavioral Economics</em>" in searchable)

    status = "PASS" if not errors else "FAIL"
    lines = [
        "# EPUB QA report",
        "",
        f"**Release status: {status}**",
        "",
        f"Artifact: `docs/{EPUB.name}`",
        "",
        "| Check | Result |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {label.replace('|', '/')} | **{result}** |" for label, result in checks)
    lines.extend(["", "## Issues", ""])
    lines.extend(f"- {error}" for error in errors)
    if not errors:
        lines.append("No package, navigation, numbering, date, or required-content issues were found.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"EPUB QA {status}: {len(errors)} error(s); report={REPORT}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
