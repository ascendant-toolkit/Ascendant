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

/* ---------- equilibrium picture ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD, SRAS and LRAS with equilibrium output below potential output">${adasPlot({ a: 0, s: 0, l: 0, g: 1, n: 0 })}</svg>`;
function ex2(s) { return adasPlot({ a: s.a, s: s.s, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifts right and output and the price level rise">${ex2({ a: 20, s: 0, n: 1 })}</svg>`;
Lib.stepper($("#stX"), { w: 760, h: 300, label: "Shifts of AD and SRAS and their effects", base: { a: 0, s: 0, n: 0 }, draw: ex2, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD1 and SRAS1 meet at a price level of 50 and real output of 50, below potential output (LRAS at 75): there is spare capacity.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>AD shifts right</b> (for example lower interest rates). Real output and employment rise and the price level rises: <b>demand-pull</b>.", s: { a: 20, s: 0, n: 1 } },
  { cap: "<b>SRAS shifts left</b> (costs rise). The price level rises and output falls: <b>stagflation</b>.", s: { a: 0, s: -20, n: 1 } },
  { cap: "<b>AD and SRAS both shift right.</b> Output rises for certain. The price level is uncertain: here AD rises more than SRAS, so prices rise slightly.", s: { a: 25, s: 15, n: 1 } },
] });

/* ---------- three-section AS ---------- */
const ASP = [[0, 14], [10, 15], [35, 18], [60, 35], [72, 65], [75, 100]];
const asf = (q) => { if (q > 75) return 1000; for (let i = 1; i < ASP.length; i++) if (q <= ASP[i][0]) { const [x0, y0] = ASP[i - 1], [x1, y1] = ASP[i]; return y0 + (y1 - y0) * (q - x0) / (x1 - x0); } return 100; };
function eqAS(c) { let q = 0; for (; q <= 75; q += 0.05) if (asf(q) >= c - 0.8 * q) break; q = Math.min(q, 75); return { q, p: Math.max(0, Math.min(c - 0.8 * q, 110)) }; }
function zoneOf(q) { return q < 40 ? "Flat: spare capacity" : q < 70 ? "Upward sloping" : "Vertical: full capacity"; }
function azDraw(s) {
  const e = eqAS(s.c); let o = axes(70, 270, 720, 25, "Real output (Y)", "Price level");
  o += SV.path("M" + ASP.map(([q, p]) => SDX(q) + "," + SDY(p)).join(" L"), "c1", { fill: "none", "stroke-width": 3.5 }) + tag(SDX(75) + 8, SDY(95), "AS (three sections)", "c1");
  o += SV.line(SDX(0), SDY(s.c), SDX(Math.min(100, s.c / 0.8)), SDY(0), "c2", { "stroke-width": 3 }) + tag(SDX(Math.min(100, s.c / 0.8)) - 40, SDY(8), "AD", "c2");
  o += SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash") + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash") + SV.circle(SDX(e.q), SDY(e.p), 7, "dot3") + SV.text(SDX(e.q), 286, Lib.fmtN(e.q, 0), "sm", { "text-anchor": "middle" }) + SV.text(62, SDY(e.p) + 4, Lib.fmtN(e.p, 0), "sm", { "text-anchor": "end" });
  return o;
}
$("#pic1").innerHTML = $("#pic1").innerHTML;
Lib.stepper($("#stZ"), { w: 760, h: 300, label: "An AD increase on three parts of the AS curve", base: { c: 45 }, draw: azDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>Deep recession.</b> The economy is on the flat part of AS with plenty of spare capacity (output about 34, price level about 18).", s: { c: 45 } },
  { cap: "<b>AD rises on the flat part.</b> Output rises from about 34 to 43, while the price level rises only from about 18 to 24. Unemployment falls.", s: { c: 58 } },
  { cap: "<b>Normal conditions (sloping part).</b> Equilibrium output is 60 and the price level 35.", s: { c: 83 } },
  { cap: "<b>AD rises on the sloping part.</b> Output rises from 60 to about 65 and the price level from 35 to about 48: both rise.", s: { c: 100 } },
  { cap: "<b>Near full capacity.</b> AD rises on the vertical part: output can barely rise (about 74 at most) so the price level shoots up, to about 91. This is <b>demand-pull inflation</b>.", s: { c: 150 } },
] });

