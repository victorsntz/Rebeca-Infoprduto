const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 } });
  await p.goto('file://' + __dirname + '/bomtempo-flores.html', { waitUntil: 'networkidle' });
  console.log('buque', await p.evaluate(() => window.pronto));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  await (await p.$('#p1')).screenshot({ path: `${__dirname}/bomtempo-flores.png` });
  await b.close(); console.log('ok');
})();
