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

/* ---------- components stack ---------- */
function acDraw(s) {
  const Y = (v) => 250 - v * 1.7; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn at the current price level", "sm");
  const parts = [["C", s.c, "f1"], ["I", s.i, "f2"], ["G", s.g, "f3"], ["X", s.x, "f1"]]; let y = 250;
  parts.forEach(([l, v, c], k) => { const h = v * 1.7; if (v > 0.5) o += SV.rect(150 + k * 0, y - h, 140, h, c, op(0.65)) + SV.text(220, y - h / 2 + 5, l + " " + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }); y -= h; });
  if (s.m > 0.5) { const h = s.m * 1.7; o += SV.rect(340, 250 - h, 140, h, "f3", op(0.65)) + SV.text(410, 250 - h / 2 + 5, "M " + Lib.fmtN(s.m, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(410, 270, "Imports (subtracted)", "sm", { "text-anchor": "middle" }); }
  const ad = s.c + s.i + s.g + s.x - s.m; o += SV.text(220, 270, "Gross spending", "sm", { "text-anchor": "middle" }) + SV.line(500, Y(ad), 700, Y(ad), "c4", { "stroke-dasharray": "6 4", "stroke-width": 2 }) + tag(704, Y(ad) + 4, "AD = " + Lib.fmtN(ad, 0), "c4", 1, "end");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Consumption, investment, government spending and exports add up, with imports subtracted, to aggregate demand">${acDraw({ c: 60, i: 20, g: 25, x: 25, m: 30 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 290, label: "C + I + G + X − M", base: { c: 0, i: 0, g: 0, x: 0, m: 0 }, draw: acDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Consumption (C)</b>: household spending, the largest component, here $60bn.", s: { c: 60 } },
  { cap: "<b>Investment (I)</b>: firms' spending on capital, $20bn.", s: { c: 60, i: 20 } },
  { cap: "<b>Government spending (G)</b> on public services and infrastructure, $25bn.", s: { c: 60, i: 20, g: 25 } },
  { cap: "<b>Exports (X)</b>: foreign spending on domestic output, $25bn.", s: { c: 60, i: 20, g: 25, x: 25 } },
  { cap: "<b>Imports (M)</b> are subtracted, because they are spending that does not go to domestic output. AD = 60 + 20 + 25 + 25 − 30 = $100bn.", s: { c: 60, i: 20, g: 25, x: 25, m: 30 } },
] });

