const {chromium}=require('/Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-gpu']});
 const out='/Users/ra25fi/Library/CloudStorage/OneDrive-AalborgUniversitet/decision_book/audits/personal-social-norms-20260919/';
 const checks=[];
 for(const width of [1400,390]){
  const p=await b.newPage({viewport:{width,height:1000}});
  await p.goto('http://127.0.0.1:8836/docs/chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html',{waitUntil:'networkidle'});
  await p.addStyleTag({content:'html{scroll-behavior:auto!important;}'});
  const note=p.locator('.callout.personal-example').filter({hasText:'From my experience: following the crowd despite the sign'});
  await note.screenshot({path:out+'story-'+width+'.png'});
  checks.push({width,overflow:await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),text:await note.innerText()});
  await p.close();
 }
 await b.close();fs.writeFileSync(out+'layout-qa.json',JSON.stringify(checks,null,2)+'\n');
 console.log(JSON.stringify(checks.map(({text,...x})=>x)));
 if(checks.some(x=>x.overflow))process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
