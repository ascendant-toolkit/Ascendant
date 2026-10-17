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
