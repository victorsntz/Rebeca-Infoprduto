# Gera banner.html: capa do canal do YouTube (2560x1440) com o nome da Rebeca.
# Reaproveita o papel de parede jacobino de sola.html.
s = open("sola.html").read()
defs = s[s.index("const DEFS = (id,c) => `"):]
defs = defs[:defs.index("`;") + 2]
html = r'''<!doctype html><html><head><meta charset="utf-8">
<style>
@font-face{font-family:"GreatVibes";src:url("fonts/great-vibes.ttf")}
@font-face{font-family:"Playfair";src:url("fonts/playfair-regular.ttf")}
body{margin:0;background:#333}
.capa{width:2560px;height:1440px;position:relative;overflow:hidden;margin:0 0 20px}
.capa svg{position:absolute;inset:0}
.nome{position:absolute;left:0;right:0;top:556px;text-align:center}
.nome .r{display:block;font-family:"GreatVibes";font-size:252px;line-height:1}
.nome .f{display:inline-flex;align-items:center;gap:44px;margin-top:6px;font-family:"Playfair";font-size:60px;letter-spacing:.46em;padding-left:.46em}
.nome .f i{display:block;width:150px;height:2px}
.guia{position:absolute;border:3px dashed rgba(255,255,255,.85);font:600 30px sans-serif;color:#fff;padding:8px 14px;box-sizing:border-box}
</style></head><body>
<script>
''' + defs + r'''
const V = [
  { id:"b1", fundo:"#5E1A26", padrao:0, traco:"#000", fill1:"#000", fill2:"#000", script:"#F4E8DA", caps:"#D9B98A", linha:"#B8975B", luz:"rgba(255,226,205,.13)", sombra:"rgba(25,4,9,.55)" },
  { id:"b2", fundo:"#F3E9DF", padrao:0, traco:"#000", fill1:"#000", fill2:"#000", script:"#5E1A26", caps:"#8E2A3A", linha:"#B8975B", luz:"rgba(255,250,244,.7)", sombra:"rgba(120,70,60,.16)" },
];
// Cor direto nos desenhos (as cópias do padrão não herdam o CSS da página com segurança).
function pinta(d, c){
  return d.replace(/class="f1"/g, `fill="${c.fill1}" stroke="${c.traco}" stroke-width="1.4"`)
          .replace(/class="f2"/g, `fill="${c.fill2}" stroke="${c.traco}" stroke-width="1.4"`)
          .replace(/class="ln"/g, `fill="none" stroke="${c.traco}" stroke-width="1.2" stroke-linecap="round"`)
          .replace(/class="vn"/g, `fill="none" stroke="${c.traco}" stroke-width="1.8" stroke-linecap="round"`)
          .replace(/class="dt"/g, `fill="${c.traco}"`);
}
function capa(c){
  return `<div class="capa" id="${c.id}" style="background:${c.fundo}">
  <svg viewBox="0 0 2560 1440" width="2560" height="1440">${pinta(DEFS(c.id,{trama:c.linha}), c)}
    <style>
      #${c.id} .f1{fill:${c.fill1};stroke:${c.traco};stroke-width:1.4}
      #${c.id} .f2{fill:${c.fill2};stroke:${c.traco};stroke-width:1.4}
      #${c.id} .ln{fill:none;stroke:${c.traco};stroke-width:1.2;stroke-linecap:round}
      #${c.id} .vn{fill:none;stroke:${c.traco};stroke-width:1.8;stroke-linecap:round}
      #${c.id} .dt{fill:${c.traco}}
    </style>
    <defs>
      <radialGradient id="${c.id}-luz" cx="50%" cy="50%" r="42%"><stop offset="0" stop-color="${c.luz}"/><stop offset="1" stop-color="${c.luz}" stop-opacity="0"/></radialGradient>
      <radialGradient id="${c.id}-vinheta" cx="50%" cy="50%" r="75%"><stop offset=".55" stop-color="${c.sombra}" stop-opacity="0"/><stop offset="1" stop-color="${c.sombra}"/></radialGradient>
    </defs>
    <g opacity="${c.padrao}" transform="scale(1.6)"><rect x="-60" y="-60" width="1700" height="1000" fill="url(#${c.id}-papel)"/></g>
    <rect width="2560" height="1440" fill="url(#${c.id}-luz)"/>
    <rect width="2560" height="1440" fill="url(#${c.id}-vinheta)"/>
    <rect width="2560" height="1440" filter="url(#${c.id}-grao)"/>
  </svg>
  <div class="nome"><span class="r" style="color:${c.script}">Rebeca</span><span class="f" style="color:${c.caps}"><i style="background:${c.linha}"></i>FORTUNATO<i style="background:${c.linha}"></i></span></div>
</div>`;
}
document.body.insertAdjacentHTML("beforeend", V.map(capa).join(""));
// Guias de corte (só na prévia): TV = tudo; computador = faixa do meio; celular = miolo seguro.
if (location.search === "?guias") document.querySelectorAll(".capa").forEach(el => el.insertAdjacentHTML("beforeend",
  `<div class="guia" style="left:0;right:0;top:508px;height:424px">computador</div>
   <div class="guia" style="left:507px;width:1546px;top:508px;height:424px;border-color:#ffd27a;color:#ffd27a;text-align:right">celular (área segura)</div>
   <div class="guia" style="left:0;top:0;border:none">TV mostra a capa inteira</div>`));
</script>
</body></html>'''
# o grão vem do sola: garante que o filtro exista com esse nome
open("banner.html", "w").write(html)
print("ok")
