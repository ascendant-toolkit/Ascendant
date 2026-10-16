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

const RD = ["The government cuts spending and raises taxes (or raises interest rates)", "Households have less income to spend", "Spending on imports falls", "The current account deficit narrows", "But AD, growth and jobs also fall", "A conflict between BoP stability and growth and employment"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Expenditure-reducing policy", base: { n: 0 }, draw: mkChain(RD, "--warn"), steps: chainSteps(["The government <b>cuts spending and raises taxes</b> (or the central bank raises interest rates).", "Households have <b>less income</b> to spend.", "<b>Spending on imports falls</b>.", "The <b>current account deficit narrows</b>.", "But <b>AD, growth and jobs also fall</b>.", "A <b>conflict of aims</b>: balance of payments stability against growth and employment."]) });
const SW = ["The government lowers the exchange rate or puts tariffs on imports", "Imports become dearer; exports become cheaper abroad", "Demand switches from imports to home-made goods; export demand rises", "Import spending falls and export earnings rise", "The deficit narrows", "But imported inflation, retaliation and elasticity limit the effect"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "Expenditure-switching policy", base: { n: 0 }, draw: mkChain(SW, "--accent"), steps: chainSteps(["The government <b>lowers the exchange rate</b> or puts <b>tariffs on imports</b>.", "Imports become <b>dearer</b>; exports become <b>cheaper</b> abroad.", "Demand <b>switches</b> from imports to home-made goods; export demand rises.", "<b>Import spending falls</b> and export earnings rise.", "The <b>deficit narrows</b>.", "<b>Evaluate:</b> imported inflation, retaliation and elasticity limit the effect."]) });
const SS = ["The government invests in education, infrastructure and technology", "Productivity rises and costs fall; quality improves", "Exports become more competitive; imports less necessary", "Export revenue rises and import spending falls over time", "The deficit narrows without cutting growth", "Evaluation: slow, costly and uncertain"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Supply-side policy", base: { n: 0 }, draw: mkChain(SS, "--good"), steps: chainSteps(["The government invests in <b>education, infrastructure and technology</b>.", "<b>Productivity rises</b> and costs fall; quality improves.", "Exports become <b>more competitive</b>; imports less necessary.", "<b>Export revenue rises</b> and import spending falls over time.", "The deficit narrows <b>without cutting growth</b>.", "<b>Evaluate:</b> slow, costly and uncertain."]) });

/* Lab 1: mix */
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc")) return;
  const c = +$("#ma").value, d = +$("#mb").value, s = +$("#mc").value, def0 = 20, def = def0 - 0.8 * c - 0.5 * d * 1 - 0.4 * s, gdp = -0.5 * c + 0.2 * d + 0.1 * s, inf = 0.3 * d - 0.2 * c - 0.05 * s;
  $("#ma1").textContent = "$" + money(Math.max(def, -10), 1) + "bn"; $("#ma2").textContent = (gdp >= 0 ? "+" : "−") + money(Math.abs(gdp), 1) + "%"; $("#ma3").textContent = (inf >= 0 ? "+" : "−") + money(Math.abs(inf), 1) + " pts";
  $("#mav").textContent = `Starting from a $20bn deficit: cutting demand by ${c} reduces imports but also GDP by ${money(Math.abs(0.5 * c), 1)}%. A ${d}% fall in the exchange rate narrows the deficit but adds ${money(0.3 * d, 1)} points to inflation. Supply-side effort of ${s} helps most slowly (and is shown at full effect here). The best mix depends on which aims matter most: use more than one policy and watch the trade-offs.`;
  const base = 290, k = 8; let o = SV.line(60, base, 700, base);
  [["Deficit ($bn)", Math.max(def, 0), "--bad"], ["Change in GDP (%)", gdp, "--accent"], ["Change in inflation (pts)", inf, "--warn"]].forEach(([n, v, cl], i) => { const x = 110 + i * 190, h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(x, y, 120, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 60, v >= 0 ? y - 8 : y + h + 16, (v >= 0 ? "" : "−") + money(Math.abs(v), 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 40, n, "sm", { "text-anchor": "middle" }); });
  $("#labM").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ma", label: "Expenditure-reducing: cut in demand", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Expenditure-switching: fall in the exchange rate (%)", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v + "%", onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Supply-side: investment in competitiveness", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labM });
const PP = [
  { n: "Cut government spending / raise taxes", t: "Expenditure-reducing", w: "Lower incomes cut spending on imports.", p: "Lower growth, higher unemployment." },
  { n: "Raise interest rates", t: "Expenditure-reducing", w: "Less borrowing and spending; hot money may raise the currency.", p: "Slows growth; a higher rate may hurt exports." },
  { n: "Lower the exchange rate", t: "Expenditure-switching", w: "Exports cheaper, imports dearer.", p: "Imported inflation; depends on elasticity." },
  { n: "Tariffs and quotas", t: "Expenditure-switching", w: "Imports dearer or limited.", p: "Retaliation; higher prices." },
  { n: "Export subsidies", t: "Expenditure-switching", w: "Lower costs for exporters.", p: "Cost to taxpayers; trade disputes." },
  { n: "Education, investment and infrastructure", t: "Supply-side", w: "Raises productivity and competitiveness.", p: "Slow, costly, uncertain." },
];
button_table("ppBtns", "ppOut", PP, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>How it works</th><th>Problems</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td><td>${p.p}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of policy</b> to reduce a current account deficit is each?", buckets: [{ label: "Expenditure-reducing" }, { label: "Expenditure-switching" }, { label: "Supply-side" }], items: [
  { text: "Raise taxes and cut government spending", b: 0 }, { text: "Raise interest rates", b: 0 },
  { text: "Lower the exchange rate", b: 1 }, { text: "Impose import tariffs", b: 1 }, { text: "Subsidise exporters", b: 1 },
  { text: "Invest in education and infrastructure", b: 2 }, { text: "Encourage innovation and lower business costs", b: 2 },
], done: "Reduce demand, switch demand, or raise competitiveness." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>problem</b> with the policy to reduce a deficit, and which policy?", buckets: [{ label: "Slows growth and raises unemployment" }, { label: "Imported inflation or retaliation" }, { label: "Slow to work" }], items: [
  { text: "Cutting government spending", b: 0 }, { text: "Raising interest rates", b: 0 },
  { text: "Lowering the exchange rate", b: 1 }, { text: "Raising tariffs", b: 1 },
  { text: "Investing in education", b: 2 }, { text: "Building new infrastructure", b: 2 },
], done: "Every policy has a cost." });
Lib.match($("#m1"), { prompt: "Match the policy to its main effect on the current account.", pairs: [
  ["Contractionary fiscal policy", "Lower incomes reduce spending on imports"],
  ["Lower exchange rate", "Exports cheaper abroad, imports dearer"],
  ["Tariffs", "Imports dearer, so fewer imported"],
  ["Export subsidies", "Lower costs for exporters"],
  ["Education and training", "Raise productivity and competitiveness"],
  ["Expansionary policy (for a surplus)", "Raises spending on imports"],
], done: "Link each policy to the mechanism." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a fall in the exchange rate could reduce a deficit</b>.", items: [
  "The government allows or causes the exchange rate to fall",
  "Exports become cheaper in foreign currency; imports become dearer",
  "Demand for exports rises and demand for imports falls",
  "Export revenue rises and import spending falls",
  "The current account deficit narrows",
], done: "An expenditure-switching chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A deficit is $20bn. A policy cuts import spending by $6bn and raises exports by $4bn. What is the new deficit ($bn)?", a: 10, sol: "20 − 6 − 4 = <b>$10bn</b>." },
  { q: "Incomes fall by $10bn and households spend 30% of any change on imports. By how much do imports fall ($bn)?", a: 3, sol: "30% × 10 = <b>$3bn</b>." },
  { q: "A tariff of 10% raises the price of imports and imports fall from $100bn to $90bn. By what percentage did imports fall?", a: 10, sol: "10 ÷ 100 × 100 = <b>10%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an expenditure-reducing policy?", opts: ["A lower exchange rate", "Raising government spending on infrastructure", "Raising taxes and cutting government spending", "Tariffs"], a: 2, why: "Reduces demand and imports." },
  { q: "Which is a supply-side policy to improve the current account?", opts: ["A tariff", "Education and training that raise productivity", "A quota", "Raising interest rates"], a: 1, why: "Raises competitiveness." },
  { q: "A disadvantage of cutting government spending to reduce a deficit is:", opts: ["Higher growth", "Higher unemployment and lower growth", "Cheaper imports", "More exports"], a: 1, why: "AD falls." },
  { q: "A lower exchange rate may fail to reduce a deficit if demand for imports is:", opts: ["Elastic", "Inelastic", "Unit elastic", "Rising"], a: 1, why: "Quantities barely change." },
  { q: "To reduce a large surplus a government could:", opts: ["Raise tariffs", "Cut taxes to raise spending on imports", "Cut government spending", "Lower the exchange rate"], a: 1, why: "Expansionary policy." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Expenditure-reducing policy", "Policy that cuts demand, including spending on imports, such as higher taxes or interest rates."],
  ["Expenditure-switching policy", "Policy that switches spending from imports to home-produced goods, such as a lower exchange rate or tariffs."],
  ["Supply-side policy", "Policy that raises productive capacity and competitiveness."],
  ["Devaluation", "A government lowering the value of a fixed currency."],
  ["Revaluation", "A government raising the value of a fixed currency."],
  ["Tariff", "A tax on imports."],
  ["Subsidy", "A payment by the government to lower producers' costs."],
  ["Retaliation", "Responding to a trade restriction with another."],
  ["Balance of payments stability", "Avoiding large persistent deficits or surpluses on the current account."],
] });
labM(); 
