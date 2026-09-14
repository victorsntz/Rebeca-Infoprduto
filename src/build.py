# -*- coding: utf-8 -*-
"""
Gera dist/de-tola-a-virtuosa.html a partir de src/content.py.
Depois, o Chromium imprime esse HTML em PDF (ver Makefile / README).
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
OUT_HTML = os.path.join(DIST, "de-tola-a-virtuosa.html")

FOOT_BRAND = "De Tola a Virtuosa"


def e(s):
    return html.escape(str(s), quote=False)


def fase_de(dia):
    for f in C.FASES:
        if f["inicio"] <= dia <= f["fim"]:
            return f
    raise ValueError(dia)


def bloco_de(dia):
    for b in C.BLOCOS:
        if b["inicio"] <= dia <= b["fim"]:
            return b
    raise ValueError(dia)


def lines(n, cls=""):
    return f'<div class="lines {cls}">' + "<i></i>" * n + "</div>"


def lines_fill(cls=""):
    return f'<div class="lines fill {cls}">' + "<i></i>" * 45 + "</div>"


def fill_field(label, hint=""):
    h = f' <span class="hint">{e(hint)}</span>' if hint else ""
    return f'<div class="field grow"><div class="label">{e(label)}{h}</div>{lines_fill()}</div>'


def field(label, n, hint=""):
    h = f' <span class="hint">{e(hint)}</span>' if hint else ""
    return f'<div class="field"><div class="label">{e(label)}{h}</div>{lines(n)}</div>'


def qfield(q, n):
    return f'<div class="field"><div class="q">{e(q)}</div>{lines(n)}</div>'


def check(text, cls=""):
    return f'<div class="check {cls}"><span class="box"></span><span>{e(text)}</span></div>'


def verse_box(texto, ref, extra=""):
    return (f'<div class="verse-box {extra}"><p class="verse">“{e(texto)}”'
            f'<span class="verse-ref">{e(ref)}</span></p></div>')


def scale(n=11, start=0):
    return '<div class="scale">' + "".join(f'<span class="dot">{i}</span>' for i in range(start, start + n)) + "</div>"


def scale5():
    return '<span class="scale5">' + '<span class="dot"></span>' * 5 + "</span>"


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
pages = []  # lista de (classe_extra, html_interno, mostrar_rodape)


def page(inner, cls="", foot=True, section=""):
    pages.append({"cls": cls, "inner": inner, "foot": foot, "section": section})


def head(left, right=""):
    return f'<div class="head"><span class="tag">{left}</span><span class="tag">{right}</span></div>'


# Capa ----------------------------------------------------------------------
page(f'''
<div class="frame"></div>
<div class="kicker">Caderno prático de 100 dias</div>
<h1>De Tola<br>a <em>Virtuosa</em></h1>
<p class="sub">{e(C.SUBTITULO)}</p>
<div class="tag">{e(C.TAGLINE)}</div>
<p class="verse">“{e(C.VERSICULO_CAPA["texto"])}”<span class="verse-ref">{e(C.VERSICULO_CAPA["ref"])}</span></p>
''', cls="cover", foot=False)

# Este caderno é de ----------------------------------------------------------
page(f'''
{head("Antes de tudo")}
<div style="margin-top:30mm" class="owner">
  <div class="eyebrow">Este caderno é de</div>
  <div class="line" style="height:14mm"></div>
  <div class="cols" style="margin-top:12mm">
    <div><div class="line"></div><div class="lbl">Data do dia 1</div></div>
    <div><div class="line"></div><div class="lbl">Data do dia 100</div></div>
  </div>
  <div style="margin-top:14mm">
    <div class="eyebrow">Meu porquê, em uma frase</div>
    {lines(3)}
  </div>
  <div style="margin-top:14mm">
    <div class="eyebrow">Onde eu estou hoje</div>
    <div class="cols tight" style="flex-wrap:wrap">
      {check("Solteira")}{check("Namorando")}{check("Noiva")}{check("Casada")}{check("Mãe")}
    </div>
    <p class="small muted" style="margin-top:2mm">Cada fase da vida tem seus desafios. O chamado é o mesmo. Marque a sua e adapte os desafios à sua realidade.</p>
  </div>
</div>
<div style="margin-top:auto">{verse_box("Ensina-nos a contar os nossos dias, de tal maneira que alcancemos corações sábios.", "Salmo 90:12", "center")}</div>
''', section="Início")

# Carta de boas-vindas ------------------------------------------------------
cw = C.CARTA_BOAS_VINDAS
page(f'''
{head("Carta de boas-vindas")}
<h1>{e(cw["titulo"])}</h1>
<div style="font-size:10.2pt;line-height:1.5;max-width:165mm">
{"".join(f"<p>{e(p)}</p>" for p in cw["paragrafos"])}
<p class="serif" style="font-size:15pt;font-style:italic;color:var(--rubi);margin-top:5mm">{e(cw["assinatura"])}</p>
</div>
<div class="compromisso">
  <div class="eyebrow">Meu compromisso</div>
  <p style="font-size:10pt;margin-bottom:1mm">Eu, <span style="display:inline-block;border-bottom:0.3mm solid var(--carvao);width:80mm"></span>, decido viver estes 100 dias com honestidade, sem perfeição e sem desistir. Quando falhar, viro a página. Quando acertar, agradeço a Deus.</p>
  <div class="sig"><div>Assinatura</div><div class="short">Data</div></div>
</div>
''', section="Início")

# Como usar -----------------------------------------------------------------
cu = C.COMO_USAR
page(f'''
{head("Regras do jogo")}
<h1>{e(cu["titulo"])}</h1>
<p class="muted">{e(cu["intro"])}</p>
<ol class="steps">
{"".join(f"<li><div><b>{e(t)}</b><span>{e(d)}</span></div></li>" for t, d in cu["regras"])}
</ol>
<h3 style="margin-top:5mm">{e(cu["legenda_titulo"])}</h3>
<div class="legend">
{"".join(f"<div><b>{e(t)}</b>{e(d)}</div>" for t, d in cu["legenda"])}
</div>
<div class="rituais">
  <div><div class="eyebrow">Ritual da manhã · 10 minutos</div><ol><li>Um copo de água antes de qualquer coisa.</li><li>Louvor ou silêncio, sem tela.</li><li>Leitura de hoje, com caneta na mão.</li><li>Ler o desafio do dia e decidir quando vai fazer.</li><li>Uma oração curta: "Senhor, hoje é teu."</li></ol></div>
  <div><div class="eyebrow">Ritual da noite · 5 minutos</div><ol><li>Marcar o checklist com honestidade.</li><li>Três gratidões específicas.</li><li>A maior dificuldade e o que ela mostrou.</li><li>Amanhã eu vou: uma coisa só.</li><li>Celular fora do quarto. Deitar de verdade.</li></ol></div>
</div>
''', section="Início")

# Tola ou virtuosa ----------------------------------------------------------
tv = C.TOLA_VIRTUOSA
page(f'''
{head("Diagnóstico")}
<h1>{e(tv["titulo"])}</h1>
{verse_box(tv["versiculo"], tv["ref"])}
<p style="font-size:10pt">{e(tv["intro"])}</p>
<table class="contrast">
<tr><th>A tola</th><th class="v">A virtuosa</th></tr>
{"".join(f'<tr><td class="t">{e(a)}</td><td class="v">{e(b)}</td></tr>' for a, b in tv["contrastes"])}
</table>
<p style="font-size:10pt;margin-top:3mm">{e(tv["fechamento"])}</p>
<div class="field" style="margin-top:3mm"><div class="label">Em qual linha eu mais me reconheci? Por quê?</div>{lines(3)}</div>
''', cls="c-rubi", section="Início")

# Identidade ----------------------------------------------------------------
idn = C.IDENTIDADE
page(f'''
{head("Identidade")}
<h1>{e(idn["titulo"])}</h1>
<p style="font-size:10pt">{e(idn["intro"])}</p>
<div class="idgrid">
{"".join(f'<div class="id"><b>{e(t)}</b><span>“{e(v)}”</span><i>{e(r)}</i></div>' for t, v, r in idn["versiculos"])}
</div>
<div class="field"><div class="q">{e(idn["pergunta1"])}</div>{lines(5)}</div>
<div class="field"><div class="q">{e(idn["pergunta2"])}</div>{lines(5)}</div>
''', cls="c-rubi", section="Início")

# Corpo, alma e espírito ----------------------------------------------------
cae = C.CORPO_ALMA_ESPIRITO
pil = ""
for p in cae["pilares"]:
    pil += f'''<div class="card accent c-{p["cor"]}" style="--accent:var(--{p["cor"]})">
      <div class="eyebrow" style="color:var(--{p["cor"]})">{e(p["nome"])}</div>
      <p class="serif" style="font-size:11.5pt;line-height:1.2;margin-bottom:2mm">{e(p["frase"])}</p>
      <p class="small" style="margin-bottom:2mm">{" · ".join(e(i) for i in p["itens"])}</p>
      <p class="verse" style="font-size:9.5pt">“{e(p["versiculo"])}”<span class="verse-ref">{e(p["ref"])}</span></p>
    </div>'''
page(f'''
{head("Tudo está ligado")}
<h1>{e(cae["titulo"])}</h1>
{verse_box(cae["versiculo"], cae["ref"])}
<p style="font-size:10pt">{e(cae["intro"])}</p>
<div class="cols tight" style="margin:3mm 0 4mm">{pil}</div>
<p style="font-size:10pt">{e(cae["fechamento"])}</p>
{verse_box(cae["disciplina"], cae["disciplina_ref"])}
<div class="field"><div class="label">Qual hábito de um pilar está derrubando os outros dois na minha vida hoje?</div>{lines(2)}</div>
''', cls="c-rubi", section="Início")

# Virtudes ------------------------------------------------------------------
vt = C.VIRTUDES
page(f'''
{head("Glossário")}
<h1>{e(vt["titulo"])}</h1>
<p style="font-size:10pt">{e(vt["intro"])}</p>
<div class="vgrid">
{"".join(f'<div class="vi"><span class="box"></span><div><b>{e(n)}</b><span>{e(d)}</span><i>{e(r)}</i></div></div>' for n, d, r in vt["lista"])}
</div>
{verse_box(vt["fruto"], vt["fruto_ref"])}
<div class="field"><div class="label">{e(vt["pergunta"])}</div>{lines(3)}</div>
''', cls="c-rubi", section="Início")

# Feminilidade --------------------------------------------------------------
fm = C.FEMINILIDADE
page(f'''
{head("Força e dignidade")}
<h1>{e(fm["titulo"])}</h1>
<p style="font-size:10pt">{e(fm["intro"])}</p>
{"".join(verse_box(v, r) for v, r in fm["versiculos"])}
<h3 style="margin-top:2mm">{e(fm["mulheres_titulo"])}</h3>
<div class="wgrid">
{"".join(f'<div class="w"><b>{e(n)}</b><span>{e(d)}</span><i>{e(r)}</i></div>' for n, d, r in fm["mulheres"])}
</div>
<div class="field" style="margin-top:4mm"><div class="q">{e(fm["pergunta"])}</div>{lines(4)}</div>
''', cls="c-rubi", section="Início")

# Autoconhecimento ----------------------------------------------------------
ac = C.AUTOCONHECIMENTO
page(f'''
{head("Quem eu sou")}
<h1>{e(ac["titulo"])}</h1>
{verse_box(ac["versiculo"], ac["ref"])}
<p class="muted">{e(ac["intro"])}</p>
{"".join(qfield(q, 3) for q in ac["perguntas"])}
''', cls="c-rubi", section="Início")

# Propósito -----------------------------------------------------------------
pr = C.PROPOSITO
page(f'''
{head("Pra que eu fui chamada")}
<h1>{e(pr["titulo"])}</h1>
{verse_box(pr["versiculo"], pr["ref"])}
<p style="font-size:10pt">{e(pr["intro"])}</p>
{"".join(qfield(q, 3) for q in pr["perguntas"])}
<div class="card fill c-dourado" style="--accent-claro:var(--dourado-claro);margin-top:1mm">
  <div class="label">{e(pr["frase"])}</div>{lines(3)}
</div>
<div style="margin-top:3mm">{verse_box(pr["versiculo2"], pr["ref2"])}</div>
''', cls="c-dourado", section="Início")

# Limites -------------------------------------------------------------------
lm = C.LIMITES
areas = ""
for nome, desc in lm["areas"]:
    cols = "".join(f'<div><div class="label">{e(c)}</div>{lines(4, "tight")}</div>' for c in lm["colunas"])
    areas += f'''<div class="limites-area">
      <h3>{e(nome)} <span class="small muted" style="font-family:var(--sans);font-weight:400">{e(desc)}</span></h3>
      <div class="cols tight">{cols}</div></div>'''
page(f'''
{head("Antes que a situação apareça")}
<h1>{e(lm["titulo"])}</h1>
<p style="font-size:9.5pt">{e(lm["intro"])}</p>
<div class="cols tight" style="margin-bottom:3mm">
{"".join(f'<p class="verse" style="font-size:9.5pt">“{e(v)}”<span class="verse-ref">{e(r)}</span></p>' for v, r in lm["versiculos"])}
</div>
{areas}
''', cls="c-rubi", section="Início")

# Regras --------------------------------------------------------------------
rg = C.REGRAS
page(f'''
{head("Inegociáveis")}
<h1>{e(rg["titulo"])}</h1>
<p style="font-size:10pt">{e(rg["intro"])}</p>
<ul class="rules">{"".join(f'<li><span class="box"></span><span>{e(r)}</span></li>' for r in rg["lista"])}</ul>
<div class="field"><div class="label">{e(rg["minhas"])}</div>{lines(8)}</div>
<div style="margin-top:auto">{verse_box(rg["versiculo"], rg["ref"], "center")}</div>
''', cls="c-rubi", section="Início")

# Quadro dos sonhos ---------------------------------------------------------
qs = C.QUADRO_SONHOS
dreams = ""
for nome, cor in qs["areas"]:
    dreams += f'''<div class="d c-{cor}"><h3>{e(nome)}</h3>
      <div class="label">{e(qs["campos"][0])}</div>{lines(3, "tight")}
      <div class="label">{e(qs["campos"][1])}</div>{lines(2, "tight")}</div>'''
page(f'''
{head("Escreve a visão")}
<h1>{e(qs["titulo"])}</h1>
{verse_box(qs["versiculo"], qs["ref"])}
<p style="font-size:9.5pt">{e(qs["intro"])}</p>
<div class="dreams">{dreams}</div>
''', cls="c-rubi", section="Início")

# Carta pro futuro ----------------------------------------------------------
cf = C.CARTA_FUTURO
page(f'''
{head("Só abrir no dia 100")}
<h1>{e(cf["titulo"])}</h1>
<p class="muted">{e(cf["intro"])}</p>
<div class="letter">
  <div class="serif" style="font-size:13pt;font-style:italic;margin:2mm 0 1mm">{e(cf["cabecalho"])}</div>
  {lines_fill()}
</div>
<p class="tiny muted" style="margin:2mm 0 0;text-align:right">{e(cf["rodape"])}</p>
<div class="corner"></div>
''', cls="c-rubi", section="Início")

# Retrato do dia 1 ----------------------------------------------------------
rt = C.RETRATO
def retrato(dia100=False):
    rows = ""
    for a in rt["areas"]:
        if dia100:
            rows += f'<div class="retrato-row two"><span class="nm">{e(a)}</span><span class="lbl">Dia 1</span>{scale()}<span class="lbl">Dia 100</span>{scale()}</div>'
        else:
            rows += f'<div class="retrato-row"><span class="nm">{e(a)}</span>{scale()}</div>'
    if dia100:
        meas = "".join(f'<div class="m"><b>{e(m)}</b><span><i>dia 1</i><i>dia 100</i></span></div>' for m in rt["medidas"])
        meas = f'<div class="measures two">{meas}</div>'
        extra = (f'<div class="cols"><div class="field"><div class="label">{e(rt["dia100_mudou"])}</div>{lines(4)}</div>'
                 f'<div class="field"><div class="label">{e(rt["dia100_deus"])}</div>{lines(4)}</div></div>'
                 + fill_field("Oração de chegada", "o que eu quero dizer a Deus ao terminar"))
    else:
        meas = "".join(f'<div class="m"><b>{e(m)}</b></div>' for m in rt["medidas"])
        meas = f'<div class="measures">{meas}</div>'
        extra = (f'<div class="cols"><div class="field"><div class="label">{e(rt["palavras"])}</div>{lines(2)}</div>'
                 f'<div class="field"><div class="label">{e(rt["incomodo"])}</div>{lines(2)}</div></div>'
                 + fill_field("Oração de partida", "o que eu quero pedir a Deus antes do dia 1"))
    t = rt["titulo_dia100"] if dia100 else rt["titulo_dia1"]
    i = rt["intro_dia100"] if dia100 else rt["intro_dia1"]
    return f'''
{head("Foto honesta", "Dia 100" if dia100 else "Dia 1")}
<h1>{e(t)}</h1>
<p class="muted">{e(i)}</p>
<div class="label">De 0 a 10, como está cada área hoje</div>
{rows}
<div class="label" style="margin-top:4mm">Números</div>
{meas}
{extra}
'''

page(retrato(False), cls="c-rubi", section="Início")

# Mapa dos 100 dias ---------------------------------------------------------
mp = C.MAPA
mapa = ""
for f in C.FASES:
    bl = [b for b in C.BLOCOS if b["fase"] == f["num"]]
    blist = "".join(f'<div><span class="bn">Bloco {b["num"]} · dias {b["inicio"]} a {b["fim"]}</span><span class="bv">{e(b["virtude"])}</span><span class="bd">{e(b["sub"])}</span><span class="bd" style="margin-top:2mm">Início ___/___ · Fim ___/___</span><span class="box"></span></div>' for b in bl)
    mapa += f'''<div class="map-fase c-{f["cor"]}">
      <div class="fcard"><div class="eyebrow">Fase {f["num"]} · {e(f["dias"])}</div><h3>{e(f["nome"])}</h3><p class="small" style="margin:1.5mm 0 0">{e(f["versiculo"])}</p></div>
      <div class="blist">{blist}</div></div>'''
page(f'''
{head("Visão geral")}
<h1>{e(mp["titulo"])}</h1>
<p class="muted">{e(mp["intro"])}</p>
{mapa}
<div class="field" style="margin-top:auto"><div class="label">Uma pessoa a quem vou prestar contas nesses 100 dias <span class="hint">(amiga, irmã, discipuladora, marido)</span></div>{lines(1)}</div>
''', section="Início")

# ---------------------------------------------------------------------------
# Fases, blocos e dias
# ---------------------------------------------------------------------------
def tracker(fase):
    n = fase["fim"] - fase["inicio"] + 1
    dias = list(range(fase["inicio"], fase["fim"] + 1))
    ths = "".join(f"<th>{d}</th>" for d in dias)
    rows = ""
    for h in C.TRACKER_HABITOS:
        tds = "".join('<td class="sep"></td>' if (i + 1) % 10 == 0 and i + 1 < n else "<td></td>" for i in range(n))
        rows += f'<tr><th class="h">{e(h)}</th>{tds}</tr>'
    return f'<table class="tracker"><thead><tr><th class="h">Hábito / dia</th>{ths}</tr></thead><tbody>{rows}</tbody></table>'


def fase_pages(f):
    cls = f"fase-open c-{f['cor']}"
    page(f'''
<div class="fnum">{f["num"]}</div>
<div class="eyebrow">Fase {f["num"]} · {e(f["dias"])}</div>
<h1>{e(f["nome"])}</h1>
{verse_box(f["versiculo"], f["ref"])}
<p>{e(f["resumo"])}</p>
<div class="eyebrow" style="margin-top:6mm">O que acontece nesta fase</div>
<ul class="foco">{"".join(f"<li>{e(x)}</li>" for x in f["foco"])}</ul>
<div class="compromisso">
  <div class="label">Nesta fase eu me comprometo com <span class="hint" style="color:rgba(249,245,238,0.7)">(três coisas concretas)</span></div>
  {lines(3)}
  <div class="sig"><div>Assinatura</div><div class="short">Data de início</div><div class="short">Data de fim</div></div>
</div>
''', cls=cls, section=f"Fase {f['num']} · {f['nome']}")
    # tracker da fase
    page(f'''
{head(f"Fase {f['num']} · {e(f['nome'])}", e(f["dias"]))}
<h2>Tracker de hábitos</h2>
<p class="muted small">Pinte o quadradinho no fim do dia. Olhar 30 dias de uma vez mostra o que o checklist diário esconde: o padrão.</p>
{tracker(f)}
<div class="cols" style="margin-top:5mm">
  <div class="field"><div class="label">O hábito que mais falhou nesta fase</div>{lines(2)}</div>
  <div class="field"><div class="label">O hábito que virou automático</div>{lines(2)}</div>
</div>
<div class="cols"><div class="field"><div class="label">Sequência mais longa sem falhar <span class="hint">(dias seguidos)</span></div>{lines(1)}</div>
<div class="field"><div class="label">Dias com o checklist completo</div>{lines(1)}</div></div>
{fill_field("Notas da fase", "o que eu percebi olhando o padrão")}
''', cls=f"c-{f['cor']}", section=f"Fase {f['num']} · {f['nome']}")


def bloco_open(b):
    f = fase_de(b["inicio"])
    cls = f"bloco-open c-{f['cor']}"
    metas = "".join(
        f'<div class="p-{k}"><div class="eyebrow">{k.capitalize().replace("Espirito", "Espírito")}</div>{e(v)}</div>'
        for k, v in b["metas"].items())
    page(f'''
<div class="num">{b["num"]:02d}</div>
<div class="eyebrow">Bloco {b["num"]} · dias {b["inicio"]} a {b["fim"]} · Fase {f["num"]}, {e(f["nome"])}</div>
<div class="big">{e(b["virtude"])}</div>
<div class="sub">{e(b["sub"])}</div>
<p style="font-size:10.5pt;max-width:160mm">{e(b["definicao"])}</p>
{verse_box(b["versiculo"], b["ref"])}
<div class="tv">
  <div class="t"><span class="who">A tola</span>{e(b["tola"])}</div>
  <div class="v"><span class="who">A virtuosa</span>{e(b["virtuosa"])}</div>
</div>
<div class="eyebrow">Metas destes 10 dias</div>
<div class="metas">{metas}</div>
<div class="field"><div class="label">Minha meta pessoal deste bloco <span class="hint">(uma só, mensurável)</span></div>{lines(2)}</div>
<div class="field"><div class="label">Uma pessoa que eu quero abençoar neste bloco</div>{lines(1)}</div>
<div class="field"><div class="label">Onde eu acho que a {e(b["virtude"].lower())} vai ser testada nesses dias</div>{lines(3)}</div>
<div class="field"><div class="label">Uma oração pra estes 10 dias</div>{lines(3)}</div>
''', cls=cls, section=f"Bloco {b['num']} · {b['virtude']}")


def day_page(d):
    f = fase_de(d)
    b = bloco_de(d)
    pct = d  # 0..100
    corpo = "".join(check(x) for x in C.CHECKLIST["corpo"])
    mente = "".join(check(x) for x in C.CHECKLIST["mente"])
    esp = "".join(check(x) for x in C.CHECKLIST["espirito"])
    page(f'''
<div class="head">
  <div class="daynum"><small>Dia</small>{d:02d}</div>
  <div class="meta">
    <div class="virt">{e(b["virtude"])}</div>
    <span class="tag">Bloco {b["num"]} · Fase {f["num"]}, {e(f["nome"])}</span>
    <div class="date">Data <span></span>/<span></span>/<span></span></div>
  </div>
</div>
<div class="topgrid">
  <div class="reading"><div class="box"><div class="eyebrow">Leitura de hoje</div><div class="txt">{e(C.LEITURAS[d-1])}</div></div></div>
  <div class="challenge"><div class="box"><div class="eyebrow">Desafio do dia</div><div class="txt">{e(C.DESAFIOS[d-1])}</div></div></div>
</div>
<div class="pillars">
  <div class="p-corpo"><div class="eyebrow">Corpo</div>{corpo}</div>
  <div class="p-mente"><div class="eyebrow">Mente</div>{mente}</div>
  <div class="p-espirito"><div class="eyebrow">Espírito</div>{esp}</div>
</div>
<div class="field"><div class="label">{e(b["virtude"])} em ação <span class="hint">hoje eu pratiquei quando…  ou faltou quando…</span></div>{lines(2)}</div>
<div class="field"><div class="label">Três coisas pelas quais sou grata hoje</div>{lines(3)}</div>
<div class="field"><div class="label">Minha maior dificuldade hoje foi <span class="hint">e o que ela me mostrou</span></div>{lines(5)}</div>
<div class="field"><div class="label">Uma linha pra Deus <span class="hint">oração, pedido, agradecimento, desabafo</span></div>{lines(2)}</div>
<div class="field"><div class="label">Amanhã eu vou <span class="hint">uma coisa só</span></div>{lines(1)}</div>
<p class="verse" style="margin-top:auto;text-align:center;font-size:10.5pt;padding:0 10mm">“{e(b["versiculo"])}”<span class="verse-ref">{e(b["ref"])}</span></p>
<div class="bottom">
  <div class="grp">Energia {scale5()}</div>
  <div class="grp">Humor {scale5()}</div>
  <div class="grp"><span class="progress"><i style="width:{pct}%"></i></span> {d} de 100</div>
  <div class="skip"><span class="box"></span> Pulei hoje</div>
</div>
''', cls=f"day c-{f['cor']}", section=f"Bloco {b['num']} · {b['virtude']}")


def bloco_review(b):
    f = fase_de(b["inicio"])
    rv = C.REVISAO
    notas = "".join(f'<div><div class="label">{e(n)}</div>{scale5()}</div>' for n in rv["notas"])
    qs_ = "".join(field(q, n) for q, n in rv["perguntas"])
    page(f'''
{head(f"Bloco {b['num']} · {e(b['virtude'])}", f"dias {b['inicio']} a {b['fim']}")}
<h1>{e(rv["titulo"])} {b["num"]}</h1>
<div class="cols" style="align-items:center;margin-bottom:3mm">
  <div><div class="label">Dias completos</div><div class="serif" style="font-size:22pt">____ / 10</div></div>
  <div><div class="label">Cumpri a meta pessoal do bloco?</div><div style="display:flex;gap:5mm">{check("Sim")}{check("Em parte")}{check("Não")}</div></div>
</div>
<div class="label">Nota de 1 a 5</div>
<div class="notas">{notas}</div>
{qs_}
''', cls=f"review c-{f['cor']}", section=f"Bloco {b['num']} · {b['virtude']}")


for f in C.FASES:
    fase_pages(f)
    for b in [x for x in C.BLOCOS if x["fase"] == f["num"]]:
        bloco_open(b)
        for d in range(b["inicio"], b["fim"] + 1):
            day_page(d)
        bloco_review(b)

# ---------------------------------------------------------------------------
# Fechamento
# ---------------------------------------------------------------------------
page(retrato(True), cls="c-ameixa", section="Fechamento")

fc = C.FECHAMENTO
page(f'''
{head("Dia 100")}
<h1>{e(fc["titulo"])}</h1>
{verse_box(fc["versiculo"], fc["ref"])}
<div style="font-size:10pt">{"".join(f"<p>{e(p)}</p>" for p in fc["paragrafos"])}</div>
<div class="card accent c-ameixa" style="margin-top:3mm">
  <div class="label">{e(fc["proximos_titulo"])} <span class="hint">____ / ____ / ______</span></div>
  {"".join(field(q, 2) for q in fc["proximos"])}
</div>
<p class="serif" style="font-size:12pt;font-style:italic;margin-top:4mm;color:var(--rubi)">{e(fc["comunidade"])}</p>
''', cls="c-ameixa", section="Fechamento")

# Página de notas livres
page(f'''
{head("Notas livres")}
<h2>O que não coube nas outras páginas</h2>
{lines_fill()}
''', section="Fechamento")

# Contracapa
cc = C.CONTRACAPA
page(f'''
<p class="verse">“{e(cc["versiculo"])}”<span class="verse-ref">{e(cc["ref"])}</span></p>
<div class="brand">De Tola a Virtuosa<small>100 dias · corpo, alma e espírito</small></div>
''', cls="back", foot=False)

# ---------------------------------------------------------------------------
# Montagem
# ---------------------------------------------------------------------------
out = []
out.append('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">')
out.append(f'<title>{e(C.TITULO)}: 100 dias</title>')
out.append('<link rel="stylesheet" href="../src/styles.css">')
out.append('</head><body>')
total = len(pages)
for i, p in enumerate(pages, start=1):
    foot = ""
    if p["foot"]:
        foot = f'<div class="foot"><span>{e(FOOT_BRAND)}</span><span class="stripe"></span><span>{e(p["section"])}</span><span class="stripe"></span><span class="num">{i}</span></div>'
    out.append(f'<section class="page {p["cls"]}">{p["inner"]}{foot}</section>')
out.append('</body></html>')

os.makedirs(DIST, exist_ok=True)
with open(OUT_HTML, "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))

print(f"{total} páginas -> {OUT_HTML}")
