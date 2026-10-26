const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

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

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

/* circuit drawer: geom comes from ak15.circuit(); vals colours the wires */
function circEval(G, inp, st) {
  const v = Object.assign({}, inp); G.net.forEach(([n]) => v[n] = (st && st[n]) || 0);
  for (let k = 0; k < 8; k++) G.net.forEach(([n, t, s]) => {
    const a = s.map((x) => v[x]); let base = t, neg = false;
    if (t !== "NOT" && t[0] === "N") { base = t.slice(1); neg = true; }
    let r = base === "AND" ? a.every((x) => x) : base === "OR" ? a.some((x) => x) : base === "XOR" ? a.reduce((p, x) => p + x, 0) % 2 === 1 : !a[0];
    r = (neg ? !r : r) ? 1 : 0; v[n] = r;
  });
  return v;
}
function circInner(G, vals, opt) {
  opt = opt || {};
  const cl = (s) => (vals ? (vals[s] ? "w on" : "w off") : "w"); let o = "";
  G.wires.forEach((w) => { o += `<path class="${cl(w.s)}" d="${w.d}"/>`; if (w.dot) o += `<circle class="dot" cx="${w.dot[0]}" cy="${w.dot[1]}" r="3.2"/>`; });
  G.outs.forEach((w) => o += `<path class="${cl(w.s)}" d="${w.d}"/>`);
  G.gates.forEach((g) => { o += g.svg; if (!G.outset.includes(g.n)) o += `<text class="sm" x="${g.ox + 4}" y="${g.cy - 7}">${g.n}${vals && opt.vals ? " = " + vals[g.n] : ""}</text>`; });
  G.inputs.forEach((i) => o += `<text class="lbl bd" x="2" y="${i.y + 4}">${i.n}${vals ? " " + vals[i.n] : ""}</text>`);
  G.outs.forEach((w) => o += `<text class="lbl bd" x="${w.x + 6}" y="${w.y + 4}">${w.s}${vals ? " = " + vals[w.s] : ""}</text>`);
  return o;
}
function circFit(G, vals, W, opt) {
  const k = Math.min(2.2, (W - 20) / G.w), dx = (W - G.w * k) / 2;
  return `<g transform="translate(${dx.toFixed(1)},6) scale(${k.toFixed(3)})">` + circInner(G, vals, opt) + "</g>";
}
function circSvg(G, vals, opt) {
  return `<svg viewBox="0 0 ${G.w} ${G.h}" style="width:${Math.round(G.w * 1.2)}px;max-width:100%;display:block">` + circInner(G, vals, opt) + "</svg>";
}
/* toggle lab: one button per input, live circuit and a table of every row with the current one highlighted */
function circLab(el, G, work, outs) {
  const ins = G.in; let cur = ins.map(() => 0);
  const root = typeof el === "string" ? $(el) : el;
  root.innerHTML = '<div class="btnrow" data-b></div><div data-s></div><div data-t></div>';
  const bw = root.querySelector("[data-b]"), sw = root.querySelector("[data-s]"), tw = root.querySelector("[data-t]");
  function paint() {
    const inp = {}; ins.forEach((n, i) => inp[n] = cur[i]);
    const v = circEval(G, inp);
    sw.innerHTML = circSvg(G, v, { vals: true });
    bw.querySelectorAll("button").forEach((b, i) => { b.textContent = ins[i] + " = " + cur[i]; b.className = cur[i] ? "on" : ""; });
    const cols = ins.concat(work, outs); let h = '<div class="tw"><table class="t mono"><tr>' + cols.map((c) => `<th>${c}</th>`).join("") + "</tr>";
    for (let m = 0; m < 1 << ins.length; m++) {
      const b = ins.map((_, i) => (m >> (ins.length - 1 - i)) & 1), iv = {}; ins.forEach((n, i) => iv[n] = b[i]);
      const r = circEval(G, iv), on = b.every((x, i) => x === cur[i]);
      h += `<tr style="${on ? "background:var(--accent-soft);font-weight:700" : ""}">` + b.map((x) => `<td>${x}</td>`).join("") + work.concat(outs).map((n) => `<td>${r[n]}</td>`).join("") + "</tr>";
    }
    tw.innerHTML = h + "</table></div>";
  }
  ins.forEach((n, i) => { const b = document.createElement("button"); b.onclick = () => { cur[i] ^= 1; paint(); }; bw.appendChild(b); });
  paint();
}
const GSR = {"w": 272, "h": 195.0, "inputs": [{"n": "R", "y": 40}, {"n": "S", "y": 160}], "gates": [{"n": "Q", "x": 94, "cy": 50, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,29.0 Q126.4,29.0 148,50 Q126.4,71.0 94,71.0 Q109.12,50 94,29.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"152\" cy=\"50\" r=\"4\"/>", "ox": 156}, {"n": "Qb", "x": 94, "cy": 150, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,129.0 Q126.4,129.0 148,150 Q126.4,171.0 94,171.0 Q109.12,150 94,129.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"152\" cy=\"150\" r=\"4\"/>", "ox": 156}], "wires": [{"d": "M58,40 H82 V39.0 H99.48571428571428", "s": "R", "dot": null}, {"d": "M156,150 H170 V105 H77 V61.0 H99.48571428571428", "s": "Qb", "dot": null}, {"d": "M156,50 H170 V95 H82 V139.0 H99.48571428571428", "s": "Q", "dot": null}, {"d": "M58,160 H77 V161.0 H99.48571428571428", "s": "S", "dot": null}, {"d": "M50,40 H58", "s": "R", "dot": null}, {"d": "M50,160 H58", "s": "S", "dot": null}], "outs": [{"d": "M156,50 H186", "s": "Q", "x": 186, "y": 50}, {"d": "M156,150 H186", "s": "Qb", "x": 186, "y": 150}], "outset": ["Q", "Qb"], "net": [["Q", "NOR", ["R", "Qb"]], ["Qb", "NOR", ["Q", "S"]]], "in": ["R", "S"]};

