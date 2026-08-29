#!/usr/bin/env node
/** Inspect the extracted EPUB's XHTML figures and key table/caption changes. */

const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

const epubRoot = path.resolve(process.argv[2] || "/private/tmp/dpn-epub-inspect-20260829/EPUB");
const screenshotDir = path.resolve(process.argv[3] || "/private/tmp/dpn-epub-render-qa");
const textDir = path.join(epubRoot, "text");
const reportPath = path.resolve(__dirname, "..", "audits", "rendered-epub-figure-qa.json");

function chromeExecutable() {
  return [
    process.env.CHROME_PATH,
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
  ].find((candidate) => candidate && fs.existsSync(candidate));
}

function xhtmlFiles() {
  return fs.readdirSync(textDir).filter((name) => name.endsWith(".xhtml")).sort().map((name) => path.join(textDir, name));
}

function fileContaining(files, needle) {
  const found = files.find((file) => fs.readFileSync(file, "utf8").includes(needle));
  if (!found) throw new Error(`Could not find ${needle} in EPUB XHTML`);
  return found;
}

async function main() {
  const files = xhtmlFiles();
  fs.mkdirSync(screenshotDir, { recursive: true });
  const executablePath = chromeExecutable();
  const browser = await chromium.launch({ headless: true, ...(executablePath ? { executablePath } : {}) });
  const issues = [];
  let imagePlacements = 0;
  try {
    for (const viewport of [{ width: 768, height: 1024 }, { width: 390, height: 844 }]) {
      const context = await browser.newContext({ viewport, colorScheme: "light" });
      const page = await context.newPage();
      let viewportImages = 0;
      for (const file of files) {
        await page.goto(pathToFileURL(file).href, { waitUntil: "domcontentloaded" });
        await page.waitForFunction(() => [...document.images].every((image) => image.complete), null, { timeout: 30000 });
        const check = await page.evaluate(() => {
          const images = [...document.images];
          // In Chromium's raw XHTML mode, the documentElement can report a
          // phantom width from MathML/SVG ink even when the reflowing body is
          // fully contained. Body scroll width is the reader-visible test.
          const overflow = document.body.scrollWidth > document.body.clientWidth + 2;
          const offenders = overflow
            ? [...document.querySelectorAll("body *")]
                .filter((element) => element.getBoundingClientRect().right > innerWidth + 2)
                .slice(0, 4)
                .map((element) => `${element.tagName.toLowerCase()}${element.id ? `#${element.id}` : ""}.${[...element.classList].join(".")} (${Math.round(element.getBoundingClientRect().right)}px)`)
            : [];
          if (overflow && offenders.length === 0) {
            offenders.push(
              `html scroll/client ${document.documentElement.scrollWidth}/${document.documentElement.clientWidth}`,
              `body scroll/client ${document.body.scrollWidth}/${document.body.clientWidth}`,
              ...[...document.querySelectorAll("body *")]
                .filter((element) => element.scrollWidth > element.clientWidth + 1)
                .slice(0, 3)
                .map((element) => `${element.tagName.toLowerCase()}${element.id ? `#${element.id}` : ""} scroll/client ${element.scrollWidth}/${element.clientWidth}`),
            );
          }
          return {
            count: images.length,
            broken: images.filter((image) => image.naturalWidth < 1 || image.naturalHeight < 1).map((image) => image.getAttribute("src")),
            overflow,
            offenders,
          };
        });
        viewportImages += check.count;
        if (check.broken.length) issues.push(`${viewport.width}px/${path.basename(file)}: broken ${check.broken.join(", ")}`);
        if (check.overflow) issues.push(`${viewport.width}px/${path.basename(file)}: horizontal page overflow; ${check.offenders.join(", ")}`);
      }
      if (viewport.width === 768) imagePlacements = viewportImages;
      if (viewportImages !== imagePlacements) issues.push(`${viewport.width}px: image count ${viewportImages} differs from ${imagePlacements}`);
      await context.close();
    }

    const context = await browser.newContext({ viewport: { width: 768, height: 1024 }, colorScheme: "light" });
    const page = await context.newPage();
    const captures = [
      ["fig-behavioral-decision-loop", "epub-figure-1-2.png"],
      ["fig-fluency-pathway", "epub-figure-13-2.png"],
      ["fig-reward-prediction-error-shift", "epub-reward-prediction-error.png"],
      ["fig-finance-event-study-drift", "epub-event-study.png"],
      ["tbl-self-fulfilling-self-defeating", "epub-table-6-1.png"],
    ];
    for (const [id, output] of captures) {
      const file = fileContaining(files, `id="${id}"`);
      await page.goto(pathToFileURL(file).href, { waitUntil: "domcontentloaded" });
      const locator = page.locator(`#${id}`).first();
      await locator.scrollIntoViewIfNeeded();
      await locator.screenshot({ path: path.join(screenshotDir, output) });
    }

    const tableFile = fileContaining(files, 'id="tbl-self-fulfilling-self-defeating"');
    await page.goto(pathToFileURL(tableFile).href);
    if (await page.locator("#tbl-self-fulfilling-self-defeating th[scope='rowgroup'][rowspan='2']").count() !== 2) {
      issues.push("EPUB Table 6.1 does not contain two two-row rowgroups");
    }
    const aiFile = fileContaining(files, 'id="tbl-ai-prediction-judgment-causation"');
    await page.goto(pathToFileURL(aiFile).href);
    const aiText = await page.locator("#tbl-ai-prediction-judgment-causation").innerText();
    if (!/Valuation/.test(aiText) || /\nJudgment\n/.test(aiText)) issues.push("EPUB Table 4.1 does not use Valuation");
    await context.close();
  } finally {
    await browser.close();
  }

  const report = {
    status: issues.length ? "FAIL" : "PASS",
    generated: new Date().toISOString(),
    xhtmlDocuments: files.length,
    figurePlacements: imagePlacements,
    viewports: [768, 390],
    issues,
    screenshots: screenshotDir,
  };
  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`);
  process.stdout.write(`${report.status}: ${imagePlacements} EPUB figure placements loaded at 768px and 390px; ${issues.length} issue(s)\n`);
  if (issues.length) process.stdout.write(`${issues.join("\n")}\n`);
  process.exitCode = issues.length ? 1 : 0;
}

main().catch((error) => {
  process.stderr.write(`${error.stack || error}\n`);
  process.exitCode = 1;
});
