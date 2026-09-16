// Run with the bundled Node runtime and NODE_PATH pointing to its packages.
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const root = process.cwd();
  const out = __dirname;
  const targets = [{format:'html', file:path.join(root, 'docs/chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html')}];
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
          const ids = ['bridge-preferences-norms-and-enforcement-are-different','group-identity-changes-the-social-boundary','superordinate-goals-and-cooperation','common-ingroup-identity','application-build-cooperation-around-the-diagnosed-failure'];
          const positions = ids.map(id => {const e=document.getElementById(id); return {id,top:e ? e.getBoundingClientRect().top : null};});
          const section=document.getElementById('group-identity-changes-the-social-boundary');
          const table=document.getElementById('tbl-cooperation-mechanisms');
          const allIds=[...document.querySelectorAll('[id]')].map(e=>e.id);
          const text=document.body.innerText;
          const citations=['Balliet','Sherif','Gaertner','Levine','Dovidio','Tajfel','Chen'].map(name=>({name,present:text.includes(name)}));
          const issues=[];
          const tableScrollers=table ? [table,...table.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+2 && ['auto','scroll'].includes(getComputedStyle(e).overflowX)) : [];
          const horizontalTableScroll=tableScrollers.map(e=>{const original=e.scrollLeft;e.scrollLeft=e.scrollWidth;const reached=e.scrollLeft;e.scrollLeft=original;return {available:e.scrollWidth-e.clientWidth,reached};});
          if(horizontalTableScroll.some(s=>s.reached<s.available-2)) issues.push('Table horizontal scrolling failed');
          if(positions.some(p=>p.top===null)) issues.push('Missing chapter section');
          if(positions.some((p,i)=>i && p.top<=positions[i-1].top)) issues.push('Incorrect section order');
          if(section?.closest('.callout,details,.collapse')) issues.push('Main discussion placed inside optional notes');
          if(!table || table.querySelectorAll('tbody tr').length!==5) issues.push('Cooperation table missing or row count incorrect');
          if(!table?.textContent.includes('Shared task across groups')) issues.push('New table row missing');
          if(!document.querySelector('a[href$="#tbl-cooperation-mechanisms"]')) issues.push('Missing numbered table link');
          if(!document.querySelector('a[href$="#private-mutual-common-knowledge"]')) issues.push('Missing common-knowledge cross-reference');
          if(document.documentElement.scrollWidth>window.innerWidth+2) issues.push('Page-wide horizontal overflow');
          if(new Set(allIds).size!==allIds.length) issues.push('Duplicate identifiers');
          if(document.querySelector('.quarto-unresolved-ref')) issues.push('Unresolved cross-reference');
          if(citations.some(c=>!c.present)) issues.push('Source missing');
          return {positions,citations,tableRows:table?.querySelectorAll('tbody tr').length,horizontalTableScroll,scrollWidth:document.documentElement.scrollWidth,viewport:window.innerWidth,issues};
        });
        results.push({format:target.format,width,...result});
        for(const [label,id] of [['opening','group-identity-changes-the-social-boundary'],['goals','superordinate-goals-and-cooperation'],['identity','common-ingroup-identity'],['repair','rebuild-cooperation-without-erasing-differences']]) {
          await page.locator('#'+id).evaluate(e=>window.scrollTo({top:Math.max(0,e.getBoundingClientRect().top+window.scrollY-(window.innerWidth<768?110:20)),behavior:'instant'}));
          await page.screenshot({path:path.join(out,`${target.format}-${width}-${label}.png`)});
        }
        if(target.format==='html' && width===390) {
          await page.locator('#tbl-cooperation-mechanisms').evaluate(e=>window.scrollTo({top:e.getBoundingClientRect().top+window.scrollY-110,behavior:'instant'}));
          await page.screenshot({path:path.join(out,`${target.format}-${width}-table.png`)});
          await page.locator('#tbl-cooperation-mechanisms').evaluate(e=>[e,...e.querySelectorAll('*')].filter(n=>n.scrollWidth>n.clientWidth+2 && ['auto','scroll'].includes(getComputedStyle(n).overflowX)).forEach(n=>n.scrollLeft=n.scrollWidth));
          await page.screenshot({path:path.join(out,`${target.format}-${width}-table-right.png`)});
        } else {
          await page.locator('#tbl-cooperation-mechanisms').screenshot({path:path.join(out,`${target.format}-${width}-table.png`)});
        }
        await page.close();
      }
    }
  } finally {await browser.close();}
  const report={status:results.some(r=>r.issues.length)?'FAIL':'PASS',results,limit:'Extracted EPUB inspected in Chromium; native EPUB reader pagination not tested.'};
  fs.writeFileSync(path.join(out,'layout-qa.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  process.exitCode=report.status==='FAIL'?1:0;
})().catch(error=>{console.error(error);process.exitCode=1;});
