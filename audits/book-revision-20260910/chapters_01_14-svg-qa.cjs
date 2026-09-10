const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
(async()=>{
 const dir=path.resolve('audits/book-revision-20260910');
 const figs=JSON.parse(fs.readFileSync(path.join(dir,'inventory.json'))).figures.filter(x=>x.owner==='chapters_01_14'&&x.path.endsWith('.svg'));
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',args:['--allow-file-access-from-files']});
 const page=await browser.newPage();const results=[];
 for(const fig of figs){
  await page.goto(pathToFileURL(path.resolve(fig.path)).href);
  const r=await page.evaluate(()=>{
   const svg=document.querySelector('svg'),v=svg.viewBox.baseVal;
   const text=[...svg.querySelectorAll('text')].map(e=>{const b=e.getBoundingClientRect(),r=svg.getBoundingClientRect(),scale=v.width/r.width;return{text:e.textContent.trim(),x:(b.x-r.x)*scale,y:(b.y-r.y)*scale,w:b.width*scale,h:b.height*scale,font:parseFloat(getComputedStyle(e).fontSize)};});
   const outside=text.filter(t=>t.x<-1||t.y<-1||t.x+t.w>v.width+1||t.y+t.h>v.height+1);
   return{viewBox:[v.width,v.height],textElements:text.length,minFont:Math.min(...text.map(t=>t.font)),outside};
  });results.push({path:fig.path,...r});
 }
 await browser.close();fs.writeFileSync(path.join(dir,'chapters_01_14-svg-text-qa.json'),JSON.stringify(results,null,2)+'\n');
 console.log(JSON.stringify({figures:results.length,outside:results.filter(x=>x.outside.length)}));
})().catch(e=>{console.error(e);process.exit(1)});
