#!/usr/bin/env python3
"""Render labeled contact sheets for visual inspection of canonical chapter figures."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from sync_references import canonical_chapters


ROOT = Path(__file__).resolve().parents[1]
FIGURE = re.compile(r"!\[[^\]]*\]\((\.\./figures/[^)]+)\)\{[^}\n]*\}")


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/System/Library/Fonts/Supplemental/Helvetica.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def figure_paths() -> list[Path]:
    paths: list[Path] = []
    seen: set[Path] = set()
    for chapter in canonical_chapters():
        text = chapter.read_text(encoding="utf-8")
        for target in FIGURE.findall(text):
            source = (chapter.parent / target).resolve()
            png = source.with_suffix(".png")
            if png not in seen:
                seen.add(png)
                paths.append(png)
    missing = [path for path in paths if not path.exists()]
    if missing:
        joined = ", ".join(path.name for path in missing)
        raise SystemExit(f"Missing PNG companion(s): {joined}")
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, default=Path("/private/tmp/dpn-figure-contact"))
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--rows", type=int, default=4)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    paths = figure_paths()
    cell_w, cell_h = 480, 335
    margin, title_h = 28, 60
    per_sheet = args.columns * args.rows
    sheets = math.ceil(len(paths) / per_sheet)
    label_font = font(18, bold=True)
    title_font = font(25, bold=True)

    for page in range(sheets):
        width = margin * 2 + args.columns * cell_w
        height = margin * 2 + title_h + args.rows * cell_h
        canvas = Image.new("RGB", (width, height), "#f4f7f9")
        draw = ImageDraw.Draw(canvas)
        draw.text((margin, margin), f"Canonical chapter figures — sheet {page + 1} of {sheets}", fill="#183047", font=title_font)
        subset = paths[page * per_sheet : (page + 1) * per_sheet]
        for index, path in enumerate(subset):
            row, col = divmod(index, args.columns)
            x = margin + col * cell_w
            y = margin + title_h + row * cell_h
            draw.rounded_rectangle((x + 7, y + 7, x + cell_w - 7, y + cell_h - 7), radius=15, fill="white", outline="#b9c8d4", width=2)
            image = Image.open(path).convert("RGB")
            image.thumbnail((cell_w - 34, cell_h - 70), Image.Resampling.LANCZOS)
            px = x + (cell_w - image.width) // 2
            py = y + 20 + (cell_h - 70 - image.height) // 2
            canvas.paste(image, (px, py))
            label = path.stem
            bbox = draw.textbbox((0, 0), label, font=label_font)
            tx = x + (cell_w - (bbox[2] - bbox[0])) // 2
            draw.text((tx, y + cell_h - 38), label, fill="#183047", font=label_font)
        output = args.outdir / f"figures-{page + 1:02d}.png"
        canvas.save(output, quality=92)
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
