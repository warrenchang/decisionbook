// Run with the bundled Node runtime and NODE_PATH pointing to its packages.
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const root = process.cwd();
  const out = __dirname;
  const html = path.join(root, 'docs/chapters/24-behavioral-game-theory-equilibrium-is-a-benchmark-not-a-portrait.html');
  const targets = [{format:'html', file:html}];
  if (process.argv[2]) targets.push({format:'epub', file:path.resolve(process.argv[2])});
  const browser = await chromium.launch({headless:true, executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const results = [];
  try {
    for (const target of targets) {
      for (const width of [1440,390]) {
        const page = await browser.newPage({viewport:{width,height:1000},deviceScaleFactor:1});
        await page.route(/^https?:/,route=>route.abort());
        await page.goto(pathToFileURL(target.file).href,{waitUntil:'load'});
        await page.addStyleTag({content:'html,body {scroll-behavior:auto !important;}'});
        await page.evaluate(() => document.fonts.ready);
        const result = await page.evaluate(() => {
          const ids = ['coordination-shared-expectations-can-do-the-work','private-mutual-common-knowledge','focality-payoff-dominance-and-evidence','commitment-changes-the-game'];
          const positions = ids.map(id => {const e=document.getElementById(id); return {id,top:e ? e.getBoundingClientRect().top : null};});
          const table=document.getElementById('tbl-private-mutual-common-knowledge');
          const allIds=[...document.querySelectorAll('[id]')].map(e=>e.id);
          const text=document.body.innerText;
          const citations=['Aumann','Lewis','Pinker','Rubinstein','Chwe'].map(name=>({name,present:text.includes(name)}));
          const issues=[];
          if(positions.some(p=>p.top===null)) issues.push('Missing chapter section');
          if(positions.some((p,i)=>i && p.top<=positions[i-1].top)) issues.push('Incorrect section order');
          if(!table || table.querySelectorAll('tbody tr').length!==3) issues.push('Knowledge table missing or row count incorrect');
          if(!document.querySelector('a[href="#tbl-private-mutual-common-knowledge"]')) issues.push('Missing numbered table link');
          if(document.documentElement.scrollWidth>window.innerWidth+2) issues.push('Page-wide horizontal overflow');
          if(new Set(allIds).size!==allIds.length) issues.push('Duplicate identifiers');
          if(document.querySelector('.quarto-unresolved-ref')) issues.push('Unresolved cross-reference');
          if(citations.some(c=>!c.present)) issues.push('New source missing');
          return {positions,citations,tableRows:table?.querySelectorAll('tbody tr').length,scrollWidth:document.documentElement.scrollWidth,viewport:window.innerWidth,issues};
        });
        results.push({format:target.format,width,...result});
        await page.locator('#private-mutual-common-knowledge').evaluate(e=>e.scrollIntoView());
        await page.screenshot({path:path.join(out,`${target.format}-${width}-opening.png`)});
        await page.locator('#tbl-private-mutual-common-knowledge').screenshot({path:path.join(out,`${target.format}-${width}-table.png`)});
        await page.locator('#commitment-changes-the-game').evaluate(e=>e.scrollIntoView());
        await page.screenshot({path:path.join(out,`${target.format}-${width}-commitment.png`)});
        await page.close();
      }
    }
  } finally {await browser.close();}
  const report={status:results.some(r=>r.issues.length)?'FAIL':'PASS',results,limit:'Extracted EPUB inspected in Chromium; native EPUB reader pagination not tested.'};
  fs.writeFileSync(path.join(out,'layout-qa.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  process.exitCode=report.status==='FAIL'?1:0;
})().catch(error=>{console.error(error);process.exitCode=1;});