/* ---------- Lab 1 ---------- */
function labE() {
  if (!["ad", "sr"].every((i) => $("#" + i))) return;
  const a = +$("#ad").value, s = +$("#sr").value, e = sdEq(a, s), gap = 75 - e.q;
  $("#r1").textContent = Lib.fmtN(e.q, 1); $("#r2").textContent = Lib.fmtN(e.p, 1); $("#r3").textContent = gap > 0 ? "Spare capacity " + Lib.fmtN(gap, 1) : "Inflationary " + Lib.fmtN(-gap, 1);
  $("#rv").textContent = `AD shifts ${a > 0 ? "right" : a < 0 ? "left" : "not at all"} and SRAS ${s > 0 ? "right" : s < 0 ? "left" : "not at all"}. Real output is ${Lib.fmtN(e.q, 1)} (from 50) and the price level ${Lib.fmtN(e.p, 1)} (from 50). Output is ${gap > 0 ? Lib.fmtN(gap, 1) + " below potential (75), so there is spare capacity and unemployment" : "at or above potential output, so the economy is overheating and inflationary pressure builds"}. ${a * s > 0 ? "With both curves moving the same way one effect is certain (output), while the other depends on which shift is bigger." : ""}`;
  $("#labA").innerHTML = adasPlot({ a, s, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "ad", label: "AD shift (negative = left, positive = right) ", min: -30, max: 40, step: 5, value: 15, fmt: (v) => v, onInput: labE });
Lib.slider($("#g2"), { id: "sr", label: "SRAS shift (negative = left, positive = right) ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labE });
labE();

/* ---------- Lab 2 ---------- */
function labZ() {
  if (!$("#cz")) return;
  const c = +$("#cz").value, e = eqAS(c), e0 = eqAS(c - 20), dq = e.q - e0.q, dp = e.p - e0.p;
  $("#t1").textContent = Lib.fmtN(e.q, 1); $("#t2").textContent = Lib.fmtN(e.p, 1); $("#t3").textContent = zoneOf(e.q);
  $("#tv").textContent = `Equilibrium output is ${Lib.fmtN(e.q, 1)} and the price level ${Lib.fmtN(e.p, 1)}: ${zoneOf(e.q).toLowerCase()}. A further rise in AD of 20 at this point would change output by ${Lib.fmtN(dq, 1)} and prices by ${Lib.fmtN(dp, 1)} (compared with the position at AD 20 lower): ${dq > dp * 0.5 && e.q < 70 ? "mostly output" : e.q >= 70 ? "mostly prices" : "both"}.`;
  $("#labB").innerHTML = azDraw({ c });
}
Lib.slider($("#g3"), { id: "cz", label: "Position of AD (higher = more demand) ", min: 45, max: 160, step: 5, value: 80, fmt: (v) => v, onInput: labZ });
labZ();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens to real output and the price level?", buckets: [{"label": "Output up, price level up"}, {"label": "Output down, price level up"}, {"label": "Output up, price level down"}, {"label": "Output down, price level down"}], items: [{"text": "AD shifts right", "b": 0}, {"text": "SRAS shifts left", "b": 1}, {"text": "SRAS shifts right", "b": 2}, {"text": "AD shifts left", "b": 3}, {"text": "Lower interest rates", "b": 0}, {"text": "A rise in raw material prices", "b": 1}, {"text": "Falling energy costs", "b": 2}, {"text": "A fall in consumer confidence", "b": 3}], done: "AD moves output and prices the same way; SRAS moves them in opposite ways." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Macroeconomic equilibrium", "Where AD equals short-run aggregate supply"], ["Negative output gap", "Actual output below potential output"], ["Stagflation", "Rising prices with falling output"], ["Demand-pull inflation", "Prices rise because AD rises when capacity is limited"], ["Potential output", "Output at full employment: LRAS"], ["Inflationary gap", "Actual output above potential output"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of an AD increase near full capacity in order.", items: ["AD shifts to the right", "Firms cannot raise output because resources are fully employed", "Competition for resources pushes up costs", "The price level rises", "Real output rises little or not at all"], done: "At full capacity extra demand is inflationary." });
Lib.calc($("#c1"), { qs: [
  {"q": "Equilibrium output is 880 and potential output is 1,000. What is the output gap (negative means spare capacity)?", "a": -120, "unit": "", "tol": 0.5, "hint": "880 − 1,000.", "sol": "<b>−120</b>, a negative output gap."},
  {"q": "Real GDP rises from 900 to 927 after AD shifts right. What is the % growth?", "a": 3, "unit": "%", "tol": 0.1, "hint": "27 ÷ 900.", "sol": "<b>3%</b>."},
  {"q": "The price level index rises from 100 to 104 over the same period. What is the % change in the price level?", "a": 4, "unit": "%", "tol": 0.1, "hint": "4 ÷ 100.", "sol": "<b>4%</b>."},
  {"q": "Using the output gap of −120 on potential output of 1,000, what is the gap as a percentage of potential output?", "a": -12, "unit": "%", "tol": 0.2, "hint": "−120 ÷ 1,000.", "sol": "<b>−12%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Macroeconomic equilibrium is where:", opts: ["AD equals SRAS", "AD equals LRAS only", "SRAS equals LRAS only", "Output is zero"], a: 0, why: "Intersection of AD and SRAS." },
  { q: "A leftward shift of SRAS causes:", opts: ["Higher prices and lower output", "Lower prices and higher output", "Higher prices and higher output", "No change"], a: 0, why: "Cost-push." },
  { q: "An AD increase raises mainly prices when:", opts: ["The economy is near full capacity", "There is much spare capacity", "SRAS is flat", "Unemployment is high"], a: 0, why: "Output cannot rise." },
  { q: "Real output is below potential. This means:", opts: ["Spare capacity", "Overheating", "Zero unemployment", "Full employment"], a: 0, why: "A negative output gap." },
  { q: "Stagflation is:", opts: ["Rising prices and falling output", "Falling prices and rising output", "Rising prices and rising output", "Falling prices and falling output"], a: 0, why: "SRAS shifts left." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Equilibrium", "AD = SRAS."],
  ["Long-run", "AD = SRAS = LRAS."],
  ["AD right", "Output and prices up."],
  ["SRAS left", "Prices up, output down."],
  ["Flat AS", "AD rise: output."],
  ["Vertical AS", "AD rise: prices."],
  ["Output gap", "Actual minus potential."],
  ["Employment", "Follows output."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a closed economy a rise in aggregate demand is needed to increase output in the country. What is necessary to achieve this increase in output in the economy? (Feb/March 2020 · 12 · Q27, reworded)", opts: ["enough capacity to produce the extra goods and services demanded", "free trade to allow imports to make up any shortages in supply", "government spending to be less than tax revenue", "reduced credit to lower inflation"], a: 0, why: "Output can rise only if the economy has spare capacity to produce the extra goods and services." },
  { q: "The diagram shows that when aggregate demand increases from AD1 to AD2 the average price level rises from P1 to P2, along a vertical LRAS curve. Which statement relating to this change in aggregate demand is correct? (May/June 2024 · 13 · Q16, reworded)", opts: ["Nominal GDP has increased", "Nominal GDP is unchanged", "Real GDP has increased", "Real GDP has fallen"], a: 0, why: "On a vertical LRAS, real GDP stays at its potential level while prices rise, so nominal GDP (output times price) rises." },
  { q: "Which statement correctly describes an increase in real GDP? (May/June 2025 · 11 · Q16, reworded)", opts: ["Nominal GDP rising faster than nominal income", "Nominal GDP rising faster than the rate of inflation", "The rate of inflation rising faster than aggregate demand", "The rate of inflation rising faster than nominal income"], a: 1, why: "Real GDP rises when nominal GDP grows by more than the price level." },
  { q: "A government uses expansionary monetary policy over a three-year period. Which combination identifies the likely impact of such a policy on real GDP, the price level and unemployment? (May/June 2025 · 11 · Q23, reworded)", opts: ["falling, rising, falling", "rising, rising, rising", "rising, rising, falling", "rising, falling, rising"], a: 2, why: "Expansionary policy shifts AD right, raising real GDP and the price level, so unemployment falls." },
  { q: "What is least likely to rise as a result of the use of expansionary fiscal policy? (Feb/March 2023 · 12 · Q28, reworded)", opts: ["aggregate demand", "budget surplus", "nominal income", "inflation"], a: 1, why: "Higher spending or lower taxes raise AD, nominal income and inflation, but reduce any budget surplus." },
  { q: "To counter deflation a central bank uses expansionary monetary policy. What is likely to result? (May/June 2024 · 11 · Q20, reworded)", opts: ["a higher cost of borrowing", "an increase in aggregate demand", "an appreciation of the exchange rate", "an increase in government debt"], a: 1, why: "Lower interest rates raise AD." },
  { q: "Under which combination of circumstances will a policy of increasing the money supply be most effective at moving an economy out of recession? (circumstance one, circumstance two) (Oct/Nov 2020 · 12 · Q19, reworded)", opts: ["depreciating exchange rate, global financial crisis", "high nominal interest rates, appreciating exchange rate", "low aggregate demand, inflation rate above the target level", "low nominal interest rates, no spare capacity available"], a: 1, why: "High interest rates leave room to cut them, and a currency that appreciates is not the constraint, so more money supply can raise AD." },
  { q: "The government wishes to increase aggregate demand. Which actions would be most likely to succeed? (Oct/Nov 2021 · 11 · Q30, reworded)", opts: ["a reduction in income tax and an increase in interest rates", "a reduction in income tax and an increase in production subsidies", "an increase in corporate tax and an increase in government spending", "an increase in value added tax and a reduction in government spending"], a: 1, why: "Lower income tax raises consumption, and subsidies boost production, raising spending." },
] });
