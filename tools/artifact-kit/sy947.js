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

/* ---------- Money market ---------- */
const MX = (m) => 70 + m * 6.4, MY = (r) => 310 - r * 27;
const lpR = (m, sh) => { const x = Math.max(0, Math.min(100, m - sh)); return 1.5 + 9 * Math.pow((100 - x) / 100, 2.2); };
function mmDraw(s) {
  let o = axes(70, 310, 730, 30, "Quantity of money", "Interest rate (%)"); [0, 2, 4, 6, 8, 10].forEach((r) => (o += SV.text(64, MY(r) + 4, r, "sm", { "text-anchor": "end" })));
  const pts = []; for (let m = 0; m <= 99; m += 1) pts.push([MX(m), MY(lpR(m, s.sh))]);
  o += SV.path(Lib.ptsPath(pts), "c2") + tag(MX(99) - 4, MY(lpR(99, s.sh)) - 8, "LP", "t2", 1, "end");
  if (s.l > 0) { o += SV.line(MX(70), MY(2.2), MX(100), MY(2.2), "c4 dash", op(s.l)) + tag(MX(85), MY(2.2) - 12, "liquidity trap: flat", "t4", s.l, "middle"); }
  const r = lpR(s.m, s.sh);
  if (s.o > 0) o += SV.line(MX(s.o), 310, MX(s.o), 40, "c1 dash", op(0.45)) + tag(MX(s.o) + 4, 54, "MS₁", "t1", 0.7);
  o += SV.line(MX(s.m), 310, MX(s.m), 40, "c1") + tag(MX(s.m) + 4, 50, "MS", "t1");
  o += SV.circle(MX(s.m), MY(r), 7, "dot4") + SV.line(70, MY(r), MX(s.m), MY(r), "gr") + tag(76, MY(r) - 8, "r = " + Lib.fmtN(r, 1) + "%", "t4");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Money market: downward sloping liquidity preference, vertical money supply and the equilibrium interest rate">${mmDraw({ m: 50, o: 0, sh: 0, l: 0 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 340, label: "Money market with a vertical money supply, liquidity preference, a rise in the money supply and a liquidity trap", base: { m: 50, o: 0, sh: 0, l: 0 }, draw: mmDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Liquidity preference.</b> The LP curve slopes down: at higher interest rates people hold less idle money, at lower rates more (the speculative motive, linked to bond prices).", s: { m: 50 } },
  { cap: "<b>Equilibrium.</b> The money supply is a vertical line set by the central bank and banks. The interest rate (about 3.5%) is where LP meets MS.", s: { m: 50 } },
  { cap: "<b>An increase in the money supply</b> (QE or lower reserve requirements) shifts MS right. People hold more money than they want, so they buy bonds, bond prices rise and the <b>interest rate falls</b> (to about 2.1%).", s: { m: 70, o: 50 } },
  { cap: "<b>The liquidity trap.</b> At very low rates bond prices are very high and people expect them to fall, so they hold money: LP becomes nearly <b>flat</b>. A further rise in MS hardly lowers the rate.", s: { m: 90, o: 70, l: 1 } },
  { cap: "<b>A rise in income</b> raises transactions demand, so LP shifts right and the interest rate rises for the same money supply.", s: { m: 50, o: 0, sh: 15, l: 0 } },
] });

