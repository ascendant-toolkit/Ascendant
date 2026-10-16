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

/* ---------- Transmission chain ---------- */
const TB = [["Central bank raises the policy rate", 40, 30, "f4"], ["Loan and mortgage rates rise; saving pays more", 40, 120, "f1"], ["Consumption and investment fall; asset prices fall", 40, 210, "f1"], ["Aggregate demand shifts left", 400, 210, "f2"], ["Output gap narrows, price pressure falls", 400, 120, "f3"], ["Inflation falls (after 12 to 24 months)", 400, 30, "f3"]];
function transDraw(s) {
  let o = "";
  TB.forEach(([l, x, y, c], i) => { const v = Math.max(0, Math.min(1, s.n - i)); if (v <= 0) return; o += SV.rect(x, y, 320, 62, c, op(v)) + SV.text(x + 160, y + 36, l, "lbl bd", { "text-anchor": "middle", ...op(v) }); });
  const AR = [[200, 94, 200, 118, "d"], [200, 184, 200, 208, "d"], [365, 241, 395, 241, "r"], [560, 208, 560, 184, "u"], [560, 118, 560, 94, "u"]];
  AR.forEach((a, i) => { const v = Math.max(0, Math.min(1, s.n - i - 0.5)); if (v > 0) o += arrow(a[0], a[1], a[2], a[3], a[4], "c1", v); });
  if (s.x > 0) o += tag(380, 316, "also: exchange rate rises, import prices fall, and expectations of inflation fall", "t3", s.x, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Chain from a rise in the policy interest rate to lower inflation">${transDraw({ n: 7, x: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 330, label: "Monetary transmission mechanism from a higher interest rate to lower inflation", base: { n: 0, x: 0 }, draw: transDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The decision.</b> Inflation is above target, so the central bank raises its policy interest rate.", s: { n: 1.4 } },
  { cap: "<b>Market rates.</b> Banks raise lending rates, so loans and mortgages are dearer. Saving earns more.", s: { n: 2.4 } },
  { cap: "<b>Spending.</b> Households cut consumption, firms cut investment, and the value of bonds, shares and houses falls, reducing wealth and spending.", s: { n: 3.4 } },
  { cap: "<b>Aggregate demand falls.</b> The AD curve shifts to the left. A stronger currency and lower inflation expectations also work in the same direction.", s: { n: 4.4, x: 1 } },
  { cap: "<b>Prices.</b> Demand falls back towards capacity and inflation falls, but only after a lag of 12 to 24 months, at the cost of lower growth and higher unemployment.", s: { n: 6.5, x: 1 } },
] });

