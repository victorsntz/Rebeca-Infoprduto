const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 820, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/midiakit.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const pgs = await p.$$('.pg');
  for (let i = 0; i < pgs.length; i++) await pgs[i].screenshot({ path: `${__dirname}/midiakit-${i + 1}.png` });
  await p.pdf({ path: `${__dirname}/midiakit-rebeca-fortunato.pdf`, width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
  await b.close(); console.log('paginas', pgs.length);
})();
