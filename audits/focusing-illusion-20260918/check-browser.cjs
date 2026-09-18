const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
(async()=>{
 const out=path.join(process.cwd(),'audits/focusing-illusion-20260918');
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const reports=[];
 try{
  for(const width of [1280,390]){
   const page=await browser.newPage({viewport:{width,height:900}});
   await page.goto(pathToFileURL(path.join(process.cwd(),'docs/chapters/22-deciding-for-a-better-life-satisfaction-connection-and-meaning.html')).href);
   const section=page.locator('#focusing-illusion');
   if(await section.count()!==1)throw Error('Missing or nonunique focusing-illusion anchor');
   const text=(await section.textContent()).replace(/\s+/g,' ');
   for(const phrase of ['weekly calendars','Schkade and Kahneman (1998)','prospective study of 27 fans','Meaningful achievement'])if(!text.includes(phrase))throw Error('Missing '+phrase);
   for(const id of ['focusing-illusion','bring-the-rest-of-the-day-into-the-forecast']){
    await page.locator('#'+id).evaluate(n=>window.scrollTo({top:scrollY+n.getBoundingClientRect().top-115,behavior:'instant'}));
    await page.screenshot({path:path.join(out,`${id}-${width}.png`)});
   }
   const dimensions=await page.evaluate(()=>({viewport:innerWidth,pageWidth:document.documentElement.scrollWidth}));
   if(dimensions.pageWidth>width+1)throw Error('Horizontal overflow');
   if(await page.locator('#social-comparison-and-the-focusing-illusion').count()!==1)throw Error('Old link target lost');
   reports.push({...dimensions,newSectionPresent:true,oldLinkTargetPreserved:true,textChecks:4});
   await page.close();
  }
  fs.writeFileSync(path.join(out,'browser-checks.json'),JSON.stringify(reports,null,2)+'\n');
  console.log(JSON.stringify(reports,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
