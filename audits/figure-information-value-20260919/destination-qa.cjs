/** Run from repository root with NODE_PATH pointing to Playwright dependencies.
 * node audits/figure-information-value-20260919/destination-qa.cjs EXTRACTED_EPUB_ROOT
 */
const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url'),{chromium}=require('playwright');
const root=path.resolve(__dirname,'../..'),out=__dirname;
const removed=JSON.parse(fs.readFileSync(path.join(out,'removed-figures.json')));
const sources=[...new Set([...fs.readFileSync(path.join(root,'_quarto-html.yml'),'utf8').matchAll(/^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$/gm)].map(m=>m[1]))];
const epub=path.resolve(process.argv[2]);
const cases=[{format:'html',files:sources.map(s=>path.join(root,'docs',s.replace(/\.qmd$/,'.html'))),widths:[1440,390]}, {format:'epub',files:fs.readdirSync(path.join(epub,'text')).filter(s=>s.endsWith('.xhtml')).map(s=>path.join(epub,'text',s)),widths:[768,390]}];
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROME_PATH||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--allow-file-access-from-files']});
 const results=[],issues=[],screenshots=[];
 try {
  for(const c of cases) for(const width of c.widths){
   const context=await browser.newContext({viewport:{width,height:1000},colorScheme:'light'}),page=await context.newPage();
   for(const file of c.files){
    await page.goto(pathToFileURL(file).href,{waitUntil:'load'});
    await page.evaluate(()=>{document.querySelectorAll('.callout-collapse.collapse').forEach(e=>e.classList.add('show'));document.querySelectorAll('details').forEach(e=>e.open=true)});
    await page.waitForFunction(()=>[...document.images].every(i=>i.complete));
    const result=await page.evaluate(({format,removedIds})=>{
     const main=document.querySelector('main.content')||document.body,rect=main.getBoundingClientRect();
     const imgs=[...main.querySelectorAll('img')],errors=[];
     for(const img of imgs){
      const r=img.getBoundingClientRect();
      if(!img.naturalWidth)errors.push('Broken image: '+img.getAttribute('src'));
      if(r.width>rect.width+2){
       const pane=img.closest('div[aria-describedby]');
       if(!pane||!/auto|scroll/.test(getComputedStyle(pane).overflowX))errors.push('Uncontained image: '+img.getAttribute('src'));
      }
     }
     if(format==='html' ? document.documentElement.scrollWidth>innerWidth+2 : document.body.scrollWidth>document.body.clientWidth+2) errors.push('Horizontal page overflow');
     for(const id of removedIds){
      const target=document.getElementById(id);
      if(target?.querySelector('img')) errors.push('Removed figure still contains image: '+id);
     }
     const fig=document.getElementById('fig-cultural-market-study-redraw'),img=fig?.querySelector('img');
     return {images:imgs.length,errors,musicLab:img?{width:img.getBoundingClientRect().width,height:img.getBoundingClientRect().height,caption:fig.textContent.trim(),smallestEssentialFont:23*Math.min(img.getBoundingClientRect().width/640,img.getBoundingClientRect().height/1090)}:null};
    },{format:c.format,removedIds:removed.map(r=>r.id)});
    results.push({format:c.format,width,page:path.basename(file),...result});
    issues.push(...result.errors.map(e=>`${c.format}/${width}/${path.basename(file)}: ${e}`));
    if(result.musicLab){
     const dest=path.join(out,`music-lab-${c.format}-${width}.png`);
     await page.locator('#fig-cultural-market-study-redraw').screenshot({path:dest});screenshots.push(path.basename(dest));
     if(result.musicLab.smallestEssentialFont<11.5)issues.push(`${c.format}/${width}: Music Lab type too small`);
    }
   }
   await context.close();
  }
 } finally {await browser.close()}
 const report={status:issues.length?'FAIL':'PASS',generated:new Date().toISOString(),issues,screenshots,results};
 fs.writeFileSync(path.join(out,'destination-qa.json'),JSON.stringify(report,null,2)+'\n');
 console.log(report.status+': '+results.length+' page/viewport checks; '+issues.length+' issues');console.log(issues.join('\n'));
 process.exitCode=issues.length?1:0;
})().catch(e=>{console.error(e);process.exitCode=1});
