const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + __dirname + '/bomtempo.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  for (const el of await p.$$('.post')) {
    const nome = await el.getAttribute('data-nome');
    await el.screenshot({ path: `${__dirname}/bomtempo-${nome}.png` });
  }
  await b.close(); console.log('ok');
})();
