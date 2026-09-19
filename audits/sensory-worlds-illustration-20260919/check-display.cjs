// Run from repository root with Playwright on NODE_PATH and an extracted EPUB/ directory argument.
const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url'),{chromium}=require('playwright');
const out=__dirname,root=path.resolve(out,'../..'),epub=process.argv[2];
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',args:['--allow-file-access-from-files']});
 const cases=[{format:'html',file:path.join(root,'docs/chapters/03-attention-what-becomes-evidence.html'),widths:[1440,390]}];
 if(epub){const files=fs.readdirSync(path.join(epub,'text')).filter(x=>x.endsWith('.xhtml')).map(x=>path.join(epub,'text',x));const file=files.find(x=>fs.readFileSync(x,'utf8').includes('id="fig-sensory-windows"'));if(!file)throw Error('EPUB figure missing');cases.push({format:'epub',file,widths:[768,390]})}
 const checks=[];
 try{for(const c of cases)for(const width of c.widths){
  const page=await browser.newPage({viewport:{width,height:950},colorScheme:'light'});
  await page.goto(pathToFileURL(c.file).href,{waitUntil:'load'});
  const loc=page.locator('#fig-sensory-windows');
  if(await loc.count()!==1)throw Error('Figure must occur once');
  await loc.scrollIntoViewIfNeeded();
  const r=await loc.evaluate(el=>{const img=el.querySelector('img'),pane=img.parentElement,ir=img.getBoundingClientRect(),pr=pane.getBoundingClientRect();return {loaded:img.complete&&img.naturalWidth===1536&&img.naturalHeight===1024,imageWidth:ir.width,imageHeight:ir.height,paneWidth:pr.width,scrollable:pane.scrollWidth>pane.clientWidth&&['auto','scroll'].includes(getComputedStyle(pane).overflowX),caption:el.textContent.trim(),bodyOverflow:document.body.scrollWidth>document.body.clientWidth+2,alt:img.alt,oldAssetPresent:[...document.images].some(i=>/sensory-windows-partial-world|attention-bottleneck/.test(i.src))}});
  if(!r.loaded||r.bodyOverflow||r.oldAssetPresent||!/3.2/.test(r.caption))throw Error(JSON.stringify({format:c.format,width,...r}));
  if(width===390&&(!r.scrollable||r.imageWidth<798||r.paneWidth>390))throw Error('Unreadable or uncontained mobile illustration');
  await loc.screenshot({path:path.join(out,`${c.format}-${width}-left.png`)});
  if(width===390){await loc.locator('img').evaluate(i=>{i.parentElement.scrollLeft=i.parentElement.scrollWidth});await loc.screenshot({path:path.join(out,`${c.format}-${width}-right.png`)})}
  checks.push({format:c.format,width,...r});await page.close();
 }}finally{await browser.close()}
 fs.writeFileSync(path.join(out,epub?'display-qa.json':'html-display-qa.json'),JSON.stringify({status:'PASS',checks},null,2)+'\n');console.log('PASS: '+checks.length+' figure display checks.');
})().catch(e=>{console.error(e);process.exit(1)});
