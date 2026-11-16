"""Shared helpers for the 20.2.1 extra resource pages (storing records in serial/sequential files, adding to a sequential file, adding to and finding in a random file)."""
import json as _j
import re as _re
from ak20 import *
from ac20r import both, practise, _PT, _PE

SUB = CBK("Chapter 20 · Further programming, section 20.2 File processing and exception handling")


def old_questions(fn="mk_ac2021.py"):
    """Real Paper 3 and 4 file questions already written for the main 20.2.1 page, keyed by their source chip."""
    ns = {}
    src = open(__file__.replace("ac20f.py", fn)).read().replace('\nbuild(', '\n_nob(')
    exec(compile("def _nob(*a, **k): pass\n" + src, "mk_ac2021", "exec"), ns)
    out = {}
    for c in _re.split(r'(?=  <details class="eq">)', ns["past"]):
        m = _re.search(r'<span class="src">(.*?)</span>', c)
        if m:
            out[m.group(1)] = _re.sub(r"\s*<h3>.*?</h3>\s*$", "\n", c, flags=_re.S)
    return out


def F(x, y, t, rows, **kw):
    """One file column for a step drawing."""
    return dict(x=x, y=y, t=t, r=rows, **kw)


def stp(el, label, steps, ps=None, py=None, lh=22, vw=150, fh=160, dwell=3200):
    """Stepper. steps: dicts with c (caption), p/y (highlighted pseudocode/python line), v (variable boxes), f (file columns), t (text)."""
    n = max(len(ps), len(py)) if ps else 0
    h = (22 + n * lh + 14 if ps else 8) + (82 if any(s.get("v") for s in steps) else 0) + fh
    cfg = dict(ps=ps, py=py, lh=lh, vw=vw)
    return (f'(function () {{ const C = {_j.dumps(cfg)}, ST = {_j.dumps(steps)};\n'
            f'  Lib.stepper($("#{el}"), {{ w: 760, h: {h}, label: {_j.dumps(label)}, base: {{ i: 0 }}, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: {dwell}, steps: ST.map((t, i) => ({{ cap: t.c, s: {{ i }} }})) }}); }})();\n')


FILEJS = AKJS + AK20JS + r'''
const MONO = "font-family:var(--mono);font-size:13px";
function codeLines(x, y, lines, hl, w, lh) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 3, i === hl ? "cell-warn" : "cell", { rx: 4 }) + SV.text(x + 8, y + i * lh + lh / 2 + 3, l, "lbl", { style: "font-family:var(--mono);font-size:11px;white-space:pre" })).join("");
}
function vbox(x, y, name, val, cls, w) {
  return SV.text(x, y - 7, name, "sm") + SV.rect(x, y, w, 34, cls || "f2", { rx: 6, ...op(0.6) }) + SV.rect(x, y, w, 34, "ax", { rx: 6, fill: "none" }) + SV.text(x + w / 2, y + 22, String(val), "lbl bd", { "text-anchor": "middle", style: MONO });
}
/* a column of file rows. o: x,y,t,r + optional w, lh, hl (warn row), ok[], no[], nw (new row), ptr (pointer row), ptrLabel, addr (show row numbers), eof */
function fcol(o) {
  const w = o.w || 210, lh = o.lh || 28, rows = o.r || [];
  let s = SV.text(o.x, o.y - 8, o.t, "sm");
  if (!rows.length) s += SV.rect(o.x, o.y, w, lh - 4, "cell", { rx: 5, ...op(0.5) }) + SV.text(o.x + 10, o.y + lh / 2 + 3, "(empty)", "sm");
  rows.forEach((r, i) => {
    let c = "cell";
    if (o.ok && o.ok.includes(i)) c = "cell-ok";
    if (o.no && o.no.includes(i)) c = "cell-no";
    if (o.nw === i) c = "f3";
    if (o.hl === i) c = "cell-warn";
    s += SV.rect(o.x, o.y + i * lh, w, lh - 4, c, { rx: 5 });
    if (o.addr) s += SV.text(o.x + 10, o.y + i * lh + lh / 2 + 3, String(i), "sm", { style: MONO }) + SV.text(o.x + 36, o.y + i * lh + lh / 2 + 3, r, "lbl", { style: MONO });
    else s += SV.text(o.x + 10, o.y + i * lh + lh / 2 + 3, r, "lbl", { style: MONO });
  });
  if (o.ptr !== undefined && o.ptr !== null && o.ptr >= 0) s += SV.text(o.x + w + 8, o.y + o.ptr * lh + lh / 2 + 3, "◀ " + (o.ptrLabel || "pointer"), "sm");
  if (o.eof) s += SV.text(o.x, o.y + rows.length * lh + 12, "end of file", "sm");
  return s;
}
function stepDraw(C, t) {
  let o = "", y = 8;
  if (C.ps) {
    o += SV.text(8, 14, "Pseudocode", "sm");
    const wa = Math.max(...C.ps.map((l) => l.length)) * 6.6 + 18, wb = Math.max(...C.py.map((l) => l.length)) * 6.6 + 18, ex = Math.max(0, (744 - wa - wb - 14) / 2), xb = 8 + wa + ex + 14;
    o += SV.text(xb, 14, "Python", "sm") + codeLines(8, 22, C.ps, t.p, wa + ex, C.lh) + codeLines(xb, 22, C.py, t.y, wb + ex, C.lh);
    y = 22 + Math.max(C.ps.length, C.py.length) * C.lh + 14;
  }
  if (t.v && t.v.length) { t.v.forEach((v, j) => { o += vbox(8 + j * C.vw, y + 16, v[0], v[1], v[2], C.vw - 12); }); y += 82; }
  (t.f || []).forEach((f) => { o += fcol({ ...f, y: y + f.y }); });
  (t.t || []).forEach((q) => { o += SV.text(q[0], y + q[1], q[2], q[3] || "sm"); });
  return o;
}
const lineHTML = (L) => '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
'''


def finishf(name, slug, title, lead, learn, watch, explore, prac, real, review, tipsl, sents, js, where, past, note, words, sub_num="20.2.1"):
    exam = exam20("Real Paper 3 and Paper 4 questions, then review questions for practice.", where, past, review, note)
    tips = tips_html(tipsl, sents, words) + FC
    build(name, slug, title, EYA(sub_num), lead, dict(sub=SUB, **tabs(learn, watch, explore, prac, real, exam, tips)), FILEJS + js)
