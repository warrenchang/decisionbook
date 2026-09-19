const { chromium } = require('/Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const fs = require('fs');
(async () => {
 const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-gpu']});
 const base = 'http://127.0.0.1:8836/docs/chapters/';
 const checks = [];
 const cases = [
  ['valuation-desktop','06-valuation-how-options-become-worth-choosing.html','music-and-cultural-reward',1400,1000],
  ['valuation-phone','06-valuation-how-options-become-worth-choosing.html','music-and-cultural-reward',390,844],
  ['mental-accounting-desktop','20-mental-accounting-money-is-fungible-minds-label-it.html','four-operations-label-bracket-couple-and-close',1400,1000],
  ['narrative-desktop','31-why-stories-move-minds.html','four-mechanisms-of-narrative-persuasion',1400,1000]
 ];
 for (const [name,file,anchor,width,height] of cases) {
  const page = await browser.newPage({viewport:{width,height}});
  await page.goto(base+file,{waitUntil:'networkidle',timeout:30000});
  await page.addStyleTag({content:'html {scroll-behavior:auto!important;}'});
  const found = await page.evaluate(anchor => {
   const el = document.getElementById(anchor);
   if (!el) return false;
   const target = el.tagName==='SPAN' ? el.parentElement.nextElementSibling : el;
   window.scrollTo({top:window.scrollY+target.getBoundingClientRect().top-95,behavior:'instant'});
   return true;
  },anchor);
  const layout = await page.evaluate(() => ({scrollWidth:document.documentElement.scrollWidth, viewportWidth:innerWidth, headings:[...document.querySelectorAll('main h2,main h3')].map(e=>({level:e.tagName,text:e.textContent.trim()}))}));
  await page.screenshot({path:path.join(__dirname,name+'.png')});
  checks.push({name,file,anchor,found,...layout,overflow:layout.scrollWidth>width});
  await page.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(__dirname,'layout-qa.json'),JSON.stringify(checks,null,2)+'\n');
 console.log(JSON.stringify(checks.map(({headings,...r})=>r),null,2));
 if(checks.some(x=>!x.found||x.overflow))process.exit(1);
})().catch(e=>{console.error(e);process.exit(1);});
