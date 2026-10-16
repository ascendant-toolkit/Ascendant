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

/* ---------- AD and AS helper ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adas(a, lr) {
  const Q = (a - 15) / 1.6, P = 15 + 0.7 * Q; let s = axes(70, 320, 740, 30, "Real GDP", "Price level");
  s += SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  s += SV.line(AX(0), AY(15), AX(100), AY(85), "c2") + tag(AX(100) - 4, AY(85) - 8, "SRAS", "t2", 1, "end");
  s += SV.line(AX(0), AY(a), AX(100), AY(a - 90), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  s += SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + SV.circle(AX(Q), AY(P), 7, "dot4");
  return { s, Q, P };
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Policy map: demand-side policy shifts AD for cyclical unemployment, supply-side policy shifts LRAS and lowers the natural rate">${(() => { let o = tag(380, 24, "Match the policy to the cause", "t1", 1, "middle"); const rows = [["Cyclical", "AD policy", "fiscal, monetary, exchange rate", "t2"], ["Frictional", "Information", "job centres, vacancy sites", "t1"], ["Structural", "Skills and mobility", "training, housing, regional aid", "t4"], ["Real wage", "Wage flexibility", "union reform, minimum wage review", "t3"], ["Seasonal", "Diversify", "year-round jobs, off-season training", "t1"]]; rows.forEach(([a, b, c, t], i) => { const y = 50 + i * 54; o += SV.rect(60, y, 150, 40, "f1") + SV.text(135, y + 26, a, "lbl bd", { "text-anchor": "middle" }) + arrow(215, y + 20, 290, y + 20, "r", "c1", 1) + SV.rect(295, y, 170, 40, "f4") + SV.text(380, y + 26, b, "lbl bd", { "text-anchor": "middle" }) + tag(480, y + 25, c, t); }); return o; })()}</svg>`;

/* ---------- Watch 1: fiscal stimulus ---------- */
function stimDraw(s) {
  const r = adas(s.a, 60), gap = r.Q - 60, u = gap < 0 ? 5 + 0.6 * -gap : Math.max(2.5, 5 - 0.2 * gap);
  let o = r.s;
  if (Math.abs(gap) > 0.8) o += SV.line(AX(Math.min(r.Q, 60)), 296, AX(Math.max(r.Q, 60)), 296, gap < 0 ? "c2" : "c4", { "stroke-width": 5 }) + tag(AX((r.Q + 60) / 2), 288, gap < 0 ? "negative gap" : "positive gap", gap < 0 ? "t2" : "t4", 1, "middle");
  o += SV.rect(300, 36, 150, 54, "f1") + tag(375, 58, "Unemployment", "t1", 1, "middle") + SV.text(375, 82, Lib.fmtN(u, 1) + "%", "lbl bd", { "text-anchor": "middle", style: "font-size:20px" });
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 365, label: "AD shifting right with a fiscal stimulus: unemployment falls, then inflation rises if the stimulus overshoots", base: { a: 100 }, draw: stimDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>Cyclical unemployment.</b> AD is too low, so equilibrium output is below the LRAS: a negative output gap and unemployment of about 9%, well above the natural rate of 5%.", s: {} },
  { cap: "<b>A fiscal stimulus.</b> The government raises spending or cuts taxes. AD shifts right. Output rises through the multiplier, firms hire and unemployment falls towards the natural rate.", s: { a: 111 } },
  { cap: "<b>The right size.</b> The gap is closed and unemployment is at the natural rate of 5%. A stimulus sized to the gap cuts cyclical unemployment without raising prices much.", s: { a: 111 } },
  { cap: "<b>Overshooting.</b> If the stimulus is too big, output goes above potential. Unemployment can only dip below the natural rate temporarily, and the price level rises: inflation. This is the limit of demand-side policy.", s: { a: 128 } },
] });

