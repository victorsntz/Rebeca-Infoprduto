# -*- coding: utf-8 -*-
"""
Gera dist/de-tola-a-virtuosa.html (A5 paisagem, só frente) a partir de src/content.py,
e exporta site/app/content.json pra área de membros usar o mesmo conteúdo.
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
OUT_HTML = os.path.join(DIST, "de-tola-a-virtuosa.html")
OUT_JSON = os.path.join(ROOT, "site", "app", "content.json")

FLAME_HEART = (
    '<svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M12 22s-8-5.2-8-11.2A4.4 4.4 0 0 1 12 8.6a4.4 4.4 0 0 1 8 2.2C20 16.8 12 22 12 22z" fill="currentColor"/>'
    '<path d="M12 1.5c1.6 2 2.2 3.6 1.4 5.2-.4.8-1.2 1.3-1.2 2.3 0 .5.2.9.6 1.3-2-.4-3.2-1.7-3.2-3.5 0-2 1.4-3.2 2.4-5.3z" fill="#E8C27A"/>'
    '</svg>'
)


def e(s):
    return html.escape(str(s), quote=False)


def bloco_de(dia):
    for b in C.BLOCOS:
        if b["inicio"] <= dia <= b["fim"]:
            return b
    raise ValueError(dia)


def lines(n, cls=""):
    return f'<div class="lines {cls}">' + "<i></i>" * n + "</div>"


def lines_fill(cls=""):
    return f'<div class="lines fill {cls}">' + "<i></i>" * 30 + "</div>"


def field(label, n, hint="", cls=""):
    h = f' <span class="hint">{e(hint)}</span>' if hint else ""
    return f'<div class="field"><div class="label">{e(label)}{h}</div>{lines(n, cls)}</div>'


def fill_field(label, hint=""):
    h = f' <span class="hint">{e(hint)}</span>' if hint else ""
    return f'<div class="field grow"><div class="label">{e(label)}{h}</div>{lines_fill()}</div>'


def check(text):
    return f'<div class="check"><span class="box"></span><span>{e(text)}</span></div>'


def chips(items, cls=""):
    return '<div class="chips">' + "".join(f'<span class="chip {cls}">{e(i)}</span>' for i in items) + "</div>"


def verse_box(texto, ref, extra=""):
    return (f'<div class="verse-box {extra}"><p class="verse">“{e(texto)}”'
            f'<span class="verse-ref">{e(ref)}</span></p></div>')


def scale(n=11):
    return '<div class="scale">' + "".join(f'<span class="dot">{i}</span>' for i in range(n)) + "</div>"


def scale5():
    return '<span class="scale5">' + '<span class="dot"></span>' * 5 + "</span>"


pages = []


def page(inner, cls="", foot=True, section=""):
    pages.append({"cls": cls, "inner": inner, "foot": foot, "section": section})


def head(left, right=""):
    return f'<div class="head"><span class="tag">{left}</span><span class="tag">{right}</span></div>'


# ---------------------------------------------------------------------------
# Capa
# ---------------------------------------------------------------------------
DECO = '''<svg class="floral" viewBox="0 0 210 148" preserveAspectRatio="none" aria-hidden="true">
  <defs>
    <pattern id="fl" width="32" height="32" patternUnits="userSpaceOnUse" patternTransform="rotate(-8)"><g fill="none" stroke="#E8C27A" stroke-width="0.32" stroke-linecap="round" stroke-linejoin="round" opacity="0.28"><path d="M2 31 C 8 21, 14 18, 23 7"/><path d="M8 22 c 3 -4.5 6.5 -4.5 7.5 -1 c -3.5 3 -6.5 2.5 -7.5 1 z"/><path d="M14 15.5 c 4 -3 7 -2 7.5 1 c -4 2 -7 1 -7.5 -1 z"/><path d="M11 18 c -4.5 -1 -6.5 -4.5 -4.5 -7 c 3 1.5 5 4 4.5 7 z"/><path d="M5 27 c -3.5 -0.5 -5 -3 -3.5 -5 c 2.5 1 3.8 3 3.5 5 z"/><g transform="translate(25.5 5) scale(1)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><g transform="translate(28 25) scale(0.75)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><path d="M28 25 c -2 3 -6 4 -9 3"/><path d="M21 27.5 c 1.5 -2.5 4.5 -2.5 5.5 -0.5 c -2.5 2 -5 1.5 -5.5 0.5 z"/><circle cx="18" cy="30" r="0.7" fill="#E8C27A" stroke="none"/><circle cx="16.3" cy="28.6" r="0.6" fill="#E8C27A" stroke="none"/><circle cx="19.6" cy="28.4" r="0.55" fill="#E8C27A" stroke="none"/></g></pattern>
    <radialGradient id="vig" cx="50%" cy="52%" r="46%"><stop offset="0" stop-color="#5E1A26" stop-opacity="0.96"/><stop offset="0.7" stop-color="#5E1A26" stop-opacity="0.8"/><stop offset="1" stop-color="#5E1A26" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="210" height="148" fill="url(#fl)"/>
  <rect width="210" height="148" fill="url(#vig)"/>
</svg>
<svg class="spray tl" viewBox="0 0 60 60" aria-hidden="true"><g fill="none" stroke="#E8C27A" stroke-width="0.7" stroke-linecap="round" stroke-linejoin="round" opacity="0.85"><path d="M4 58 C 14 40, 22 30, 44 10"/><path d="M24 30 C 30 32, 38 30, 46 34"/><path d="M15 43 C 8 42, 4 38, 2 32"/><path d="M12 46 c 4 -7 10 -7 12 -2 c -5 5 -10 4 -12 2 z"/><path d="M20 36 c 6 -4 11 -2 11 2 c -6 3 -10 1 -11 -2 z"/><path d="M17 40 c -7 -1 -10 -6 -8 -10 c 5 2 8 6 8 10 z"/><path d="M30 24 c 6 -5 12 -3 12 1 c -6 4 -11 2 -12 -1 z"/><path d="M27 27 c -6 -3 -8 -9 -5 -12 c 4 3 6 8 5 12 z"/><path d="M38 17 c -4 -5 -3 -11 1 -12 c 2 5 1 9 -1 12 z"/><g transform="translate(47 8) scale(1.9)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><g transform="translate(48 35) scale(1.4)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><g transform="translate(3 31) scale(1.1)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><circle cx="34" cy="21" r="1" fill="#E8C27A" stroke="none"/><circle cx="36.5" cy="23.5" r="0.8" fill="#E8C27A" stroke="none"/><circle cx="10" cy="52" r="0.9" fill="#E8C27A" stroke="none"/></g></svg>
<svg class="spray br" viewBox="0 0 60 60" aria-hidden="true"><g fill="none" stroke="#E8C27A" stroke-width="0.7" stroke-linecap="round" stroke-linejoin="round" opacity="0.85"><path d="M4 58 C 14 40, 22 30, 44 10"/><path d="M24 30 C 30 32, 38 30, 46 34"/><path d="M15 43 C 8 42, 4 38, 2 32"/><path d="M12 46 c 4 -7 10 -7 12 -2 c -5 5 -10 4 -12 2 z"/><path d="M20 36 c 6 -4 11 -2 11 2 c -6 3 -10 1 -11 -2 z"/><path d="M17 40 c -7 -1 -10 -6 -8 -10 c 5 2 8 6 8 10 z"/><path d="M30 24 c 6 -5 12 -3 12 1 c -6 4 -11 2 -12 -1 z"/><path d="M27 27 c -6 -3 -8 -9 -5 -12 c 4 3 6 8 5 12 z"/><path d="M38 17 c -4 -5 -3 -11 1 -12 c 2 5 1 9 -1 12 z"/><g transform="translate(47 8) scale(1.9)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><g transform="translate(48 35) scale(1.4)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><g transform="translate(3 31) scale(1.1)"><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(0)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(72)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(144)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(216)"/><ellipse rx="1.6" ry="2.8" cy="-3" transform="rotate(288)"/><circle r="0.9" fill="#E8C27A" stroke="none"/></g><circle cx="34" cy="21" r="1" fill="#E8C27A" stroke="none"/><circle cx="36.5" cy="23.5" r="0.8" fill="#E8C27A" stroke="none"/><circle cx="10" cy="52" r="0.9" fill="#E8C27A" stroke="none"/></g></svg>'''
page(f'''
{DECO}
<div class="frame"></div>
<div class="cv-top">
  <div class="kicker">Caderno prático</div>
  <div class="kicker sub">Corpo · alma · espírito</div>
</div>
<div class="cv-mid">
  <h1><span class="l1">De Tola</span><span class="l2">a <em>Virtuosa</em></span></h1>
  <div class="orn"><span class="ln"></span>{FLAME_HEART}<span class="ln"></span></div>
  <p class="sub">{e(C.SUBTITULO)}</p>
  <div class="tag">Quatro provas de dez dias</div>
</div>
<div class="cv-bot">
  <p class="verse">“{e(C.VERSICULO_CAPA["texto"])}”<span class="verse-ref">{e(C.VERSICULO_CAPA["ref"])}</span></p>
  <div class="autora">por {e(C.AUTORA)}</div>
</div>
''', cls="cover", foot=False)

# Este caderno é de + compromisso -------------------------------------------
page(f'''
{head("Antes de tudo")}
<div class="split even">
  <div class="l owner">
    <div class="eyebrow">Este caderno é de</div>
    <div class="line" style="height:10mm"></div>
    <div class="cols" style="margin-top:5mm">
      <div><div class="line"></div><div class="lbl">Data do dia 1</div></div>
      <div><div class="line"></div><div class="lbl">Data do dia 40</div></div>
    </div>
    <div style="margin-top:5mm"><div class="eyebrow">Meu porquê, em uma frase</div>{lines(3)}</div>
    <div style="margin-top:4mm">
      <div class="eyebrow">Onde eu estou hoje</div>
      <div class="chips">{"".join(f'<span class="chip">{x}</span>' for x in ["Solteira","Namorando","Noiva","Casada","Mãe"])}</div>
      <p class="tiny muted" style="margin-top:1.5mm">Cada fase tem seus desafios. O chamado é o mesmo. Marque a sua e adapte os desafios à sua vida.</p>
    </div>
  </div>
  <div class="r">
    <div class="compromisso">
      <div class="eyebrow">Meu compromisso</div>
      <p style="font-size:8pt;line-height:1.45">Eu, <span style="display:inline-block;border-bottom:0.25mm solid var(--carvao);width:52mm"></span>, decido atravessar estes 40 dias com honestidade, sem perfeição e sem desistir. Quando falhar, viro a página. Quando acertar, agradeço a Deus.</p>
      <div class="sig"><div>Assinatura</div><div class="short">Data</div></div>
    </div>
    <div style="margin-top:auto">{verse_box("Ensina-nos a contar os nossos dias, de tal maneira que alcancemos corações sábios.", "Salmo 90:12", "center")}</div>
  </div>
</div>
''', section="Início")

# Carta ---------------------------------------------------------------------
cw = C.CARTA
half = (len(cw["paragrafos"]) + 1) // 2
page(f'''
{head("Carta de boas-vindas")}
<h1>{e(cw["titulo"])}</h1>
<div class="cols" style="font-size:9.4pt;line-height:1.55;margin-top:2mm">
  <div>{"".join(f"<p>{e(p)}</p>" for p in cw["paragrafos"][:half])}</div>
  <div>{"".join(f"<p>{e(p)}</p>" for p in cw["paragrafos"][half:])}
    <p class="serif" style="font-size:12pt;font-style:italic;color:var(--rubi);margin-top:2mm">{e(cw["assinatura"])}</p>
    <div class="assin"><span class="nome">{e(C.AUTORA)}</span><span class="fh" style="color:var(--rubi)">{FLAME_HEART}</span><span class="cargo">Autora de De Tola a Virtuosa</span></div></div>
</div>
''', section="Início")

# Como usar -----------------------------------------------------------------
cu = C.COMO_USAR
page(f'''
{head("Regras do jogo")}
<h1>{e(cu["titulo"])}</h1>
<div class="split even">
  <div class="l"><ol class="steps">{"".join(f"<li><div><b>{e(t)}</b><span>{e(d)}</span></div></li>" for t, d in cu["regras"])}</ol></div>
  <div class="r rituais">
    <div><div class="eyebrow">Ritual da manhã · 5 minutos</div><ol>{"".join(f"<li>{e(x)}</li>" for x in cu["manha"])}</ol></div>
    <div style="margin-top:3mm"><div class="eyebrow">Ritual da noite · 1 minuto pra marcar, 3 se quiser escrever</div><ol>{"".join(f"<li>{e(x)}</li>" for x in cu["noite"])}</ol></div>
    <div class="card fill c-dourado" style="margin-top:auto">
      <div class="eyebrow" style="color:var(--dourado)">A prova de Daniel</div>
      <p style="font-size:7.2pt;margin:0">Daniel pediu dez dias pra provar que obedecer a Deus funciona (Daniel 1:12). Aqui são quatro provas de dez. Cada uma tem um lugar da travessia, uma virtude e uma mulher da Bíblia que já passou por ali.</p>
    </div>
  </div>
</div>
''', section="Início")

# Tola ou virtuosa ----------------------------------------------------------
tv = C.TOLA_VIRTUOSA
page(f'''
{head("Diagnóstico")}
<div class="split even">
  <div class="l">
    <h1>{e(tv["titulo"])}</h1>
    {verse_box(tv["versiculo"], tv["ref"])}
    <p style="font-size:9pt;line-height:1.5">{e(tv["intro"])}</p>
    <div style="margin-top:auto">{field(tv["pergunta"], 3)}</div>
  </div>
  <div class="r">
    <table class="contrast">
    <tr><th>A tola</th><th class="v">A virtuosa</th></tr>
    {"".join(f'<tr><td class="t">{e(a)}</td><td class="v">{e(b)}</td></tr>' for a, b in tv["contrastes"])}
    </table>
  </div>
</div>
''', cls="c-rubi", section="Início")

# Identidade ----------------------------------------------------------------
idn = C.IDENTIDADE
page(f'''
{head("Identidade")}
<div class="split even">
  <div class="l">
    <h1>{e(idn["titulo"])}</h1>
    <p style="font-size:9pt;line-height:1.5">{e(idn["intro"])}</p>
    <div class="idgrid">{"".join(f'<div class="id"><b>{e(t)}</b><span>“{e(v)}”</span><i>{e(r)}</i></div>' for t, v, r in idn["versiculos"])}</div>
  </div>
  <div class="r">
    <div class="field"><div class="q">{e(idn["pergunta1"])}</div>{lines(7)}</div>
    <div class="field grow"><div class="q">{e(idn["pergunta2"])}</div>{lines_fill()}</div>
  </div>
</div>
''', cls="c-rubi", section="Início")

# Corpo, alma e espírito ----------------------------------------------------
cae = C.CORPO_ALMA_ESPIRITO
pil = "".join(f'''<div class="pilar c-{cor}">
  <div class="band"><span class="n">{i+1}</span><span class="nm">{e(n)}</span></div>
  <p class="fr">{e(fr)}</p>
  <div class="itens">{"".join(f'<span class="chip">{e(x.strip())}</span>' for x in it.split("·"))}</div>
  <p class="verse">“{e(v)}”<span class="verse-ref">{e(r)}</span></p></div>''' for i, (n, cor, fr, it, v, r) in enumerate(cae["pilares"]))
virt = "".join(f'<div class="vi"><b>{e(n)}</b><span>{e(d)}</span><i>{e(r)}</i></div>' for n, d, r in cae["virtudes"])
page(f'''
{head("Tudo está ligado")}
<div class="cae-top">
  <div><h1>{e(cae["titulo"])}</h1><p style="font-size:9pt;line-height:1.5;margin:0">{e(cae["intro"])}</p></div>
  <div>{verse_box(cae["versiculo"], cae["ref"])}</div>
</div>
<div class="pilares">{pil}</div>
<div class="virtudes"><div class="eyebrow" style="margin:0">{e(cae["virtudes_titulo"])}</div>{virt}</div>
''', cls="c-rubi", section="Início")

# Propósito e limites -------------------------------------------------------
pl = C.PROPOSITO_LIMITES
lim = ""
for a in pl["lim_areas"]:
    lim += f'<div style="margin-bottom:1.5mm"><div class="label">{e(a)}</div><div class="cols tight">' + "".join(
        f'<div><span class="tiny muted">{e(c)}</span>{lines(3, "tight")}</div>' for c in pl["lim_cols"]) + "</div></div>"
page(f'''
{head("Antes que a situação apareça")}
<div class="split even">
  <div class="l">
    <h1>Propósito</h1>
    <p style="font-size:7.4pt">{e(pl["prop_intro"])}</p>
    {"".join(f'<div class="field"><div class="q" style="font-size:8.6pt">{e(q)}</div>{lines(4, "tight")}</div>' for q in pl["prop_perguntas"])}
  </div>
  <div class="r">
    <h1>Limites</h1>
    <p style="font-size:7.4pt">{e(pl["lim_intro"])} <i class="serif" style="font-size:8.4pt;color:var(--rubi)">“{e(pl["lim_versiculo"])}” <span class="tiny muted" style="font-style:normal">{e(pl["lim_ref"])}</span></i></p>
    {lim}
  </div>
</div>
<div class="card fill c-dourado" style="margin-top:3mm"><div class="label">{e(pl["prop_frase"])}</div>{lines(2, "tight")}</div>
''', cls="c-rubi", section="Início")

# Regras -------------------------------------------------------------------
rs = C.REGRAS_SONHOS
page(f'''
{head("Inegociáveis")}
<div class="split even">
  <div class="l">
    <h1>As regras</h1>
    <p style="font-size:9pt;line-height:1.5">{e(rs["regras_intro"])}</p>
    <ul class="rules">{"".join(f'<li><span class="box"></span><span>{e(r)}</span></li>' for r in rs["regras"])}</ul>
  </div>
  <div class="r">
    <div class="field grow"><div class="label">Minhas regras <span class="hint">as que eu não negocio por 40 dias</span></div>{lines_fill()}</div>
  </div>
</div>
''', cls="c-rubi", section="Início")

# Quadro dos sonhos (moodboard) ---------------------------------------------
frames = "".join(f'''<div class="mb-col c-{cor}">
  <div class="frame-img"><span class="tape"></span><span class="hint">cole aqui uma imagem</span></div>
  <div class="mb-label">{e(n)}</div>
  <div class="label">Meta que dá pra medir</div>{lines(2, "tight")}
  <div class="label" style="margin-top:1mm">Como vou saber que cheguei</div>{lines(1, "tight")}
</div>''' for n, cor in rs["areas"])
page(f'''
{head("Escreve a visão", "Habacuque 2:2")}
<div class="mb-head">
  <div><h1>Quadro dos sonhos</h1><p style="font-size:8.6pt;line-height:1.45;margin:0">Cole fotos, recortes, palavras, cores. Um moodboard de 40 dias: só cabe aqui o que dá pra medir e cabe em 40 dias. {e(rs["sonhos_intro"].split(". ",1)[1] if ". " in rs["sonhos_intro"] else "")}</p></div>
  <div class="frame-img wide"><span class="tape"></span><span class="hint">a imagem que resume a mulher que eu quero ser no dia 40</span></div>
</div>
<div class="mb-grid">{frames}</div>
<div class="mb-frase"><span class="label" style="margin:0;white-space:nowrap">Minha frase de 40 dias</span>{lines(1, "tight")}</div>
''', cls="c-rubi", section="Início")

# Carta pro futuro ----------------------------------------------------------
cf = C.CARTA_FUTURO
page(f'''
{head("Só abrir no dia 40")}
<div class="split even">
  <div class="l" style="flex:0 0 55mm">
    <h1>{e(cf["titulo"])}</h1>
    <p class="small muted">{e(cf["intro"])}</p>
    <p class="serif" style="font-size:10pt;font-style:italic;margin-top:auto">{e(cf["cabecalho"])}</p>
  </div>
  <div class="r">{lines_fill()}</div>
</div>
<p class="tiny muted" style="margin:1.5mm 0 0;text-align:right">{e(cf["rodape"])}</p>
<div class="corner"></div>
''', cls="c-rubi", section="Início")

# Retrato -------------------------------------------------------------------
rt = C.RETRATO
def retrato(dia40=False):
    if dia40:
        rows = "".join(f'<div class="retrato-row cmp"><span class="nm">{e(a)}</span><span class="lbl">Dia 1</span>{scale()}<span class="lbl">Dia 40</span>{scale()}</div>' for a in rt["areas"])
        return f'''
{head("Foto honesta", "Dia 40")}
<h1>{e(rt["titulo_40"])}</h1>
<p class="small muted" style="font-size:8pt">{e(rt["intro_40"])}</p>
<div class="label">De 0 a 10, como está cada área</div>
{rows}
<div class="cols" style="margin-top:3mm">
  {field(rt["mudou_40"], 3, cls="tight")}
  {field(rt["deus_40"], 3, cls="tight")}
  {field("Oração de chegada", 3, "o que eu quero dizer a Deus ao terminar", "tight")}
</div>
'''
    rows = "".join(f'<div class="retrato-row"><span class="nm">{e(a)}</span>{scale()}</div>' for a in rt["areas"])
    right = (f'{field(rt["palavras_1"], 2, cls="tight")}{field(rt["incomodo_1"], 3, cls="tight")}'
             + fill_field("Oração de partida", "o que eu quero pedir a Deus antes do dia 1"))
    return f'''
{head("Foto honesta", "Dia 1")}
<h1>{e(rt["titulo_1"])}</h1>
<p class="small muted" style="font-size:8pt">{e(rt["intro_1"])}</p>
<div class="split">
  <div class="l" style="flex:0 0 104mm"><div class="label">De 0 a 10, como está cada área</div>{rows}</div>
  <div class="r">{right}</div>
</div>
'''

page(retrato(False), cls="c-rubi", section="Início")

# A travessia (mapa) --------------------------------------------------------
mp = C.MAPA
cards = "".join(f'''<div class="m" style="background:var(--{b["cor"]})">
  <div class="eyebrow">Prova {b["num"]} · dias {b["inicio"]} a {b["fim"]}</div>
  <h3>{e(b["lugar"])}</h3>
  <div class="v">{e(b["virtude"])}</div>
  <div class="w">{e(b["chamada"])}. Com {e(b["mulher"])}.</div>
  <div class="dt">Início ___/___ &nbsp; Fim ___/___</div>
  <div class="box"></div></div>''' for b in C.BLOCOS)
page(f'''
{head("Visão geral")}
<h1>{e(mp["titulo"])}</h1>
<p class="small muted">{e(mp["intro"])}</p>
<div class="map">{cards}</div>
<div style="margin-top:3mm">{field("Uma pessoa a quem vou prestar contas nesses 40 dias", 1, "amiga, irmã, discipuladora, marido")}</div>
''', section="Início")


# ---------------------------------------------------------------------------
# Provas
# ---------------------------------------------------------------------------
def tracker(b):
    dias = list(range(b["inicio"], b["fim"] + 1))
    ths = "".join(f"<th>{d}</th>" for d in dias)
    rows = "".join(f'<tr><th class="h">{e(h)}</th>{"<td></td>" * len(dias)}</tr>' for h in C.TRACKER_HABITOS)
    return f'<table class="tracker"><thead><tr><th class="h">Hábito / dia</th>{ths}</tr></thead><tbody>{rows}</tbody></table>'


def prova_open(b):
    sec = f"Prova {b['num']} · {b['lugar']}"
    metas = "".join(f'<div class="p-{k}"><div class="eyebrow">{"Espírito" if k == "espirito" else k.capitalize()}</div>{e(v)}</div>' for k, v in b["metas"].items())
    page(f'''
<div class="num">{b["num"]:02d}</div>
<div class="split even">
  <div class="l">
    <div class="eyebrow">Prova {b["num"]} de 4 · dias {b["inicio"]} a {b["fim"]} · {e(b["chamada"])}</div>
    <div class="big">{e(b["lugar"])}</div>
    <div class="virt">{e(b["virtude"])} · {e(b["sub"])}</div>
    {verse_box(b["versiculo_lugar"], b["ref_lugar"])}
    <div class="woman"><b>{e(b["mulher"])}</b><span>{e(b["mulher_desc"])}</span><i>{e(b["mulher_ref"])}</i></div>
  </div>
  <div class="r">
    <p style="margin-top:3mm">{e(b["resumo"])}</p>
    <p>{e(b["definicao"])}</p>
    {verse_box(b["versiculo"], b["ref"])}
    <div class="tv"><div class="t"><span class="who">A tola</span>{e(b["tola"])}</div><div class="v"><span class="who">A virtuosa</span>{e(b["virtuosa"])}</div></div>
    <div class="eyebrow" style="margin-top:auto">Metas destes 10 dias</div>
    <div class="metas light">{metas}</div>
  </div>
</div>
''', cls=f"prova-open c-{b['cor']}", section=sec)
    page(f'''
{head(sec, f"dias {b['inicio']} a {b['fim']}")}
<div class="split">
  <div class="l" style="flex:0 0 118mm">
    <h2>Tracker da prova {b["num"]}</h2>
    <p class="small muted" style="margin-bottom:1.5mm">Pinte o quadradinho no fim do dia. Dez dias de uma vez mostram o padrão que o dia a dia esconde.</p>
    {tracker(b)}
    <div class="cols" style="margin-top:2.5mm">
      {field("O hábito que mais falhou", 1, cls="tight")}
      {field("O hábito que virou automático", 1, cls="tight")}
    </div>
  </div>
  <div class="r">
    {field("Minha meta pessoal desta prova", 2, "uma só, mensurável", "tight")}
    {field("Uma pessoa que quero abençoar nesses dias", 1, cls="tight")}
    {fill_field("Notas da prova", "o que eu percebi no caminho")}
  </div>
</div>
''', cls=f"c-{b['cor']}", section=sec)


def day_page(d):
    b = bloco_de(d)
    sec = f"Prova {b['num']} · {b['lugar']}"
    pil = "".join(f'<div class="p-{k}"><div class="eyebrow">{"Espírito" if k == "espirito" else k.capitalize()}</div>{"".join(check(x) for x in v)}</div>' for k, v in C.CHECKLIST.items())
    page(f'''
<div class="head">
  <div class="daynum"><small>Dia</small>{d:02d}<small style="margin-left:3mm">de 40</small></div>
  <div class="meta"><div class="virt">{e(b["virtude"])} · {e(b["lugar"])}</div><span class="tag">Prova {b["num"]} · {e(b["chamada"])}</span></div>
</div>
<div class="split">
  <div class="l">
    <div class="box reading"><div class="eyebrow">Leitura de hoje</div><div class="txt">{e(C.LEITURAS[d-1])}</div></div>
    <div class="box ch"><div class="eyebrow">Desafio do dia</div><div class="txt">{e(C.DESAFIOS[d-1])}</div></div>
    <div class="pillars">{pil}</div>
    <p class="verse lverse">“{e(b["versiculo"])}”<span class="verse-ref">{e(b["ref"])}</span></p>
  </div>
  <div class="r">
    <div class="row" style="display:flex;justify-content:space-between;align-items:baseline"><div class="label" style="margin:0">Hoje</div><div class="date">Data <span></span>/<span></span>/<span></span></div></div>
    <div class="row"><div class="label">Hoje eu me senti <span class="hint">circule</span></div>{chips(C.SENTI)}</div>
    <div class="row"><div class="label">O que pesou hoje <span class="hint">marque</span></div>{chips(C.PESOU, "soft")}</div>
    <div class="row" style="display:flex;align-items:center;gap:2.5mm"><div class="label" style="margin:0">{e(b["virtude"])} hoje</div>{chips(C.VIRTUDE_OPCOES, "acc")}</div>
    <div class="row"><div class="label">Sou grata por</div>{lines(2, "tight")}</div>
    <div class="row"><div class="label">Minha maior dificuldade hoje <span class="hint">e o que ela me mostrou</span></div>{lines(4, "tight")}</div>
    <div class="row"><div class="label">Uma linha pra Deus</div>{lines(1, "tight")}</div>
    <div class="row"><div class="label">Amanhã eu vou <span class="hint">uma coisa só</span></div>{lines(1, "tight")}</div>
    <div class="bottom">
      <div class="grp">Energia {scale5()}</div>
      <div class="grp"><span class="progress"><i style="width:{d * 2.5}%"></i></span></div>
      <div class="skip"><span class="box"></span> Pulei</div>
    </div>
  </div>
</div>
''', cls=f"day c-{b['cor']}", section=sec)


def prova_review(b):
    rv = C.REVISAO
    sec = f"Prova {b['num']} · {b['lugar']}"
    notas = "".join(f'<div><div class="label">{e(n)}</div>{scale5()}</div>' for n in rv["notas"])
    page(f'''
{head(sec, f"dias {b['inicio']} a {b['fim']}")}
<div class="split even">
  <div class="l" style="flex:0 0 60mm">
    <h1>{e(rv["titulo"])} {b["num"]}</h1>
    <div class="label">Dias completos</div><div class="serif" style="font-size:18pt;margin-bottom:2mm">____ / 10</div>
    <div class="label">Cumpri a meta pessoal?</div><div class="chips" style="margin-bottom:3mm">{"".join(f'<span class="chip">{x}</span>' for x in ["Sim","Em parte","Não"])}</div>
    <div class="label">Nota de 1 a 5</div>
    <div class="notas">{notas}</div>
    <div class="card fill" style="margin-top:auto"><div class="eyebrow" style="color:var(--accent)">{e(b["mulher"])} diria</div><p class="serif" style="font-size:8.6pt;font-style:italic;margin:0">{e(b["virtuosa"].capitalize())}</p></div>
  </div>
  <div class="r">{"".join(field(q, n, cls="tight") for q, n in rv["perguntas"])}</div>
</div>
''', cls=f"c-{b['cor']}", section=sec)


for b in C.BLOCOS:
    prova_open(b)
    for d in range(b["inicio"], b["fim"] + 1):
        day_page(d)
    prova_review(b)

# ---------------------------------------------------------------------------
# Fechamento
# ---------------------------------------------------------------------------
page(retrato(True), cls="c-ameixa", section="Fechamento")

fc = C.FECHAMENTO
page(f'''
{head("Dia 40")}
<div class="split even">
  <div class="l">
    <h1>{e(fc["titulo"])}</h1>
    {verse_box(fc["versiculo"], fc["ref"])}
    <div style="font-size:7.6pt">{"".join(f"<p>{e(p)}</p>" for p in fc["paragrafos"])}</div>
    <p class="serif" style="font-size:9.5pt;font-style:italic;color:var(--rubi);margin-top:auto">{e(fc["comunidade"])}</p>
  </div>
  <div class="r">
    <div class="card accent c-ameixa" style="flex:1;display:flex;flex-direction:column">
      <div class="eyebrow" style="color:var(--ameixa)">Minha próxima travessia começa em ___/___/______</div>
      {"".join(field(q, 2, cls="tight") for q in fc["proximos"])}
    </div>
  </div>
</div>
''', cls="c-ameixa", section="Fechamento")

page(f'''
{head("Notas livres")}
<h2>O que não coube nas outras páginas</h2>
{lines_fill()}
''', section="Fechamento")

cc = C.CONTRACAPA
page(f'''
<p class="frase">“{e(cc["frase"])}”</p>
<div class="autora">{FLAME_HEART}<span>{e(C.AUTORA)}</span></div>
<p class="verse">“{e(cc["versiculo"])}”<span class="verse-ref">{e(cc["ref"])}</span></p>
<div class="brand">De Tola a Virtuosa<small>40 dias no deserto · corpo, alma e espírito</small></div>
''', cls="back", foot=False)

# ---------------------------------------------------------------------------
# Montagem
# ---------------------------------------------------------------------------
out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
       f'<title>{e(C.TITULO)}: {e(C.SUBTITULO)}</title>',
       '<link rel="stylesheet" href="../src/styles.css">', '</head><body>']
for i, p in enumerate(pages, start=1):
    foot = ""
    if p["foot"]:
        fh_icon = FLAME_HEART.replace("<svg", '<svg class="fh" style="color:var(--rubi)"', 1)
        foot = (f'<div class="foot"><span>{fh_icon}{e(C.FOOT)}</span>'
                f'<span class="stripe"></span><span>{e(p["section"])}</span><span class="stripe"></span><span class="num">{i}</span></div>')
    out.append(f'<section class="page {p["cls"]}">{p["inner"]}{foot}</section>')
out.append('</body></html>')

os.makedirs(DIST, exist_ok=True)
with open(OUT_HTML, "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print(f"{len(pages)} páginas -> {OUT_HTML}")

# Exporta o conteúdo pra área de membros -------------------------------------
data = {
    "titulo": C.TITULO, "subtitulo": C.SUBTITULO, "tagline": C.TAGLINE, "autora": C.AUTORA,
    "versiculo_capa": C.VERSICULO_CAPA, "contracapa": C.CONTRACAPA,
    "blocos": C.BLOCOS, "desafios": C.DESAFIOS, "leituras": C.LEITURAS,
    "checklist": C.CHECKLIST, "senti": C.SENTI, "pesou": C.PESOU, "virtude_opcoes": C.VIRTUDE_OPCOES,
    "carta": C.CARTA, "como_usar": C.COMO_USAR, "tola_virtuosa": C.TOLA_VIRTUOSA,
    "identidade": C.IDENTIDADE, "corpo_alma_espirito": C.CORPO_ALMA_ESPIRITO,
    "proposito_limites": C.PROPOSITO_LIMITES, "regras_sonhos": C.REGRAS_SONHOS,
    "carta_futuro": C.CARTA_FUTURO, "retrato": C.RETRATO, "mapa": C.MAPA,
    "tracker_habitos": C.TRACKER_HABITOS, "revisao": C.REVISAO, "fechamento": C.FECHAMENTO,
}
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)
with open(OUT_JSON.replace(".json", ".js"), "w", encoding="utf-8") as fh:
    fh.write("// Gerado por src/build.py. Mesmo conteúdo do caderno impresso.\nwindow.DTV_CONTENT = " + json.dumps(data, ensure_ascii=False) + ";\n")
print(f"conteúdo -> {OUT_JSON} (+ content.js)")
