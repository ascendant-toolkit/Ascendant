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

function lcg(seed) { let s = seed; return () => ((s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff); }
function pts(seed) { const r = lcg(seed), out = []; for (let i = 0; i < 8; i++) out.push([60 + r() * 140, 40 + r() * 120, 0]); for (let i = 0; i < 8; i++) out.push([320 + r() * 140, 110 + r() * 120, 1]); return out; }
const P = pts(5);
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "labelled training data", "sm");
    P.forEach(([x, y, c], i) => { o += SV.circle(x, y, 8, c ? "dot2" : "dot1"); });
    if (k >= 1) o += SV.text(300, 20, "labels: red = spam, blue = ok", "sm");
    if (k >= 2) o += SV.path("M260,20 L260,260", "ax", { style: "stroke-dasharray:6 5;stroke:var(--accent)" }) + SV.text(262, 275, "learned boundary", "sm");
    if (k >= 3) o += SV.circle(420, 70, 9, "dot4") + SV.text(420, 55, "new?", "sm", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(300, 56, "predicted: ok", "lbl bd t3", { style: "font-size:12px", "text-anchor": "start" }) + SV.text(20, 292, "", "sm"); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 290, label: "Supervised", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "A set of examples with data points (blue and red). At first the system knows only the points.", s: { i: 0 } }, { cap: "Each example comes with a <b>label</b> supplied by people: the known output (ok or spam).", s: { i: 1 } }, { cap: "The system <b>learns a mapping</b> from the inputs to the labels, here a boundary between the two groups.", s: { i: 2 } }, { cap: "A <b>new, unlabelled</b> point arrives.", s: { i: 3 } }, { cap: "The system <b>predicts</b> its label from what it learned.", s: { i: 4 } }].map((x) => ({ cap: x.cap, s: x.s })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "unlabelled data: no known outputs", "sm");
    P.forEach(([x, y, c]) => (o += SV.circle(x, y, 8, k >= 2 ? (c ? "dot2" : "dot1") : "dot3")));
    if (k >= 1) o += SV.circle(130, 100, 5, "dot4") + SV.circle(390, 170, 5, "dot4") + SV.text(130, 128, "centre 1", "sm", { "text-anchor": "middle" }) + SV.text(390, 198, "centre 2", "sm", { "text-anchor": "middle" });
    if (k >= 3) o += SV.rect(40, 30, 180, 150, "ax", { rx: 14, fill: "none", style: "stroke:var(--accent);stroke-dasharray:6 5" }) + SV.rect(300, 90, 180, 160, "ax", { rx: 14, fill: "none", style: "stroke:var(--bad);stroke-dasharray:6 5" }); if (k >= 3) o += SV.text(20, 275, "two clusters found, nobody labelled them", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 290, label: "Unsupervised", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "The data has <b>no labels</b>. The system does not know what the points are.", s: { i: 0 } }, { cap: "It looks for structure: it places some trial group centres.", s: { i: 1 } }, { cap: "Each point joins the nearest group, and the centres move to fit the groups.", s: { i: 2 } }, { cap: "Two <b>clusters</b> are found: hidden patterns discovered with no human help.", s: { i: 3 } }] });
})();
(function () {
  const loop = [["Agent", "chooses an action"], ["Environment", "responds to the action"], ["Feedback", "reward (+) or punishment (−)"], ["Agent", "adjusts how it chooses next time"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(30, 40, 160, 60, k === 0 || k === 3 ? "cell-warn" : "cell", { rx: 10 }) + SV.text(110, 76, "Agent", "lbl bd", { "text-anchor": "middle" }) + SV.rect(330, 40, 160, 60, k === 1 ? "cell-warn" : "cell", { rx: 10 }) + SV.text(410, 76, "Environment", "lbl bd", { "text-anchor": "middle" });
    if (k >= 0) o += SV.path("M190,58 H330", "ax") + SV.arrowHead(330, 58, "r", "arr") + SV.text(260, 50, "action", "sm", { "text-anchor": "middle" });
    if (k >= 2) o += SV.path("M330,86 H190", "ax", { style: "stroke:" + (k === 2 ? "var(--good)" : "var(--muted)") + ";stroke-width:3" }) + SV.arrowHead(190, 86, "l", "arr") + SV.text(260, 112, "reward / punishment", "sm", { "text-anchor": "middle" });
    if (k >= 3) o += SV.text(110, 140, "learns: do more of what earned a reward", "lbl bd t3", { "text-anchor": "start", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 170, label: "Reinforcement", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: loop.map((x, i) => ({ cap: `<b>${x[0]}</b> ${x[1]}.`, s: { i } })) });
})();

(function () {
  let labels = true; const b = $("#sB"); let newPt = [260, 120], cl = null;
  const nearest = () => P.reduce((m, p) => (Math.hypot(p[0] - newPt[0], p[1] - newPt[1]) < Math.hypot(m[0] - newPt[0], m[1] - newPt[1]) ? p : m));
  const kmeans = () => { let c = [[100, 100], [400, 180]]; let asg = P.map(() => 0); for (let it = 0; it < 6; it++) { asg = P.map((p) => (Math.hypot(p[0] - c[0][0], p[1] - c[0][1]) <= Math.hypot(p[0] - c[1][0], p[1] - c[1][1]) ? 0 : 1)); c = [0, 1].map((k) => { const m = P.filter((_, i) => asg[i] === k); return m.length ? [m.reduce((a, p) => a + p[0], 0) / m.length, m.reduce((a, p) => a + p[1], 0) / m.length] : c[k]; }); } return { asg, c }; };
  const paint = () => { let o = ""; const km = kmeans();
    P.forEach(([x, y, c], i) => { const col = labels ? (c ? "dot2" : "dot1") : "dot3"; o += SV.circle(x, y, 8, col); if (!labels) o += SV.circle(x, y, 12, "ax", { fill: "none", style: "stroke:" + (km.asg[i] ? "var(--bad)" : "var(--accent)") + ";stroke-width:2" }); });
    const near = nearest(); if (labels) o += SV.circle(newPt[0], newPt[1], 9, "dot4") + SV.path("M" + newPt[0] + "," + newPt[1] + " L" + near[0] + "," + near[1], "ax", { style: "stroke-dasharray:4 4" });
    $("#sG").innerHTML = `<svg viewBox="0 0 520 260" style="width:520px;max-width:100%;display:block;cursor:crosshair" id="svgS">${o}</svg>`;
    $("#svgS").onclick = (e) => { if (!labels) return; const r = e.currentTarget.getBoundingClientRect(); newPt = [((e.clientX - r.left) / r.width) * 520, ((e.clientY - r.top) / r.height) * 260]; paint(); };
    $("#sV").innerHTML = labels ? `<b>Supervised</b>: the points carry labels (colours). The new point (yellow) is classified as <b>${near[2] ? "red" : "blue"}</b>, the label of its nearest labelled neighbour. Click the graph to move it.` : "<b>Unsupervised</b>: no labels. The computer groups the points itself and finds <b>2 clusters</b> (the rings). It does not know what the groups mean.";
    b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "s") === labels ? "on" : "")); };
  [["s", "Supervised (labels)"], ["u", "Unsupervised (no labels)"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { labels = k === "s"; paint(); }; b.appendChild(x); }); paint();
})();
(function () {
  const prob = [0.2, 0.7, 0.4], q = [0, 0, 0], n = [0, 0, 0]; const rnd = lcg(3); let trials = 0, total = 0; const b = $("#rB");
  const step = () => { const eps = 0.15; let a = rnd() < eps || trials < 3 ? Math.floor(rnd() * 3) : q.indexOf(Math.max(...q)); const r = rnd() < prob[a] ? 1 : 0; n[a]++; q[a] += (r - q[a]) / n[a]; trials++; total += r; };
  const paint = () => { $("#rT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Lever</th><th>Times chosen</th><th>Estimated reward (learned)</th></tr>' + [0, 1, 2].map((i) => `<tr><td>${i + 1}</td><td>${n[i]}</td><td>${n[i] ? q[i].toFixed(2) : "?"}</td></tr>`).join("") + "</table></div>";
    $("#rV").innerHTML = trials ? `After <b>${trials}</b> trials the agent has earned <b>${total}</b> rewards. It chooses the lever with the best estimate most of the time and tries others now and then. The hidden payout rates are 20%, 70% and 40%: lever 2 is best.` : "Press Train. At first the agent tries levers at random."; };
  [["Train 10 trials", 10], ["Train 100 trials", 100], ["Reset", 0]].forEach(([t, k]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = () => { if (!k) { q.fill(0); n.fill(0); trials = 0; total = 0; } else for (let i = 0; i < k; i++) step(); paint(); }; b.appendChild(x); }); paint();
})();
btnTable("mB", "mO", [
  ["Sort photos into known categories using thousands of tagged examples", "Supervised learning", "Labelled data with known outputs"],
  ["Group customers by behaviour with no categories decided", "Unsupervised learning", "Unlabelled data; find clusters"],
  ["A program learns to play a game by playing it many times", "Reinforcement learning", "Rewards and punishments for actions"],
  ["Recognise faces using a neural network with many hidden layers", "Deep learning", "Many layers extract features from large data"],
  ["Predict next month's sales from past sales", "Supervised learning", "Past data with known outcomes"],
  ["Find unusual patterns in network traffic with no labels", "Unsupervised learning", "Hidden patterns in unlabelled data"]
], ["Situation", "Method", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which category of machine learning?", buckets: [{"label": "Supervised"}, {"label": "Unsupervised"}, {"label": "Reinforcement"}], items: [{"text": "Uses labelled training data", "b": 0}, {"text": "Finds hidden clusters in unlabelled data", "b": 1}, {"text": "An agent learns from rewards and punishments", "b": 2}, {"text": "Needs initial human input to label data", "b": 0}, {"text": "Learns by trial and error in an environment", "b": 2}, {"text": "Needs no human intervention to find groupings", "b": 1}], done: "Labelled: supervised. Unlabelled: unsupervised. Feedback: reinforcement." });
Lib.classify($("#cl2"), { prompt: "Is it a reason for using deep learning?", buckets: [{"label": "Yes"}, {"label": "No"}], items: [{"text": "It uses unstructured data well", "b": 0}, {"text": "It outperforms other methods with large data sets", "b": 0}, {"text": "It finds hidden patterns humans might not see", "b": 0}, {"text": "It needs no data at all", "b": 1}, {"text": "More hidden layers can give more accurate results", "b": 0}, {"text": "It always works best with very small data sets", "b": 1}], done: "Deep learning suits large and unstructured data." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Supervised learning", "Mapping inputs to outputs from example input–output pairs"], ["Unsupervised learning", "Discovering patterns on its own that were previously undetected"], ["Reinforcement learning", "Learning in an interactive environment by trial and error"], ["Deep learning", "A neural network with many hidden layers, like the brain"], ["Back propagation", "Passing information about errors back through the network"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the reinforcement learning loop in order.", items: ["The agent chooses an action", "The environment responds", "The agent receives a reward or punishment", "The agent adjusts how it chooses actions", "It tries again and gets better at the task"], done: "Action, response, feedback, adjust, repeat." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many categories of machine learning are named in the syllabus (supervised, unsupervised, reinforcement)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Three.", "sol": "<b>3</b>."},
  {"q": "A deep learning network has an input layer, 4 hidden layers and an output layer. How many layers in total?", "a": 6, "unit": "", "tol": 0.01, "hint": "1 + 4 + 1.", "sol": "<b>6</b>."},
  {"q": "A supervised data set has 1000 examples and 25% are labelled spam. How many are spam?", "a": 250, "unit": "", "tol": 0.5, "hint": "1000 × 0.25.", "sol": "<b>250</b>."},
  {"q": "An agent gets +1 for a good action and −1 for a bad action. After 7 good and 3 bad actions, what is its total reward?", "a": 4, "unit": "", "tol": 0.01, "hint": "7 − 3.", "sol": "<b>4</b>."},
  {"q": "How many of the three categories (supervised, unsupervised, reinforcement) use labelled training data?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only supervised.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Supervised learning uses:", opts: ["Labelled data", "No data", "Only rewards", "Only images"], a: 0, why: "Labelled data." },
  { q: "Which finds hidden patterns in unlabelled data?", opts: ["Supervised", "Unsupervised", "Reinforcement", "None"], a: 1, why: "Unsupervised." },
  { q: "In reinforcement learning an agent receives:", opts: ["Labelled data", "Rewards and punishments", "Passwords", "Nothing"], a: 1, why: "Feedback." },
  { q: "Deep learning is:", opts: ["Part of machine learning", "Unrelated to AI", "A type of storage", "A database"], a: 0, why: "A branch of machine learning." },
  { q: "More hidden layers usually make deep learning:", opts: ["Less effective", "More effective", "Unchanged", "Unusable"], a: 1, why: "More effective." },
  { q: "Which subset of AI uses an artificial neural network?", opts: ["Deep learning", "Sorting", "Compression", "Encryption"], a: 0, why: "Deep learning." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Supervised", "Labelled data; known outputs; predicts future outcomes."],
  ["Unsupervised", "Unlabelled data; hidden patterns and clusters."],
  ["Reinforcement", "Agent; environment; reward and punishment; trial and error."],
  ["Deep learning", "Neural network with many hidden layers."],
  ["Why deep learning", "Unstructured and large data; hidden patterns; non-linear."],
  ["Make it better", "More hidden layers."],
  ["AI > ML > DL", "Deep learning is part of machine learning, part of AI."],
  ["Back propagation", "Errors fed back to adjust weights (18.1.4)."],
] });
