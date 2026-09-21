// The fallback and size-check images are rendered from the final SVG.
const path = require('path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '../..');
const svg = path.join(root, 'figures/finance-earnings-drift-redraw.svg');
(async () => {
  await sharp(svg, {density: 180}).png().toFile(path.join(root, 'figures/finance-earnings-drift-redraw.png'));
  for (const width of [800, 390]) {
    await sharp(svg, {density: 144}).resize({width}).png().toFile(path.join(__dirname, `redraw-${width}.png`));
  }
})();
