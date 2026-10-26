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

const sig = (x) => 1 / (1 + Math.exp(-x));
const fmt = (x) => (Math.round(x * 100) / 100).toString();
/* 2-2-1 network with fixed starting weights */
const NET0 = { w1: [[0.5, -0.3], [0.2, 0.8]], b1: [0.1, -0.1], w2: [0.7, -0.6], b2: 0.2 }; const IN = [1, 0], TARGET = 1;
function fwd(n, x) { const h = [0, 1].map((j) => sig(x[0] * n.w1[0][j] + x[1] * n.w1[1][j] + n.b1[j])); const o = sig(h[0] * n.w2[0] + h[1] * n.w2[1] + n.b2); return { h, o }; }
function backprop(n, x, t, lr) { const { h, o } = fwd(n, x), dO = (o - t) * o * (1 - o), dH = [0, 1].map((j) => dO * n.w2[j] * h[j] * (1 - h[j]));
  const m = JSON.parse(JSON.stringify(n)); [0, 1].forEach((j) => { m.w2[j] -= lr * dO * h[j]; m.b1[j] -= lr * dH[j]; [0, 1].forEach((i) => (m.w1[i][j] -= lr * dH[j] * x[i])); }); m.b2 -= lr * dO; return { m, dO, dH }; }
