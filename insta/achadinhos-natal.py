# Monta a colagem "Coisas fofas de Natal" sobre as bases de tecido (achadinhos.html).
import re
src = open("achadinhos.html").read()
head, body = src.split("<body>", 1)
posts = re.findall(r'<div class="post" id="p\d">.*?(?=<div class="post" id="p\d">|</body>)', body, re.S)
R = "achadinhos/recortes/"
# (arquivo, centro x, centro y, largura, giro, espelhar)
ITENS = [
    ("03-guirlanda", 185, 215, 430, -4, False),
    ("08-globo", 540, 200, 240, 0, False),
    ("06-boleira", 850, 240, 420, 3, False),
    ("05-quebra-nozes", 130, 700, None, -3, False),   # altura fixa, ver abaixo
    ("09-pratos-arvore", 930, 660, 335, 3, False),
    ("07-xicara", 560, 975, 330, -2, False),
    ("04-toalha", 200, 1165, 420, -6, False),
    ("10-canecas", 585, 1192, 320, 2, False),
    ("01-meia", 935, 1080, 285, 5, False),
]
from PIL import Image
def tag(nome, cx, cy, w, giro, esp):
    iw, ih = Image.open(R + nome + ".png").size
    if w is None:
        h = 600; w = round(h * iw / ih)
    else:
        h = round(w * ih / iw)
    t = f"rotate({giro}deg)" + (" scaleX(-1)" if esp else "")
    return (f'<img class="prod" src="{R}{nome}.png" style="left:{cx - w/2:.0f}px;top:{cy - h/2:.0f}px;'
            f'width:{w}px;height:{h}px;transform:{t}">')
imgs = "".join(tag(*i) for i in ITENS)
out = []
for i, p in enumerate(posts[:2]):
    p = re.sub(r'<div class="ph"[^>]*>[^<]*</div>', "", p)
    p = p.replace("Achadinhos de Natal que eu compraria pra minha casa", "Coisas fofas de Natal que eu compraria")
    p = p.replace('<div class="titulo"', imgs + '<div class="titulo"', 1)
    p = p.replace("padding:10px 22px", "padding:6px 15px").replace("top:430px", "top:392px").replace("top:450px", "top:410px")  # @ menorzinho, sem chamar atenção
    out.append(p)
css = ".prod{position:absolute;filter:drop-shadow(0 6px 10px rgba(60,20,25,.18))}\n.titulo{z-index:2}\n.at{z-index:2;font-size:14px !important;letter-spacing:.22em !important}\n"
head = head.replace("</style>", css + "</style>")
open("achadinhos-natal.html", "w").write(head + "<body>" + "".join(out) + "</body></html>")
print("posts", len(out))
