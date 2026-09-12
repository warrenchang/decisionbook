#!/usr/bin/env node
/** Focused, read-only rendered QA. Writes only this audit's outputs and temp screenshots. */
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '../..');
const docs = path.join(root, 'docs');
const screenshotDir = process.env.READING_ROUTE_SCREENSHOTS || '/private/tmp/decision-book-reading-route';
const reportPath = path.join(__dirname, 'reading-route-qa.json');
const markdownPath = path.join(__dirname, 'reading-route-qa.md');
const phase = process.env.READING_ROUTE_PHASE || 'current-build';
// Remove only fixed navigation from the crop; figure/column layout is unchanged.
const captureStyle = '#quarto-header, .quarto-secondary-nav, #quarto-back-to-top { visibility: hidden !important; }';
const chapter = n => 'chapters/' + fs.readdirSync(path.join(root, 'chapters')).find(x => x.startsWith(String(n).padStart(2,'0')+'-') && x.endsWith('.qmd')).replace(/\.qmd$/,'.html');
const figures = [
 [1,'decision-loop','fig-normative-decision-loop'],
 [1,'decision-making-according-to-behavioral-evidence','fig-behavioral-decision-loop'],
 [21,'urge-wave-observation','fig-urge-wave-observation'],
 [21,'habit-formation-curve','fig-habit-formation-curve'],
 [40,'digital-arrow-affordance','fig-digital-arrow-affordance'],
 [8,'heuristic-substitution','fig-heuristic-substitution'],
 [12,'context-mechanisms','fig-context-mechanisms'],
 [13,'fluency-pathway','fig-fluency-pathway'],
 [33,'communication-grounding','fig-communication-grounding'],
 [34,'conversation-needs-map','fig-conversation-needs-map'],
 [28,'silence-mechanism-diagnostic','fig-silence-mechanisms'],
].map(([n,name,id]) => ({page:chapter(n),name,id}));
const comparisons = [
 [1,'Two examples from commercial practice'],
 [22,'Compare the six questions'],
 [24,'Compare the three lenses'],
 [25,'Compare the cooperation mechanisms'],
 [26,'A reference table for social cues'],
 [28,'Diagnose the pathway'],
].map(([n,title]) => ({chapter:n,page:chapter(n),title}));
const levels = JSON.parse(fs.readFileSync(path.join(__dirname,'tool-levels.json'),'utf8'));
const levelLabels = {core:'Core tool',quick:'Quick check',extension:'Specialized extension'};
const issues = [], warnings = [];
async function load(page, relative) {
 await page.goto(pathToFileURL(path.join(docs,relative)).href, {waitUntil:'domcontentloaded'});
 await page.waitForFunction(() => [...document.images].every(x=>x.complete), null, {timeout:30000});
 await page.evaluate(() => document.fonts.ready);
}
async function inspectFigure(page, f, viewport) {
 await load(page,f.page);
 const figure = page.locator('#'+f.id).first();
 if (await figure.count() !== 1) throw new Error('Missing figure '+f.id);
 const defaultVisible = await figure.isVisible();
 // Optional depth is opened only for its figure inspection, after recording default state.
 await figure.evaluate(el=>{
  for(let parent=el.parentElement;parent;parent=parent.parentElement){
   if(parent.classList.contains('collapse')) parent.classList.add('show');
   if(parent.tagName==='DETAILS') parent.open=true;
  }
 });
 await figure.scrollIntoViewIfNeeded();
 const svgText = fs.readFileSync(path.join(root,'figures',f.name+'.svg'),'utf8');
 const result = await figure.evaluate((figure,{name,svgText,viewport})=>{
  const img=figure.querySelector('img[src$="'+name+'.svg"]');
  if(!img) return {error:'Matching SVG image missing'};
  const rect=o=>({left:o.left,right:o.right,top:o.top,bottom:o.bottom,width:o.width,height:o.height});
  const ir=img.getBoundingClientRect(), main=document.querySelector('main.content')||document.querySelector('main');
  const mr=main.getBoundingClientRect(), pane=img.closest('div[aria-describedby]')||img.parentElement;
  const pr=pane.getBoundingClientRect(), cap=figure.querySelector('figcaption'),cr=cap?.getBoundingClientRect();
  const host=document.createElement('div');host.style.cssText='position:fixed;left:-10000px;top:0;visibility:hidden;pointer-events:none;';
  const shadow=host.attachShadow({mode:'open'});shadow.innerHTML=svgText;document.body.append(host);
  const svg=shadow.querySelector('svg'), vb=svg.viewBox.baseVal;
  const scale=Math.min(ir.width/vb.width,ir.height/vb.height);
  const text=[...shadow.querySelectorAll('text')].map(el=>{
   const cs=getComputedStyle(el), b=el.getBBox(),m=el.getCTM();
   const pts=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));
   const xs=pts.map(p=>p.x),ys=pts.map(p=>p.y);
   const bounds={left:Math.min(...xs),right:Math.max(...xs),top:Math.min(...ys),bottom:Math.max(...ys)};
   return {text:el.textContent,font:Number.parseFloat(cs.fontSize),renderedFont:Number.parseFloat(cs.fontSize)*scale,title:el.classList.contains('title'),bounds};
  });
  const sourceOverflow=text.filter(t=>t.bounds.left < -1 || t.bounds.right > vb.width+1 || t.bounds.top < -1 || t.bounds.bottom > vb.height+1).map(t=>t.text);
  const minFont=Math.min(...text.filter(t=>!t.title).map(t=>t.renderedFont));
  const clip=[];
  for(let a=img.parentElement;a && a!==document.body;a=a.parentElement){
   const cs=getComputedStyle(a),ar=a.getBoundingClientRect();
   if(/hidden|clip/.test(cs.overflowX) && (ir.left<ar.left-2 || ir.right>ar.right+2))clip.push('image clipped horizontally by '+a.tagName+'.'+a.className);
   if(/hidden|clip/.test(cs.overflowY) && (ir.top<ar.top-2 || ir.bottom>ar.bottom+2))clip.push('image clipped vertically by '+a.tagName+'.'+a.className);
  }
  const result={image:rect(ir),main:rect(mr),pane:rect(pr),caption:cr?rect(cr):null,phoneFit:img.classList.contains('phone-fit'),loaded:img.complete&&img.naturalWidth>0,sourceWidth:vb.width,sourceHeight:vb.height,paintedWidth:vb.width*scale,paintedHeight:vb.height*scale,objectFit:getComputedStyle(img).objectFit,scale,minimumRenderedNonTitleFont:minFont,smallestLabels:text.filter(t=>!t.title&&t.renderedFont<12).map(t=>({text:t.text,px:t.renderedFont})),sourceOverflow,clip,paneScrollWidth:pane.scrollWidth,paneClientWidth:pane.clientWidth,captionScrollWidth:cap?.scrollWidth,captionClientWidth:cap?.clientWidth,pageOverflow:document.documentElement.scrollWidth>innerWidth+2};
  host.remove();return result;
 },{name:f.name,svgText,viewport});
 const filename=f.name+'-'+viewport+'.png';
 await figure.screenshot({path:path.join(screenshotDir,filename),animations:'disabled',style:captureStyle});
 const record={...f,viewport,defaultVisible,screenshot:filename,...result};
 const prefix=viewport+'/'+f.name;
 if(result.error)issues.push(prefix+': '+result.error);
 else {
  if(!result.loaded)issues.push(prefix+': image failed to load');
  if(!result.phoneFit)issues.push(prefix+': missing phone-fit class');
  if(result.image.left<result.main.left-2 || result.image.right>result.main.right+2)issues.push(prefix+': exceeds main column');
  if(result.image.left<result.pane.left-2 || result.image.right>result.pane.right+2)issues.push(prefix+': exceeds reading pane');
  if(viewport==='mobile'&&result.paneScrollWidth>result.paneClientWidth+2)issues.push(prefix+': phone-fit pane scrolls horizontally');
  if(result.minimumRenderedNonTitleFont<11.5)issues.push(prefix+': minimum non-title text below approximately12px ('+result.minimumRenderedNonTitleFont.toFixed(2)+'px)');
  else if(result.minimumRenderedNonTitleFont<12)warnings.push(prefix+': minimum supporting text slightly below12px ('+result.minimumRenderedNonTitleFont.toFixed(2)+'px)');
  if(!result.caption)issues.push(prefix+': caption missing');
  else if(result.caption.left<result.main.left-2 ||result.caption.right>result.main.right+2 ||result.captionScrollWidth>result.captionClientWidth+2)issues.push(prefix+': caption exceeds reading width');
  for(const c of result.clip)issues.push(prefix+': '+c);
  for(const c of result.sourceOverflow)issues.push(prefix+': source text exceeds SVG viewBox: '+c);
  if(result.pageOverflow)warnings.push(prefix+': whole page overflows; root whole-book QA should diagnose other content');
 }
 return record;
}
async function inspectComparison(page,item,viewport) {
 await load(page,item.page);
 const result=await page.evaluate(title=>{
  const heading=[...document.querySelectorAll('main h1,main h2,main h3,main h4,main .callout-title-container')].find(el=>{const c=el.cloneNode(true);c.querySelectorAll('.screen-reader-only,.anchorjs-link').forEach(x=>x.remove());return c.textContent.trim()===title;});
  if(!heading)return {found:false};
  const callout=heading.closest('.callout'),container=callout||heading.closest('section')||heading;
  const visible=el=>{for(let p=el;p;p=p.parentElement){const s=getComputedStyle(p);if(s.display==='none'||s.visibility==='hidden')return false;}return el.getBoundingClientRect().height>0;};
  const table=container.querySelector('table');
  return {found:true,isCallout:!!callout,visible:visible(heading)&&visible(container),tablePresent:!!table,tableVisible:table?visible(table):null,collapsedAncestors:[...function*(el){for(let p=el;p;p=p.parentElement)yield p;}(heading)].filter(p=>p.classList.contains('collapse')&&!p.classList.contains('show')).length,text:container.innerText.slice(0,260),selector:container.id?'#'+container.id:null};
 },item.title);
 if(!result.found||!result.visible||result.collapsedAncestors>0||item.chapter!==1&&!result.tableVisible)issues.push(viewport+'/Chapter'+item.chapter+': core comparison is not fully visible by default');
 if(item.chapter===1){
  const numbered=await page.evaluate(()=>[...document.querySelectorAll('main h4')].filter(el=>/^[45]\./.test(el.textContent.trim())).map(el=>({text:el.textContent.trim(),visible:el.getBoundingClientRect().height>0&&!el.closest('.collapse:not(.show)')})));
  result.commercialExamples=numbered;
  if(numbered.length!==2||numbered.some(x=>!x.visible))issues.push(viewport+'/Chapter1: commercial examples4and5 not visible');
 }
 return {...item,viewport,...result};
}
async function inspectTools(page,viewport){
 await load(page,'appendices/appendix-c-portable-course-tools.html');
 const result=await page.evaluate(({levels,labels})=>{
  const boxes=[...document.querySelectorAll('main .callout.tool')];
  return boxes.map(box=>{
   const key=Object.keys(levels).find(k=>box.classList.contains(k)),badge=box.querySelector('.tool-level'),title=box.querySelector('.callout-title-container');
   const b=badge?.getBoundingClientRect(),s=badge?getComputedStyle(badge):null;
   return {key,expected:key?levels[key]:null,title:title?.textContent.trim(),classCorrect:!!key&&box.classList.contains('tool-'+levels[key]),label:badge?.textContent.trim(),labelCorrect:!!key&&badge?.textContent.trim()===labels[levels[key]],badgeVisible:!!b&&b.width>0&&b.height>0&&s.display!=='none'&&s.visibility!=='hidden',badgeFont:s?.fontSize,borderColor:getComputedStyle(box).borderLeftColor,collapsed:!!box.querySelector('.collapse:not(.show)')};
  });
 },{levels,labels:levelLabels});
 if(result.length!==30)issues.push(viewport+'/AppendixC: '+result.length+' tool boxes, expected30');
 if(new Set(result.map(x=>x.borderColor)).size<3)warnings.push(viewport+'/AppendixC: level-specific border styling is not visually distinguished');
 for(const t of result)if(!t.key||!t.classCorrect||!t.labelCorrect||!t.badgeVisible||t.collapsed)issues.push(viewport+'/AppendixC/'+t.key+': missing, hidden, or incorrect level');
 for(const type of ['core','quick','extension']){
  const key=Object.keys(levels).find(k=>levels[k]===type),loc=page.locator('.callout.tool.'+key);
  await loc.scrollIntoViewIfNeeded();
  await loc.screenshot({path:path.join(screenshotDir,'appendix-c-'+type+'-'+viewport+'.png'),animations:'disabled',style:captureStyle});
 }
 return {viewport,count:result.length,tools:result};
}
async function main(){
 fs.mkdirSync(screenshotDir,{recursive:true});
 const needed=[...new Set([...figures,...comparisons].map(x=>x.page)), 'appendices/appendix-c-portable-course-tools.html'];
 const missing=needed.filter(x=>!fs.existsSync(path.join(docs,x)));
 if(missing.length)throw new Error('Rendered pages not yet available: '+missing.join(', '));
 const chrome=process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
 const browser=await chromium.launch({headless:true,executablePath:chrome,args:['--allow-file-access-from-files']});
 const figureResults=[],comparisonResults=[],toolResults=[];
 try{
  for(const vp of [{name:'desktop',width:1440,height:1000},{name:'mobile',width:390,height:844}]){
   const context=await browser.newContext({viewport:{width:vp.width,height:vp.height},colorScheme:'light',deviceScaleFactor:1});
   const page=await context.newPage();
   for(const c of comparisons)comparisonResults.push(await inspectComparison(page,c,vp.name));
   toolResults.push(await inspectTools(page,vp.name));
   for(const f of figures){figureResults.push(await inspectFigure(page,f,vp.name));process.stdout.write(vp.name+' '+f.name+' checked\n');}
   await context.close();
  }
 }finally{await browser.close();}
 const report={status:issues.length?'FAIL':'PASS',phase,generated:new Date().toISOString(),viewports:[{name:'desktop',width:1440,height:1000},{name:'mobile',width:390,height:844}],figureCount:figures.length,figurePlacementChecks:figureResults.length,coreComparisonChecks:comparisonResults.length,toolLabelChecks:toolResults.reduce((n,x)=>n+x.count,0),figures:figureResults,comparisons:comparisonResults,toolLevels:toolResults,issues,warnings,screenshotDir,visualReview:{status:'PENDING',note:'The script does not substitute for visual inspection. Update this field only after reviewing screenshots.'},limitations:['Focused eleven-figure reading-route audit; not all book figures.','Source SVG font sizes are scaled by the smaller measured width/height ratio, allowing for desktop contain letterboxing; CSS font substitution is separately screened using browser-computed SVG text.','Optional figure notes are opened only for figure inspection; comparison visibility is checked on fresh default page loads.','No EPUB or whole-book content audit.','Screenshot crops hide fixed navigation overlays only; figure layout and measured geometry are not changed.']};
 fs.writeFileSync(reportPath,JSON.stringify(report,null,2)+'\n');
 const lines=['# Rendered reading-route QA','',`Run: ${report.generated}. Phase: ${phase}. Automated status: **${report.status}**. Visual review pending.`, '', 'Scope: eleven revised SVGs at desktop 1440 × 1000 and mobile 390 × 844; six core comparison sections on fresh page loads; all thirty Appendix C tool levels at both widths. Optional notes were opened only when needed to inspect their figures.', '', '| Figure | Viewport | Image width | Minimum non-title font | Phone-fit |','| --- | --- | ---: | ---: | --- |',...figureResults.map(x=>`| ${x.name} | ${x.viewport} | ${x.image?.width.toFixed(1)}px | ${x.minimumRenderedNonTitleFont?.toFixed(2)}px | ${x.phoneFit} |`),'','## Automated issues','',...(issues.length?issues.map(x=>'- '+x):['None.']),'','## Warnings','',...(warnings.length?warnings.map(x=>'- '+x):['None.']),'',`Screenshots: ${screenshotDir}. Detailed measurements, default visibility, and per-tool labels are in reading-route-qa.json.`,'','## Limits','','This focused check does not certify all historical book figures, every page, or EPUB display. Figure font sizes are estimated from browser-computed SVG text and the measured contain scale, including desktop height constraints. Screenshot inspection must be recorded separately.'];
 fs.writeFileSync(markdownPath,lines.join('\n')+'\n');
 process.stdout.write(report.status+': '+figureResults.length+' figure checks; '+comparisonResults.length+' default comparison checks; '+report.toolLabelChecks+' tool label checks; '+issues.length+' issues\n');
 if(issues.length)process.stdout.write(issues.join('\n')+'\n');
 process.exitCode=issues.length?1:0;
}
main().catch(e=>{process.stderr.write(e.stack+'\n');process.exitCode=1;});
