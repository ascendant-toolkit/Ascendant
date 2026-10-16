const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

const SC = ["People have unlimited wants", "But resources (land, labour, capital, enterprise) are finite", "Not everything can be produced or bought: scarcity", "People, firms and governments must make choices", "Every choice gives up the next best alternative: opportunity cost"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "From wants to scarcity", base: { n: 0 }, draw: mkChain(SC, "--accent"), steps: chainSteps(["People have <b>unlimited wants</b>.", "But <b>resources are finite</b>: land, labour, capital and enterprise.", "Not everything can be produced or bought: <b>scarcity</b>.", "People, firms and governments must <b>make choices</b>.", "Every choice gives up the next best alternative: <b>opportunity cost</b>."]) });
function gapChart(s) {
  let o = SV.line(60, 300, 700, 300) + SV.text(60, 26, "Wants and resources over time", "sm");
  const lab = ["Today", "Next year", "In 5 years"], res = [100, 108, 140], wants = [160, 190, 300];
  lab.forEach((l, i) => { const x = 110 + i * 200, op = clamp(s.n - i, 0, 1); if (op <= 0) return; o += `<g opacity="${op}">` + SV.rect(x, 300 - res[i], 70, res[i], "", { style: "fill:var(--good)", opacity: 0.85 }) + SV.text(x + 35, 300 - res[i] - 6, "Resources", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.rect(x + 80, 300 - wants[i] * 0.9, 70, wants[i] * 0.9, "", { style: "fill:var(--bad)", opacity: 0.85 }) + SV.text(x + 115, 300 - wants[i] * 0.9 - 6, "Wants", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + 75, 322, l, "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 340, label: "The gap never closes", base: { n: 0 }, draw: gapChart, steps: [
  { cap: "Today wants exceed resources: a <b>gap</b> (illustrative figures).", s: { n: 1 } },
  { cap: "Resources grow with better technology and investment, but wants grow faster.", s: { n: 2 } },
  { cap: "Even with more resources, the gap remains: <b>scarcity never disappears</b>.", s: { n: 3 } },
] });

/* Lab 1: budget choice */
function labB() {
  if (!$("#ba") || !$("#bb")) return;
  const inc = +$("#ba").value, food = +$("#bb").value, wantsList = [["Phone", 600], ["Holiday", 800], ["Games console", 400], ["New clothes", 300], ["Concert tickets", 200]];
  let left = inc - food, got = [], skipped = []; wantsList.forEach(([n, c]) => { if (c <= left) { left -= c; got.push(n); } else skipped.push(n); });
  $("#ba1").textContent = "$" + left; $("#ba2").textContent = got.length; $("#ba3").textContent = skipped.length;
  $("#bav").textContent = `With income $${inc} and $${food} needed for essentials, you can afford: ${got.join(", ") || "none"}. Unaffordable wants: ${skipped.join(", ") || "none"}. Higher income lets you buy more, but the list of wants is never finished. That is scarcity.`;
  const base = 280; let o = SV.line(60, base, 700, base);
  wantsList.forEach(([n, c], i) => { const x = 90 + i * 120, ok = got.includes(n), h = c * 0.24; o += SV.rect(x, base - h, 90, h, "", { style: `fill:var(${ok ? "--good" : "--bad"})`, opacity: ok ? 0.85 : 0.35 }) + SV.text(x + 45, base - h - 6, "$" + c, "sm bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 18, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labB").innerHTML = o + SV.text(60, 24, "Green: bought. Faded red: given up.", "sm");
}
Lib.slider($("#g1"), { id: "ba", label: "Monthly income", min: 500, max: 3000, step: 100, value: 1200, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g2"), { id: "bb", label: "Spending on needs (food, rent)", min: 200, max: 1500, step: 50, value: 700, fmt: (v) => "$" + v, onInput: labB });
const EX = [
  { n: "Consumer", w: "Wants a phone, holiday and car", r: "Limited income", c: "Choose which to buy first" },
  { n: "Worker", w: "Wants more pay and more leisure", r: "Only 24 hours a day", c: "Overtime or free time" },
  { n: "Firm", w: "Wants more machines and staff", r: "Limited finance", c: "Invest in machinery or marketing" },
  { n: "Government", w: "Wants better hospitals, schools, roads", r: "Limited tax revenue", c: "Spend on health or education" },
];
button_table("exBtns", "exOut", EX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Wants</th><th>Limited resource</th><th>Choice</th></tr><tr><td>${p.w}</td><td>${p.r}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> faces each problem?", buckets: [{ label: "Consumer" }, { label: "Worker" }, { label: "Firm" }, { label: "Government" }], items: [
  { text: "Limited income to spend on many goods", b: 0 }, { text: "Choosing between a phone and a holiday", b: 0 },
  { text: "Choosing between overtime and leisure time", b: 1 }, { text: "Only 24 hours in a day", b: 1 },
  { text: "Limited finance to buy machinery and hire staff", b: 2 }, { text: "Deciding which product to make", b: 2 },
  { text: "Limited tax revenue for hospitals and schools", b: 3 }, { text: "Choosing between defence and healthcare", b: 3 },
], done: "Everyone faces scarcity and must choose." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>want</b> or a <b>need</b> (a want is not essential for survival)?", buckets: [{ label: "Need" }, { label: "Want" }], items: [
  { text: "Clean drinking water", b: 0 }, { text: "Basic food", b: 0 }, { text: "Shelter", b: 0 },
  { text: "A designer handbag", b: 1 }, { text: "A holiday abroad", b: 1 }, { text: "The latest games console", b: 1 },
], done: "Wants are unlimited; needs are essential." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Scarcity", "Limited resources compared with unlimited wants"],
  ["Basic economic problem", "Infinite wants but finite resources"],
  ["Finite resources", "Resources limited in supply"],
  ["Wants", "Goods and services people would like to have"],
  ["Needs", "Goods and services essential for survival"],
  ["Choice", "Selecting some alternatives and giving up others"],
], done: "Good definitions score marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>from wants to opportunity cost</b>.", items: [
  "People have unlimited wants",
  "Resources are finite",
  "Scarcity exists",
  "Choices must be made",
  "Each choice has an opportunity cost",
], done: "The logic of the basic economic problem." });
Lib.calc($("#c1"), { qs: [
  { q: "A consumer earns $900 a month and spends $600 on needs. How much is left for wants ($)?", a: 300, sol: "900 − 600 = <b>$300</b>." },
  { q: "A government has $50bn of tax revenue. It spends 30% on healthcare. How much is spent on healthcare ($bn)?", a: 15, sol: "30% × 50 = <b>$15bn</b>." },
  { q: "A worker has 24 hours a day, sleeps 8 and works 8. How many hours are left for leisure?", a: 8, sol: "24 − 8 − 8 = <b>8 hours</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the basic economic problem?", opts: ["Unemployment", "Infinite wants but finite resources", "Inflation", "Too many goods"], a: 1, why: "Scarcity of resources." },
  { q: "Scarcity exists because:", opts: ["Wants are limited", "Resources are limited compared with wants", "Money is scarce only", "Governments exist"], a: 1, why: "Finite resources, infinite wants." },
  { q: "Which country faces the basic economic problem?", opts: ["Only poor countries", "Only rich countries", "All countries", "No country"], a: 2, why: "Every country has finite resources." },
  { q: "For a worker, a scarce resource is:", opts: ["Time", "Free air", "Sunlight", "Space in the ocean"], a: 0, why: "24 hours a day." },
  { q: "Which is an example of a government facing scarcity?", opts: ["Choosing between schools and hospitals", "Printing money freely", "Having a surplus", "No decisions"], a: 0, why: "Limited revenue." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Basic economic problem", "Infinite wants but finite resources."],
  ["Scarcity", "Limited resources compared with unlimited wants."],
  ["Finite resources", "Resources limited in supply."],
  ["Wants", "Goods and services people would like to have; unlimited."],
  ["Needs", "Goods and services essential for survival."],
  ["Choice", "Selecting between alternatives."],
  ["Opportunity cost", "The next best alternative given up."],
  ["Consumer", "A person who buys goods and services."],
  ["Producer", "A firm that makes goods and services."],
] });
labB(); 
