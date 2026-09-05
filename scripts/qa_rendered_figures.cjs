#!/usr/bin/env node
/** Audit every configured book figure in the rendered HTML at desktop and phone widths. */

const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const docs = path.join(root, "docs");
const reportPath = path.join(root, "audits", "rendered-figure-qa.json");
const screenshotDir = process.argv[2] || "/private/tmp/dpn-final-render-qa";

function bookPages() {
  const config = fs.readFileSync(path.join(root, "_quarto-html.yml"), "utf8");
  const qmd = [...config.matchAll(/^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$/gm)].map((match) => match[1]);
  return [...new Set(qmd)].map((source) => path.join(docs, source.replace(/\.qmd$/i, ".html")));
}

function chromeExecutable() {
  return [
    process.env.CHROME_PATH,
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
  ].find((candidate) => candidate && fs.existsSync(candidate));
}

async function inspectPage(page, file, viewportName) {
  const relative = path.relative(docs, file);
  await page.goto(pathToFileURL(file).href, { waitUntil: "domcontentloaded" });
  await page.waitForFunction(() => [...document.images].every((image) => image.complete), null, { timeout: 30000 });

  const result = await page.evaluate((name) => {
    const main = document.querySelector("main.content") || document.querySelector("main");
    const mainRect = main?.getBoundingClientRect();
    const images = [...document.querySelectorAll('main img[src*="figures/"]')];
    const issues = [];
    for (const [index, image] of images.entries()) {
      const rect = image.getBoundingClientRect();
      const src = image.getAttribute("src") || `image-${index + 1}`;
      if (!image.complete || image.naturalWidth < 1 || image.naturalHeight < 1) {
        issues.push(`${src}: image did not load`);
        continue;
      }
      if (rect.width < 40 || rect.height < 40) issues.push(`${src}: rendered smaller than 40 px`);
      if (!mainRect) continue;
      const isSvg = /\.svg(?:$|[?#])/i.test(src);
      const readingPane = image.closest('div[aria-describedby]');
      if (name === "desktop") {
        if (rect.left < mainRect.left - 2 || rect.right > mainRect.right + 2) {
          issues.push(`${src}: exceeds desktop content column`);
        }
      } else if (isSvg && rect.width > mainRect.width + 2) {
        if (!readingPane) {
          issues.push(`${src}: wide mobile SVG lacks a reading pane`);
        } else {
          const style = getComputedStyle(readingPane);
          if (!/(auto|scroll)/.test(style.overflowX) || readingPane.scrollWidth <= readingPane.clientWidth) {
            issues.push(`${src}: wide mobile SVG is not deliberately scrollable`);
          }
          const paneRect = readingPane.getBoundingClientRect();
          if (paneRect.right > mainRect.right + 2 || paneRect.left < mainRect.left - 2) {
            issues.push(`${src}: mobile reading pane exceeds content column`);
          }
        }
      } else if (!isSvg && (rect.left < mainRect.left - 2 || rect.right > mainRect.right + 2)) {
        issues.push(`${src}: raster image exceeds mobile content column`);
      }
      const outerFigure = image.closest("figure");
      const caption = outerFigure?.querySelector("figcaption");
      if (caption && !caption.textContent.trim()) issues.push(`${src}: empty caption`);
    }
    if (document.documentElement.scrollWidth > innerWidth + 2) {
      const offenders = [...document.querySelectorAll("main *")]
        .filter((element) => element.getBoundingClientRect().right > innerWidth + 2)
        .slice(0, 4)
        .map((element) => {
          const label = [element.tagName.toLowerCase(), element.id ? `#${element.id}` : "", ...element.classList].join(".");
          return `${label} (${Math.round(element.getBoundingClientRect().right)}px)`;
        });
      issues.push(`page creates horizontal overflow: ${document.documentElement.scrollWidth}px > ${innerWidth}px; ${offenders.join(", ")}`);
    }
    return { imageCount: images.length, issues };
  }, viewportName);
  return { page: relative, viewport: viewportName, ...result };
}

async function screenshotFigure(page, relative, selector, outputName) {
  await page.goto(pathToFileURL(path.join(docs, relative)).href, { waitUntil: "domcontentloaded" });
  const locator = page.locator(selector).first();
  await locator.scrollIntoViewIfNeeded();
  await locator.screenshot({ path: path.join(screenshotDir, outputName) });
}

async function main() {
  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.mkdirSync(screenshotDir, { recursive: true });
  const pages = bookPages();
  const missing = pages.filter((file) => !fs.existsSync(file));
  if (missing.length) throw new Error(`Missing rendered pages: ${missing.join(", ")}`);

  const executablePath = chromeExecutable();
  const browser = await chromium.launch({
    headless: true,
    args: ["--allow-file-access-from-files"],
    ...(executablePath ? { executablePath } : {}),
  });
  const results = [];
  try {
    for (const viewport of [
      { name: "desktop", width: 1440, height: 1000 },
      { name: "mobile", width: 390, height: 844 },
    ]) {
      const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, colorScheme: "light" });
      const page = await context.newPage();
      for (const file of pages) results.push(await inspectPage(page, file, viewport.name));
      await context.close();
    }

    const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, colorScheme: "light" });
    const page = await context.newPage();
    const screenshots = [
      ["parts/part-1.html", "main img[src$='master-loop-part-1.svg']", "part-loop-desktop.png"],
      ["chapters/01-how-decisions-should-be-made-and-how-they-actually-are.html", "#fig-normative-decision-loop", "normative-decision-loop-desktop.png"],
      ["chapters/01-how-decisions-should-be-made-and-how-they-actually-are.html", "#fig-behavioral-decision-loop", "behavioral-decision-loop-desktop.png"],
      ["chapters/02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.html", "#fig-option-information", "better-decision-process-desktop.png"],
      ["chapters/13-accessibility-familiarity-and-ease.html", "#fig-fluency-pathway", "figure-13-2-desktop.png"],
      ["chapters/21-habits-wanting-and-self-control.html", "#fig-habit-formation-curve", "habit-formation-desktop.png"],
      ["chapters/21-habits-wanting-and-self-control.html", "#fig-urge-wave-observation", "urge-wave-observation-desktop.png"],
      ["chapters/21-habits-wanting-and-self-control.html", "#fig-reward-prediction-error-shift", "reward-prediction-error-desktop.png"],
      ["chapters/27-markets-mispricing-and-bubbles.html", "#fig-finance-event-study-drift", "event-study-desktop.png"],
      ["chapters/05-expectations-when-predictions-become-causes.html", "#tbl-self-fulfilling-self-defeating", "table-5-1-desktop.png"],
      ["chapters/04-the-predictive-mind-perception-is-inference.html", "#fig-context-b13-demonstration", "context-b13-desktop.png"],
      ["chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-personal-mimicry-crossed-arms", "personal-mimicry-desktop.png"],
      ["chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-social-learning-culture", "figure-26-1-desktop.png"],
      ["chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-norm-message-diagnostic", "figure-26-4-desktop.png"],
      ["chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-social-pathways", "figure-26-5-desktop.png"],
      ["chapters/38-designing-better-agreements.html", "#fig-lie-cues-belief-gap", "lie-cues-desktop.png"],
      ["chapters/40-choice-architecture-the-environment-gets-a-vote.html", "#fig-mpg-fuel-use", "mpg-fuel-use-desktop.png"],
      ["chapters/40-choice-architecture-the-environment-gets-a-vote.html", "#fig-choice-architecture-simplified-remote", "simplified-remote-desktop.png"],
      ["chapters/08-fast-and-frugal-thinking.html", "#fig-stroop-interference-lab", "stroop-interference-desktop.png"],
      ["chapters/04-the-predictive-mind-perception-is-inference.html", "#fig-perception-context-lab", "perception-context-desktop.png"],
      ["chapters/15-samples-randomness-regression-and-calibration.html", "#fig-monty-hall-protocol", "monty-hall-desktop.png"],
      ["chapters/12-framing-when-the-same-facts-become-different-decisions.html", "#fig-assumed-choice-eggs", "assumed-choice-eggs-desktop.png"],
      ["chapters/07-the-narrator-after-choice-why-reasons-are-not-always-causes.html", "#fig-choice-blindness-swap", "choice-blindness-desktop.png"],
      ["chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-asch-line-comparison", "asch-lines-desktop.png"],
      ["appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.html", "#fig-schelling-emergence", "schelling-emergence-desktop.png"],
      ["chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html", "#fig-fairness-entitlements-redraw", "fairness-entitlements-desktop.png"],
      ["chapters/11-when-context-rewrites-comparison.html", "#fig-subscription-decoy", "subscription-decoy-desktop.png"],
      ["chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html", "#fig-watched-eyes-evidence-update", "watched-eyes-desktop.png"],
      ["chapters/40-choice-architecture-the-environment-gets-a-vote.html", "#fig-digital-arrow-affordance", "digital-arrow-desktop.png"],
    ];
    for (const [relative, selector, output] of screenshots) await screenshotFigure(page, relative, selector, output);
    await context.close();

    const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 }, colorScheme: "light" });
    const mobilePage = await mobileContext.newPage();
    await screenshotFigure(
      mobilePage,
      "chapters/13-accessibility-familiarity-and-ease.html",
      "#fig-fluency-pathway",
      "figure-13-2-mobile.png",
    );
    await screenshotFigure(mobilePage, "chapters/01-how-decisions-should-be-made-and-how-they-actually-are.html", "#fig-normative-decision-loop", "normative-decision-loop-mobile.png");
    await screenshotFigure(mobilePage, "chapters/01-how-decisions-should-be-made-and-how-they-actually-are.html", "#fig-behavioral-decision-loop", "behavioral-decision-loop-mobile.png");
    await screenshotFigure(mobilePage, "chapters/02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.html", "#fig-option-information", "better-decision-process-mobile.png");
    await screenshotFigure(mobilePage, "chapters/21-habits-wanting-and-self-control.html", "#fig-habit-formation-curve", "habit-formation-mobile.png");
    await screenshotFigure(mobilePage, "chapters/21-habits-wanting-and-self-control.html", "#fig-urge-wave-observation", "urge-wave-observation-mobile.png");
    await screenshotFigure(mobilePage, "chapters/04-the-predictive-mind-perception-is-inference.html", "#fig-context-b13-demonstration", "context-b13-mobile.png");
    await screenshotFigure(mobilePage, "chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-social-learning-culture", "figure-26-1-mobile.png");
    await screenshotFigure(mobilePage, "chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-norm-message-diagnostic", "figure-26-4-mobile.png");
    await screenshotFigure(mobilePage, "chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-social-pathways", "figure-26-5-mobile.png");
    await screenshotFigure(mobilePage, "chapters/38-designing-better-agreements.html", "#fig-lie-cues-belief-gap", "lie-cues-mobile.png");
    await screenshotFigure(mobilePage, "chapters/40-choice-architecture-the-environment-gets-a-vote.html", "#fig-mpg-fuel-use", "mpg-fuel-use-mobile.png");
    await screenshotFigure(mobilePage, "chapters/08-fast-and-frugal-thinking.html", "#fig-stroop-interference-lab", "stroop-interference-mobile.png");
    await screenshotFigure(mobilePage, "chapters/04-the-predictive-mind-perception-is-inference.html", "#fig-perception-context-lab", "perception-context-mobile.png");
    await screenshotFigure(mobilePage, "chapters/15-samples-randomness-regression-and-calibration.html", "#fig-monty-hall-protocol", "monty-hall-mobile.png");
    await screenshotFigure(mobilePage, "chapters/12-framing-when-the-same-facts-become-different-decisions.html", "#fig-assumed-choice-eggs", "assumed-choice-eggs-mobile.png");
    await screenshotFigure(mobilePage, "chapters/07-the-narrator-after-choice-why-reasons-are-not-always-causes.html", "#fig-choice-blindness-swap", "choice-blindness-mobile.png");
    await screenshotFigure(mobilePage, "chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html", "#fig-asch-line-comparison", "asch-lines-mobile.png");
    await screenshotFigure(mobilePage, "appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.html", "#fig-schelling-emergence", "schelling-emergence-mobile.png");
    await screenshotFigure(mobilePage, "chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html", "#fig-fairness-entitlements-redraw", "fairness-entitlements-mobile.png");
    await screenshotFigure(mobilePage, "chapters/11-when-context-rewrites-comparison.html", "#fig-subscription-decoy", "subscription-decoy-mobile.png");
    await screenshotFigure(mobilePage, "chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html", "#fig-watched-eyes-evidence-update", "watched-eyes-mobile.png");
    await screenshotFigure(mobilePage, "chapters/40-choice-architecture-the-environment-gets-a-vote.html", "#fig-digital-arrow-affordance", "digital-arrow-mobile.png");
    await mobileContext.close();

    const validationContext = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
    const validationPage = await validationContext.newPage();
    await validationPage.goto(pathToFileURL(path.join(docs, "chapters/05-expectations-when-predictions-become-causes.html")).href);
    const rowgroups = await validationPage.locator("#tbl-self-fulfilling-self-defeating th[scope='rowgroup'][rowspan='2']").count();
    await validationPage.goto(pathToFileURL(path.join(docs, "chapters/41-decision-hygiene-build-a-process-that-can-learn.html")).href);
    const valuation = await validationPage.locator("#tbl-ai-prediction-judgment-causation").innerText();
    await validationPage.goto(pathToFileURL(path.join(docs, "chapters/08-fast-and-frugal-thinking.html")).href);
    const daughterCaption = await validationPage.locator("#fig-daughter-finger-counting figcaption").innerText();
    await validationContext.close();

    const totalByViewport = Object.fromEntries(
      ["desktop", "mobile"].map((name) => [name, results.filter((result) => result.viewport === name).reduce((sum, result) => sum + result.imageCount, 0)]),
    );
    const issues = results.flatMap((result) => result.issues.map((issue) => `${result.viewport}/${result.page}: ${issue}`));
    // The book contains 113 rendered placements; the base loop is deliberately
    // repeated as a navigation device across Part openers.
    if (totalByViewport.desktop !== 113 || totalByViewport.mobile !== 113) {
      issues.push(`configured rendered figure placement count is ${JSON.stringify(totalByViewport)}, expected 113 in each viewport`);
    }
    if (rowgroups !== 2) issues.push(`The self-fulfilling and self-defeating table has ${rowgroups} two-row rowgroups; expected 2`);
    if (!/Valuation/.test(valuation) || /\nJudgment\n/.test(valuation)) issues.push("Table 4.1 terminology is not Valuation");
    if (!/System 2/.test(daughterCaption) || !/System 1/.test(daughterCaption) || !/4 \+ 1/.test(daughterCaption)) {
      issues.push("Figure 8.3 caption does not state the System 2 to System 1 transition");
    }

    const report = {
      status: issues.length ? "FAIL" : "PASS",
      generated: new Date().toISOString(),
      configuredPages: pages.length,
      renderedFigures: totalByViewport,
      checks: results,
      table61TwoRowGroups: rowgroups,
      issues,
      screenshots: screenshotDir,
    };
    fs.writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`);
    process.stdout.write(`${report.status}: ${totalByViewport.desktop} figure placements checked at desktop and mobile widths; ${issues.length} issue(s)\n`);
    if (issues.length) process.stdout.write(`${issues.join("\n")}\n`);
    process.exitCode = issues.length ? 1 : 0;
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  process.stderr.write(`${error.stack || error}\n`);
  process.exitCode = 1;
});
