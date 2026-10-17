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

const SDX = (q) => 70 + q * 6.4, SDY = (p) => 270 - p * 2.4;
const sdEq = (d, s) => { const q = 50 + 0.5 * (d + s); return { q, p: 10 + 0.8 * (q - s) }; };
const sdSeg = (k, sh) => {
  const f = (q) => (k === "D" ? 90 - 0.8 * (q - sh) : 10 + 0.8 * (q - sh)), inv = (p) => (k === "D" ? sh + (90 - p) / 0.8 : sh + (p - 10) / 0.8);
  const qa = inv(k === "D" ? 95 : 12), qb = inv(k === "D" ? 12 : 95), lo = Math.max(0, Math.min(qa, qb)), hi = Math.min(100, Math.max(qa, qb));
  return [lo, f(lo), hi, f(hi)];
};
const sdCurve = (k, sh, c, v, name) => { const [a, b, e, f] = sdSeg(k, sh); return SV.line(SDX(a), SDY(b), SDX(e), SDY(f), c, { "stroke-width": 3, ...op(v) }) + tag(SDX(e) + 6, SDY(f) + (k === "D" ? 14 : -4), name, c, v); };
const sdGuide = (e, pn, qn, v) => SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash", op(v)) + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash", op(v)) + SV.text(62, SDY(e.p) + 4, pn, "sm", { "text-anchor": "end", ...op(v) }) + SV.text(SDX(e.q), 286, qn, "sm", { "text-anchor": "middle", ...op(v) });
function sdPlot(st, lab = {}) {
  const { d = 0, s = 0, g = 1, n = 1 } = st, mv = Math.abs(d) > 0.05 || Math.abs(s) > 0.05, e0 = sdEq(0, 0), e1 = sdEq(d, s);
  let o = axes(70, 270, 720, 25, lab.x || "Quantity", lab.y || "Price");
  o += sdCurve("D", 0, "c2", Math.abs(d) > 0.05 ? 0.4 : 1, lab.D1 || "D1") + sdCurve("S", 0, "c1", Math.abs(s) > 0.05 ? 0.4 : 1, lab.S1 || "S1");
  if (Math.abs(d) > 0.05) o += sdCurve("D", d, "c2", n, lab.D2 || "D2");
  if (Math.abs(s) > 0.05) o += sdCurve("S", s, "c1", n, lab.S2 || "S2");
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, lab.P1 || "P1", lab.Q1 || "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, lab.P2 || "P2", lab.Q2 || "Q2", g * n);
  return o;
}

const adLab = { x: "Real output (Y)", y: "Price level", D1: "AD1", D2: "AD2", S1: "SRAS1", S2: "SRAS2", P1: "P1", Q1: "Y1", P2: "P2", Q2: "Y2" };
function adasPlot(st, o = {}) {
  const l = st.l || 0, ln = o.lras !== false;
  let s = sdPlot({ d: st.a || 0, s: st.s || 0, g: st.g === undefined ? 1 : st.g, n: st.n === undefined ? 1 : st.n }, adLab);
  if (ln) s += SV.line(SDX(75 + l), SDY(0), SDX(75 + l), SDY(100), "c4", { "stroke-width": 3, "stroke-dasharray": "7 4" }) + tag(SDX(75 + l) + 6, SDY(98), "LRAS", "c4");
  return s;
}

function gcDraw(s) { return adasPlot({ a: s.a, s: s.s, l: s.l, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifting right and LRAS and SRAS shifting right">${gcDraw({ a: 20, s: 15, l: 15, n: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 300, label: "Demand-led and supply-led growth", base: { a: 0, s: 0, l: 0, n: 0 }, draw: gcDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is at output 50, below potential output of 75: there is spare capacity.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Demand-led growth.</b> Lower interest rates shift AD to the right. Real output rises to about 60 and prices rise a little. Growth uses up spare capacity.", s: { a: 20, s: 0, l: 0, n: 1 } },
  { cap: "<b>Supply-led growth.</b> Investment and better education shift SRAS and LRAS to the right. Potential output rises to 90, so the economy can keep growing without inflation.", s: { a: 20, s: 15, l: 15, n: 1 } },
] });

