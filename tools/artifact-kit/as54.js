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

/* ---------- transmission chain ---------- */
function trDraw(s) {
  const bx = (x, y, w, t, k, v) => SV.rect(x, y, w, 46, k, { rx: 8, ...op(0.55 * v) }) + SV.text(x + w / 2, y + 28, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
  const ar = (x1, y1, x2, y2, d, v) => SV.line(x1, y1, x2, y2, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y2, d, "dot4");
  let o = bx(20, 20, 180, "Central bank cuts the base rate", "f3", s.a) + ar(202, 43, 250, 43, "r", s.b) + bx(252, 20, 220, "Borrowing cheaper, saving less attractive", "f1", s.b) + ar(474, 43, 522, 43, "r", s.c) + bx(524, 20, 220, "Consumption and investment rise", "f2", s.c);
  o += ar(634, 68, 634, 118, "d", s.d) + bx(480, 122, 264, "AD shifts right; currency may weaken", "f1", s.d) + ar(478, 145, 430, 145, "l", s.e) + bx(140, 122, 288, "Output and employment rise; prices may rise", "f3", s.e);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 190" role="img" aria-label="A cut in the base rate lowers borrowing costs, raises consumption and investment, and shifts AD right">${trDraw({ a: 1, b: 1, c: 1, d: 1, e: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 190, label: "The transmission of an interest rate cut", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: trDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>The central bank cuts its base rate.</b> This is expansionary monetary policy.", s: { a: 1 } },
  { cap: "<b>Borrowing becomes cheaper</b> (loans, mortgages) and saving less rewarding, so people have an incentive to spend.", s: { a: 1, b: 1 } },
  { cap: "<b>Consumption and investment rise.</b> Households borrow to buy and firms to expand.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>AD shifts right.</b> Lower interest rates may also weaken the currency, raising net exports.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>Output and employment rise,</b> and prices may rise if there is little spare capacity.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

function mcDraw(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: false }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A higher interest rate shifts AD to the left, lowering the price level and output">${mcDraw({ a: -20, n: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary monetary policy to reduce inflation", base: { a: 0, n: 0 }, draw: mcDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Inflation is above target and AD is strong.", s: { a: 0, n: 0 } },
  { cap: "<b>The central bank raises interest rates.</b> Borrowing is dearer, saving is more attractive and the currency may rise. Consumption, investment and net exports fall: AD shifts <b>left</b>. The price level falls (inflation eases) but so does output.", s: { a: -20, n: 1 } },
  { cap: "<b>The trade-off.</b> Lower inflation comes with slower growth and possibly higher unemployment in the short run, and the effect appears only after a time lag.", s: { a: -20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
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

/* ---------- Lab 2 ---------- */
function labI() {
  if (!["nm", "fl"].every((i) => $("#" + i))) return;
  const n = +$("#nm").value, f = +$("#fl").value, r = n - f;
  $("#t1").textContent = (r >= 0 ? "+" : "") + Lib.fmtN(r, 1) + "%"; $("#t2").textContent = r < 0 ? "Very attractive" : r < 2 ? "Moderate" : "Discouraged"; $("#t3").textContent = r < 0 ? "Savers lose" : r < 2 ? "Modest reward" : "Rewarded";
  $("#tv").textContent = `A nominal rate of ${n}% with inflation of ${f}% gives a real rate of ${Lib.fmtN(r, 1)}%. ${r < 0 ? "Borrowing costs less than inflation: the real value of debt falls, so borrowing is attractive and savers lose in real terms." : r < 2 ? "A low real rate keeps borrowing fairly cheap." : "A high real rate makes borrowing costly and saving rewarding, which reduces spending."}`;
  const Y = (v) => 120 - v * 8; let o = SV.line(40, 120, 400, 120) + SV.line(40, 20, 40, 190);
  [["Nominal rate", n, "f1"], ["Inflation", f, "f3"], ["Real rate", r, r >= 0 ? "f2" : "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, v >= 0 ? Y(v) : 120, 80, Math.abs(Y(v) - 120), c, op(0.65)) + SV.text(110 + i * 110, 185, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, v >= 0 ? Y(v) - 6 : 120 + Math.abs(Y(v) - 120) + 14, Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "nm", label: "Nominal interest rate, % ", min: 0, max: 12, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g4"), { id: "fl", label: "Inflation rate, % ", min: 0, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%", onInput: labI });
labI();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Expansionary or contractionary monetary policy?", buckets: [{"label": "Expansionary"}, {"label": "Contractionary"}], items: [{"text": "A cut in the base rate", "b": 0}, {"text": "A rise in the base rate", "b": 1}, {"text": "Quantitative easing", "b": 0}, {"text": "Reducing the money supply", "b": 1}, {"text": "Looser rules on mortgage lending", "b": 0}, {"text": "Tighter credit regulation for banks", "b": 1}, {"text": "Lowering interest rates to end deflation", "b": 0}, {"text": "Raising rates to reduce inflation", "b": 1}], done: "Expansionary: cheaper, easier credit. Contractionary: dearer, tighter credit." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Monetary policy", "Use of interest rates, money supply and credit regulation"], ["Base rate", "The central bank's policy interest rate"], ["Quantitative easing", "Creating money to buy bonds and raise the money supply"], ["Credit regulation", "Rules on how banks lend"], ["Real interest rate", "Nominal rate minus inflation"], ["Time lag", "Delay before a policy takes full effect"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a rise in interest rates in order.", items: ["The central bank raises the base rate", "Borrowing becomes dearer and saving more attractive", "Consumption and investment fall", "AD shifts to the left", "The price level and inflation fall"], done: "Higher rates reduce spending and AD, lowering inflation." });
Lib.calc($("#c1"), { qs: [
  {"q": "The nominal interest rate is 5% and inflation 3%. What is the real interest rate (%)?", "a": 2, "unit": "%", "tol": 0.1, "hint": "5 − 3.", "sol": "<b>2%</b>."},
  {"q": "A firm borrows $200,000 at 6%. What is the yearly interest ($)?", "a": 12000, "unit": "$", "tol": 1, "hint": "0.06 × 200,000.", "sol": "<b>$12,000</b>."},
  {"q": "The rate rises to 8%. What is the new yearly interest ($)?", "a": 16000, "unit": "$", "tol": 1, "hint": "0.08 × 200,000.", "sol": "<b>$16,000</b>."},
  {"q": "By what % has the cost of borrowing risen?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4,000 ÷ 12,000.", "sol": "<b>33.3%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Monetary policy uses:", opts: ["Interest rates, money supply and credit regulation", "Taxes and spending", "Training schemes", "Tariffs"], a: 0, why: "Not fiscal." },
  { q: "A rise in interest rates will usually:", opts: ["Shift AD left", "Shift AD right", "Shift LRAS right", "Raise investment"], a: 0, why: "Borrowing dearer." },
  { q: "Quantitative easing is:", opts: ["Expansionary", "Contractionary", "A tax", "A subsidy"], a: 0, why: "Raises the money supply." },
  { q: "A limit of monetary policy is:", opts: ["Time lags", "Instant effect", "No effect on AD", "It lowers the deficit"], a: 0, why: "Delays." },
  { q: "Which inflation is monetary policy least suited to?", opts: ["Cost-push", "Demand-pull", "Both equally", "Neither"], a: 0, why: "Higher rates do not cut costs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Tools", "Rates, money supply, credit rules."],
  ["Expansionary", "AD right."],
  ["Contractionary", "AD left."],
  ["QE", "Creates money for bonds."],
  ["Credit rules", "Looser = expansionary."],
  ["Real rate", "Nominal − inflation."],
  ["Lags", "12 to 18 months."],
  ["Limits", "Confidence, zero bound."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A country's central bank decides to reduce the level of credit regulation. What is this an example of? (Feb/March 2025 · 12 · Q23, reworded)", opts: ["contractionary fiscal policy", "contractionary monetary policy", "expansionary fiscal policy", "expansionary monetary policy"], a: 3, why: "Looser credit rules make borrowing easier, which is expansionary monetary policy." },
  { q: "To counter deflation a central bank uses expansionary monetary policy. What is likely to result? (May/June 2024 · 11 · Q20, reworded)", opts: ["a higher cost of borrowing", "an increase in aggregate demand", "an appreciation of the exchange rate", "an increase in government debt"], a: 1, why: "Lower interest rates and more credit raise AD." },
  { q: "Why will a contractionary monetary policy reduce inflation? (May/June 2022 · 11 · Q29, reworded)", opts: ["Banks will lend more", "Consumers will have higher disposable income", "Consumers will pay more tax", "Consumers will save more"], a: 3, why: "Higher interest rates encourage saving and reduce spending, lowering AD." },
  { q: "The diagram shows the current equilibrium of an economy. The government introduces a contractionary monetary policy. What is the most likely outcome? (May/June 2023 · 12 · Q27, reworded)", opts: ["a fall in investment and a fall in inflation", "a fall in investment and a rise in inflation", "a rise in investment and a fall in inflation", "a rise in investment and a rise in inflation"], a: 0, why: "Higher interest rates raise the cost of borrowing, so investment falls, AD shifts left and inflationary pressure falls." },
  { q: "A government has a target to reduce the rate of inflation. Why might it not want to raise interest rates to achieve this target? (May/June 2025 · 13 · Q25, reworded)", opts: ["aggregate demand may fall", "aggregate supply may fall", "saving may fall", "the exchange rate may fall"], a: 1, why: "Higher rates raise firms' borrowing costs and can reduce investment, which may reduce capacity (aggregate supply), shifting SRAS left and worsening cost-push inflation." },
  { q: "What would make a policy of raising interest rates less likely to be effective in reducing inflation? (Oct/Nov 2021 · 12 · Q29, reworded)", opts: ["Aggregate supply is increasing faster than aggregate demand", "Consumers expect prices to rise even faster in the future", "Consumers' spending is largely paid for on credit", "Interest rates are still higher abroad"], a: 1, why: "If consumers expect faster price rises, they bring forward spending, offsetting the effect of higher rates." },
  { q: "Why are higher interest rates together with increased taxation on expenditure likely to cause domestic deflation? (May/June 2021 · 12 · Q28, reworded)", opts: ["because the contractionary monetary policy will over-ride the expansionary fiscal policy", "because the monetary and fiscal policies involved will reinforce each other", "because the expansionary monetary policy will over-ride the contractionary fiscal policy", "because the monetary and fiscal policies involved will cancel each other out"], a: 1, why: "Both are contractionary, so they reinforce each other, strongly reducing AD." },
  { q: "Which type of policy would have the most immediate effect in dealing with a deflationary economic downturn? (May/June 2021 · 13 · Q27, reworded)", opts: ["increasing the government's budget surplus", "increasing borrowing by assisting banks to lend more", "investing in long-term projects to improve transport networks", "switching the burden of taxation from earning to spending"], a: 1, why: "Helping banks to lend more raises credit and spending quickly. Long-term projects take years." },
] });
