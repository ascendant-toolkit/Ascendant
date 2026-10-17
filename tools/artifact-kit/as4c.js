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

/* ---------- real value ---------- */
function rvDraw(s) {
  const Y = (v) => 250 - v * 0.2, f = (r, n) => Math.pow(1 + r / 100, n); let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Real value ($, year-0 prices)", "sm");
  const r = 6, yrs = s.k, v = 1000 / f(r, yrs), dpt = 1000 / f(r, yrs);
  o += SV.rect(110, Y(1000), 90, 200, "f1", op(0.25)) + SV.text(155, 270, "Cash or fixed pension", "sm", { "text-anchor": "middle" }) + SV.rect(110, Y(v), 90, 250 - Y(v), "f3", op(0.7)) + SV.text(155, Y(v) - 6, "$" + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(300, Y(1000), 90, 200, "f1", op(0.25)) + SV.text(345, 270, "A debt of $1,000", "sm", { "text-anchor": "middle" }) + SV.rect(300, Y(dpt), 90, 250 - Y(dpt), "f2", op(0.7)) + SV.text(345, Y(dpt) - 6, "$" + Lib.fmtN(dpt, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.text(540, 130, "After " + Lib.fmtN(yrs, 0) + " years at 6% inflation", "lbl bd", { "text-anchor": "middle" }) + SV.text(540, 152, "the saver loses and the borrower gains", "sm", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Cash and debt both fall in real value after years of inflation">${rvDraw({ k: 10 })}</svg>`;
Lib.stepper($("#stV"), { w: 760, h: 290, label: "The real value of cash and of debt at 6% inflation", base: { k: 0 }, draw: rvDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>Start.</b> $1,000 in cash (or a fixed pension) and a $1,000 debt. The shaded boxes show the starting value.", s: { k: 0 } },
  { cap: "<b>After 5 years at 6% inflation</b> the $1,000 buys only about $747 worth of today's goods. The saver or fixed-income earner has lost; the borrower's debt is also worth only $747 in real terms.", s: { k: 5 } },
  { cap: "<b>After 10 years</b> it is worth about $558. Inflation redistributes real income from lenders and savers to borrowers.", s: { k: 10 } },
] });
const CMP = (home, rival, yr) => ({ h: 100 * Math.pow(1 + home / 100, yr), r: 100 * Math.pow(1 + rival / 100, yr) });
function cpDraw(s) {
  let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Export price index", "sm") + SV.text(700, 270, "Years", "sm", { "text-anchor": "end" });
  let dh = "", dr = ""; for (let t = 0; t <= s.k; t += 0.25) { const p = CMP(8, 2, t), x = 60 + t * 62, yh = 250 - (p.h - 90) * 4, yr = 250 - (p.r - 90) * 4; dh += (t ? " L" : "M") + x + "," + yh; dr += (t ? " L" : "M") + x + "," + yr; }
  o += SV.path(dr, "c1", { fill: "none", "stroke-width": 3 }) + SV.path(dh, "c3", { fill: "none", "stroke-width": 3 });
  const p = CMP(8, 2, s.k); o += tag(66 + s.k * 62, 250 - (p.h - 90) * 4 - 6, "Home " + Lib.fmtN(p.h, 0), "c3") + tag(66 + s.k * 62, 250 - (p.r - 90) * 4 + 18, "Rival " + Lib.fmtN(p.r, 0), "c1");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Home export prices rising faster than a rival's">${cpDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 290, label: "Export prices when home inflation is 8% and the rival's 2%", base: { k: 0 }, draw: cpDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>Start.</b> A home exporter and a foreign rival both sell at an index price of 100.", s: { k: 0 } },
  { cap: "<b>After 3 years</b> the home price has risen 26% (inflation 8%) and the rival's 6% (inflation 2%).", s: { k: 3 } },
  { cap: "<b>After 5 years</b> the home price is about 47% higher against 10% for the rival. Home exports are now much less price competitive: sales fall and the current account is likely to worsen.", s: { k: 5 } },
] });

/* ---------- Lab 1 ---------- */
function labV() {
  if (!["in", "yr"].every((i) => $("#" + i))) return;
  const r = +$("#in").value, n = +$("#yr").value, f = Math.pow(1 + r / 100, n), v = 1000 / f;
  $("#r1").textContent = "$" + Lib.fmtN(v, 0); $("#r2").textContent = "$" + Lib.fmtN(v, 0); $("#r3").textContent = Lib.fmtN(100 / f, 0) + "% as much";
  $("#rv").textContent = `With ${r}% inflation for ${n} years prices are ${Lib.fmtN((f - 1) * 100, 0)}% higher. $1,000 held in cash or as a fixed pension buys what $${Lib.fmtN(v, 0)} bought at the start, so savers and pensioners lose. A $1,000 debt is also worth only $${Lib.fmtN(v, 0)} in real terms, so borrowers gain at the expense of lenders.`;
  const Y = (x) => 250 - x * 0.2; let o = SV.line(40, 250, 400, 250);
  [["Saved cash", v, "f3"], ["Debt owed", v, "f2"], ["Pension buys", v, "f1"]].forEach(([l, z, c], i) => (o += SV.rect(60 + i * 110, Y(1000), 80, 200, "f1", op(0.2)) + SV.rect(60 + i * 110, Y(z), 80, 250 - Y(z), c, op(0.7)) + SV.text(100 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(100 + i * 110, Y(z) - 6, "$" + Lib.fmtN(z, 0), "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "in", label: "Inflation rate, % per year ", min: 0, max: 15, step: 1, value: 5, fmt: (v) => v + "%", onInput: labV });
Lib.slider($("#g2"), { id: "yr", label: "Number of years ", min: 1, max: 15, step: 1, value: 10, fmt: (v) => v, onInput: labV });
labV();

/* ---------- Lab 2 ---------- */
function labK() {
  if (!["hm", "fr"].every((i) => $("#" + i))) return;
  const h = +$("#hm").value, r = +$("#fr").value, p = CMP(h, r, 5), rel = p.h / p.r * 100;
  $("#t1").textContent = Lib.fmtN(p.h, 0); $("#t2").textContent = Lib.fmtN(p.r, 0); $("#t3").textContent = Lib.fmtN(rel, 0) + "%";
  $("#tv").textContent = h > r ? `Home inflation (${h}%) exceeds the rival's (${r}%), so after 5 years home exports cost ${Lib.fmtN(rel - 100, 0)}% more relative to the rival's: less price competitive, falling export sales and a worse current account (other things equal, including the exchange rate).` : h < r ? `Home inflation (${h}%) is below the rival's (${r}%), so home exports become relatively cheaper (${Lib.fmtN(100 - rel, 0)}% cheaper): more competitive.` : "Equal inflation leaves relative prices unchanged.";
  let o = SV.line(40, 190, 400, 190) + SV.line(40, 190, 40, 20), a = "", b = ""; for (let t = 0; t <= 5; t += 0.25) { const q = CMP(h, r, t), x = 40 + t * 70; a += (t ? " L" : "M") + x + "," + (190 - (q.h - 95) * 3); b += (t ? " L" : "M") + x + "," + (190 - (q.r - 95) * 3); }
  o += SV.path(b, "c1", { fill: "none", "stroke-width": 3 }) + SV.path(a, "c3", { fill: "none", "stroke-width": 3 }) + tag(330, 40, "Home", "c3") + tag(330, 58, "Rival", "c1");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "hm", label: "Home inflation, % per year ", min: 0, max: 12, step: 1, value: 8, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g4"), { id: "fr", label: "Foreign (rival) inflation, % per year ", min: 0, max: 12, step: 1, value: 2, fmt: (v) => v + "%", onInput: labK });
labK();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the group gain or lose from unexpected inflation?", buckets: [{"label": "Gains"}, {"label": "Loses"}], items: [{"text": "A borrower with a fixed-rate loan", "b": 0}, {"text": "A saver with low interest", "b": 1}, {"text": "A pensioner on a fixed pension", "b": 1}, {"text": "A firm with large debts", "b": 0}, {"text": "A worker whose pay does not rise", "b": 1}, {"text": "A lender", "b": 1}, {"text": "A homeowner whose property price rises", "b": 0}, {"text": "An exporter facing dearer home costs", "b": 1}], done: "Inflation helps debtors and owners of real assets; it hurts savers, lenders and those on fixed incomes." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Menu costs", "Costs to firms of changing prices"], ["Shoe leather costs", "Time and effort spent looking for better returns"], ["Purchasing power", "What money can buy"], ["Hyperinflation", "Extremely rapid price rises that destroy money's functions"], ["Loss of competitiveness", "Exports dearer than rivals' because of higher inflation"], ["Fixed income", "Income that does not rise with prices"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the competitiveness effect of inflation in order.", items: ["Domestic inflation is higher than abroad", "Home exports become dearer relative to foreign goods", "Foreign buyers switch to rivals; home buyers switch to imports", "Net exports fall and the current account worsens", "The exchange rate may fall"], done: "Higher inflation reduces competitiveness and the current account." });
Lib.calc($("#c1"), { qs: [
  {"q": "Prices rise 5% a year for 3 years. By roughly what percentage have they risen in total (nearest whole number)?", "a": 16, "unit": "%", "tol": 0.5, "hint": "1.05³ = 1.158.", "sol": "<b>16%</b>."},
  {"q": "A fixed pension of $1,000 a month faces inflation of 4% for a year. What is it worth in last year's prices ($, nearest whole number)?", "a": 962, "unit": "$", "tol": 1, "hint": "1,000 ÷ 1.04.", "sol": "<b>$962</b>."},
  {"q": "A savings account pays 2% and inflation is 5%. What is the real interest rate (%)?", "a": -3, "unit": "%", "tol": 0.2, "hint": "2 − 5.", "sol": "<b>−3%</b>: savers lose in real terms."},
  {"q": "A firm reprints a menu at a cost of $500 four times a year. What are its yearly menu costs ($)?", "a": 2000, "unit": "$", "tol": 1, "hint": "4 × 500.", "sol": "<b>$2,000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Who is most likely to gain from unexpected inflation?", opts: ["Borrowers", "Savers", "Pensioners on fixed incomes", "Lenders"], a: 0, why: "Debts fall in real terms." },
  { q: "Menu costs are:", opts: ["The costs of changing prices", "The costs of eating out", "The costs of borrowing", "Tax on food"], a: 0, why: "A cost to firms." },
  { q: "Higher inflation than competitors is likely to:", opts: ["Reduce export competitiveness", "Raise export competitiveness", "Improve the current account", "Reduce imports"], a: 0, why: "Exports dearer." },
  { q: "Hyperinflation can destroy:", opts: ["Money's functions as a medium of exchange and store of value", "Tax revenue only", "Unemployment", "Interest rates"], a: 0, why: "Money loses trust." },
  { q: "A low and stable rate of inflation is usually considered:", opts: ["Acceptable", "Harmful", "The same as deflation", "Impossible"], a: 0, why: "Few costs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Gain", "Borrowers, owners of real assets."],
  ["Lose", "Savers, lenders, fixed incomes."],
  ["Menu costs", "Changing prices."],
  ["Shoe leather", "Searching for returns."],
  ["Uncertainty", "Less investment."],
  ["Competitiveness", "Exports dearer."],
  ["Hyperinflation", "Money fails."],
  ["Evaluate", "Rate, expected or not, who."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which group is most likely to suffer during high inflation? (May/June 2023 · 11 · Q17, reworded)", opts: ["borrowers", "importers", "producers", "fixed wage earners"], a: 3, why: "Fixed wages lose purchasing power as prices rise. Borrowers gain." },
  { q: "What is a likely consequence of inflation? (May/June 2022 · 14 · Q23, reworded)", opts: ["Fixed-income earners gain more than those whose income is gained from the ownership of property", "Real wages rise more than money wages", "The assets of creditors decrease in value at the expense of those of debtors", "The domestic purchasing power of money increases"], a: 2, why: "Inflation erodes the real value of money owed to creditors, which benefits debtors. Purchasing power falls." },
  { q: "A sudden rise in the price of imported oil caused the annual rate of inflation in a given period to be higher than expected. What might be a likely result of this? (May/June 2021 · 13 · Q22, reworded)", opts: ["Borrowers would gain", "Real wages would rise", "The balance of trade would improve", "Unemployment would fall"], a: 0, why: "Unexpectedly high inflation reduces the real value of debts, so borrowers gain." },
  { q: "Other things being equal, what is most likely to be reduced by falling labour productivity? (Feb/March 2021 · 12 · Q29, reworded)", opts: ["the balance of trade deficit", "the internal value of money", "the level of unemployment", "the rate of domestic inflation"], a: 1, why: "Lower productivity raises unit costs and prices, which reduces the internal value (purchasing power) of money." },
] });
