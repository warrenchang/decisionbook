#!/usr/bin/env python3
"""Build Chapter 27's empirical news plots in a common book style.

Inputs remain immutable. Fed paths retain source vector coordinates; Challenger
uses all published vector marker centers; September 11 uses an explicitly
approximate trace of the lecture's raster. No fitted or smoothed price series.
"""
from pathlib import Path
import csv,json,hashlib
from html import escape
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.ticker import FuncFormatter, StrMethodFormatter

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'audits/ch27-news-figures-20260921'
LECTURE=ROOT/'audits/ch27-finance-lecture-20260921'
OUT=ROOT/'figures'
NAVY,BLUE,TEAL,MUTED,RED='#183047','#254f77','#087e8b','#536879','#b65d62'
GRID,AXIS='#dce3e8','#9aabb5'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
    'svg.fonttype':'none','svg.hashsalt':'finance-news-book-style',
    'text.color':NAVY,'axes.labelcolor':NAVY,'xtick.color':MUTED,
    'ytick.color':MUTED,'axes.edgecolor':AXIS})

def axes(height=5.4,top=.80,bottom=.16):
    fig,ax=plt.subplots(figsize=(8.4,height))
    fig.subplots_adjust(left=.10,right=.965,top=top,bottom=bottom)
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(length=4,width=.8,pad=6)
    ax.set_axisbelow(True)
    return fig,ax

def save(fig,name,title,desc):
    path=OUT/(name+'.svg')
    fig.savefig(path,facecolor='white',metadata={'Date':None})
    plt.close(fig)
    svg=path.read_text();i=svg.index('>',svg.index('<svg'))+1
    svg=svg[:i]+'\n<title id="title">'+escape(title)+'</title><desc id="desc">'+escape(desc)+'</desc>\n'+svg[i:]
    svg=svg.replace('<svg ','<svg role="img" aria-labelledby="title desc" ',1)
    path.write_text(svg)

# 27.2: retain every vector segment of the source chart.
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
root=ET.parse(LECTURE/'slide11.xml').getroot();paths=[]
for sp in root.findall('.//p:sp',ns):
    if 'source vectors' not in sp.find('.//p:cNvPr',ns).get('name'):continue
    off=sp.find('.//a:xfrm/a:off',ns);ox,oy=int(off.get('x')),int(off.get('y'))
    paths.append([(ox+int(p.get('x')),-(oy+int(p.get('y')))) for p in sp.findall('.//a:pt',ns)])
flat=sum(paths,[])
x0,x1=min(p[0] for p in flat),max(p[0] for p in flat)
y0,y1=min(p[1] for p in flat),max(p[1] for p in flat)
norm=lambda p:((p[0]-x0)/(x1-x0),(p[1]-y0)/(y1-y0))
fig,ax=axes(4.8,.81,.19)
for pts,col in zip(paths,[BLUE,TEAL]):
    ax.add_collection(LineCollection([[norm(pts[i]),norm(pts[i+1])] for i in range(0,len(pts),2)],colors=col,linewidths=1.6,capstyle='round',joinstyle='round'))
marker=norm(paths[1][0])[0]
ax.axvline(marker,color=AXIS,lw=1.1,ls=(0,(4,4)))
ax.text(marker-.015,1.12,'Fed announcement',ha='right',fontsize=12,color=MUTED)
ax.text(0,norm(paths[0][0])[1]+.08,'1,705.48',va='bottom',fontsize=13)
ax.text(1,norm(paths[1][-1])[1]+.065,'1,725.52',ha='right',va='bottom',fontsize=13)
ax.set_xticks([0,marker,1],['09:30','14:00','16:00']);ax.set_yticks([])
ax.set_xlabel('18 September 2013 · US Eastern time',labelpad=13)
ax.set_title('S&P 500 index',loc='left',fontsize=15,pad=24)
ax.spines['left'].set_visible(False);ax.spines['bottom'].set_bounds(0,1)
ax.set_xlim(-.025,1.025);ax.set_ylim(-.07,1.24)
save(fig,'finance-fed-announcement','S&P 500 response to the September 2013 Fed announcement',
    'Original published vector geometry: the S&P 500 rises sharply at 14:00 US Eastern. Opening and closing values are 1,705.48 and 1,725.52. The chart does not measure millisecond response.')

# 27.3: isolate the existing price stroke, excluding grid, axes and annotations.
source=LECTURE/'image6.tiff'
assert hashlib.sha256(source.read_bytes()).hexdigest() == 'c3ce9ecc2a744b7c4a22657d20fc7267bb6cbd801476aa9a097efde635d38bf8'
im=np.array(Image.open(source).convert('L'))
mask=np.zeros_like(im,dtype=bool);mask[50:960,108:1709]=im[50:960,108:1709]<85
excluded=[(105,246,471,331),(239,117,283,226),(785,342,1144,430),(1028,241,1106,334)]
for x0,y0,x1,y1 in excluded:mask[y0:y1,x0:x1]=False

def runs(x):
    ys=np.flatnonzero(mask[:,x])
    return [r for r in np.split(ys,np.flatnonzero(np.diff(ys)>1)+1) if len(r)]
segments=[]
for x in range(109,1709):
    for r in runs(x):
        # Retain narrow vertical spikes; averaging them would conceal extremes.
        if len(r)>3:segments.append(((x,float(r[0])),(x,float(r[-1]))))
    if x==1708:continue
    for a in runs(x):
        for b in runs(x+1):
            if a[0]<=b[-1]+1 and b[0]<=a[-1]+1:
                segments.append(((x,float(np.mean(a))),(x+1,float(np.mean(b)))))
