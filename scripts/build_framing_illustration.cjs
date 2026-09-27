/* Assemble Figure 12.1 from original generated artwork and exact reused views.
 * Requires Node.js and sharp. Run: node scripts/build_framing_illustration.cjs
 * The SVG reuses each selected region plus one frame definition in both rows.
 * Raster verification compares every pixel, including the frame, in each pair.
 * The artwork is illustrative; no empirical observations are represented.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
const dir = path.join(root, 'figures-src/framing');
const master = fs.readFileSync(path.join(dir, 'master-scene.png'));
const imagined = fs.readFileSync(path.join(dir, 'imagined-surroundings.png'));
const sprinkler = fs.readFileSync(path.join(dir, 'master-scene-rain-streaks.png'));
const wetGround = fs.readFileSync(path.join(dir, 'master-scene-wet-ground.png'));
const rain = fs.readFileSync(path.join(dir, 'imagined-surroundings-rain-aligned.png'));
const width = 1536, height = 1076, opening = 280, rim = 12;
const frameSize = opening + 2 * rim;
const sourceTop = 476, sceneTop = 528;
const selections = [
  {name: 'buildings', x: 124, y: 532, topX: 104},
  {name: 'park', x: 626, y: 579, topX: 616},
  // The third view excludes the sprinkler head at approximately (1135, 842).
  {name: 'water', x: 1232, y: 650, topX: 1128},
];
const topY = 186;
const imaginedOpacity = 0.72;
const framedView = (s) => `<g id="view-${s.name}">
  <rect width="${frameSize}" height="${frameSize}" fill="#85542f"/>
  <svg x="${rim}" y="${rim}" width="${opening}" height="${opening}" viewBox="${s.x} ${s.y} ${opening} ${opening}" overflow="hidden"><use href="#master"/></svg>
  <use href="#frame"/>
</g>`;
const placements = selections.flatMap(s => [
  `<use href="#view-${s.name}" x="${s.topX}" y="${topY}"/>`,
  `<use href="#view-${s.name}" x="${s.x-rim}" y="${sceneTop+s.y-sourceTop-rim}"/>`,
]);
const svg = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title desc">
<title id="title">Selected evidence and possible reconstructed surroundings</title>
<desc id="desc">The lower scene contains buildings, a park and a lawn sprinkler. The third frame shows falling water droplets but excludes the sprinkler head. Each frame and its contents are repeated exactly above, against lighter imagined surroundings: a dense city, an extensive park, or an ordinary rainy street. The imagined surroundings go beyond the observed evidence.</desc>
<defs>
  <linearGradient id="wet-ground-transition" gradientUnits="userSpaceOnUse" x1="1000" y1="0" x2="1160" y2="0">
    <stop offset="0" stop-color="black"/><stop offset="1" stop-color="white"/>
  </linearGradient>
  <mask id="wet-ground-mask" maskUnits="userSpaceOnUse" x="1000" y="850" width="536" height="174">
    <rect x="1000" y="850" width="536" height="174" fill="url(#wet-ground-transition)"/>
  </mask>
  <g id="master">
    <image width="1536" height="1024" href="data:image/png;base64,${master.toString('base64')}"/>
    <!-- Replace only the right-hand example; retain the accepted left and middle artwork. -->
    <svg x="1000" y="476" width="536" height="548" viewBox="1000 476 536 548" overflow="hidden">
      <image width="1536" height="1024" href="data:image/png;base64,${sprinkler.toString('base64')}"/>
    </svg>
    <!-- Reuse the accepted water trajectories; update only the wet ground beneath them. -->
    <svg x="1000" y="850" width="536" height="174" viewBox="1000 850 536 174" overflow="hidden" mask="url(#wet-ground-mask)">
      <image width="1536" height="1024" href="data:image/png;base64,${wetGround.toString('base64')}"/>
    </svg>
  </g>
  <g id="imagined">
    <image width="1536" height="512" href="data:image/png;base64,${imagined.toString('base64')}"/>
    <svg x="1024" y="0" width="512" height="512" viewBox="1024 0 512 512" overflow="hidden">
      <image width="1536" height="512" href="data:image/png;base64,${rain.toString('base64')}"/>
    </svg>
  </g>
  <g id="frame">
    <path d="M0 0H304L292 12H12Z" fill="#bd8d5e"/>
    <path d="M0 0V304L12 292V12Z" fill="#a47448"/>
    <path d="M304 0V304L292 292V12Z" fill="#85542f"/>
    <path d="M0 304H304L292 292H12Z" fill="#946039"/>
    <rect x="1" y="1" width="302" height="302" fill="none" stroke="#68452f" stroke-width="2"/>
    <rect x="11" y="11" width="282" height="282" fill="none" stroke="#68452f" stroke-width="2"/>
  </g>
  ${selections.map(framedView).join('\n')}
</defs>
<rect width="${width}" height="${height}" fill="white"/>
<use href="#imagined" x="0" y="0" opacity="${imaginedOpacity}"/>
<svg x="0" y="${sceneTop}" width="1536" height="548" viewBox="0 ${sourceTop} 1536 548" overflow="hidden"><use href="#master"/></svg>
${placements.join('\n')}
</svg>`;

(async () => {
  const metadata = await sharp(master).metadata();
  if (metadata.width !== 1536 || metadata.height !== 1024) throw Error('Unexpected master dimensions');
  const sprinklerMetadata = await sharp(sprinkler).metadata();
  if (sprinklerMetadata.width !== 1536 || sprinklerMetadata.height !== 1024) throw Error('Unexpected sprinkler artwork dimensions');
  const wetGroundMetadata = await sharp(wetGround).metadata();
  if (wetGroundMetadata.width !== 1536 || wetGroundMetadata.height !== 1024) throw Error('Unexpected wet-ground artwork dimensions');
  const svgFile = path.join(dir, 'framing-three-windows.svg');
  fs.writeFileSync(svgFile, svg);
  const pngFile = path.join(root, 'figures/framing-three-windows.png');
  await sharp(Buffer.from(svg)).png().toFile(pngFile);
  const checks = [];
  for (const s of selections) {
    const upper = {left: s.topX, top: topY, width: frameSize, height: frameSize};
    const lower = {left: s.x-rim, top: sceneTop+s.y-sourceTop-rim, width: frameSize, height: frameSize};
    const a = await sharp(pngFile).extract(upper).raw().toBuffer();
    const b = await sharp(pngFile).extract(lower).raw().toBuffer();
    let unequalChannels = 0;
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) unequalChannels++;
    if (unequalChannels) throw Error(`${s.name}: ${unequalChannels} unequal channels`);
    checks.push({name: s.name, source: {x:s.x,y:s.y,width:opening,height:opening}, upper, lower, unequalChannels, identical: true});
  }
  const report = {figure:'fig-framing-three-windows', width, height, frameSize, opening, imaginedOpacity,
    masterSha256:crypto.createHash('sha256').update(master).digest('hex'),
    imaginedSha256:crypto.createHash('sha256').update(imagined).digest('hex'),
    sprinklerSha256:crypto.createHash('sha256').update(sprinkler).digest('hex'),
    wetGroundSha256:crypto.createHash('sha256').update(wetGround).digest('hex'),
    rainSha256:crypto.createHash('sha256').update(rain).digest('hex'),
    outputSha256:crypto.createHash('sha256').update(fs.readFileSync(pngFile)).digest('hex'),
    checks};
  fs.writeFileSync(path.join(dir, 'pixel-consistency.json'), JSON.stringify(report, null, 2)+'\n');
  console.log(`PASS: ${checks.length} pairs of ${frameSize} x ${frameSize} framed views are pixel-identical.`);
})().catch(error => { console.error(error); process.exit(1); });
