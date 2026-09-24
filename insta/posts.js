const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 1 });
  await p.goto('file:///tmp/claude-0/-home-user-Rebeca-Infoprduto/f44a588c-76ca-527d-8433-d1071a513749/scratchpad/posts.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(900);
  for (let i = 1; i <= 13; i++) {
    await (await p.$('#p' + i)).screenshot({ path: `/home/user/Rebeca-Infoprduto/insta/post-${String(i).padStart(2,'0')}.png` });
  }
  await b.close();
})();
