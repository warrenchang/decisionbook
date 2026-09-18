const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
(async()=>{
 const out=path.join(process.cwd(),'audits/brain-urge-practice-20260918');
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const reports=[];
 try{
  for(const width of [1280,390]){
   const page=await browser.newPage({viewport:{width,height:900}});
   await page.goto(pathToFileURL(path.join(process.cwd(),'docs/chapters/21-habits-wanting-and-self-control.html')).href);
   const brain=page.locator('#observing-an-urge-with-brain');
   if(await brain.count()!==1)throw Error('Missing or nonunique BRAIN section');
   const text=(await brain.textContent()).replace(/\s+/g,' ');
   for(const phrase of ['Breathe, Recognize, Allow, Investigate, and Non-identify','Briefly notice the sensations','rise, peak, and subside'])if(!text.includes(phrase))throw Error('Missing '+phrase);
   for(const id of ['observing-an-urge-with-brain','tbl-20-brain','fig-urge-wave-observation']){
    const locator=page.locator('#'+id);
    if(await locator.count()!==1)throw Error('Missing or nonunique '+id);
    const visible=await locator.isVisible();
    const insideCollapse=await locator.evaluate(n=>Boolean(n.closest('.callout,.collapse,details')));
    if(!visible||insideCollapse)throw Error(id+' is not in the visible main narrative');
   }
   for(const id of ['observing-an-urge-with-brain','tbl-20-brain','fig-urge-wave-observation','decide-how-to-return-after-a-lapse']){
    await page.locator('#'+id).evaluate(n=>window.scrollTo({top:scrollY+n.getBoundingClientRect().top-115,behavior:'instant'}));
    await page.screenshot({path:path.join(out,`${id}-${width}.png`)});
   }
   for(const id of ['optional-practice-observing-an-urge-with-brain','optional-research-and-practice-notes','create-space-without-demanding-that-the-urge-disappear','research-urge-surfing'])if(await page.locator('#'+id).count()!==1)throw Error('Old anchor lost: '+id);
   const image=page.locator('#fig-urge-wave-observation img');
   if(!await image.evaluate(n=>n.complete&&n.naturalWidth>0&&n.alt.length>30))throw Error('Figure image or alt text missing');
   const dimensions=await page.evaluate(()=>({viewport:innerWidth,pageWidth:document.documentElement.scrollWidth}));
   if(dimensions.pageWidth>width+1)throw Error('Horizontal page overflow');
   const focus=page.locator('#create-space-without-demanding-that-the-urge-disappear a[href*="22-deciding-for-a-better-life"][href$="#focusing-illusion"]');
   if(await focus.count()!==1)throw Error('Focusing-illusion cross-reference missing');
   const target=new URL(await focus.getAttribute('href'),page.url());
   await page.goto(target.href);
   if(await page.locator('#focusing-illusion').count()!==1)throw Error('Focusing-illusion target missing');
   reports.push({...dimensions,brainInMainText:true,tableAndFigureVisible:true,preservedAnchors:4,figureLoadedWithAltText:true,focusingIllusionLinkResolves:true});
   await page.close();
  }
  fs.writeFileSync(path.join(out,'browser-checks.json'),JSON.stringify(reports,null,2)+'\n');
  console.log(JSON.stringify(reports,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
