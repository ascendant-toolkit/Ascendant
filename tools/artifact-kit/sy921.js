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

/* ---------- Learn picture: PPC and LRAS ---------- */
const PX = (v) => 70 + v * 2.6, PY = (v) => 310 - v * 2.6;
function ppc(k, o = "c1", v = 1) { return SV.path(`M ${PX(0)} ${PY(100 * k)} Q ${PX(100 * k)} ${PY(100 * k)} ${PX(100 * k)} ${PY(0)}`, o, op(v)); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="PPC with a point inside, on the curve and outside showing actual growth, and an outward shifted curve showing potential growth">
  ${axes(70, 310, 340, 40, "Consumer goods", "Capital goods")}
  ${ppc(0.9)}${ppc(1.12, "c3 dash", 1)}
  ${SV.circle(PX(40), PY(40), 6, "dot2")}${tag(PX(40) + 10, PY(40) + 18, "A: inside, negative gap", "t2")}
  ${SV.circle(PX(72), PY(52), 6, "dot1")}${tag(PX(72) + 10, PY(52) - 10, "B: on the PPC", "t1")}
  ${tag(PX(40), PY(40) - 14, "", "t2")}
  ${SV.path(`M ${PX(41)} ${PY(41)} L ${PX(66)} ${PY(50)}`, "c4 dash", {})}${tag(150, 120, "actual growth: A to B", "t4")}
  ${tag(70, 352, "dashed curve: the PPC after potential growth", "t3")}
  ${axes(430, 310, 740, 40, "Real GDP", "Price level")}
  ${SV.line(600, 310, 600, 60, "c3")}${tag(606, 70, "LRAS₁", "t3")}${SV.line(675, 310, 675, 60, "c3 dash")}${tag(681, 70, "LRAS₂", "t3")}
  ${SV.path("M 440 280 Q 560 230 720 90", "c2")}${tag(722, 98, "AS", "t2", 1, "end")}${SV.path("M 440 80 Q 540 190 720 280", "c1")}${tag(722, 288, "AD", "t1", 1, "end")}
  ${SV.line(600, 198, 675, 198, "c4", { "stroke-width": 4 })}${tag(637, 190, "potential growth", "t4", 1, "middle")}
</svg>`;

/* ---------- Watch 1: PPC ---------- */
function ppcDraw(s) {
  const k = s.k;
  let o = axes(70, 310, 420, 40, "Consumer goods", "Capital goods") + SV.path(`M ${PX(0)} ${PY(90)} Q ${PX(90)} ${PY(90)} ${PX(90)} ${PY(0)}`, "c1", op(0.4 + 0.6 * (1 - s.s)));
  if (s.s > 0) o += SV.path(`M ${PX(0)} ${PY(90 * k)} Q ${PX(90 * k)} ${PY(90 * k)} ${PX(90 * k)} ${PY(0)}`, "c3", op(s.s));
  const px = s.x, py = s.y;
  o += SV.circle(PX(px), PY(py), 7, s.m > 0.5 ? "dot1" : "dot2");
  if (s.l > 0) o += tag(PX(px) - 50, PY(py) + 22, "inside the PPC: spare capacity", "t2", s.l);
  if (s.g > 0) o += tag(PX(px) + 12, PY(py) - 12, "on the PPC: full use of resources", "t1", s.g);
  if (s.s > 0) o += tag(300, 62, "PPC shifts out: potential growth", "t3", s.s, "middle");
  if (s.q > 0) o += SV.line(PX(54), PY(54), PX(71), PY(66), "c4", { "stroke-width": 4, ...op(s.q) });
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 360, label: "A production possibility curve with a point inside it, a move to the curve and then an outward shift of the curve", base: { k: 1, s: 0, x: 40, y: 40, l: 1, g: 0, m: 0, q: 0 }, draw: ppcDraw, tween: 800, dwell: 5400, steps: [
  { cap: "<b>A negative output gap.</b> The economy is at A, <b>inside</b> its PPC. Some workers and machines are idle, so actual output is below potential.", s: {} },
  { cap: "<b>Actual growth.</b> Demand recovers and idle resources are put back to work. The economy moves from A to B on the curve. Output rises, but <b>potential has not changed</b>.", s: { x: 68, y: 60, l: 0, g: 1, m: 1 } },
  { cap: "<b>The limit.</b> At B the economy is using everything it has. More actual growth is impossible without more capacity. Pushing demand further would only raise prices (a positive output gap).", s: { x: 68, y: 60, l: 0, g: 1, m: 1 } },
  { cap: "<b>Potential growth.</b> Investment, education and new technology shift the whole PPC outwards. The economy can now reach combinations that were impossible before.", s: { x: 78, y: 70, l: 0, g: 0, m: 1, s: 1, k: 1.17 } },
] });

/* ---------- Watch 2: AD and AS with output gaps ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adasDraw(s) {
  const sh = s.sh, lr = s.lr, a = s.a, Q = (a - 15 + 0.7 * sh) / 1.6, P = 15 + 0.7 * (Q - sh);
  let o = axes(70, 320, 740, 30, "Real GDP", "Price level");
  o += SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  o += SV.line(AX(0), AY(15 + 0.7 * (0 - sh)), AX(100), AY(15 + 0.7 * (100 - sh)), "c2") + tag(AX(100) - 4, AY(15 + 0.7 * (100 - sh)) - 8, "SRAS", "t2", 1, "end");
  o += SV.line(AX(0), AY(a), AX(100), AY(a - 0.9 * 100), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  o += SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + SV.circle(AX(Q), AY(P), 7, "dot4") + tag(AX(Q), 338, "Y", "t4", 1, "middle");
  const g = Q - lr;
  if (s.gp > 0 && Math.abs(g) > 0.8) o += SV.line(AX(Math.min(Q, lr)), 296, AX(Math.max(Q, lr)), 296, g < 0 ? "c2" : "c4", { "stroke-width": 5, ...op(s.gp) }) + tag(AX((Q + lr) / 2), 288, g < 0 ? "negative gap" : "positive gap", g < 0 ? "t2" : "t4", s.gp, "middle");
  if (s.gp > 0 && Math.abs(g) <= 0.8) o += tag(AX(lr) - 8, 288, "no gap", "t3", s.gp, "end");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 365, label: "AD and AS with a vertical LRAS showing a negative output gap, no gap and a positive output gap, then LRAS shifting right", base: { a: 100, sh: 0, lr: 60, gp: 0 }, draw: adasDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Potential output.</b> The vertical <b>LRAS</b> is the most the economy can produce without pushing up costs. Here AD and SRAS cross to its left.", s: { gp: 0 } },
  { cap: "<b>A negative output gap.</b> Equilibrium output is <b>below</b> potential. There is spare capacity, so unemployment is likely to be above the natural rate and inflation low.", s: { gp: 1 } },
  { cap: "<b>Demand rises.</b> AD shifts right until the equilibrium is on the LRAS: the economy is at potential and the <b>gap is closed</b>.", s: { gp: 1, a: 111 } },
  { cap: "<b>A positive output gap.</b> If AD keeps rising, output is pushed <b>above</b> potential. Labour and capital are stretched, costs and prices rise faster: inflationary pressure. This cannot last.", s: { gp: 1, a: 128 } },
  { cap: "<b>Potential growth.</b> Better skills, capital and technology shift the LRAS (and SRAS) to the right. The same AD now gives a smaller gap and less inflation pressure, and the economy can grow faster without overheating.", s: { gp: 1, a: 128, lr: 76, sh: 16 } },
] });

/* ---------- Lab 1: output gap ---------- */
function labGap() {
  if (!$("#ya") || !$("#yp")) return;
  const A = +$("#ya").value, P = +$("#yp").value, g = (A - P) / P * 100, lab = Math.abs(g) < 0.5 ? "None" : g > 0 ? "Positive" : "Negative";
  $("#r1").textContent = Lib.fmtN(g, 1) + "%"; $("#r2").textContent = lab;
  $("#r3").textContent = lab === "None" ? "Balanced" : g > 0 ? "Inflation up" : "Unemployment up";
  $("#rv").textContent = lab === "None" ? "Actual output equals potential output. Resources are fully used and inflation should be stable." : g > 0 ? `Actual output is ${Lib.fmtN(g, 1)}% above potential. Firms are stretched, unemployment is probably below its natural rate and inflation is likely to rise.` : `Actual output is ${Lib.fmtN(-g, 1)}% below potential. There is spare capacity, unemployment is probably above its natural rate and inflation is likely to fall.`;
  const mx = Math.max(A, P, 100) * 1.1, y = (v) => 250 - v / mx * 210;
  let o = SV.line(40, 250, 400, 250) + SV.rect(90, y(A), 90, 250 - y(A), "f1") + SV.rect(240, y(P), 90, 250 - y(P), "f3") + tag(135, y(A) - 6, "Actual " + A, "t1", 1, "middle") + tag(285, y(P) - 6, "Potential " + P, "t3", 1, "middle");
  o += SV.line(180, y(A), 330, y(A), "c4 dash") + SV.line(180, y(P), 330, y(P), "c3 dash") + tag(210, 275, "gap " + Lib.fmtN(g, 1) + "%", g < 0 ? "t2" : "t4", 1, "start");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ya", label: "Actual GDP ($bn) ", min: 80, max: 120, step: 1, value: 96, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g2"), { id: "yp", label: "Potential GDP ($bn) ", min: 80, max: 120, step: 1, value: 100, fmt: (v) => v, onInput: labGap });
labGap();
btnTable("lbBtns", "lbOut", [
  ["Government funds a university skills programme", "Potential growth (LRAS shifts right) over time", "Little change now; raises capacity later", "Gap may widen if AD does not keep up", "Supply-side"],
  ["Consumer confidence jumps and spending surges", "Actual growth (AD shifts right)", "Output moves towards or above potential", "Gap becomes less negative or turns positive", "Demand-side"],
  ["An earthquake destroys factories and roads", "Potential falls (LRAS shifts left)", "Actual output falls too", "Gap could be small, with falling living standards", "Supply shock"],
  ["Interest rates rise sharply", "Fall in actual output (AD shifts left)", "Potential unchanged in the short run", "Gap becomes more negative", "Demand-side"],
  ["New oil field and cheaper energy", "Potential growth (LRAS and SRAS shift right)", "Actual output rises and prices fall", "Gap unchanged or smaller; less inflation pressure", "Supply-side"],
  ["Export orders collapse in a global recession", "Actual output falls (AD shifts left)", "Potential unchanged", "Negative gap opens", "Demand-side"]
], ["Event", "What moves", "Immediate effect", "Effect on the gap", "Type"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the event mainly raise actual growth or potential growth?", buckets: [{"label": "Actual growth"}, {"label": "Potential growth"}], items: [{"text": "Firms use idle machines after demand picks up", "b": 0}, {"text": "Government cuts income tax and spending rises", "b": 0}, {"text": "A new apprenticeship scheme raises skills", "b": 1}, {"text": "Investment in broadband infrastructure", "b": 1}, {"text": "Unemployed workers return to jobs in a recovery", "b": 0}, {"text": "A breakthrough in battery technology", "b": 1}, {"text": "A boom in exports raises output from existing factories", "b": 0}, {"text": "Net migration raises the size of the workforce", "b": 1}], done: "Actual growth uses spare capacity. Potential growth adds capacity." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Actual growth", "The percentage rise in real GDP over a period"], ["Potential growth", "A rise in the productive capacity of the economy"], ["Positive output gap", "Actual output is above potential output"], ["Negative output gap", "Actual output is below potential output: spare capacity"], ["LRAS", "The vertical curve showing potential output"], ["Inflationary gap", "Expenditure above the level that gives full employment on a Keynesian cross"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a rising positive output gap in order.", items: ["Aggregate demand rises above what the economy can supply", "Firms compete for scarce workers and materials", "Wages and input costs rise", "Firms raise prices and inflation increases", "The central bank raises interest rates to cool demand"], done: "A positive gap tends to lead to inflation, then tighter policy." });
Lib.calc($("#c1"), { qs: [
  {"q": "Actual GDP is $1,040bn and potential GDP is $1,000bn. Calculate the output gap as a percentage of potential GDP.", "a": 4, "unit": "%", "tol": 0.05, "hint": "(actual − potential) ÷ potential × 100.", "sol": "(1040 − 1000) ÷ 1000 × 100 = <b>4%</b>, a positive gap."},
  {"q": "Real GDP rises from $2,500bn to $2,575bn. Calculate the rate of actual economic growth.", "a": 3, "unit": "%", "tol": 0.05, "hint": "Change ÷ original × 100.", "sol": "75 ÷ 2500 × 100 = <b>3%</b>."},
  {"q": "Potential GDP is $800bn and actual GDP is $760bn. Calculate the output gap as a percentage of potential GDP. Use a minus sign for a negative gap.", "a": -5, "unit": "%", "tol": 0.05, "hint": "Actual is below potential, so the answer is negative.", "sol": "(760 − 800) ÷ 800 × 100 = <b>−5%</b>, a negative gap."},
  {"q": "A closed economy has equilibrium income of $900m. Full employment income is $1,000m and the marginal propensity to consume is 0.75. What size of rise in spending (in $m) would close the gap?", "a": 25, "unit": "$m", "tol": 0.05, "hint": "Multiplier = 1 ÷ (1 − MPC). Gap in income ÷ multiplier.", "sol": "Multiplier = 1 ÷ 0.25 = 4. Income gap = 100, so spending must rise by 100 ÷ 4 = <b>$25m</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An economy moves from inside its PPC towards the curve. What has occurred?", opts: ["Potential growth", "Actual growth", "A fall in the output gap to zero from a positive gap", "A fall in productive capacity"], a: 1, why: "A move towards the curve uses spare capacity: actual growth. Potential growth would shift the curve." },
  { q: "Which would most likely raise potential output?", opts: ["A cut in interest rates", "A rise in government spending", "An increase in the number of skilled workers", "A fall in the exchange rate"], a: 2, why: "More and better factors of production shift the LRAS. The others mainly move AD." },
  { q: "An economy has a negative output gap. Which is most likely?", opts: ["Unemployment above its natural rate", "Rising inflation", "Output above capacity", "A shortage of skilled labour"], a: 0, why: "Spare capacity means unemployment above the natural rate and weak inflation pressure." },
  { q: "Actual growth is 4% a year and potential growth is 2.5% a year. What is likely to happen to the output gap?", opts: ["It will move towards negative", "It will become more positive", "It will stay the same", "It will disappear"], a: 1, why: "Output is growing faster than capacity, so the gap becomes more positive (or less negative)." },
  { q: "Which statement about the output gap is correct?", opts: ["It is observed directly in national accounts", "It is an estimate because potential output cannot be measured exactly", "It always equals the inflation rate", "It is the same as the budget deficit"], a: 1, why: "Potential output has to be estimated, so the output gap is an estimate that is often revised." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Actual growth", "Percentage change in real GDP over a period."],
  ["Potential growth", "Rise in the economy's productive capacity (LRAS or PPC shifts out)."],
  ["Output gap", "Actual output minus potential output, as a % of potential."],
  ["Positive output gap", "Actual above potential: inflation pressure, unemployment below natural rate."],
  ["Negative output gap", "Actual below potential: spare capacity, cyclical unemployment."],
  ["Inflationary gap", "Expenditure above full-employment output on a Keynesian cross."],
  ["Deflationary gap", "Expenditure short of full-employment output on a Keynesian cross."],
  ["Trend growth", "The average rate of growth of potential output over time."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What movement on a production possibility diagram shows actual economic growth? (Feb/March 2025 · 32 · Q16, reworded)", opts: ["A positive output gap", "A move from a point inside the curve towards the curve", "A recession", "An outward shift of the curve"], a: 1, why: "Actual growth uses existing capacity; an outward shift of the curve is potential growth." },
  { q: "What does an output gap show? (Oct/Nov 2021 · 33 · Q18, reworded)", opts: ["The gap between actual output and long-run potential output", "The gap between maximum output in a boom and minimum output in a recession", "The gap between exports and imports", "The gap between actual output and output at full employment of labour only"], a: 0, why: "Output gap is actual output minus long-run potential output." },
  { q: "What is most likely in an economy with a positive output gap? (May/June 2022 · 31 · Q24, reworded)", opts: ["Potential GDP above actual GDP", "High unemployment", "Inflation", "Low labour costs"], a: 2, why: "Output above potential stretches resources, so inflation tends to rise." },
  { q: "An economy has a positive output gap. What is happening to growth and the price level? (May/June 2025 · 31 · Q17, reworded)", opts: ["Growth below trend, prices falling", "Growth above trend, prices rising", "Growth below trend, prices rising", "Growth above trend, prices falling"], a: 1, why: "Above-trend growth pushes output over potential and puts upward pressure on prices." },
  { q: "An economy has a negative output gap. What is most likely to happen to inflation and unemployment? (Oct/Nov 2022 · 32 · Q24, reworded)", opts: ["Inflation falls, unemployment falls", "Inflation falls, unemployment rises", "Inflation rises, unemployment falls", "Inflation rises, unemployment rises"], a: 1, why: "Spare capacity means weak price pressure and unemployment above its natural rate." },
  { q: "A closed economy with no government has equilibrium income of $1,000bn. Households spend 80% of any income. Full employment income is $1,200bn. By how much must aggregate demand rise initially to close the deflationary gap? (Oct/Nov 2021 · 33 · Q26, reworded)", opts: ["−$200bn", "−$40bn", "+$40bn", "+$200bn"], a: 2, why: "Multiplier = 1 ÷ 0.2 = 5. Income gap $200bn ÷ 5 = $40bn of extra spending." },
  { q: "What may prevent a government achieving a faster rate of growth of real GDP? (Feb/March 2020 · 32 · Q30, reworded)", opts: ["Consumption and investment are sensitive to interest rates", "Inflation is below the central bank target", "The economy is already operating on its long-run aggregate supply curve", "There is a large negative output gap"], a: 2, why: "If the economy is already at potential output on LRAS, more demand only raises prices; faster growth needs a shift in LRAS." },
] });
