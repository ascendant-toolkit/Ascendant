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

/* ---------- Marshall-Lerner bars ---------- */
const MB = (v) => 300 - v * 2.3;
function mlDraw(s) {
  let o = axes(70, 300, 730, 30, "", "Value ($m)"); [0, 50, 100].forEach((v) => (o += SV.text(64, MB(v) + 4, v, "sm", { "text-anchor": "end" })));
  o += SV.line(70, MB(100), 730, MB(100), "gr dash", op(0.6));
  const bx = (i, v, c, l, k) => SV.rect(130 + i * 200, MB(v), 90, 300 - MB(v), c, op(k)) + tag(175 + i * 200, MB(v) - 8, Lib.fmtN(v, 1), "t1", k, "middle") + tag(175 + i * 200, 322, l, "t1", k, "middle");
  o += bx(0, s.x, "f1", "Export revenue", 1) + bx(1, s.m, "f2", "Import spending", 1);
  const b = s.x - s.m; o += tag(620, 120, "Balance", "t1", 1, "middle") + tag(620, 156, (b >= 0 ? "+" : "") + Lib.fmtN(b, 1), b >= 0 ? "t3" : "t2", 1, "middle");
  if (s.n > 0) o += tag(620, 190, s.n === 1 ? "sum = 1.4: improves" : "sum = 0.5: worsens", "t4", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Export revenue and import spending bars after a depreciation when the Marshall-Lerner condition holds">${mlDraw({ x: 108, m: 103.4, n: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 340, label: "A 10 percent depreciation: export revenue and import spending when the elasticity sum is high and low", base: { x: 100, m: 100, n: 0 }, draw: mlDraw, tween: 1100, dwell: 6200, steps: [
  { cap: "<b>Start.</b> Trade is balanced: exports $100m, imports $100m.", s: { x: 100, m: 100, n: 0 } },
  { cap: "<b>The price effect.</b> A 10% depreciation raises the home price of imports by 10% at once. Before quantities change, the import bill rises to $110m and the balance falls to −$10m.", s: { x: 100, m: 110, n: 0 } },
  { cap: "<b>Elastic demand (PEDx 0.8, PEDm 0.6, sum 1.4).</b> Exports rise 8% to $108m and import volumes fall 6%, so imports cost $103.4m. The balance improves to +$4.6m: Marshall-Lerner holds.", s: { x: 108, m: 103.4, n: 1 } },
  { cap: "<b>Inelastic demand (PEDx 0.3, PEDm 0.2, sum 0.5).</b> Exports rise only 3% to $103m and import volumes fall just 2%, so imports cost $107.8m. The balance is −$4.8m: the condition fails.", s: { x: 103, m: 107.8, n: 2 } },
] });

