#!/usr/bin/env node
/** Render SVG book figures to tightly matched, high-resolution PNG fallbacks. */

const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

function dimensions(svg, source) {
  const tag = svg.match(/<svg\b[^>]*>/i)?.[0] || "";
  const width = Number(tag.match(/\bwidth=["']([0-9.]+)/i)?.[1]);
  const height = Number(tag.match(/\bheight=["']([0-9.]+)/i)?.[1]);
  if (width > 0 && height > 0) return { width, height };
  const viewBox = tag.match(/\bviewBox=["'][^"']*?([0-9.]+)\s+([0-9.]+)["']/i);
  if (viewBox) return { width: Number(viewBox[1]), height: Number(viewBox[2]) };
  throw new Error(`${source}: SVG needs numeric width/height or a viewBox`);
}

async function main() {
  const sources = process.argv.slice(2);
  if (!sources.length) {
    throw new Error("Usage: render_svg_png_fallbacks.cjs path/to/figure.svg [...]");
  }

  const executablePath = [
    process.env.CHROME_PATH,
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
  ].find((candidate) => candidate && fs.existsSync(candidate));
  const browser = await chromium.launch({
    headless: true,
    ...(executablePath ? { executablePath } : {}),
  });
  try {
    for (const sourceArg of sources) {
      const source = path.resolve(sourceArg);
      const target = source.replace(/\.svg$/i, ".png");
      if (target === source) throw new Error(`${source}: expected an .svg filename`);
      const raw = fs.readFileSync(source, "utf8");
      const svg = raw.replace(/^\s*<\?xml[^>]*>\s*/i, "");
      const { width, height } = dimensions(svg, source);
      const context = await browser.newContext({
        viewport: { width: Math.ceil(width), height: Math.ceil(height) },
        deviceScaleFactor: 1.5,
        colorScheme: "light",
      });
      const page = await context.newPage();
      await page.setContent(
        `<!doctype html><html><head><meta charset="utf-8"><style>` +
          `html,body{margin:0;width:${width}px;height:${height}px;overflow:hidden;background:#fff}` +
          `body>svg{display:block;width:${width}px;height:${height}px}` +
          `</style></head><body>${svg}</body></html>`,
        { waitUntil: "load" },
      );
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: target, type: "png", omitBackground: false });
      await context.close();
      process.stdout.write(`${path.relative(process.cwd(), source)} -> ${path.relative(process.cwd(), target)}\n`);
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  process.stderr.write(`${error.stack || error}\n`);
  process.exitCode = 1;
});
