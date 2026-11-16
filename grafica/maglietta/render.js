const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const svg = fs.readFileSync(__dirname + '/design.svg', 'utf8');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 3.75 });
  const page = bg => `<html><body style="margin:0;background:${bg}">${svg}</body></html>`;
  await p.setContent(page('transparent'));
  await p.screenshot({ path: __dirname + '/mantra-prompting-stampa.png', omitBackground: true });
  await p.setViewportSize({ width: 1200, height: 1600 });
  const q = await b.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 1 });
  await q.setContent(page('#111318'));
  await q.screenshot({ path: __dirname + '/anteprima-maglietta-nera.png' });
  await b.close();
})();
