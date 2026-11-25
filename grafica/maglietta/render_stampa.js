const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const svg = fs.readFileSync(__dirname + '/design-stampa.svg', 'utf8');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 3.75 });
  await p.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
  await p.screenshot({ path: __dirname + '/mantra-prompting-stampa-piena.png', omitBackground: true });
  const q = await b.newPage({ viewport: { width: 1200, height: 1600 } });
  await q.setContent(`<html><body style="margin:0;background:#000">${svg}</body></html>`);
  await q.screenshot({ path: __dirname + '/anteprima-stampa-piena.png' });
  await b.close();
})();
