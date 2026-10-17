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

/* ---------- Web of objectives ---------- */
const OBJ = ["Inflation", "Unemployment", "Growth", "Current account", "Sustainability", "Equity"];
const WC = 380, WCY = 165, WR = 120;
const wp = (i) => { const a = -Math.PI / 2 + i * Math.PI / 3; return [WC + Math.cos(a) * WR, WCY + Math.sin(a) * WR]; };
const LINKS = [[0, 1, "c", 1], [2, 0, "c", 2], [2, 3, "c", 2], [2, 4, "c", 3], [2, 5, "c", 3], [3, 0, "c", 3], [2, 1, "g", 4], [4, 0, "g", 4]];
function webDraw(s) {
  let o = "";
  LINKS.forEach(([a, b, k, st]) => { const v = Math.max(0, Math.min(1, s.n - st + 1)); if (v <= 0) return; const A = wp(a), B = wp(b); o += SV.line(A[0], A[1], B[0], B[1], k === "c" ? "c2" : "c3", { "stroke-width": 3.5, ...(k === "c" ? { "stroke-dasharray": "7 5" } : {}), ...op(v) }); });
  OBJ.forEach((n, i) => { const p = wp(i), side = i === 0 ? "t" : i === 3 ? "b" : i < 3 ? "r" : "l"; o += SV.circle(p[0], p[1], 20, "nd"); const tx = side === "r" ? p[0] + 30 : side === "l" ? p[0] - 30 : p[0], ty = side === "t" ? p[1] - 30 : side === "b" ? p[1] + 40 : p[1] + 5, an = side === "r" ? "start" : side === "l" ? "end" : "middle"; o += SV.text(tx, ty, n, "lbl bd", { "text-anchor": an }); });
  return o + tag(40, 24, "red dashed = conflict   green = reinforce", "t1");
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Six macroeconomic objectives joined by lines showing conflicts and links">${webDraw({ n: 4 })}</svg>`;
Lib.stepper($("#stW"), { w: 760, h: 330, label: "Six macroeconomic objectives with red dashed lines for conflicts and green lines for reinforcing links", base: { n: 0 }, draw: webDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Six objectives</b>: inflation, unemployment, growth, the current account, sustainability and equity. No links yet.", s: { n: 0 } },
  { cap: "<b>Inflation and unemployment.</b> In the short run lowering unemployment tends to raise inflation (the Phillips curve). A <b>conflict</b>.", s: { n: 1 } },
  { cap: "<b>Growth and inflation, and growth and the current account.</b> Demand-led growth near capacity raises prices, and higher incomes raise imports. Two more <b>conflicts</b>.", s: { n: 2 } },
  { cap: "<b>Growth and sustainability, growth and equity, the current account and inflation.</b> Faster growth uses resources and may be uneven; a weak currency helps the current account but raises inflation.", s: { n: 3 } },
  { cap: "<b>Reinforcing links.</b> Growth can reduce unemployment, and supply-side growth can <b>reduce</b> inflation by raising capacity. Policy works best when it uses these links.", s: { n: 4 } },
] });

/* ---------- Time lags ---------- */
const TX = (t) => 70 + t * 66, TY = (v) => 170 - v * 70;
const cyc = (t) => Math.sin(2 * Math.PI * t / 6), pol = (t, lag, k) => (t < lag ? 0 : -k * Math.sin(2 * Math.PI * (t - lag) / 6));
function lagDraw(s) {
  let o = SV.line(70, 170, 730, 170) + SV.line(70, 40, 70, 300) + SV.text(730, 190, "Time (years)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Output relative to trend", "sm");
  const line = (fn, cls) => { const pts = []; for (let t = 0; t <= 10; t += 0.1) pts.push([TX(t), TY(fn(t))]); return SV.path(Lib.ptsPath(pts), cls); };
  o += line(cyc, "c1 dash") + tag(TX(1.5), TY(1) - 10, "no policy", "t1", 1, "middle");
  if (s.k > 0) o += line((t) => cyc(t) + pol(t, s.lag, s.k), "c2") + tag(TX(4.5), TY(cyc(4.5) + pol(4.5, s.lag, s.k)) + 26, "with policy", "t2", 1, "middle");
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 320, label: "Business cycle with no policy, well-timed counter-cyclical policy, and policy delayed by time lags that amplifies the cycle", base: { k: 0, lag: 0 }, draw: lagDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The cycle.</b> Output swings around trend (dashed). A government wants to reduce the swings.", s: {} },
  { cap: "<b>Well-timed policy.</b> If the government raises demand just as output falls and cuts it as output rises, the combined line is much flatter: <b>stabilisation</b>.", s: { k: 0.8, lag: 0 } },
  { cap: "<b>Policy with a lag.</b> If it takes about half a cycle to recognise the problem, decide and for the effect to arrive, the stimulus lands when the economy is already recovering. It adds to the boom and the later bust.", s: { k: 0.8, lag: 3 } },
  { cap: "<b>Government failure.</b> With a long lag the policy makes the cycle <b>larger</b>, not smaller. Automatic stabilisers have almost no lag, which is why they help avoid this problem.", s: { k: 0.8, lag: 3 } },
] });