/* ---------- movement and shift ---------- */
function msDraw(s) {
  let o = axes(70, 270, 720, 25, "Real output (Y)", "Price level") + sdCurve("D", 0, "c2", s.a > 0.05 ? 0.4 : 1, "AD1");
  if (s.a > 0.05) o += sdCurve("D", s.a, "c2", 1, "AD2");
  const p = s.p, q = (90 - p) / 0.8 + (s.a > 0.05 ? s.a * (s.k || 0) : 0); o += SV.line(SDX(q), SDY(p), SDX(q), 270, "dash") + SV.line(70, SDY(p), SDX(q), SDY(p), "dash") + SV.circle(SDX(q), SDY(p), 7, "dot3") + SV.text(62, SDY(p) + 4, Lib.fmtN(p, 0), "sm", { "text-anchor": "end" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in the price level moves along AD, while a rise in a component shifts AD right">${msDraw({ p: 40, a: 20, k: 0 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A movement along AD and a shift of AD", base: { p: 50, a: 0, k: 0 }, draw: msDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> At a price level of 50, planned spending on domestic output is 50 units.", s: { p: 50, a: 0, k: 0 } },
  { cap: "<b>The price level falls to 35.</b> Real wealth rises, interest rates fall and exports become cheaper, so spending rises along the same AD curve: a <b>movement along</b>.", s: { p: 35, a: 0, k: 0 } },
  { cap: "<b>Interest rates fall.</b> At every price level consumers and firms want to spend more, so the whole AD curve <b>shifts right</b> to AD2. At a price level of 35 spending is now higher still.", s: { p: 35, a: 20, k: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labC() {
  const ids = ["cc", "ii", "gg", "xx", "mm"]; if (!ids.every((i) => $("#" + i))) return;
  const [c, i, g, x, m] = ids.map((k) => +$("#" + k).value), ad = c + i + g + x - m;
  $("#r1").textContent = "$" + ad + "bn"; $("#r2").textContent = (x - m >= 0 ? "+" : "") + (x - m); $("#r3").textContent = (ad - 100 >= 0 ? "+" : "") + (ad - 100);
  $("#rv").textContent = `AD = ${c} + ${i} + ${g} + (${x} − ${m}) = ${ad}. ${ad > 100 ? "Higher than the starting $100bn: the AD curve has shifted to the right." : ad < 100 ? "Lower than the starting $100bn: the AD curve has shifted to the left." : "Equal to the starting $100bn: no shift."} Net exports are ${x - m >= 0 ? "a surplus" : "a deficit"} of ${Math.abs(x - m)}.`;
  $("#labA").innerHTML = acDraw({ c, i, g, x, m });
}
[["g1", "cc", "Consumption (C), $bn ", 60], ["g2", "ii", "Investment (I), $bn ", 20], ["g3", "gg", "Government spending (G), $bn ", 25], ["g4", "xx", "Exports (X), $bn ", 25], ["g5", "mm", "Imports (M), $bn ", 30]].forEach(([el, id, lab, v]) => Lib.slider($("#" + el), { id, label: lab, min: 0, max: 80, step: 5, value: v, fmt: (z) => z, onInput: labC }));
labC();

/* ---------- Lab 2 ---------- */
const EVA = [["Interest rates fall", "C and I", 15], ["Income tax rises", "C", -15], ["Consumer confidence falls", "C", -20], ["Currency depreciates", "X − M", 15], ["Government spends more on roads", "G", 15], ["Trading partners' incomes rise", "X", 15], ["Business confidence rises", "I", 15], ["Currency appreciates", "X − M", -15]];
function showA(i) {
  const [n, comp, a] = EVA[i], e = sdEq(a, 0), e0 = sdEq(0, 0); $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = comp; $("#t2").textContent = a > 0 ? "Shifts right" : "Shifts left"; $("#t3").textContent = (e.q > e0.q ? "Output up, " : "Output down, ") + (e.p > e0.p ? "prices up" : "prices down");
  $("#tv").textContent = `${n}: this changes ${comp}, so AD shifts ${a > 0 ? "right" : "left"} at every price level. In the short run real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 0)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 0)} (from 50 each), using an upward-sloping SRAS curve.`;
  $("#labB").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 }, { lras: false });
}
$("#evB").innerHTML = EVA.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showA(+b.dataset.i)));
showA(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which component of AD changes?", buckets: [{"label": "Consumption (C)"}, {"label": "Investment (I)"}, {"label": "Government spending (G)"}, {"label": "Net exports (X − M)"}], items: [{"text": "Households spend more after an income tax cut", "b": 0}, {"text": "A firm buys new machinery", "b": 1}, {"text": "The state builds a new hospital", "b": 2}, {"text": "Foreign buyers purchase more of the country's cars", "b": 3}, {"text": "Consumer confidence falls", "b": 0}, {"text": "Business confidence rises", "b": 1}, {"text": "The currency depreciates", "b": 3}, {"text": "The government employs more teachers", "b": 2}], done: "C: households. I: firms' capital. G: government. X − M: trade." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Aggregate demand", "Total planned spending on an economy's output at each price level"], ["Wealth effect", "A lower price level raises the real value of savings"], ["Shift of AD", "A change in a component at every price level"], ["Movement along AD", "Caused only by a change in the price level"], ["Net exports", "Exports minus imports"], ["Interest rate effect", "A lower price level lowers interest rates and raises spending"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of lower interest rates on output in order.", items: ["The central bank cuts interest rates", "Borrowing becomes cheaper", "Consumption and investment rise", "The AD curve shifts to the right", "Real output rises and the price level may rise"], done: "Lower rates raise C and I, shifting AD right." });
Lib.calc($("#c1"), { qs: [
  {"q": "C = 400, I = 120, G = 150, X = 130, M = 140. What is AD ($bn)?", "a": 660, "unit": "$bn", "tol": 0.5, "hint": "400 + 120 + 150 + 130 − 140.", "sol": "<b>$660bn</b>."},
  {"q": "In the same economy, what are net exports ($bn)? (use a minus sign for a deficit)", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "130 − 140.", "sol": "<b>−$10bn</b>, a deficit."},
  {"q": "Investment rises by $30bn. What is the new AD ($bn)?", "a": 690, "unit": "$bn", "tol": 0.5, "hint": "660 + 30.", "sol": "<b>$690bn</b>."},
  {"q": "What is the percentage rise in AD (to one decimal place)?", "a": 4.5, "unit": "%", "tol": 0.1, "hint": "30 ÷ 660.", "sol": "<b>4.5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "AD equals:", opts: ["C + I + G + (X − M)", "C + S + T", "I + G + X", "C − I − G"], a: 0, why: "The four components." },
  { q: "A fall in the price level causes:", opts: ["A movement along AD", "A leftward shift of AD", "A rightward shift of AD", "A fall in G"], a: 0, why: "Only the price level moves along the curve." },
  { q: "Which would shift AD to the right?", opts: ["A fall in interest rates", "A rise in income tax", "An appreciation", "A cut in government spending"], a: 0, why: "Cheaper borrowing." },
  { q: "Imports are:", opts: ["Subtracted in AD", "Added in AD", "Part of G", "Part of C only"], a: 0, why: "They are spending that leaks abroad." },
  { q: "A fall in consumer confidence would:", opts: ["Shift AD left", "Shift AD right", "Shift AS right", "Shift LRAS"], a: 0, why: "Consumption falls." },
] });
Lib.cards($("#fc1"), { cards: [
  ["AD", "C + I + G + (X − M)."],
  ["Slope", "Wealth, interest, trade effects."],
  ["Shift right", "Lower rates, lower taxes, confidence."],
  ["Shift left", "Higher rates, cuts, appreciation."],
  ["Movement along", "Price level only."],
  ["Not in G", "Transfer payments."],
  ["Net exports", "X − M."],
  ["Effect", "Depends on the AS curve."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is a correct description of an aggregate demand (AD) curve? (May/June 2022 · 13 · Q21, reworded)", opts: ["It is a curve obtained by adding the market demand curves of all consumer goods traded in an economy", "It is a curve determined by the horizontal summation of all individual consumer demand curves for a product", "It is a curve that shows the total amount of goods and services firms are willing to buy at a given price in an economy", "It is a curve that shows the total demand of all goods and services produced at all price levels in an economy"], a: 3, why: "AD shows total planned spending on domestic output at each price level." },
  { q: "The diagram shows an aggregate demand (AD) curve with X on the horizontal axis and Y on the vertical axis. What is measured on each axis? (May/June 2022 · 13 · Q19, reworded)", opts: ["X: money national output, Y: real disposable income", "X: price level, Y: real GDP", "X: real GDP, Y: price level", "X: real disposable income, Y: money national output"], a: 2, why: "AD is drawn with real GDP (output) on the horizontal axis and the price level on the vertical axis." },
  { q: "What are the components of aggregate demand? (Oct/Nov 2021 · 13 · Q30, reworded)", opts: ["consumption + investment + government spending + (exports − imports)", "consumption + investment + taxation − (exports − imports)", "consumption + saving + taxation − (exports − imports)", "consumption + saving + taxation + (exports − imports)"], a: 0, why: "AD = C + I + G + (X − M)." },
  { q: "Which statement explains why the aggregate demand curve is downward sloping? (May/June 2023 · 11 · Q18, reworded)", opts: ["As prices fall, the demand for exports becomes more elastic", "As prices fall, fewer goods are imported", "As prices fall, the rate of interest will rise", "As prices fall, real wealth rises and so spending increases"], a: 3, why: "The wealth effect: a lower price level raises the real value of savings, so spending rises." },
  { q: "Why would a fall in a country's average price level cause its aggregate demand curve to slope downwards? (May/June 2024 · 11 · Q19, reworded)", opts: ["It leads to an increase in interest rates", "It reduces the real value of money balances", "It makes the country's goods cheaper relative to foreign goods", "It leads to the expectation of further price falls"], a: 2, why: "Cheaper domestic goods boost exports and cut imports, raising net exports." },
  { q: "The aggregate demand curve is typically downward sloping. What is one possible explanation for this? (May/June 2025 · 12 · Q18, reworded)", opts: ["A fall in the price level will lead to a rise in demand for imports", "As the price level falls, improved productivity will reduce unit costs", "If the price level is high, any interest rate changes will encourage consumption", "The real value of assets increases as the price level falls"], a: 3, why: "A lower price level raises the real value of assets, which raises spending (the wealth effect)." },
  { q: "Why might aggregate demand increase when a country's price level falls? (May/June 2023 · 12 · Q19, reworded)", opts: ["Domestic interest rates will tend to fall", "Imports become more price competitive", "Real incomes fall", "The purchasing power of savings falls"], a: 0, why: "A lower price level reduces demand for money, so interest rates tend to fall and spending rises." },
  { q: "What is the most likely cause of an outward shift of a country's aggregate demand curve? (May/June 2023 · 13 · Q25, reworded)", opts: ["a decrease in the competitiveness of domestically produced products", "a decrease in the general price level", "a decrease in the money supply", "a depreciation of the country's exchange rate"], a: 3, why: "A depreciation raises net exports. A price-level fall is a movement along." },
  { q: "An increase in what will shift the aggregate demand curve in an economy to the right? (Oct/Nov 2022 · 12 · Q20, reworded)", opts: ["budget deficit", "consumer savings", "general price level", "interest rate"], a: 0, why: "A larger deficit means higher government spending or lower taxes, raising AD." },
  { q: "What is likely to cause a decrease in aggregate demand? (May/June 2020 · 12 · Q19, reworded)", opts: ["an appreciation in the exchange rate", "an improvement in consumer confidence", "an increase in government expenditure", "an increase in the money supply"], a: 0, why: "An appreciation makes exports dearer and imports cheaper, lowering net exports." },
  { q: "Aggregate demand in an economy may decrease as a result of an increase in which of the following? (Feb/March 2024 · 12 · Q19, reworded)", opts: ["consumption expenditure", "government expenditure", "import expenditure", "investment expenditure"], a: 2, why: "Imports are subtracted in AD, so higher spending on imports lowers it." },
  { q: "A government increases the rate of income tax. What is the effect, in the short run, on the aggregate demand curve or the aggregate supply curve? (Oct/Nov 2023 · 12 · Q24, reworded)", opts: ["The aggregate demand curve shifts left", "The aggregate demand curve shifts right", "The aggregate supply curve shifts left", "The aggregate supply curve shifts right"], a: 0, why: "Higher income tax cuts disposable income and consumption, so AD shifts left." },
] });
