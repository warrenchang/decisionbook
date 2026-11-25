# Communication as projection: geography and build

- Data: [Natural Earth, 1:110m admin-0 countries, v5.1.2](https://github.com/nvkelso/natural-earth-vector/blob/v5.1.2/geojson/ne_110m_admin_0_countries.geojson), [public domain](https://www.naturalearthdata.com/about/terms-of-use/). The local gzip holds the unchanged upstream GeoJSON bytes; SHA-256 of the uncompressed file: `6866c877d39cba9c357620878839b336d569f8c662d3cfab4cb1dbe2d39c977f`.
- Africa is the dataset's Africa continent group; Greenland is `ADM0_A3=GRL`. No political boundaries are drawn. The globe is orthographic, centered at 19°W, 29°N. Both flat maps are centered at 0° longitude and clipped to ±85° latitude. Each map uses one uniform scale to achieve the same width without changing its aspect ratio.
- Projection definitions: [Mercator](https://proj.org/en/stable/operations/projections/merc.html) is conformal, preserving local angles. [Gall–Peters](https://proj.org/en/stable/operations/projections/cea.html) is the spherical cylindrical equal-area form with standard parallels at ±45°. Using the generalized polygons, the builder measures a projected Africa/Greenland area ratio of about 0.93 on Mercator and 13.72 on Gall–Peters. These are illustration checks, not precise geographic area estimates. The builder asserts both ratios stay in range and fails rather than printing a stale claim, to keep the Chapter 33 comparison accurate.
- [Tissot indicatrices](https://en.wikipedia.org/wiki/Tissot%27s_indicatrix): circles of 7° angular radius centred at 25°W and 60°N, 30°N, 0°, drawn on the globe and on both flat maps. They are equal in size on the sphere, so each map's rendering of them is its distortion made visible: Mercator keeps them circular (it is conformal) while area grows as sec²(latitude), and Gall–Peters holds area exactly while the axis ratio runs from 2:1 at the equator through 1:1 at ±45° to about 7:1 at 75°. 25°W keeps all three clear of Greenland and Africa.
- Both maps use the same unlabeled 30° grid, projected with the same functions as the geography. Equal longitude steps stay equally spaced across both maps; equal latitude steps spread apart toward the poles on Mercator and draw closer on Gall–Peters.

From the repository root:

```sh
curl -fsSL https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js -o /tmp/d3-7.9.0.cjs
node scripts/build_communication_projection_figure.cjs /tmp/d3-7.9.0.cjs
node scripts/render_svg_png_fallbacks.cjs figures/communication-projections.svg
```

The first script checks both input digests and generates the SVG. The second uses the book's Playwright renderer to make the matching PNG.
