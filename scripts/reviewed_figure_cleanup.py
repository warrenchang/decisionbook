"""Apply exact, reviewed figure edits to still-active SVG generator output.

The manifest records the generator input, transparent text/layout deltas, the
reviewed viewBox, and both hashes. It includes earlier reviewed font/wrapping
repairs where a generator predated them. It never deletes by a keyword rule or
loads a canonical SVG as a substitute for executing its generator. Input drift
fails explicitly, so rerunning an edited generator cannot silently discard the
review. Reapplying cleanup to the reviewed output is an exact no-op.
"""
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import xml.etree.ElementTree as ET


@lru_cache(maxsize=1)
def _manifest():
    return json.loads(Path(__file__).with_suffix('.json').read_text(encoding='utf-8'))['figures']


def clean_svg(filename: str, svg: str) -> str:
    """Return reviewed output, or fail on drift in a covered generator.

    Unlisted outputs are unaffected; the generator owns their normal review.
    """
    name = Path(filename).name
    entry = _manifest().get(name)
    if entry is None:
        return svg
    fingerprint = sha256(svg.encode('utf-8')).hexdigest()
    if fingerprint == entry['output_sha256']:
        return svg
    if fingerprint != entry['input_sha256']:
        raise ValueError(
            f'{name}: generator output differs from its reviewed cleanup input. '
            'Review the changed source and update reviewed_figure_cleanup.json '
            'before replacing the canonical figure.'
        )
    for patch in reversed(entry['patches']):
        start, end = patch['start'], patch['end']
        if svg[start:end] != patch['before']:
            raise ValueError(f'{name}: reviewed patch does not match its source.')
        svg = svg[:start] + patch['after'] + svg[end:]
    if sha256(svg.encode('utf-8')).hexdigest() != entry['output_sha256']:
        raise ValueError(f'{name}: reviewed cleanup output failed its fingerprint.')
    if ET.fromstring(svg).attrib.get('viewBox') != entry['reviewed_viewBox']:
        raise ValueError(f'{name}: reviewed figure has an unexpected viewBox.')
    return svg
