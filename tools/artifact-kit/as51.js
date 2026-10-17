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

/* ---------- budget bars ---------- */
function bdDraw(s) {
  const Y = (v) => 250 - v * 1.7; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm");
  const rev = 100, spend = s.e; o += SV.rect(180, Y(rev), 120, 250 - Y(rev), "f2", op(0.65)) + SV.text(240, 270, "Revenue", "sm", { "text-anchor": "middle" }) + SV.text(240, Y(rev) - 6, rev, "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(400, Y(spend), 120, 250 - Y(spend), "f3", op(0.65)) + SV.text(460, 270, "Expenditure", "sm", { "text-anchor": "middle" }) + SV.text(460, Y(spend) - 6, Lib.fmtN(spend, 0), "lbl bd", { "text-anchor": "middle" });
  const b = rev - spend; o += SV.text(380, 60, Math.abs(b) < 0.5 ? "Balanced budget" : b < 0 ? "Budget deficit of " + Lib.fmtN(-b, 0) + ": the government borrows" : "Budget surplus of " + Lib.fmtN(b, 0) + ": it can repay debt", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Revenue of 100 against expenditure of 120 gives a budget deficit">${bdDraw({ e: 120 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 290, label: "Revenue against expenditure", base: { e: 100 }, draw: bdDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Balanced budget.</b> Revenue ($100bn) equals expenditure ($100bn).", s: { e: 100 } },
  { cap: "<b>Budget deficit.</b> Spending rises to $120bn. The $20bn gap is the deficit and must be borrowed. It adds to AD.", s: { e: 120 } },
  { cap: "<b>Budget surplus.</b> Spending falls to $85bn. The $15bn surplus can repay debt, but takes demand out of the economy.", s: { e: 85 } },
] });

