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

$("#pic1").innerHTML = (() => {
  const B = [["Interest rates", "The base rate and the rates that follow it", 30, "f1"], ["Money supply", "Open market operations and QE", 270, "f2"], ["Credit regulation", "Rules on bank lending", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 55, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 82, d, "sm", { "text-anchor": "middle" }); });
  o += SV.text(380, 142, "All three change the cost and availability of credit, so spending and AD change", "sm", { "text-anchor": "middle" });
  return `<svg viewBox="0 0 760 160" role="img" aria-label="The three tools of monetary policy">${o}</svg>`;
})();
chainStep("#stT", "A cut in the base rate", ["The central bank cuts the base rate", "Commercial banks cut mortgage and loan rates; saving returns fall", "Borrowing is cheaper and saving less attractive", "Consumption and investment rise; asset prices rise", "The currency may fall, raising net exports; AD shifts right"], [
  "<b>Expansionary monetary policy</b> begins with the base rate.", "<b>Pass-through</b> to the rates households and firms face.", "<b>Incentives change:</b> spend and invest rather than save.", "<b>Components of AD rise</b> and wealth effects add to spending.", "<b>AD shifts right</b>, with net exports helped by a weaker currency."]);
chainStep("#stQ", "Quantitative easing", ["Interest rates are already close to zero", "The central bank creates money and buys government bonds", "Bond prices rise, so long-term interest rates fall", "Banks and investors have more money to lend and invest", "Spending and AD rise, if people borrow and spend"], [
  "<b>The usual tool is exhausted</b> at the zero bound.", "<b>Open market purchases</b> put money into the banking system.", "<b>Lower long-term rates</b> make borrowing cheaper.", "<b>More credit</b> is available.", "<b>The effect depends</b> on confidence and the willingness to borrow."]);
chainStep("#stC", "Tightening credit regulation", ["The central bank raises deposit and capital requirements", "Banks lend less and check borrowers more strictly", "Households find it harder to borrow, especially for housing", "Spending and house prices rise more slowly", "AD grows more slowly, reducing inflationary pressure"], [
  "<b>Contractionary credit regulation.</b>", "<b>Credit supply</b> falls.", "<b>Borrowing</b> becomes harder, even at the same interest rate.", "<b>House purchases</b> slow.", "<b>AD growth falls</b> without changing the base rate."]);

/* ---------- Lab 1 ---------- */
function labM() {
  if (!["rt", "mg", "sv"].every((i) => $("#" + i))) return;
  const r = +$("#rt").value / 10, mg = +$("#mg").value, sv = +$("#sv").value, mi = (mg * r) / 100 / 12, si = (sv * r) / 100 * 0.5, base = (mg * 4) / 100 / 12, bs = (sv * 4) / 100 * 0.5, net = (si - bs) / 12 - (mi - base);
  $("#r1").textContent = "$" + Lib.fmtN(mi, 0); $("#r2").textContent = "$" + Lib.fmtN(si, 0); $("#r3").textContent = (net >= 0 ? "+" : "−") + "$" + Lib.fmtN(Math.abs(net), 0);
  $("#rv").textContent = `At a rate of ${Lib.fmtN(r, 1)}% the monthly mortgage interest on $${Lib.fmtN(mg, 0)} is $${Lib.fmtN(mi, 0)}, compared with $${Lib.fmtN(base, 0)} at 4%. Savings earn about half the base rate here ($${Lib.fmtN(si, 0)} a year). The household's monthly budget is ${net >= 0 ? "better" : "worse"} by $${Lib.fmtN(Math.abs(net), 0)}. ${net < 0 ? "A rate rise reduces the spending power of borrowers, which is how it reduces AD." : net > 0 ? "A rate cut raises the spending power of borrowers." : ""}`;
  const mx = Math.max(mi, si / 12, 1), W = (v) => (v / mx) * 250, bar = (y, l, v, c) => SV.text(10, y + 15, l, "sm") + SV.rect(150, y, Math.max(2, W(v)), 24, c, op(0.7)) + SV.text(156 + W(v), y + 17, "$" + Lib.fmtN(v, 0), "lbl bd");
  $("#labA").innerHTML = bar(40, "Mortgage interest / month", mi, "f3") + bar(100, "Savings interest / month", si / 12, "f1");
}
Lib.slider($("#g1"), { id: "rt", label: "Base rate, % × 10 ", min: 10, max: 100, step: 5, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1) + "%", onInput: labM });
Lib.slider($("#g2"), { id: "mg", label: "Variable-rate mortgage, $ ", min: 50000, max: 400000, step: 25000, value: 200000, fmt: (v) => Lib.fmtN(v, 0), onInput: labM });
Lib.slider($("#g3"), { id: "sv", label: "Savings, $ ", min: 0, max: 100000, step: 5000, value: 20000, fmt: (v) => Lib.fmtN(v, 0), onInput: labM });
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
Lib.slider($("#g4"), { id: "nm", label: "Nominal interest rate, % ", min: 0, max: 12, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g5"), { id: "fl", label: "Inflation rate, % ", min: 0, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%", onInput: labI });
labI();

