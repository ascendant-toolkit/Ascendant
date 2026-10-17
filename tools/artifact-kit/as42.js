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

/* ---------- circular flow ---------- */
function cfDraw(s) {
  const H = [270, 200, 150, 90], F = [270, 40, 150, 90]; // household box (x,y,w,h) and firm box
  let o = SV.rect(60, 120, 160, 60, "f1", op(0.5)) + SV.text(140, 156, "Households", "lbl bd", { "text-anchor": "middle" }) + SV.rect(540, 120, 160, 60, "f2", op(0.5)) + SV.text(620, 156, "Firms", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(220, 135, 535, 135, "c2", { "stroke-width": 3 }) + SV.arrowHead(538, 135, "r", "dot2") + SV.text(380, 126, "Consumer expenditure", "sm", { "text-anchor": "middle" });
  o += SV.line(540, 168, 225, 168, "c1", { "stroke-width": 3 }) + SV.arrowHead(222, 168, "l", "dot1") + SV.text(380, 188, "Income (wages, rent, interest, profit)", "sm", { "text-anchor": "middle" });
  if (s.w > 0) o += SV.line(110, 182, 110, 250, "c3", { "stroke-width": 3, ...op(s.w) }) + SV.arrowHead(110, 254, "d", "dot3") + SV.text(110, 272, "Saving (S) to banks", "sm", { "text-anchor": "middle", ...op(s.w) }) + SV.line(160, 182, 160, 250, "c3", { "stroke-width": 3, ...op(s.w) }) + SV.arrowHead(160, 254, "d", "dot3") + SV.text(200, 290, "Taxes (T) to government", "sm", { "text-anchor": "middle", ...op(s.w) });
  if (s.i > 0) o += SV.line(560, 250, 560, 186, "c4", { "stroke-width": 3, ...op(s.i) }) + SV.arrowHead(560, 182, "u", "dot4") + SV.text(560, 272, "Investment (I)", "sm", { "text-anchor": "middle", ...op(s.i) }) + SV.line(620, 250, 620, 186, "c4", { "stroke-width": 3, ...op(s.i) }) + SV.arrowHead(620, 182, "u", "dot4") + SV.text(640, 290, "Government spending (G)", "sm", { "text-anchor": "middle", ...op(s.i) });
  if (s.x > 0) o += SV.line(660, 40, 660, 114, "c4", { "stroke-width": 3, ...op(s.x) }) + SV.arrowHead(660, 118, "d", "dot4") + SV.text(660, 30, "Exports (X) in", "sm", { "text-anchor": "middle", ...op(s.x) }) + SV.line(580, 118, 580, 44, "c3", { "stroke-width": 3, ...op(s.x) }) + SV.arrowHead(580, 40, "u", "dot3") + SV.text(560, 30, "Imports (M) out", "sm", { "text-anchor": "middle", ...op(s.x) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Households and firms exchange income and expenditure, with withdrawals and injections added">${cfDraw({ w: 1, i: 1, x: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "The circular flow from two sectors to an open economy", base: { w: 0, i: 0, x: 0 }, draw: cfDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The basic flow.</b> Firms pay income to households for factors of production. Households spend it on goods and services, which becomes firms' revenue.", s: { w: 0 } },
  { cap: "<b>Withdrawals (leakages).</b> Households save some income (S) and pay taxes (T). These leave the flow and reduce spending.", s: { w: 1 } },
  { cap: "<b>Injections.</b> Firms invest (I) and the government spends (G). These add spending back into the flow.", s: { w: 1, i: 1 } },
  { cap: "<b>The open economy.</b> Exports (X) are a new injection and imports (M) a new withdrawal. Equilibrium: I + G + X = S + T + M.", s: { w: 1, i: 1, x: 1 } },
] });

