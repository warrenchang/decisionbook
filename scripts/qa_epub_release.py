#!/usr/bin/env python3
"""Validate the canonical EPUB release and write a concise QA report."""

from __future__ import annotations

import hashlib
import posixpath
import re
import zipfile
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
EPUB = ROOT / "docs" / "Decision-in-the-Making.epub"
STAGED_EPUB = ROOT / "_epub" / EPUB.name
REPORT = ROOT / "EPUB_QA_REPORT.md"

XHTML = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
CONTAINER = "urn:oasis:names:tc:opendocument:xmlns:container"
NCX = "http://www.daisy.org/z3986/2005/ncx/"
MATHML = "http://www.w3.org/1998/Math/MathML"

EXPECTED_PARTS = [
    "Part I. How a Choice Takes Shape",
    "Part II. Judgment Under Uncertainty",
    "Part III. Risk, Time, and Well-Being",
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

EXPECTED_APPENDICES = [
    ("Appendix A", "Rational Choice and Decision Analysis"),
    ("Appendix B", "Evolutionary Explanations of Value, Choice, and Rationality"),
    ("Appendix C", "Portable Tools"),
    ("Appendix D", "Index of Major Examples"),
    ("Appendix E", "Running an Experimental Study"),
    ("Appendix F", "When Evidence Breaks"),
]

REQUIRED_CONTENT = [
    "How Decisions Should Be Made—and How They Actually Are",
    "Building a Better Decision: Alternatives, Opportunity Cost, Information, and Robustness",
    "Rational Choice and Decision Analysis",
    "Probability Judgment",
    "Risky Decision-Making",
    "Prospect Theory",
    "Decisions from Experience",
    "Intertemporal Decision-Making",
    "Mental Accounting",
    "Deciding for a Better Life",
    "Behavioral Finance",
    "Asset Bubbles",
    "Subjective Well-Being",
    "Social Norms and Conformity",
    "Descriptive norm",
    "Injunctive norm",
    "Groupthink",
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
    "A Decision Is Already in the Making",
    "At 3:17 p.m.",
    "The decision is already in the making.",
    "Predictive processing and predictive judgment ask different questions",
    "Prediction is not responsibility",
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

    source_inputs = [
        *ROOT.glob("*.qmd"),
        *ROOT.glob("chapters/*.qmd"),
        *ROOT.glob("parts/*.qmd"),
        *ROOT.glob("appendices/*.qmd"),
        *ROOT.glob("_quarto*.yml"),
        ROOT / "epub-custom.css",
        ROOT / "filters" / "epub-parts.lua",
        ROOT / "scripts" / "normalize_epub_toc.py",
        ROOT / "scripts" / "sync_epub_release.py",
    ]
    source_inputs = [path for path in source_inputs if path.is_file()]
    latest_source = max(source_inputs, key=lambda path: path.stat().st_mtime_ns)
    check(
        "Released EPUB is newer than every source and EPUB-build input",
        EPUB.stat().st_mtime_ns >= latest_source.stat().st_mtime_ns,
        f"newest input is {latest_source.relative_to(ROOT)}",
    )

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

        css_paths = [
            manifest_paths[item_id]
            for item_id, item in manifest.items()
            if item.get("media-type") == "text/css" and manifest_paths[item_id] in names
        ]
        packaged_css = "\n".join(archive.read(path).decode("utf-8", "ignore") for path in css_paths)
        table_cell_rule = re.search(r"th\s*,\s*td\s*\{(?P<body>.*?)\}", packaged_css, flags=re.DOTALL | re.I)
        check(
            "EPUB table cells have visible borders",
            table_cell_rule is not None and "border:" in table_cell_rule.group("body").lower(),
            ", ".join(css_paths),
        )
        check(
            "EPUB table headers have a contrasting background",
            re.search(r"thead\s+th\s*\{[^}]*background-color\s*:", packaged_css, flags=re.DOTALL | re.I)
            is not None,
            ", ".join(css_paths),
        )

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
        check("Navigation has 19 compact top-level items", len(top_items) == 19, str(len(top_items)))

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
            "Decision in the Making" not in labels,
        )

        preface_item = next(
            (
                item
                for item in top_items
                if (anchor := item.find(f"{{{XHTML}}}a")) is not None
                and normalized_text(anchor).startswith("Preface:")
            ),
            None,
        )
        preface_anchor = preface_item.find(f"{{{XHTML}}}a") if preface_item is not None else None
        preface_href = preface_anchor.get("href", "").split("#", 1)[0] if preface_anchor is not None else ""
        preface_path = posixpath.normpath(posixpath.join(posixpath.dirname(nav_path), preface_href)) if preface_href else ""
        preface_text = ""
        if preface_path in names:
            preface_text = normalized_text(ET.fromstring(archive.read(preface_path)))
        check(
            "Preface contains the current hiring-committee opening",
            "At 3:17 p.m." in preface_text,
            preface_path,
        )
        check(
            "Preface contains the current closing sentence",
            "The decision is already in the making." in preface_text,
            preface_path,
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
            "Appendices A through F are present",
            all(any(label.startswith(f"Appendix {letter}") for label in labels) for letter in "ABCDEF"),
        )
        appendix_labels = [label for label in labels if label.startswith("Appendix ")]
        check(
            "Appendices have the intended order and titles",
            len(appendix_labels) >= len(EXPECTED_APPENDICES)
            and all(
                appendix_labels[index].startswith(prefix) and title in appendix_labels[index]
                for index, (prefix, title) in enumerate(EXPECTED_APPENDICES)
            ),
            " | ".join(appendix_labels[:6]),
        )
        appendix_f_position = next((i for i, label in enumerate(labels) if label.startswith("Appendix F")), -1)
        references_position = labels.index("References") if "References" in labels else -1
        index_position = labels.index("Index of Concepts") if "Index of Concepts" in labels else -1
        about_position = labels.index("About This Book") if "About This Book" in labels else -1
        check(
            "Appendices precede References, Index, and About",
            appendix_f_position >= 0
            and references_position > appendix_f_position
            and index_position > references_position
            and about_position > index_position,
            f"Appendix F={appendix_f_position}, References={references_position}, Index={index_position}, About={about_position}",
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
                "Decision in the Making" not in ncx_top_labels,
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

        identifier = package.findtext(f".//{{{DC}}}identifier", default="")
        publisher = package.findtext(f".//{{{DC}}}publisher", default="")
        rights = package.findtext(f".//{{{DC}}}rights", default="")
        subjects = [normalized_text(element) for element in package.findall(f".//{{{DC}}}subject")]
        metadata_entries = package.findall(f".//{{{OPF}}}metadata/{{{OPF}}}meta")
        properties: dict[str, list[str]] = {}
        for element in metadata_entries:
            property_name = element.get("property", "")
            if property_name:
                properties.setdefault(property_name, []).append(normalized_text(element))
        check(
            "EPUB uses the stable publication identifier",
            identifier == "urn:uuid:d5f0cd81-a793-488a-87d3-47257fdb4c0d",
            identifier,
        )
        check("EPUB identifies its publisher", publisher == "Huanren Warren Zhang", publisher)
        check("EPUB states publication rights", "Huanren Warren Zhang" in rights and "rights reserved" in rights.lower(), rights)
        check(
            "EPUB carries subject metadata",
            {"Decision science", "Behavioral economics", "Negotiation"}.issubset(set(subjects)),
            ", ".join(subjects),
        )
        check(
            "EPUB declares textual and visual access modes",
            {"textual", "visual"}.issubset(set(properties.get("schema:accessMode", []))),
            ", ".join(properties.get("schema:accessMode", [])),
        )
        check(
            "EPUB declares MathML and alternative-text accessibility features",
            {"MathML", "alternativeText"}.issubset(set(properties.get("schema:accessibilityFeature", []))),
            ", ".join(properties.get("schema:accessibilityFeature", [])),
        )
        check(
            "EPUB includes an accessibility summary",
            bool(properties.get("schema:accessibilitySummary", [])),
        )

        chapter_files = sorted(name for name in names if re.fullmatch(r"EPUB/text/ch\d{3}\.xhtml", name))
        media_files = sorted(name for name in names if name.startswith("EPUB/media/"))
        check("All 60 source documents are packaged", len(chapter_files) == 60, str(len(chapter_files)))
        check("Book figures and cover are packaged", len(media_files) >= 71, str(len(media_files)))

        malformed_xhtml: list[str] = []
        overnested_callout_titles: list[str] = []
        parsed_chapters: dict[str, ET.Element] = {}
        for chapter_path in chapter_files:
            try:
                chapter_root = ET.fromstring(archive.read(chapter_path))
            except ET.ParseError as error:
                malformed_xhtml.append(f"{chapter_path}: {error}")
                continue
            parsed_chapters[chapter_path] = chapter_root
            for div in chapter_root.findall(f".//{{{XHTML}}}div"):
                if "callout-title" not in div.get("class", "").split():
                    continue
                bad_heading = any(div.find(f".//{{{XHTML}}}h{level}") is not None for level in range(1, 7))
                bad_table = div.find(f".//{{{XHTML}}}table") is not None
                bad_body = any(
                    "callout-body" in child.get("class", "").split()
                    for child in div.findall(f".//{{{XHTML}}}div")
                )
                if bad_heading or bad_table or bad_body:
                    overnested_callout_titles.append(chapter_path)
                    break
        check("Every packaged chapter is well-formed XHTML", not malformed_xhtml, "; ".join(malformed_xhtml[:3]))
        check(
            "Callout titles do not contain later headings, tables, or callout bodies",
            not overnested_callout_titles,
            ", ".join(overnested_callout_titles[:5]),
        )

        epigraph_count = sum(
            1
            for chapter_root in parsed_chapters.values()
            for div in chapter_root.findall(f".//{{{XHTML}}}div")
            if "chapter-epigraph" in div.get("class", "").split()
        )
        check("Every main chapter packages one epigraph", epigraph_count == 41, str(epigraph_count))

        appendix_a = next(
            (
                (path, root)
                for path, root in parsed_chapters.items()
                if "Rational Choice and Decision Analysis" in normalized_text(root)
            ),
            None,
        )
        check("Appendix A is present for mathematics QA", appendix_a is not None)
        if appendix_a is not None:
            appendix_a_path, appendix_a_root = appendix_a
            inline_math = [
                element
                for element in appendix_a_root.findall(f".//{{{MATHML}}}math")
                if element.get("display") == "inline"
            ]
            empty_inline_math = [element for element in inline_math if not normalized_text(element)]
            appendix_a_text = normalized_text(appendix_a_root)
            check(
                "Appendix A packages its inline formulas as MathML",
                len(inline_math) >= 100,
                f"{appendix_a_path}: found {len(inline_math)} inline MathML elements",
            )
            check(
                "Every Appendix A inline MathML formula contains content",
                not empty_inline_math,
                f"{appendix_a_path}: found {len(empty_inline_math)} empty inline formulas",
            )
            check(
                "Appendix A contains no empty-parenthesis math loss",
                not re.search(r"\b(?:Let|where|Suppose|when|If)\s+\(\)", appendix_a_text),
                appendix_a_path,
            )

        broken_content_links: list[str] = []
        empty_image_alts: list[str] = []
        id_cache: dict[str, set[str]] = {
            path: {element.get("id", "") for element in root.iter() if element.get("id")}
            for path, root in parsed_chapters.items()
        }
        for chapter_path, chapter_root in parsed_chapters.items():
            for image in chapter_root.findall(f".//{{{XHTML}}}img"):
                if not image.get("alt", "").strip():
                    empty_image_alts.append(f"{chapter_path}: {image.get('src', '')}")
            for anchor in chapter_root.findall(f".//{{{XHTML}}}a"):
                href = anchor.get("href", "").strip()
                if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                    continue
                parsed_href = urlsplit(href)
                raw_path = unquote(parsed_href.path)
                fragment = unquote(parsed_href.fragment)
                target_path = (
                    chapter_path
                    if not raw_path
                    else posixpath.normpath(posixpath.join(posixpath.dirname(chapter_path), raw_path))
                )
                if target_path not in names:
                    broken_content_links.append(f"{chapter_path}: {href} -> missing {target_path}")
                    continue
                if fragment:
                    if target_path not in id_cache and target_path.endswith((".xhtml", ".html")):
                        try:
                            target_root = ET.fromstring(archive.read(target_path))
                            id_cache[target_path] = {
                                element.get("id", "") for element in target_root.iter() if element.get("id")
                            }
                        except ET.ParseError:
                            id_cache[target_path] = set()
                    if target_path in id_cache and fragment not in id_cache[target_path]:
                        broken_content_links.append(f"{chapter_path}: {href} -> missing fragment #{fragment}")
        check(
            "Every internal content link and fragment resolves",
            not broken_content_links,
            "; ".join(broken_content_links[:5]),
        )
        check(
            "Every packaged content image has nonempty alternative text",
            not empty_image_alts,
            "; ".join(empty_image_alts[:5]),
        )

        chapter_four_item = next(
            (
                item
                for item in all_items
                if (anchor := item.find(f"{{{XHTML}}}a")) is not None
                and re.match(r"^4\s+", normalized_text(anchor))
            ),
            None,
        )
        chapter_four_anchor = chapter_four_item.find(f"{{{XHTML}}}a") if chapter_four_item is not None else None
        chapter_four_href = chapter_four_anchor.get("href", "").split("#", 1)[0] if chapter_four_anchor is not None else ""
        chapter_four_path = (
            posixpath.normpath(posixpath.join(posixpath.dirname(nav_path), chapter_four_href))
            if chapter_four_href
            else ""
        )
        chapter_four_root = parsed_chapters.get(chapter_four_path)
        prediction_meanings = (
            chapter_four_root.find(f".//*[@id='tbl-two-meanings-prediction']")
            if chapter_four_root is not None
            else None
        )
        meanings_table = prediction_meanings.find(f".//{{{XHTML}}}table") if prediction_meanings is not None else None
        first_row = meanings_table.find(f".//{{{XHTML}}}tr") if meanings_table is not None else None
        first_row_cells = (
            [child for child in list(first_row) if child.tag in {f"{{{XHTML}}}th", f"{{{XHTML}}}td"}]
            if first_row is not None
            else []
        )
        chapter_four_text = normalized_text(chapter_four_root) if chapter_four_root is not None else ""
        check(
            "Chapter 4 prediction distinction uses an EPUB-safe two-column table",
            len(first_row_cells) == 2,
            f"{chapter_four_path}: {len(first_row_cells)} columns",
        )
        check("Chapter 4 contains no stale manual Table 6.1 caption", "Table 6.1" not in chapter_four_text)

        searchable = "\n".join(
            archive.read(name).decode("utf-8", "ignore")
            for name in sorted(names)
            if name.endswith((".xhtml", ".svg", ".opf"))
        )
        for phrase in REQUIRED_CONTENT:
            check(f"Required content: {phrase}", phrase.lower() in searchable.lower())
        check(
            "Rendered EPUB contains no duplicated Figure Figure cross-reference labels",
            re.search(r">\s*Figures?\s+<a\b[^>]*>\s*Figure", searchable, flags=re.DOTALL | re.I) is None,
        )
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
