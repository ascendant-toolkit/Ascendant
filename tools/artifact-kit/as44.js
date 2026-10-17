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

/* ---------- SRAS shift ---------- */
function cuDraw(s) { return adasPlot({ a: 0, s: s.s, g: 1, n: s.n, l: 0 }, { lras: false }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A rise in costs shifts SRAS to the left, raising the price level and reducing output">${cuDraw({ s: -20, n: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A rise in costs shifts SRAS to the left", base: { s: 0, n: 0 }, draw: cuDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD1 and SRAS1 meet at a price level of 50 and real output of 50.", s: { s: 0, n: 0 } },
  { cap: "<b>A rise in raw material and energy prices</b> raises costs at every output. SRAS shifts <b>left</b>. The price level rises and real output falls: <b>cost-push inflation</b>.", s: { s: -20, n: 1 } },
  { cap: "<b>A fall in costs</b> (or a stronger currency, or higher productivity) shifts SRAS <b>right</b>: lower prices and higher output.", s: { s: 20, n: 1 } },
] });

/* ---------- LRAS ---------- */
function lrDraw(s) {
  let o = axes(70, 270, 720, 25, "Real output (Y)", "Price level");
  const x1 = SDX(75), x2 = SDX(75 + s.l);
  if (s.t < 0.5) { o += SV.line(x1, SDY(0), x1, SDY(100), "c4", { "stroke-width": 3.5, "stroke-dasharray": "7 4" }) + tag(x1 + 6, SDY(98), "LRAS1: potential output", "c4"); if (s.l > 0.5) o += SV.line(x2, SDY(0), x2, SDY(100), "c4", { "stroke-width": 3.5 }) + tag(x2 + 6, SDY(88), "LRAS2", "c4", 1) + arrow(x1 + 4, SDY(60), x2 - 6, SDY(60), "r", "c4", 1); }
  else { const P = [[SDX(10), SDY(15)], [SDX(35), SDY(18)], [SDX(60), SDY(35)], [SDX(72), SDY(65)], [SDX(75), SDY(100)]]; o += SV.path("M" + P.map((p) => p.join(",")).join(" L"), "c4", { fill: "none", "stroke-width": 3.5 }) + tag(SDX(12), SDY(10), "Highly elastic: spare capacity", "c4") + tag(SDX(38), SDY(48), "Upward sloping", "c4") + tag(SDX(75) + 8, SDY(90), "Vertical: full capacity", "c4"); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="LRAS as a vertical line at potential output shifting right">${lrDraw({ t: 0, l: 15 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "LRAS: potential output and the three-section view", base: { t: 0, l: 0 }, draw: lrDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The vertical LRAS</b> sits at the economy's <b>potential output</b>: what it can produce when all resources are fully employed. In the long run, output does not depend on the price level.", s: { t: 0, l: 0 } },
  { cap: "<b>Shifting LRAS right.</b> Better education, more capital, new technology or a bigger labour force raise potential output. This is long-run <b>economic growth</b>.", s: { t: 0, l: 15 } },
  { cap: "<b>The three-section view.</b> With much spare capacity, output can rise without raising prices (flat). As capacity tightens, prices begin to rise (sloping). At full capacity, only prices rise (vertical).", s: { t: 1, l: 0 } },
] });

/* ---------- Lab 1 ---------- */
function labS() {
  if (!["wg", "rm", "pd"].every((i) => $("#" + i))) return;
  const w = +$("#wg").value, r = +$("#rm").value, p = +$("#pd").value, s = Math.max(-30, Math.min(30, 0.5 * w + 0.5 * r + 0.8 * p)), e = sdEq(0, s), e0 = sdEq(0, 0);
  $("#r1").textContent = Math.abs(s) < 0.5 ? "No shift" : s > 0 ? "Right" : "Left"; $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = Lib.fmtN(e.p, 1);
  $("#rv").textContent = Math.abs(s) < 0.5 ? "Costs are unchanged, so SRAS stays put (price level 50, output 50)." : `${s > 0 ? "Lower costs or higher productivity" : "Higher costs"} shift SRAS to the ${s > 0 ? "right" : "left"}: real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. ${s < 0 ? "This is cost-push inflation with lower output." : "Prices fall and output rises."}`;
  $("#labA").innerHTML = adasPlot({ a: 0, s, g: 1, n: 1 }, { lras: false });
}
Lib.slider($("#g1"), { id: "wg", label: "Fall in wage costs (negative = rise), % ", min: -20, max: 20, step: 5, value: -10, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "rm", label: "Fall in raw material costs (negative = rise), % ", min: -20, max: 20, step: 5, value: -10, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g3"), { id: "pd", label: "Rise in productivity, % ", min: -10, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["lb", "cp", "tc"].every((i) => $("#" + i))) return;
  const l = +$("#lb").value, c = +$("#cp").value, t = +$("#tc").value, sh = Math.min(20, 0.4 * l + 0.4 * c + 0.6 * t), pot = 75 + sh, e = sdEq(0, 0), gap = pot - e.q;
  $("#t1").textContent = Lib.fmtN(pot, 1); $("#t2").textContent = Lib.fmtN(e.q, 1); $("#t3").textContent = Lib.fmtN(gap, 1);
  $("#tv").textContent = sh <= 0.5 ? "No change in the quantity or quality of resources, so LRAS stays at 75 units of potential output. The economy produces 50 now, so it has spare capacity of 25." : `Better resources shift LRAS right by ${Lib.fmtN(sh, 1)} to ${Lib.fmtN(pot, 1)}: potential output has grown. Actual output is still ${Lib.fmtN(e.q, 1)}, so spare capacity is ${Lib.fmtN(gap, 1)}. To use the extra capacity AD would also need to rise.`;
  $("#labB").innerHTML = adasPlot({ a: 0, s: 0, l: sh, g: 1, n: 1 });
}
Lib.slider($("#g4"), { id: "lb", label: "Growth in the labour force or skills, % ", min: 0, max: 20, step: 5, value: 10, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g5"), { id: "cp", label: "Net investment in capital, % ", min: 0, max: 20, step: 5, value: 10, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g6"), { id: "tc", label: "Technological progress, % ", min: 0, max: 20, step: 5, value: 5, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which curve shifts?", buckets: [{"label": "SRAS"}, {"label": "LRAS"}], items: [{"text": "A rise in oil prices", "b": 0}, {"text": "A rise in the size of the labour force", "b": 1}, {"text": "A fall in wage costs", "b": 0}, {"text": "Net investment in new factories", "b": 1}, {"text": "A cut in business taxes", "b": 0}, {"text": "Better education and training", "b": 1}, {"text": "A stronger exchange rate lowers import costs", "b": 0}, {"text": "A new technology raises potential output", "b": 1}], done: "Costs and short-term factors shift SRAS. The quantity and quality of resources shift LRAS." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Aggregate supply", "Total output firms will supply at each price level"], ["SRAS", "Slopes up because wages and other costs are slow to adjust"], ["LRAS", "Potential output when resources are fully employed"], ["Cost-push inflation", "A rise in costs shifts SRAS left, raising prices"], ["Productivity", "Output per worker or per unit of input"], ["Potential output", "What the economy can produce at full employment"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of higher raw material costs in order.", items: ["Raw material prices rise", "Firms' costs rise at every level of output", "SRAS shifts to the left", "The price level rises", "Real output falls"], done: "Higher costs shift SRAS left: prices up, output down." });
Lib.calc($("#c1"), { qs: [
  {"q": "Equilibrium before: price level 50, output 50. After SRAS shifts left, price level 60 and output 40. What is the % rise in the price level?", "a": 20, "unit": "%", "tol": 0.2, "hint": "10 ÷ 50.", "sol": "<b>20%</b>."},
  {"q": "What is the % fall in output?", "a": 20, "unit": "%", "tol": 0.2, "hint": "10 ÷ 50.", "sol": "<b>20%</b>."},
  {"q": "Potential output is 800 and actual output is 740. What is the output gap (units)?", "a": 60, "unit": "", "tol": 0.5, "hint": "800 − 740.", "sol": "<b>60</b> units of spare capacity."},
  {"q": "Potential output rises from 800 to 840. What is the % growth in potential output?", "a": 5, "unit": "%", "tol": 0.1, "hint": "40 ÷ 800.", "sol": "<b>5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in wage costs will:", opts: ["Shift SRAS to the left", "Shift SRAS to the right", "Shift AD to the right", "Shift LRAS right"], a: 0, why: "Costs rise." },
  { q: "The LRAS curve shows:", opts: ["Potential output", "Planned spending", "Short-run output", "Unemployment"], a: 0, why: "Full employment output." },
  { q: "An increase in the labour force shifts:", opts: ["LRAS to the right", "SRAS to the left", "AD to the left", "Nothing"], a: 0, why: "More resources." },
  { q: "Cost-push inflation is caused by:", opts: ["A leftward shift of SRAS", "A rightward shift of AD", "A fall in costs", "Rising productivity"], a: 0, why: "Higher costs." },
  { q: "The three-section LRAS is flat when:", opts: ["There is much spare capacity", "The economy is at full capacity", "Inflation is high", "Prices are falling"], a: 0, why: "Output can rise without price pressure." },
] });
Lib.cards($("#fc1"), { cards: [
  ["AS", "Output supplied at each price level."],
  ["SRAS", "Upward sloping; shifts with costs."],
  ["LRAS", "Potential output; shifts with capacity."],
  ["Costs rise", "SRAS left."],
  ["Productivity rises", "AS right."],
  ["Three sections", "Flat, sloping, vertical."],
  ["Cost-push", "SRAS left raises prices."],
  ["Growth", "LRAS shifts right."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What will cause a movement along an aggregate supply curve? (May/June 2021 · 12 · Q19, reworded)", opts: ["a rise in the demand for exports", "a rise in the price of raw materials", "a rise in the productivity of labour", "a rise in the rate of sales tax"], a: 0, why: "A rise in export demand raises AD and the price level, which moves the economy along the AS curve. The other options shift AS." },
  { q: "A country imports oil. Why might an increase in the world price of oil have caused a shift in its short-run aggregate supply curve to the left? (May/June 2022 · 12 · Q27, reworded)", opts: ["A rise in inflation is expected", "Consumers face a fall in their disposable income", "Domestic firms' costs have increased", "The government reduces tax on oil and petroleum products"], a: 2, why: "Dearer oil raises firms' costs at every output level, which shifts SRAS." },
  { q: "What is a certain outcome on an aggregate demand and aggregate supply diagram of an increase in factor productivity? (May/June 2022 · 13 · Q24, reworded)", opts: ["downward shift of the aggregate demand curve", "downward shift of the aggregate supply curve", "an upward shift of the aggregate demand curve", "an upward shift of the aggregate supply curve"], a: 1, why: "Higher productivity lowers unit costs, so AS shifts down (to the right)." },
  { q: "Which statement is not correct? (May/June 2025 · 11 · Q19, reworded)", opts: ["The long-run aggregate supply curve can be downward sloping", "The long-run aggregate supply curve can be horizontal", "The long-run aggregate supply curve can be upward sloping", "The long-run aggregate supply curve can be vertical"], a: 0, why: "LRAS may be vertical, horizontal (at low output), or upward sloping in the three-section model, but not downward sloping." },
  { q: "Which supply-side measure is most likely to produce short-run growth in a country's aggregate supply? (Oct/Nov 2023 · 12 · Q26, reworded)", opts: ["easing of controls on immigration of workers", "expenditure on primary education", "expenditure on research and development", "privatisation of public utilities"], a: 0, why: "More workers raise the available labour quickly. Education and R&D take years." },
  { q: "A government decides to use supply-side policy to increase long-run aggregate supply (LRAS). What is the most likely reason why this policy tool will not lead to a fall in the price level? (Feb/March 2025 · 12 · Q24, reworded)", opts: ["Aggregate demand will also increase", "Labour productivity levels will increase", "Workers will save any extra wages they earn", "Workers will spend any extra wages on imports"], a: 0, why: "Higher incomes raise AD, which offsets the downward pressure on prices from higher AS." },
  { q: "Which change is shown directly by the use of aggregate demand and aggregate supply analysis? (May/June 2023 · 12 · Q18, reworded)", opts: ["the nominal income level", "the price level", "the unemployment level", "the wage level"], a: 1, why: "The vertical axis is the price level. Unemployment and wages are inferred." },
  { q: "What will increase if aggregate demand rises when aggregate supply is perfectly elastic? (May/June 2020 · 13 · Q21, reworded)", opts: ["labour shortages", "real output", "the price level", "wage rates"], a: 1, why: "With perfectly elastic AS, extra demand raises output but not prices." },
  { q: "An economy is initially in equilibrium. Which combination of events will definitely cause an increase in the general price level of the economy and a decrease in its real output? (Oct/Nov 2022 · 13 · Q21, reworded)", opts: ["aggregate demand decreases, short-run aggregate supply decreases", "aggregate demand decreases, short-run aggregate supply unchanged", "aggregate demand increases, short-run aggregate supply decreases", "aggregate demand unchanged, short-run aggregate supply decreases"], a: 3, why: "A fall in SRAS with unchanged AD raises the price level and lowers output for certain. In the other cases one of the two effects is uncertain." },
] });
