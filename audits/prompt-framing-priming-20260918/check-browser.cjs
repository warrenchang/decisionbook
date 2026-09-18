const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
(async()=>{
 const out=path.join(process.cwd(),'audits/prompt-framing-priming-20260918');
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const reports=[];
 try {
  for(const width of [1280,390]){
   const page=await browser.newPage({viewport:{width,height:900}});
   await page.goto(pathToFileURL(path.join(process.cwd(),'docs/chapters/04-the-predictive-mind-perception-is-inference.html')).href);
   const lens=page.locator('#generative-ai-and-predictive-processing');
   const body=lens.locator('.callout-body').first(),header=lens.locator('.callout-header');
   if(await body.isVisible())throw Error('Lens should start closed');
   await header.click();await body.waitFor({state:'visible'});
   await page.waitForFunction(()=>document.querySelector('#generative-ai-and-predictive-processing .callout-collapse').classList.contains('show'));
   const target=lens.locator('#prompt-framing-and-priming');
   if(await target.count()!==1)throw Error('Missing or nonunique subsection anchor');
   const text=(await body.textContent()).replace(/\s+/g,' ');
   for(const phrase of ['Binz and Schulz (2023)','Sinclair et al. (2022)','Jumelet et al., 2024','separate priming comparison'])if(!text.includes(phrase))throw Error('Missing: '+phrase);
   await target.evaluate(n=>window.scrollTo({top:scrollY+n.getBoundingClientRect().top-110,behavior:'instant'}));
   await page.screenshot({path:path.join(out,`prompts-open-${width}.png`)});
   const dimension=await page.evaluate(()=>({viewport:innerWidth,pageWidth:document.documentElement.scrollWidth}));
   if(dimension.pageWidth>width+1)throw Error('Horizontal overflow');
   for(const chapter of ['12-framing-when-the-same-facts-become-different-decisions','13-accessibility-familiarity-and-ease']){
    const link=lens.locator(`a[href*="${chapter}.html"]`);
    if(await link.count()!==1)throw Error('Missing chapter cross-link: '+chapter);
   }
   await header.click();await body.waitFor({state:'hidden'});
   reports.push({...dimension,defaultClosed:true,opensAndCloses:true,newTextPresent:true,chapterLinksPresent:true});
   await page.close();
  }
  fs.writeFileSync(path.join(out,'browser-checks.json'),JSON.stringify(reports,null,2)+'\n');
  console.log(JSON.stringify(reports,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
