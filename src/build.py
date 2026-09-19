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
DECO = '''<svg class="floral" viewBox="0 0 210 148" preserveAspectRatio="none" aria-hidden="true"><defs><radialGradient id="g-rosa" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#E9C3BE" stop-opacity="0.72"/><stop offset="0.55" stop-color="#C46A75" stop-opacity="0.62"/><stop offset="0.92" stop-color="#7A2C3A" stop-opacity="0.35"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0"/></radialGradient><linearGradient id="l-rosa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E9C3BE" stop-opacity="0.85"/><stop offset="0.7" stop-color="#C46A75" stop-opacity="0.55"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.25"/></linearGradient><radialGradient id="g-rosa2" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F1D6CF" stop-opacity="0.72"/><stop offset="0.55" stop-color="#D08A8A" stop-opacity="0.62"/><stop offset="0.92" stop-color="#8E3F4A" stop-opacity="0.35"/><stop offset="1" stop-color="#8E3F4A" stop-opacity="0"/></radialGradient><linearGradient id="l-rosa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F1D6CF" stop-opacity="0.85"/><stop offset="0.7" stop-color="#D08A8A" stop-opacity="0.55"/><stop offset="1" stop-color="#8E3F4A" stop-opacity="0.25"/></linearGradient><radialGradient id="g-gold" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F5E3B4" stop-opacity="0.72"/><stop offset="0.55" stop-color="#D2A85E" stop-opacity="0.62"/><stop offset="0.92" stop-color="#8A6A2B" stop-opacity="0.35"/><stop offset="1" stop-color="#8A6A2B" stop-opacity="0"/></radialGradient><linearGradient id="l-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F5E3B4" stop-opacity="0.85"/><stop offset="0.7" stop-color="#D2A85E" stop-opacity="0.55"/><stop offset="1" stop-color="#8A6A2B" stop-opacity="0.25"/></linearGradient><radialGradient id="g-salvia" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#C3CFBB" stop-opacity="0.72"/><stop offset="0.55" stop-color="#7F937A" stop-opacity="0.62"/><stop offset="0.92" stop-color="#4F6349" stop-opacity="0.35"/><stop offset="1" stop-color="#4F6349" stop-opacity="0"/></radialGradient><linearGradient id="l-salvia" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C3CFBB" stop-opacity="0.85"/><stop offset="0.7" stop-color="#7F937A" stop-opacity="0.55"/><stop offset="1" stop-color="#4F6349" stop-opacity="0.25"/></linearGradient><radialGradient id="g-salvia2" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#D5DECE" stop-opacity="0.72"/><stop offset="0.55" stop-color="#8FA388" stop-opacity="0.62"/><stop offset="0.92" stop-color="#5A6E55" stop-opacity="0.35"/><stop offset="1" stop-color="#5A6E55" stop-opacity="0"/></radialGradient><linearGradient id="l-salvia2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D5DECE" stop-opacity="0.85"/><stop offset="0.7" stop-color="#8FA388" stop-opacity="0.55"/><stop offset="1" stop-color="#5A6E55" stop-opacity="0.25"/></linearGradient><radialGradient id="g-wine" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#D39AA3" stop-opacity="0.72"/><stop offset="0.55" stop-color="#8E3B4B" stop-opacity="0.62"/><stop offset="0.92" stop-color="#4A1520" stop-opacity="0.35"/><stop offset="1" stop-color="#4A1520" stop-opacity="0"/></radialGradient><linearGradient id="l-wine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D39AA3" stop-opacity="0.85"/><stop offset="0.7" stop-color="#8E3B4B" stop-opacity="0.55"/><stop offset="1" stop-color="#4A1520" stop-opacity="0.25"/></linearGradient><radialGradient id="wash" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#C97B7B" stop-opacity="0.32"/><stop offset="0.6" stop-color="#C97B7B" stop-opacity="0.12"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0"/></radialGradient><radialGradient id="washg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7E9377" stop-opacity="0.3"/><stop offset="0.6" stop-color="#7E9377" stop-opacity="0.1"/><stop offset="1" stop-color="#7E9377" stop-opacity="0"/></radialGradient></defs>
  <ellipse cx="196" cy="128" rx="80" ry="52" fill="url(#wash)"/><ellipse cx="180" cy="138" rx="55" ry="34" fill="url(#washg)"/>
  <ellipse cx="14" cy="14" rx="62" ry="42" fill="url(#wash)" opacity="0.8"/><ellipse cx="30" cy="10" rx="40" ry="26" fill="url(#washg)" opacity="0.8"/>
</svg>
<svg class="aq br" viewBox="0 0 70 70" aria-hidden="true"><defs><radialGradient id="g-rosa" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#E9C3BE" stop-opacity="0.72"/><stop offset="0.55" stop-color="#C46A75" stop-opacity="0.62"/><stop offset="0.92" stop-color="#7A2C3A" stop-opacity="0.35"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0"/></radialGradient><linearGradient id="l-rosa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E9C3BE" stop-opacity="0.85"/><stop offset="0.7" stop-color="#C46A75" stop-opacity="0.55"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.25"/></linearGradient><radialGradient id="g-rosa2" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F1D6CF" stop-opacity="0.72"/><stop offset="0.55" stop-color="#D08A8A" stop-opacity="0.62"/><stop offset="0.92" stop-color="#8E3F4A" stop-opacity="0.35"/><stop offset="1" stop-color="#8E3F4A" stop-opacity="0"/></radialGradient><linearGradient id="l-rosa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F1D6CF" stop-opacity="0.85"/><stop offset="0.7" stop-color="#D08A8A" stop-opacity="0.55"/><stop offset="1" stop-color="#8E3F4A" stop-opacity="0.25"/></linearGradient><radialGradient id="g-gold" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F5E3B4" stop-opacity="0.72"/><stop offset="0.55" stop-color="#D2A85E" stop-opacity="0.62"/><stop offset="0.92" stop-color="#8A6A2B" stop-opacity="0.35"/><stop offset="1" stop-color="#8A6A2B" stop-opacity="0"/></radialGradient><linearGradient id="l-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F5E3B4" stop-opacity="0.85"/><stop offset="0.7" stop-color="#D2A85E" stop-opacity="0.55"/><stop offset="1" stop-color="#8A6A2B" stop-opacity="0.25"/></linearGradient><radialGradient id="g-salvia" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#C3CFBB" stop-opacity="0.72"/><stop offset="0.55" stop-color="#7F937A" stop-opacity="0.62"/><stop offset="0.92" stop-color="#4F6349" stop-opacity="0.35"/><stop offset="1" stop-color="#4F6349" stop-opacity="0"/></radialGradient><linearGradient id="l-salvia" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C3CFBB" stop-opacity="0.85"/><stop offset="0.7" stop-color="#7F937A" stop-opacity="0.55"/><stop offset="1" stop-color="#4F6349" stop-opacity="0.25"/></linearGradient><radialGradient id="g-salvia2" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#D5DECE" stop-opacity="0.72"/><stop offset="0.55" stop-color="#8FA388" stop-opacity="0.62"/><stop offset="0.92" stop-color="#5A6E55" stop-opacity="0.35"/><stop offset="1" stop-color="#5A6E55" stop-opacity="0"/></radialGradient><linearGradient id="l-salvia2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D5DECE" stop-opacity="0.85"/><stop offset="0.7" stop-color="#8FA388" stop-opacity="0.55"/><stop offset="1" stop-color="#5A6E55" stop-opacity="0.25"/></linearGradient><radialGradient id="g-wine" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#D39AA3" stop-opacity="0.72"/><stop offset="0.55" stop-color="#8E3B4B" stop-opacity="0.62"/><stop offset="0.92" stop-color="#4A1520" stop-opacity="0.35"/><stop offset="1" stop-color="#4A1520" stop-opacity="0"/></radialGradient><linearGradient id="l-wine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D39AA3" stop-opacity="0.85"/><stop offset="0.7" stop-color="#8E3B4B" stop-opacity="0.55"/><stop offset="1" stop-color="#4A1520" stop-opacity="0.25"/></linearGradient><radialGradient id="wash" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#C97B7B" stop-opacity="0.32"/><stop offset="0.6" stop-color="#C97B7B" stop-opacity="0.12"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0"/></radialGradient><radialGradient id="washg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7E9377" stop-opacity="0.3"/><stop offset="0.6" stop-color="#7E9377" stop-opacity="0.1"/><stop offset="1" stop-color="#7E9377" stop-opacity="0"/></radialGradient></defs><path d="M6.0 62.0 14.0 50.0 24.0 40.0 38.0 30.0" fill="none" stroke="#6F8468" stroke-width="0.9" stroke-linecap="round" opacity="0.75"/><path d="M18.0 60.0 26.0 48.0 40.0 42.0" fill="none" stroke="#6F8468" stroke-width="0.9" stroke-linecap="round" opacity="0.75"/><path d="M30.0 64.0 36.0 52.0 46.0 48.0" fill="none" stroke="#6F8468" stroke-width="0.9" stroke-linecap="round" opacity="0.75"/><g transform="translate(12.0 54.0) rotate(-40)"><path d="M0 0 C 4.97 -3.99, 5.97 -9.98, 0.01 -14.00 C -5.43 -9.13, -5.06 -4.07, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -11.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(20.0 46.0) rotate(20)"><path d="M0 0 C 5.87 -3.69, 5.34 -9.47, 0.27 -15.00 C -6.00 -9.32, -6.18 -4.79, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -12.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(26.0 44.0) rotate(-60)"><path d="M0 0 C 4.90 -3.77, 4.41 -8.00, 0.02 -13.00 C -4.26 -8.49, -4.32 -3.13, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -10.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(33.0 36.0) rotate(25)"><path d="M0 0 C 4.99 -3.85, 5.84 -10.14, 0.11 -14.00 C -5.29 -10.57, -4.98 -3.66, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -11.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(40.0 44.0) rotate(-30)"><path d="M0 0 C 4.96 -3.86, 5.00 -9.18, -0.13 -12.00 C -4.17 -8.09, -3.76 -3.63, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -9.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(46.0 50.0) rotate(40)"><path d="M0 0 C 4.54 -4.02, 4.75 -10.65, 0.26 -13.00 C -4.18 -8.54, -5.26 -3.61, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -10.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(30.0 58.0) rotate(60)"><path d="M0 0 C 4.53 -2.99, 3.63 -8.23, 0.18 -11.00 C -3.87 -6.94, -3.76 -3.51, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -8.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(50.0 42.0) rotate(-20)"><path d="M0 0 C 3.88 -2.48, 3.49 -6.34, -0.25 -10.00 C -4.12 -6.50, -3.66 -2.76, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -7.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(24.0 56.0) rotate(-85)"><path d="M0 0 C 2.94 -2.70, 3.03 -6.76, -0.20 -9.00 C -3.32 -5.92, -3.02 -2.88, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -6.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(40.0 28.0) rotate(10)"><path d="M0 0 C 7.25 -3.69, 6.61 -11.50, 0.15 -14.44 C -6.01 -11.92, -5.94 -3.75, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(6.1)"/><path d="M0 0 C 6.10 -3.54, 5.99 -10.70, -0.27 -14.51 C -7.03 -10.04, -6.41 -4.62, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(45.5)"/><path d="M0 0 C 7.21 -3.84, 6.12 -12.24, 0.33 -15.14 C -6.31 -9.89, -6.97 -4.80, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(79.7)"/><path d="M0 0 C 7.25 -4.65, 6.66 -10.23, -0.48 -16.12 C -7.77 -10.70, -6.90 -4.18, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(113.9)"/><path d="M0 0 C 6.10 -3.84, 7.28 -9.53, -0.28 -15.20 C -6.95 -12.10, -6.72 -3.98, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(166.5)"/><path d="M0 0 C 5.56 -3.70, 6.71 -8.86, -0.34 -14.18 C -6.56 -10.43, -5.78 -3.81, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(208.3)"/><path d="M0 0 C 6.81 -4.80, 7.00 -10.41, -0.48 -16.20 C -5.84 -13.10, -6.89 -5.17, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(247.8)"/><path d="M0 0 C 6.47 -4.58, 6.45 -12.67, -0.44 -15.30 C -6.92 -11.80, -7.28 -4.59, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(270.4)"/><path d="M0 0 C 7.31 -4.20, 7.20 -12.67, 0.39 -15.71 C -6.66 -12.30, -7.21 -4.50, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(324.1)"/><path d="M0 0 C 5.60 -3.48, 5.01 -9.03, 0.43 -12.04 C -6.39 -9.27, -5.28 -3.61, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(2.0)"/><path d="M0 0 C 6.01 -2.99, 6.16 -7.54, 0.09 -12.20 C -5.70 -8.07, -5.78 -3.41, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(41.3)"/><path d="M0 0 C 5.06 -3.21, 5.39 -10.20, -0.26 -13.44 C -5.16 -10.86, -5.72 -3.70, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(81.8)"/><path d="M0 0 C 5.73 -3.03, 5.61 -9.35, 0.36 -11.90 C -6.39 -8.27, -5.60 -3.15, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(126.3)"/><path d="M0 0 C 6.01 -3.82, 6.10 -10.08, -0.19 -12.34 C -5.16 -8.75, -5.09 -3.16, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(154.2)"/><path d="M0 0 C 5.45 -3.35, 6.32 -10.45, -0.04 -12.68 C -5.00 -7.84, -6.07 -3.06, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(198.6)"/><path d="M0 0 C 5.15 -3.82, 4.91 -8.04, -0.04 -12.53 C -4.92 -9.92, -5.03 -3.13, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(243.3)"/><path d="M0 0 C 5.37 -3.69, 6.00 -9.98, 0.40 -12.69 C -6.05 -8.31, -5.42 -3.21, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(272.8)"/><path d="M0 0 C 5.81 -3.11, 5.34 -8.43, 0.17 -12.28 C -5.77 -9.14, -5.88 -3.33, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(312.2)"/><path d="M0 0 C 3.42 -2.50, 4.37 -5.07, -0.03 -7.91 C -4.25 -6.40, -3.76 -2.26, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(18.5)"/><path d="M0 0 C 4.42 -2.14, 4.28 -5.08, 0.14 -7.74 C -4.49 -5.81, -4.15 -1.98, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(79.6)"/><path d="M0 0 C 4.46 -2.27, 4.45 -5.47, 0.26 -8.03 C -4.53 -5.52, -3.41 -2.21, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(139.8)"/><path d="M0 0 C 3.89 -1.85, 4.47 -4.82, 0.19 -7.70 C -3.69 -5.27, -4.24 -1.92, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(195.6)"/><path d="M0 0 C 4.16 -2.25, 4.33 -5.96, -0.00 -7.31 C -4.65 -4.61, -3.57 -2.06, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(250.8)"/><path d="M0 0 C 4.06 -2.15, 4.52 -5.60, -0.12 -7.64 C -3.95 -6.07, -4.37 -1.95, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(312.5)"/><circle r="1.8" fill="#E8C27A" opacity="0.75"/><circle cx="3.8" cy="0.5" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="2.3" cy="2.4" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="0.3" cy="3.3" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.4" cy="2.4" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="-3.8" cy="0.6" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.2" cy="-2.2" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="0.3" cy="-3.3" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="2.5" cy="-2.5" r="0.58" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(22.0 40.0) rotate(-30)"><path d="M0 0 C 4.63 -3.50, 5.62 -7.37, -0.02 -11.00 C -4.43 -7.76, -5.20 -3.45, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(-8.7)"/><path d="M0 0 C 4.31 -3.07, 5.62 -6.77, 0.21 -10.58 C -4.27 -6.92, -4.36 -3.13, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(39.5)"/><path d="M0 0 C 4.92 -2.63, 5.33 -6.80, 0.01 -10.65 C -4.61 -6.97, -4.79 -2.93, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(76.4)"/><path d="M0 0 C 4.79 -2.71, 4.55 -8.05, 0.11 -10.76 C -5.03 -8.56, -4.91 -3.34, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(117.5)"/><path d="M0 0 C 5.19 -3.57, 4.71 -7.74, 0.32 -11.38 C -4.57 -9.42, -5.30 -2.84, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(154.7)"/><path d="M0 0 C 4.41 -2.80, 5.48 -7.98, 0.22 -11.36 C -4.43 -7.94, -5.01 -2.72, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(194.8)"/><path d="M0 0 C 5.34 -3.60, 4.41 -8.13, 0.20 -11.27 C -4.99 -8.57, -4.31 -2.75, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(234.0)"/><path d="M0 0 C 4.82 -2.83, 5.09 -6.47, -0.24 -10.05 C -4.54 -7.97, -5.45 -3.17, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(272.1)"/><path d="M0 0 C 5.39 -2.79, 5.38 -6.89, -0.03 -10.09 C -5.01 -7.11, -4.89 -2.41, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(311.9)"/><path d="M0 0 C 3.61 -2.67, 4.49 -6.77, -0.19 -9.68 C -3.77 -7.00, -3.41 -3.03, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(3.2)"/><path d="M0 0 C 4.42 -2.74, 4.07 -6.98, 0.00 -9.41 C -4.80 -7.40, -3.70 -2.96, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(44.8)"/><path d="M0 0 C 4.37 -2.60, 4.69 -7.66, 0.12 -9.55 C -4.53 -7.43, -3.88 -2.85, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(83.9)"/><path d="M0 0 C 3.95 -2.08, 4.01 -6.54, 0.08 -8.72 C -3.85 -7.12, -4.19 -2.32, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(113.1)"/><path d="M0 0 C 4.03 -2.48, 4.82 -6.87, 0.13 -9.16 C -4.52 -7.54, -3.42 -2.65, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(162.6)"/><path d="M0 0 C 3.87 -2.07, 3.81 -5.94, -0.26 -8.56 C -3.88 -6.92, -4.05 -2.40, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(203.8)"/><path d="M0 0 C 4.58 -2.67, 4.58 -5.75, 0.06 -9.15 C -4.52 -5.69, -4.50 -2.30, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(247.5)"/><path d="M0 0 C 3.98 -2.43, 3.63 -6.85, -0.05 -8.40 C -4.22 -6.22, -3.83 -2.20, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(279.5)"/><path d="M0 0 C 3.73 -2.73, 3.93 -5.62, -0.16 -9.14 C -3.61 -5.90, -4.29 -2.47, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(322.5)"/><path d="M0 0 C 2.47 -1.80, 3.39 -3.52, 0.18 -5.60 C -2.93 -4.01, -3.25 -1.45, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(19.8)"/><path d="M0 0 C 3.04 -1.61, 3.42 -4.59, 0.05 -5.82 C -2.65 -4.35, -2.81 -1.48, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(75.3)"/><path d="M0 0 C 2.53 -1.47, 3.14 -3.80, -0.11 -5.35 C -3.07 -3.76, -3.09 -1.51, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(129.6)"/><path d="M0 0 C 3.05 -1.51, 2.65 -4.70, 0.13 -5.84 C -3.10 -4.02, -2.65 -1.72, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(201.0)"/><path d="M0 0 C 2.96 -1.63, 2.71 -3.61, 0.22 -5.42 C -3.37 -4.35, -2.46 -1.32, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(255.8)"/><path d="M0 0 C 2.96 -1.29, 3.03 -3.29, -0.19 -5.23 C -3.15 -3.83, -2.96 -1.41, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(312.3)"/><circle r="1.3" fill="#E8C27A" opacity="0.75"/><circle cx="2.1" cy="-0.0" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="1.9" cy="1.7" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-0.2" cy="2.0" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-1.6" cy="2.1" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-2.6" cy="-0.1" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-1.8" cy="-1.5" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-0.2" cy="-2.7" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="1.7" cy="-1.9" r="0.43" fill="#8E3F4A" opacity="0.7"/></g><g transform="translate(50.0 46.0) rotate(50)"><path d="M0 0 C 3.55 -2.35, 4.14 -5.50, -0.07 -7.81 C -3.23 -6.25, -3.06 -1.91, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(9.8)"/><path d="M0 0 C 3.69 -2.11, 3.98 -5.05, -0.16 -8.03 C -3.85 -5.06, -3.29 -2.40, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(46.3)"/><path d="M0 0 C 3.13 -2.08, 3.92 -5.35, -0.21 -7.75 C -3.91 -5.69, -3.94 -2.46, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(93.9)"/><path d="M0 0 C 3.82 -2.10, 3.47 -5.56, 0.24 -7.96 C -4.11 -5.30, -3.35 -2.14, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(143.3)"/><path d="M0 0 C 3.38 -2.01, 3.75 -6.20, 0.02 -7.90 C -4.05 -5.80, -3.16 -2.39, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(177.3)"/><path d="M0 0 C 3.00 -2.18, 3.72 -5.69, 0.26 -7.74 C -3.84 -6.08, -3.04 -2.20, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(232.6)"/><path d="M0 0 C 3.06 -2.24, 4.11 -4.71, 0.08 -7.47 C -3.28 -5.77, -3.66 -1.93, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(275.8)"/><path d="M0 0 C 3.52 -2.55, 3.56 -5.77, 0.26 -8.42 C -3.87 -6.05, -3.54 -2.51, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(309.4)"/><path d="M0 0 C 2.86 -2.22, 3.24 -5.76, 0.14 -7.23 C -3.40 -5.81, -3.34 -2.11, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(3.3)"/><path d="M0 0 C 3.21 -1.90, 3.01 -4.47, 0.11 -6.94 C -3.54 -4.81, -2.65 -1.77, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(45.4)"/><path d="M0 0 C 3.35 -1.55, 2.91 -4.05, 0.07 -6.36 C -3.34 -4.14, -2.55 -1.76, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(88.8)"/><path d="M0 0 C 2.53 -1.79, 2.79 -4.76, -0.12 -7.22 C -3.29 -5.35, -2.70 -1.83, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(136.3)"/><path d="M0 0 C 3.17 -1.64, 3.13 -4.88, -0.01 -6.19 C -2.87 -4.98, -3.31 -1.65, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(176.5)"/><path d="M0 0 C 2.92 -1.87, 2.67 -5.95, 0.14 -7.29 C -2.98 -5.29, -2.95 -1.90, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(225.8)"/><path d="M0 0 C 2.71 -1.64, 3.06 -4.76, 0.14 -6.87 C -3.28 -5.10, -2.64 -1.73, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(277.8)"/><path d="M0 0 C 3.27 -1.78, 3.21 -5.22, -0.11 -6.31 C -3.12 -4.07, -3.18 -1.50, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(312.1)"/><path d="M0 0 C 2.30 -1.03, 2.05 -3.23, -0.14 -4.21 C -2.19 -3.00, -2.39 -1.21, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(18.9)"/><path d="M0 0 C 2.28 -1.03, 2.48 -2.37, 0.11 -3.76 C -2.01 -2.74, -2.12 -0.94, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(79.3)"/><path d="M0 0 C 1.98 -0.92, 2.08 -2.68, 0.07 -3.76 C -2.11 -2.86, -1.85 -1.02, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(139.0)"/><path d="M0 0 C 2.31 -1.26, 1.88 -2.99, 0.07 -4.31 C -2.03 -3.16, -2.07 -1.03, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(194.5)"/><path d="M0 0 C 1.92 -1.21, 2.07 -2.89, 0.01 -4.17 C -2.07 -2.86, -2.03 -1.23, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(260.9)"/><path d="M0 0 C 2.25 -0.97, 2.50 -2.69, 0.08 -3.67 C -2.09 -2.90, -1.84 -0.92, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(312.1)"/><circle r="1.0" fill="#E8C27A" opacity="0.75"/><circle cx="1.9" cy="-0.3" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="1.0" cy="1.2" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="0.1" cy="2.0" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-1.1" cy="1.0" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-1.5" cy="0.1" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-1.3" cy="-1.0" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-0.3" cy="-2.0" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="1.2" cy="-1.3" r="0.32" fill="#8A6A2B" opacity="0.7"/></g><g transform="translate(58.0 32.0) rotate(0)"><path d="M0 0 C 3.01 -1.79, 2.74 -4.64, -0.21 -6.62 C -2.80 -5.05, -3.15 -2.01, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(2.9)"/><path d="M0 0 C 2.35 -1.71, 2.75 -4.85, -0.17 -6.44 C -2.78 -4.65, -2.99 -1.98, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(54.6)"/><path d="M0 0 C 2.97 -1.87, 2.93 -4.09, 0.00 -5.95 C -2.58 -4.56, -3.15 -1.67, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(105.1)"/><path d="M0 0 C 2.50 -2.12, 3.00 -4.38, -0.18 -6.69 C -2.67 -4.93, -2.91 -1.78, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(158.6)"/><path d="M0 0 C 2.72 -1.53, 3.30 -3.96, 0.18 -6.17 C -2.93 -4.53, -2.80 -1.61, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(214.3)"/><path d="M0 0 C 3.01 -1.98, 2.56 -5.43, -0.09 -6.87 C -3.23 -4.56, -2.81 -2.11, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(265.3)"/><path d="M0 0 C 2.40 -1.54, 2.61 -5.26, 0.19 -6.38 C -3.02 -4.33, -2.89 -1.91, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(302.3)"/><path d="M0 0 C 2.52 -1.27, 2.21 -3.80, -0.13 -5.33 C -2.34 -3.91, -2.08 -1.50, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(-1.9)"/><path d="M0 0 C 2.19 -1.55, 2.09 -4.01, -0.13 -5.30 C -2.76 -3.93, -2.29 -1.44, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(47.6)"/><path d="M0 0 C 2.49 -1.64, 2.42 -4.49, 0.13 -5.43 C -2.68 -3.81, -2.26 -1.55, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(104.8)"/><path d="M0 0 C 2.33 -1.44, 2.72 -3.58, -0.16 -5.25 C -2.59 -4.24, -2.47 -1.51, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(160.8)"/><path d="M0 0 C 2.37 -1.22, 2.15 -3.55, 0.00 -5.01 C -2.35 -3.12, -2.45 -1.41, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(209.7)"/><path d="M0 0 C 2.24 -1.29, 2.11 -4.05, 0.17 -5.01 C -2.55 -4.01, -2.26 -1.53, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(253.0)"/><path d="M0 0 C 2.36 -1.73, 2.13 -4.30, -0.14 -5.50 C -2.45 -4.49, -1.96 -1.42, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(304.1)"/><path d="M0 0 C 1.43 -0.93, 1.90 -2.07, -0.04 -2.96 C -1.78 -1.84, -1.42 -0.93, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(12.6)"/><path d="M0 0 C 1.86 -0.99, 1.72 -2.02, -0.05 -3.08 C -1.95 -2.48, -1.50 -0.95, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(72.7)"/><path d="M0 0 C 1.49 -0.95, 1.99 -2.01, 0.03 -3.06 C -1.57 -2.46, -1.43 -0.76, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(133.2)"/><path d="M0 0 C 1.85 -0.92, 1.84 -1.90, 0.05 -2.96 C -1.96 -2.09, -1.44 -0.76, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(197.7)"/><path d="M0 0 C 1.50 -0.82, 1.59 -2.43, 0.08 -3.22 C -1.67 -2.43, -1.84 -0.93, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(252.7)"/><path d="M0 0 C 1.86 -0.87, 1.62 -2.21, -0.11 -2.95 C -1.98 -2.09, -1.66 -0.83, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(311.7)"/><circle r="0.8" fill="#E8C27A" opacity="0.75"/><circle cx="1.4" cy="-0.2" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="0.9" cy="0.8" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-0.1" cy="1.1" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-1.0" cy="1.1" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-1.2" cy="0.1" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-0.8" cy="-0.9" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="0.2" cy="-1.6" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="0.8" cy="-1.1" r="0.25" fill="#4A1520" opacity="0.7"/></g><circle cx="14" cy="60" r="1.1" fill="#E8C27A" opacity="0.7"/><circle cx="52" cy="58" r="0.8" fill="#E8C27A" opacity="0.7"/><circle cx="60" cy="22" r="1.2" fill="#E8C27A" opacity="0.7"/><circle cx="30" cy="24" r="0.9" fill="#E8C27A" opacity="0.7"/><circle cx="8" cy="44" r="0.7" fill="#E8C27A" opacity="0.7"/></svg>
<svg class="aq tl" viewBox="0 0 70 70" aria-hidden="true"><defs><radialGradient id="g-rosa" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#E9C3BE" stop-opacity="0.72"/><stop offset="0.55" stop-color="#C46A75" stop-opacity="0.62"/><stop offset="0.92" stop-color="#7A2C3A" stop-opacity="0.35"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0"/></radialGradient><linearGradient id="l-rosa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E9C3BE" stop-opacity="0.85"/><stop offset="0.7" stop-color="#C46A75" stop-opacity="0.55"/><stop offset="1" stop-color="#7A2C3A" stop-opacity="0.25"/></linearGradient><radialGradient id="g-rosa2" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F1D6CF" stop-opacity="0.72"/><stop offset="0.55" stop-color="#D08A8A" stop-opacity="0.62"/><stop offset="0.92" stop-color="#8E3F4A" stop-opacity="0.35"/><stop offset="1" stop-color="#8E3F4A" stop-opacity="0"/></radialGradient><linearGradient id="l-rosa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F1D6CF" stop-opacity="0.85"/><stop offset="0.7" stop-color="#D08A8A" stop-opacity="0.55"/><stop offset="1" stop-color="#8E3F4A" stop-opacity="0.25"/></linearGradient><radialGradient id="g-gold" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F5E3B4" stop-opacity="0.72"/><stop offset="0.55" stop-color="#D2A85E" stop-opacity="0.62"/><stop offset="0.92" stop-color="#8A6A2B" stop-opacity="0.35"/><stop offset="1" stop-color="#8A6A2B" stop-opacity="0"/></radialGradient><linearGradient id="l-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F5E3B4" stop-opacity="0.85"/><stop offset="0.7" stop-color="#D2A85E" stop-opacity="0.55"/><stop offset="1" stop-color="#8A6A2B" stop-opacity="0.25"/></linearGradient><radialGradient id="g-salvia" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#C3CFBB" stop-opacity="0.72"/><stop offset="0.55" stop-color="#7F937A" stop-opacity="0.62"/><stop offset="0.92" stop-color="#4F6349" stop-opacity="0.35"/><stop offset="1" stop-color="#4F6349" stop-opacity="0"/></radialGradient><linearGradient id="l-salvia" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C3CFBB" stop-opacity="0.85"/><stop offset="0.7" stop-color="#7F937A" stop-opacity="0.55"/><stop offset="1" stop-color="#4F6349" stop-opacity="0.25"/></linearGradient><radialGradient id="g-salvia2" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#D5DECE" stop-opacity="0.72"/><stop offset="0.55" stop-color="#8FA388" stop-opacity="0.62"/><stop offset="0.92" stop-color="#5A6E55" stop-opacity="0.35"/><stop offset="1" stop-color="#5A6E55" stop-opacity="0"/></radialGradient><linearGradient id="l-salvia2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D5DECE" stop-opacity="0.85"/><stop offset="0.7" stop-color="#8FA388" stop-opacity="0.55"/><stop offset="1" stop-color="#5A6E55" stop-opacity="0.25"/></linearGradient><radialGradient id="g-wine" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#D39AA3" stop-opacity="0.72"/><stop offset="0.55" stop-color="#8E3B4B" stop-opacity="0.62"/><stop offset="0.92" stop-color="#4A1520" stop-opacity="0.35"/><stop offset="1" stop-color="#4A1520" stop-opacity="0"/></radialGradient><linearGradient id="l-wine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D39AA3" stop-opacity="0.85"/><stop offset="0.7" stop-color="#8E3B4B" stop-opacity="0.55"/><stop offset="1" stop-color="#4A1520" stop-opacity="0.25"/></linearGradient><radialGradient id="wash" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#C97B7B" stop-opacity="0.32"/><stop offset="0.6" stop-color="#C97B7B" stop-opacity="0.12"/><stop offset="1" stop-color="#C97B7B" stop-opacity="0"/></radialGradient><radialGradient id="washg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7E9377" stop-opacity="0.3"/><stop offset="0.6" stop-color="#7E9377" stop-opacity="0.1"/><stop offset="1" stop-color="#7E9377" stop-opacity="0"/></radialGradient></defs><path d="M6.0 62.0 14.0 50.0 24.0 40.0 38.0 30.0" fill="none" stroke="#6F8468" stroke-width="0.9" stroke-linecap="round" opacity="0.75"/><path d="M18.0 60.0 26.0 48.0 40.0 42.0" fill="none" stroke="#6F8468" stroke-width="0.9" stroke-linecap="round" opacity="0.75"/><path d="M30.0 64.0 36.0 52.0 46.0 48.0" fill="none" stroke="#6F8468" stroke-width="0.9" stroke-linecap="round" opacity="0.75"/><g transform="translate(12.0 54.0) rotate(-40)"><path d="M0 0 C 5.12 -4.09, 5.07 -10.56, 0.23 -14.00 C -5.32 -10.10, -5.56 -4.14, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -11.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(20.0 46.0) rotate(20)"><path d="M0 0 C 5.43 -4.77, 5.12 -11.71, -0.29 -15.00 C -5.85 -9.94, -5.30 -4.54, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -12.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(26.0 44.0) rotate(-60)"><path d="M0 0 C 5.08 -3.96, 4.52 -9.33, -0.21 -13.00 C -5.03 -9.36, -4.03 -3.75, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -10.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(33.0 36.0) rotate(25)"><path d="M0 0 C 5.36 -4.01, 5.88 -9.11, -0.28 -14.00 C -4.53 -10.07, -4.94 -3.85, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -11.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(40.0 44.0) rotate(-30)"><path d="M0 0 C 4.01 -3.66, 3.95 -9.70, 0.05 -12.00 C -4.59 -9.40, -3.98 -3.00, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -9.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(46.0 50.0) rotate(40)"><path d="M0 0 C 4.41 -3.14, 4.64 -9.70, 0.02 -13.00 C -4.57 -9.61, -4.10 -3.99, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -10.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(30.0 58.0) rotate(60)"><path d="M0 0 C 3.57 -2.85, 3.73 -8.37, 0.21 -11.00 C -4.52 -6.88, -3.85 -2.95, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -8.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(50.0 42.0) rotate(-20)"><path d="M0 0 C 3.29 -3.20, 3.26 -7.18, 0.15 -10.00 C -4.33 -6.43, -3.55 -3.01, 0 0 z" fill="url(#l-salvia2)" stroke="#5A6E55" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -7.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(24.0 56.0) rotate(-85)"><path d="M0 0 C 2.79 -2.32, 3.80 -5.78, -0.06 -9.00 C -3.20 -6.33, -2.83 -2.17, 0 0 z" fill="url(#l-salvia)" stroke="#4F6349" stroke-width="0.12" stroke-opacity="0.35"/><path d="M0 -1.5 L0 -6.5" stroke="#F9F5EE" stroke-width="0.3" opacity="0.4"/></g><g transform="translate(40.0 28.0) rotate(10)"><path d="M0 0 C 6.96 -4.02, 6.32 -11.43, -0.27 -15.63 C -6.75 -12.72, -6.23 -4.16, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(9.9)"/><path d="M0 0 C 5.60 -4.14, 7.13 -9.52, -0.16 -15.24 C -7.22 -12.17, -6.68 -4.76, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(49.6)"/><path d="M0 0 C 7.17 -3.96, 7.40 -9.66, -0.16 -14.67 C -6.18 -10.72, -5.84 -3.74, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(79.3)"/><path d="M0 0 C 6.13 -4.10, 7.84 -11.28, 0.38 -14.87 C -6.22 -10.33, -5.67 -4.40, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(114.3)"/><path d="M0 0 C 5.56 -3.64, 6.34 -10.01, 0.44 -14.36 C -7.27 -9.62, -6.23 -3.60, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(157.3)"/><path d="M0 0 C 7.02 -4.36, 7.66 -8.99, -0.19 -14.59 C -6.59 -9.19, -7.25 -3.87, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(208.7)"/><path d="M0 0 C 5.63 -4.07, 6.29 -9.31, -0.36 -15.00 C -7.02 -9.28, -6.13 -4.10, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(245.4)"/><path d="M0 0 C 6.90 -3.64, 7.29 -10.59, -0.37 -14.00 C -6.22 -9.42, -6.91 -3.81, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(280.9)"/><path d="M0 0 C 5.97 -4.17, 6.51 -10.47, -0.48 -15.90 C -5.85 -11.90, -6.63 -4.86, 0 0 z" fill="url(#g-rosa)" opacity="0.45" transform="rotate(317.7)"/><path d="M0 0 C 5.74 -3.73, 5.24 -9.00, 0.15 -11.83 C -6.52 -9.45, -5.03 -3.44, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(7.6)"/><path d="M0 0 C 5.28 -2.96, 5.53 -8.31, -0.00 -12.16 C -5.35 -7.86, -5.30 -3.38, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(33.4)"/><path d="M0 0 C 5.03 -3.14, 5.46 -8.99, -0.31 -12.78 C -5.88 -9.76, -5.55 -3.79, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(74.7)"/><path d="M0 0 C 5.24 -2.94, 5.57 -7.53, -0.00 -12.07 C -5.88 -8.61, -5.17 -3.13, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(112.4)"/><path d="M0 0 C 6.10 -3.41, 5.32 -9.04, -0.27 -11.95 C -5.68 -8.90, -6.20 -3.21, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(152.4)"/><path d="M0 0 C 5.90 -3.92, 5.94 -9.46, -0.07 -13.50 C -5.35 -10.68, -6.08 -3.65, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(201.2)"/><path d="M0 0 C 4.86 -3.13, 5.40 -7.69, 0.42 -11.15 C -5.13 -7.29, -5.02 -3.29, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(246.6)"/><path d="M0 0 C 5.53 -3.00, 5.28 -7.94, 0.13 -11.05 C -5.82 -8.25, -5.56 -3.40, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(275.8)"/><path d="M0 0 C 5.21 -3.72, 5.41 -9.14, 0.17 -11.92 C -6.05 -9.77, -5.99 -3.00, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(327.5)"/><path d="M0 0 C 3.97 -1.95, 3.83 -5.62, 0.02 -7.27 C -3.77 -4.84, -3.70 -1.84, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(16.5)"/><path d="M0 0 C 3.39 -1.63, 3.61 -5.12, -0.24 -6.70 C -4.04 -5.22, -3.88 -1.69, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(75.2)"/><path d="M0 0 C 3.38 -2.04, 4.10 -6.16, -0.07 -7.86 C -4.36 -5.24, -4.15 -2.09, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(139.4)"/><path d="M0 0 C 4.30 -2.36, 4.18 -5.40, 0.13 -7.68 C -4.25 -6.08, -4.25 -1.91, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(193.0)"/><path d="M0 0 C 3.59 -1.91, 3.50 -5.57, 0.28 -7.54 C -4.67 -4.84, -4.12 -2.06, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(253.5)"/><path d="M0 0 C 4.41 -2.29, 3.54 -5.45, -0.24 -7.12 C -3.53 -4.80, -4.17 -2.29, 0 0 z" fill="url(#g-rosa)" stroke="#7A2C3A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(316.6)"/><circle r="1.8" fill="#E8C27A" opacity="0.75"/><circle cx="3.0" cy="-0.4" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="2.7" cy="1.9" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="0.0" cy="3.1" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.4" cy="2.7" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.9" cy="-0.4" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="-2.5" cy="-2.3" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="0.4" cy="-3.9" r="0.58" fill="#7A2C3A" opacity="0.7"/><circle cx="2.4" cy="-2.6" r="0.58" fill="#7A2C3A" opacity="0.7"/></g><g transform="translate(22.0 40.0) rotate(-30)"><path d="M0 0 C 4.25 -2.90, 4.40 -9.35, -0.19 -11.50 C -4.97 -7.33, -4.50 -2.75, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(0.9)"/><path d="M0 0 C 4.93 -2.67, 4.58 -7.34, -0.10 -10.25 C -4.63 -6.39, -4.13 -3.21, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(41.3)"/><path d="M0 0 C 4.30 -2.82, 5.73 -6.64, 0.28 -10.12 C -4.96 -7.10, -5.19 -2.75, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(76.2)"/><path d="M0 0 C 4.97 -3.20, 4.65 -8.98, 0.28 -11.02 C -5.73 -7.80, -5.23 -3.29, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(111.2)"/><path d="M0 0 C 4.28 -2.49, 4.35 -6.91, 0.19 -10.03 C -4.70 -7.25, -4.05 -2.56, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(153.5)"/><path d="M0 0 C 4.79 -3.06, 5.42 -7.71, -0.08 -10.00 C -5.44 -7.90, -5.13 -3.21, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(209.2)"/><path d="M0 0 C 4.61 -3.50, 4.61 -9.52, -0.36 -11.78 C -5.10 -7.79, -4.59 -3.17, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(232.0)"/><path d="M0 0 C 4.56 -3.36, 4.77 -7.74, 0.31 -11.52 C -4.72 -7.28, -4.51 -3.46, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(283.1)"/><path d="M0 0 C 4.82 -3.36, 4.50 -7.23, -0.27 -11.39 C -4.76 -8.03, -4.05 -3.19, 0 0 z" fill="url(#g-rosa2)" opacity="0.45" transform="rotate(314.2)"/><path d="M0 0 C 4.03 -2.76, 3.82 -6.97, -0.11 -8.69 C -4.51 -5.52, -4.57 -2.38, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(-1.5)"/><path d="M0 0 C 3.88 -2.52, 3.78 -5.70, 0.11 -8.49 C -4.75 -5.79, -3.61 -2.28, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(47.4)"/><path d="M0 0 C 4.15 -2.25, 4.37 -5.50, 0.07 -8.36 C -4.68 -6.66, -4.14 -2.34, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(87.8)"/><path d="M0 0 C 4.39 -2.45, 4.13 -6.27, -0.05 -8.29 C -4.04 -5.49, -4.11 -2.37, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(121.1)"/><path d="M0 0 C 4.14 -2.24, 4.31 -6.02, 0.28 -8.14 C -3.75 -5.80, -4.58 -2.44, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(160.2)"/><path d="M0 0 C 4.58 -2.58, 4.65 -6.06, 0.31 -9.47 C -4.18 -6.28, -4.40 -2.77, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(197.0)"/><path d="M0 0 C 4.35 -2.71, 4.81 -6.04, 0.24 -9.65 C -4.46 -6.43, -4.36 -2.66, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(247.0)"/><path d="M0 0 C 3.63 -2.54, 4.37 -6.10, 0.04 -9.72 C -4.55 -6.98, -3.68 -2.97, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(280.6)"/><path d="M0 0 C 4.05 -3.00, 4.56 -6.15, -0.09 -9.54 C -3.69 -5.91, -3.81 -2.96, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(325.7)"/><path d="M0 0 C 2.58 -1.32, 3.31 -3.64, 0.18 -4.88 C -2.61 -4.03, -2.60 -1.42, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(19.0)"/><path d="M0 0 C 2.59 -1.64, 2.93 -3.43, -0.07 -5.58 C -2.83 -4.17, -2.66 -1.61, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(79.5)"/><path d="M0 0 C 2.53 -1.47, 2.96 -3.17, -0.18 -4.96 C -3.39 -3.69, -2.73 -1.26, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(137.3)"/><path d="M0 0 C 3.05 -1.49, 2.82 -3.88, -0.16 -5.54 C -3.11 -3.90, -3.12 -1.51, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(200.9)"/><path d="M0 0 C 3.23 -1.42, 3.18 -3.53, 0.04 -5.33 C -2.80 -4.26, -2.67 -1.65, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(254.5)"/><path d="M0 0 C 3.22 -1.43, 3.21 -3.91, -0.02 -5.27 C -2.60 -3.70, -2.66 -1.45, 0 0 z" fill="url(#g-rosa2)" stroke="#8E3F4A" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(317.1)"/><circle r="1.3" fill="#E8C27A" opacity="0.75"/><circle cx="2.2" cy="0.3" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="1.7" cy="1.9" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="0.2" cy="2.3" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-1.7" cy="2.2" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-2.3" cy="0.2" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="-2.0" cy="-1.8" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="0.3" cy="-2.4" r="0.43" fill="#8E3F4A" opacity="0.7"/><circle cx="1.4" cy="-1.4" r="0.43" fill="#8E3F4A" opacity="0.7"/></g><g transform="translate(50.0 46.0) rotate(50)"><path d="M0 0 C 3.36 -2.01, 3.92 -5.65, -0.09 -7.47 C -4.11 -6.11, -3.00 -2.18, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(7.9)"/><path d="M0 0 C 3.46 -2.08, 3.86 -5.84, 0.26 -7.86 C -4.20 -6.49, -3.39 -2.42, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(44.4)"/><path d="M0 0 C 4.02 -2.03, 3.63 -5.82, 0.09 -8.33 C -3.36 -6.88, -3.19 -2.24, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(93.0)"/><path d="M0 0 C 3.75 -1.94, 3.31 -5.94, 0.07 -7.90 C -3.94 -5.27, -3.83 -2.37, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(127.9)"/><path d="M0 0 C 3.47 -1.80, 4.07 -6.13, 0.22 -7.52 C -3.15 -5.17, -3.54 -2.13, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(185.5)"/><path d="M0 0 C 3.29 -2.37, 3.26 -6.21, -0.21 -8.45 C -3.22 -6.11, -3.28 -2.56, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(217.2)"/><path d="M0 0 C 3.03 -2.03, 3.62 -5.81, -0.02 -7.93 C -4.06 -5.03, -3.87 -1.99, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(264.9)"/><path d="M0 0 C 3.40 -2.34, 4.08 -6.63, -0.05 -8.08 C -3.14 -5.22, -3.83 -2.42, 0 0 z" fill="url(#g-gold)" opacity="0.45" transform="rotate(324.4)"/><path d="M0 0 C 2.97 -1.48, 2.73 -4.18, 0.22 -6.17 C -3.22 -4.91, -2.54 -1.68, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(3.4)"/><path d="M0 0 C 2.60 -1.99, 2.93 -4.53, 0.07 -6.32 C -3.45 -5.16, -3.00 -1.77, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(38.3)"/><path d="M0 0 C 2.76 -1.95, 2.86 -4.50, -0.03 -6.50 C -3.07 -4.48, -2.88 -1.79, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(96.5)"/><path d="M0 0 C 2.55 -2.01, 3.13 -4.97, -0.13 -7.12 C -2.72 -4.93, -2.78 -1.98, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(127.8)"/><path d="M0 0 C 2.93 -1.67, 3.00 -5.74, -0.23 -7.00 C -3.17 -5.74, -2.82 -2.02, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(175.7)"/><path d="M0 0 C 3.04 -1.83, 2.92 -4.58, 0.01 -6.37 C -3.32 -3.97, -2.58 -1.65, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(222.9)"/><path d="M0 0 C 2.87 -2.19, 3.00 -4.76, 0.08 -7.06 C -2.70 -5.82, -3.23 -1.88, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(266.3)"/><path d="M0 0 C 3.19 -2.07, 2.68 -5.51, -0.21 -7.10 C -3.20 -5.19, -3.32 -2.07, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(312.1)"/><path d="M0 0 C 2.26 -1.23, 1.88 -3.30, -0.03 -4.28 C -2.32 -3.53, -2.36 -1.05, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(9.3)"/><path d="M0 0 C 2.26 -1.04, 2.17 -2.73, -0.13 -3.87 C -2.09 -2.98, -1.83 -0.96, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(78.4)"/><path d="M0 0 C 2.13 -1.00, 1.95 -2.76, 0.15 -4.06 C -2.24 -3.29, -1.92 -1.11, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(139.0)"/><path d="M0 0 C 1.86 -1.31, 2.19 -2.60, -0.02 -4.20 C -2.12 -3.19, -2.37 -1.18, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(195.4)"/><path d="M0 0 C 2.28 -0.94, 2.37 -2.48, 0.03 -3.83 C -2.01 -2.63, -1.89 -1.02, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(257.3)"/><path d="M0 0 C 2.03 -1.13, 2.43 -2.71, 0.03 -3.94 C -2.19 -3.24, -1.99 -1.17, 0 0 z" fill="url(#g-gold)" stroke="#8A6A2B" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(316.1)"/><circle r="1.0" fill="#E8C27A" opacity="0.75"/><circle cx="1.6" cy="-0.1" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="1.2" cy="1.4" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="0.1" cy="1.4" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-1.3" cy="1.0" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-1.7" cy="-0.1" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="-1.2" cy="-1.3" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="0.3" cy="-2.0" r="0.32" fill="#8A6A2B" opacity="0.7"/><circle cx="1.2" cy="-1.2" r="0.32" fill="#8A6A2B" opacity="0.7"/></g><g transform="translate(58.0 32.0) rotate(0)"><path d="M0 0 C 2.42 -1.74, 3.19 -4.09, 0.09 -6.60 C -2.95 -4.83, -2.61 -1.66, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(-5.4)"/><path d="M0 0 C 3.00 -1.63, 3.13 -4.36, -0.13 -6.62 C -2.92 -4.92, -2.44 -2.00, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(60.4)"/><path d="M0 0 C 3.10 -2.00, 2.77 -5.53, 0.10 -6.76 C -2.71 -5.39, -2.94 -1.76, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(104.5)"/><path d="M0 0 C 2.78 -1.50, 2.71 -3.86, -0.16 -5.80 C -2.87 -3.89, -2.57 -1.51, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(149.3)"/><path d="M0 0 C 2.47 -2.09, 3.19 -5.01, 0.02 -6.74 C -3.09 -4.90, -2.88 -2.12, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(205.9)"/><path d="M0 0 C 2.38 -1.92, 2.77 -4.74, -0.12 -6.06 C -2.85 -4.19, -2.94 -1.92, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(262.6)"/><path d="M0 0 C 2.63 -1.65, 3.28 -4.07, 0.19 -6.40 C -3.02 -4.01, -3.08 -1.58, 0 0 z" fill="url(#g-wine)" opacity="0.45" transform="rotate(308.7)"/><path d="M0 0 C 2.65 -1.27, 2.70 -3.01, 0.06 -4.81 C -2.11 -2.97, -2.36 -1.54, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(1.0)"/><path d="M0 0 C 2.51 -1.58, 2.12 -4.08, -0.12 -5.62 C -2.44 -3.87, -2.31 -1.43, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(54.4)"/><path d="M0 0 C 2.30 -1.26, 2.42 -3.76, 0.17 -5.13 C -2.47 -3.29, -2.17 -1.37, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(106.1)"/><path d="M0 0 C 2.64 -1.81, 2.73 -4.55, 0.16 -5.71 C -2.08 -4.10, -2.37 -1.69, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(157.5)"/><path d="M0 0 C 2.61 -1.31, 2.44 -4.38, -0.17 -5.35 C -2.14 -4.28, -2.63 -1.28, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(207.5)"/><path d="M0 0 C 2.44 -1.57, 2.48 -4.33, 0.11 -5.59 C -2.06 -3.50, -2.51 -1.79, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(249.7)"/><path d="M0 0 C 2.20 -1.37, 2.07 -3.99, -0.09 -5.12 C -2.49 -3.72, -2.20 -1.51, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.12" stroke-opacity="0.35" transform="rotate(313.9)"/><path d="M0 0 C 1.84 -0.73, 1.55 -1.94, -0.01 -2.90 C -1.88 -1.99, -1.52 -0.85, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(14.5)"/><path d="M0 0 C 1.53 -0.96, 1.57 -2.05, -0.05 -3.10 C -1.64 -2.38, -1.74 -0.94, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(72.1)"/><path d="M0 0 C 1.78 -0.72, 1.59 -1.97, 0.13 -2.80 C -1.67 -1.93, -1.85 -0.90, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(135.5)"/><path d="M0 0 C 1.79 -0.86, 1.65 -2.22, -0.03 -2.84 C -1.62 -2.10, -1.77 -0.79, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(193.6)"/><path d="M0 0 C 1.65 -0.74, 1.51 -2.23, -0.09 -2.76 C -1.58 -2.21, -1.88 -0.87, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(258.8)"/><path d="M0 0 C 1.47 -1.00, 1.96 -2.20, -0.10 -3.36 C -1.83 -2.70, -1.76 -1.07, 0 0 z" fill="url(#g-wine)" stroke="#4A1520" stroke-width="0.1" stroke-opacity="0.3" opacity="0.95" transform="rotate(313.1)"/><circle r="0.8" fill="#E8C27A" opacity="0.75"/><circle cx="1.3" cy="-0.0" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="1.0" cy="0.8" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-0.2" cy="1.1" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-0.8" cy="1.0" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-1.3" cy="0.2" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="-0.9" cy="-0.7" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="0.0" cy="-1.4" r="0.25" fill="#4A1520" opacity="0.7"/><circle cx="1.1" cy="-1.0" r="0.25" fill="#4A1520" opacity="0.7"/></g><circle cx="14" cy="60" r="0.9" fill="#E8C27A" opacity="0.7"/><circle cx="52" cy="58" r="1.2" fill="#E8C27A" opacity="0.7"/><circle cx="60" cy="22" r="0.6" fill="#E8C27A" opacity="0.7"/><circle cx="30" cy="24" r="0.7" fill="#E8C27A" opacity="0.7"/><circle cx="8" cy="44" r="0.6" fill="#E8C27A" opacity="0.7"/></svg>'''
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
  <div class="label">Meta que dá pra medir</div>{lines(3)}
  <div class="label" style="margin-top:2mm">Como vou saber que cheguei</div>{lines(3)}</div>''' for n, cor in rs["areas"])
page(f'''
{head("Escreve a visão", "Habacuque 2:2")}
<div class="split even">
  <div class="l">
    <h1>Quadro dos sonhos</h1>
    <p style="font-size:9pt;line-height:1.5">Meta que fica só na cabeça vira desejo vago. Meta que você vê todo dia vira direção. Quando o que você quer é concreto, dá pra medir e está na sua frente, a disciplina cresce sozinha, porque você sabe pra onde está indo. É por isso que Deus mandou Habacuque escrever a visão em tábuas grandes, legíveis pra quem passa correndo. Este quadro é a sua tábua.</p>
    <p style="font-size:9pt;line-height:1.5">Dois passos. Nesta página, escreva metas que cabem em 40 dias e que dá pra medir: "treinar 3 vezes por semana", "guardar 300 reais", "fazer as pazes com minha irmã". Nas duas páginas seguintes, monte o mural: fotos do lugar que você quer conhecer, da vida saudável que quer viver, do que espera de Deus, um versículo que segura você ("sê forte e corajosa"), palavras, cores, recortes. Cole, desenhe, escreva. Passe da moldura. Mural bonito é mural usado.</p>
    {verse_box("Escreve a visão e torna bem legível sobre tábuas, para que a possa ler o que correndo passa.", "Habacuque 2:2")}
    <div style="margin-top:auto">{field("Minha frase de 40 dias", 2, "a que resume tudo", "tight")}</div>
  </div>
  <div class="r"><div class="sonho-area">{areas}</div></div>
