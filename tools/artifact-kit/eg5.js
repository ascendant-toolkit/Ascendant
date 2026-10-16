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

const PCH = ["Government cuts interest rates and raises spending", "Borrowing and spending rise: AD shifts right", "Real GDP rises quickly if there is spare capacity", "But the price level may rise, and imports and the deficit grow", "Government also invests in education and infrastructure", "AS shifts right over time: growth that can last"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Short-run and long-run growth policies", base: { n: 0 }, draw: mkChain(PCH, "--accent"), steps: chainSteps(["<b>Demand-side:</b> the government cuts interest rates and raises spending.", "Borrowing and spending rise: <b>AD shifts right</b>.", "If there is <b>spare capacity</b>, real GDP rises quickly.", "<b>Cost:</b> the price level may rise, imports rise and the deficit grows.", "<b>Supply-side:</b> the government also invests in education and infrastructure.", "<b>AS shifts right</b> over the years: higher capacity, so growth can last with less inflation."]) });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Demand-side and supply-side policy", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "<b>Demand-side policy</b> (lower interest rates, higher spending, lower taxes): AD shifts right. Output rises quickly but the price level rises.", s: { sh: 14, a: 0 } },
  { cap: "<b>Supply-side policy</b> (education, infrastructure, deregulation): AS shifts right over time. Output rises and the price level falls.", s: { sh: 0, a: 14 } },
  { cap: "A <b>mix of both</b> gives strong growth with a stable price level: demand-side policy for the short run and supply-side policy for the long run.", s: { sh: 14, a: 14 } },
] });