/* ---------- Watch 2: policy match ---------- */
function mtDraw(s) {
  const rows = [["Cyclical", "raise AD: fiscal and monetary policy", "t2"], ["Frictional", "better job information", "t1"], ["Structural", "retraining, relocation, regional aid", "t4"], ["Real wage", "union reform, wage flexibility", "t3"], ["Seasonal", "diversify, off-season training", "t1"]];
  let o = ""; rows.forEach(([a, b, t], i) => { const v = Math.max(0, Math.min(1, s.n - i)); const y = 30 + i * 56; o += SV.rect(50, y, 150, 40, "f1") + SV.text(125, y + 26, a, "lbl bd", { "text-anchor": "middle" }); if (v > 0) o += arrow(205, y + 20, 270, y + 20, "r", "c1", v) + SV.rect(275, y, 190, 40, "f4", op(v)) + SV.text(370, y + 26, ["demand-side", "supply-side: information", "supply-side: skills", "supply-side: market-based", "supply-side: structure"][i], "lbl bd", { "text-anchor": "middle", ...op(v) }) + tag(480, y + 25, b, t, v); }); return o;
}
Lib.stepper($("#stM"), { w: 760, h: 320, label: "Each type of unemployment matched to the policy that tackles its cause", base: { n: 0 }, draw: mtDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Cyclical.</b> The cause is too little spending, so the cure is demand-side: more government spending or lower taxes and interest rates.", s: { n: 1 } },
  { cap: "<b>Frictional.</b> The cause is search time, so the cure is information: job centres and online vacancy sites. Extra demand is not needed.", s: { n: 2 } },
  { cap: "<b>Structural.</b> The cause is a skills or location mismatch, so the cure is retraining, relocation help and regional investment.", s: { n: 3 } },
  { cap: "<b>Real wage.</b> The cause is a wage above equilibrium, so the cure is wage flexibility: union reform or a more careful minimum wage.", s: { n: 4 } },
  { cap: "<b>Seasonal.</b> The cause is seasonal demand, so the cure is diversifying local industry and training for off-season work. <b>Using the wrong policy wastes money:</b> demand stimulus does little for structural unemployment.", s: { n: 5 } },
] });

/* ---------- Lab 1: fiscal stimulus size ---------- */
function labStim() {
  if (!$("#gp") || !$("#st") || !$("#km")) return;
  const gap = -+$("#gp").value, S = +$("#st").value / 10, k = +$("#km").value / 10, rise = S * k, after = gap + rise;
  const u = after < 0 ? 5 + 0.6 * -after : Math.max(2.5, 5 - 0.2 * after), infl = after > 0 ? 2 + 0.8 * after : 2, def = S;
  $("#r1").textContent = Lib.fmtN(u, 1) + "%"; $("#r2").textContent = (after >= 0 ? "+" : "") + Lib.fmtN(after, 1) + "%"; $("#r3").textContent = "+" + Lib.fmtN(def, 1) + "%";
  $("#rv").textContent = after < -0.5 ? `A stimulus of ${Lib.fmtN(S, 1)}% of GDP with a multiplier of ${Lib.fmtN(k, 1)} raises output by ${Lib.fmtN(rise, 1)}%. The gap narrows from ${Lib.fmtN(gap, 1)}% to ${Lib.fmtN(after, 1)}%, but unemployment is still ${Lib.fmtN(u - 5, 1)} points above the natural rate. The stimulus is too small, or the multiplier too weak.` : after <= 1 ? `The stimulus raises output by ${Lib.fmtN(rise, 1)}% and almost closes the gap. Unemployment is back at about the natural rate with little inflation pressure. The deficit is ${Lib.fmtN(def, 1)}% of GDP higher.` : `The stimulus raises output by ${Lib.fmtN(rise, 1)}%, pushing output ${Lib.fmtN(after, 1)}% above potential. Unemployment dips below the natural rate temporarily and inflation pressure rises to about ${Lib.fmtN(infl, 1)}%. The stimulus is too large.`;
  const bars = [["Gap before", gap, gap < 0 ? "f2" : "f4"], ["Gap after", after, after < -0.5 ? "f2" : after <= 1 ? "f3" : "f4"]], mx = 12, base = 150, sc = 100 / mx;
  let o = SV.line(40, base, 400, base);
  bars.forEach((b, i) => { const x = 90 + i * 150, h = Math.abs(b[1]) * sc, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, 90, Math.max(h, 2), b[2]) + tag(x + 45, b[1] >= 0 ? y - 8 : y + h + 18, (b[1] >= 0 ? "+" : "") + Lib.fmtN(b[1], 1) + "%", "t1", 1, "middle") + SV.text(x + 45, 280, b[0], "sm bd", { "text-anchor": "middle" }); });
  o += tag(40, 24, "Output gap, % of potential", "t1");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gp", label: "Size of negative output gap (%) ", min: 1, max: 10, step: 1, value: 6, fmt: (v) => v, onInput: labStim });