</div>
''', cls="c-rubi", section="Início")
page(f'''
{head("Meu mural · 1 de 2", "uma área em cada canto")}
<div class="mural c-rubi">
  <span class="tape a"></span><span class="tape b"></span><span class="tape c"></span>
  {"".join(f'<div class="c-{cor}"><span>{e(n)}</span></div>' for n, cor in rs["areas"])}
</div>
''', cls="c-rubi", section="Início")
page(f'''
{head("Meu mural · 2 de 2", "sonhos, sem limite de área")}
<div class="mural livre c-rubi">
  <span class="tape a"></span><span class="tape b"></span><span class="tape c"></span>
  <div class="dica">O que eu quero ver acontecer</div>
  <span class="pin p1">uma viagem</span><span class="pin p2">meu trabalho</span><span class="pin p3">amizades</span><span class="pin p4">família e filhos</span><span class="pin p5">minha casa</span><span class="pin p6">meu corpo</span>
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
<div class="cmp-wrap">{rows}</div>
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
    {field("Por quem vou orar nesta prova", 2, "uma pessoa por dia, cada dia alguém", "tight")}
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
    <div class="bottom">
      <div class="grp">Energia {scale5()}</div>
      <div class="grp"><span class="progress"><i style="width:{d * 2.5}%"></i></span></div>
      <div class="skip"><span class="box"></span> Pulei</div>
    </div>
  </div>
  <div class="r">
    <div class="row" style="display:flex;justify-content:space-between;align-items:baseline"><div class="label" style="margin:0">Hoje</div><div class="date">Data <span></span>/<span></span>/<span></span></div></div>
    <div class="row"><div class="label">Hoje eu me senti <span class="hint">circule</span></div>{chips(C.SENTI)}</div>
    <div class="row"><div class="label">O que pesou hoje <span class="hint">marque</span></div>{chips(C.PESOU, "soft")}</div>
    <div class="row" style="display:flex;align-items:center;gap:2.5mm"><div class="label" style="margin:0">{e(b["virtude"])} hoje</div>{chips(C.VIRTUDE_OPCOES, "acc")}</div>
    <div class="row"><div class="label">Sou grata por</div>{lines(2, "tight")}</div>
    <div class="row"><div class="label">Minha maior dificuldade hoje <span class="hint">e o que ela me mostrou</span></div>{lines(3, "tight")}</div>
    <div class="row"><div class="label">Hoje eu oro por <span class="hint">uma pessoa, pelo nome</span></div>{lines(1, "tight")}</div>
    <div class="row"><div class="label">Uma linha pra Deus</div>{lines(1, "tight")}</div>
    <div class="row"><div class="label">Amanhã eu vou <span class="hint">uma coisa só</span></div>{lines(1, "tight")}</div>
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
    <div class="card fill" style="margin-top:auto"><div class="eyebrow" style="color:var(--accent)">{e(b["mulher"])} diria</div><p class="serif" style="font-size:8.6pt;font-style:italic;margin:0">{e(b["virtuosa"][:1].upper() + b["virtuosa"][1:])}</p></div>
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
page(f'''
{head("Foto honesta", "Dia 40")}
<h1>O que os 40 dias fizeram</h1>
<p class="small muted" style="font-size:8pt">Olhe o retrato do dia 1 e o do dia 40 lado a lado. Não só os números. Escreva o que você vê.</p>
<div class="split even">
  <div class="l">
    {field(rt["mudou_40"], 6)}
    {field(rt["deus_40"], 6)}
  </div>
  <div class="r">{fill_field("Oração de chegada", "o que eu quero dizer a Deus agora que terminei")}</div>
</div>
''', cls="c-ameixa", section="Fechamento")

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
      <div class="eyebrow" style="color:var(--ameixa)">Pra levar daqui</div>
      {field(fc["proximos"][0], 4)}{field(fc["proximos"][1], 3)}{field(fc["proximos"][2], 4)}{field(fc["proximos"][3], 2)}
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
{DECO}
<div class="frame"></div>
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
        foot = (f'<div class="foot"><span>{e(C.TITULO)}</span><span class="num">{i}</span></div>')
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
