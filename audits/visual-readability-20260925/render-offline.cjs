// Offline rendering of generated HTML/CSS. No browser navigation or network.
const fs=require('fs'),path=require('path');
const {chromium}=require('playwright');
const root=process.cwd();
const epubRoot=process.argv[2] ? path.resolve(process.argv[2]) : null;
const artifactRoot=epubRoot || path.join(root,'docs');
const out=path.join(root,'audits/visual-readability-20260925/visual-qa');fs.mkdirSync(out,{recursive:true});
const cases=[['22-deciding-for-a-better-life','fig-cold-water-better-ending'],['24-coordination-and-focal-points','fig-stag-hunt-belief-payoffs'],['30-persuasion','fig-elaboration-quadrant'],['38-designing-better-agreements','fig-contract-state-payoffs']];
const mime={'.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2','.woff':'font/woff','.jpg':'image/jpeg'};
function dataurl(p){return 'data:'+(mime[path.extname(p)]||'application/octet-stream')+';base64,'+fs.readFileSync(p).toString('base64')}
function local(dir,url){if(/^(https?:|data:|#)/.test(url))return null;const p=path.resolve(dir,url.split(/[?#]/)[0]);return p.startsWith(artifactRoot+'/')&&fs.existsSync(p)?p:null}
function cssEmbedded(file){return fs.readFileSync(file,'utf8').replace(/url\(["']?([^\)'"\s]+)["']?\)/g,(m,u)=>{const p=local(path.dirname(file),u);return p?'url("'+dataurl(p)+'")':m})}
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const results=[];
 try{
 for(const [stem,id] of cases){
  const p=epubRoot ? fs.readdirSync(path.join(epubRoot,'text')).filter(n=>n.endsWith('.xhtml')).map(n=>path.join(epubRoot,'text',n)).find(f=>fs.readFileSync(f,'utf8').includes('id="'+id+'"')) : path.join(root,'docs/chapters',stem+'.html');
  if(!p)throw new Error('Missing '+id);
  const dir=path.dirname(p);
  let html=fs.readFileSync(p,'utf8').replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi,'');
  html=html.replace(/<link\b[^>]*>/gi,m=>{const href=m.match(/href="([^"]+)"/)?.[1];const f=href&&local(dir,href);return f&&f.endsWith('.css')?'<style>'+cssEmbedded(f)+'</style>':''});
  html=html.replace(/(<img\b[^>]*?\bsrc=")([^"]+)(")/gi,(m,a,u,z)=>{const f=local(dir,u);return f?a+dataurl(f)+z:m});
  for(const width of (epubRoot ? [390,768] : [390,1280])){
   const context=await browser.newContext({viewport:{width,height:1000},deviceScaleFactor:1,colorScheme:'light'});
   const page=await context.newPage();await page.route('**/*',r=>r.abort());
   await page.setContent(html,{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);
   const figure=page.locator('#'+id);
   await figure.screenshot({path:path.join(out,(epubRoot?'epub-':'')+id+'-'+width+'.png')});
   const geom=await figure.evaluate(el=>{const im=el.querySelector('img');const box=el.getBoundingClientRect(),ib=im.getBoundingClientRect();return {figureWidth:box.width,imageWidth:ib.width,imageHeight:ib.height,naturalWidth:im.naturalWidth,naturalHeight:im.naturalHeight,imageComplete:im.complete,caption:el.querySelector('figcaption')?.innerText}});
   results.push({id,viewport:width,source:p,...geom});await context.close();
  }
 }
 fs.writeFileSync(path.join(out,(epubRoot?'epub-':'')+'rendered-geometry.json'),JSON.stringify({method:'Generated HTML with its local CSS and image assets embedded; scripts and network disabled; offline browser rendering',results},null,2)+'\n');
 console.log(JSON.stringify(results.map(({id,viewport,figureWidth,imageWidth,imageComplete})=>({id,viewport,figureWidth,imageWidth,imageComplete})),null,2));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