function netDraw(n, x, o) { /* nodes: in 0,1 ; hidden 0,1 ; out */ const P = { i0: [70, 70], i1: [70, 170], h0: [250, 50], h1: [250, 190], o: [430, 120] }; let s = "";
  const edge = (a, b, w) => (s += SV.line(P[a][0], P[a][1], P[b][0], P[b][1], "ax", { style: "stroke:" + (w >= 0 ? "var(--good)" : "var(--bad)") + ";stroke-width:" + (1 + Math.abs(w) * 5) + ";opacity:.8" }));
  [0, 1].forEach((j) => [0, 1].forEach((i) => edge("i" + i, "h" + j, n.w1[i][j]))); [0, 1].forEach((j) => edge("h" + j, "o", n.w2[j]));
  const node = (k, v, lab) => (s += SV.circle(P[k][0], P[k][1], 26, "nd", {}) + SV.text(P[k][0], P[k][1] + 5, v === null ? "" : fmt(v), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(P[k][0], P[k][1] + 44, lab, "sm", { "text-anchor": "middle" }));
  node("i0", x[0], "input 1"); node("i1", x[1], "input 2"); if (o) { node("h0", o.h[0], "hidden 1"); node("h1", o.h[1], "hidden 2"); node("o", o.o, "output"); } else { node("h0", null, "hidden 1"); node("h1", null, "hidden 2"); node("o", null, "output"); } return s; }
(function () {
  const r = fwd(NET0, IN);
  const draw = (s) => { const k = Math.round(s.i); let o = netDraw(NET0, IN, k >= 1 ? { h: k >= 2 ? r.h : [0, 0], o: k >= 3 ? r.o : 0 } : null); if (k < 2 && k >= 1) o = netDraw(NET0, IN, null); return o + SV.text(20, 20, "weights: green positive, red negative", "sm"); };
  Lib.stepper($("#stA"), { w: 500, h: 250, label: "Forward pass", base: { i: 0 }, draw: (s) => { const k = Math.round(s.i); return netDraw(NET0, IN, k >= 2 ? { h: k >= 3 ? r.h : [0, 0], o: k >= 4 ? r.o : 0 } : null) + SV.text(20, 18, "weights: green positive, red negative", "sm"); }, tween: 120, dwell: 2800, steps: [{ cap: "A small network: 2 inputs, 2 hidden nodes and 1 output. Each line is a connection with a <b>weight</b>.", s: { i: 0 } }, { cap: "The input layer receives the data: the inputs are 1 and 0.", s: { i: 1 } }, { cap: "Each hidden node adds up its weighted inputs plus a bias and applies the activation function.", s: { i: 2 } }, { cap: `The hidden outputs are ${fmt(r.h[0])} and ${fmt(r.h[1])}, which feed the output node.`, s: { i: 3 } }, { cap: `The network outputs <b>${fmt(r.o)}</b>. The expected output is <b>${TARGET}</b>, so there is an error of ${fmt(TARGET - r.o)}.`, s: { i: 4 } }] });
})();
(function () {
  const r0 = fwd(NET0, IN), bp = backprop(NET0, IN, TARGET, 2), r1 = fwd(bp.m, IN);
  const draw = (s) => { const k = Math.round(s.i); const n = k >= 3 ? bp.m : NET0, r = k >= 4 ? r1 : r0; let o = netDraw(n, IN, r);
    if (k >= 1 && k < 4) o += SV.text(430, 190, "error " + fmt(TARGET - r0.o), "lbl bd t2", { "text-anchor": "middle", style: "font-size:13px" }); if (k >= 2 && k < 3) o += SV.path("M400,120 H280", "ax", { style: "stroke:var(--bad);stroke-width:3" }) + SV.arrowHead(274, 120, "l", "dot2");
    if (k >= 4) o += SV.text(430, 190, "error " + fmt(TARGET - r1.o), "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 500, h: 250, label: "Back propagation", base: { i: 0 }, draw, tween: 120, dwell: 3000, steps: [{ cap: `The network's output is ${fmt(r0.o)}.`, s: { i: 0 } }, { cap: `The expected output is ${TARGET}: the <b>error</b> is ${fmt(TARGET - r0.o)}. The output is compared with the expected output.`, s: { i: 1 } }, { cap: "The error is <b>fed back</b> through the network, from the output layer towards the input layer. Calculus gives each weight's share of the error (the error gradient).", s: { i: 2 } }, { cap: "The <b>weights are adjusted</b> to reduce the error: some connections grow stronger and some weaker.", s: { i: 3 } }, { cap: `After one round the output is ${fmt(r1.o)} and the error has fallen to ${fmt(TARGET - r1.o)}. The process <b>repeats</b> until the results are accurate.`, s: { i: 4 } }] });
})();
(function () {
  const D = [[1, 2.2], [2, 3.1], [3, 4.4], [4, 4.8], [5, 6.2], [6, 6.9], [7, 8.3]]; const n = D.length, sx = D.reduce((a, d) => a + d[0], 0), sy = D.reduce((a, d) => a + d[1], 0), sxy = D.reduce((a, d) => a + d[0] * d[1], 0), sxx = D.reduce((a, d) => a + d[0] * d[0], 0);
  const m = (n * sxy - sx * sy) / (n * sxx - sx * sx), c = (sy - m * sx) / n; const X = (x) => 40 + x * 55, Y = (y) => 230 - y * 24;
  const draw = (s) => { const k = Math.round(s.i); const lm = k === 0 ? 0.2 : k === 1 ? 2 : m, lc = k === 0 ? 4 : k === 1 ? -1 : c; let o = SV.path("M40,20 V230 H440", "ax") + SV.text(240, 252, "independent variable (x)", "sm", { "text-anchor": "middle" });
    if (k >= 1) D.forEach(([x, y]) => (o += SV.line(X(x), Y(y), X(x), Y(lm * x + lc), "ax", { style: "stroke:var(--bad);stroke-width:1.5;opacity:.7" }))); D.forEach(([x, y]) => (o += SV.circle(X(x), Y(y), 5, "dot1")));
    if (k >= 0) o += SV.line(X(0.4), Y(lm * 0.4 + lc), X(7.6), Y(lm * 7.6 + lc), "ax", { style: "stroke:var(--good);stroke-width:3" }); const err = D.reduce((a, [x, y]) => a + (y - (lm * x + lc)) ** 2, 0); if (k >= 1) o += SV.text(50, 14, "squared error = " + fmt(err), "lbl bd", { "text-anchor": "start", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 262, label: "Regression", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "Past data: each dot is an example (an x value and the actual y). A first, poor line is tried.", s: { i: 0 } }, { cap: "The <b>differences</b> between the predicted values (on the line) and the actual values are the red lines. The goal is to <b>minimise</b> them.", s: { i: 1 } }, { cap: "The best-fit line is found. Its total error is the smallest possible, and it can now be used to <b>predict</b> y for a new x.", s: { i: 2 } }] });
})();

(function () {
  const x = [1, 1], b = $("#nB"); let w1 = 0.8, w2 = -0.4, bi = 0.1;
  const paint = () => { const z = x[0] * w1 + x[1] * w2 + bi, a = sig(z); $("#nV").innerHTML = `Total = ${x[0]} × ${w1} + ${x[1]} × ${w2} + ${bi} = <b>${fmt(z)}</b>. Activation (sigmoid) = <b>${a.toFixed(3)}</b>. ${a >= 0.5 ? "The neuron fires (output near 1)." : "The neuron stays quiet (output near 0)."}`; b.querySelectorAll("button").forEach((y, i) => { y.textContent = "Input " + (i + 1) + " = " + x[i]; y.className = x[i] ? "on" : ""; }); };
  [0, 1].forEach((i) => { const y = document.createElement("button"); y.onclick = () => { x[i] ^= 1; paint(); }; b.appendChild(y); });
  Lib.slider($("#nW1"), { id: "w1", label: "Weight 1 ", min: -20, max: 20, value: 8, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { w1 = v / 10; paint(); } });
  Lib.slider($("#nW2"), { id: "w2", label: "Weight 2 ", min: -20, max: 20, value: -4, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { w2 = v / 10; paint(); } });
  Lib.slider($("#nBi"), { id: "bi", label: "Bias ", min: -20, max: 20, value: 1, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { bi = v / 10; paint(); } }); paint();
})();
(function () {
  const DATA = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]; let w = [0.1, -0.2], bi = 0.0, ep = 0; const hist = []; const b = $("#tB");
  const err = () => DATA.reduce((a, [x1, x2, t]) => a + Math.abs(t - sig(x1 * w[0] + x2 * w[1] + bi)), 0);
  const round = () => { DATA.forEach(([x1, x2, t]) => { const o = sig(x1 * w[0] + x2 * w[1] + bi), d = (o - t) * o * (1 - o); w[0] -= 2 * d * x1; w[1] -= 2 * d * x2; bi -= 2 * d; }); ep++; hist.push(err()); if (hist.length > 8) hist.shift(); };
  const paint = () => { $("#tT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>x1</th><th>x2</th><th>expected</th><th>output</th></tr>' + DATA.map(([x1, x2, t]) => { const o = sig(x1 * w[0] + x2 * w[1] + bi); return `<tr><td>${x1}</td><td>${x2}</td><td>${t}</td><td style="color:${Math.abs(o - t) < 0.3 ? "var(--good)" : "var(--bad)"};font-weight:700">${o.toFixed(2)}</td></tr>`; }).join("") + "</table></div>";
    $("#tV").innerHTML = `Rounds of training: <b>${ep}</b>. Weights: ${w.map(fmt).join(", ")}, bias ${fmt(bi)}. Total error <b>${err().toFixed(2)}</b>` + (hist.length > 1 ? " (recent: " + hist.map((h) => h.toFixed(2)).join(" → ") + ")" : "") + ". The error falls as the weights are adjusted."; };
  [["Train 1 round", 1], ["Train 100 rounds", 100], ["Reset", 0]].forEach(([t, k]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = () => { if (!k) { w = [0.1, -0.2]; bi = 0; ep = 0; hist.length = 0; } else for (let i = 0; i < k; i++) round(); paint(); }; b.appendChild(x); }); paint();
})();
(function () {
  const D = [[1, 2.2], [2, 3.1], [3, 4.4], [4, 4.8], [5, 6.2], [6, 6.9], [7, 8.3]]; let m = 0.5, c = 3; const X = (x) => 40 + x * 55, Y = (y) => 230 - y * 24;
  const n = D.length, sx = D.reduce((a, d) => a + d[0], 0), sy = D.reduce((a, d) => a + d[1], 0), sxy = D.reduce((a, d) => a + d[0] * d[1], 0), sxx = D.reduce((a, d) => a + d[0] * d[0], 0), bm = (n * sxy - sx * sy) / (n * sxx - sx * sx), bc = (sy - bm * sx) / n;
  const paint = () => { let o = '<path d="M40,20 V230 H440" class="ax"/>'; D.forEach(([x, y]) => (o += `<line x1="${X(x)}" y1="${Y(y)}" x2="${X(x)}" y2="${Y(m * x + c)}" stroke="var(--bad)" stroke-width="1.5" opacity=".7"/>`)); D.forEach(([x, y]) => (o += `<circle cx="${X(x)}" cy="${Y(y)}" r="5" class="dot1"/>`)); o += `<line x1="${X(0.4)}" y1="${Y(m * 0.4 + c)}" x2="${X(7.6)}" y2="${Y(m * 7.6 + c)}" stroke="var(--good)" stroke-width="3"/>`;
    $("#gG").innerHTML = `<svg viewBox="0 0 480 250" style="width:480px;max-width:100%;display:block">${o}</svg>`; const e = D.reduce((a, [x, y]) => a + (y - (m * x + c)) ** 2, 0), eb = D.reduce((a, [x, y]) => a + (y - (bm * x + bc)) ** 2, 0);
    $("#gV").innerHTML = `y = ${m.toFixed(2)}x + ${c.toFixed(2)}. Sum of squared differences: <b>${e.toFixed(2)}</b> (the best possible is ${eb.toFixed(2)}). Prediction for x = 8: <b>${(m * 8 + c).toFixed(1)}</b>.`; };
  Lib.slider($("#gS"), { id: "gs", label: "Slope ", min: 0, max: 30, value: 5, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { m = v / 10; paint(); } });
  Lib.slider($("#gI"), { id: "gi", label: "Intercept ", min: -20, max: 60, value: 30, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { c = v / 10; paint(); } });
  const b = $("#gB"), x = document.createElement("button"); x.textContent = "Best fit"; x.onclick = () => { m = bm; c = bc; paint(); }; b.appendChild(x); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which layer of an artificial neural network?", buckets: [{"label": "Input layer"}, {"label": "Hidden layer"}, {"label": "Output layer"}], items: [{"text": "Receives the data", "b": 0}, {"text": "Extracts characteristics from the data", "b": 1}, {"text": "Gives the result", "b": 2}, {"text": "A deep network has many of these", "b": 1}, {"text": "One node for each input value", "b": 0}, {"text": "Feeds the next layer after analysing", "b": 1}], done: "Input receives, hidden extracts, output gives the answer." });
Lib.classify($("#cl2"), { prompt: "Back propagation or regression?", buckets: [{"label": "Back propagation"}, {"label": "Regression"}], items: [{"text": "Feeds the error back through the network", "b": 0}, {"text": "Finds a best-fit line between variables", "b": 1}, {"text": "Adjusts the weights of the nodes", "b": 0}, {"text": "Forecasts trends from past data", "b": 1}, {"text": "Compares the output with the expected output", "b": 0}, {"text": "Maps independent variables to a dependent variable", "b": 1}], done: "Back propagation trains network weights; regression fits a function." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Weight", "A value on a connection that training adjusts"], ["Hidden layer", "A layer between input and output where characteristics are extracted"], ["Back propagation", "Errors are fed back to adjust the weights"], ["Regression", "A supervised method that fits a best-fit line or curve"], ["Error gradient", "Found using calculus to see how to change each weight"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of training with back propagation in order.", items: ["Feed data forward through the network", "Compare the output with the expected output", "Work out the error and feed it back through the network", "Adjust the weights to reduce the error", "Repeat until the results are accurate"], done: "Forward, compare, feed back, adjust, repeat." });
Lib.calc($("#c1"), { qs: [
  {"q": "A neuron has inputs 1 and 1, weights 0.5 and 0.5, and bias 0. What is the total?", "a": 1, "unit": "", "tol": 0.01, "hint": "0.5 + 0.5.", "sol": "<b>1</b>."},
  {"q": "A network has an input layer of 3 nodes, a hidden layer of 4 and an output of 2. How many connections between the input and hidden layers (every node to every node)?", "a": 12, "unit": "", "tol": 0.01, "hint": "3 × 4.", "sol": "<b>12</b>."},
  {"q": "And between the hidden and output layers?", "a": 8, "unit": "", "tol": 0.01, "hint": "4 × 2.", "sol": "<b>8</b>."},
  {"q": "The expected output is 1 and the network outputs 0.6. What is the error?", "a": 0.4, "unit": "", "tol": 0.01, "hint": "1 − 0.6.", "sol": "<b>0.4</b>."},
  {"q": "A regression line is y = 2x + 1. What does it predict for x = 5?", "a": 11, "unit": "", "tol": 0.01, "hint": "2 × 5 + 1.", "sol": "<b>11</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does an artificial neural network simulate?", opts: ["A biological brain", "A hard disk", "A monitor", "A keyboard"], a: 0, why: "The brain." },
  { q: "What is adjusted during training?", opts: ["The weights", "The screen", "The power", "The font"], a: 0, why: "The weights." },
  { q: "Back propagation feeds back:", opts: ["The error", "The input only", "The password", "The file name"], a: 0, why: "The error." },
  { q: "Regression is a type of:", opts: ["Supervised learning", "Reinforcement only", "Encryption", "Sorting"], a: 0, why: "Supervised." },
  { q: "The goal of regression is to:", opts: ["Maximise the error", "Minimise the difference between predicted and actual values", "Delete data", "Add layers"], a: 1, why: "Minimise the difference." },
  { q: "More hidden layers lead to:", opts: ["Deeper learning of complex features", "Fewer weights", "No learning", "Smaller data"], a: 0, why: "More complex learning." },
] });
Lib.cards($("#fc1"), { cards: [
  ["ANN", "Layers of connected nodes simulating the brain."],
  ["Layers", "Input, hidden (one or many), output."],
  ["Weight", "Value on a connection, adjusted in training."],
  ["Back propagation", "Compare, feed back the error, adjust weights, repeat."],
  ["Error gradient", "Found with calculus."],
  ["Regression", "Best-fit function between variables; supervised."],
  ["Forecasting", "A use of regression."],
  ["Deep learning", "ANN with many hidden layers."],
] });
