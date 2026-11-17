# Gera bomtempo-flores.html: "Deus é bom o tempo todo" numa colagem de flores,
# com carta escrita à mão no fundo e painel bordô (papel de parede jacobino do sola.html).
s = open("sola.html").read()
defs = s[s.index("const DEFS = (id,c) => `"):]
defs = defs[:defs.index("`;") + 2]
html = r'''<!doctype html><html><head><meta charset="utf-8">
<style>
@font-face{font-family:"Apple";src:url("fonts/homemade-apple.ttf")}
@font-face{font-family:"Caslon";src:url("../site/assets/fonts/LibreCaslonText-Regular.ttf")}
body{margin:0;background:#333}
.post{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 20px;background:#EADCC5}
.post svg{position:absolute;inset:0}
.carta{position:absolute;left:-90px;top:-60px;width:1300px;font-family:"Apple";font-size:30px;line-height:64px;color:#4A3A2E;opacity:.42;transform:rotate(-4deg)}
.flor{position:absolute;filter:drop-shadow(0 8px 12px rgba(40,15,10,.32))}
.etiqueta{position:absolute;text-align:center;color:#3B2A20}
.etiqueta span{position:relative}
</style></head><body>
<script>
''' + defs + r'''
function pinta(d, c){
  return d.replace(/class="f1"/g, `fill="${c.fill1}" stroke="${c.traco}" stroke-width="1.4"`)
          .replace(/class="f2"/g, `fill="${c.fill2}" stroke="${c.traco}" stroke-width="1.4"`)
          .replace(/class="ln"/g, `fill="none" stroke="${c.traco}" stroke-width="1.2" stroke-linecap="round"`)
          .replace(/class="vn"/g, `fill="none" stroke="${c.traco}" stroke-width="1.8" stroke-linecap="round"`)
          .replace(/class="dt"/g, `fill="${c.traco}"`);
}
// Recorte de papel com a borda irregular (sempre igual: sorteio com semente fixa).
let semente = 7;
const sorte = () => ((semente = (semente * 16807) % 2147483647) / 2147483647);
function rasgado(x, y, w, h, passo, mexe){
  const p = [];
  for (let i = 0; i <= w; i += passo) p.push([x + i, y + (sorte() - .5) * mexe]);
  for (let i = 0; i <= h; i += passo) p.push([x + w + (sorte() - .5) * mexe, y + i]);
  for (let i = w; i >= 0; i -= passo) p.push([x + i, y + h + (sorte() - .5) * mexe]);
  for (let i = h; i >= 0; i -= passo) p.push([x + (sorte() - .5) * mexe, y + i]);
  return p.map(q => q.map(v => v.toFixed(1)).join(",")).join(" ");
}
const CARTA = "Querida amiga, hoje acordei pensando em como Deus foi fiel em cada estação. Nos dias de sol e nos dias de chuva, Ele estava lá, cuidando de cada detalhe da nossa casa. Quando o coração apertou, Ele trouxe paz. Quando faltou força, Ele foi a minha força. Quando eu não entendia nada, Ele já sabia tudo. Por isso escrevo: não esqueça das bondades do Senhor. Elas se renovam a cada manhã, como o pão quentinho na mesa e as flores na janela. ";
const C = { fill1:"#7E2C38", fill2:"#8E3A44", traco:"#E7C3AE" };
const painel = rasgado(150, 318, 780, 720, 46, 30);
document.body.insertAdjacentHTML("beforeend", `
<div class="post" id="p1">
  <div class="carta">${(CARTA + CARTA + CARTA + CARTA).trim()}</div>
  <svg viewBox="0 0 1080 1350" width="1080" height="1350">${pinta(DEFS("p1", { trama:"#000" }), C)}
    <defs>
      <clipPath id="p1-corte"><polygon points="${painel}"/></clipPath>
      <filter id="p1-sombra" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="3" dy="10" stdDeviation="10" flood-color="#2a0f0a" flood-opacity=".35"/></filter>
      <filter id="p1-rasgo" x="-5%" y="-5%" width="110%" height="110%">
        <feTurbulence type="fractalNoise" baseFrequency=".08" numOctaves="2" seed="5" result="t"/>
        <feDisplacementMap in="SourceGraphic" in2="t" scale="8" xChannelSelector="R" yChannelSelector="G" result="d"/>
        <feDropShadow in="d" dx="2" dy="7" stdDeviation="7" flood-color="#2a0f0a" flood-opacity=".35"/>
      </filter>
      <filter id="p1-kraft" x="0" y="0" width="100%" height="100%">
        <feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="4" seed="11" result="n"/>
        <feColorMatrix in="n" type="matrix" values="0 0 0 0 .45  0 0 0 0 .33  0 0 0 0 .2  0 0 0 .3 0" result="m"/>
        <feComposite in="m" in2="SourceGraphic" operator="in"/>
      </filter>
    </defs>
    <g filter="url(#p1-sombra)"><polygon points="${painel}" fill="#F3E9DA" stroke="#F3E9DA" stroke-width="16" stroke-linejoin="round"/></g>
    <g clip-path="url(#p1-corte)">
      <rect x="140" y="300" width="800" height="760" fill="#6B1F2C"/>
      <g transform="scale(1.15)"><rect x="100" y="250" width="740" height="700" fill="url(#p1-papel)"/></g>
      <rect x="140" y="300" width="800" height="760" fill="#000" filter="url(#p1-kraft)" opacity=".6"/>
    </g>
  </svg>
  <img class="flor" src="gen/magnolia-recorte.png" style="left:-20px;top:-10px;width:1120px">
  <img class="flor" id="brancas" style="left:-10px;top:770px;width:360px;transform:rotate(-12deg)">
  <img class="flor" src="gen/tulipas-recorte.png" style="left:770px;top:300px;width:300px;transform:rotate(14deg)">
  <svg viewBox="0 0 1080 1350" width="1080" height="1350" style="pointer-events:none">
    <g transform="rotate(-3 540 680)"><rect x="258" y="566" width="564" height="228" fill="#E4D2B3" filter="url(#p1-rasgo)"/>
      <rect x="258" y="566" width="564" height="228" fill="#000" filter="url(#p1-kraft)" opacity=".7"/></g>
    <g transform="rotate(2 540 1270)"><rect x="352" y="1238" width="376" height="62" fill="#E4D2B3" filter="url(#p1-rasgo)"/></g>
  </svg>
  <div class="etiqueta" style="left:270px;width:540px;top:598px;font-family:'Apple';font-size:48px;line-height:1.5;transform:rotate(-3deg)">“Deus é bom o<br>tempo todo.”</div>
  <div class="etiqueta" style="left:352px;width:376px;top:1258px;font-family:'Caslon';font-size:16px;letter-spacing:.24em;transform:rotate(2deg)">@REBECAFORTUNATO__</div>
</div>`);
// Tulipas brancas: tira o fundo escuro da pintura e deixa só o buquê.
window.pronto = new Promise(res => {
  const im = new Image();
  im.onload = () => {
    const cv = document.createElement("canvas"); cv.width = im.width; cv.height = im.height;
    const cx = cv.getContext("2d"); cx.drawImage(im, 0, 0);
    const d = cx.getImageData(0, 0, cv.width, cv.height), p = d.data, br = p[0], bg = p[1], bb = p[2];
    let x0 = 1e9, y0 = 1e9, x1 = 0, y1 = 0;
    for (let i = 0; i < p.length; i += 4) {
      const dist = Math.abs(p[i] - br) + Math.abs(p[i + 1] - bg) + Math.abs(p[i + 2] - bb);
      const a = Math.max(0, Math.min(1, (dist - 22) / 40));
      p[i + 3] = Math.round(a * 255);
      if (a > .5) { const px = (i / 4) % cv.width, py = Math.floor(i / 4 / cv.width);
        if (px < x0) x0 = px; if (px > x1) x1 = px; if (py < y0) y0 = py; if (py > y1) y1 = py; }
    }
    cx.putImageData(d, 0, 0);
    const w = x1 - x0 + 16, h = y1 - y0 + 16, out = document.createElement("canvas"); out.width = w; out.height = h;
    out.getContext("2d").drawImage(cv, x0 - 8, y0 - 8, w, h, 0, 0, w, h);
    document.getElementById("brancas").src = out.toDataURL("image/png");
    res([w, h]);
  };
  im.src = "gen/tulipas-brancas-bordo.png";
});
</script>
</body></html>'''
open("bomtempo-flores.html", "w").write(html)
print("ok")
