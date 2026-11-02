# Monta a colagem "Coisas fofas de Natal" sobre as bases de tecido (achadinhos.html).
import re
src = open("achadinhos.html").read()
head, body = src.split("<body>", 1)
posts = re.findall(r'<div class="post" id="p\d">.*?(?=<div class="post" id="p\d">|</body>)', body, re.S)
R = "achadinhos/recortes/"
# (arquivo, centro x, centro y, largura, giro, espelhar)
ITENS = [
    ("03-guirlanda", 185, 215, 430, -4, False),
    ("08-globo", 540, 215, 255, 0, False),
    ("06-boleira", 860, 245, 440, 3, False),
    ("05-quebra-nozes", 135, 760, None, -3, False),   # altura fixa, ver abaixo
    ("02a-papai-noel", 850, 610, 185, -6, False),
    ("02b-rena", 985, 680, 190, 8, False),
    ("07-xicara", 555, 1095, 380, -2, False),
    ("04-toalha", 195, 1160, 420, -6, False),
    ("01-meia", 945, 1080, 320, 6, True),
]
from PIL import Image
def tag(nome, cx, cy, w, giro, esp):
    iw, ih = Image.open(R + nome + ".png").size
    if w is None:
        h = 680; w = round(h * iw / ih)
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
    out.append(p)
css = ".prod{position:absolute;filter:drop-shadow(0 6px 10px rgba(60,20,25,.18))}\n.titulo{z-index:2}\n.at{z-index:2}\n"
head = head.replace("</style>", css + "</style>")
open("achadinhos-natal.html", "w").write(head + "<body>" + "".join(out) + "</body></html>")
print("posts", len(out))