/* ---------- Lab 1: policy mix ---------- */
function labMix() {
  if (!$("#mi") || !$("#mg") || !$("#me")) return;
  const i = +$("#mi").value / 10, g = +$("#mg").value / 10, e = +$("#me").value / 10;
  const coef = { inf: [-0.4, 0.3, 0.08], unemp: [0.3, -0.4, -0.03], gr: [-0.5, 0.8, 0.05], ca: [-0.3, -0.3, 0.08] };
  const eff = (k) => coef[k][0] * i + coef[k][1] * g + coef[k][2] * e;
  const rows = [["Inflation", eff("inf"), -1], ["Unemployment", eff("unemp"), -1], ["Growth", eff("gr"), 1], ["Current account", eff("ca"), 1]];
  const good = rows.filter((r) => r[1] * r[2] > 0.05), bad = rows.filter((r) => r[1] * r[2] < -0.05);
  $("#r1").textContent = good.length; $("#r2").textContent = bad.length; $("#r3").textContent = good.length && bad.length ? "Yes" : good.length ? "No" : bad.length ? "All worse" : "None";
  $("#rv").textContent = !good.length && !bad.length ? "No policy change: nothing moves." : good.length && bad.length ? `Better: ${good.map((r) => r[0].toLowerCase()).join(", ")}. Worse: ${bad.map((r) => r[0].toLowerCase()).join(", ")}. The same package improves some objectives and damages others: a conflict.` : good.length ? `Only improvements: ${good.map((r) => r[0].toLowerCase()).join(", ")}. Check whether this package is realistic in the short run.` : `All affected objectives are worse: ${bad.map((r) => r[0].toLowerCase()).join(", ")}.`;
  const mx = 1.2; let o = SV.line(40, 150, 400, 150) + tag(40, 24, "Change in each indicator (illustrative, per unit)", "t1");
  rows.forEach((r, k) => { const x = 60 + k * 85, h = Math.min(100, Math.abs(r[1]) / mx * 100), y = r[1] >= 0 ? 150 - h : 150, better = r[1] * r[2] > 0.05, worse = r[1] * r[2] < -0.05; o += SV.rect(x, y, 60, Math.max(h, 2), better ? "f3" : worse ? "f2" : "f1") + tag(x + 30, r[1] >= 0 ? y - 6 : y + h + 16, (r[1] >= 0 ? "+" : "") + Lib.fmtN(r[1], 2), better ? "t3" : worse ? "t2" : "t1", 1, "middle") + SV.text(x + 30, 290, r[0], "sm bd", { "text-anchor": "middle" }) + SV.text(x + 30, 270, better ? "better" : worse ? "worse" : "", "sm", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "mi", label: "Change in interest rate (points) ", min: -20, max: 40, step: 5, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labMix });
Lib.slider($("#g2"), { id: "mg", label: "Change in government spending (% of GDP) ", min: -20, max: 40, step: 5, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labMix });
Lib.slider($("#g3"), { id: "me", label: "Change in the exchange rate (% depreciation) ", min: -100, max: 100, step: 10, value: 0, fmt: (v) => Lib.fmtN(v / 10, 0), onInput: labMix });
labMix();
btnTable("lbBtns", "lbOut", [
  ["A stimulus arrives after the recovery has begun", "Time lag", "The policy takes effect after the problem has changed", "Rely more on automatic stabilisers, act early, monitor forecasts"],
  ["A government overestimates spare capacity", "Poor information", "Stimulus is too large and inflation rises", "Use a range of indicators, publish forecasts, review the estimates"],
  ["Tax cuts and public spending timed before an election", "Political motives", "Policy serves the election cycle, not the economy", "Independent central bank, fiscal rules"],
  ["High government borrowing pushes up interest rates", "Crowding out", "Private investment falls, offsetting the stimulus", "Finance deficits in recessions when private demand for funds is low"],
  ["Workers expect inflation and demand higher pay", "Expectations", "Demand policy only has temporary effects", "Credible inflation target, supply-side policy"],
  ["Privatisation creates a private monopoly", "Unintended consequence", "Efficiency gains are lost to higher prices", "Regulation, promote competition"]
], ["Scenario", "Type of failure", "Why it fails", "How to reduce it"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the pair of objectives usually conflict or reinforce each other?", buckets: [{"label": "Usually conflict (short run)"}, {"label": "Can reinforce each other"}], items: [{"text": "Low unemployment and low inflation", "b": 0}, {"text": "Fast growth and a balanced current account", "b": 0}, {"text": "Growth from supply-side improvement and low inflation", "b": 1}, {"text": "Growth and sustainability if growth uses fossil fuels", "b": 0}, {"text": "Growth and falling unemployment", "b": 1}, {"text": "Lower inflation and a stronger currency", "b": 1}, {"text": "Fast growth and a more equal income distribution when gains go to owners of capital", "b": 0}, {"text": "Fixed exchange rate and independent interest rate policy", "b": 0}], done: "Many pairs conflict in the short run but can be reconciled by supply-side policy." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Government failure", "Intervention fails to meet its aim or makes things worse"], ["Time lag", "Delay between a problem, a policy and its effect"], ["Political business cycle", "Policy timed to win elections rather than to suit the economy"], ["Crowding out", "Public borrowing reduces private investment"], ["Policy mix", "The combination of fiscal, monetary and other policies used together"], ["Automatic stabiliser", "A tax or benefit that moves with the cycle without delay"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the political business cycle in order.", items: ["An election is approaching", "The government cuts taxes and raises spending", "Output and employment rise and the government is popular", "After the election inflation and debt rise and the government tightens policy", "A slowdown follows"], done: "Policy timed for votes can create a cycle." });
Lib.calc($("#c1"), { qs: [
  {"q": "A government raises spending by 2% of GDP and the multiplier is 1.5. Calculate the rise in output as a % of GDP.", "a": 3, "unit": "%", "tol": 0.05, "hint": "2 × 1.5.", "sol": "2 × 1.5 = <b>3%</b>."},
  {"q": "The true output gap is −2% but the government estimates it at −5% and sets a stimulus to close it using a multiplier of 1.5. By what % of GDP does it overshoot if it fully closes the estimated gap (output rise = 5%)?", "a": 3, "unit": "%", "tol": 0.05, "hint": "Output rise minus true gap.", "sol": "Output rises 5% against a true gap of 2%, so output ends <b>3%</b> above potential, which is inflationary."},
  {"q": "Inflation falls by 3 points when interest rates rise 2 points, and unemployment rises by 1.5 points. Calculate the rise in unemployment per point of fall in inflation.", "a": 0.5, "tol": 0.01, "hint": "1.5 ÷ 3.", "sol": "1.5 ÷ 3 = <b>0.5 points</b> of unemployment per point of inflation."},
  {"q": "A government borrows an extra $40bn. Because of higher interest rates, private investment falls by $12bn. Calculate the crowding out as a percentage of the extra borrowing.", "a": 30, "unit": "%", "tol": 0.05, "hint": "12 ÷ 40.", "sol": "12 ÷ 40 × 100 = <b>30%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a likely conflict when a government raises interest rates to cut inflation?", opts: ["Lower growth and higher unemployment", "Higher growth", "A weaker currency", "Lower savings"], a: 0, why: "Higher rates reduce spending and investment." },
  { q: "Why may a stimulus package fail to stabilise the economy?", opts: ["Time lags mean it may take effect after the recovery has begun", "Fiscal policy has no effect on AD", "The multiplier is always zero", "The exchange rate is always fixed"], a: 0, why: "Lags can turn a counter-cyclical policy into a pro-cyclical one." },
  { q: "Which is an example of a political business cycle?", opts: ["Tax cuts before an election followed by tighter policy after it", "A central bank setting rates by a rule", "An automatic stabiliser", "A currency intervention"], a: 0, why: "Policy timed for votes rather than economic needs." },
  { q: "Which reduces the risk of government failure caused by lags?", opts: ["Automatic stabilisers", "Larger deficits", "Higher tariffs", "Fewer forecasts"], a: 0, why: "Automatic stabilisers respond immediately without any decision." },
  { q: "Which policy pair is most likely to offset each other?", opts: ["A tax cut and a rise in interest rates", "A tax cut and a rise in government spending", "A rise in interest rates and a cut in government spending", "Quantitative easing and a rate cut"], a: 0, why: "One policy raises AD and the other reduces it." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Policy conflict", "A policy that helps one objective but harms another."],
  ["Trade-off", "Having to give up some of one objective to gain more of another."],
  ["Government failure", "Intervention that fails or makes things worse."],
  ["Time lag", "Delay before a policy takes effect."],
  ["Political business cycle", "Policy timed to elections."],
  ["Crowding out", "Government borrowing displaces private spending."],
  ["Time inconsistency", "Government announces a policy and then has an incentive to change it."],
  ["Automatic stabiliser", "Moves with the cycle without a decision."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which policy is most likely to conflict with a government's aim of price stability in the short run? (Oct/Nov 2021 · 32 · Q29, reworded)", opts: ["More spending on education and health", "Raising the basic rate of income tax", "Limiting public sector wage rises", "Preventing mergers of large firms"], a: 0, why: "More spending raises aggregate demand and, if the economy is near capacity, prices." },
  { q: "The government raises interest rates to reduce inflation. What else is likely to result? (Feb/March 2024 · 32 · Q23, reworded)", opts: ["A depreciation of the currency", "A fall in savings", "A reduction in economic growth", "A reduction in unemployment"], a: 2, why: "Higher interest rates reduce consumption and investment, so growth slows." },
  { q: "Which policy combination will reduce national income by the greatest amount? (Feb/March 2021 · 32 · Q23, reworded)", opts: ["Cut direct taxes and raise interest rates", "Cut direct taxes and increase quantitative easing", "Raise direct taxes and raise interest rates", "Raise direct taxes and increase quantitative easing"], a: 2, why: "Both policies are contractionary and reinforce each other." },
  { q: "Which statement would both Keynesian and monetarist economists accept? (May/June 2021 · 31 · Q28, reworded)", opts: ["High inflation and high unemployment are undesirable in a properly functioning economy", "Higher government spending on investment always crowds out private investment", "The best way out of recession is higher government spending", "The most effective way to cut inflation is tight control of the money supply"], a: 0, why: "Both schools agree these are problems. They disagree about causes and cures." },
  { q: "Which combination of policies will most likely succeed in reducing both unemployment and inflation? (Oct/Nov 2020 · 32 · Q30, reworded)", opts: ["Contractionary supply-side policies and higher interest rates", "Expansionary supply-side policies and lower indirect taxes", "Higher direct taxes and lower indirect taxes", "Lower interest rates and a depreciation of the exchange rate"], a: 1, why: "Supply-side policy shifts LRAS right, and lower indirect taxes cut prices directly: both aims can improve." },
  { q: "Which condition attached to an IMF loan to a low-income country conflicts with the infant industry argument? (May/June 2025 · 32 · Q29, reworded)", opts: ["The need to allow free trade", "The need to control inflation", "The need for contractionary fiscal policy", "The need to privatise state firms"], a: 0, why: "The infant industry argument supports temporary protection, which free trade rules out." },
  { q: "Which combination of policies is most likely to increase output? (May/June 2023 · 31 · Q23, reworded)", opts: ["Smaller budget deficit and lower interest rates", "Smaller budget deficit and higher interest rates", "Larger budget deficit and lower interest rates", "Larger budget deficit and higher interest rates"], a: 2, why: "Expansionary fiscal and monetary policy both raise aggregate demand." },
  { q: "What is a reflationary fiscal measure? (Feb/March 2021 · 32 · Q30, reworded)", opts: ["Increasing government spending", "Increasing taxes", "Increasing the money supply", "Reducing interest rates"], a: 0, why: "Reflationary fiscal policy raises AD through higher spending or lower taxes. The money supply and interest rates are monetary measures." },
] });
