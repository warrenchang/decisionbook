#!/usr/bin/env python3
"""Redraw the *graphical evidence*, not an unavailable numerical dataset.

The input is the immutable lecture reproduction of Rendleman et al. (1982).
Dark runs in successive source-image columns provide approximate curve
centerlines. Connected runs are linked, retaining the visible intersections.
All paths share one color: no decile identity is inferred at merged crossings.
The ten right-end labels retain the identities explicitly printed in the source.
Source axes, ticks, lettering and announcement marker are replaced, not copied.
"""
from pathlib import Path
import csv
import hashlib
import json
from html import escape
import numpy as np
from PIL import Image
from scipy.ndimage import label
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'figures/finance-earnings-drift-evidence.png'
OUT = ROOT / 'figures/finance-earnings-drift-redraw.svg'
SOURCE_SHA = '1a3ac4a128b076e2ccb2ba452165aab135b3489ffe801b8a7600a5db126bb4a4'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA
im = np.array(Image.open(SOURCE).convert('L'))
# Bounds exclude the old axes, lettering, and endpoint labels, not any curve.
mask = np.zeros_like(im, dtype=bool)
mask[130:1090, 120:1114] = im[130:1090, 120:1114] < 128
# The scanned dashed announcement line occupies this narrow strip.
# Its removal also obscures <1.4 days of the steep response. Rejoin below.
mask[:, 297:308] = False
# Remove isolated ink/dust. Largest gaps are retained as gaps, not smoothed.
components, n = label(mask, structure=np.ones((3, 3), dtype=int))
counts = np.bincount(components.ravel())
mask &= counts[components] >= 5

def runs(x):
    ys = np.flatnonzero(mask[:, x])
    return [r for r in np.split(ys, np.flatnonzero(np.diff(ys) > 1)+1) if len(r)]

segments = []
for x in range(120, 1113):
    if 296 <= x <= 307:
        continue
    a, b = runs(x), runs(x+1)
    for ra in a:
        for rb in b:
            # Adjacent strokes meet where their dark-pixel intervals touch.
            if ra[0] <= rb[-1]+1 and rb[0] <= ra[-1]+1:
                segments.append(((x, float(np.mean(ra))), (x+1, float(np.mean(rb)))))
# Both extremes have merged pairs at the left of the removed marker. Preserve
# that visible merging; do not claim to distinguish portfolio identities there.
left, right = runs(296), runs(308)
assert len(left) == 8 and len(right) == 10
bridge_left_indices = [0, 0, 1, 2, 3, 4, 5, 6, 7, 7]
bridges = []
for i, j in enumerate(bridge_left_indices):
    seg = ((296, float(np.mean(left[j]))), (308, float(np.mean(right[i]))))
    bridges.append(seg)
    segments.append(seg)

# Piecewise calibration accommodates the small distortion in the source scan.
# Source tick centers: day -20 = 120px, day 0 = 303px, day 90 = 1113px;
# return +10% = 28px, 0% = 584px, -10% = 1144px.
def x_data(x):
    return (x-303)/((303-120)/20 if x <= 303 else (1113-303)/90)
def y_data(y):
    return (584-y)/((584-28)/10 if y <= 584 else (1144-584)/10)
def data(p):
    return x_data(p[0]), y_data(p[1])
plotted = [[data(a), data(b)] for a,b in segments]
with (HERE/'digitized-geometry.csv').open('w') as f:
    w = csv.writer(f)
    w.writerow(['segment', 'day_start_approx', 'return_start_percent_approx',
                'day_end_approx', 'return_end_percent_approx', 'marker_bridge'])
    for i, (a, b) in enumerate(plotted):
        w.writerow([i, *[round(v, 6) for v in (*a, *b)], i >= len(segments)-10])

# Plain, source-faithful plotting with the book's typography and palette.
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
    'svg.fonttype': 'none', 'svg.hashsalt': 'finance-earnings-drift-redraw',
    'text.color': '#183047', 'axes.labelcolor': '#183047',
    'xtick.color': '#536879', 'ytick.color': '#536879',
    'axes.edgecolor': '#9aabb5'})
