const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 } });
  await p.goto('file://' + __dirname + '/constante.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const n = await p.$$eval('.post', e => e.length);
  for (let i = 1; i <= n; i++) await (await p.$('#p' + i)).screenshot({ path: `${__dirname}/constante-${i}.png` });
  await b.close(); console.log('posts', n);
})();
