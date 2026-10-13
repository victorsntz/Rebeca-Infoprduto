const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 1 });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + process.cwd() + '/timoteo.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(800);
  const n = await p.$$eval('.post', els => els.length);
  for (let i = 1; i <= n; i++) await (await p.$('#p' + i)).screenshot({ path: `/home/user/Rebeca-Infoprduto/insta/timoteo-${i}.png` });
  await b.close(); console.log('posts', n);
})();
