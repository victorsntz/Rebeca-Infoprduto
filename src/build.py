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
DECO = '''<svg class="floral" viewBox="0 0 210 148" preserveAspectRatio="none" aria-hidden="true"><defs><radialGradient id="g-rosa" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#E3B6B1" stop-opacity="0.95"/><stop offset="0.55" stop-color="#B95E6A" stop-opacity="0.75"/><stop offset="1" stop-color="#B95E6A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-rosa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E3B6B1" stop-opacity="0.9"/><stop offset="1" stop-color="#B95E6A" stop-opacity="0.35"/></linearGradient><radialGradient id="g-rosa2" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#F0CFC6" stop-opacity="0.95"/><stop offset="0.55" stop-color="#C97B7B" stop-opacity="0.75"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0.05"/></radialGradient><linearGradient id="l-rosa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F0CFC6" stop-opacity="0.9"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0.35"/></linearGradient><radialGradient id="g-gold" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#F3DDA6" stop-opacity="0.95"/><stop offset="0.55" stop-color="#C9A15A" stop-opacity="0.75"/><stop offset="1" stop-color="#C9A15A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F3DDA6" stop-opacity="0.9"/><stop offset="1" stop-color="#C9A15A" stop-opacity="0.35"/></linearGradient><radialGradient id="g-salvia" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#B9C6B0" stop-opacity="0.95"/><stop offset="0.55" stop-color="#6F8468" stop-opacity="0.75"/><stop offset="1" stop-color="#6F8468" stop-opacity="0.05"/></radialGradient><linearGradient id="l-salvia" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B9C6B0" stop-opacity="0.9"/><stop offset="1" stop-color="#6F8468" stop-opacity="0.35"/></linearGradient><radialGradient id="g-salvia2" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#CFD9C8" stop-opacity="0.95"/><stop offset="0.55" stop-color="#7E9377" stop-opacity="0.75"/><stop offset="1" stop-color="#7E9377" stop-opacity="0.05"/></radialGradient><linearGradient id="l-salvia2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#CFD9C8" stop-opacity="0.9"/><stop offset="1" stop-color="#7E9377" stop-opacity="0.35"/></linearGradient><radialGradient id="g-wine" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#C88A93" stop-opacity="0.95"/><stop offset="0.55" stop-color="#7A2C3A" stop-opacity="0.75"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-wine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C88A93" stop-opacity="0.9"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.35"/></linearGradient><radialGradient id="wash" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#C97B7B" stop-opacity="0.35"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0"/></radialGradient><radialGradient id="washg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7E9377" stop-opacity="0.35"/><stop offset="1" stop-color="#7E9377" stop-opacity="0"/></radialGradient></defs>
  <ellipse cx="200" cy="140" rx="90" ry="60" fill="url(#wash)" opacity="0.7"/><ellipse cx="10" cy="8" rx="70" ry="50" fill="url(#wash)" opacity="0.5"/>
</svg>
<svg class="aq br" viewBox="0 0 70 70" aria-hidden="true"><defs><radialGradient id="g-rosa" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#E3B6B1" stop-opacity="0.95"/><stop offset="0.55" stop-color="#B95E6A" stop-opacity="0.75"/><stop offset="1" stop-color="#B95E6A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-rosa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E3B6B1" stop-opacity="0.9"/><stop offset="1" stop-color="#B95E6A" stop-opacity="0.35"/></linearGradient><radialGradient id="g-rosa2" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#F0CFC6" stop-opacity="0.95"/><stop offset="0.55" stop-color="#C97B7B" stop-opacity="0.75"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0.05"/></radialGradient><linearGradient id="l-rosa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F0CFC6" stop-opacity="0.9"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0.35"/></linearGradient><radialGradient id="g-gold" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#F3DDA6" stop-opacity="0.95"/><stop offset="0.55" stop-color="#C9A15A" stop-opacity="0.75"/><stop offset="1" stop-color="#C9A15A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F3DDA6" stop-opacity="0.9"/><stop offset="1" stop-color="#C9A15A" stop-opacity="0.35"/></linearGradient><radialGradient id="g-salvia" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#B9C6B0" stop-opacity="0.95"/><stop offset="0.55" stop-color="#6F8468" stop-opacity="0.75"/><stop offset="1" stop-color="#6F8468" stop-opacity="0.05"/></radialGradient><linearGradient id="l-salvia" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B9C6B0" stop-opacity="0.9"/><stop offset="1" stop-color="#6F8468" stop-opacity="0.35"/></linearGradient><radialGradient id="g-salvia2" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#CFD9C8" stop-opacity="0.95"/><stop offset="0.55" stop-color="#7E9377" stop-opacity="0.75"/><stop offset="1" stop-color="#7E9377" stop-opacity="0.05"/></radialGradient><linearGradient id="l-salvia2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#CFD9C8" stop-opacity="0.9"/><stop offset="1" stop-color="#7E9377" stop-opacity="0.35"/></linearGradient><radialGradient id="g-wine" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#C88A93" stop-opacity="0.95"/><stop offset="0.55" stop-color="#7A2C3A" stop-opacity="0.75"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-wine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C88A93" stop-opacity="0.9"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.35"/></linearGradient><radialGradient id="wash" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#C97B7B" stop-opacity="0.35"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0"/></radialGradient><radialGradient id="washg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7E9377" stop-opacity="0.35"/><stop offset="1" stop-color="#7E9377" stop-opacity="0"/></radialGradient></defs><g transform="scale(1.0)"><ellipse cx="34" cy="30" rx="40" ry="30" fill="url(#washg)"/><path d="M6.0 62.0 14.0 50.0 24.0 40.0 38.0 30.0" fill="none" stroke="#7E9377" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/><path d="M18.0 60.0 26.0 48.0 40.0 42.0" fill="none" stroke="#7E9377" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/><path d="M30.0 64.0 36.0 52.0 46.0 48.0" fill="none" stroke="#7E9377" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/><g transform="translate(12.0 54.0) rotate(-40)"><path d="M0 0 C 5.3 -4.9, 5.3 -10.5, 0 -14.0 C -5.3 -10.5, -5.3 -4.9, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -11.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(20.0 46.0) rotate(20)"><path d="M0 0 C 5.7 -5.2, 5.7 -11.2, 0 -15.0 C -5.7 -11.2, -5.7 -5.2, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -12.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(26.0 44.0) rotate(-60)"><path d="M0 0 C 4.9 -4.5, 4.9 -9.8, 0 -13.0 C -4.9 -9.8, -4.9 -4.5, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -10.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(33.0 36.0) rotate(25)"><path d="M0 0 C 5.3 -4.9, 5.3 -10.5, 0 -14.0 C -5.3 -10.5, -5.3 -4.9, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -11.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(40.0 44.0) rotate(-30)"><path d="M0 0 C 4.6 -4.2, 4.6 -9.0, 0 -12.0 C -4.6 -9.0, -4.6 -4.2, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -9.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(46.0 50.0) rotate(40)"><path d="M0 0 C 4.9 -4.5, 4.9 -9.8, 0 -13.0 C -4.9 -9.8, -4.9 -4.5, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -10.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(30.0 58.0) rotate(60)"><path d="M0 0 C 4.2 -3.8, 4.2 -8.2, 0 -11.0 C -4.2 -8.2, -4.2 -3.8, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -8.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(50.0 42.0) rotate(-20)"><path d="M0 0 C 3.8 -3.5, 3.8 -7.5, 0 -10.0 C -3.8 -7.5, -3.8 -3.5, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -7.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(24.0 56.0) rotate(-85)"><path d="M0 0 C 3.4 -3.1, 3.4 -6.8, 0 -9.0 C -3.4 -6.8, -3.4 -3.1, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -6.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(40.0 28.0) rotate(10)"><ellipse rx="17.6" ry="15.6" fill="url(#wash)"/><ellipse cx="0" cy="-6.3" rx="4.8" ry="7.2" fill="url(#g-rosa)" transform="rotate(-2.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.2" rx="4.7" ry="7.0" fill="url(#g-rosa)" transform="rotate(42.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.7" rx="5.1" ry="7.6" fill="url(#g-rosa)" transform="rotate(80.6)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.0" rx="5.3" ry="7.9" fill="url(#g-rosa)" transform="rotate(112.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.9" rx="5.2" ry="7.7" fill="url(#g-rosa)" transform="rotate(152.6)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.2" rx="4.8" ry="7.0" fill="url(#g-rosa)" transform="rotate(193.1)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.6" rx="5.8" ry="8.5" fill="url(#g-rosa)" transform="rotate(238.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.5" rx="4.9" ry="7.3" fill="url(#g-rosa)" transform="rotate(274.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.8" rx="5.9" ry="8.8" fill="url(#g-rosa)" transform="rotate(322.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(308.0)" opacity="0.9"/><circle r="2.1" fill="#F3DDA6" opacity="0.9"/><circle cx="3.4" cy="0.0" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="2.1" cy="2.6" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.8" cy="3.3" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-3.0" cy="1.5" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-3.0" cy="-1.5" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.8" cy="-3.3" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="2.1" cy="-2.6" r="0.7" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(22.0 40.0) rotate(-30)"><ellipse rx="12.8" ry="11.4" fill="url(#wash)"/><ellipse cx="0" cy="-5.0" rx="3.8" ry="5.6" fill="url(#g-rosa2)" transform="rotate(1.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.5" rx="3.4" ry="5.1" fill="url(#g-rosa2)" transform="rotate(47.6)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.8" rx="3.7" ry="5.4" fill="url(#g-rosa2)" transform="rotate(85.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.6" rx="3.5" ry="5.2" fill="url(#g-rosa2)" transform="rotate(114.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.5" rx="4.2" ry="6.2" fill="url(#g-rosa2)" transform="rotate(156.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.2" rx="4.0" ry="5.9" fill="url(#g-rosa2)" transform="rotate(194.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.9" rx="3.8" ry="5.6" fill="url(#g-rosa2)" transform="rotate(242.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.5" rx="3.5" ry="5.1" fill="url(#g-rosa2)" transform="rotate(280.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.7" rx="3.6" ry="5.3" fill="url(#g-rosa2)" transform="rotate(313.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(308.0)" opacity="0.9"/><circle r="1.5" fill="#F3DDA6" opacity="0.9"/><circle cx="2.5" cy="0.0" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="1.5" cy="1.9" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.5" cy="2.4" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.2" cy="1.1" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.2" cy="-1.1" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.5" cy="-2.4" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="1.5" cy="-1.9" r="0.5" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(50.0 46.0) rotate(50)"><ellipse rx="9.5" ry="8.4" fill="url(#wash)"/><ellipse cx="0" cy="-3.7" rx="2.8" ry="4.2" fill="url(#g-gold)" transform="rotate(2.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.8" rx="2.9" ry="4.3" fill="url(#g-gold)" transform="rotate(42.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.6" rx="2.7" ry="4.0" fill="url(#g-gold)" transform="rotate(89.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.9" rx="3.0" ry="4.4" fill="url(#g-gold)" transform="rotate(139.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.8" rx="2.9" ry="4.3" fill="url(#g-gold)" transform="rotate(175.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.1" rx="3.1" ry="4.6" fill="url(#g-gold)" transform="rotate(225.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.5" rx="2.7" ry="4.0" fill="url(#g-gold)" transform="rotate(273.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.4" rx="2.6" ry="3.8" fill="url(#g-gold)" transform="rotate(322.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(308.0)" opacity="0.9"/><circle r="1.1" fill="#F3DDA6" opacity="0.9"/><circle cx="1.8" cy="0.0" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="1.1" cy="1.4" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.4" cy="1.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.6" cy="0.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.6" cy="-0.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.4" cy="-1.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="1.1" cy="-1.4" r="0.4" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(58.0 32.0) rotate(0)"><ellipse rx="7.4" ry="6.6" fill="url(#wash)"/><ellipse cx="0" cy="-3.1" rx="2.4" ry="3.5" fill="url(#g-wine)" transform="rotate(-1.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.9" rx="2.2" ry="3.3" fill="url(#g-wine)" transform="rotate(45.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.1" rx="2.3" ry="3.5" fill="url(#g-wine)" transform="rotate(95.5)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.0" rx="2.3" ry="3.4" fill="url(#g-wine)" transform="rotate(158.5)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.8" rx="2.1" ry="3.2" fill="url(#g-wine)" transform="rotate(211.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.0" rx="2.3" ry="3.4" fill="url(#g-wine)" transform="rotate(260.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.9" rx="2.2" ry="3.3" fill="url(#g-wine)" transform="rotate(309.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(308.0)" opacity="0.9"/><circle r="0.9" fill="#F3DDA6" opacity="0.9"/><circle cx="1.4" cy="0.0" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="0.9" cy="1.1" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.3" cy="1.4" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.3" cy="0.6" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.3" cy="-0.6" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.3" cy="-1.4" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="0.9" cy="-1.1" r="0.3" fill="#7A2C3A" opacity="0.7"/></g><circle cx="14" cy="60" r="1.2" fill="#F3DDA6" opacity="0.8"/><circle cx="52" cy="58" r="1.3" fill="#F3DDA6" opacity="0.8"/><circle cx="60" cy="22" r="1.0" fill="#F3DDA6" opacity="0.8"/><circle cx="30" cy="24" r="1.1" fill="#F3DDA6" opacity="0.8"/></g></svg>
<svg class="aq tl" viewBox="0 0 70 70" aria-hidden="true"><defs><radialGradient id="g-rosa" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#E3B6B1" stop-opacity="0.95"/><stop offset="0.55" stop-color="#B95E6A" stop-opacity="0.75"/><stop offset="1" stop-color="#B95E6A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-rosa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E3B6B1" stop-opacity="0.9"/><stop offset="1" stop-color="#B95E6A" stop-opacity="0.35"/></linearGradient><radialGradient id="g-rosa2" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#F0CFC6" stop-opacity="0.95"/><stop offset="0.55" stop-color="#C97B7B" stop-opacity="0.75"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0.05"/></radialGradient><linearGradient id="l-rosa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F0CFC6" stop-opacity="0.9"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0.35"/></linearGradient><radialGradient id="g-gold" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#F3DDA6" stop-opacity="0.95"/><stop offset="0.55" stop-color="#C9A15A" stop-opacity="0.75"/><stop offset="1" stop-color="#C9A15A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F3DDA6" stop-opacity="0.9"/><stop offset="1" stop-color="#C9A15A" stop-opacity="0.35"/></linearGradient><radialGradient id="g-salvia" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#B9C6B0" stop-opacity="0.95"/><stop offset="0.55" stop-color="#6F8468" stop-opacity="0.75"/><stop offset="1" stop-color="#6F8468" stop-opacity="0.05"/></radialGradient><linearGradient id="l-salvia" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B9C6B0" stop-opacity="0.9"/><stop offset="1" stop-color="#6F8468" stop-opacity="0.35"/></linearGradient><radialGradient id="g-salvia2" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#CFD9C8" stop-opacity="0.95"/><stop offset="0.55" stop-color="#7E9377" stop-opacity="0.75"/><stop offset="1" stop-color="#7E9377" stop-opacity="0.05"/></radialGradient><linearGradient id="l-salvia2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#CFD9C8" stop-opacity="0.9"/><stop offset="1" stop-color="#7E9377" stop-opacity="0.35"/></linearGradient><radialGradient id="g-wine" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#C88A93" stop-opacity="0.95"/><stop offset="0.55" stop-color="#7A2C3A" stop-opacity="0.75"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.05"/></radialGradient><linearGradient id="l-wine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C88A93" stop-opacity="0.9"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.35"/></linearGradient><radialGradient id="wash" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#C97B7B" stop-opacity="0.35"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0"/></radialGradient><radialGradient id="washg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7E9377" stop-opacity="0.35"/><stop offset="1" stop-color="#7E9377" stop-opacity="0"/></radialGradient></defs><g transform="scale(1.0)"><ellipse cx="34" cy="30" rx="40" ry="30" fill="url(#washg)"/><path d="M6.0 62.0 14.0 50.0 24.0 40.0 38.0 30.0" fill="none" stroke="#7E9377" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/><path d="M18.0 60.0 26.0 48.0 40.0 42.0" fill="none" stroke="#7E9377" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/><path d="M30.0 64.0 36.0 52.0 46.0 48.0" fill="none" stroke="#7E9377" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/><g transform="translate(12.0 54.0) rotate(-40)"><path d="M0 0 C 5.3 -4.9, 5.3 -10.5, 0 -14.0 C -5.3 -10.5, -5.3 -4.9, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -11.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(20.0 46.0) rotate(20)"><path d="M0 0 C 5.7 -5.2, 5.7 -11.2, 0 -15.0 C -5.7 -11.2, -5.7 -5.2, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -12.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(26.0 44.0) rotate(-60)"><path d="M0 0 C 4.9 -4.5, 4.9 -9.8, 0 -13.0 C -4.9 -9.8, -4.9 -4.5, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -10.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(33.0 36.0) rotate(25)"><path d="M0 0 C 5.3 -4.9, 5.3 -10.5, 0 -14.0 C -5.3 -10.5, -5.3 -4.9, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -11.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(40.0 44.0) rotate(-30)"><path d="M0 0 C 4.6 -4.2, 4.6 -9.0, 0 -12.0 C -4.6 -9.0, -4.6 -4.2, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -9.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(46.0 50.0) rotate(40)"><path d="M0 0 C 4.9 -4.5, 4.9 -9.8, 0 -13.0 C -4.9 -9.8, -4.9 -4.5, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -10.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(30.0 58.0) rotate(60)"><path d="M0 0 C 4.2 -3.8, 4.2 -8.2, 0 -11.0 C -4.2 -8.2, -4.2 -3.8, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -8.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(50.0 42.0) rotate(-20)"><path d="M0 0 C 3.8 -3.5, 3.8 -7.5, 0 -10.0 C -3.8 -7.5, -3.8 -3.5, 0 0 z" fill="url(#l-salvia2)"/><path d="M0 -2 L0 -7.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(24.0 56.0) rotate(-85)"><path d="M0 0 C 3.4 -3.1, 3.4 -6.8, 0 -9.0 C -3.4 -6.8, -3.4 -3.1, 0 0 z" fill="url(#l-salvia)"/><path d="M0 -2 L0 -6.0" stroke="#F9F5EE" stroke-width="0.35" opacity="0.45"/></g><g transform="translate(40.0 28.0) rotate(10)"><ellipse rx="17.6" ry="15.6" fill="url(#wash)"/><ellipse cx="0" cy="-7.3" rx="5.6" ry="8.3" fill="url(#g-rosa)" transform="rotate(-7.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.9" rx="6.0" ry="8.9" fill="url(#g-rosa)" transform="rotate(42.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.6" rx="5.0" ry="7.4" fill="url(#g-rosa)" transform="rotate(85.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.3" rx="5.6" ry="8.2" fill="url(#g-rosa)" transform="rotate(118.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.9" rx="5.3" ry="7.8" fill="url(#g-rosa)" transform="rotate(152.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.3" rx="4.8" ry="7.1" fill="url(#g-rosa)" transform="rotate(194.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.5" rx="5.7" ry="8.4" fill="url(#g-rosa)" transform="rotate(232.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-6.5" rx="5.0" ry="7.3" fill="url(#g-rosa)" transform="rotate(274.1)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-7.6" rx="5.8" ry="8.6" fill="url(#g-rosa)" transform="rotate(318.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-3.6" rx="2.9" ry="4.3" fill="url(#g-rosa)" transform="rotate(308.0)" opacity="0.9"/><circle r="2.1" fill="#F3DDA6" opacity="0.9"/><circle cx="3.4" cy="0.0" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="2.1" cy="2.6" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.8" cy="3.3" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-3.0" cy="1.5" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-3.0" cy="-1.5" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.8" cy="-3.3" r="0.7" fill="#7A2C3A" opacity="0.7"/><circle cx="2.1" cy="-2.6" r="0.7" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(22.0 40.0) rotate(-30)"><ellipse rx="12.8" ry="11.4" fill="url(#wash)"/><ellipse cx="0" cy="-5.0" rx="3.8" ry="5.7" fill="url(#g-rosa2)" transform="rotate(-6.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.6" rx="4.3" ry="6.3" fill="url(#g-rosa2)" transform="rotate(40.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.6" rx="4.3" ry="6.3" fill="url(#g-rosa2)" transform="rotate(85.1)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.0" rx="3.8" ry="5.6" fill="url(#g-rosa2)" transform="rotate(116.5)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.6" rx="4.3" ry="6.3" fill="url(#g-rosa2)" transform="rotate(157.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.6" rx="3.5" ry="5.2" fill="url(#g-rosa2)" transform="rotate(207.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.7" rx="3.6" ry="5.3" fill="url(#g-rosa2)" transform="rotate(234.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-5.1" rx="3.9" ry="5.7" fill="url(#g-rosa2)" transform="rotate(275.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.8" rx="3.7" ry="5.4" fill="url(#g-rosa2)" transform="rotate(321.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-2.6" rx="2.1" ry="3.1" fill="url(#g-rosa2)" transform="rotate(308.0)" opacity="0.9"/><circle r="1.5" fill="#F3DDA6" opacity="0.9"/><circle cx="2.5" cy="0.0" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="1.5" cy="1.9" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.5" cy="2.4" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.2" cy="1.1" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.2" cy="-1.1" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.5" cy="-2.4" r="0.5" fill="#7A2C3A" opacity="0.7"/><circle cx="1.5" cy="-1.9" r="0.5" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(50.0 46.0) rotate(50)"><ellipse rx="9.5" ry="8.4" fill="url(#wash)"/><ellipse cx="0" cy="-3.7" rx="2.8" ry="4.1" fill="url(#g-gold)" transform="rotate(-7.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.8" rx="2.9" ry="4.3" fill="url(#g-gold)" transform="rotate(42.9)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.9" rx="3.0" ry="4.4" fill="url(#g-gold)" transform="rotate(97.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.9" rx="3.0" ry="4.4" fill="url(#g-gold)" transform="rotate(135.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.3" rx="2.5" ry="3.7" fill="url(#g-gold)" transform="rotate(182.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.0" rx="3.1" ry="4.5" fill="url(#g-gold)" transform="rotate(231.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-4.0" rx="3.1" ry="4.6" fill="url(#g-gold)" transform="rotate(276.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.7" rx="2.8" ry="4.1" fill="url(#g-gold)" transform="rotate(313.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-1.9" rx="1.5" ry="2.3" fill="url(#g-gold)" transform="rotate(308.0)" opacity="0.9"/><circle r="1.1" fill="#F3DDA6" opacity="0.9"/><circle cx="1.8" cy="0.0" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="1.1" cy="1.4" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.4" cy="1.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.6" cy="0.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.6" cy="-0.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.4" cy="-1.8" r="0.4" fill="#7A2C3A" opacity="0.7"/><circle cx="1.1" cy="-1.4" r="0.4" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(58.0 32.0) rotate(0)"><ellipse rx="7.4" ry="6.6" fill="url(#wash)"/><ellipse cx="0" cy="-3.1" rx="2.3" ry="3.4" fill="url(#g-wine)" transform="rotate(-6.3)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.6" rx="2.0" ry="3.0" fill="url(#g-wine)" transform="rotate(44.4)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.7" rx="2.1" ry="3.0" fill="url(#g-wine)" transform="rotate(98.2)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.6" rx="2.0" ry="2.9" fill="url(#g-wine)" transform="rotate(151.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.7" rx="2.1" ry="3.0" fill="url(#g-wine)" transform="rotate(197.7)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-2.8" rx="2.2" ry="3.2" fill="url(#g-wine)" transform="rotate(250.8)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-3.2" rx="2.5" ry="3.6" fill="url(#g-wine)" transform="rotate(301.0)" style="mix-blend-mode:screen"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(20.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(92.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(164.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(236.0)" opacity="0.9"/><ellipse cx="0" cy="-1.5" rx="1.2" ry="1.8" fill="url(#g-wine)" transform="rotate(308.0)" opacity="0.9"/><circle r="0.9" fill="#F3DDA6" opacity="0.9"/><circle cx="1.4" cy="0.0" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="0.9" cy="1.1" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.3" cy="1.4" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.3" cy="0.6" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-1.3" cy="-0.6" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="-0.3" cy="-1.4" r="0.3" fill="#7A2C3A" opacity="0.7"/><circle cx="0.9" cy="-1.1" r="0.3" fill="#7A2C3A" opacity="0.7"/></g><circle cx="14" cy="60" r="1.1" fill="#F3DDA6" opacity="0.8"/><circle cx="52" cy="58" r="0.8" fill="#F3DDA6" opacity="0.8"/><circle cx="60" cy="22" r="0.9" fill="#F3DDA6" opacity="0.8"/><circle cx="30" cy="24" r="0.9" fill="#F3DDA6" opacity="0.8"/></g></svg>'''
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