/* ---------- Lab 3 ---------- */
chooser("h", [
  ["Interest rates", "A change in the base rate alters borrowing costs and the return on saving", "Cut: expansionary", "Responses may be weak if confidence is low; time lags", 5],
  ["Quantitative easing", "The central bank buys bonds, raising the money supply and lowering long-term rates", "Expansionary", "Banks may not lend; may raise asset prices more than spending", 3],
  ["Open market sales of bonds", "The central bank sells bonds, taking money out of the banking system", "Contractionary", "Raises yields; effects on spending slow", 3],
  ["Credit regulation (looser)", "Easier lending rules let more people borrow", "Expansionary", "Risk of excess lending and asset bubbles", 4],
  ["Credit regulation (tighter)", "Stricter rules limit borrowing", "Contractionary", "May reduce lending to good borrowers", 4],
  ["Inflation target", "Anchors expectations of future inflation", "Neither (framework)", "Only works if the bank is credible and willing to act", 3]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. It is ${it[2].toLowerCase()}. Main drawback: ${it[3].toLowerCase()}.`, "Importance as a tool");
Lib.classify($("#cl1"), { prompt: "Which tool of monetary policy is it?", buckets: [{"label": "Interest rates"}, {"label": "Money supply"}, {"label": "Credit regulation"}], items: [{"text": "Raising the base rate", "b": 0}, {"text": "Quantitative easing", "b": 1}, {"text": "Lowering the deposit needed for a mortgage", "b": 2}, {"text": "Selling government bonds to banks", "b": 1}, {"text": "Cutting the rate at which the central bank lends to banks", "b": 0}, {"text": "Higher capital requirements for banks", "b": 2}], done: "Interest rates: the price of money. Money supply: the amount of money. Credit regulation: rules on lending." });
Lib.classify($("#cl2"), { prompt: "Expansionary or contractionary monetary policy?", buckets: [{"label": "Expansionary"}, {"label": "Contractionary"}], items: [{"text": "A cut in the base rate", "b": 0}, {"text": "A rise in the base rate", "b": 1}, {"text": "Quantitative easing", "b": 0}, {"text": "Reducing the money supply", "b": 1}, {"text": "Looser rules on mortgage lending", "b": 0}, {"text": "Tighter credit regulation for banks", "b": 1}, {"text": "Lowering interest rates to end deflation", "b": 0}, {"text": "Raising rates to reduce inflation", "b": 1}], done: "Expansionary: cheaper, easier credit. Contractionary: dearer, tighter credit." });
Lib.order($("#o1"), { prompt: "Put the effect of a rise in interest rates in order.", items: ["The central bank raises the base rate", "Banks raise mortgage and loan rates", "Borrowing becomes dearer and saving more attractive", "Consumption and investment fall", "AD shifts to the left"], done: "Higher rates reduce spending and AD." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Monetary policy", "Use of interest rates, money supply and credit regulation"], ["Base rate", "The central bank's policy interest rate"], ["Quantitative easing", "Creating money to buy bonds and raise the money supply"], ["Credit regulation", "Rules on how banks lend"], ["Real interest rate", "Nominal rate minus inflation"], ["Inflation target", "A published goal for the inflation rate"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "The nominal interest rate is 5% and inflation 3%. What is the real interest rate (%)?", "a": 2, "unit": "%", "tol": 0.1, "hint": "5 − 3.", "sol": "<b>2%</b>."},
  {"q": "The nominal rate is 3% and inflation 7%. What is the real interest rate (%)?", "a": -4, "unit": "%", "tol": 0.1, "hint": "3 − 7.", "sol": "<b>−4%</b>."},
  {"q": "A firm borrows $200,000 at 6%. What is the yearly interest ($)?", "a": 12000, "unit": "$", "tol": 1, "hint": "0.06 × 200,000.", "sol": "<b>$12,000</b>."},
  {"q": "The rate rises to 8%. What is the new yearly interest ($)?", "a": 16000, "unit": "$", "tol": 1, "hint": "0.08 × 200,000.", "sol": "<b>$16,000</b>."},
  {"q": "By what % has the cost of borrowing risen?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4,000 ÷ 12,000.", "sol": "<b>33.3%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Monetary policy uses:", opts: ["Interest rates, money supply and credit regulation", "Taxes and spending", "Training schemes", "Tariffs"], a: 0, why: "Not fiscal." },
  { q: "A rise in the base rate will usually:", opts: ["Make borrowing dearer", "Make borrowing cheaper", "Raise investment", "Lower saving"], a: 0, why: "The cost of credit rises." },
  { q: "Quantitative easing is:", opts: ["Expansionary", "Contractionary", "A tax", "A subsidy"], a: 0, why: "Raises the money supply." },
  { q: "Credit regulation is:", opts: ["Rules on how banks lend", "A tax on loans", "The base rate", "A subsidy to borrowers"], a: 0, why: "Controls access to credit." },
  { q: "A negative real interest rate means:", opts: ["Inflation is above the nominal rate", "The nominal rate is zero", "Savers gain", "Borrowers lose"], a: 0, why: "Borrowers gain, savers lose in real terms." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Tools", "Rates, money supply, credit rules."],
  ["Base rate", "Central bank's policy rate."],
  ["QE", "Creates money for bonds."],
  ["Credit rules", "Looser = expansionary."],
  ["Real rate", "Nominal − inflation."],
  ["Pass-through", "Base rate feeds into loan and saving rates."],
  ["Inflation target", "Anchors expectations."],
  ["Central bank", "Often independent."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A country's central bank decides to reduce the level of credit regulation. What is this an example of? (Feb/March 2025 · 12 · Q23, reworded)", opts: ["contractionary fiscal policy", "contractionary monetary policy", "expansionary fiscal policy", "expansionary monetary policy"], a: 3, why: "Looser credit rules make borrowing easier, which is expansionary monetary policy." },
  { q: "What is likely to cause a decrease in aggregate demand? (May/June 2020 · 12 · Q19, reworded)", opts: ["an appreciation in the exchange rate", "an improvement in consumer confidence", "an increase in government expenditure", "an increase in the money supply"], a: 0, why: "A higher exchange rate lowers net exports, reducing AD. The other options raise AD." },
  { q: "The diagram shows a shift in an economy's aggregate demand curve from AD1 to AD2 (to the right). What could not be a cause of the shift? (Feb/March 2022 · 12 · Q23, reworded)", opts: ["a decrease in income tax", "a decrease in the price of goods", "an increase in money wage rates", "an increase in the money supply"], a: 1, why: "A change in the price level causes a movement along AD, not a shift." },
  { q: "What is most likely to cause a rise in a country's exchange rate? (Feb/March 2023 · 12 · Q22, reworded)", opts: ["a fall in its direct taxes", "a fall in its export orders", "a rise in its interest rates", "a rise in its imports"], a: 2, why: "Higher interest rates attract funds from abroad, raising demand for the currency." },
  { q: "A country operates a floating exchange rate. What will cause the demand curve for the country's currency to shift left in the foreign exchange market? (May/June 2020 · 13 · Q22, reworded)", opts: ["a decrease in the country's interest rate", "a decrease in the country's money supply", "an increase in the country's export sales", "an increase in the country's import purchases"], a: 0, why: "Lower interest rates reduce the return on holding the currency, so demand falls." },
  { q: "Which policy will not cause a reduction in the rate of inflation? (May/June 2021 · 12 · Q30, reworded)", opts: ["increasing income tax", "reducing government spending", "reducing interest rates", "removing subsidies"], a: 2, why: "Cutting interest rates raises AD, which would add to inflation." },
  { q: "The table shows the consumer prices index (CPI) for an economy: 2016 100, 2017 103, 2018 101, 2019 97. Which action is the government most likely to take to achieve price stability? (Feb/March 2021 · 12 · Q28, reworded)", opts: ["appreciate the exchange rate", "decrease the budget deficit", "increase the money supply", "increase the rate of interest"], a: 2, why: "Prices are falling, so an increase in the money supply would raise AD and push prices up." },
  { q: "In an economy with an interest rate of 4% per annum, the rate of inflation falls from 5% to 3% per annum. What will be a benefit of this fall? (May/June 2020 · 12 · Q27, reworded)", opts: ["Menu costs will fall to zero.", "People on fixed incomes will be better off in real terms.", "Savers will gain in real terms.", "The purchasing power of the currency will rise."], a: 2, why: "The real interest rate rises from −1% to +1%, so savers now earn a positive real return." },
] });
