"""Shared helpers for the 20.1.2 extra resource pages (constructor, encapsulation, getters/setters, inheritance, polymorphism, containment, binary tree)."""
import json as _j
from ak20 import *

SUB = CBK("Chapter 20 · Further programming, section 20.1 Programming paradigms")
NOTE_PAPERS = "Class design is asked in Paper 3 as pseudocode and class diagrams; writing the classes as code is asked in Paper 4. The real questions are on the 20.1.2 and 20.1.3 pages in this section; this page is the extra explanation behind them."


def both(py, ps):
    return ('<div class="grid2"><div><h4>Python</h4><div class="code">' + pc(py) + '</div></div>'
            '<div><h4>Pseudocode (exam style)</h4><div class="code">' + pc(ps) + '</div></div></div>')


def code(x, y, lines, hl=-1, w=300, lh=30):
    return dict(k="code", x=x, y=y, lines=lines, hl=hl, w=w, lh=lh)


def cls(x, y, w, title, rows, c="f1", lh=20):
    return dict(k="cls", x=x, y=y, w=w, title=title, rows=rows, cls=c, lh=lh)


def txt(x, y, s, c="sm", m=0):
    return dict(k="txt", x=x, y=y, s=s, c=c, m=m)


def arr(x1, y1, x2, y2, d="r"):
    return dict(k="arr", a=[x1, y1, x2, y2], d=d)


def stepper(el, label, w, h, steps):
    caps = [c for c, _ in steps]
    scenes = [s for _, s in steps]
    return (f'(function () {{ const SC = {_j.dumps(scenes)}, CAPS = {_j.dumps(caps)};\n'
            f'  Lib.stepper($("#{el}"), {{ w: {w}, h: {h}, label: {_j.dumps(label)}, base: {{ i: 0 }}, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({{ cap: c, s: {{ i }} }})) }}); }})();\n')


SHARED = AKJS + AK20JS + r'''
function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}
function sceneItem(o) {
  if (o.k === "code") return codeList(o.x, o.y, o.lines, o.hl, 1, o.lh, o.w);
  if (o.k === "cls") return classBox(o.x, o.y, o.w, o.title, o.rows, 1, o.cls, o.lh);
  if (o.k === "txt") return SV.text(o.x, o.y, o.s, o.c, o.m ? { style: "font-family:var(--mono);font-size:14px" } : {});
  if (o.k === "arr") return arrow(o.a[0], o.a[1], o.a[2], o.a[3], o.d, "c1", 1);
  return "";
}
const codeHTML = (L) => '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
'''

_PT = {"cl": "Sort the statements", "o": "Put the steps in order", "m": "Match the term to its meaning", "c": "Work it out", "q": "Multiple choice"}
_PE = {"cl": '<div id="cl1" class="card"></div>', "o": '<div id="o1" class="card"></div>', "m": '<div id="m1" class="card"></div>', "c": '<div id="c1"></div>', "q": '<div id="qz1"></div>'}


def practise(*ids):
    return "".join(f"  <h2>{n} · {_PT[k]}</h2>{_PE[k]}\n" for n, k in enumerate(ids, 1))


def finish(name, slug, title, lead, learn, watch, explore, prac, real, review, tipsl, sents, js, past_note=NOTE_PAPERS, sub_num="20.1.2"):
    exam = exam20("Review questions for practice; they are not in exam format.", [], '', review)
    exam = exam.replace('  <h2>1. Past paper questions</h2>\n', '  <h2>1. Where this is examined</h2>\n  <p class="note">' + past_note + '</p>\n', 1)
    tips = tips_html(tipsl, sents, [("Define / State", "Give the meaning in one precise sentence."), ("Write program code", "Produce working Python in the form the question describes."), ("Complete the class diagram", "Fill in properties and methods; the question tells you which are missing."), ("Explain", "A reason as well as the fact.")]) + FC
    build(name, slug, title, EYA(sub_num), lead, dict(sub=SUB, **tabs(learn, watch, explore, prac, real, exam, tips)), SHARED + js)
