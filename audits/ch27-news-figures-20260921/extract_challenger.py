"""Extract all plotted marker centers from the paper's original Figure 1.
Usage: python extract_challenger.py /path/to/challenger.pdf
Requires PyMuPDF; no original numerical trade records are inferred.
"""
from pathlib import Path
import sys,csv,json,hashlib
import pymupdf
HERE=Path(__file__).resolve().parent
source=Path(sys.argv[1]); doc=pymupdf.open(source); page=doc[5]
# PDF points, read from the original plot frame; page coordinates point down.
left,top,right,bottom=87.10900115966797,75.74298095703125,393.0050048828125,240.02200317382812
kind={('f',4):'Lockheed',('fs',3):'Martin Marietta',('fs',4):'Rockwell',('fs',1):'Morton Thiokol'}
rows=[]
for index,path in enumerate(page.get_drawings()):
 r=path['rect']; key=(path['type'],len(path['items']))
 if not (key in kind and 2.3<r.width<2.5 and 2.3<r.height<2.5): continue
 cx,cy=(r.x0+r.x1)/2,(r.y0+r.y1)/2
 if not (left<cx<right and top<cy<bottom): continue
 hour=11+(cx-left)*6/(right-left)
 ratio=1.02+(cy-top)*(.86-1.02)/(bottom-top)
 rows.append((kind[key],index,cx,cy,hour,ratio,100*(ratio-1)))
with (HERE/'challenger-vector-points.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['company','pdf_path_index','x_pdf','y_pdf','time_hour','price_relative_to_open','change_from_open_percent']);w.writerows(rows)
counts={k:sum(r[0]==k for r in rows) for k in kind.values()}
assert all(v>100 for v in counts.values())
meta={'source_url':'https://maloney.people.clemson.edu/challenger.pdf','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'page_index':5,'printed_page':458,'figure':1,'axis_frame_pdf_points':[left,top,right,bottom],'axis_limits':{'time_hours':[11,17],'price_ratio':[.86,1.02]},'observations':len(rows),'markers_by_company':counts,'status':'All vector marker centers from the published plot; not original transaction records. Repeated and overlapping source markers are retained.'}
(HERE/'challenger-extraction.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