Lib.slider($("#g2"), { id: "st", label: "Stimulus (% of GDP) ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labStim });
Lib.slider($("#g3"), { id: "km", label: "Multiplier", min: 8, max: 25, step: 1, value: 15, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labStim });
labStim();
btnTable("lbBtns", "lbOut", [
  ["Increase government spending", "Cyclical", "Months to 2 years", "Deficit, crowding out, leakages, inflation near capacity"],
  ["Cut interest rates / QE", "Cyclical", "6 to 18 months", "Weak in a liquidity trap or low confidence; asset bubbles"],
  ["Retraining and apprenticeships", "Structural, youth", "2 to 10 years", "Costly, slow, may not match vacancies"],
  ["Job centres and vacancy information", "Frictional", "Months", "Limited effect if the cause is a skills mismatch"],
  ["Cut benefits or tighten job-search conditions", "Frictional, voluntary, natural rate", "1 to 3 years", "Hardship, inequality, low-quality jobs"],
  ["Cut payroll taxes / hiring subsidies", "Structural, natural rate", "1 to 3 years", "Cost to the government, may subsidise jobs that would exist anyway"],
  ["Weaken union power / reform the minimum wage", "Real wage", "2 to 5 years", "Lower wages, inequality, political resistance"]
], ["Policy", "Mainly targets", "Time lag", "Main weaknesses"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What kind of policy is it?", buckets: [{"label": "Demand-side"}, {"label": "Supply-side (interventionist)"}, {"label": "Supply-side (market-based)"}], items: [{"text": "Cut income tax and raise government spending to boost AD", "b": 0}, {"text": "Fund an apprenticeship scheme", "b": 1}, {"text": "Shorten the period for which unemployment benefits are paid", "b": 2}, {"text": "Cut interest rates", "b": 0}, {"text": "Relocation grants for workers moving to vacancies", "b": 1}, {"text": "Weaken the legal power of trade unions", "b": 2}, {"text": "Quantitative easing", "b": 0}, {"text": "Build a job centre network with vacancy information", "b": 1}], done: "Demand-side moves AD. Interventionist supply-side uses government spending on skills and information. Market-based supply-side relies on incentives and competition." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Cyclical unemployment", "Caused by a fall in aggregate demand"], ["Structural unemployment", "Caused by a mismatch of skills or location"], ["Crowding out", "Government borrowing reduces private investment"], ["Multiplier", "Total rise in income is a multiple of the initial rise in spending"], ["Active labour market policy", "Training, job-search help and subsidies for hiring"], ["Hysteresis", "Cyclical unemployment that becomes long-term"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a fiscal stimulus on cyclical unemployment in order.", items: ["The government raises spending or cuts taxes", "Aggregate demand rises", "Firms see higher sales and increase output", "Firms hire more workers", "Unemployment falls, helped by the multiplier"], done: "The stimulus works through demand for output, then demand for labour." });
Lib.calc($("#c1"), { qs: [
  {"q": "The multiplier is 2 and the government raises spending by $5bn. Calculate the rise in national income ($bn).", "a": 10, "unit": "$bn", "tol": 0.05, "hint": "Multiplier × change in spending.", "sol": "2 × 5 = <b>$10bn</b>."},
  {"q": "The output gap is −6% of potential GDP and the multiplier is 1.5. By what percentage of GDP must government spending rise to close the gap?", "a": 4, "unit": "%", "tol": 0.05, "hint": "Gap ÷ multiplier.", "sol": "6 ÷ 1.5 = <b>4% of GDP</b>."},
  {"q": "A retraining scheme costs the government $12,000 per trainee. 500 of 2,000 trainees find jobs they would not have found otherwise. Calculate the cost per extra job ($).", "a": 48000, "unit": "$", "tol": 1, "hint": "Total cost ÷ extra jobs.", "sol": "Total cost = 2,000 × 12,000 = $24m. Cost per extra job = 24,000,000 ÷ 500 = <b>$48,000</b>."},
  {"q": "Unemployment is 9% and the natural rate is 5%. Using Okun's law (2% of output per point of cyclical unemployment), by what percentage must output rise to remove cyclical unemployment?", "a": 8, "unit": "%", "tol": 0.05, "hint": "4 points × 2.", "sol": "4 × 2 = <b>8%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is most likely to reduce cyclical unemployment?", opts: ["Retraining", "A fall in interest rates", "Relocation grants", "A cut in unemployment benefit"], a: 1, why: "Lower interest rates raise AD, which raises demand for labour." },
  { q: "Which policy best matches structural unemployment?", opts: ["Quantitative easing", "Retraining and relocation support", "A fall in the exchange rate", "A rise in government spending on defence"], a: 1, why: "Structural unemployment is a skills or location mismatch." },
  { q: "What is a main weakness of fiscal stimulus?", opts: ["It cannot raise AD", "It may crowd out private investment and raise debt", "It always lowers prices", "It only affects imports"], a: 1, why: "Borrowing can raise interest rates and the national debt." },
  { q: "What is a main weakness of supply-side policy?", opts: ["It lowers potential output", "It takes a long time to work", "It always raises inflation", "It only affects cyclical unemployment"], a: 1, why: "Skills, mobility and incentives change slowly." },
  { q: "Which would most reduce frictional unemployment?", opts: ["A rise in government spending", "A better online vacancy service", "A fall in interest rates", "A weaker currency"], a: 1, why: "Faster matching of workers and vacancies shortens search time." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Demand-side policy", "Fiscal, monetary or exchange rate policy to raise AD."],
  ["Supply-side policy", "Policy to improve the labour market and raise capacity."],
  ["Interventionist supply-side", "Training, subsidies, job centres, infrastructure."],
  ["Market-based supply-side", "Lower benefits and taxes, weaker unions, deregulation."],
  ["Multiplier", "Total rise in income as a multiple of the initial injection."],
  ["Crowding out", "Government borrowing reduces private investment."],
  ["Active labour market policy", "Training, job-search help and hiring subsidies."],
  ["Time lag", "Delay before a policy takes full effect."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is an example of a Keynesian policy that would reduce cyclical unemployment? (Feb/March 2020 · 32 · Q23, reworded)", opts: ["Government spending on new infrastructure such as roads", "Government spending on retraining workers", "A cut in the tax on imports", "A cut in the tax on goods and services"], a: 0, why: "Keynesian policy raises aggregate demand directly. Retraining is supply-side." },
  { q: "Which of these is a Keynesian measure to reduce cyclical unemployment? (Oct/Nov 2020 · 33 · Q28, reworded)", opts: ["Retraining unskilled workers", "Letting the private sector supply merit goods", "Using more capital equipment per worker", "Using fiscal policy to increase effective demand"], a: 3, why: "Keynesian policy tackles deficient demand through fiscal policy." },
  { q: "Which combination of fiscal, monetary and supply-side policies is most likely to reduce unemployment? (Feb/March 2021 · 32 · Q22, reworded)", opts: ["Raise taxes, raise interest rates, increase labour market flexibility", "Raise government spending, cut the money supply, more education and training", "Cut taxes, cut interest rates, more labour market flexibility", "Cut government spending, raise the money supply, more education and training"], a: 2, why: "Cutting taxes and rates boosts demand, and labour market flexibility improves the supply side." },
  { q: "Which statement is correct about government policy to reduce unemployment? (Oct/Nov 2021 · 33 · Q22, reworded)", opts: ["A government cannot reduce seasonal unemployment", "Changing interest rates is the best way to reduce the natural rate", "A change in the exchange rate cannot reduce demand-deficient unemployment", "Supply-side policy can be used to reduce frictional unemployment"], a: 3, why: "Better job information is supply-side and cuts frictional unemployment." },
  { q: "What is the most effective policy a government could introduce to reduce frictional unemployment? (May/June 2023 · 31 · Q21, reworded)", opts: ["Cut welfare spending", "Improve information about job vacancies", "Reduce tax rates", "Raise interest rates"], a: 1, why: "Frictional unemployment is about search time, so better information is the most direct policy." },
  { q: "There has been a switch in demand from labour-intensive products to products made using high technology. Unemployment has risen. What is the best policy to reduce this unemployment? (May/June 2022 · 31 · Q22, reworded)", opts: ["Cut the rate of income tax", "Raise the interest rate on borrowing for investment", "Subsidise products made by labour-intensive methods", "Subsidise exports of high-technology industries"], a: 2, why: "A subsidy for labour-intensive products raises demand for the labour that was displaced. The other options do not target the mismatch." },
  { q: "Which policy is likely to increase unemployment? (Feb/March 2023 · 32 · Q20, reworded)", opts: ["More retraining facilities", "A large rise in indirect taxes", "Selective import controls", "A larger public sector deficit"], a: 1, why: "Higher indirect taxes cut real incomes and demand, so firms cut jobs." },
  { q: "In an economy with unemployed resources the marginal propensity to consume is 0.2. The government raises its deficit and borrows from the non-bank public. What is the likely consequence? (Feb/March 2025 · 32 · Q24, reworded)", opts: ["The currency will depreciate and the trade deficit will fall", "The rise in real output will be limited because the multiplier is low", "The money supply will fall, reducing aggregate demand", "Interest rates will fall, causing demand-pull inflation"], a: 1, why: "With an MPC of 0.2 the multiplier is only 1.25, so the stimulus has a small effect on output." },
] });
