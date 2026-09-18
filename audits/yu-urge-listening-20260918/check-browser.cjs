const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
(async()=>{
 const out=path.join(process.cwd(),'audits/yu-urge-listening-20260918');
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const targets=[
  {file:'21-habits-wanting-and-self-control',ids:['yu-and-the-flood'],phrases:['Ancient Chinese tradition','You can allow the urge and redirect the action'],link:'#replace-mind-reading-with-verified-understanding'},
  {file:'34-connection-and-repair-warm-honesty-makes-truth-usable',ids:['replace-mind-reading-with-verified-understanding','support-without-trapping-attention'],phrases:['Reflect the event, its felt impact','115 participants','The colleague may still be angry','supposed provocateur'],link:'#yu-and-the-flood'}
 ];
 const reports=[];
 try{
  for(const width of [1280,390])for(const target of targets){
   const page=await browser.newPage({viewport:{width,height:1000}});
   await page.goto(pathToFileURL(path.join(process.cwd(),'docs/chapters',target.file+'.html')).href);
   const text=(await page.locator('main').textContent()).replace(/\s+/g,' ');
   for(const phrase of target.phrases)if(!text.includes(phrase))throw Error('Missing '+phrase);
   for(const id of target.ids){
    const section=page.locator('#'+id);
    if(await section.count()!==1)throw Error('Missing or duplicate '+id);
    if(await section.evaluate(n=>Boolean(n.closest('.callout,.collapse,details'))))throw Error('Section unexpectedly collapsed');
    await section.evaluate(n=>window.scrollTo({top:scrollY+n.getBoundingClientRect().top-110,behavior:'instant'}));
    await page.screenshot({path:path.join(out,`${id}-${width}.png`)});
   }
   const dimensions=await page.evaluate(()=>({viewport:innerWidth,pageWidth:document.documentElement.scrollWidth}));
   if(dimensions.pageWidth>width+1)throw Error('Horizontal overflow');
   const link=page.locator('main a[href$="'+target.link+'"]');
   if(await link.count()!==1)throw Error('Missing or duplicate cross-chapter link');
   const href=new URL(await link.getAttribute('href'),page.url()).href;
   await page.goto(href);
   if(await page.locator(target.link).count()!==1)throw Error('Cross-reference target missing');
   reports.push({chapter:target.file,...dimensions,visibleSections:target.ids,crossChapterLinkResolves:true,textChecks:target.phrases.length});
   await page.close();
  }
  fs.writeFileSync(path.join(out,'browser-checks.json'),JSON.stringify(reports,null,2)+'\n');
  console.log(JSON.stringify(reports,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
