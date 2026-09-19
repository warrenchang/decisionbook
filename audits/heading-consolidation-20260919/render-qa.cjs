const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
(async()=>{
 const out=path.resolve('audits/heading-consolidation-20260919');
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 const records=[];
 try {
  for(const width of [1280,390]) {
   const page=await browser.newPage({viewport:{width,height:1000},colorScheme:'light'});
   await page.goto(pathToFileURL(path.resolve('docs/chapters/13-accessibility-familiarity-and-ease.html')).href,{waitUntil:'networkidle'});
   await page.evaluate(()=>document.fonts.ready);
   const section=page.locator('#repetition-can-become-liking-and-truth');
   if(await section.locator('h3,h4').count())throw Error('Short headings remain in repetition section');
   for(const id of ['language-beauty-and-familiarity','flavor-learning-before-birth','repetition-and-perceived-truth']) {
    const target=page.locator('#'+id);
    const result=await target.evaluate(n=>({id:n.id,tag:n.tagName,section:n.closest('section').id,callout:!!n.closest('.callout')}));
    if(result.section!=='repetition-can-become-liking-and-truth'||result.callout)throw Error(JSON.stringify(result));
    records.push({width,...result});
   }
   const overflow=await section.evaluate(n=>n.scrollWidth>n.clientWidth+2);
   if(overflow)throw Error('Repetition section overflows at '+width);
   // Suppress fixed navigation only in the section capture; it otherwise overlays a stitched screenshot.
   await page.addStyleTag({content:'#quarto-header, .quarto-secondary-nav { visibility: hidden !important; }'});
   await section.screenshot({path:path.join(out,`chapter13-${width}.png`)});
   await page.goto(pathToFileURL(path.resolve('docs/chapters/35-negotiation-as-joint-decision-design.html')).href,{waitUntil:'networkidle'});
   for(const [id,parent] of [['positions-interests-and-issues','soft-hard-principled-negotiation'],['design-for-your-own-predictable-errors','interact-learn-propose-and-protect']]) {
    const actual=await page.locator('#'+id).evaluate(n=>n.closest('section').id);
    if(actual!==parent)throw Error(id+' belongs to '+actual+' instead of '+parent);
    records.push({width,id,parent:actual});
   }
   await page.close();
  }
  fs.writeFileSync(path.join(out,'browser-qa.json'),JSON.stringify({status:'PASS',records},null,2)+'\n');
  console.log('PASS: continuous Chapter 13 text on desktop and mobile; Chapter 35 passages under correct sections.');
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
