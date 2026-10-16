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

Lib.stepper($("#stS"), { w: 760, h: 400, label: "Demand-led and supply-led growth", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b> with some spare capacity.", s: { sh: 0, a: 0 } },
  { cap: "<b>Growth from higher demand:</b> consumption, investment, government spending or exports rise. AD shifts <b>right</b>. Real GDP rises and prices rise a little.", s: { sh: 14, a: 0 } },
  { cap: "<b>Evaluate:</b> push AD too far and the economy runs short of capacity. Output barely rises and most of the effect is <b>inflation</b>.", s: { sh: 40, a: 0 } },
  { cap: "<b>Growth from more or better resources:</b> AS shifts <b>right</b>. Real GDP rises and the price level <b>falls</b>: growth that can be sustained.", s: { sh: 0, a: 14 } },
] });
const GCH = ["Growth rises: real GDP and incomes increase", "Firms hire more workers: unemployment falls", "Higher incomes and profits raise tax revenue", "The government can spend more on services or cut its deficit", "But: more output may cause pollution and resource depletion", "And: gains may be unequal; imports and prices may rise"];
Lib.stepper($("#stB"), { w: 760, h: 400, label: "Benefits and costs of growth", base: { n: 0 }, draw: mkChain(GCH, "--good"), steps: chainSteps(["<b>Growth:</b> real GDP and incomes increase.", "<b>Jobs:</b> firms hire more workers and unemployment falls.", "<b>Tax revenue:</b> higher incomes and profits raise what the government collects.", "<b>Public services:</b> the government can spend more on health and education, or reduce its deficit.", "<b>Cost:</b> more output may mean more pollution and use of resources.", "<b>Cost:</b> the gains may be unequal, and higher incomes raise imports and may raise prices."]) });

