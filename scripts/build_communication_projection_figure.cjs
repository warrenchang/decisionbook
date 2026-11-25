#!/usr/bin/env node
"use strict";

// See figures-src/communication-projections/README.md for pinned inputs and rebuild commands.
const fs = require("node:fs");
const path = require("node:path");
const zlib = require("node:zlib");
const crypto = require("node:crypto");

const root = path.resolve(__dirname, "..");
const source = path.join(root, "figures-src/communication-projections/ne_110m_admin_0_countries-v5.1.2.geojson.gz");
const d3Path = process.argv[2];
if (!d3Path) throw new Error("Usage: node scripts/build_communication_projection_figure.cjs /path/to/d3-7.9.0.cjs");
const sha256 = (bytes) => crypto.createHash("sha256").update(bytes).digest("hex");
const raw = zlib.gunzipSync(fs.readFileSync(source));
if (sha256(raw) !== "6866c877d39cba9c357620878839b336d569f8c662d3cfab4cb1dbe2d39c977f") {
  throw new Error("Unexpected Natural Earth source bytes");
}
if (sha256(fs.readFileSync(d3Path)) !== "f2094bbf6141b359722c4fe454eb6c4b0f0e42cc10cc7af921fc158fceb86539") {
  throw new Error("Expected the pinned D3 7.9.0 distribution");
}
const d3 = require(path.resolve(d3Path));
const { features } = JSON.parse(raw);
const collections = [
  { color: "#c9d5df", features: [] },
  { color: "#d4793e", label: "Africa", features: [] },
  { color: "#268280", fill: "url(#greenland-hatch)", label: "Greenland", features: [] },
];
for (const feature of features) {
  const { CONTINENT, ADM0_A3 } = feature.properties;
  const group = ADM0_A3 === "GRL" ? 2 : CONTINENT === "Africa" ? 1 : 0;
  const polys = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
  // D3 interprets the interior of a small spherical exterior ring as clockwise.
  const coords = polys.map((poly) => poly.map((ring, i) => {
    const area = ring.slice(1).reduce((sum, [x, y], j) => sum + ring[j][0] * y - x * ring[j][1], 0);
    return (area > 0) === (i === 0) ? ring.slice().reverse() : ring;
  }));
  collections[group].features.push({
    type: "Feature",
    geometry: { type: "MultiPolygon", coordinates: coords },
  });
}
for (const group of collections) group.type = "FeatureCollection";

const ink = "#17324d";
const muted = "#425c72";
const ocean = "#edf4f8";
const grid = "#a2b7c7";
const outline = "#7b94a8";
const cap = 85 * Math.PI / 180;
const width = 302;
const centerY = 435;
const height = 604;
// Tissot indicatrices: circles of equal size on the sphere, drawn as each projection renders them.
// Placed over open Atlantic at 25°W so they clear Greenland and Africa.
const tissotFill = "#b2474b";
const tissotStroke = "#8f3034";
const tissotLon = -25;
const tissotLats = [60, 30, 0];
const tissotCircle = d3.geoCircle().radius(7).precision(2);
const k = Math.SQRT1_2;
const equalAreaRaw = (lambda, phi) => [k * lambda, Math.sin(phi) / k];
const shape = { type: "Sphere" };
const graticule = d3.geoGraticule().step([30, 30])();
const globe = d3.geoOrthographic().rotate([19, -29]).scale(110).translate([189, 128]).precision(0.18);
const figures = [
  { title: "Mercator", x: 21, raw: d3.geoMercatorRaw, scale: width / (2 * Math.PI) },
  { title: "Gall–Peters", x: 337, raw: equalAreaRaw, scale: width / (2 * Math.PI * k) },
];

const label = (x, y, value, size = 27, weight = 400, color = ink, align = "start") =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" fill="${color}" text-anchor="${align}">${value}</text>`;

function layers(project, boundary) {
  const plot = d3.geoPath(project).digits(2);
  const paths = [boundary(ocean, "none", plot),
    `<path d="${plot(graticule)}" fill="none" stroke="${grid}" stroke-width="0.8"/>`];
  for (const group of collections) {
    const d = plot(group);
    paths.push(`<path d="${d}" fill="${group.fill || group.color}" stroke="${group.color}" stroke-width="0.45"/>`);
  }
  for (const latitude of tissotLats) {
    const d = plot(tissotCircle.center([tissotLon, latitude])());
    if (d) paths.push(`<path d="${d}" fill="${tissotFill}" fill-opacity="0.32" stroke="${tissotStroke}" stroke-width="1.1"/>`);
  }
  paths.push(boundary("none", outline, plot));
  return paths.join("\n");
}

const parts = [`<svg xmlns="http://www.w3.org/2000/svg" width="660" height="${height}" viewBox="0 0 660 ${height}" role="img" aria-labelledby="map-title map-desc" font-family="Arial, Helvetica, sans-serif">
<title id="map-title">One Earth, two map projections</title>
<desc id="map-desc">A globe, a Mercator map, and a Gall–Peters map highlight Africa and Greenland. The red circles have equal area on the globe. Mercator enlarges them toward the poles; Gall–Peters preserves their area while changing their shape. Africa is about fourteen times the area of Greenland, yet Mercator draws Greenland slightly larger.</desc>
<defs>
  <pattern id="greenland-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
    <rect width="6" height="6" fill="#268280"/>
    <path d="M0 0V6" stroke="#ffffff" stroke-opacity="0.62" stroke-width="2"/>
  </pattern>
</defs>
<rect width="660" height="${height}" fill="#fff"/>`,
layers(globe, (fill, stroke, plot) => `<path d="${plot(shape)}" fill="${fill}" stroke="${stroke}" stroke-width="1.4"/>`)];
for (const [index, item] of collections.slice(1).entries()) {
  const y = 96 + index * 42;
  parts.push(`<rect x="334" y="${y}" width="22" height="22" rx="3" fill="${item.fill || item.color}"/>`,
    label(369, y + 20, item.label, 28, 400, muted));
}
for (const panel of figures) {
  const [left, right] = [panel.x, panel.x + width];
  const h = panel.scale * panel.raw(0, cap)[1];
  const project = d3.geoProjection(panel.raw).scale(panel.scale).translate([left + width / 2, centerY])
    .clipExtent([[left, centerY - h], [right, centerY + h]]).precision(0.18);
  const area = d3.geoPath(project);
  const ratio = area.area(collections[1]) / area.area(collections[2]);
  panel.ratio = ratio;
  console.log(`${panel.title}: projected Africa / Greenland area ≈ ${ratio.toFixed(2)}`);
  parts.push(label(left + width / 2, 271, panel.title, 33, 700, ink, "middle"),
    layers(project, (fill, stroke) => `<rect x="${left}" y="${(centerY - h).toFixed(2)}" width="${width}" height="${(2 * h).toFixed(2)}" fill="${fill}" stroke="${stroke}" stroke-width="1.4"/>`));
}
// Gall–Peters is equal-area, so its measured ratio is the area ratio; Mercator's shows what the
// page actually displays. Fail loudly if either drifts, rather than printing a stale claim.
const [mercatorRatio, petersRatio] = figures.map((panel) => panel.ratio);
if (!(petersRatio > 13 && petersRatio < 15) || !(mercatorRatio > 0.85 && mercatorRatio < 1)) {
  throw new Error(`Unexpected projected ratios: Mercator ${mercatorRatio.toFixed(2)}, Gall–Peters ${petersRatio.toFixed(2)}`);
}
parts.push("</svg>");
fs.writeFileSync(path.join(root, "figures/communication-projections.svg"), parts.join("\n") + "\n");
