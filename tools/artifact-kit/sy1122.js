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

/* ---------- Currency market ---------- */
const EQ = (sh, ss) => ({ q: 50 + (sh + ss) / 2, e: 1.4 + 0.006 * (sh - ss) });
const FX = (q) => 70 + q * 6.2, FY = (e) => 300 - (e - 0.8) * 220;
function fxDraw(s) {
  const sh = s.sh || 0, ss = s.ss || 0, eq = EQ(sh, ss), peg = s.peg || 0, lo = s.lo || 0, hi = s.hi || 0;
  let o = axes(70, 300, 730, 30, "Quantity of the currency", "Exchange rate ($ per £)"); [1.0, 1.2, 1.4, 1.6, 1.8].forEach((v) => (o += SV.text(64, FY(v) + 4, v.toFixed(1), "sm", { "text-anchor": "end" })));
  const D = (dd) => [[FX(0), FY(2.0 + 0.012 * dd)], [FX(100), FY(2.0 - 1.2 + 0.012 * dd)]], S = (dd) => [[FX(0), FY(0.8 - 0.012 * dd)], [FX(100), FY(2.0 - 0.012 * dd)]];
  if (sh) o += SV.line(...D(0)[0], ...D(0)[1], "c1 dash", op(0.35)); if (ss) o += SV.line(...S(0)[0], ...S(0)[1], "c3 dash", op(0.35));
  const d = D(sh), sp = S(ss);
  o += SV.line(...d[0], ...d[1], "c1") + tag(FX(90), FY(2.0 - 0.012 * (90 - sh)) - 8, "D", "t1", 1, "middle") + SV.line(...sp[0], ...sp[1], "c3") + tag(FX(100) - 4, sp[1][1] - 8, "S", "t3", 1, "end");
  if (lo > 0) o += SV.line(70, FY(lo), 730, FY(lo), "c4 dash", op(0.8)) + SV.line(70, FY(hi), 730, FY(hi), "c4 dash", op(0.8)) + tag(726, FY(hi) - 6, "upper limit " + hi.toFixed(2), "t4", 1, "end") + tag(726, FY(lo) + 16, "lower limit " + lo.toFixed(2), "t4", 1, "end");
  let r = eq.e; if (peg > 0) r = peg; else if (lo > 0) r = Math.max(lo, Math.min(hi, eq.e));
  const qd = (2.0 - r) / 0.012 + sh, qs = (r - 0.8) / 0.012 + ss, gap = qd - qs;
  if (peg > 0) o += SV.line(70, FY(peg), 730, FY(peg), "c4") + tag(80, FY(peg) - 8, "Peg " + peg.toFixed(2), "t4");
  o += SV.circle(FX(eq.q), FY(eq.e), 6, "dot2") + tag(FX(eq.q) + 8, FY(eq.e) + 20, "market " + eq.e.toFixed(2), "t2");
  if ((peg > 0 || lo > 0) && Math.abs(gap) > 1 && (peg > 0 || r !== eq.e)) {
    const a = Math.min(qd, qs), b = Math.max(qd, qs); o += SV.line(FX(a), FY(r), FX(b), FY(r), "c2", { "stroke-width": 5 }) + tag((FX(a) + FX(b)) / 2, FY(r) + (gap > 0 ? 28 : -14), gap > 0 ? "excess demand " + Lib.fmtN(gap, 0) + ": bank SELLS currency" : "excess supply " + Lib.fmtN(-gap, 0) + ": bank BUYS currency", "t2", 1, "middle");
  }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Currency market with a peg above the equilibrium exchange rate and the excess supply the central bank must buy">${fxDraw({ peg: 1.6 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 340, label: "A fixed exchange rate above equilibrium: excess supply, central bank buying the currency and eventual devaluation", base: { sh: 0, ss: 0, peg: 0, lo: 0, hi: 0 }, draw: fxDraw, tween: 1100, dwell: 6000, steps: [
  { cap: "<b>Market equilibrium.</b> Demand for and supply of the currency meet at $1.40. In a free float this would be the exchange rate.", s: {} },
  { cap: "<b>The peg.</b> The government fixes the rate at $1.60, above equilibrium. At that rate the supply of pounds (67) is greater than the demand (33): excess supply of 33.", s: { peg: 1.6 } },
  { cap: "<b>Defending the peg.</b> To stop the pound from falling, the central bank <b>buys the 33 surplus units</b> with foreign exchange reserves, and may raise interest rates to attract demand.", s: { peg: 1.6 } },
  { cap: "<b>Devaluation.</b> If reserves run low and pressure continues, the government lowers the official rate. A fall to about $1.40 removes the gap and ends the need to intervene.", s: { peg: 1.4 } },
] });
Lib.stepper($("#stM"), { w: 760, h: 340, label: "A managed float with a band: market movement inside the band and intervention at the upper limit", base: { sh: 0, ss: 0, peg: 0, lo: 1.3, hi: 1.5 }, draw: fxDraw, tween: 1100, dwell: 6000, steps: [
  { cap: "<b>A band.</b> The central bank allows the rate to float between $1.30 and $1.50. At equilibrium ($1.40) there is no intervention.", s: { sh: 0, lo: 1.3, hi: 1.5 } },
  { cap: "<b>A small rise in demand</b> moves the market rate to about $1.46. This is inside the band, so the market decides and the central bank does nothing.", s: { sh: 10, lo: 1.3, hi: 1.5 } },
  { cap: "<b>A large rise in demand</b> would push the rate to about $1.58, above the upper limit. The central bank <b>sells the currency</b> to hold the rate at $1.50 (excess demand of about 13 is met).", s: { sh: 30, lo: 1.3, hi: 1.5 } },
  { cap: "<b>The judgement.</b> A managed float gives stability while the market rate is in the band, but if the shock is lasting the central bank may need to move the band, which is like a revaluation.", s: { sh: 30, lo: 1.4, hi: 1.6 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#sd") || !$("#pg")) return;
  const sh = +$("#sd").value, pg = +$("#pg").value / 100, eq = EQ(sh, 0), qd = (2.0 - pg) / 0.012 + sh, qs = (pg - 0.8) / 0.012, gap = qd - qs;
  $("#r1").textContent = "$" + eq.e.toFixed(2); $("#r2").textContent = "$" + pg.toFixed(2); $("#r3").textContent = Math.abs(gap) < 0.5 ? "None needed" : gap > 0 ? "Sells " + Lib.fmtN(gap, 0) : "Buys " + Lib.fmtN(-gap, 0);
  $("#rv").textContent = Math.abs(gap) < 0.5 ? "The peg equals the market rate, so no intervention is needed." : gap > 0 ? `The peg ($${pg.toFixed(2)}) is below the market rate ($${eq.e.toFixed(2)}): demand for the currency exceeds supply by ${Lib.fmtN(gap, 0)}. The central bank sells its currency and its reserves of foreign exchange rise. The currency is under-valued.` : `The peg ($${pg.toFixed(2)}) is above the market rate ($${eq.e.toFixed(2)}): supply of the currency exceeds demand by ${Lib.fmtN(-gap, 0)}. The central bank must buy the excess using its reserves. The currency is over-valued and reserves will fall.`;
  $("#labA").innerHTML = (() => { const X = (q) => 40 + q * 3.5, Y = (e) => 270 - (e - 0.8) * 200; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Quantity of the currency", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Exchange rate ($ per £)", "sm");
    o += SV.line(X(0), Y(2.0 + 0.012 * sh), X(100), Y(0.8 + 0.012 * sh), "c1") + SV.line(X(0), Y(0.8), X(100), Y(2.0), "c3") + SV.line(40, Y(pg), 400, Y(pg), "c4") + SV.circle(X(eq.q), Y(eq.e), 6, "dot2");
    if (Math.abs(gap) > 0.5) o += SV.line(X(Math.min(qd, qs)), Y(pg), X(Math.max(qd, qs)), Y(pg), "c2", { "stroke-width": 5 });
    return o + tag(44, Y(pg) - 8, "peg " + pg.toFixed(2), "t4"); })();
}
Lib.slider($("#g1"), { id: "sd", label: "Shift in demand for the currency ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labF });
Lib.slider($("#g2"), { id: "pg", label: "Pegged rate, $ per £ × 100 ", min: 120, max: 170, step: 5, value: 160, fmt: (v) => (v / 100).toFixed(2), onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labS() {
  if (!$("#sk")) return;
  const sh = +$("#sk").value, eq = EQ(sh, 0), band = Math.max(1.3, Math.min(1.5, eq.e)), act = (r) => { const g = (2.0 - r) / 0.012 + sh - (r - 0.8) / 0.012; return Math.abs(g) < 0.5 ? "none" : g > 0 ? "sells " + Lib.fmtN(g, 0) : "buys " + Lib.fmtN(-g, 0); };
  const rows = [["Floating", "$" + eq.e.toFixed(2), "none", eq.e > 1.41 ? "appreciation" : eq.e < 1.39 ? "depreciation" : "no change"], ["Managed (1.30 to 1.50)", "$" + band.toFixed(2), act(band), band > 1.41 ? "rises within the limits" : band < 1.39 ? "falls within the limits" : "no change"], ["Fixed at 1.40", "$1.40", act(1.4), "no change in the rate; reserves move"]];
  $("#tbl").innerHTML = `<div class="tw"><table class="t"><tr><th>System</th><th>Exchange rate</th><th>Central bank</th><th>What happens</th></tr>${rows.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>`).join("")}</table></div>`;
  $("#tv").textContent = sh === 0 ? "No shock: all three systems have the same rate." : Math.abs(eq.e - 1.4) < 0.101 ? "A small shock stays inside the band, so the managed float lets the market decide and does not need to intervene. The peg needs intervention from the first unit." : "A large shock: the float moves furthest, the managed float is held at its limit by intervention, and the peg is held at 1.40 by the biggest intervention. This shows the trade-off between stability and reserves.";
}
Lib.slider($("#g3"), { id: "sk", label: "Shift in demand for the currency (shock) ", min: -40, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labS });
labS();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which exchange rate system is it?", buckets: [{"label": "Fixed"}, {"label": "Managed float"}, {"label": "Free float"}], items: [{"text": "The central bank holds the rate at exactly $1.60 by buying and selling", "b": 0}, {"text": "The rate moves within a band; the central bank steps in at the limits", "b": 1}, {"text": "Only market supply and demand set the rate", "b": 2}, {"text": "Requires a large stock of foreign exchange reserves", "b": 0}, {"text": "Gives the country the most freedom to set its own interest rates", "b": 2}, {"text": "A 'dirty' float", "b": 1}, {"text": "A devaluation changes the official rate", "b": 0}, {"text": "Offers a compromise between stability and flexibility", "b": 1}], done: "Fixed: the central bank sets it. Managed: market within limits. Free float: market only." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Peg", "An official exchange rate maintained by the central bank"], ["Devaluation", "A deliberate cut in the official rate of a fixed currency"], ["Revaluation", "A deliberate rise in the official rate of a fixed currency"], ["Depreciation", "A market-driven fall in a floating currency"], ["Managed float", "A market rate with central bank intervention to limit moves"], ["Foreign exchange reserves", "Stocks of foreign currency held by the central bank"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the defence of an over-valued peg in order.", items: ["The peg is set above the equilibrium rate", "Supply of the currency exceeds demand at the peg", "The central bank buys the surplus currency", "Foreign exchange reserves fall", "If reserves run low, the currency is devalued"], done: "Excess supply, intervention, falling reserves, possible devaluation." });
Lib.calc($("#c1"), { qs: [
  {"q": "A fixed rate of $1.60 is devalued to $1.40. Calculate the percentage devaluation (%).", "a": 12.5, "unit": "%", "tol": 0.05, "hint": "Change ÷ original.", "sol": "(1.60 − 1.40) ÷ 1.60 = <b>12.5%</b>."},
  {"q": "A currency pegged at €1.20 is revalued to €1.26. Calculate the percentage revaluation (%).", "a": 5, "unit": "%", "tol": 0.05, "hint": "6 cents on 120.", "sol": "0.06 ÷ 1.20 = <b>5%</b>."},
  {"q": "At the pegged rate the demand for a currency is 30m units and supply is 45m units. How many units must the central bank buy (m)?", "a": 15, "unit": "m", "tol": 0.05, "hint": "Excess supply.", "sol": "45 − 30 = <b>15m</b> units."},
  {"q": "A central bank holds $90bn of reserves and sells $6bn a month to defend a peg. For how many months can it continue (months)?", "a": 15, "unit": "months", "tol": 0.05, "hint": "90 ÷ 6.", "sol": "<b>15 months</b>, if the pressure stays the same."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in a fixed exchange rate decided by the government is called:", opts: ["Appreciation", "Revaluation", "Devaluation", "Depreciation"], a: 1, why: "Revaluation is the official rise under a fixed system." },
  { q: "To defend a peg that is above the equilibrium rate, the central bank must:", opts: ["Sell its currency", "Buy its currency", "Cut interest rates", "Print more money"], a: 1, why: "Buying the surplus currency raises demand to match supply at the peg." },
  { q: "A feature of a managed float is that:", opts: ["The central bank intervenes to keep the rate within limits", "The rate never moves", "Reserves are never used", "The government sets all prices"], a: 0, why: "The market sets the rate within a band, with intervention at the edges." },
  { q: "Which is an advantage of a fixed exchange rate?", opts: ["Certainty for traders", "Independent interest rates", "Automatic adjustment of the balance of payments", "No need for reserves"], a: 0, why: "A stable rate reduces risk for trade and investment." },
  { q: "A devaluation is most likely to:", opts: ["Raise the price of imports", "Lower the price of imports", "Lower the price of exports at home", "End inflation"], a: 0, why: "The home currency price of imports rises." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Fixed exchange rate", "Central bank sets and defends the rate."],
  ["Managed float", "Market within a band, with intervention."],
  ["Devaluation", "Deliberate fall in the official rate."],
  ["Revaluation", "Deliberate rise in the official rate."],
  ["Over-valued peg", "Peg above equilibrium: bank buys the currency."],
  ["Under-valued peg", "Peg below equilibrium: bank sells the currency."],
  ["Reserves", "Foreign currency held by the central bank."],
  ["Trade-off", "Fixed: stability but less freedom. Float: freedom but volatility."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "An increase or decrease in the exchange rate can occur in both floating and fixed systems, but different terms are used. Which correctly names a decrease under a floating rate and an increase under a fixed rate? (Oct/Nov 2024 · 32 · Q27, reworded)", opts: ["Depreciation; appreciation", "Depreciation; revaluation", "Devaluation; appreciation", "Devaluation; revaluation"], a: 1, why: "A fall in a floating rate is depreciation. A deliberate rise in a fixed rate is a revaluation." },
  { q: "A country keeps its exchange rate against the US dollar within a narrow but changing band. What type of exchange rate is this? (Feb/March 2024 · 32 · Q28, reworded)", opts: ["Fixed", "Floating", "Managed float", "Trade-weighted"], a: 2, why: "The rate is held within a band by the central bank but the band moves, which is a managed float." },
  { q: "In an open economy with a fixed exchange rate, the currency is significantly below its purchasing power parity value. If the country moves to a floating rate, which macroeconomic aim is most likely to benefit? (May/June 2025 · 32 · Q26, reworded)", opts: ["Low inflation", "Low unemployment", "A smaller current account deficit", "Steady economic growth"], a: 0, why: "An undervalued currency would tend to appreciate when floated, making imports cheaper and lowering imported inflation, but making exports dearer." },
  { q: "A country devalues its currency to eliminate a balance of payments deficit. Why might this have a positive macroeconomic effect? (Feb/March 2023 · 32 · Q24, reworded)", opts: ["Competitive pricing of exports may create employment", "Foreign importers may depreciate their own currencies and remove the advantage", "Inelastic demand for imported raw materials may cause cost inflation", "Lost import duties may reduce government support for trade promotion"], a: 0, why: "Cheaper exports can raise export sales and create jobs. The other options describe drawbacks." },
  { q: "In which situation is a devaluation of the currency most likely to cause inflation? (Feb/March 2024 · 32 · Q25, reworded)", opts: ["Excess capacity is available", "Import tariffs are reduced", "Local substitutes for imported raw materials are unavailable", "The demand for exports is price inelastic"], a: 2, why: "If firms cannot replace imported inputs, the dearer imports raise costs and prices directly." },
  { q: "A government sets an inflation target of 3% or less. Which circumstance would make it difficult to achieve? (May/June 2025 · 32 · Q22, reworded)", opts: ["A devaluation of the currency leads to a trade surplus", "Interest rates are raised to control demand", "The government increases its tax revenue", "Wage rises are kept in line with productivity"], a: 0, why: "A devaluation-driven rise in net exports raises aggregate demand, and dearer imports add to cost pressure, both pushing inflation up." },
] });