/* ---------- injections and withdrawals bars ---------- */
function jwDraw(s) {
  const Y = (v) => 250 - v * 1.6; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm");
  const stack = (x, parts, cols, lab) => { let y = 250; parts.forEach((p, i) => { const h = p * 1.6; o += SV.rect(x, y - h, 120, h, cols[i], op(0.7)) + SV.text(x + 60, y - h / 2 + 5, ["I", "G", "X"][i] === undefined ? "" : "", "sm"); y -= h; }); o += SV.text(x + 60, 270, lab, "lbl bd", { "text-anchor": "middle" }); };
  const J = [s.i, s.g, s.x], W = [s.s, s.t, s.m];
  let y = 250; J.forEach((p, k) => { const h = p * 1.6; o += SV.rect(180, y - h, 120, h, ["f2", "f3", "f1"][k], op(0.7)) + SV.text(240, y - h / 2 + 5, ["I " + Lib.fmtN(p, 0), "G " + Lib.fmtN(p, 0), "X " + Lib.fmtN(p, 0)][k], "lbl bd", { "text-anchor": "middle" }); y -= h; });
  y = 250; W.forEach((p, k) => { const h = p * 1.6; o += SV.rect(440, y - h, 120, h, ["f2", "f3", "f1"][k], op(0.7)) + SV.text(500, y - h / 2 + 5, ["S " + Lib.fmtN(p, 0), "T " + Lib.fmtN(p, 0), "M " + Lib.fmtN(p, 0)][k], "lbl bd", { "text-anchor": "middle" }); y -= h; });
  const jt = s.i + s.g + s.x, wt = s.s + s.t + s.m;
  o += SV.text(240, 270, "Injections " + Lib.fmtN(jt, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(500, 270, "Withdrawals " + Lib.fmtN(wt, 0), "lbl bd", { "text-anchor": "middle" });
  const d = jt - wt; o += SV.text(380, 60, Math.abs(d) < 1 ? "Equilibrium: injections = withdrawals" : d > 0 ? "Injections > withdrawals: national income rises" : "Withdrawals > injections: national income falls", "lbl bd", { "text-anchor": "middle", style: Math.abs(d) < 1 ? "fill:var(--good)" : "fill:var(--accent)" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Bars of injections and withdrawals in equilibrium">${jwDraw({ i: 30, g: 30, x: 40, s: 30, t: 30, m: 40 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 290, label: "A rise in investment and the adjustment of withdrawals", base: { i: 30, g: 30, x: 40, s: 30, t: 30, m: 40 }, draw: jwDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Equilibrium.</b> Injections (I 30 + G 30 + X 40 = 100) equal withdrawals (S 30 + T 30 + M 40 = 100). National income is stable.", s: { i: 30, g: 30, x: 40, s: 30, t: 30, m: 40 } },
  { cap: "<b>Investment rises by 20.</b> Injections are now 120, more than withdrawals of 100. Spending exceeds leakages, so national income rises.", s: { i: 50, g: 30, x: 40, s: 30, t: 30, m: 40 } },
  { cap: "<b>As national income rises</b> households save more, pay more tax and buy more imports. Withdrawals grow until they reach 120 and equal injections at a higher level of income.", s: { i: 50, g: 30, x: 40, s: 36, t: 36, m: 48 } },
] });

/* ---------- Lab 1 ---------- */
function labJ() {
  const ids = ["ii", "gg", "xx", "ss", "tt", "mm"]; if (!ids.every((i) => $("#" + i))) return;
  const v = ids.map((i) => +$("#" + i).value), [I, G, X, S, T, M] = v, J = I + G + X, W = S + T + M;
  $("#r1").textContent = J; $("#r2").textContent = W; $("#r3").textContent = Math.abs(J - W) < 1 ? "stay stable" : J > W ? "rise" : "fall";
  $("#rv").textContent = Math.abs(J - W) < 1 ? `Injections (${I} + ${G} + ${X} = ${J}) equal withdrawals (${S} + ${T} + ${M} = ${W}), so the circular flow is in equilibrium.` : `Injections are ${J} and withdrawals ${W}. ${J > W ? "More is injected than leaks out, so national income will rise" : "More leaks out than is injected, so national income will fall"} until withdrawals and injections are equal again. Budget balance (T − G) = ${T - G}; trade balance (X − M) = ${X - M}.`;
  $("#labA").innerHTML = jwDraw({ i: I, g: G, x: X, s: S, t: T, m: M });
}
[["g1", "ii", "Investment (I), $bn "], ["g2", "gg", "Government spending (G), $bn "], ["g3", "xx", "Exports (X), $bn "], ["g4", "ss", "Saving (S), $bn "], ["g5", "tt", "Taxes (T), $bn "], ["g6", "mm", "Imports (M), $bn "]].forEach(([el, id, lab]) => Lib.slider($("#" + el), { id, label: lab, min: 10, max: 60, step: 5, value: [30, 30, 40, 30, 30, 40][["ii", "gg", "xx", "ss", "tt", "mm"].indexOf(id)], fmt: (v) => v, onInput: labJ }));
labJ();

/* ---------- Lab 2 ---------- */
const ECO = [["Closed economy, no government", "I", "S", "I = S", "Only households and firms. Firms' investment is the only injection and household saving the only withdrawal."], ["Closed economy with government", "I + G", "S + T", "I + G = S + T", "The government adds spending (G) as an injection and taxes (T) as a withdrawal."], ["Open economy", "I + G + X", "S + T + M", "I + G + X = S + T + M", "Exports (X) are an injection from foreign buyers and imports (M) a withdrawal to foreign sellers."]];
function showE(i) {
  const [n, j, w, c, why] = ECO[i]; $$("#eB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = j; $("#t2").textContent = w; $("#t3").textContent = c; $("#tv").textContent = n + ". " + why;
  const box = (x, y, t, k) => SV.rect(x, y, 120, 44, k, op(0.55)) + SV.text(x + 60, y + 27, t, "lbl bd", { "text-anchor": "middle" });
  $("#labB").innerHTML = box(40, 80, "Households", "f1") + box(260, 80, "Firms", "f2") + SV.line(160, 95, 258, 95, "c2", { "stroke-width": 3 }) + SV.line(260, 112, 162, 112, "c1", { "stroke-width": 3 }) + box(150, 10, "Banks (S, I)", "f3") + (i >= 1 ? box(150, 160, "Government (T, G)", "f2") : "") + (i >= 2 ? box(300, 160, "Rest of world (X, M)", "f1") : "");
}
$("#eB").innerHTML = ECO.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#eB button").forEach((b) => (b.onclick = () => showE(+b.dataset.i)));
showE(2);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Injection or withdrawal?", buckets: [{"label": "Injection"}, {"label": "Withdrawal"}], items: [{"text": "Investment by firms", "b": 0}, {"text": "Household saving", "b": 1}, {"text": "Government spending", "b": 0}, {"text": "Taxes", "b": 1}, {"text": "Exports", "b": 0}, {"text": "Imports", "b": 1}, {"text": "A new road building programme", "b": 0}, {"text": "A rise in the rate of income tax", "b": 1}], done: "Injections: I, G, X. Withdrawals: S, T, M." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Circular flow", "Income and expenditure moving between households and firms"], ["Injection", "Spending added to the flow: I, G, X"], ["Withdrawal", "Income removed from the flow: S, T, M"], ["Equilibrium", "Injections equal withdrawals"], ["Open economy", "Trades with the rest of the world"], ["Closed economy", "No trade with the rest of the world"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a rise in exports in order.", items: ["Overseas buyers increase spending on exports", "Injections exceed withdrawals", "Firms produce more and pay more income", "National income rises", "Saving, taxes and imports rise until withdrawals equal injections again"], done: "Higher injections raise national income until withdrawals catch up." });
Lib.calc($("#c1"), { qs: [
  {"q": "I = 60, G = 50, X = 40. What are total injections ($bn)?", "a": 150, "unit": "$bn", "tol": 0.5, "hint": "Add them.", "sol": "<b>$150bn</b>."},
  {"q": "S = 50, T = 45, M = 45. What are total withdrawals ($bn)?", "a": 140, "unit": "$bn", "tol": 0.5, "hint": "Add them.", "sol": "<b>$140bn</b>."},
  {"q": "With injections of 150 and withdrawals of 140, by how much do injections exceed withdrawals ($bn)?", "a": 10, "unit": "$bn", "tol": 0.5, "hint": "150 − 140.", "sol": "<b>$10bn</b>, so national income will rise."},
  {"q": "Government spending is $50bn and taxes $45bn. What is the budget balance? (deficit as a negative number)", "a": -5, "unit": "$bn", "tol": 0.5, "hint": "T − G.", "sol": "<b>−$5bn</b>, a budget deficit."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An injection into the circular flow is:", opts: ["Exports", "Imports", "Saving", "Taxes"], a: 0, why: "Foreign spending on domestic output." },
  { q: "A withdrawal from the circular flow is:", opts: ["Imports", "Investment", "Government spending", "Exports"], a: 0, why: "Spending leaving to other countries." },
  { q: "National income rises when:", opts: ["Injections exceed withdrawals", "Withdrawals exceed injections", "Both equal zero", "Taxes fall"], a: 0, why: "More is added than leaks out." },
  { q: "The equilibrium condition for an open economy is:", opts: ["I + G + X = S + T + M", "I = S", "G = T", "X = M only"], a: 0, why: "Total injections equal total withdrawals." },
  { q: "When an economy becomes open, the flow gains:", opts: ["Exports and imports", "Saving and taxes", "Investment only", "Profits only"], a: 0, why: "A new injection and a new withdrawal." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Circular flow", "Income and expenditure round."],
  ["Injections", "I, G, X."],
  ["Withdrawals", "S, T, M."],
  ["Equilibrium", "J = W."],
  ["J > W", "National income rises."],
  ["W > J", "National income falls."],
  ["Open economy", "Adds X and M."],
  ["Not required", "Multiplier, marginal propensities."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which statement about the circular flow of income is correct? (Feb/March 2023 · 12 · Q18, reworded)", opts: ["Exports and imports do not affect the equilibrium level of national income because they always cancel each other out", "The greater the level of saving, the greater the level of injections in the form of investment must be", "When consumers use past savings to increase their spending, there will be a rise in national income", "When a government increases withdrawals by increasing taxes, national income will rise"], a: 2, why: "More spending from past savings is an increase in consumption, so national income rises. Saving does not force investment to be larger, and higher taxes are a withdrawal." },
  { q: "According to the circular flow of income, what would be the immediate result of an increase in the value of a country's exports? (Feb/March 2024 · 12 · Q17, reworded)", opts: ["imports would increase", "national income would increase", "savings would increase", "taxes would increase"], a: 1, why: "Exports are an injection, so national income rises immediately. Imports, saving and taxes rise only later as income grows." },
  { q: "The diagram shows a basic two-sector circular flow of income, with the factor market and the product market between firms and households. What can be concluded about the direction of the flows? (May/June 2023 · 12 · Q21, reworded)", opts: ["Consumer expenditure flows anticlockwise", "Goods and services flow clockwise", "Incomes flow anticlockwise", "Resources flow anticlockwise"], a: 3, why: "In the standard diagram money flows clockwise (income to households, expenditure to firms) while real flows, such as resources, go the other way, anticlockwise." },
  { q: "The table lists the values of the components of an economy's circular flow of income ($m): government spending 6, exports 8, investment 9, imports 7, saving 10, tax 5. What can be concluded about the economy from the information shown? (May/June 2024 · 13 · Q17, reworded)", opts: ["It has a budget surplus", "It has a trade deficit", "It is a mixed, open economy", "Its circular flow is in equilibrium"], a: 2, why: "It has a government sector and trade with abroad, so it is a mixed, open economy. G > T (deficit), X > M (surplus) and injections of 23 exceed withdrawals of 22, so not in equilibrium." },
  { q: "Based on the circular flow of income, which condition is necessary for an open economy to be in equilibrium? (May/June 2025 · 12 · Q17, reworded)", opts: ["Government investment is equal to private investment", "Planned injections are equal to planned withdrawals", "Spending by households is equal to taxes collected by government", "Value of export earnings is equal to expenditure on imports"], a: 1, why: "Equilibrium requires I + G + X = S + T + M. Individual components need not match." },
  { q: "An open economy with a government sector is in equilibrium. Households in this economy save $100 million and firms spend $150 million on investment. Which combination of the budget balance and the current account balance would lead to an equilibrium position? (May/June 2025 · 11 · Q17, reworded)", opts: ["$100m deficit and $50m deficit", "$100m deficit and $50m surplus", "$100m surplus and $50m deficit", "$100m surplus and $50m surplus"], a: 3, why: "S − I = −50, so (T − G) + (M − X) must equal +50. A budget surplus of 100 and a current account surplus of 50 (M − X = −50) satisfy 100 − 50 = 50." },
] });
