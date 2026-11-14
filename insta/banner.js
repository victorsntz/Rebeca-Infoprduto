const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2600, height: 1500 } });
  for (const [hash, suf] of [['', ''], ['?guias', '-guias']]) {
    await p.goto('file://' + __dirname + '/banner.html' + hash, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    for (const id of ['b1', 'b2']) await (await p.$('#' + id)).screenshot({ path: `${__dirname}/youtube-capa-${id.slice(1)}${suf}.png` });
  }
  await b.close(); console.log('ok');
})();