/* ---------- debt path ---------- */
const DEF = [20, 25, 15, 10, -5, -10, 5, 10];
function dbDraw(s) {
  const n = Math.round(s.t); let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm"), debt = 100, pts = [];
  o += SV.text(60, 270, "", "sm");
  for (let i = 0; i <= 8; i++) { if (i > 0) debt += DEF[i - 1]; if (i <= n) { const x = 100 + i * 70, h = debt * 1.4; o += SV.rect(x - 22, 250 - h, 44, h, "f1", op(0.5)) + SV.text(x, 244 - h, Lib.fmtN(debt, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x, 268, i === 0 ? "Start" : "Y" + i, "sm", { "text-anchor": "middle" }); if (i > 0) o += SV.text(x, 230 - h, (DEF[i - 1] > 0 ? "+" : "") + DEF[i - 1], "sm", { "text-anchor": "middle", style: DEF[i - 1] > 0 ? "fill:var(--bad)" : "fill:var(--good)" }); } }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="National debt rising with deficits and falling with surpluses">${dbDraw({ t: 8 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 290, label: "The national debt as deficits and surpluses accumulate", base: { t: 0 }, draw: dbDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Start.</b> The national debt is $100bn: the stock of past borrowing.", s: { t: 0 } },
  { cap: "<b>Deficits add to the debt.</b> Deficits of $20bn, $25bn, $15bn and $10bn take it to $170bn.", s: { t: 4 } },
  { cap: "<b>Surpluses reduce it.</b> Surpluses of $5bn and $10bn pay the debt down to $155bn.", s: { t: 6 } },
  { cap: "<b>Deficits resume,</b> raising it again to $170bn. The debt is the accumulated total of all the yearly flows.", s: { t: 8 } },
] });

/* ---------- Lab 1 ---------- */
function labB() {
  if (!["rvn", "spd", "dbt"].every((i) => $("#" + i))) return;
  const r = +$("#rvn").value, e = +$("#spd").value, d = +$("#dbt").value, b = r - e, nd = d - b;
  $("#r1").textContent = (b >= 0 ? "+" : "−") + "$" + Math.abs(b) + "bn"; $("#r2").textContent = b > 0 ? "Surplus" : b < 0 ? "Deficit" : "Balanced"; $("#r3").textContent = "$" + nd + "bn";
  $("#rv").textContent = b === 0 ? `Revenue of $${r}bn equals spending of $${e}bn: a balanced budget, so the national debt is unchanged at $${d}bn.` : b < 0 ? `Spending ($${e}bn) exceeds revenue ($${r}bn) by $${-b}bn: a budget deficit, financed by borrowing. The national debt rises from $${d}bn to $${nd}bn.` : `Revenue ($${r}bn) exceeds spending ($${e}bn) by $${b}bn: a surplus, which can repay debt. The national debt falls from $${d}bn to $${nd}bn.`;
  const Y = (v) => 250 - v * 0.9; let o = SV.line(40, 250, 400, 250);
  [["Revenue", r, "f2"], ["Spending", e, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(80 + i * 140, Y(v), 100, 250 - Y(v), c, op(0.65)) + SV.text(130 + i * 140, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(130 + i * 140, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "rvn", label: "Government revenue, $bn ", min: 60, max: 200, step: 5, value: 100, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g2"), { id: "spd", label: "Government spending, $bn ", min: 60, max: 200, step: 5, value: 115, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g3"), { id: "dbt", label: "National debt at start of year, $bn ", min: 100, max: 800, step: 50, value: 400, fmt: (v) => "$" + v, onInput: labB });
labB();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["df", "gn"].every((i) => $("#" + i))) return;
  const def = +$("#df").value, g = +$("#gn").value; let d = 60, pts = [d]; for (let i = 0; i < 10; i++) { d = (d + def) / (1 + g / 100); pts.push(d); }
  const stable = 60 * g / (100 + g) * 1;
  $("#t1").textContent = Lib.fmtN(d, 0) + "% of GDP"; $("#t2").textContent = d > 60.5 ? "Rising" : d < 59.5 ? "Falling" : "Stable"; $("#t3").textContent = Lib.fmtN(stable, 1) + "% of GDP";
  $("#tv").textContent = `With a deficit of ${def}% of GDP each year and nominal GDP growth of ${g}%, the debt ratio moves from 60% to ${Lib.fmtN(d, 0)}% in ten years. ${d > 61 ? "The ratio is rising, so interest costs may take a growing share of revenue." : d < 59 ? "The ratio is falling because the economy is growing faster than the debt." : "The ratio is roughly stable."} A deficit of about ${Lib.fmtN(stable, 1)}% of GDP would keep the ratio at 60% at this growth rate.`;
  const Y = (v) => 200 - v * 1.2; let o = SV.line(40, 200, 400, 200) + SV.line(40, 200, 40, 20) + SV.text(46, 16, "Debt, % of GDP", "sm"), p = ""; pts.forEach((v, i) => (p += (i ? " L" : "M") + (40 + i * 34) + "," + Y(v)));
  o += SV.path(p, "c3", { fill: "none", "stroke-width": 3 }) + SV.line(40, Y(60), 400, Y(60), "dash") + SV.text(398, Y(60) - 6, "60% start", "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "df", label: "Budget deficit, % of GDP each year ", min: 0, max: 10, step: 1, value: 4, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g5"), { id: "gn", label: "Growth of nominal GDP, % per year ", min: 0, max: 8, step: 1, value: 4, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Flow or stock?", buckets: [{"label": "Flow (one year)"}, {"label": "Stock (accumulated)"}], items: [{"text": "The budget deficit", "b": 0}, {"text": "The national debt", "b": 1}, {"text": "Government spending this year", "b": 0}, {"text": "Total government borrowing outstanding", "b": 1}, {"text": "Tax revenue in a year", "b": 0}, {"text": "Debt as a share of GDP at the end of the year", "b": 1}, {"text": "A budget surplus", "b": 0}, {"text": "The debt built up over 20 years", "b": 1}], done: "The deficit and surplus are annual flows. The national debt is the accumulated stock." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Budget deficit", "Spending exceeds revenue in a year"], ["Budget surplus", "Revenue exceeds spending in a year"], ["National debt", "Total stock of government borrowing"], ["Debt to GDP ratio", "The debt relative to the size of the economy"], ["Balanced budget", "Revenue equals spending"], ["Price stability", "A low, stable rate of inflation"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put how a deficit becomes debt in order.", items: ["Government spending exceeds revenue", "A budget deficit arises", "The government borrows to cover it", "The national debt increases", "Interest must be paid on the larger debt"], done: "Deficits add to debt, and debt costs interest." });
Lib.calc($("#c1"), { qs: [
  {"q": "Revenue is $180bn and spending $200bn. What is the budget balance (deficit as a negative, $bn)?", "a": -20, "unit": "$bn", "tol": 0.5, "hint": "180 − 200.", "sol": "<b>−$20bn</b>, a deficit."},
  {"q": "The national debt was $500bn. After that deficit, what is it ($bn)?", "a": 520, "unit": "$bn", "tol": 0.5, "hint": "500 + 20.", "sol": "<b>$520bn</b>."},
  {"q": "GDP is $1,000bn. What is the debt to GDP ratio (%)?", "a": 52, "unit": "%", "tol": 0.2, "hint": "520 ÷ 1,000.", "sol": "<b>52%</b>."},
  {"q": "The government pays 4% interest on the $520bn debt. How much is the interest ($bn)?", "a": 20.8, "unit": "$bn", "tol": 0.1, "hint": "0.04 × 520.", "sol": "<b>$20.8bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A budget deficit means:", opts: ["Government spending exceeds revenue", "Revenue exceeds spending", "Exports exceed imports", "Imports exceed exports"], a: 0, why: "Government budget, not trade." },
  { q: "The national debt is:", opts: ["The total stock of government borrowing", "The annual deficit", "A trade deficit", "Household debt"], a: 0, why: "Accumulated." },
  { q: "A deficit usually:", opts: ["Raises AD", "Lowers AD", "Reduces debt", "Cuts unemployment only"], a: 0, why: "Expansionary." },
  { q: "A government runs a surplus. The national debt:", opts: ["Falls", "Rises", "Is unchanged", "Doubles"], a: 0, why: "Surpluses reduce debt." },
  { q: "Which is an objective of macroeconomic policy?", opts: ["Price stability", "A trade deficit", "Higher debt", "Lower growth"], a: 0, why: "Stable prices." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Budget", "Planned revenue and spending."],
  ["Deficit", "Spending > revenue."],
  ["Surplus", "Revenue > spending."],
  ["Debt", "Accumulated borrowing."],
  ["Deficit adds", "To the debt."],
  ["Debt ratio", "Debt ÷ GDP."],
  ["Cost of debt", "Interest, opportunity cost."],
  ["Objectives", "Prices, jobs, growth."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "To improve its financial position, a government decided to reduce expenditure on investment in the public sector. There was not a fall in economic growth. What was the most likely effect of the government's action? (Feb/March 2022 · 12 · Q14, reworded)", opts: ["An original budget deficit was reduced", "An original budget surplus was reduced", "Consumer expenditure decreased", "Public sector productivity decreased"], a: 0, why: "Lower spending with unchanged growth (and revenue) reduces a deficit." },
  { q: "A government has a balanced budget. It decides to increase its spending by 10%. Which increase in government revenue would produce a budget surplus? (Feb/March 2024 · 12 · Q20, reworded)", opts: ["−10%", "0%", "+10%", "+20%"], a: 3, why: "With a balanced budget, revenue must rise by more than the 10% rise in spending to create a surplus." },
  { q: "Which combination correctly classifies an expansionary fiscal measure and its impact on a budget deficit? (fiscal policy, budget deficit) (May/June 2020 · 12 · Q28, reworded)", opts: ["increased quantitative easing, unchanged", "increased welfare spending, increased", "lower income tax, reduced", "lower interest rates, unchanged"], a: 1, why: "Welfare spending is a fiscal measure that raises the deficit. Quantitative easing and interest rates are monetary policy, and lower income tax would raise the deficit." },
] });
