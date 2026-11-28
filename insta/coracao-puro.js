const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + __dirname + '/coracao-puro.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  await (await p.$('#p1')).screenshot({ path: `${__dirname}/coracao-puro-story.png` });
  await (await p.$('#p2')).screenshot({ path: `${__dirname}/coracao-puro-feed.png` });
  await b.close(); console.log('ok');
})();
