const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 } });
  await p.goto('file://' + __dirname + '/sola.html', { waitUntil: 'networkidle' });
  console.log('buque', await p.evaluate(() => window.pronto));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  const n = await p.$$eval('.post', e => e.length);
  for (let i = 1; i <= n; i++) await (await p.$('#p' + i)).screenshot({ path: `${__dirname}/sola-${i}.png` });
  await b.close(); console.log('posts', n);
})();