function srStep(st, S, R) { let Q = st.Q, Qb = st.Qb; for (let i = 0; i < 6; i++) { const nq = (R | Qb) ? 0 : 1, nqb = (S | nq) ? 0 : 1; Q = nq; Qb = nqb; } return { Q, Qb }; }
function srVals(st, S, R) { return { R, S, Q: st.Q, Qb: st.Qb }; }
(function () {
  const seq = [[0, 0], [1, 0], [0, 0], [0, 1], [0, 0]]; let st = { Q: 0, Qb: 1 }; const hist = [{ st, S: 0, R: 0 }];
  seq.forEach(([S, R], i) => { st = srStep(st, S, R); hist.push({ st, S, R }); });
  const draw = (s) => { const h = hist[Math.round(s.i) + 1]; return circFit(GSR, srVals(h.st, h.S, h.R), 560, { vals: false }); };
  const caps = ["Start: Q = 0, S = 0 and R = 0. Nothing is stored yet (Q = 0).", "S goes to 1: the flip-flop is <b>set</b>. Q becomes 1.", "S returns to 0. Q is <b>still 1</b>: the flip-flop has remembered.", "R goes to 1: the flip-flop is <b>reset</b>. Q becomes 0.", "R returns to 0. Q stays 0. The bit is stored again, this time as 0."];
  Lib.stepper($("#stA"), { w: 560, h: Math.round(SRNOR.h * 2.2) + 12, label: "SR flip-flop remembering", base: { i: 0 }, draw, tween: 150, dwell: 2800, steps: caps.map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const ev = [{ j: 1, k: 0, q: 1, c: "J = 1, K = 0, clock pulse: Q is <b>set</b> to 1." }, { j: 0, k: 0, q: 1, c: "J = 0, K = 0, clock pulse: Q <b>keeps</b> its value, 1." }, { j: 1, k: 1, q: 0, c: "J = 1, K = 1, clock pulse: Q <b>toggles</b> from 1 to 0." }, { j: 1, k: 1, q: 1, c: "J = 1, K = 1, another pulse: Q toggles from 0 to 1." }, { j: 0, k: 1, q: 0, c: "J = 0, K = 1, clock pulse: Q is <b>reset</b> to 0." }];
  const draw = (s) => { const i = Math.round(s.i), e = ev[i]; let o = SV.rect(210, 20, 180, 150, "cell", { rx: 10 }) + SV.text(300, 46, "JK flip-flop", "lbl bd", { "text-anchor": "middle" });
    o += SV.text(60, 70, "J = " + e.j, "lbl bd") + SV.text(60, 110, "K = " + e.k, "lbl bd") + SV.text(60, 150, "clock pulse " + (i + 1), "lbl bd t1") + SV.path("M150,66 H210 M150,106 H210 M150,146 H210", "ax");
    o += SV.rect(430, 70, 100, 50, e.q ? "cell-ok" : "cell", { rx: 8 }) + SV.text(480, 103, "Q = " + e.q, "lbl bd", { "text-anchor": "middle" }) + SV.path("M390,95 H430", "ax");
    o += SV.text(60, 200, "Q before the pulse: " + (i === 0 ? 0 : ev[i - 1].q), "sm"); return o; };
  Lib.stepper($("#stB"), { w: 640, h: 215, label: "JK flip-flop", base: { i: 0 }, draw, tween: 150, dwell: 2800, steps: ev.map((e, i) => ({ cap: e.c, s: { i } })) });
})();
(function () {
  const target = [1, 0, 1, 1, 0, 0, 0, 1];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; target.forEach((b, i) => { const on = i < k; o += SV.rect(30 + i * 80, 30, 66, 60, on ? (b ? "cell-ok" : "cell-warn") : "cell", { rx: 8 }) + SV.text(63 + i * 80, 68, on ? String(b) : "?", "lbl bd", { "text-anchor": "middle", style: "font-size:22px;font-family:var(--mono)" }) + SV.text(63 + i * 80, 110, "bit " + (7 - i), "sm", { "text-anchor": "middle" }); });
    o += SV.text(30, 150, k === 8 ? "stored: 10110001 = " + parseInt(target.join(""), 2) + " (hex " + hx(parseInt(target.join(""), 2)) + ")" : "each flip-flop stores one bit", "lbl bd t3"); return o; };
  Lib.stepper($("#stC"), { w: 680, h: 170, label: "A register of eight flip-flops", base: { i: 0 }, draw, tween: 150, dwell: 1200, steps: [0, 1, 2, 3, 4, 5, 6, 7, 8].map((i) => ({ cap: i === 0 ? "A register is a row of flip-flops. Each will store one bit of the byte." : i === 8 ? "All eight bits are stored: 10110001. They stay until new values are loaded." : "Bit " + (8 - i) + " is stored in its own flip-flop (set for 1, reset for 0).", s: { i } })) });
})();

(function () {
  let S = 0, R = 0, st = { Q: 0, Qb: 1 }, note = "";
  const b = $("#srB");
  const paint = () => { $("#srS").innerHTML = circSvg(SRG, srVals(st, S, R), { vals: false }); b.querySelectorAll("button").forEach((x, i) => { const v = i ? R : S; x.textContent = (i ? "R" : "S") + " = " + v; x.className = v ? "on" : ""; });
    $("#srV").innerHTML = S && R ? "S = R = 1 is <b>invalid</b>: both outputs are 0. When you release them the result is unpredictable." : S ? "Set: Q = 1." : R ? "Reset: Q = 0." : "S = 0 and R = 0: the flip-flop <b>keeps</b> its value, Q = " + st.Q + "." + note; };
  const SRG = GSR;
  [0, 1].forEach((i) => { const x = document.createElement("button"); x.onclick = () => { const was = S && R; if (i) R ^= 1; else S ^= 1; st = srStep(st, S, R); note = was && !S && !R ? " (it was set to 0 by R = S = 1 being released, so the result here is arbitrary)" : ""; paint(); }; b.appendChild(x); });
  paint();
})();
(function () {
  let J = 0, K = 0, Q = 0, n = 0; const hist = [];
  const b = $("#jkB");
  const paint = () => { let o = SV.rect(150, 15, 170, 110, "cell", { rx: 10 }) + SV.text(235, 40, "JK flip-flop", "lbl bd", { "text-anchor": "middle" }) + SV.text(30, 56, "J = " + J, "lbl bd") + SV.text(30, 96, "K = " + K, "lbl bd") + SV.path("M100,52 H150 M100,92 H150", "ax") + SV.rect(350, 55, 100, 46, Q ? "cell-ok" : "cell", { rx: 8 }) + SV.text(400, 85, "Q = " + Q, "lbl bd", { "text-anchor": "middle" }) + SV.path("M320,78 H350", "ax");
    $("#jkS").innerHTML = `<svg viewBox="0 0 480 140" style="width:480px;max-width:100%;display:block">` + o + "</svg>";
    b.querySelectorAll("button").forEach((x, i) => { if (i === 0) x.textContent = "J = " + J, x.className = J ? "on" : ""; if (i === 1) x.textContent = "K = " + K, x.className = K ? "on" : ""; if (i === 2) x.textContent = "Clock pulse"; });
    $("#jkV").innerHTML = n ? "After " + n + " pulse" + (n > 1 ? "s" : "") + " the outputs have been: " + hist.join(", ") + "." + (J && K ? " J = K = 1 toggles on every pulse." : "") : "Click Clock pulse. J and K are only looked at when the clock pulses."; };
  [0, 1, 2].forEach((i) => { const x = document.createElement("button"); x.onclick = () => { if (i === 0) J ^= 1; else if (i === 1) K ^= 1; else { Q = J && K ? 1 - Q : J ? 1 : K ? 0 : Q; n++; hist.push(Q); if (hist.length > 12) hist.shift(); } paint(); }; b.appendChild(x); });
  paint();
})();
(function () {
  const bits = [0, 0, 0, 0, 0, 0, 0, 0]; const b = $("#rgB");
  const paint = () => { b.querySelectorAll("button").forEach((x, i) => { x.textContent = "bit " + (7 - i) + " = " + bits[i]; x.className = bits[i] ? "on" : ""; }); const v = parseInt(bits.join(""), 2); $("#rgV").innerHTML = "Stored: <b>" + bits.join("") + "</b> = " + v + " (hex " + hx(v) + ")"; };
  bits.forEach((_, i) => { const x = document.createElement("button"); x.onclick = () => { bits[i] ^= 1; paint(); }; b.appendChild(x); }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which effect does the SR input combination have?", buckets: [{"label": "Keeps Q"}, {"label": "Sets Q to 1"}, {"label": "Resets Q to 0"}, {"label": "Invalid"}], items: [{"text": "S = 0, R = 0", "b": 0}, {"text": "S = 1, R = 0", "b": 1}, {"text": "S = 0, R = 1", "b": 2}, {"text": "S = 1, R = 1", "b": 3}], done: "00 keep, 10 set, 01 reset, 11 invalid (NOR version)." });
Lib.classify($("#cl2"), { prompt: "Is the statement about an SR or a JK flip-flop?", buckets: [{"label": "SR flip-flop"}, {"label": "JK flip-flop"}], items: [{"text": "Has set and reset inputs but no clock in its basic form", "b": 0}, {"text": "Has a clock input", "b": 1}, {"text": "An input of 1 and 1 is not allowed", "b": 0}, {"text": "An input of 1 and 1 makes the output toggle", "b": 1}, {"text": "Is made of two cross-coupled NOR or NAND gates", "b": 0}], done: "SR: set and reset, 11 invalid. JK: clocked, 11 toggles." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Flip-flop", "A circuit that stores one bit"], ["Set", "Makes Q = 1"], ["Reset", "Makes Q = 0"], ["Toggle", "Output swaps on each clock pulse"], ["Register", "A group of flip-flops holding one value"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order for storing a 1 in an SR flip-flop (NOR version).", items: ["S goes to 1 (R stays 0)", "Q becomes 1", "S returns to 0", "Q stays at 1: the bit is stored"], done: "Set, output changes, set released, value kept." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many flip-flops are needed to store one byte?", "a": 8, "unit": "", "tol": 0.01, "hint": "One bit per flip-flop.", "sol": "<b>8</b>."},
  {"q": "A JK flip-flop has Q = 0 and J = K = 1. What is Q after three clock pulses?", "a": 1, "unit": "", "tol": 0.01, "hint": "1, 0, 1.", "sol": "<b>1</b>."},
  {"q": "How many flip-flops would store a 16-bit word?", "a": 16, "unit": "", "tol": 0.01, "hint": "One per bit.", "sol": "<b>16</b>."},
  {"q": "An SR flip-flop with Q = 1 gets S = 0 and R = 0. What is Q?", "a": 1, "unit": "", "tol": 0.01, "hint": "It remembers.", "sol": "<b>1</b>."},
  {"q": "How many gates are in an SR flip-flop?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two NOR or two NAND.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does a flip-flop store?", opts: ["One bit", "One byte", "A program", "A character set"], a: 0, why: "One binary digit." },
  { q: "Which gates can make an SR flip-flop?", opts: ["One AND, one OR", "Two NOR or two NAND", "Two XOR", "Three NOT"], a: 1, why: "Same type, cross-connected." },
  { q: "In a NOR SR flip-flop, S = 1 and R = 0 gives:", opts: ["Q = 0", "Q = 1", "Invalid", "No change"], a: 1, why: "Set." },
  { q: "The JK flip-flop with J = K = 1 on a clock pulse:", opts: ["Resets", "Sets", "Toggles", "Is invalid"], a: 2, why: "Toggle." },
  { q: "A circuit whose output depends on stored state is:", opts: ["Combinational", "Sequential", "Parallel", "Serial"], a: 1, why: "Sequential." },
  { q: "A register is made of:", opts: ["Flip-flops", "Resistors only", "Hard disk sectors", "Capacitors only"], a: 0, why: "One flip-flop per bit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Flip-flop", "Stores one bit. Sequential, uses feedback."],
  ["SR", "Two cross-coupled NOR or NAND gates. S sets, R resets, 11 invalid."],
  ["JK", "Clocked. J set, K reset, 11 toggle."],
  ["Register", "Flip-flops side by side, one per bit."],
  ["Combinational", "Output depends only on the current inputs."],
  ["Sequential", "Output depends on the inputs and stored state."],
  ["SRAM", "Flip-flop-style cells; no refresh needed."],
  ["Drawing", "Same gate type, crossed outputs, labelled S and R."],
] });
