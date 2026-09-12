const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
const root=process.cwd();
const format=process.argv[2]||'html';
const records=JSON.parse(fs.readFileSync('audits/chapter-openings-20260912/changes.json','utf8'));
const temp=process.env.OPENING_CHECK_TEMP||'/private/tmp/decision-book-chapter-openings-20260912';
const epubDir=path.join(temp,'epub/EPUB/text');
function fileFor(r){
 if(format==='html')return path.join(root,'docs',r.file.replace(/\.qmd$/,'.html'));
 const needle=`id="chapter-${String(r.chapter).padStart(2,'0')}-start"`;
 return path.join(epubDir,fs.readdirSync(epubDir).find(f=>f.endsWith('.xhtml')&&fs.readFileSync(path.join(epubDir,f),'utf8').includes(needle)));
}
(async()=>{
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 const results=[];
 for(const r of records){
  await page.goto(pathToFileURL(fileFor(r)).href,{waitUntil:'domcontentloaded'});
  const check=await page.evaluate(({expected,anchors,chapter})=>{
   const container=document.querySelector('main.content')||document.body;
   const ep=container.querySelector('.chapter-epigraph');
   const core=container.querySelector('.core-idea');
   const h1=container.querySelector('h1');
   const preceding=(a,b)=>Boolean(a.compareDocumentPosition(b)&Node.DOCUMENT_POSITION_FOLLOWING);
   const norm=s=>s.replace(/[‘’]/g,"'").replace(/[“”]/g,'"').replace(/\s+/g,' ').trim();
   if(!ep||!core||!h1)return {error:'Missing title, epigraph, or Core Idea'};
   const subtitles=[...container.querySelectorAll('p')].filter(p=>preceding(h1,p)&&preceding(p,ep)&&p.children.length===1&&p.firstElementChild.tagName.toLowerCase()==='em');
   const headings=[...container.querySelectorAll('h2,h3')].filter(h=>preceding(ep,h)&&preceding(h,core));
   const firstProse=[...container.querySelectorAll('p')].find(p=>!ep.contains(p)&&preceding(ep,p)&&preceding(p,core)&&p.textContent.trim());
   const goals=[...container.querySelectorAll('h2')].find(h=>norm(h.textContent)==='Learning goals');
   const missingAnchors=anchors.filter(id=>!document.getElementById(id));
   const numbered=[...container.querySelectorAll('h2')].filter(h=>/^\d+\. /.test(h.textContent.trim()));
   const error=[];
   if(subtitles.length!==1||norm(subtitles[0]?.textContent||'')!==norm(expected))error.push('Subtitle mismatch');
   if(headings.length)error.push('Heading before opening scene');
   if(!firstProse||!preceding(ep,firstProse)||!preceding(firstProse,core)||!goals||!preceding(core,goals))error.push('Opening order mismatch');
   if(missingAnchors.length)error.push('Missing legacy anchor');
   if(chapter===36&&(numbered.length!==5||!preceding(goals,numbered[0])))error.push('Chapter 36 stage sequence mismatch');
   return {subtitleCount:subtitles.length,subtitle:subtitles[0]?.textContent,openingHeadingCount:headings.length,missingAnchors,errors:error};
  },{expected:r.kept_subtitle.slice(1,-1),anchors:[...r.retained_opening_anchors,...(r.moved_heading?[r.moved_heading.anchor]:[])],chapter:r.chapter});
  results.push({chapter:r.chapter,...check});
 }
 const errors=results.filter(r=>r.error||r.errors?.length);
 const report={format,chapters:results.length,errors,results};
 fs.writeFileSync(path.join(root,'audits/chapter-openings-20260912',format+'-openings.json'),JSON.stringify(report,null,2)+'\n');
 if(errors.length)throw Error(JSON.stringify(errors));
 for(const width of (format==='html'?[1440,390]:[768,390])){
  await page.setViewportSize({width,height:1000});
  for(const n of (format==='html'?[2,17,36]:[2,17])){
   const r=records.find(r=>r.chapter===n);
   await page.goto(pathToFileURL(fileFor(r)).href,{waitUntil:'load'});
   await page.evaluate(()=>document.fonts.ready);
   const h1=page.locator('h1').first();
   await h1.scrollIntoViewIfNeeded();
   await page.screenshot({path:path.join(temp,`${format}-chapter-${n}-${width}.png`),style:'#quarto-header,.quarto-secondary-nav,#quarto-back-to-top{visibility:hidden!important}'});
  }
 }
 console.log(`PASS: all ${results.length} ${format} chapter openings have one subtitle, an unheaded scene, Core Idea, and Learning goals; legacy anchors retained.`);
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
