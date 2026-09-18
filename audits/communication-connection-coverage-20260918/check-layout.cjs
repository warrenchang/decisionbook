const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'../..');
const chapters={33:'33-communication-language-is-not-a-file-transfer',34:'34-connection-and-repair-warm-honesty-makes-truth-usable'};
const views=[
 [33,'speaker-listener-neural-coupling'],
 [34,'supportive-and-ambivalent-relationships'],
 [34,'tbl-34-deeper-questions'],
 [34,'tbl-34-listening-moves'],
 [34,'tbl-34-honesty-styles'],
 [34,'tbl-34-three-realities'],
 [34,'cross-the-net-carefully'],
 [34,'lab-2-practice-depth-and-responsiveness-14-minutes'],
 [34,'tbl-34-conflict-observer']
];
const walk=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):e.name.endsWith('.xhtml')?[path.join(dir,e.name)]:[]);
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const results=[];
 try{
  const formats=[{kind:'html',files:Object.fromEntries(Object.entries(chapters).map(([n,s])=>[n,path.join(root,'docs/chapters',s+'.html')]))}];
  if(process.argv[2]){
   const files=walk(path.resolve(process.argv[2]));
   formats.push({kind:'epub',files:Object.fromEntries(Object.keys(chapters).map(n=>{
    const match=files.filter(f=>fs.readFileSync(f,'utf8').includes(`id="chapter-${n}-start"`));
    if(match.length!==1)throw Error('Wrong EPUB chapter count '+n);
    return [n,match[0]];
   }))});
  }
  for(const format of formats)for(const n of Object.keys(chapters))for(const width of [1280,390]){
   const page=await browser.newPage({viewport:{width,height:900}});
   await page.goto(pathToFileURL(format.files[n]).href,{waitUntil:'load'});
   await page.evaluate(()=>document.fonts.ready);
   const metrics=await page.evaluate(()=>({pageWidth:document.documentElement.scrollWidth,viewport:innerWidth,brokenImages:[...document.querySelectorAll('main img,body>section img')].filter(n=>!n.complete||!n.naturalWidth).map(n=>n.src),tables:[...document.querySelectorAll('table')].map(n=>({width:n.getBoundingClientRect().width,rows:n.rows.length}))}));
   if(metrics.pageWidth>width+1)throw Error('Page overflow '+JSON.stringify({n,width,...metrics}));
   if(metrics.brokenImages.length)throw Error('Broken images');
   for(const [chapter,id]of views.filter(v=>String(v[0])===n)){
    const node=page.locator(`[id="${id}"]`);
    if(await node.count()!==1)throw Error('Missing ID '+id);
    await node.screenshot({path:path.join(__dirname,`${format.kind}-${id}-${width}.png`),style:'#quarto-header,.quarto-secondary-nav{visibility:hidden!important}'});
   }
   results.push({kind:format.kind,chapter:n,width,...metrics});
   await page.close();
  }
  fs.writeFileSync(path.join(__dirname,'layout-check.json'),JSON.stringify(results,null,2)+'\n');
  console.log(`PASS: ${results.length} chapter/format/viewport layouts; all target sections present; no page overflow or broken images.`);
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
