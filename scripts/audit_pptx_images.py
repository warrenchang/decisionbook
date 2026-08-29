#!/usr/bin/env python3
"""Create a reproducible occurrence-level inventory of visual assets in PPTX decks.

The audit is intentionally descriptive. It records every embedded/linked bitmap,
SVG, native chart, and native diagram occurrence without making copyright claims.
Editorial rights decisions live in the reviewed integration ledger.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import mimetypes
import posixpath
import re
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any
import xml.etree.ElementTree as ET

try:
    from PIL import Image
except ImportError:  # pragma: no cover - dimensions are optional
    Image = None


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
R_EMBED = f"{{{NS['r']}}}embed"
R_LINK = f"{{{NS['r']}}}link"


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def numeric_key(path: str) -> tuple[int, str]:
    match = re.search(r"(\d+)(?=\.[^.]+$)", path)
    return (int(match.group(1)) if match else 10**9, path)


def relationships(zf: zipfile.ZipFile, owner: str) -> dict[str, dict[str, str]]:
    owner_path = PurePosixPath(owner)
    rel_path = str(owner_path.parent / "_rels" / f"{owner_path.name}.rels")
    if rel_path not in zf.namelist():
        return {}
    root = ET.fromstring(zf.read(rel_path))
    result: dict[str, dict[str, str]] = {}
    for rel in root.findall("rel:Relationship", NS):
        rel_id = rel.get("Id")
        if rel_id:
            result[rel_id] = {
                "target": rel.get("Target", ""),
                "type": rel.get("Type", ""),
                "mode": rel.get("TargetMode", ""),
            }
    return result


def resolve_target(owner: str, target: str) -> str:
    # OOXML relationships may be package-relative (../media/image1.png) or
    # package-absolute (/ppt/slides/slide1.xml). Zip member names never begin
    # with a slash, so normalize both forms to the package member path.
    if target.startswith("/"):
        return posixpath.normpath(target).lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(owner), target)).lstrip("/")


def slide_order(zf: zipfile.ZipFile) -> list[tuple[str, bool]]:
    presentation = "ppt/presentation.xml"
    if presentation not in zf.namelist():
        slides = sorted(
            (name for name in zf.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=numeric_key,
        )
        return [(slide, False) for slide in slides]
    root = ET.fromstring(zf.read(presentation))
    rels = relationships(zf, presentation)
    ordered: list[tuple[str, bool]] = []
    for slide_id in root.findall(".//p:sldIdLst/p:sldId", NS):
        rel_id = slide_id.get(f"{{{NS['r']}}}id", "")
        rel = rels.get(rel_id)
        if not rel:
            continue
        path = resolve_target(presentation, rel["target"])
        hidden = slide_id.get("show") == "0"
        ordered.append((path, hidden))
    return ordered


def image_metadata(data: bytes, media_path: str) -> dict[str, Any]:
    width = height = None
    image_format = None
    if Image is not None:
        try:
            with Image.open(io.BytesIO(data)) as image:
                width, height = image.size
                image_format = image.format
        except Exception:
            pass
    mime, _ = mimetypes.guess_type(media_path)
    return {
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "width_px": width,
        "height_px": height,
        "image_format": image_format or Path(media_path).suffix.lstrip(".").upper(),
        "mime_type": mime or "",
    }


def nearest_object(element: ET.Element, parents: dict[ET.Element, ET.Element]) -> ET.Element | None:
    current: ET.Element | None = element
    while current is not None:
        if local_name(current.tag) in {"pic", "sp", "graphicFrame", "bg", "grpSp"}:
            return current
        current = parents.get(current)
    return None


def object_properties(obj: ET.Element | None) -> dict[str, Any]:
    if obj is None:
        return {"object_id": "", "object_name": "", "alt_title": "", "alt_description": "", "decorative": False}
    c_nv_pr = next((node for node in obj.iter() if local_name(node.tag) == "cNvPr"), None)
    decorative = any(
        local_name(node.tag) == "decorative" and node.get("val", "1") not in {"0", "false", "False"}
        for node in obj.iter()
    )
    return {
        "object_id": c_nv_pr.get("id", "") if c_nv_pr is not None else "",
        "object_name": c_nv_pr.get("name", "") if c_nv_pr is not None else "",
        "alt_title": c_nv_pr.get("title", "") if c_nv_pr is not None else "",
        "alt_description": c_nv_pr.get("descr", "") if c_nv_pr is not None else "",
        "decorative": decorative,
    }


def crop_value(blip: ET.Element, parents: dict[ET.Element, ET.Element]) -> str:
    obj = nearest_object(blip, parents)
    if obj is None:
        return ""
    src = next((node for node in obj.iter() if local_name(node.tag) == "srcRect"), None)
    if src is None:
        return ""
    values = [f"{key}={src.get(key)}" for key in ("l", "t", "r", "b") if src.get(key) is not None]
    return ";".join(values)


def graphic_kind(uri: str) -> str | None:
    uri = uri.casefold()
    if "chart" in uri:
        return "native-chart"
    if "diagram" in uri:
        return "native-diagram"
    return None


def audit_deck(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    metadata_cache: dict[str, dict[str, Any]] = {}
    with zipfile.ZipFile(path) as zf:
        members = set(zf.namelist())
        for slide_number, (slide_path, hidden_from_list) in enumerate(slide_order(zf), start=1):
            root = ET.fromstring(zf.read(slide_path))
            hidden = hidden_from_list or root.get("show") == "0"
            rels = relationships(zf, slide_path)
            parents = {child: parent for parent in root.iter() for child in parent}
            ordinal = 0
            for blip in root.findall(".//a:blip", NS):
                ordinal += 1
                rel_id = blip.get(R_EMBED) or blip.get(R_LINK) or ""
                rel = rels.get(rel_id, {})
                target = rel.get("target", "")
                external = rel.get("mode", "").casefold() == "external" or bool(blip.get(R_LINK))
                media_path = target if external else resolve_target(slide_path, target) if target else ""
                obj = nearest_object(blip, parents)
                props = object_properties(obj)
                meta: dict[str, Any] = {
                    "sha256": "",
                    "bytes": None,
                    "width_px": None,
                    "height_px": None,
                    "image_format": Path(media_path).suffix.lstrip(".").upper(),
                    "mime_type": "",
                }
                if media_path and not external and media_path in members:
                    if media_path not in metadata_cache:
                        metadata_cache[media_path] = image_metadata(zf.read(media_path), media_path)
                    meta = metadata_cache[media_path]
                rows.append(
                    {
                        "deck": path.name,
                        "deck_path": str(path),
                        "slide_number": slide_number,
                        "hidden_slide": hidden,
                        "occurrence_ordinal": ordinal,
                        "asset_kind": "linked-image" if external else "embedded-image",
                        "relationship_id": rel_id,
                        "relationship_type": rel.get("type", ""),
                        "media_path": media_path,
                        "external": external,
                        "crop": crop_value(blip, parents),
                        **props,
                        **meta,
                    }
                )
            for frame in root.findall(".//p:graphicFrame", NS):
                graphic_data = frame.find(".//a:graphic/a:graphicData", NS)
                kind = graphic_kind(graphic_data.get("uri", "")) if graphic_data is not None else None
                if not kind:
                    continue
                ordinal += 1
                props = object_properties(frame)
                rows.append(
                    {
                        "deck": path.name,
                        "deck_path": str(path),
                        "slide_number": slide_number,
                        "hidden_slide": hidden,
                        "occurrence_ordinal": ordinal,
                        "asset_kind": kind,
                        "relationship_id": "",
                        "relationship_type": "",
                        "media_path": "",
                        "external": False,
                        "crop": "",
                        **props,
                        "sha256": "",
                        "bytes": None,
                        "width_px": None,
                        "height_px": None,
                        "image_format": "",
                        "mime_type": "",
                    }
                )
    return rows


def write_outputs(rows: list[dict[str, Any]], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    hashes = Counter(row["sha256"] for row in rows if row["sha256"])
    for row in rows:
        row["duplicate_group"] = f"sha256:{row['sha256'][:16]}" if row["sha256"] else ""
        row["duplicate_occurrences"] = hashes.get(row["sha256"], 0) if row["sha256"] else 0
        row["occurrence_id"] = f"{Path(row['deck']).stem}:s{row['slide_number']}:o{row['occurrence_ordinal']}"

    fields = [
        "occurrence_id", "deck", "deck_path", "slide_number", "hidden_slide", "occurrence_ordinal",
        "asset_kind", "object_id", "object_name", "alt_title", "alt_description", "decorative",
        "relationship_id", "relationship_type", "media_path", "external", "crop", "image_format",
        "mime_type", "width_px", "height_px", "bytes", "sha256", "duplicate_group", "duplicate_occurrences",
    ]
    with (out_dir / "slide-image-occurrences.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)
    (out_dir / "slide-image-occurrences.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    by_deck = Counter(row["deck"] for row in rows)
    hidden = Counter(row["deck"] for row in rows if row["hidden_slide"])
    unique_hashes = {row["sha256"] for row in rows if row["sha256"]}
    duplicated_hashes = {value for value, count in hashes.items() if count > 1}
    lines = [
        "# Raw slide-image occurrence inventory",
        "",
        "This machine-generated inventory records embedded or linked images and native chart/diagram objects in the editable 2026 lecture decks. It does not make rights judgments; see the reviewed image-integration ledger for editorial treatment.",
        "",
        f"- Occurrences: **{len(rows)}**",
        f"- Unique embedded-image hashes: **{len(unique_hashes)}**",
        f"- Hash groups reused more than once: **{len(duplicated_hashes)}**",
        f"- Occurrences on hidden slides: **{sum(hidden.values())}**",
        "",
        "| Deck | Occurrences | On hidden slides |",
        "| --- | ---: | ---: |",
    ]
    for deck in sorted(by_deck):
        lines.append(f"| {deck} | {by_deck[deck]} | {hidden[deck]} |")
    lines.extend(
        [
            "",
            "The occurrence-level CSV includes slide number, hidden status, object ID/name, alternative text, crop, relationship target, media dimensions, SHA-256 hash, and duplicate group.",
            "",
        ]
    )
    (out_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Directory containing PPTX files, or one PPTX file.")
    parser.add_argument("--out-dir", type=Path, default=Path("audits/slide-images-raw"))
    args = parser.parse_args()
    decks = [args.source] if args.source.is_file() else sorted(args.source.glob("*.pptx"))
    if not decks:
        raise SystemExit(f"No PPTX files found at {args.source}")
    rows: list[dict[str, Any]] = []
    for deck in decks:
        rows.extend(audit_deck(deck.resolve()))
    write_outputs(rows, args.out_dir.resolve())
    print(f"Inventoried {len(rows)} visual occurrences across {len(decks)} deck(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
