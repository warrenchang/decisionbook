#!/usr/bin/env python3
"""Derive a two-tone teaching image by an explicit global luminance threshold.

The source is never modified. No features are redrawn, masked, or repositioned.
Requires Pillow. A threshold must be supplied so the processing choice is explicit.
"""

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path,
                        default=root / "figures/recognition-grayscale-reveal.png")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--threshold", type=int, required=True)
    args = parser.parse_args()
    if not 1 <= args.threshold <= 255:
        parser.error("--threshold must be between 1 and 255")
    if args.source.resolve() == args.output.resolve():
        parser.error("The output must not overwrite the source")

    source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    with Image.open(args.source) as source:
        luminance = source.convert("L")
        binary = luminance.point(
            [0 if value < args.threshold else 255 for value in range(256)]
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    binary.save(args.output, format="PNG", optimize=True)

    with Image.open(args.output) as saved:
        assert saved.mode == "L" and saved.size == luminance.size
        assert saved.tobytes() == binary.tobytes()
        assert set(saved.tobytes()) <= {0, 255}
    assert hashlib.sha256(args.source.read_bytes()).hexdigest() == source_hash
    print(json.dumps({
        "source": str(args.source),
        "source_sha256": source_hash,
        "output": str(args.output),
        "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "size": list(binary.size),
        "threshold": args.threshold,
        "rule": "Pillow L luminance < threshold -> 0 (black); otherwise 255 (white)",
        "black_fraction": binary.histogram()[0] / (binary.width * binary.height),
    }, indent=2))


if __name__ == "__main__":
    main()
