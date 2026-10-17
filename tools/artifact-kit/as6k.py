"""Shared pieces for the AS Topic 6 pages: causal chain steppers, chooser labs and the standard Practise/Watch shells."""
from asx import *

CHAINJS = '''
function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
'''


def chooser_html(p, title, intro, heads):
    r = "".join(f'<div><small>{h}</small><strong id="{p}{i + 1}"></strong></div>' for i, h in enumerate(heads))
    return f'''
  <h2>{title}</h2>
  <p>{intro}</p>
  <div class="card"><div class="grid2"><div><div id="{p}B" class="btnrow"></div>
    <div class="readout">{r}</div>
    <div class="verdict" id="{p}v"></div></div>
    <div><svg id="{p}S" viewBox="0 0 420 200" role="img" aria-label="{title}"></svg></div></div></div>
'''


def watch_html(t1, t2):
    return f'''
  <h2>1 · {t1}</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · {t2}</h2>
  <div id="stB"></div>
'''


def practise_html(h1, h2, h3):
    return f'''
  <h2>1 · {h1}</h2><div id="cl1" class="card"></div>
  <h2>2 · {h2}</h2><div id="m1" class="card"></div>
  <h2>3 · {h3}</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

WFJS = '''
function wfDraw(items, s) {
  const max = Math.max(...items.map((it) => it[3] || 0)) * 1.15, Y = (v) => 250 - (v / max) * 190, w = 600 / items.length; let o = SV.line(50, 250, 740, 250);
  items.forEach((it, i) => {
    const [lab, val, kind, top, bot] = it, x = 70 + i * (w + 8), v = Math.max(0, Math.min(1, s.k - i));
    if (v <= 0) return;
    o += SV.rect(x, Y(top), w - 20, Math.max(2, Y(bot) - Y(top)), kind === "t" ? "f1" : val < 0 ? "f3" : "f2", op(0.65 * v)) + SV.text(x + (w - 20) / 2, Y(top) - 8, (kind === "d" && val > 0 ? "+" : "") + Lib.fmtN(val, 0), "lbl bd", { "text-anchor": "middle", ...op(v) }) + SV.text(x + (w - 20) / 2, 270, lab, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return o;
}
'''


import ast as _ast, glob as _glob, os as _os
_GRAB = {}
def grab(code, q):
    """Return the eq(...) block already written for P(code, q) in another mk_as page (so exam-technique pages reuse the same reworded questions)."""
    if not _GRAB:
        here = _os.path.dirname(_os.path.abspath(__file__))
        for f in sorted(_glob.glob(_os.path.join(here, "mk_as*.py"))):
            if f.endswith("mk_asx.py"): continue
            src = open(f).read()
            try: tree = _ast.parse(src)
            except SyntaxError: continue
            for n in _ast.walk(tree):
                if isinstance(n, _ast.Call) and getattr(n.func, "id", "") == "eq" and n.args and isinstance(n.args[0], _ast.Call) and getattr(n.args[0].func, "id", "") == "P":
                    a = n.args[0].args
                    if len(a) == 2 and all(isinstance(x, _ast.Constant) for x in a):
                        _GRAB.setdefault((a[0].value, a[1].value), _ast.get_source_segment(src, n))
    return eval(_GRAB[(code, q)], globals())


def exam_rows(items, mc_codes=()):
    """Header rows for exam_page built from the (code, part, marks) items actually shown, so counts and sources always match."""
    M = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}
    lab = lambda c, q: f"{M[c.split('_')[0][0]]} 20{c.split('_')[0][1:]} ({c.split('_')[1]}) Q{q}"
    g = {}
    for c, q, m in items: g.setdefault(int(m), []).append(lab(c, q))
    rows = []
    for m in (8, 12):
        if m in g: rows.append((f"Essay parts, {m} marks", str(len(g[m])), "; ".join(g[m])))
    for m in sorted(k for k in g if k not in (8, 12)):
        rows.append((f"Data response, {m} marks", str(len(g[m])), "; ".join(g[m])))
    if mc_codes:
        ys = sorted(int("20" + c[1:3]) for c in mc_codes)
        rows.append(("Multiple choice (Paper 1)", f"{len(mc_codes)} shown below", f"{ys[0]} to {ys[-1]}"))
    return rows
