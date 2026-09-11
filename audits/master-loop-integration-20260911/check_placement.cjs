const {chromium}=require('playwright'),fs=require('fs'),path=require('path');const {pathToFileURL}=require('url');
(async()=>{
 const target=process.argv[2],format=process.argv[3],out='audits/master-loop-integration-20260911';
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});const checks=[];
 for(const [name,width,height] of [['desktop',1280,1024],['mobile',390,844]]){
  const page=await browser.newPage({viewport:{width,height}});await page.goto(pathToFileURL(path.resolve(target)).href,{waitUntil:'domcontentloaded'});
  const fig=page.locator('#fig-master-loop'),img=fig.locator('img');await img.scrollIntoViewIfNeeded();await page.waitForFunction(()=>{const i=document.querySelector('#fig-master-loop img');return i&&i.complete&&i.naturalWidth>0});
  const check=await img.evaluate(i=>{const b=i.getBoundingClientRect(),fit=getComputedStyle(i).objectFit;const scale=fit==='contain'?Math.min(i.clientWidth/700,i.clientHeight/978):i.clientWidth/700;return {width:b.width,height:b.height,left:b.left,right:b.right,viewport:innerWidth,objectFit:fit,artworkWidth:700*scale,artworkHeight:978*scale,minLabelPx:26*scale,src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0}});
  check.format=format;check.size=name;check.pass=check.loaded&&check.left>=-1&&check.right<=width+1&&Math.abs(check.artworkHeight/check.artworkWidth-978/700)<.01&&check.minLabelPx>=12;
  await fig.screenshot({path:path.join(out,format+'-'+name+'.png')});checks.push(check);await page.close();
 }
 await browser.close();fs.writeFileSync(path.join(out,format+'-placement-checks.json'),JSON.stringify(checks,null,2)+'\n');console.log(JSON.stringify(checks));if(checks.some(c=>!c.pass))process.exit(1);
})();
