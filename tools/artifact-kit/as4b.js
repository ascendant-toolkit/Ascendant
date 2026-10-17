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

function dpDraw(s) { return adasPlot({ a: s.a, s: s.s, l: 0, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A rightward shift of AD raises the price level and output">${dpDraw({ a: 20, s: 0, n: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A leftward shift of SRAS raises the price level and lowers output">${dpDraw({ a: 0, s: -20, n: 1 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 300, label: "Demand-pull inflation", base: { a: 0, s: 0, n: 0 }, draw: dpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD1 and SRAS1 meet at a price level of 50 and real output of 50.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>A rise in AD.</b> Lower interest rates raise consumption and investment, shifting AD to the right. The price level rises to about 58 and output rises: <b>demand-pull inflation</b>.", s: { a: 20, s: 0, n: 1 } },
  { cap: "<b>A larger rise in AD</b> pushes the price level up further, and nearer to potential output (the LRAS) the effect is increasingly on prices rather than output.", s: { a: 35, s: 0, n: 1 } },
] });
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Cost-push inflation and a wage-price spiral", base: { a: 0, s: 0, n: 0 }, draw: dpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>A rise in costs</b> (oil prices, wages above productivity) shifts SRAS left. The price level rises to about 58 and output falls: <b>cost-push inflation</b> and stagflation.", s: { a: 0, s: -20, n: 1 } },
  { cap: "<b>The spiral.</b> Workers demand higher wages to keep up with prices. Higher wages raise costs (SRAS shifts left again) and also raise spending (AD shifts right): prices rise further and inflation becomes embedded.", s: { a: 15, s: -35, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
const CAU = [["Lower interest rates", 20, 0, "Demand-pull"], ["Tax cuts raise incomes", 15, 0, "Demand-pull"], ["Export boom", 20, 0, "Demand-pull"], ["Higher government spending", 20, 0, "Demand-pull"], ["Oil price rise", 0, -20, "Cost-push"], ["Wages rise faster than productivity", 0, -15, "Cost-push"], ["Higher indirect taxes", 0, -15, "Cost-push"], ["Depreciation raises import costs", 8, -12, "Both (mainly cost-push)"]];
function showC(i) {
  const [n, a, s, t] = CAU[i], e = sdEq(a, s), e0 = sdEq(0, 0); $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#r1").textContent = t; $("#r2").textContent = (e.p > e0.p ? "Up to " : "Down to ") + Lib.fmtN(e.p, 1); $("#r3").textContent = (e.q > e0.q ? "Up to " : "Down to ") + Lib.fmtN(e.q, 1);
  $("#rv").textContent = `${n}: ${a > 0 && s < 0 ? "AD shifts right (higher export demand) and SRAS shifts left (dearer imported inputs)" : a > 0 ? "AD shifts right" : "SRAS shifts left"}. The price level rises from 50 to ${Lib.fmtN(e.p, 1)} and real output ${e.q > e0.q ? "rises" : "falls"} from 50 to ${Lib.fmtN(e.q, 1)}: ${t.toLowerCase()} inflation.`;
  $("#labA").innerHTML = adasPlot({ a, s, g: 1, n: 1 }, { lras: false });
}
$("#evB").innerHTML = CAU.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showC(+b.dataset.i)));
showC(0);

/* ---------- Lab 2 ---------- */
function labT() {
  if (!["ad", "sr"].every((i) => $("#" + i))) return;
  const a = +$("#ad").value, s = +$("#sr").value, e = sdEq(a, s), pc = (e.p - 50) / 50 * 100, qc = (e.q - 50) / 50 * 100, dp = 0.4 * a, cp = -0.4 * s;
  $("#t1").textContent = (pc >= 0 ? "+" : "") + Lib.fmtN(pc, 1) + "%"; $("#t2").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#t3").textContent = pc <= 0.5 ? "Little inflation" : dp > cp * 1.3 ? "Demand-pull" : cp > dp * 1.3 ? "Cost-push" : "Both";
  $("#tv").textContent = `The AD shift adds about ${Lib.fmtN(dp / 50 * 100, 1)} points to the price level and the SRAS shift ${Lib.fmtN(cp / 50 * 100, 1)} points. Price level ${Lib.fmtN(pc, 1)}%, real output ${Lib.fmtN(qc, 1)}%. ${qc > 1 ? "Output rises with prices: more like demand-pull." : qc < -1 ? "Output falls as prices rise: more like cost-push (stagflation)." : "Output is roughly unchanged."}`;
  $("#labB").innerHTML = adasPlot({ a, s, g: 1, n: 1 }, { lras: false });
}
Lib.slider($("#g1"), { id: "ad", label: "AD shift (positive = right) ", min: -20, max: 40, step: 5, value: 15, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "sr", label: "SRAS shift (negative = left, costs rising) ", min: -30, max: 20, step: 5, value: -15, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Demand-pull or cost-push?", buckets: [{"label": "Demand-pull"}, {"label": "Cost-push"}], items: [{"text": "A cut in interest rates raises spending", "b": 0}, {"text": "A rise in oil prices", "b": 1}, {"text": "An export boom", "b": 0}, {"text": "Wages rise faster than productivity", "b": 1}, {"text": "A cut in income tax", "b": 0}, {"text": "A rise in indirect taxes on firms", "b": 1}, {"text": "Government spending rises near full capacity", "b": 0}, {"text": "A depreciation raises the price of imported raw materials", "b": 1}], done: "Demand-pull: AD shifts right. Cost-push: SRAS shifts left." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Demand-pull inflation", "AD rises faster than AS"], ["Cost-push inflation", "Higher costs shift SRAS left"], ["Stagflation", "Rising prices with falling output"], ["Wage-price spiral", "Higher prices lead to higher wages, then higher prices"], ["Full capacity", "Output cannot rise, so extra demand raises prices"], ["Depreciation", "Can raise import costs and export demand"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the wage-price spiral in order.", items: ["Prices rise", "Workers demand higher wages", "Firms' costs rise", "Firms raise prices again", "Inflation becomes embedded"], done: "Prices lead to wages, which lead to prices again." });
Lib.calc($("#c1"), { qs: [
  {"q": "The price level index rises from 100 to 108 after AD shifts right and output rises 2%. What is the inflation rate (%)?", "a": 8, "unit": "%", "tol": 0.1, "hint": "8 ÷ 100.", "sol": "<b>8%</b>."},
  {"q": "After a cost shock the price level rises from 100 to 106 and output falls from 500 to 485. What is the % fall in output?", "a": 3, "unit": "%", "tol": 0.1, "hint": "15 ÷ 500.", "sol": "<b>3%</b>."},
  {"q": "In the second case, are output and prices moving in the same direction (yes = 1, no = 0)?", "a": 0, "unit": "", "tol": 0.1, "hint": "Prices up, output down.", "sol": "<b>No (0)</b>: stagflation, a sign of cost-push."},
  {"q": "A firm's wage bill is 60% of costs and wages rise 5% with no productivity gain. By how much do its costs rise (%)?", "a": 3, "unit": "%", "tol": 0.1, "hint": "0.6 × 5.", "sol": "<b>3%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Demand-pull inflation is shown by:", opts: ["A rightward shift of AD", "A leftward shift of SRAS", "A rightward shift of LRAS", "A fall in AD"], a: 0, why: "AD rises." },
  { q: "Cost-push inflation is shown by:", opts: ["A leftward shift of SRAS", "A rightward shift of AD", "A rightward shift of SRAS", "A fall in costs"], a: 0, why: "Higher costs." },
  { q: "Stagflation means:", opts: ["Rising prices and falling output", "Falling prices and rising output", "Rising prices and rising output", "Falling prices and falling output"], a: 0, why: "Cost-push." },
  { q: "Which could cause cost-push inflation?", opts: ["Higher oil prices", "A cut in interest rates", "A rise in exports", "A tax cut"], a: 0, why: "Raises costs." },
  { q: "Extra AD is most likely to cause only inflation when:", opts: ["The economy is at full capacity", "There is much spare capacity", "Unemployment is high", "SRAS is flat"], a: 0, why: "Output cannot rise." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Demand-pull", "AD right."],
  ["Cost-push", "SRAS left."],
  ["Stagflation", "Prices up, output down."],
  ["Spiral", "Wages and prices chase."],
  ["Capacity", "Near full: inflationary."],
  ["Diagram", "AD/AS, general price level."],
  ["Cause", "Name and explain."],
  ["Compare", "Which is worse?"],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is least likely to cause a simultaneous increase in demand-pull and cost-push inflation? (Feb/March 2024 · 12 · Q16, reworded)", opts: ["depreciation of currency", "increased import tariffs", "decreased spending on infrastructure", "increased wages"], a: 2, why: "Less spending on infrastructure reduces AD, so is least likely to cause either. Depreciation, tariffs and wage rises can raise both demand and costs." },
  { q: "In an economy, wages and prices are both rising but wages are rising faster. Which features are likely to exist in this economy? (cost-push inflation, rise in real incomes) (Feb/March 2023 · 12 · Q20, reworded)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 3, why: "Rising wages raise costs (cost-push), and wages rising faster than prices means real incomes are rising." },
  { q: "What would be likely to increase inflation in an economy? (May/June 2021 · 11 · Q27, reworded)", opts: ["an increase in consumer saving", "an increase in interest rates", "an increase in labour productivity", "an increase in taxes on imports"], a: 3, why: "Taxes on imports raise the cost of imported inputs, shifting SRAS left. Saving, higher rates and productivity reduce inflation." },
  { q: "What is correct about the causes of inflation? (May/June 2021 · 12 · Q22, reworded)", opts: ["Cost-push inflation can be caused by a rising exchange rate", "Cost-push inflation can be caused by lower indirect taxes", "Demand-pull inflation can be caused by a rising exchange rate", "Demand-pull inflation can be caused by lower direct taxes"], a: 3, why: "Lower direct taxes raise disposable income and consumption, so AD rises." },
  { q: "An appreciation of the South African rand in the foreign exchange markets is most likely to assist the South African government achieve which policy objective? (Feb/March 2020 · 12 · Q20, reworded)", opts: ["a redistribution of income", "a reduction in the rate of inflation", "a reduction in the volume of imports", "an increase in the level of employment"], a: 1, why: "A stronger rand makes imports cheaper, reducing costs and inflation." },
] });