/* Lab 1: AD vs AS growth */
function labC() {
  if (!$("#ca") || !$("#cb")) return;
  const sh = +$("#ca").value, a = +$("#cb").value, [y, p] = solve2(sh, a);
  $("#ca1").textContent = "+" + money(y - 50, 1); $("#ca2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#ca3").textContent = a > 0 && sh > 0 ? "Both" : a > 0 ? "Quantity or quality of resources" : sh > 0 ? "Demand" : "None";
  $("#cav").textContent = a === 0 && sh === 0 ? "Move a slider." : a === 0 ? `AD rises: output +${money(y - 50, 1)} but the price level +${money(p - 50, 1)}. Demand-led growth brings more inflationary pressure.` : sh === 0 ? `AS rises: output +${money(y - 50, 1)} and the price level ${p - 50 >= 0 ? "+" : "−"}${money(Math.abs(p - 50), 1)}. Supply-led growth can be sustained.` : "Both shift: strong growth with a modest change in prices.";
  $("#labC").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g1"), { id: "ca", label: "Rise in total demand (AD shift)", min: 0, max: 40, step: 2, value: 12, fmt: (v) => "+" + v, onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "More or better resources (AS shift)", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labC });
/* Lab 2: winners and losers */
const WL = [
  { n: "Consumers", g: "Higher incomes and more choice; cheaper goods as firms expand.", c: "Higher prices if demand outpaces supply; pollution and congestion." },
  { n: "Workers", g: "More jobs, higher wages and more promotion chances.", c: "Pressure to work harder; those without the right skills may be left behind." },
  { n: "Producers and firms", g: "More sales and profit; funds for investment.", c: "Higher wage and input costs; stricter rules to limit pollution." },
  { n: "The government", g: "More tax revenue, fewer benefit payments.", c: "Calls for more spending on infrastructure and cleaning up pollution." },
  { n: "The environment", g: "Richer countries may pay for cleaner technology.", c: "More emissions, waste and depletion of resources." },
  { n: "Future generations", g: "Investment now leaves more capital and skills.", c: "Resources used up and pollution left behind." },
];
button_table("wlBtns", "wlOut", WL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible benefit</th><th>Possible cost</th></tr><tr><td>${p.g}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a cause of growth from <b>higher demand</b>, <b>more resources</b> or <b>better resources</b>?", buckets: [{ label: "Higher demand" }, { label: "More resources" }, { label: "Better resources" }], items: [
  { text: "Government spending rises", b: 0 }, { text: "Exports increase", b: 0 }, { text: "Interest rates fall, so firms invest", b: 0 },
  { text: "Immigration raises the labour force", b: 1 }, { text: "Oil is discovered", b: 1 }, { text: "New factories are built", b: 1 },
  { text: "Workers receive more training", b: 2 }, { text: "New technology raises productivity", b: 2 }, { text: "Better healthcare reduces sick days", b: 2 },
], done: "Demand, quantity, quality: the three causes in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of economic growth?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Higher incomes", b: 0 }, { text: "Fewer people unemployed", b: 0 }, { text: "More tax revenue for schools", b: 0 }, { text: "Higher profits for firms", b: 0 },
  { text: "More pollution", b: 1 }, { text: "Resources are used up", b: 1 }, { text: "Richer households gain most", b: 1 }, { text: "Higher imports and a worse current account", b: 1 },
], done: "Always give both sides." });
Lib.match($("#m1"), { prompt: "Match the cause to the effect on the diagrams.", pairs: [
  ["Rise in consumer spending", "AD shifts right"],
  ["Immigration of workers", "AS shifts right: more labour"],
  ["Training programme", "AS shifts right: better labour"],
  ["Discovery of a mineral deposit", "AS shifts right: more land"],
  ["Investment in new machines", "AS shifts right: more capital"],
  ["New technology", "AS shifts right: higher productivity"],
], done: "Link each cause to a diagram." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how higher government spending could cause growth</b>.", items: [
  "The government spends more on infrastructure",
  "Firms and workers are paid and spend part of it",
  "Aggregate demand shifts to the right",
  "Real GDP rises: economic growth",
  "Firms hire more workers and tax revenue rises",
], done: "A demand-led growth chain." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP rises from $250bn to $260bn. What is the growth rate (%)?", a: 4, sol: "10 ÷ 250 × 100 = <b>4%</b>." },
  { q: "The labour force rises from 20 million to 21 million and output per worker stays the same. By what percentage does output rise?", a: 5, sol: "1 ÷ 20 × 100 = <b>5%</b>." },
  { q: "Growth raises tax revenue from $50bn to $56bn. What is the percentage rise in tax revenue?", a: 12, sol: "6 ÷ 50 × 100 = <b>12%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which could cause economic growth by increasing the quality of resources?", opts: ["Immigration", "A rise in exports", "Training and education", "A tax cut"], a: 2, why: "Training improves the quality of labour." },
  { q: "Which is a possible disadvantage of economic growth?", opts: ["Higher incomes", "More jobs", "More pollution", "More tax revenue"], a: 2, why: "Higher output can mean more emissions." },
  { q: "A rise in total demand when the economy has spare capacity is most likely to cause:", opts: ["Growth with little inflation", "Falling output", "Higher unemployment", "A lower exchange rate only"], a: 0, why: "Spare resources can be used." },
  { q: "Which is most likely to raise an economy's capacity in the long run?", opts: ["Higher consumer spending", "Investment in capital and skills", "A fall in interest rates", "Lower exports"], a: 1, why: "More and better resources shift AS." },
  { q: "Economic growth could conflict with the balance of payments because:", opts: ["Higher incomes raise spending on imports", "Higher incomes reduce imports", "It lowers the exchange rate", "It raises exports only"], a: 0, why: "More income means more imports." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Total demand", "Aggregate demand: C + I + G + (X − M)."],
  ["Quantity of resources", "The amount of land, labour, capital or enterprise available."],
  ["Quality of resources", "How productive resources are, for example skills and technology."],
  ["Immigration", "People moving into a country, which can raise the labour force."],
  ["Investment", "Spending on capital goods such as machinery and buildings."],
  ["Environmental sustainability", "Meeting today's needs without damaging the ability of future generations to meet theirs."],
  ["Inequality", "An unequal distribution of income or wealth."],
  ["Living standards", "The quality and quantity of goods and services people can obtain."],
] });
labC();
