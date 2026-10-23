"""Shared pieces for the A Level Computer Science (9618) syllabus-numbered pages: labels, exam helpers and small JS drawing helpers."""
from csk import *

_CMA = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}


def EYA(sub):
    return f"A Level Computer Science · 9618 · Syllabus {sub}"


def CBK(txt):
    return f"Coursebook: {txt}"


def AP(code, q):
    """Source line for a written question: AP('s23_11', '3(d)') -> 'Based on May/June 2023 · 9618/11 · Q3(d)'."""
    ser, var = code.split("_")
    return f"Based on {_CMA[ser[0]]} 20{ser[1:]} · 9618/{var} · Q{q}"


def _alabel(c, q):
    ser, var = c.split("_")
    return f"{_CMA[ser[0]]} 20{ser[1:]} ({var}) Q{q}"


def arows(items):
    """Header rows for the exam table, built from the (code, part, marks) items actually shown so counts always match."""
    return [("Paper 1 written questions", f"{len(items)} shown below", "; ".join(f"{_alabel(c, q)} [{m}]" for c, q, m in items))]


def aexam(title, intro, items, qs):
    return cs_exam(title, intro, arows(items), qs)


def tbl(heads, rows):
    return table(heads, rows)


# Shared JS: binary strings and a row of bit boxes for the stepper drawings.
AKJS = '''
const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}
'''