# Minute 0=08:43. Source chart tick centers: x94..1710, y17..1005.
data=lambda p:((p[0]-94)*32/(1710-94),1105-(p[1]-17)*45/(1005-17))
plotted=[[data(a),data(b)] for a,b in segments]
with (HERE/'september11-digitized-geometry.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['segment','minutes_after_0843_start_approx','index_start_approx','minutes_after_0843_end_approx','index_end_approx'])
    for i,(a,b) in enumerate(plotted):w.writerow([i,*a,*b])
fig,ax=axes(5.4,.77,.16)
ax.add_collection(LineCollection(plotted,colors=BLUE,linewidths=1.35,capstyle='round',joinstyle='round'))
ax.set_xlim(0,32);ax.set_ylim(1060,1105)
ax.set_yticks([1060,1070,1080,1090,1100]);ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
ax.grid(axis='y',color=GRID,lw=.7)
ax.set_xticks([2,7,12,17,22,27,32],['08:45','08:50','08:55','09:00','09:05','09:10','09:15'])
for t,label in [(3,'First impact\n08:46'),(20,'Second impact\n09:03')]:
    ax.axvline(t,color=AXIS,lw=1.1,ls=(0,(4,4)),zorder=0)
    ax.text(t,1.035,label,transform=ax.get_xaxis_transform(),ha='center',va='bottom',fontsize=12,color=MUTED,linespacing=1.25)
ax.set_title('S&P 500 futures price (index points)',loc='left',fontsize=15,pad=53)
ax.set_xlabel('11 September 2001 · US Eastern time',labelpad=13)
save(fig,'finance-september11-futures','S&P 500 futures as the September 11 attacks unfolded',
    'Approximate tracing of the lecture reproduction of Siegel (2008), Figure 13-1. Between 08:43 and 09:15, futures initially fall and recover, then drop steeply around the second impact at 09:03. The sharp fluctuations and partial rebound are retained. Event times are from the 9/11 Commission.')
# Pixel fidelity screen: this measures graphical agreement, not data accuracy.
from scipy.ndimage import distance_transform_edt
from PIL import ImageDraw
check_im=Image.new('1',(im.shape[1],im.shape[0]));draw=ImageDraw.Draw(check_im)
for a,b in segments:draw.line([a,b],fill=1,width=1)
dist=distance_transform_edt(~np.array(check_im))[mask]
septmeta={'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'status':'Approximate graphical tracing, not original price observations',
 'source_shape_px':[im.shape[1],im.shape[0]],'threshold':85,'annotation_masks_xyxy':excluded,
 'calibration':{'x_pixels':[94,1710],'minutes_after_0843':[0,32],'y_pixels':[17,1005],'index_points':[1105,1060]},
 'segments':len(segments),'smoothing':'None; vertical ink runs retained to preserve spikes',
 'source_ink_to_trace_distance_px':{'median':float(np.median(dist)),'p95':float(np.percentile(dist,95)),'max':float(np.max(dist))},
 'impact_times_source':'https://9-11commission.gov/report/911Report_Ch9.htm'}
(HERE/'september11-extraction.json').write_text(json.dumps(septmeta,indent=2)+'\n')

# 27.4: replot every source vector marker, with no connecting lines.
with (HERE/'challenger-vector-points.csv').open() as f:rows=list(csv.DictReader(f))
spec=[('Lockheed','D',BLUE),('Martin Marietta','^',MUTED),('Rockwell','o',TEAL),('Morton Thiokol','s',RED)]
fig,ax=axes(6.0,.75,.14)
for name,marker,color in spec:
    pts=[r for r in rows if r['company']==name]
    ax.scatter([float(p['time_hour']) for p in pts],[float(p['change_from_open_percent']) for p in pts],
        s=13,marker=marker,linewidths=.65,edgecolors=color,facecolors='white' if marker in ['D','o'] else color,label=name,zorder=3)
ax.set_xlim(11.5,16.08);ax.set_ylim(-14,2)
ax.set_yticks([-12,-8,-4,0]);ax.yaxis.set_major_formatter(FuncFormatter(lambda y,_: f'{y:.0f}'))
ax.grid(axis='y',color=GRID,lw=.7);ax.axhline(0,color='#b7c5ce',lw=.9,zorder=0)
ax.axvline(11+39/60,color=AXIS,lw=1.1,ls=(0,(4,4)),zorder=0)
ax.set_xticks([11.5,12,13,14,15,16],['11:30','12:00','13:00','14:00','15:00','16:00'])
ax.set_xlabel('28 January 1986 · US Eastern time',labelpad=13)
ax.set_title('Price change from opening price (%)',loc='left',fontsize=15,pad=69)
ax.legend(frameon=False,ncol=2,loc='lower left',bbox_to_anchor=(0,1.025),borderaxespad=0,fontsize=12,columnspacing=2.1,handletextpad=.55,markerscale=1.25)
save(fig,'finance-challenger-redraw','The four shuttle contractors after the Challenger explosion',
    'All published vector markers from Maloney and Mulherin (2003), Figure 1, expressed as percent change from each opening price. Morton Thiokol, marked with squares, has the greatest sustained decline and a gap in observations during its trading halt. The vertical reference marks the 11:39 explosion. Points are not joined across trading gaps.')
print('Built three consistent book plots: Fed, September 11 futures, and Challenger.')
