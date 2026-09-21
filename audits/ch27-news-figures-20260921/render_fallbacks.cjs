const path = require('path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '../..');
(async () => {
 for (const name of ['finance-fed-announcement','finance-september11-futures','finance-challenger-redraw']) {
  const svg=path.join(root,'figures',name+'.svg');
  await sharp(svg,{density:180}).png().toFile(path.join(root,'figures',name+'.png'));
  for (const width of [800,390]) await sharp(svg,{density:144}).resize({width}).png().toFile(path.join(__dirname,`${name}-${width}.png`));
 }
})();