fig, ax = plt.subplots(figsize=(8.4, 6.0))
fig.subplots_adjust(left=.09, right=.94, top=.86, bottom=.14)
ax.set_xlim(-22, 102); ax.set_ylim(-10, 10)
ax.set_xticks([-20, 0, 20, 40, 60, 80, 90])
ax.set_yticks([-10, -5, 0, 5, 10])
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:+.0f}' if y else '0'))
ax.set_xlabel('Days from earnings announcement', labelpad=13)
ax.set_title('Cumulative average excess return (%)', loc='left', fontsize=15, pad=31)
ax.spines[['top', 'right']].set_visible(False)
ax.spines['left'].set_bounds(-10, 10)
ax.spines['bottom'].set_bounds(-20, 90)
ax.tick_params(length=4, width=.8, pad=6)
for y in [-10, -5, 0, 5, 10]:
    ax.hlines(y, -20, 90, colors='#dce3e8' if y else '#b7c5ce', lw=.7, zorder=0)
ax.vlines(0, -10, 10, colors='#9aabb5', lw=1.1, linestyles=(0, (4, 4)), zorder=0)
ax.text(0, 10.7, 'Announcement', fontsize=12, ha='center', va='bottom', color='#536879')
ax.text(96, 10.7, 'Decile', fontsize=12, ha='center', va='bottom', color='#536879')
ax.add_collection(LineCollection(plotted, colors='#254f77', linewidths=1.4,
                                 capstyle='round', joinstyle='round', zorder=3))
# The last column in which all ten source paths have visible ink.
ends = runs(1110)
assert len(ends) == 10
for rank, r in enumerate(ends):
    ax.text(94, y_data(float(np.mean(r))), str(10-rank), color='#087e8b',
            fontsize=13, ha='left', va='center', fontweight='normal')
fig.savefig(OUT, facecolor='white', metadata={'Date': None})
plt.close(fig)
svg = OUT.read_text()
pos = svg.index('>', svg.index('<svg')) + 1
svg = svg[:pos] + '\n<title id="title">Earnings surprises and subsequent return drift</title>\n<desc id="desc">' + escape(
    'Approximate tracing of ten historical earnings-surprise groups from Rendleman, Jones and Latane (1982). '
    'Cumulative average excess returns separate before and around announcement day zero, and continue '
    'diverging over the following 90 days. Decile 10 has the most favorable earnings surprises; decile 1 '
    'the least favorable. The crossing paths and irregularities of the source are retained. '
    'These traced graphical coordinates are not the original return observations.') + '</desc>\n' + svg[pos:]
svg = svg.replace('<svg ', '<svg role="img" aria-labelledby="title desc" ', 1)
OUT.write_text(svg)

# Quantify source fidelity away from the explicitly reconstructed marker strip.
# Distance is in pixels of the supplied scan, not a sampling error estimate.
from scipy.ndimage import distance_transform_edt
from PIL import ImageDraw
trace_im = Image.new('1', (im.shape[1], im.shape[0]))
draw = ImageDraw.Draw(trace_im)
for a,b in segments[:-10]:
    draw.line([a,b], fill=1, width=1)
trace = np.array(trace_im)
dist = distance_transform_edt(~trace)
valid_source = mask.copy(); valid_source[:, 295:310] = False
pixel_distances = dist[valid_source]
(HERE/'extraction-checks.json').write_text(json.dumps({
    'status': 'Approximate graphical digitization; not original portfolio observations',
    'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': SOURCE_SHA,
    'source_size_px': [int(im.shape[1]), int(im.shape[0])],
    'source_study': 'Rendleman, Jones and Latane (1982), JFE 10(3), 269-287',
    'source_doi': '10.1016/0304-405X(82)90003-4',
    'method': 'Column-run centers joined across touching ink; no fitted smoothing; a narrow announcement-marker strip is linearly reconstructed',
    'identity_boundary': 'Geometric segments have no inferred decile identity at intersections; all are drawn in one color. Right-end labels are read from the source.',
    'marker_strip_x_px': [297, 307],
    'bridge_endpoints_x_px': [296, 308],
    'bridged_time_width_days_approx': x_data(308)-x_data(296),
    'black_threshold': 128, 'minimum_component_pixels': 5,
    'curve_segments': len(segments), 'linear_bridges': len(bridges),
    'day_90_returns_top_to_bottom_approx': [round(y_data(float(np.mean(r))), 2) for r in ends],
    'source_ink_to_trace_distance_px_excluding_marker': {
        'median': float(np.median(pixel_distances)),
        'p95': float(np.percentile(pixel_distances,95)),
        'p99': float(np.percentile(pixel_distances,99)),
        'max': float(np.max(pixel_distances))},
    'versions': {'numpy': np.__version__, 'matplotlib': matplotlib.__version__}
}, indent=2)+'\n')
print(f'Built {OUT.name}: {len(segments)} digitized segments, including 10 marker bridges.')
