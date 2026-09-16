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
        const ids=['reputation-networks-and-institutions-change-incentives','robot-eyes-and-perceived-observation','mutual-cooperation-and-reward','punishment-and-anticipated-reward','group-identity-changes-the-social-boundary'];
        const nodes=ids.map(id=>document.getElementById(id));
        const all=[...document.querySelectorAll('[id]')].map(e=>e.id);
        const issues=[];
        if(nodes.some(e=>!e))issues.push('Missing target section');
        if(nodes.some((e,i)=>i&&e&&nodes[i-1]&&!(nodes[i-1].compareDocumentPosition(e)&Node.DOCUMENT_POSITION_FOLLOWING)))issues.push('Incorrect section order');
        if([...document.querySelectorAll('h1,h2,h3,h4')].some(e=>e.textContent.includes('Can an image of eyes create reputation?')))issues.push('Removed heading still visible');
        if(document.body.textContent.includes('A coffee-room honesty box raises'))issues.push('Removed honesty-box passage remains');
        if(!document.getElementById('can-an-image-of-eyes-create-reputation')||!document.getElementById('fig-watched-eyes-evidence-update'))issues.push('Legacy anchor missing');
        if(!document.querySelector('a[href$="#research-near-miss-evidence"]'))issues.push('Measurement cross-reference missing');
        if(document.documentElement.scrollWidth>window.innerWidth+2)issues.push('Page-wide horizontal overflow');
        if(new Set(all).size!==all.length)issues.push('Duplicate identifiers');
        if(document.querySelector('.quarto-unresolved-ref'))issues.push('Unresolved cross-reference');
        return {issues,scrollWidth:document.documentElement.scrollWidth,viewport:window.innerWidth};
      });
      results.push({format:target.format,width,...result});
      for(const [label,id] of [['robot','robot-eyes-and-perceived-observation'],['reward','mutual-cooperation-and-reward']]) {
        await page.locator('#'+id).evaluate(e=>window.scrollTo({top:Math.max(0,e.getBoundingClientRect().top+window.scrollY-(window.innerWidth<768?110:20)),behavior:'instant'}));
        await page.screenshot({path:path.join(__dirname,`${target.format}-${width}-${label}.png`)});
      }
      await page.close();
    }
  } finally {await browser.close();}
  const report={status:results.some(r=>r.issues.length)?'FAIL':'PASS',results,limit:'EPUB checked as extracted XHTML, not in a native paginated reader.'};
  fs.writeFileSync(path.join(__dirname,'layout-qa.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  process.exitCode=report.status==='FAIL'?1:0;
})().catch(e=>{console.error(e);process.exitCode=1;});
