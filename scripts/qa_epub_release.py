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
NCX = "http://www.daisy.org/z3986/2005/ncx/"

EXPECTED_PARTS = [
    "Part I. How a Choice Takes Shape",
    "Part II. Judgment Under Uncertainty",
    "Part III. Risk, Time, Self-Regulation, and a Good Life",
    "Part IV. Strategic and Social Decisions",
    "Part V. Persuasion, Communication, and Connection",
    "Part VI. Negotiating Joint Decisions",
    "Part VII. Designing Better Loops",
]

EXPECTED_PART_CHAPTERS = [
    list(range(1, 8)),
    list(range(8, 16)),
    list(range(16, 23)),
    list(range(23, 30)),
    list(range(30, 35)),
    list(range(35, 39)),
    list(range(39, 42)),
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
    "Follow the Decision Upstream—and Outward",
    "pause without reset",
    "Scheduled cue occasions / days",
    "Index of Concepts",
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
        check("Navigation has 17 compact top-level items", len(top_items) == 17, str(len(top_items)))

        labels: list[str] = []
        all_labels: list[str] = []
        missing_targets: list[str] = []
        all_items = toc.findall(f".//{{{XHTML}}}li") if toc is not None else []
        for item in all_items:
            anchor = item.find(f"{{{XHTML}}}a")
            if anchor is None:
                continue
            all_labels.append(normalized_text(anchor))
            href = anchor.get("href", "").split("#", 1)[0]
            target = posixpath.normpath(posixpath.join(posixpath.dirname(nav_path), href))
            if href and target not in names:
                missing_targets.append(target)
        for item in top_items:
            anchor = item.find(f"{{{XHTML}}}a")
            if anchor is not None:
                labels.append(normalized_text(anchor))
        check("Every navigation target exists", not missing_targets, ", ".join(missing_targets[:5]))
        check(
            "Navigation omits the redundant generated title-page entry",
            "Decision, Persuasion, and Negotiation" not in labels,
        )

        styled_lists = toc.findall(f".//{{{XHTML}}}ol") if toc is not None else []
        styled_items = toc.findall(f".//{{{XHTML}}}li") if toc is not None else []
        unstyled_markers = [
            element
            for element in [*styled_lists, *styled_items]
            if "list-style-type: none" not in element.get("style", "")
        ]
        check(
            "Visible contents suppresses automatic ordered-list counters",
            not unstyled_markers,
            str(len(unstyled_markers)),
        )

        positions = [labels.index(part) if part in labels else -1 for part in EXPECTED_PARTS]
        check("All Part titles appear in order", all(position >= 0 for position in positions) and positions == sorted(positions))

        chapter_numbers = [
            int(match.group(1))
            for label in all_labels
            if (match := re.match(r"^(\d+)\s+", label))
        ]
        check("Chapters are numbered 1 through 41", chapter_numbers == list(range(1, 42)), str(chapter_numbers))

        hierarchy_errors: list[str] = []
        for part_title, expected_numbers in zip(EXPECTED_PARTS, EXPECTED_PART_CHAPTERS):
            part_item = next(
                (
                    item
                    for item in top_items
                    if (anchor := item.find(f"{{{XHTML}}}a")) is not None
                    and normalized_text(anchor) == part_title
                ),
                None,
            )
            nested = part_item.find(f"{{{XHTML}}}ol") if part_item is not None else None
            chapter_items = nested.findall(f"{{{XHTML}}}li") if nested is not None else []
            actual_numbers: list[int] = []
            for chapter_item in chapter_items:
                anchor = chapter_item.find(f"{{{XHTML}}}a")
                match = re.match(r"^(\d+)\s+", normalized_text(anchor)) if anchor is not None else None
                if match:
                    actual_numbers.append(int(match.group(1)))
                if chapter_item.find(f"{{{XHTML}}}ol") is not None:
                    hierarchy_errors.append(f"{part_title} contains section-level navigation")
            if actual_numbers != expected_numbers:
                hierarchy_errors.append(f"{part_title}: expected {expected_numbers}, found {actual_numbers}")
        check(
            "Every chapter is nested under its Part with no section titles",
            not hierarchy_errors,
            "; ".join(hierarchy_errors[:5]),
        )

        nonpart_nested: list[str] = []
        for item in top_items:
            anchor = item.find(f"{{{XHTML}}}a")
            label = normalized_text(anchor)
            if label not in EXPECTED_PARTS and item.find(f"{{{XHTML}}}ol") is not None:
                nonpart_nested.append(label)
        check(
            "Preface and back matter have no section-level navigation",
            not nonpart_nested,
            ", ".join(nonpart_nested),
        )
        check("Navigation contains no section titles", "Learning goals" not in all_labels and "Core Idea" not in all_labels)

        check(
            "Appendices A, B, C, and D are present",
            all(any(label.startswith(f"Appendix {letter}") for label in labels) for letter in "ABCD"),
        )
        appendix_d_position = next((i for i, label in enumerate(labels) if label.startswith("Appendix D")), -1)
        references_position = labels.index("References") if "References" in labels else -1
        index_position = labels.index("Index of Concepts") if "Index of Concepts" in labels else -1
        about_position = labels.index("About This Book") if "About This Book" in labels else -1
        check(
            "Appendices precede References, Index, and About",
            appendix_d_position >= 0
            and references_position > appendix_d_position
            and index_position > references_position
            and about_position > index_position,
            f"Appendix D={appendix_d_position}, References={references_position}, Index={index_position}, About={about_position}",
        )

        ncx_items = [item for item in manifest_items if item.get("media-type") == "application/x-dtbncx+xml"]
        check("One NCX navigation document is declared", len(ncx_items) == 1, str(len(ncx_items)))
        if len(ncx_items) == 1:
            ncx_path = posixpath.normpath(posixpath.join(opf_dir, ncx_items[0].get("href", "")))
            ncx_root = ET.fromstring(archive.read(ncx_path))
            ncx_depth = ncx_root.find(f"{{{NCX}}}head/{{{NCX}}}meta[@name='dtb:depth']")
            check("NCX declares a two-level hierarchy", ncx_depth is not None and ncx_depth.get("content") == "2")
            nav_map = ncx_root.find(f"{{{NCX}}}navMap")
            ncx_top = nav_map.findall(f"{{{NCX}}}navPoint") if nav_map is not None else []
            ncx_top_labels = [
                normalized_text(point.find(f"{{{NCX}}}navLabel/{{{NCX}}}text"))
                for point in ncx_top
            ]
            check(
                "NCX omits the redundant generated title-page entry",
                "Decision, Persuasion, and Negotiation" not in ncx_top_labels,
            )
            ncx_hierarchy_errors: list[str] = []
            for part_title, expected_numbers in zip(EXPECTED_PARTS, EXPECTED_PART_CHAPTERS):
                part_point = next(
                    (
                        point
                        for point in ncx_top
                        if normalized_text(point.find(f"{{{NCX}}}navLabel/{{{NCX}}}text")) == part_title
                    ),
                    None,
                )
                nested_points = part_point.findall(f"{{{NCX}}}navPoint") if part_point is not None else []
                actual_numbers: list[int] = []
                for point in nested_points:
                    label = normalized_text(point.find(f"{{{NCX}}}navLabel/{{{NCX}}}text"))
                    match = re.match(r"^(\d+)\s+", label)
                    if match:
                        actual_numbers.append(int(match.group(1)))
                    if point.find(f"{{{NCX}}}navPoint") is not None:
                        ncx_hierarchy_errors.append(f"{part_title} contains section-level NCX entries")
                if actual_numbers != expected_numbers:
                    ncx_hierarchy_errors.append(f"{part_title}: expected {expected_numbers}, found {actual_numbers}")
            check("NCX mirrors the compact Part-to-Chapter hierarchy", not ncx_hierarchy_errors, "; ".join(ncx_hierarchy_errors[:5]))

        publication_date = package.findtext(f".//{{{DC}}}date", default="")
        check("Compilation date is current", publication_date == date.today().isoformat(), publication_date)

        chapter_files = sorted(name for name in names if re.fullmatch(r"EPUB/text/ch\d{3}\.xhtml", name))
        media_files = sorted(name for name in names if name.startswith("EPUB/media/"))
        check("All 58 source documents are packaged", len(chapter_files) == 58, str(len(chapter_files)))
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