/* ---------- Loanable funds ---------- */
const LX = (q) => 70 + q * 6.4, LYY = (r) => 310 - r * 30;
function lfDraw(s) {
  const sS = s.s, sD = s.d, Q = 50 + 0.5 * (sS + sD), r = 1 + 0.08 * (Q - sS);
  let o = axes(70, 310, 730, 30, "Loanable funds (saving and investment)", "Interest rate (%)"); [0, 2, 4, 6, 8, 10].forEach((v) => (o += SV.text(64, LYY(v) + 4, v, "sm", { "text-anchor": "end" })));
  if (s.o > 0) { o += SV.line(LX(0), LYY(1 + 0.08 * (0 - 0)), LX(100), LYY(1 + 0.08 * 100), "c3 dash", op(0.4)) + SV.line(LX(0), LYY(9), LX(100), LYY(1), "c1 dash", op(0.4)); }
  o += SV.line(LX(0), LYY(1 + 0.08 * (0 - sS)), LX(100), LYY(1 + 0.08 * (100 - sS)), "c3") + tag(LX(100) - 4, LYY(1 + 0.08 * (100 - sS)) - 8, "Supply of funds (saving)", "t3", 1, "end");
  o += SV.line(LX(0), LYY(9 - 0.08 * (0 - sD)), LX(100), LYY(9 - 0.08 * (100 - sD)), "c1") + tag(LX(100) - 4, LYY(9 - 0.08 * (100 - sD)) + 18, "Demand for funds (investment)", "t1", 1, "end");
  o += SV.circle(LX(Q), LYY(r), 7, "dot4") + SV.line(LX(Q), LYY(r), LX(Q), 310, "gr") + SV.line(70, LYY(r), LX(Q), LYY(r), "gr") + tag(76, LYY(r) - 8, "r = " + Lib.fmtN(r, 1) + "%", "t4") + tag(LX(Q), 330, "Q = " + Lib.fmtN(Q, 0), "t4", 1, "middle");
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 345, label: "Loanable funds market: supply of saving, demand for investment funds, a rise in saving and a rise in investment demand", base: { s: 0, d: 0, o: 0 }, draw: lfDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Equilibrium.</b> Households, firms and others supply funds by saving (the supply slopes up). Firms and others borrow to invest (the demand slopes down). The interest rate (5%) balances them.", s: {} },
  { cap: "<b>More saving.</b> A rise in saving shifts the supply of funds right. The interest rate falls and more is borrowed and invested.", s: { s: 20, o: 1 } },
  { cap: "<b>Higher investment demand.</b> If business confidence rises, firms want to borrow more at every rate. Demand shifts right and the interest rate rises (about 6.6%).", s: { s: 20, d: 20, o: 1 } },
  { cap: "<b>The Keynesian objection.</b> Keynes argued the interest rate need not make saving equal to investment, because people save and invest for different reasons; income would change to bring them into balance (the paradox of thrift).", s: { s: 20, d: 20, o: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labMM() {
  if (!$("#sm") || !$("#iy")) return;
  const m = +$("#sm").value, sh = +$("#iy").value, r = lpR(m, sh), bp = 100 / (r / 3.5);
  $("#r1").textContent = Lib.fmtN(r, 1) + "%"; $("#r2").textContent = Lib.fmtN(bp, 0); $("#r3").textContent = r < 2.3 ? "Liquidity trap zone" : r > 6 ? "Tight money" : "Normal";
  $("#rv").textContent = r < 2.3 ? `At about ${Lib.fmtN(r, 1)}% the LP curve is almost flat, so more money barely cuts the rate. Monetary policy is weak and fiscal policy is more effective.` : `At a money supply of ${m} and income shift ${sh}, the interest rate is ${Lib.fmtN(r, 1)}%. Bond prices (index 100 at 3.5%) are at ${Lib.fmtN(bp, 0)}: lower rates mean higher bond prices.`;
  const X = (v) => 40 + v * 3.5, Y = (v) => 270 - v * 22; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Quantity of money", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Interest rate (%)", "sm");
  const pts = []; for (let x = 0; x <= 99; x += 1) pts.push([X(x), Y(lpR(x, sh))]); o += SV.path(Lib.ptsPath(pts), "c2") + SV.line(X(m), 270, X(m), 30, "c1") + SV.circle(X(m), Y(r), 7, "dot4") + tag(X(m) + 8, Y(r) - 10, "r = " + Lib.fmtN(r, 1) + "%", "t4");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sm", label: "Money supply ", min: 20, max: 98, step: 2, value: 50, fmt: (v) => v, onInput: labMM });
Lib.slider($("#g2"), { id: "iy", label: "Rise in income (shifts LP right) ", min: 0, max: 20, step: 2, value: 0, fmt: (v) => v, onInput: labMM });
labMM();

/* ---------- Lab 2 ---------- */
function labLF() {
  if (!$("#ls") || !$("#ld")) return;
  const sS = +$("#ls").value, sD = +$("#ld").value, Q = 50 + 0.5 * (sS + sD), r = 1 + 0.08 * (Q - sS), r0 = 5, Q0 = 50;
  $("#t1").textContent = Lib.fmtN(r, 1) + "%"; $("#t2").textContent = Lib.fmtN(Q, 0); $("#t3").textContent = sS === 0 && sD === 0 ? "None" : r < r0 - 0.1 ? "Lower rate" : r > r0 + 0.1 ? "Higher rate" : "Rate unchanged";
  $("#tv").textContent = sS > 0 && sD === 0 ? `More saving lowers the interest rate to ${Lib.fmtN(r, 1)}% and raises investment from ${Q0} to ${Lib.fmtN(Q, 0)}. This is the classical view; Keynes warns that a rise in saving may cut spending and income instead.` : sD > 0 && sS === 0 ? `More demand for investment funds raises the interest rate to ${Lib.fmtN(r, 1)}% and the quantity of funds lent to ${Lib.fmtN(Q, 0)}.` : sS === 0 && sD === 0 ? "Base case: the interest rate is 5% and 50 units are lent." : `Saving and investment demand both change: the rate is ${Lib.fmtN(r, 1)}% and funds lent are ${Lib.fmtN(Q, 0)}.`;
  const X = (q) => 40 + q * 3.5, Y = (v) => 270 - v * 25; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Loanable funds", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Interest rate (%)", "sm");
  o += SV.line(X(0), Y(1 - 0.08 * sS), X(100), Y(1 + 0.08 * (100 - sS)), "c3") + SV.line(X(0), Y(9 + 0.08 * sD), X(100), Y(9 - 0.08 * (100 - sD)), "c1") + SV.circle(X(Q), Y(r), 7, "dot4") + tag(X(Q) + 8, Y(r) - 10, "r = " + Lib.fmtN(r, 1) + "%", "t4");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "ls", label: "Rise in saving (shifts supply right) ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labLF });
Lib.slider($("#g4"), { id: "ld", label: "Rise in investment demand (shifts demand right) ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labLF });
labLF();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which motive for holding money is it?", buckets: [{"label": "Transactions"}, {"label": "Precautionary"}, {"label": "Speculative"}], items: [{"text": "Keeping money to pay for the weekly shop", "b": 0}, {"text": "Holding cash in case the car breaks down", "b": 1}, {"text": "Holding money because bond prices are expected to fall", "b": 2}, {"text": "Keeping funds to pay rent next week", "b": 0}, {"text": "Holding a rainy-day balance for unexpected medical bills", "b": 1}, {"text": "Waiting in cash because interest rates look likely to rise", "b": 2}, {"text": "A shop keeping cash for wages on Friday", "b": 0}, {"text": "Holding extra money when interest rates are very low", "b": 2}], done: "Transactions and precautionary depend on income. Speculative depends on the interest rate." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Liquidity preference", "The demand for money for transactions, precautionary and speculative reasons"], ["Active balances", "Money held for transactions and precautionary motives"], ["Idle balances", "Money held for the speculative motive"], ["Liquidity trap", "A flat LP curve at very low rates: extra money does not reduce rates"], ["Loanable funds", "Supply of and demand for funds from saving and investment"], ["Paradox of thrift", "A rise in saving that reduces income and so total saving"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of QE on the interest rate in order.", items: ["The central bank buys bonds and creates money", "The money supply rises, MS shifts right", "People hold more money than they wish and buy bonds", "Bond prices rise", "The interest rate falls"], done: "Bond prices and interest rates move in opposite directions." });
Lib.calc($("#c1"), { qs: [
  {"q": "A bond pays a fixed $50 a year. The interest rate is 5%. Calculate the price of the bond ($).", "a": 1000, "unit": "$", "tol": 0.5, "hint": "Price = payment ÷ interest rate.", "sol": "50 ÷ 0.05 = <b>$1,000</b>."},
  {"q": "The interest rate falls to 4%. Calculate the new price of the same bond ($).", "a": 1250, "unit": "$", "tol": 0.5, "hint": "50 ÷ 0.04.", "sol": "50 ÷ 0.04 = <b>$1,250</b>: the bond price rises when the rate falls."},
  {"q": "The central bank buys $30bn of bonds and the money supply rises by the same amount. If the credit multiplier is 8, by how much could the total money supply eventually rise ($bn)?", "a": 240, "unit": "$bn", "tol": 0.5, "hint": "30 × 8.", "sol": "<b>$240bn</b> (at most)."},
  {"q": "In a loanable funds market the interest rate is 6% and inflation is 2.5%. Calculate the real interest rate (%).", "a": 3.5, "unit": "%", "tol": 0.05, "hint": "Nominal minus inflation.", "sol": "<b>3.5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "In Keynes's theory, the speculative demand for money depends mainly on:", opts: ["Income", "The interest rate", "The price level", "The exchange rate"], a: 1, why: "Idle balances respond to the interest rate and expectations about bond prices." },
  { q: "A rise in the interest rate causes bond prices to:", opts: ["Rise", "Fall", "Stay the same", "Double"], a: 1, why: "Bond prices and interest rates are inversely related." },
  { q: "What is a liquidity trap?", opts: ["A situation where a rise in the money supply does not lower interest rates", "High inflation", "A budget surplus", "A fixed exchange rate"], a: 0, why: "People hold the extra money instead of buying bonds, so rates cannot fall further." },
  { q: "Which is a feature of the loanable funds theory?", opts: ["The interest rate balances saving and investment", "Money supply is vertical", "Income has no effect", "Interest is the reward for liquidity"], a: 0, why: "Saving supplies funds and investment demands them." },
  { q: "A rise in income will shift the liquidity preference curve:", opts: ["Left", "Right", "Not at all", "To a vertical line"], a: 1, why: "Transactions demand rises with income, so more money is wanted at each rate." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Liquidity preference", "Demand for money: transactions, precautionary, speculative."],
  ["Active balances", "Transactions and precautionary money; depend on income."],
  ["Idle balances", "Speculative money; depend on interest rates."],
  ["Liquidity trap", "Flat LP at low rates: extra money does not lower the rate."],
  ["Bond price and interest rate", "Move in opposite directions."],
  ["Loanable funds", "Saving supplies, investment demands: rate balances them."],
  ["Paradox of thrift", "More saving may reduce income and total saving."],
  ["Keynesian interest rate", "Determined by the money market, not saving and investment."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which combination is consistent with liquidity preference theory? Speculative demand for money depends on the interest rate; transactions demand depends on income. (Feb/March 2021 · 32 · Q25, reworded)", opts: ["Speculative demand depends on interest rates and not on income changes; transactions demand does not depend on interest rates", "Speculative demand depends on income; transactions demand depends on interest rates", "Both depend only on interest rates", "Neither depends on interest rates"], a: 0, why: "Active balances (transactions) depend on income; idle (speculative) balances depend on the interest rate." },
  { q: "Which statement about Keynes's liquidity preference model is correct? (May/June 2022 · 31 · Q25, reworded)", opts: ["Both transactions and precautionary motives are interest rate elastic", "The demand for liquidity is completely interest inelastic at low rates", "The demand to hold liquidity by households is stable", "The demand for liquidity is highly elastic at very low interest rates"], a: 3, why: "At very low rates the speculative demand is almost infinitely elastic: the liquidity trap." },
  { q: "According to liquidity preference theory, which money balances respond to changes in the interest rate? (Oct/Nov 2021 · 32 · Q26, reworded)", opts: ["Idle balances only", "Active balances only", "Both", "Neither"], a: 0, why: "Idle (speculative) balances respond to the interest rate; active balances depend on income." },
  { q: "Keynesians say the demand for money is negatively related to the interest rate. Which motive best explains this? (Oct/Nov 2021 · 33 · Q27, reworded)", opts: ["Income motive", "Precautionary motive", "Speculative motive", "Transactions motive"], a: 2, why: "At low interest rates (high bond prices) people hold more idle money." },
  { q: "In Keynesian economic theory, what is the purpose of interest? (May/June 2025 · 34 · Q18, reworded)", opts: ["To bring national income and expenditure into line", "To control the level of economic growth", "To create a balance between saving and investment", "To provide a reward for surrendering liquidity"], a: 3, why: "Keynes saw interest as the reward for giving up liquidity, not for saving." },
  { q: "An individual's demand for active money balances will move to the left if there is an increase in: (May/June 2020 · 31 · Q25, reworded)", opts: ["The frequency of income payments", "The general price level", "The individual's income", "The rate of interest"], a: 0, why: "More frequent pay means smaller balances are needed between payments." },
  { q: "Which characteristics describe an economy in a liquidity trap? Inflation, interest rate, growth. (May/June 2024 · 32 · Q21, reworded)", opts: ["High inflation, high rate, low growth", "Low inflation, high rate, low growth", "Low inflation, low rate, low growth", "Low inflation, low rate, high growth"], a: 2, why: "A liquidity trap is found in a deep slump with low inflation, near-zero rates and weak growth." },
  { q: "According to Keynesian theory, when will an increase in the money supply leave output unchanged? (Oct/Nov 2022 · 32 · Q23, reworded)", opts: ["When there is a liquidity trap", "When the increase was not anticipated", "When the exchange rate is floating", "When expectations adjust immediately"], a: 0, why: "In a liquidity trap extra money does not lower interest rates, so spending does not rise." },
] });
