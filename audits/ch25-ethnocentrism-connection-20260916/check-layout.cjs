const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
(async()=>{
  const targets=[{format:'html',file:path.join(process.cwd(),'docs/chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html')},{format:'epub',file:path.resolve(process.argv[2])}];
  const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const results=[];
  try {
    for(const target of targets) for(const width of [1440,390]) {
      const page=await browser.newPage({viewport:{width,height:1000},deviceScaleFactor:1});
      await page.route(/^https?:/,r=>r.abort());
      await page.goto(pathToFileURL(target.file).href,{waitUntil:'load'});
      await page.addStyleTag({content:'html,body{scroll-behavior:auto!important;}'});
      await page.evaluate(()=>document.fonts.ready);
      const result=await page.evaluate(()=>{
        const ids=['group-identity-changes-the-social-boundary','ingroup-favoritism-and-evolution','superordinate-goals-and-cooperation','advanced-research-track-evolutionary-and-spatial-models','ethnocentrism-as-selective-cooperation'];
        const nodes=ids.map(id=>document.getElementById(id));
        const all=[...document.querySelectorAll('[id]')].map(e=>e.id);
        const issues=[];
        if(nodes.some(e=>!e))issues.push('Missing section');
        if(nodes.some((e,i)=>i&&e&&nodes[i-1]&&!(nodes[i-1].compareDocumentPosition(e)&Node.DOCUMENT_POSITION_FOLLOWING)))issues.push('Incorrect section order');
        for(const id of ['ingroup-favoritism-and-evolution','advanced-research-track-evolutionary-and-spatial-models','superordinate-goals-and-cooperation'])if(!document.querySelector(`a[href$="#${id}"]`))issues.push('Missing model cross-reference '+id);
        for(const id of ['robot-eyes-and-perceived-observation','mutual-cooperation-and-reward'])if(!document.getElementById(id))issues.push('Prior revision missing '+id);
        if(document.documentElement.scrollWidth>window.innerWidth+2)issues.push('Page-wide horizontal overflow');
        if(new Set(all).size!==all.length)issues.push('Duplicate identifiers');
        if(document.querySelector('.quarto-unresolved-ref'))issues.push('Unresolved cross-reference');
        return {issues,scrollWidth:document.documentElement.scrollWidth,viewport:window.innerWidth};
      });
      await page.locator('#ingroup-favoritism-and-evolution').evaluate(e=>window.scrollTo({top:Math.max(0,e.getBoundingClientRect().top+window.scrollY-(window.innerWidth<768?110:20)),behavior:'instant'}));
      await page.screenshot({path:path.join(__dirname,`${target.format}-${width}-bridge.png`)});
      const callout=page.locator('.callout').filter({has:page.locator('#ethnocentrism-as-selective-cooperation')});
      const toggle=callout.locator('[data-bs-toggle="collapse"]');
      if(await toggle.count()) {
        await toggle.first().click();
        await page.waitForFunction(()=>!document.querySelector('.collapsing'));
      }
      await page.locator('#ethnocentrism-as-selective-cooperation').waitFor({state:'visible'});
      await page.locator('#ethnocentrism-as-selective-cooperation').evaluate(e=>window.scrollTo({top:Math.max(0,e.getBoundingClientRect().top+window.scrollY-(window.innerWidth<768?110:20)),behavior:'instant'}));
      await page.screenshot({path:path.join(__dirname,`${target.format}-${width}-model.png`)});
      const expandedWidth=await page.evaluate(()=>document.documentElement.scrollWidth);
      if(expandedWidth>width+2)result.issues.push('Expanded notes overflow');
      results.push({format:target.format,width,...result,expandedWidth});
      await page.close();
    }
  } finally {await browser.close();}
  const report={status:results.some(r=>r.issues.length)?'FAIL':'PASS',results,limit:'EPUB checked as extracted XHTML; native-reader pagination not tested.'};
  fs.writeFileSync(path.join(__dirname,'layout-qa.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  process.exitCode=report.status==='FAIL'?1:0;
})().catch(e=>{console.error(e);process.exitCode=1;});