function vcDraw(s) {
  const bx = (x, y, t, k, v) => SV.rect(x, y, 170, 52, k, { rx: 8, ...op(0.55 * v) }) + SV.text(x + 85, y + 31, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
  const ar = (x1, y1, x2, y2, d, v) => SV.line(x1, y1, x2, y2, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y2, d, "dot4");
  let o = bx(60, 40, "Economic growth", "f3", s.a) + ar(232, 66, 330, 66, "r", s.b) + bx(335, 40, "Higher incomes and tax revenue", "f1", s.b) + ar(505, 66, 560, 66, "r", s.c) + bx(565, 40, "Spending on education, health, roads", "f2", s.c);
  o += ar(650, 94, 650, 150, "d", s.d) + bx(565, 155, "Higher productive capacity", "f1", s.d) + ar(560, 181, 235, 181, "l", s.e) + bx(60, 155, "LRAS shifts right: more growth", "f3", s.e);
  if (s.f > 0) o += SV.text(380, 255, "Costs to weigh: inflation, imports, pollution, inequality", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)", ...op(s.f) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 280" role="img" aria-label="A virtuous circle from growth to higher incomes and tax revenue, public spending, capacity and more growth">${vcDraw({ a: 1, b: 1, c: 1, d: 1, e: 1, f: 1 })}</svg>`;
Lib.stepper($("#stV"), { w: 760, h: 280, label: "The virtuous circle of economic growth", base: { a: 0, b: 0, c: 0, d: 0, e: 0, f: 0 }, draw: vcDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>Economic growth</b> raises real output.", s: { a: 1 } },
  { cap: "<b>Higher incomes and tax revenue.</b> People earn more, and the government collects more tax without raising rates.", s: { a: 1, b: 1 } },
  { cap: "<b>More public spending</b> on education, health care and infrastructure becomes affordable.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Productive capacity rises:</b> a healthier, more skilled workforce and better infrastructure.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>LRAS shifts right,</b> making further growth possible: a virtuous circle.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
  { cap: "<b>But there are costs to weigh:</b> inflation if demand outruns capacity, a worse current account, pollution and inequality. Growth is not always positive.", s: { a: 1, b: 1, c: 1, d: 1, e: 1, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labG() {
  if (!["lb", "cp", "tf"].every((i) => $("#" + i))) return;
  const l = +$("#lb").value, c = +$("#cp").value, t = +$("#tf").value, a = 0.6 * l, b = 0.4 * c, tot = a + b + t;
  $("#r1").textContent = Lib.fmtN(a, 1) + " pts"; $("#r2").textContent = Lib.fmtN(b, 1) + " pts"; $("#r3").textContent = Lib.fmtN(tot, 1) + "%";
  $("#rv").textContent = `Labour growth of ${l}% (weight 0.6) adds ${Lib.fmtN(a, 1)} points, capital growth of ${c}% (weight 0.4) adds ${Lib.fmtN(b, 1)}, and productivity or technology adds ${t}. Potential output grows ${Lib.fmtN(tot, 1)}% a year. ${t >= a + b ? "Most growth comes from productivity, which is the most sustainable source." : "Most growth comes from adding more labour and capital, which can be limited."}`;
  const Y = (v) => 250 - v * 28; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30) + SV.text(46, 26, "Growth (% points)", "sm"), y = 250;
  [["Labour", a, "f1"], ["Capital", b, "f2"], ["Technology", t, "f3"]].forEach(([n, v, k]) => { const h = v * 28; o += SV.rect(130, y - h, 140, h, k, op(0.65)) + (h > 14 ? SV.text(200, y - h / 2 + 5, n + " " + Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" }) : ""); y -= h; });
  o += SV.text(200, 270, "Total " + Lib.fmtN(tot, 1) + "%", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "lb", label: "Growth in the labour force, % ", min: 0, max: 4, step: 0.5, value: 1.5, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "cp", label: "Growth in the capital stock, % ", min: 0, max: 8, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g3"), { id: "tf", label: "Productivity and technology, % points ", min: 0, max: 4, step: 0.5, value: 1, fmt: (v) => v + "%", onInput: labG });
labG();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!["gg", "sp", "sh"].every((i) => $("#" + i))) return;
  const g = +$("#gg").value, sp = +$("#sp").value, sh = +$("#sh").value / 100, dem = g * (1 - sh), infl = Math.max(0, dem - sp / 2), ca = -0.45 * g;
  $("#t1").textContent = infl < 0.3 ? "Low" : infl < 2 ? "Moderate" : "High"; $("#t2").textContent = Lib.fmtN(ca, 1) + "% of GDP"; $("#t3").textContent = infl < 0.3 && sh > 0.4 ? "Mostly positive" : infl < 2 ? "Mixed" : "Risky";
  $("#tv").textContent = `${g}% growth, ${Lib.fmtN(sh * 100, 0)}% of it from higher capacity, so ${Lib.fmtN(dem, 1)} points are demand-led. With spare capacity of ${sp}% the economy can absorb about ${Lib.fmtN(sp / 2, 1)} points without much inflation, leaving inflation pressure of ${Lib.fmtN(infl, 1)}. Higher incomes also raise imports, which could worsen the current account by about ${Lib.fmtN(-ca, 1)}% of GDP. ${infl > 2 ? "The growth is likely to be inflationary and may not be sustainable." : "The growth looks reasonably sustainable."}`;
  let o = SV.line(40, 180, 400, 180); [["Total growth", g, "f1"], ["Demand-led", dem, "f3"], ["Absorbable", sp / 2, "f2"]].forEach(([n, v, k], i) => (o += SV.rect(70 + i * 110, 180 - v * 18, 80, v * 18, k, op(0.65)) + SV.text(110 + i * 110, 200, n, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, 174 - v * 18, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Real GDP growth, % ", min: 1, max: 9, step: 1, value: 5, fmt: (v) => v + "%", onInput: labB });
Lib.slider($("#g5"), { id: "sp", label: "Spare capacity in the economy, % of GDP ", min: 0, max: 12, step: 1, value: 4, fmt: (v) => v + "%", onInput: labB });
Lib.slider($("#g6"), { id: "sh", label: "Share of growth from higher productive capacity, % ", min: 0, max: 100, step: 10, value: 30, fmt: (v) => v + "%", onInput: labB });
labB();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Benefit or cost of growth?", buckets: [{"label": "Possible benefit"}, {"label": "Possible cost"}], items: [{"text": "Higher living standards", "b": 0}, {"text": "Inflation when near full capacity", "b": 1}, {"text": "Lower unemployment", "b": 0}, {"text": "Pollution and resource depletion", "b": 1}, {"text": "Higher tax revenue", "b": 0}, {"text": "A bigger current account deficit", "b": 1}, {"text": "More resources for health and education", "b": 0}, {"text": "Widening inequality", "b": 1}], done: "Growth can raise incomes and jobs but may bring inflation, imports, environmental damage and inequality." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Demand-led growth", "A rise in AD that uses up spare capacity"], ["Supply-led growth", "A rise in productive capacity: LRAS shifts right"], ["Net investment", "Spending on capital that adds to the capital stock"], ["Productivity", "Output per worker or per unit of input"], ["Informal economy", "Unrecorded output, which makes growth hard to measure"], ["Sustainable growth", "Growth that can continue without harming future output"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the virtuous circle of growth in order.", items: ["Economic growth raises output", "Incomes and tax revenue rise", "The government spends more on education and infrastructure", "Productive capacity rises", "LRAS shifts right and growth continues"], done: "Growth, revenue, investment in capacity, more growth." });
Lib.calc($("#c1"), { qs: [
  {"q": "Labour grows 2% (weight 0.6), capital grows 5% (weight 0.4) and technology adds 1 point. What is growth in potential output (%)?", "a": 4.2, "unit": "%", "tol": 0.1, "hint": "1.2 + 2.0 + 1.", "sol": "<b>4.2%</b>."},
  {"q": "What share of that growth comes from technology (%)?", "a": 23.8, "unit": "%", "tol": 0.3, "hint": "1 ÷ 4.2.", "sol": "<b>23.8%</b>."},
  {"q": "Real GDP grows 5% and imports have an income elasticity of 1.5 with imports at 30% of GDP. By roughly what % of GDP do imports rise?", "a": 2.25, "unit": "%", "tol": 0.1, "hint": "7.5% × 0.3.", "sol": "Imports rise 7.5%, which is <b>2.25%</b> of GDP."},
  {"q": "Real GDP is $400bn. After growth of 3.5% it is: ($bn)", "a": 414, "unit": "$bn", "tol": 0.5, "hint": "400 × 1.035.", "sol": "<b>$414bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a supply-side cause of growth?", opts: ["Investment in capital goods", "A cut in interest rates", "A rise in government spending", "A depreciation"], a: 0, why: "It raises capacity." },
  { q: "Demand-led growth is most likely to cause inflation when:", opts: ["The economy is near full capacity", "There is much spare capacity", "AD is falling", "Unemployment is high"], a: 0, why: "Output cannot rise." },
  { q: "A possible consequence of growth is:", opts: ["A rise in imports", "A fall in tax revenue", "A fall in living standards for all", "No change in demand"], a: 0, why: "Higher incomes raise import spending." },
  { q: "Growth is more sustainable when it comes from:", opts: ["Higher productivity", "Borrowing to spend", "Running down natural resources", "Rising prices"], a: 0, why: "Higher capacity." },
  { q: "Growth is measured by the change in:", opts: ["Real GDP", "Nominal GDP", "Prices", "Exports"], a: 0, why: "Real, not nominal." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Demand-side", "AD shifts right."],
  ["Supply-side", "LRAS shifts right."],
  ["Benefits", "Living standards, jobs, tax revenue."],
  ["Costs", "Inflation, imports, environment, inequality."],
  ["Sustainable", "Productivity-led."],
  ["Measure", "Informal economy limits it."],
  ["Actual growth", "Uses spare capacity."],
  ["Judge", "Source, capacity, distribution."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which change affecting an economy's labour force will cause an increase in economic growth in the short run? (May/June 2024 · 12 · Q18, reworded)", opts: ["an increase in students entering university", "an increase in the birth rate", "an increase in the immigration of skilled labour", "an increase in the school leaving age"], a: 2, why: "Skilled immigrants can start work at once, raising output in the short run. The other changes take years." },
  { q: "Economic growth leads to increased levels of income and consumption per capita for the adult population. Which circumstances are needed for this to happen in an economy? (May/June 2023 · 12 · Q30, reworded)", opts: ["a change in technology that maintains the same level of output", "an increase in economic efficiency through higher productivity of factor inputs", "a policy of progressive taxation to reduce inequalities", "a rise in the size of the working population due to immigration"], a: 1, why: "Higher productivity raises output per head. A larger population need not raise income per head." },
  { q: "Which government action is least likely to prevent a fall in economic growth? (May/June 2023 · 13 · Q24, reworded)", opts: ["additional controls on commercial banks' lending", "relaxation of rules for immigration of adult population", "removal of trade barriers on import of raw materials", "training and education of workforce"], a: 0, why: "Tighter controls on lending reduce credit and spending, so they are least likely to support growth." },
  { q: "What is true about a government's macroeconomic objectives? (May/June 2024 · 12 · Q20, reworded)", opts: ["Economic growth ensures a more even distribution of income", "Increasing output ensures that more workers are employed", "Choosing between macroeconomic objectives requires a normative decision", "A stable rate of inflation means zero inflation is required"], a: 2, why: "Choosing between objectives (such as growth against inflation) involves value judgements." },
] });