/* ---------- J curve ---------- */
const jb = (t) => -10 - 10 * (t / 2) * Math.exp(1 - t / 2) + 15 * (1 - Math.exp(-t / 4));
const JX = (t) => 90 + t * 52, JY = (b) => 190 - b * 7;
function jDraw(s) {
  let o = axes(70, 300, 730, 30, "Time after the depreciation", "Current account balance"); o += SV.line(70, JY(0), 730, JY(0), "gr", op(0.7)) + SV.text(66, JY(0) + 4, "0", "sm", { "text-anchor": "end" }) + SV.line(JX(0), 40, JX(0), 300, "c4 dash", op(0.8)) + tag(JX(0) + 6, 52, "depreciation", "t4");
  const pts = []; for (let t = -0.35; t <= s.p * 12 + 0.001 && t <= 12; t += 0.25) pts.push([JX(t), JY(t <= 0 ? -10 : jb(t))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  const t0 = Math.min(12, s.p * 12), last = pts.length ? pts[pts.length - 1] : [JX(0), JY(-10)];
  o += SV.circle(last[0], last[1], 6, "dot4");
  if (s.l > 0) o += tag(JX(3), 320, "Short run: contracts and habits, low elasticities", "t2", s.l, "middle");
  if (s.l > 1) o += tag(JX(7), 232, "Adjustment: elasticities rise", "t1", Math.min(1, s.l - 1), "middle");
  if (s.l > 2) o += tag(JX(11), JY(3.5) - 12, "Long run: ML holds", "t3", Math.min(1, s.l - 2), "end");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="J curve: the current account falls after a depreciation then rises above its starting level">${jDraw({ p: 1, l: 3 })}</svg>`;
Lib.stepper($("#stJ"), { w: 760, h: 340, label: "J curve: current account balance over time after a depreciation", base: { p: 0, l: 0 }, draw: jDraw, tween: 1500, dwell: 6200, steps: [
  { cap: "<b>Before.</b> The country has a current account deficit of about 10 units. The currency then depreciates.", s: { p: 0, l: 0 } },
  { cap: "<b>Short run.</b> Contracts are already agreed and buyers are slow to switch, so quantities barely change but the import bill rises. The <b>deficit widens</b> to about 14.", s: { p: 0.17, l: 1 } },
  { cap: "<b>Adjustment.</b> As contracts end, consumers switch and exporters expand, elasticities rise. The balance starts to recover and passes its starting level.", s: { p: 0.6, l: 2 } },
  { cap: "<b>Long run.</b> The sum of elasticities is above 1, so the current account is better than before the depreciation. The path looks like the letter J.", s: { p: 1, l: 3 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!$("#dp") || !$("#ex") || !$("#im")) return;
  const d = +$("#dp").value / 100, ex = +$("#ex").value / 10, im = +$("#im").value / 10, x = 100 * (1 + ex * d), m = 100 * (1 + d) * (1 - im * d), b = x - m, sum = ex + im;
  $("#r1").textContent = Lib.fmtN(sum, 1); $("#r2").textContent = Lib.fmtN(x, 1) + " / " + Lib.fmtN(m, 1); $("#r3").textContent = (b >= 0 ? "+" : "") + Lib.fmtN(b, 1);
  $("#rv").textContent = sum > 1.001 ? `The sum of the elasticities (${Lib.fmtN(sum, 1)}) is above 1: the Marshall-Lerner condition holds, so the balance improves to ${b >= 0 ? "+" : ""}${Lib.fmtN(b, 1)}.` : sum < 0.999 ? `The sum (${Lib.fmtN(sum, 1)}) is below 1: the condition fails and the balance worsens to ${Lib.fmtN(b, 1)}. The dearer import bill outweighs the export gain.` : "The sum is exactly 1: roughly no change in the balance (the exact result depends on the starting position).";
  const Y = (v) => 270 - v * 1.7; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m", "sm");
  [["Exports before", 100, "f1"], ["Exports after", x, "f1"], ["Imports before", 100, "f2"], ["Imports after", m, "f2"]].forEach(([l, v, c], i) => { const px = 55 + i * 88; o += SV.rect(px, Y(v), 60, 270 - Y(v), c, i % 2 ? {} : op(0.55)) + SV.text(px + 30, 288, l.split(" ")[1], "sm", { "text-anchor": "middle" }) + tag(px + 30, Y(v) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  o += SV.text(115, 304, "Exports", "sm", { "text-anchor": "middle" }) + SV.text(291, 304, "Imports", "sm", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dp", label: "Depreciation, % ", min: 5, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "ex", label: "PED of exports × 10 ", min: 0, max: 20, step: 1, value: 8, fmt: (v) => (v / 10).toFixed(1), onInput: labM });
Lib.slider($("#g3"), { id: "im", label: "PED of imports × 10 ", min: 0, max: 20, step: 1, value: 6, fmt: (v) => (v / 10).toFixed(1), onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labJ() {
  if (!$("#sr") || !$("#lr")) return;
  const sr = +$("#sr").value / 10, lr = +$("#lr").value / 10, f = (t) => -10 + 20 * ((sr + (lr - sr) * (1 - Math.exp(-t / 3))) - 1);
  let lo = 0, lt = 0; for (let t = 0; t <= 12; t += 0.1) { if (f(t) < lo) { lo = f(t); } } lo = Math.min(lo, -10);
  const end = f(12), shape = sr < 1 && lr > 1 ? "J curve" : sr >= 1 ? "Improves at once" : "Never improves";
  $("#t1").textContent = Lib.fmtN(lo, 1); $("#t2").textContent = (end >= 0 ? "+" : "") + Lib.fmtN(end, 1); $("#t3").textContent = shape;
  $("#tv").textContent = shape === "J curve" ? `Short-run elasticities sum to ${sr.toFixed(1)} (below 1), so the account worsens first, to about ${Lib.fmtN(lo, 1)}. They rise to ${lr.toFixed(1)} (above 1), so by period 12 the balance is ${Lib.fmtN(end, 1)}.` : shape === "Improves at once" ? "With the short-run sum already above 1, the current account improves straight away, so there is no J." : "The long-run sum stays below 1, so the Marshall-Lerner condition never holds and the current account stays worse than before.";
  const X = (t) => 40 + t * 28, Y = (b) => 150 - b * 6; let o = SV.line(40, 280, 400, 280) + SV.line(40, 280, 40, 20) + SV.text(400, 296, "Time", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Current account balance", "sm") + SV.line(40, Y(-10), 400, Y(-10), "gr dash", op(0.7)) + SV.text(44, Y(-10) - 6, "start", "sm");
  const pts = []; for (let t = 0; t <= 12; t += 0.25) pts.push([X(t), Math.max(25, Math.min(275, Y(f(t))))]);
  $("#labB").innerHTML = o + SV.path(Lib.ptsPath(pts), "c1");
}
Lib.slider($("#g4"), { id: "sr", label: "Short-run PEDx + PEDm × 10 ", min: 2, max: 14, step: 1, value: 6, fmt: (v) => (v / 10).toFixed(1), onInput: labJ });
Lib.slider($("#g5"), { id: "lr", label: "Long-run PEDx + PEDm × 10 ", min: 6, max: 24, step: 1, value: 16, fmt: (v) => (v / 10).toFixed(1), onInput: labJ });
labJ();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens to the current account?", buckets: [{"label": "Improves"}, {"label": "Worsens"}, {"label": "No change"}], items: [{"text": "Depreciation when PEDx + PEDm = 1.6", "b": 0}, {"text": "Depreciation when PEDx + PEDm = 0.6", "b": 1}, {"text": "Depreciation in the short run, when contracts are fixed and elasticities are low", "b": 1}, {"text": "Depreciation in the long run when the sum exceeds 1", "b": 0}, {"text": "Depreciation when PEDx + PEDm = 1.0", "b": 2}, {"text": "Devaluation when the country imports only essential goods with very inelastic demand", "b": 1}, {"text": "Revaluation when PEDx + PEDm = 1.8", "b": 1}, {"text": "Revaluation when PEDx + PEDm = 0.5", "b": 0}], done: "Depreciation improves the balance if the sum is above 1. A revaluation does the opposite." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Marshall-Lerner condition", "PEDx + PEDm > 1 for a depreciation to improve the current account"], ["J curve", "A current account that worsens before it improves"], ["Price effect", "Imports cost more in home currency after a depreciation"], ["Volume effect", "Export sales rise and import purchases fall"], ["Inverse J", "A revaluation that first improves, then worsens, the account"], ["Net exports", "Exports minus imports, a component of AD"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the J curve in order.", items: ["The exchange rate depreciates", "Import prices rise but quantities hardly change (contracts, habits)", "The current account deficit widens", "Elasticities rise as consumers and firms adjust", "The current account improves above its starting level"], done: "Low elasticities first, higher elasticities later." });
Lib.calc($("#c1"), { qs: [
  {"q": "PEDx is 0.9 and PEDm is 0.4. Calculate PEDx + PEDm.", "a": 1.3, "unit": "", "tol": 0.01, "hint": "Add them.", "sol": "<b>1.3</b>, which is above 1: depreciation should improve the current account."},
  {"q": "A 10% depreciation is followed by a rise in export volumes with PEDx = 1.2. By what percentage do export volumes rise (%)?", "a": 12, "unit": "%", "tol": 0.05, "hint": "PED × % change in price.", "sol": "1.2 × 10% = <b>12%</b>."},
  {"q": "Imports cost $200m. After a depreciation their home-currency price rises 8% and volume falls 5%. Calculate the new import spending ($m, 1 decimal place).", "a": 205.2, "unit": "$m", "tol": 0.1, "hint": "200 × 1.08 × 0.95.", "sol": "200 × 1.08 × 0.95 = <b>$205.2m</b>."},
  {"q": "Exports were $200m and rise 6%. Imports are $205.2m. Calculate the new trade balance ($m, 1 decimal place).", "a": 6.8, "unit": "$m", "tol": 0.1, "hint": "212 − 205.2.", "sol": "<b>+$6.8m</b>, so the balance has improved from 0."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The Marshall-Lerner condition says a depreciation improves the current account if:", opts: ["PEDx + PEDm > 1", "PEDx + PEDm < 1", "PEDx = PEDm", "Both elasticities are zero"], a: 0, why: "The sum of the elasticities must be greater than 1." },
  { q: "The J curve occurs because, in the short run:", opts: ["Elasticities are low", "Elasticities are very high", "Inflation falls", "Exports fall"], a: 0, why: "Contracts and habits delay the response." },
  { q: "A depreciation will raise the price of:", opts: ["Imports in home currency", "Exports in home currency", "Domestic services only", "Nothing"], a: 0, why: "Imports cost more in home currency." },
  { q: "Which makes the Marshall-Lerner condition less likely to hold?", opts: ["Many substitutes for imports", "Imports are essential and have no substitutes", "Exporters have spare capacity", "Plenty of time has passed"], a: 1, why: "Inelastic demand for imports keeps the sum low." },
  { q: "A depreciation could cause inflation because:", opts: ["Imports and imported inputs cost more", "Exports fall", "Interest rates fall", "Wages fall"], a: 0, why: "Imported inflation and higher AD." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Marshall-Lerner", "Depreciation improves the current account if PEDx + PEDm > 1."],
  ["J curve", "Current account worsens first, then improves."],
  ["Why a J?", "Short-run elasticities are low."],
  ["Inverse J", "A revaluation may improve, then worsen, the account."],
  ["Price effect", "Imports dearer in home currency."],
  ["Volume effect", "More exports sold, fewer imports bought."],
  ["Net exports", "X − M, part of AD."],
  ["Costs of depreciation", "Imported inflation, dearer foreign debt, retaliation."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The diagram shows a J curve: a fall in the exchange rate worsens the current account before it improves it. What is said to explain this? (May/June 2023 · 32 · Q28, reworded)", opts: ["A time lag before price changes are recognised and acted on", "An improvement in the quality of goods produced", "Demand for imports and exports is elastic in the short run", "The supply of goods is price elastic"], a: 0, why: "In the short run buyers and sellers react slowly, so elasticities are low and the dearer import bill dominates." },
  { q: "What does the J-curve effect show? (May/June 2024 · 31 · Q26, reworded)", opts: ["A depreciation works only if the sum of the elasticities of demand for exports and imports exceeds 1", "After a devaluation the current account is likely to get worse before it gets better", "In the short run the demand for imports and exports is usually price elastic", "The terms of trade decide how well a devaluation works"], a: 1, why: "The J-curve describes the time path: a worse current account first, then an improvement." },
  { q: "A government devalues its currency to move the current account from deficit to surplus. Under which condition would this succeed? (May/June 2024 · 32 · Q27, reworded)", opts: ["If the combined price elasticity of demand for exports and imports is greater than 1", "If the combined price elasticity is less than 1", "If income elasticity of demand is less than 1", "If other countries impose tariffs on all imports"], a: 0, why: "This is the Marshall-Lerner condition." },
  { q: "The values below are short-run (SR) and long-run (LR) elasticities for exports (PEDx) and imports (PEDm). In which case does a depreciation produce a J curve? A: SR 0.5 and 0.2; LR 0.6 and 0.6. B: SR 0.5 and 0.6; LR 1.2 and 1.0. C: SR 0.6 and 0.6; LR 0.5 and 0.2. D: SR 1.2 and 1.0; LR 0.5 and 0.6. (May/June 2025 · 34 · Q27, reworded)", opts: ["A", "B", "C", "D"], a: 0, why: "In A the short-run sum is 0.7 (below 1, so the account worsens) and the long-run sum is 1.2 (above 1, so it improves). In B the short-run sum is already 1.1." },
  { q: "A revaluation raises the exchange rate. The short-run PEDx and PEDm are 0.4 and 0.4 and the long-run values are 0.8 and 0.8. What shape would the current account take over time? (May/June 2025 · 31 · Q27, reworded)", opts: ["It rises, and keeps rising", "It rises, then falls", "It falls, then rises", "It falls, and keeps falling"], a: 1, why: "In the short run the sum is 0.8 (below 1) so a revaluation improves the balance. In the long run the sum is 1.6 (above 1), so it then worsens: an inverse J." },
  { q: "How would a depreciation of the currency of a low-income economy most likely affect these objectives: raising the growth rate, reducing the current account deficit, reducing unemployment? (May/June 2025 · 34 · Q29, reworded)", opts: ["Raises growth and reduces unemployment but not the deficit", "It helps all three", "Reduces the deficit and unemployment but not growth", "Reduces the deficit only"], a: 1, why: "Cheaper exports and dearer imports can increase net exports, raising AD, output and jobs and narrowing the deficit, provided the elasticity conditions are met." },
  { q: "Both the elasticity of demand for imported raw materials and the elasticity of demand for exports are 0.3. What is the effect of a depreciation on cost-push and demand-pull inflation? (Oct/Nov 2020 · 32 · Q29, reworded)", opts: ["Cost-push falls; demand-pull falls", "Cost-push falls; demand-pull rises", "Cost-push rises; demand-pull falls", "Cost-push rises; demand-pull rises"], a: 2, why: "With inelastic imports the import bill and costs rise (cost-push up). With inelastic exports net exports fall, which lowers AD (demand-pull down)." },
] });
