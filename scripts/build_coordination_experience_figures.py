#!/usr/bin/env python3
"""Build two small reading aids from a published protocol and declared payoffs.

No participant-level values, pain curves, or fitted behavioral models are made.
Render PNG companions from these final SVGs with render_svg_png_fallbacks.cjs.
Source and interpretation boundaries: audits/visual-readability-20260925/
    coordination-experience-sources.md.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INK, BLUE, TEAL = '#183047', '#254f77', '#087e8b'
MUTED, GRID = '#536879', '#dce3e8'


class SVG:
    def __init__(self, height, title, description):
        self.items = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" '
            f'viewBox="0 0 760 {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title>',
            f'<desc id="desc">{escape(description)}</desc>',
            '<style>text{font-family:Arial,Helvetica,sans-serif}</style>',
            f'<rect width="760" height="{height}" fill="white"/>',
        ]

    def text(self, x, y, label, size=30, color=INK, anchor='middle', bold=False, extra=''):
        self.items.append(
            f'<text x="{x:g}" y="{y:g}" font-size="{size}" fill="{color}" '
            f'text-anchor="{anchor}" font-weight="{700 if bold else 400}" {extra}>'
            f'{escape(label)}</text>'
        )

    def line(self, x1, y1, x2, y2, color=GRID, width=2, dash=''):
        self.items.append(
            f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
            + (f'stroke-dasharray="{dash}"' if dash else '') + '/>'
        )

    def rect(self, x, y, width, height, fill):
        self.items.append(f'<rect x="{x:g}" y="{y:g}" width="{width:g}" '
                          f'height="{height:g}" fill="{fill}"/>')

    def save(self, stem):
        target = ROOT / 'figures' / f'{stem}.svg'
        target.write_text('\n'.join(self.items + ['</svg>']) + '\n')
        print(target.relative_to(ROOT))


def cold_water():
    f = SVG(575, 'Cold-water trials: the same first minute, a different ending',
            'Protocol timelines, not pain measurements. The short trial lasts 60 seconds '
            'at 14 degrees Celsius. The long trial has the same first 60 seconds, then '
            '30 additional seconds as water warms toward 15 degrees Celsius. '
            'Twenty-two of the 32 analyzed participants chose to repeat the long trial.')
    x0, x60, x90 = 70, 490, 700
    for x in (x0, x60, x90):
        f.line(x, 67, x, 377, GRID, 1.5, '5 7')
    f.text(x0, 43, 'Short trial', anchor='start', bold=True)
    f.rect(x0, 70, x60-x0, 80, BLUE)
    f.text((x0+x60)/2, 120, '14°C', color='white', bold=True)
    f.text(x60+24, 120, 'Stop', anchor='start', color=MUTED)

    f.text(x0, 231, 'Long trial', anchor='start', bold=True)
    f.rect(x0, 258, x60-x0, 80, BLUE)
    f.rect(x60, 258, x90-x60, 80, '#c7e7e7')
    f.text((x0+x60)/2, 308, '14°C', color='white', bold=True)
    f.text((x60+x90)/2, 289, 'Warms to', size=28)
    f.text((x60+x90)/2, 322, '15°C', bold=True)

    f.line(x0, 377, x90, 377, MUTED, 2)
    for x, label in ((x0, '0'), (x60, '60'), (x90, '90')):
        f.line(x, 377, x, 386, MUTED, 2)
        f.text(x, 418, label, size=28, color=MUTED)
    f.text(385, 461, 'Time in water (seconds)')
    f.text(380, 531, '22 of 32 chose the longer trial', bold=True, color=TEAL)
    f.save('cold-water-better-ending')


def stag_hunt():
    # The chapter's illustrative table is in utility payoff units:
    # Stag: 15 with a Stag partner, 2 with a Hare partner. Hare: 10 always.
    threshold = (10-2)/(15-2)
    assert abs(threshold - 8/13) < 1e-12
    assert 2 + 13*0.5 == 8.5
    assert abs(2+13*threshold-10) < 1e-12
    f = SVG(675, 'When confidence makes Stag the better response',
            'Expected payoffs from the illustrative stag-hunt matrix. The horizontal '
            'axis is the believed probability that the other player chooses Stag. '
            'Stag increases linearly from 2 to 15; Hare remains at 10. The curves '
            'cross at 8/13, about 61.5 percent. These are calculated utility payoffs, '
            'not measured behavior.')
    x0, x1, y0, top, ymax = 140, 690, 520, 70, 16
    x = lambda p: x0 + (x1-x0)*p
    y = lambda value: y0 - (y0-top)*value/ymax
    for value in (0, 5, 10, 15):
        f.line(x0, y(value), x1, y(value), GRID, 1.5)
        f.text(x0-21, y(value)+10, str(value), size=28, color=MUTED, anchor='end')
    f.line(x0, top, x0, y0, MUTED, 2)
    f.line(x0, y0, x1, y0, MUTED, 2)
    for p, label in ((0, '0%'), (.5, '50%'), (1, '100%')):
        f.line(x(p), y0, x(p), y0+8, MUTED, 2)
        f.text(x(p), y0+42, label, size=28, color=MUTED)

    f.line(x(threshold), y(10), x(threshold), y0, MUTED, 2, '6 7')
    f.line(x(0), y(10), x(1), y(10), BLUE, 5, '12 9')
    f.line(x(0), y(2), x(1), y(15), TEAL, 5)
    f.items.append(f'<circle cx="{x(threshold):g}" cy="{y(10):g}" r="7" '
                   f'fill="white" stroke="{INK}" stroke-width="3"/>')
    f.text(x(.86), y(15)-15, 'Stag', color=TEAL, bold=True)
    f.text(x(.95), y(10)-18, 'Hare', color=BLUE, anchor='end', bold=True)
    f.text(x(threshold), y0-22, '61.5%', size=28, color=MUTED,
           extra='style="paint-order:stroke;stroke:white;stroke-width:9px;stroke-linejoin:round"')
    f.text(42, 295, 'Expected payoff', size=30,
           extra='transform="rotate(-90 42 295)"')
    f.text(415, 604, 'Believed chance the other', size=30)
    f.text(415, 641, 'player chooses Stag', size=30)
    f.save('stag-hunt-belief-payoffs')


if __name__ == '__main__':
    cold_water()
    stag_hunt()