/* ---------- AD and AS: demand-pull and cost-push ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adasDraw(s) {
  const a = s.a, sh = s.sh, lr = 60, Q = (a - 15 + 0.7 * sh) / 1.6, P = 15 + 0.7 * (Q - sh);
  let o = axes(70, 320, 740, 30, "Real GDP", "Price level") + SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  o += SV.line(AX(0), AY(15 + 0.7 * (0 - sh)), AX(100), AY(15 + 0.7 * (100 - sh)), "c2") + tag(AX(100) - 4, AY(15 + 0.7 * (100 - sh)) - 8, "SRAS", "t2", 1, "end");
  o += SV.line(AX(0), AY(a), AX(100), AY(a - 90), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  o += SV.circle(AX(Q), AY(P), 7, "dot4") + SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + tag(AX(Q) + 10, AY(P) + 22, "P " + Lib.fmtN(P, 0) + ", Q " + Lib.fmtN(Q, 0), "t4");
  return o + tag(380, 345, s.l, "t1", 1, "middle");
}
Lib.stepper($("#stA"), { w: 760, h: 360, label: "AD and AS showing demand-pull inflation cured by lower AD, and cost-push inflation where lower AD cuts output", base: { a: 111, sh: 0, l: "" }, draw: adasDraw, tween: 1000, dwell: 6000, steps: [
  { cap: "<b>Starting point.</b> AD, SRAS and LRAS meet at potential output (60) with price level 57.", s: { l: "stable prices at potential output" } },
  { cap: "<b>Demand-pull.</b> AD rises (booming spending). Output goes above potential and the price level rises to about 66: <b>demand-pull inflation</b>.", s: { a: 128, l: "demand-pull: AD shifts right" } },
  { cap: "<b>The cure.</b> Higher interest rates and tighter fiscal policy shift AD back to the left. Prices fall back and output returns to potential, with little lasting loss. The right tool for this cause.", s: { a: 111, l: "AD back: prices and output normal" } },
  { cap: "<b>Cost-push.</b> Dearer oil shifts SRAS to the left. The price level rises and output <b>falls</b> below potential: stagflation.", s: { a: 111, sh: -12, l: "cost-push: SRAS shifts left" } },
  { cap: "<b>The wrong cure.</b> Cutting AD to bring prices down would lower output <b>even further</b> and raise unemployment. Supply-side policy, a stronger currency or wage restraint (shifting SRAS right) would be better.", s: { a: 100, sh: -12, l: "cutting AD: prices fall a little, output falls a lot" } },
] });

/* ---------- Lab 1: interest rate rise ---------- */
function labIR() {
  if (!$("#ir") || !$("#cs") || !$("#is")) return;
  const d = +$("#ir").value / 10, cs = +$("#cs").value / 10, is = +$("#is").value / 10, dC = cs * d * 0.6, dI = is * d * 0.2, dAD = dC + dI;
  const dInf = 0.4 * dAD, dU = 0.5 * dAD;
  $("#r1").textContent = "−" + Lib.fmtN(dAD, 1) + "%"; $("#r2").textContent = "−" + Lib.fmtN(dInf, 1) + " pts"; $("#r3").textContent = "+" + Lib.fmtN(dU, 1) + " pts";
  $("#rv").textContent = d === 0 ? "No change in the interest rate." : `A ${Lib.fmtN(d, 1)} point rise cuts consumption (60% of AD) by ${Lib.fmtN(dC / 0.6, 1)}% and investment (20% of AD) by ${Lib.fmtN(dI / 0.2, 1)}%, so AD falls ${Lib.fmtN(dAD, 1)}%. Inflation falls about ${Lib.fmtN(dInf, 1)} points, but unemployment rises about ${Lib.fmtN(dU, 1)} points (Okun's law). If spending is insensitive to interest rates, the policy is weak and needs a larger rate rise.`;
  const mx = Math.max(dAD, 1) * 1.2, Y = (v) => 250 - v / mx * 200; let o = SV.line(40, 250, 400, 250);
  [["Consumption", dC, "f1"], ["Investment", dI, "f4"], ["Total AD", dAD, "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 110, h = v / mx * 200; o += SV.rect(x, 250 - h, 80, Math.max(h, 2), c) + tag(x + 40, 250 - h - 6, "−" + Lib.fmtN(v, 1) + "%", "t1", 1, "middle") + SV.text(x + 40, 270, l, "sm bd", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ir", label: "Rise in interest rate (points) ", min: 0, max: 60, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labIR });
Lib.slider($("#g2"), { id: "cs", label: "Sensitivity of consumption (% fall per point) ", min: 2, max: 20, step: 1, value: 8, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labIR });
Lib.slider($("#g3"), { id: "is", label: "Sensitivity of investment (% fall per point) ", min: 5, max: 60, step: 5, value: 30, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labIR });
labIR();
btnTable("lbBtns", "lbOut", [
  ["Raise interest rates", "Demand-pull (and expectations)", "12 to 24 months", "Lower growth and jobs; stronger currency hurts exporters"],
  ["Cut government spending / raise taxes", "Demand-pull", "6 to 18 months", "Political resistance; harms public services and growth"],
  ["Supply-side reform", "Cost-push; long-run inflation", "3 to 10 years", "Slow and costly"],
  ["Appreciation of the exchange rate", "Imported and cost-push", "Months", "Hurts exports and the current account"],
  ["Wage restraint / incomes policy", "Wage-push, expectations", "Months", "Hard to enforce; may cause a rebound or strikes"],
  ["Inflation target and central bank independence", "Expectations", "Builds over years", "Needs credibility; conflicts with jobs in the short run"],
  ["Reverse quantitative easing / slower money growth", "Excess money growth", "12 to 24 months", "Harder to control; may raise long-term rates"]
], ["Policy", "Mainly tackles", "Time lag", "Main cost"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which policy is best suited to the cause?", buckets: [{"label": "Cut AD (monetary or fiscal tightening)"}, {"label": "Supply-side / cost-side policy"}], items: [{"text": "Spending is booming and output is above potential", "b": 0}, {"text": "Oil prices double and firms' costs rise", "b": 1}, {"text": "Wages are growing faster than productivity", "b": 1}, {"text": "A positive output gap with rising demand for credit", "b": 0}, {"text": "A weak currency makes imported raw materials dearer", "b": 1}, {"text": "Consumers borrow heavily as interest rates stay low", "b": 0}, {"text": "High taxes on fuel raise production costs", "b": 1}, {"text": "Government spending has risen sharply in an economy at full employment", "b": 0}], done: "Cut AD for demand-pull. Cut costs or raise supply for cost-push." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Transmission mechanism", "The chain from an interest rate change to spending and prices"], ["Demand-pull inflation", "Inflation because AD exceeds capacity"], ["Cost-push inflation", "Inflation because costs rise and SRAS shifts left"], ["Inflation target", "A declared level of inflation the central bank aims at"], ["Incomes policy", "Restraint on wage and price rises"], ["Sacrifice ratio", "Output or jobs lost per point of inflation removed"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the transmission mechanism in order.", items: ["The central bank raises the policy interest rate", "Borrowing costs rise and saving becomes more rewarding", "Consumption and investment fall", "Aggregate demand shifts left", "Inflationary pressure falls, after a lag"], done: "Policy works through borrowing, spending and AD." });
Lib.calc($("#c1"), { qs: [
  {"q": "Nominal interest rate is 6% and inflation is 2.5%. Calculate the real interest rate (%).", "a": 3.5, "unit": "%", "tol": 0.05, "hint": "Nominal minus inflation.", "sol": "6 − 2.5 = <b>3.5%</b>."},
  {"q": "A government cuts spending by $20bn. The multiplier is 1.5. Calculate the fall in national income ($bn).", "a": 30, "unit": "$bn", "tol": 0.05, "hint": "20 × 1.5.", "sol": "<b>$30bn</b>."},
  {"q": "Imports are 25% of the price index. The currency appreciates and import prices fall 8%. Calculate the effect on the price level (%), ignoring other changes.", "a": -2, "unit": "%", "tol": 0.05, "hint": "25% of −8%.", "sol": "0.25 × −8 = <b>−2%</b>."},
  {"q": "Investment falls by 6% when interest rates rise 2 points. Calculate the interest elasticity of investment (% change in investment per point).", "a": -3, "tol": 0.05, "hint": "−6 ÷ 2.", "sol": "<b>−3% per point</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is best suited to demand-pull inflation?", opts: ["Higher interest rates", "Supply-side policy only", "A depreciation", "Lower taxes"], a: 0, why: "Higher rates reduce AD." },
  { q: "Which would be the least costly way to reduce cost-push inflation?", opts: ["Cutting AD sharply", "Supply-side policy that raises productivity", "Lower taxes", "More money supply"], a: 1, why: "Raising productivity shifts supply right and cuts costs." },
  { q: "Which is a reason monetary policy may not work?", opts: ["Time lags and low interest elasticity of spending", "Interest rates have no effect on borrowing", "Central banks cannot set rates", "Inflation is always demand-pull"], a: 0, why: "Lags and insensitivity to rates reduce effectiveness." },
  { q: "An independent central bank with a clear inflation target tends to:", opts: ["Lower expected inflation", "Raise expected inflation", "Remove all lags", "Eliminate unemployment"], a: 0, why: "Credibility lowers expectations and so the cost of disinflation." },
  { q: "A cost of using a stronger currency to cut inflation is:", opts: ["Lower export competitiveness", "Higher import prices", "Higher inflation", "More imported inflation"], a: 0, why: "A higher exchange rate makes exports dearer abroad." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Demand-pull", "AD above capacity pushes prices up."],
  ["Cost-push", "Higher costs shift SRAS left."],
  ["Transmission mechanism", "Chain from interest rate to inflation."],
  ["Inflation target", "Declared level of inflation to aim for."],
  ["Incomes policy", "Limits on wage and price rises."],
  ["Credibility", "Belief that policy will be followed."],
  ["Sacrifice ratio", "Cost in output of cutting inflation."],
  ["Imported inflation", "Dearer imports raise prices."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a closed economy the central bank raises interest rates to reduce rising inflation. Which policy objective is it targeting? (May/June 2025 · 32 · Q21, reworded)", opts: ["A current account surplus", "Faster economic growth", "Full employment", "Stable prices"], a: 3, why: "Higher rates reduce demand and are used to control inflation." },
  { q: "An economy is operating at full employment. Which policy is most likely to raise real output without raising inflation in the short term? (Oct/Nov 2022 · 31 · Q30, reworded)", opts: ["Subsidies to increase export earnings", "Quantitative easing", "Labour market reforms that raise output per hour", "A cut in income tax"], a: 2, why: "Supply-side reforms raise productivity and capacity, so output rises without extra demand." },
  { q: "A government cuts its main interest rate to stimulate growth. What might reduce the effectiveness of this? (May/June 2021 · 31 · Q18, reworded)", opts: ["Rising investor expectations", "More borrowing taking place", "Falling savings", "A falling marginal propensity to consume"], a: 3, why: "If households spend a smaller share of any extra income, cheaper borrowing raises spending less." },
  { q: "A government wants to raise real GDP using only fiscal and monetary policies. Which combination is most effective? (May/June 2021 · 31 · Q23, reworded)", opts: ["A bigger budget deficit and the central bank buying back government bonds", "A smaller budget deficit and the central bank selling bonds", "A smaller deficit and lower rates", "A bigger deficit and higher interest rates"], a: 0, why: "A larger deficit raises AD and the central bank buying bonds lowers interest rates and raises the money supply." },
  { q: "The government raises interest rates to reduce inflation. What will also result? (Feb/March 2024 · 32 · Q23, reworded)", opts: ["A depreciation of the currency", "A fall in savings", "A reduction in economic growth", "A reduction in unemployment"], a: 2, why: "Higher rates cut spending and investment so growth slows." },
  { q: "Which macroeconomic policy is most likely to be used as a long-run means of reducing inflationary pressure? (Feb/March 2020 · 32 · Q29, reworded)", opts: ["Exchange rate policy", "Fiscal policy", "Monetary policy", "Supply-side policy"], a: 3, why: "Supply-side policy raises capacity and productivity, which reduces cost pressure over time." },
] });