# Quadro dos sonhos: explicação + mural -------------------------------------
areas = "".join(f'''<div class="c-{cor}"><h3>{e(n)}</h3>
  <div class="label">Meta que dá pra medir</div>{lines(2, "tight")}
  <div class="label" style="margin-top:1mm">Como vou saber que cheguei</div>{lines(1, "tight")}</div>''' for n, cor in rs["areas"])
page(f'''
{head("Escreve a visão", "Habacuque 2:2")}
<div class="split even">
  <div class="l">
    <h1>Quadro dos sonhos</h1>
    <p style="font-size:9.2pt;line-height:1.5">Um quadro dos sonhos é um mural com o que você quer ver acontecer. Aqui ele tem um limite bom: 40 dias. Nada de "ser uma mulher melhor". Escreva coisas que dá pra medir e que cabem em 40 dias: "treinar 3 vezes por semana", "guardar 300 reais", "fazer as pazes com minha irmã", "ler a Bíblia 36 dias de 40".</p>
    <p style="font-size:9.2pt;line-height:1.5">Como montar: escreva as metas nesta página, uma por área. Na página seguinte, cole fotos, recortes de revista, palavras, cores, versículos. Tudo que te lembre de onde você quer chegar. Pode passar do limite da moldura. Pode ficar bagunçado. Mural bonito é mural usado.</p>
    {verse_box("Escreve a visão e torna bem legível sobre tábuas, para que a possa ler o que correndo passa.", "Habacuque 2:2")}
    <div style="margin-top:auto">{field("Minha frase de 40 dias", 2, "a que resume tudo", "tight")}</div>
  </div>
  <div class="r"><div class="sonho-area">{areas}</div></div>
</div>
''', cls="c-rubi", section="Início")
page(f'''
{head("Meu mural", "cole aqui")}
<div class="mural c-rubi">
  <span class="tape a"></span><span class="tape b"></span><span class="tape c"></span>
  {"".join(f'<div class="c-{cor}"><span>{e(n)}</span></div>' for n, cor in rs["areas"])}
</div>
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
  <div class="eyebrow">Prova {b["num"]} de 4</div>
  <div class="dias">Dias {b["inicio"]} a {b["fim"]}</div>
  <h3>{e(b["lugar"])}</h3>
  <div class="v">Virtude: {e(b["virtude"])}</div>
  <div class="w">{e(b["chamada"])}.<br>Companhia: {e(b["mulher"])}.</div>
  <div class="dt">Comecei em ___/___<br>Terminei em ___/___</div>
  <div class="ck"><span class="box"></span> Prova concluída</div></div>''' for b in C.BLOCOS)
