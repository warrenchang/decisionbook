"""Reproduce Chapter 27 additions from immutable lecture inputs.

Run with Python containing matplotlib. SVG is the canonical plot output.
The FOMC line preserves the lecture's source vector geometry: it is not
a reconstructed price dataset. Election figures use recorded observations.
"""
from pathlib import Path
import csv
import json
import datetime as dt
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.ticker import StrMethodFormatter

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / 'figures'
ETZ = ZoneInfo('America/New_York')
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'svg.fonttype': 'none', 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.labelcolor': '#183047',
                     'text.color': '#183047', 'axes.edgecolor': '#9aabb5'})
BLUE, TEAL = '#254f77', '#087e8b'

def save(fig, name):
    fig.savefig(OUT / (name + '.svg'), facecolor='white', bbox_inches='tight')
    descriptions = {
        'finance-fed-announcement': ('S&P 500 response to the September 2013 Fed announcement',
            'Published minute-scale price trace, preserving the lecture source geometry. '
            'The index rises sharply at 14:00 US Eastern; this trace does not measure millisecond adjustment.'),
        'finance-election-night': ('Prediction-market and futures prices during the 2024 election night',
            'Aligned panels show recorded minute closing trades for the Republican inauguration contract '
            'and hourly opening observations for E-mini S&P 500 futures. US Eastern time, November 5–6, 2024.')}
    from html import escape
    title, description = descriptions[name]
    path = OUT / (name + '.svg')
    svg = path.read_text()
    pos = svg.index('>', svg.index('<svg')) + 1
    svg = svg[:pos] + '<title>' + escape(title) + '</title><desc>' + escape(description) + '</desc>' + svg[pos:]
    path.write_text(svg)
    plt.close(fig)

# FOMC: preserve every source move/line pair; rescale geometry uniformly.
ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
root = ET.parse(HERE / 'slide11.xml').getroot()
paths = []
for sp in root.findall('.//p:sp', ns):
    if 'source vectors' not in sp.find('.//p:cNvPr', ns).get('name'):
        continue
    off = sp.find('.//a:xfrm/a:off', ns)
    ox, oy = int(off.get('x')), int(off.get('y'))
    points = [(ox + int(p.get('x')), -(oy + int(p.get('y'))))
              for p in sp.findall('.//a:pt', ns)]
    assert len(points) % 2 == 0
    paths.append(points)
flat = sum(paths, [])
x0, x1 = min(p[0] for p in flat), max(p[0] for p in flat)
y0, y1 = min(p[1] for p in flat), max(p[1] for p in flat)
norm = lambda p: ((p[0]-x0)/(x1-x0), (p[1]-y0)/(y1-y0))
fig, ax = plt.subplots(figsize=(7.2, 3.8))
for points, color in zip(paths, [BLUE, TEAL]):
    segments = [[norm(points[i]), norm(points[i+1])] for i in range(0,len(points),2)]
    ax.add_collection(LineCollection(segments, colors=color, linewidths=1.65))
marker = norm(paths[1][0])[0]
ax.axvline(marker, color='#777777', linestyle='--', linewidth=1.1)
ax.text(marker - .015, 1.12, 'Fed announcement', ha='right', fontsize=13)
ax.text(0, norm(paths[0][0])[1]+.07, '1,705.48', va='bottom')
ax.text(1, norm(paths[1][-1])[1]+.06, '1,725.52', ha='right', va='bottom')
ax.set_xticks([0, marker, 1], ['09:30', '14:00', '16:00'])
ax.set_xlabel('18 September 2013 · US Eastern time')
ax.set_yticks([])
ax.set_ylabel('S&P 500 index')
ax.set_xlim(-.025,1.025); ax.set_ylim(-.07,1.24)
ax.spines['left'].set_visible(False)
save(fig, 'finance-fed-announcement')

# The Kalshi timestamp is END of candle; Yahoo timestamp is START of bar.
start = dt.datetime(2024,11,5,18,tzinfo=ETZ)
end = dt.datetime(2024,11,6,6,tzinfo=ETZ)
def candles(name):
    obj = json.loads((HERE / 'data' / name).read_text())
    return [(dt.datetime.fromtimestamp(c['end_period_ts'],ETZ),100*float(c['price']['close']))
            for c in obj['candlesticks'] if c['price']['close'] is not None]
minute = candles('kalshi_minute.json')
context = candles('kalshi_context.json')
minute_night = [(t,v) for t,v in minute if start <= t <= end]
obj = json.loads((HERE/'data/es_hourly.json').read_text())['chart']['result'][0]
futures = [(dt.datetime.fromtimestamp(t,ETZ),float(v)) for t,v in
           zip(obj['timestamp'],obj['indicators']['quote'][0]['open'])
           if v is not None and start.timestamp() <= t <= end.timestamp()]
assert futures[0] == (start,5820.25)
assert futures[-1] == (end,5942.75)
observed = [(t,v) for t,v in minute if start <= t <= dt.datetime(2024,11,6,7,tzinfo=ETZ)]
last_below = max(t for t,v in observed if v < 95)
sustained = min(t for t,v in observed if t > last_below)
assert sustained == dt.datetime(2024,11,6,0,51,tzinfo=ETZ)
hour = lambda t: (t-start).total_seconds()/3600
fig, axes = plt.subplots(2,1,figsize=(7.2,6.7),sharex=True)
for ax in axes:
    ax.grid(axis='y', alpha=.2)
    ax.set_xlim(0,12)
axes[0].plot([hour(t) for t,v in minute_night], [v for t,v in minute_night],color=TEAL,lw=1.6)
axes[0].set_ylim(0,103); axes[0].set_yticks([0,25,50,75,100])
axes[0].set_ylabel('Contract price (cents)')
axes[0].set_title('A. Republican inauguration contract',loc='left',fontsize=14,pad=13)
axes[0].axvline(hour(sustained),ls=':',color='#777777',lw=1)
axes[0].annotate('At least 95¢ from 00:51',xy=(hour(sustained),95),
                xytext=(3.2,25),fontsize=12,arrowprops={'arrowstyle':'-','color':'#777777'})
axes[1].plot([hour(t) for t,v in futures],[v for t,v in futures],color=BLUE,marker='o',ms=4,lw=1.4)
axes[1].set_ylim(5800,5975);axes[1].set_yticks([5800,5850,5900,5950])
axes[1].yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
axes[1].set_ylabel('Index points')
axes[1].set_title('B. E-mini S&P 500 futures',loc='left',fontsize=14,pad=13)
axes[1].set_xticks([0,3,6,9,12],['18:00\n5 Nov','21:00','00:00\n6 Nov','03:00','06:00'])
axes[1].set_xlabel('2024 election night · US Eastern time (UTC−5)')
fig.subplots_adjust(hspace=.38)
save(fig,'finance-election-night')
with (HERE/'data/election-plotted.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['series','time_et','value','unit','field'])
    for label,rows,unit,field in [('kalshi',minute_night,'cents','close'),('ES=F',futures,'index points','open')]:
        for t,v in rows:w.writerow([label,t.isoformat(),v,unit,field])
(HERE/'numerical-checks.json').write_text(json.dumps({
    'kalshi_night_observations':len(minute_night),'futures_observations':len(futures),
    'sustained_95_cent_close_et':sustained.isoformat(),
    'futures_change_percent':100*(5942.75/5820.25-1),
    'fomc_vector_segments':len(flat)//2,
    'hypothetical_balanced_52_week_wealth':10000*(1.8*.4)**26,
    'hypothetical_expected_52_week_wealth':10000*1.1**52},indent=2))
