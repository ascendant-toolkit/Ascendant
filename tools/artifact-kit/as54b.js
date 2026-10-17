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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

function mcDraw(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: false }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A higher interest rate shifts AD to the left, lowering the price level and output">${mcDraw({ a: -20, n: 1 })}</svg>`;
$("#pic2").innerHTML = (() => {
  const B = [["Quick to change", "Often independent of politics", 30, "f2"], ["Time lags", "12 to 18 months", 270, "f3"], ["Weak when", "Low confidence, near zero rates, cost-push", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="Strengths and limits of monetary policy">${o}</svg>`;
})();
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary monetary policy to reduce inflation", base: { a: 0, n: 0 }, draw: mcDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Inflation is above target and AD is strong.", s: { a: 0, n: 0 } },
  { cap: "<b>The central bank raises interest rates.</b> Borrowing is dearer, saving is more attractive and the currency may rise. Consumption, investment and net exports fall: AD shifts <b>left</b>. The price level falls (inflation eases) but so does output.", s: { a: -20, n: 1 } },
  { cap: "<b>The trade-off.</b> Lower inflation comes with slower growth and possibly higher unemployment in the short run, and the effect appears only after a time lag.", s: { a: -20, n: 1 } },
] });
const flatDraw = (s) => adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: true });
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Expansionary monetary policy and capacity", base: { a: 0, n: 0 }, draw: flatDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Equilibrium is below potential output (the dashed LRAS line): there is spare capacity.", s: { a: 0, n: 0 } },
  { cap: "<b>Rates are cut.</b> AD shifts <b>right</b>: real output and employment rise, with a rise in the price level.", s: { a: 20, n: 1 } },
  { cap: "<b>Near full capacity</b> the same shift would raise prices by more and output by less. That is why spare capacity matters for evaluation.", s: { a: 20, n: 1 } },
] });
chainStep("#stF", "Why expansionary policy may fail in a deflation", ["The central bank cuts rates close to zero", "Households expect prices to fall further, so they delay spending", "Firms are pessimistic and do not invest; banks lend cautiously", "Borrowing and spending barely rise", "AD stays weak; fiscal policy or QE may be needed"], [
  "<b>The usual tool is nearly exhausted.</b>", "<b>Expectations</b> work against the policy.", "<b>Low confidence</b> reduces the response to cheaper credit.", "<b>The AD shift is small.</b>", "<b>Other tools</b> (government spending, QE) may be needed."]);

function labM() {
  if (!["ch", "rs"].every((i) => $("#" + i))) return;
  const c = +$("#ch").value, r = +$("#rs").value / 100, a = Math.max(-30, Math.min(30, -c * 8 * r)), e = sdEq(a, 0), e0 = sdEq(0, 0);
  $("#r1").textContent = Math.abs(a) < 0.5 ? "No shift" : a > 0 ? "Shifts right" : "Shifts left"; $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = Lib.fmtN(e.p, 1);
  $("#rv").textContent = Math.abs(a) < 0.5 ? "Either the base rate is unchanged or spending does not respond to it, so AD does not shift." : `A ${c < 0 ? "cut" : "rise"} of ${Math.abs(c)} percentage points, with spending ${Lib.fmtN(r * 100, 0)}% responsive to interest rates, shifts AD ${a > 0 ? "right (expansionary)" : "left (contractionary)"}. Real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. ${r < 0.4 ? "Households and firms respond weakly, so the policy has a small effect: a limit of monetary policy." : ""}`;
  $("#labA").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 }, { lras: false });
}
Lib.slider($("#g1"), { id: "ch", label: "Change in the base rate, percentage points ", min: -3, max: 3, step: 0.5, value: 2, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g2"), { id: "rs", label: "How responsive spending is to interest rates, % ", min: 10, max: 100, step: 10, value: 70, fmt: (v) => v + "%", onInput: labM });
labM();

chooser("h", [
  ["Demand-pull inflation", "Raise interest rates (contractionary)", "AD falls, so prices stabilise", "Time lags; lower growth and jobs", 5],
  ["Cost-push inflation", "Raise interest rates", "Output falls but costs remain high", "Does not address the source of the rise in costs", 2],
  ["Recession with spare capacity", "Cut rates and loosen credit", "AD rises, output and jobs recover", "Low confidence may limit the response", 3],
  ["Deflation", "Cut rates, QE", "AD rises and prices stop falling", "Rates near zero; expectations of falling prices", 2],
  ["Housing bubble", "Tighter credit regulation", "Slower lending and house price rises", "May hit first-time buyers; avoidance", 4],
  ["Overheating economy near full capacity", "Raise rates", "Slows AD growth to reduce inflation risk", "May slow the economy too much", 4]
], (it) => `${it[0]}: the monetary response is to ${it[1].toLowerCase()}. Likely effect: ${it[2].toLowerCase()}. Main limit: ${it[3].toLowerCase()}.`, "How effective monetary policy is likely to be");
Lib.classify($("#cl1"), { prompt: "Effect of a rise or a cut in interest rates?", buckets: [{"label": "Effect of a rise"}, {"label": "Effect of a cut"}], items: [{"text": "Borrowing becomes dearer", "b": 0}, {"text": "Saving becomes less attractive", "b": 1}, {"text": "Consumption and investment fall", "b": 0}, {"text": "The currency may weaken", "b": 1}, {"text": "AD shifts left", "b": 0}, {"text": "AD shifts right", "b": 1}, {"text": "Mortgage payments fall for borrowers", "b": 1}, {"text": "Savers earn more", "b": 0}], done: "A rise makes credit dearer and saving more attractive; a cut does the reverse." });
Lib.classify($("#cl2"), { prompt: "Is it a strength or a limit of monetary policy?", buckets: [{"label": "Strength"}, {"label": "Limit"}], items: [{"text": "Interest rates can be changed quickly", "b": 0}, {"text": "It can take 12 to 18 months to work fully", "b": 1}, {"text": "Central banks are often independent of politics", "b": 0}, {"text": "Pessimistic households may not borrow even at low rates", "b": 1}, {"text": "Rates are close to zero and cannot fall further", "b": 1}, {"text": "It can be adjusted in small steps", "b": 0}, {"text": "It is less effective against cost-push inflation", "b": 1}, {"text": "People may expect inflation and spend sooner", "b": 1}], done: "Strengths: speed and flexibility. Limits: lags, confidence, expectations, zero bound, cost-push." });
Lib.order($("#o1"), { prompt: "Put the effect of a cut in interest rates in order.", items: ["The central bank cuts the base rate", "Borrowing becomes cheaper and saving less attractive", "Consumption and investment rise", "AD shifts to the right", "Real output rises and the price level may rise"], done: "Lower rates raise spending and AD." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Expansionary policy", "Lower rates or looser credit that raise AD"], ["Contractionary policy", "Higher rates or tighter credit that reduce AD"], ["Time lag", "Delay before a policy takes full effect"], ["Zero lower bound", "Interest rates cannot usually fall far below zero"], ["Demand-pull inflation", "Inflation caused by AD growing faster than AS"], ["Cost-push inflation", "Inflation caused by rising costs of production"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "AD is 50 and spending is 70% responsive. A 2 point rate rise shifts AD left by 8 × 2 × 0.7 units. By how many units?", "a": 11.2, "unit": "", "tol": 0.1, "hint": "8 × 2 × 0.7.", "sol": "<b>11.2</b> units."},
  {"q": "A household with a $150,000 variable mortgage sees the rate rise from 4% to 6%. By how much do yearly interest payments rise ($)?", "a": 3000, "unit": "$", "tol": 1, "hint": "0.02 × 150,000.", "sol": "<b>$3,000</b> a year."},
  {"q": "That is how much more per month ($)?", "a": 250, "unit": "$", "tol": 1, "hint": "3,000 ÷ 12.", "sol": "<b>$250</b>."},
  {"q": "Inflation is 7% and the central bank's target is 2%. By how many percentage points is it above target?", "a": 5, "unit": "points", "tol": 0.1, "hint": "7 − 2.", "sol": "<b>5 points</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in interest rates will usually:", opts: ["Shift AD left", "Shift AD right", "Shift LRAS right", "Raise investment"], a: 0, why: "Borrowing dearer." },
  { q: "Which inflation is monetary policy least suited to?", opts: ["Cost-push", "Demand-pull", "Both equally", "Neither"], a: 0, why: "Higher rates do not cut costs." },
  { q: "A limit of monetary policy is:", opts: ["Time lags", "Instant effect", "No effect on AD", "It lowers the deficit"], a: 0, why: "Delays." },
  { q: "Expansionary policy is most effective when:", opts: ["There is spare capacity", "The economy is at full capacity", "Rates are negative", "Confidence is falling"], a: 0, why: "Output can rise without much inflation." },
  { q: "A higher interest rate may cause the currency to:", opts: ["Appreciate", "Depreciate", "Be fixed", "Disappear"], a: 0, why: "Attracts funds from abroad." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Expansionary", "AD right."],
  ["Contractionary", "AD left."],
  ["Time lags", "12 to 18 months."],
  ["Demand-pull", "Monetary policy works best."],
  ["Cost-push", "Monetary policy is weak."],
  ["Zero bound", "Rates cannot fall far below zero."],
  ["Exchange rate", "Can reinforce or offset."],
  ["Compare", "Fiscal and supply-side policy."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "To counter deflation a central bank uses expansionary monetary policy. What is likely to result? (May/June 2024 · 11 · Q20, reworded)", opts: ["a higher cost of borrowing", "an increase in aggregate demand", "an appreciation of the exchange rate", "an increase in government debt"], a: 1, why: "Lower interest rates and more credit raise AD." },
  { q: "Why will a contractionary monetary policy reduce inflation? (May/June 2022 · 11 · Q29, reworded)", opts: ["Banks will lend more", "Consumers will have higher disposable income", "Consumers will pay more tax", "Consumers will save more"], a: 3, why: "Higher interest rates encourage saving and reduce spending, lowering AD." },
  { q: "The diagram shows the current equilibrium of an economy. The government introduces a contractionary monetary policy. What is the most likely outcome? (May/June 2023 · 12 · Q27, reworded)", opts: ["a fall in investment and a fall in inflation", "a fall in investment and a rise in inflation", "a rise in investment and a fall in inflation", "a rise in investment and a rise in inflation"], a: 0, why: "Higher interest rates raise the cost of borrowing, so investment falls, AD shifts left and inflationary pressure falls." },
  { q: "A government has a target to reduce the rate of inflation. Why might it not want to raise interest rates to achieve this target? (May/June 2025 · 13 · Q25, reworded)", opts: ["aggregate demand may fall", "aggregate supply may fall", "saving may fall", "the exchange rate may fall"], a: 1, why: "Higher rates raise firms' borrowing costs and can reduce investment, which may reduce capacity, shifting SRAS left." },
  { q: "What would make a policy of raising interest rates less likely to be effective in reducing inflation? (Oct/Nov 2021 · 12 · Q29, reworded)", opts: ["Aggregate supply is increasing faster than aggregate demand", "Consumers expect prices to rise even faster in the future", "Consumers' spending is largely paid for on credit", "Interest rates are still higher abroad"], a: 1, why: "If consumers expect faster price rises, they bring forward spending, offsetting the effect of higher rates." },
  { q: "Why are higher interest rates together with increased taxation on expenditure likely to cause domestic deflation? (May/June 2021 · 12 · Q28, reworded)", opts: ["because the contractionary monetary policy will over-ride the expansionary fiscal policy", "because the monetary and fiscal policies involved will reinforce each other", "because the expansionary monetary policy will over-ride the contractionary fiscal policy", "because the monetary and fiscal policies involved will cancel each other out"], a: 1, why: "Both are contractionary, so they reinforce each other, strongly reducing AD." },
  { q: "Which type of policy would have the most immediate effect in dealing with a deflationary economic downturn? (May/June 2021 · 13 · Q27, reworded)", opts: ["increasing the government's budget surplus", "increasing borrowing by assisting banks to lend more", "investing in long-term projects to improve transport networks", "switching the burden of taxation from earning to spending"], a: 1, why: "Helping banks to lend more raises credit and spending quickly. Long-term projects take years." },
  { q: "Japan is suffering from deflation. Which government policy would not help to overcome this problem? (May/June 2021 · 11 · Q28, reworded)", opts: ["encouraging domestic savings rather than consumption", "increasing incentives for business start-ups by lowering profits tax", "lowering interest rates and increasing the money supply", "promoting more innovation in technical industries"], a: 0, why: "Encouraging saving instead of spending would reduce AD further, worsening deflation." },
  { q: "Which combination of fiscal and monetary policies is most likely to be effective in the short run for tackling deflation in a closed economy? (fiscal policy, monetary policy) (May/June 2020 · 13 · Q29, reworded)", opts: ["decreasing the budget deficit, decreasing the interest rate", "decreasing the budget deficit, decreasing the money supply", "increasing the budget deficit, decreasing the interest rate", "increasing the budget deficit, decreasing the money supply"], a: 2, why: "A larger budget deficit (expansionary fiscal) and lower interest rates (expansionary monetary) both raise AD." },
] });
