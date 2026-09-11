const fs=require('fs');
const photo=fs.readFileSync('figures/traffic-light-context-scene.png').toString('base64');
const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="800" height="820" viewBox="0 0 800 820" role="img" aria-labelledby="title desc">
<title id="title">The same light without and with learned traffic-signal context</title>
<desc id="desc">A gray textured glass lens appears alone on a blue-green field at left. At right the identical lens, at the same scale and height, occupies the upper position in a familiar three-lamp traffic signal. Only the right panel contains a frame, other lamps, and a street scene. The original photographic-style scene is AI-generated; the two target interiors reuse one opaque grayscale rendering of the same image region.</desc>
<defs>
 <image id="scene" width="1024" height="1536" href="data:image/png;base64,${photo}"/>
 <clipPath id="lens-clip"><circle cx="506" cy="286" r="149"/></clipPath>
 <filter id="neutral-gray" color-interpolation-filters="sRGB">
  <feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"/>
  <feComponentTransfer><feFuncR type="linear" slope="0.8" intercept="0.22"/><feFuncG type="linear" slope="0.8" intercept="0.22"/><feFuncB type="linear" slope="0.8" intercept="0.22"/></feComponentTransfer>
 </filter>
 <g id="neutral-lens" clip-path="url(#lens-clip)"><use href="#scene" filter="url(#neutral-gray)"/></g>
 <clipPath id="left-clip"><rect x="25" y="88" width="350" height="700" rx="18"/></clipPath>
 <clipPath id="right-clip"><rect x="425" y="88" width="350" height="700" rx="18"/></clipPath>
</defs>
<rect width="800" height="820" fill="#ffffff"/>
<g font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#183047"><text x="200" y="52">Isolated light</text><text x="600" y="52">Traffic-light context</text></g>
<g id="isolated-panel" clip-path="url(#left-clip)">
 <rect x="25" y="88" width="350" height="700" fill="#3aaba8"/>
 <use href="#neutral-lens" transform="translate(-55 88) scale(0.5)"/>
</g>
<g id="context-panel" clip-path="url(#right-clip)">
 <rect x="425" y="88" width="350" height="700" fill="#3aaba8"/>
 <use href="#scene" transform="translate(345 88) scale(0.5)"/>
 <rect x="425" y="88" width="350" height="700" fill="#4bc9b9" opacity="0.50"/>
 <use href="#neutral-lens" transform="translate(345 88) scale(0.5)"/>
</g>
</svg>\n`;
fs.writeFileSync('figures/traffic-light-color-context.svg',svg);