/* Lab 1: policy simulator */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc")) return;
  const f = +$("#pa").value, m = +$("#pb").value, s = +$("#pc").value, sh = f + m, [y, p] = solve2(sh, s);
  $("#pa1").textContent = "+" + money(y - 50, 1); $("#pa2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#pa3").textContent = y > 60 ? "High" : y > 54 ? "Medium" : "Low";
  $("#pav").textContent = sh === 0 && s === 0 ? "Choose a policy mix." : `Output rises by ${money(y - 50, 1)} and the price level by ${p - 50 >= 0 ? "+" : "−"}${money(Math.abs(p - 50), 1)}. ${y - 50 > 2 * Math.max(0.1, p - 50) ? "Most of the effect is extra output: growth with limited inflation." : "A large share is inflation: policy may be pushing against capacity."}${s === 0 && sh > 25 ? " Demand-side policy on its own is running out of room." : ""}${s > 0 ? " The supply-side part takes years to build." : ""}`;
  $("#labP").innerHTML = adasChart({ sh, a: s });
}
Lib.slider($("#g1"), { id: "pa", label: "Fiscal policy (AD shift)", min: 0, max: 25, step: 1, value: 8, fmt: (v) => "+" + v, onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Monetary policy (AD shift)", min: 0, max: 25, step: 1, value: 8, fmt: (v) => "+" + v, onInput: labP });
Lib.slider($("#g3"), { id: "pc", label: "Supply-side policy (AS shift)", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labP });
/* Lab 2: policy picker */
const PL = [
  { n: "Cut interest rates", t: "Monetary", w: "Cheaper borrowing raises consumption and investment.", sp: "Fast to change; effects take months", c: "Weak if confidence is low; may raise inflation and imports; hurts savers." },
  { n: "Raise government spending", t: "Fiscal", w: "G adds to AD with a multiplier effect; infrastructure and education raise capacity.", sp: "Medium", c: "Bigger deficit and debt; opportunity cost; inflation near capacity." },
  { n: "Cut taxes", t: "Fiscal", w: "More disposable income raises C; corporation tax cuts raise I.", sp: "Medium", c: "Part may be saved; revenue falls; may widen inequality." },
  { n: "Education and training", t: "Supply-side", w: "A more skilled workforce raises productivity and AS.", sp: "Slow (years)", c: "Costly; skills must match jobs." },
  { n: "Infrastructure", t: "Supply-side", w: "Better transport and power lower costs and raise capacity.", sp: "Slow (years)", c: "Large cost, delays, environmental damage." },
  { n: "Lower the exchange rate", t: "Monetary", w: "Cheaper exports and dearer imports raise net exports.", sp: "Medium", c: "Imported inflation; depends on elasticity." },
  { n: "Attract foreign investment", t: "Investment", w: "Multinationals bring capital, jobs and technology.", sp: "Medium", c: "Profits sent abroad; competition for local firms." },
  { n: "Free trade agreements", t: "Trade", w: "Larger markets and competition raise exports and efficiency.", sp: "Medium to slow", c: "Some firms and workers lose out; dependence on other economies." },
];
button_table("plBtns", "plOut", PL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>How it promotes growth</th><th>Speed</th><th>The catch</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td><td>${p.sp}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of policy</b> is each?", buckets: [{ label: "Fiscal" }, { label: "Monetary" }, { label: "Supply-side" }, { label: "Investment or trade" }], items: [
  { text: "Cut income tax", b: 0 }, { text: "Build new hospitals", b: 0 },
  { text: "Cut interest rates", b: 1 }, { text: "Allow the currency to fall", b: 1 },
  { text: "Fund training for workers", b: 2 }, { text: "Privatise state firms", b: 2 },
  { text: "Tax breaks for firms that invest", b: 3 }, { text: "Sign a free trade agreement", b: 3 },
], done: "Know the five groups of policies." });
Lib.classify($("#cl2"), { prompt: "Which policy fits each <b>situation</b>? Weak demand needs <b>demand-side</b> policy; low capacity needs <b>supply-side</b> policy.", buckets: [{ label: "Demand-side policy fits" }, { label: "Supply-side policy fits" }], items: [
  { text: "Unemployed workers and unused factories after a slump", b: 0 }, { text: "Consumer confidence has collapsed", b: 0 }, { text: "Exports have fallen because of a world slowdown", b: 0 }, { text: "Firms cannot find workers with the right skills", b: 1 },
  { text: "Poor roads and power cuts raise firms' costs", b: 1 }, { text: "Low productivity compared with competitors", b: 1 }, { text: "Barriers stop new firms entering markets", b: 1 }, { text: "High unemployment from low spending", b: 0 },
], done: "Match the policy to the cause of weak growth." });
Lib.match($("#m1"), { prompt: "Match the policy to its main weakness.", pairs: [
  ["Cut interest rates", "May not work if confidence is low"],
  ["Raise government spending", "Bigger deficit and debt"],
  ["Cut income tax", "People may save the money"],
  ["Education and training", "Takes years to have an effect"],
  ["Lower the exchange rate", "Imports cost more: imported inflation"],
  ["Privatisation", "May create private monopolies"],
], done: "Every policy needs an evaluation point." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a cut in the interest rate could raise growth</b>.", items: [
  "The central bank cuts the interest rate",
  "Borrowing becomes cheaper and saving less attractive",
  "Consumption and investment rise",
  "Aggregate demand shifts right",
  "Real GDP rises: economic growth",
], done: "A monetary growth chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A government spends $20bn more and the multiplier is 2.5. What is the rise in real GDP ($bn)?", a: 50, sol: "2.5 × 20 = <b>$50bn</b>." },
  { q: "Real GDP is $500bn. Policy raises growth from 2% to 4%. How much extra output is there after one year ($bn)?", a: 10, hint: "Compare 4% and 2% of $500bn.", sol: "2% of 500 = $10bn extra." },
  { q: "A tax cut of $12bn is 75% spent in the first round. How much extra spending is there in the first round ($bn)?", a: 9, sol: "75% of 12 = <b>$9bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is most likely to raise growth quickly when there is spare capacity?", opts: ["Education reform", "Cutting interest rates", "Privatisation", "Deregulation"], a: 1, why: "Demand-side policy works faster than supply-side." },
  { q: "Which policy is most likely to lead to growth that can be sustained without inflation?", opts: ["Short-term tax cut", "Investment in education and infrastructure", "Raising the money supply", "Lower interest rates"], a: 1, why: "Supply-side policy raises capacity." },
  { q: "A disadvantage of cutting interest rates to promote growth is:", opts: ["It raises savings income", "It may raise inflation and imports", "It always reduces output", "It reduces investment"], a: 1, why: "Higher demand may overheat the economy." },
  { q: "Attracting multinational firms could promote growth because they:", opts: ["Bring capital, jobs and technology", "Reduce competition", "Raise imports only", "Cut AD"], a: 0, why: "More resources of better quality." },
  { q: "A drawback of free trade agreements may be:", opts: ["Larger markets", "Some firms and workers lose out", "Lower prices", "More choice"], a: 1, why: "Competition hurts less efficient firms." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Fiscal policy", "Government spending and taxation used to influence AD."],
  ["Monetary policy", "Interest rates, money supply and the exchange rate used to influence AD and inflation."],
  ["Supply-side policy", "Measures to raise productive capacity and shift AS to the right."],
  ["Foreign direct investment", "Investment in a country by foreign firms, such as multinationals."],
  ["Free trade", "Trade between countries without barriers such as tariffs."],
  ["Multiplier effect", "The final impact on AD is greater than the initial change."],
  ["Spare capacity", "Unused resources, when output is below potential."],
  ["Sustainable growth", "Growth that can continue without damaging the environment or future prospects."],
] });
labP();