trail = "".join(f'<span class="seg" style="background:var(--{b["cor"]})"><i>{b["inicio"]}</i>{"<em>40</em>" if b["num"] == 4 else ""}</span>' for b in C.BLOCOS)
page(f'''
{head("Visão geral", "O caminho inteiro em uma página")}
<div class="mapa-head">
  <div><h1>O mapa dos 40 dias</h1>
  <p style="font-size:9pt;line-height:1.5;margin:0">Você vai atravessar quatro provas de dez dias, uma atrás da outra. Cada prova tem um lugar da jornada do povo de Deus no deserto, uma virtude pra treinar e uma mulher da Bíblia que já passou por ali. Esta página é o seu mapa: anote as datas, marque cada prova quando terminar e volte aqui sempre que esquecer onde está.</p></div>
</div>
<div class="trail">{trail}</div>
<div class="map">{cards}</div>
<div class="cols" style="margin-top:3mm;align-items:flex-end">
  <div style="flex:1.4">{field("Uma pessoa a quem vou prestar contas nesses 40 dias", 1, "amiga, irmã, discipuladora, marido", "tight")}</div>
  <div class="card fill c-dourado" style="flex:1"><div class="eyebrow" style="color:var(--dourado)">Como funciona uma prova</div><p style="font-size:7.6pt;margin:0">Uma página de abertura, um quadro de hábitos, dez páginas de dia e uma revisão. Leia a abertura antes de começar, marque um dia por vez e faça a revisão no fim.</p></div>
</div>
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
    <h2>Quadro de hábitos da prova {b["num"]}</h2>
    <p style="font-size:8.4pt;margin-bottom:2.5mm">Pinte o quadradinho no fim do dia. Dez dias de uma vez mostram o padrão que o dia a dia esconde.</p>
    {tracker(b)}
    <div class="cols" style="margin-top:3mm">
      {field("O hábito que mais falhou", 1)}
      {field("O hábito que virou automático", 1)}
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
    <div class="row"><div class="label">Minha maior dificuldade hoje <span class="hint">e o que ela me mostrou</span></div>{lines(3, "tight")}</div>
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
