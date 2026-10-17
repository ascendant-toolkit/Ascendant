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

/* ---------- MRT and ART ---------- */
const taxA = (y) => 0.2 * Math.max(0, Math.min(y, 30000) - 10000) + 0.4 * Math.max(0, y - 30000);
function mrDraw(s) {
  const X = (v) => 80 + v / 100000 * 600, Y = (v) => 250 - v * 5; let o = axes(80, 250, 700, 30, "Income ($)", "Tax rate (%)"), a = "", m = "";
  for (let v = 0; v <= 100000; v += 1000) { if (v <= s.k * 1000) { a += (a ? " L" : "M") + X(v) + "," + Y(v ? taxA(v) / v * 100 : 0); const mr = v < 10000 ? 0 : v < 30000 ? 20 : 40; m += (m ? " L" : "M") + X(v) + "," + Y(mr); } }
  if (m) o += SV.path(m, "c3", { fill: "none", "stroke-width": 3 }) + SV.path(a, "c2", { fill: "none", "stroke-width": 3 });
  o += tag(660, Y(40) - 6, "MRT (steps)", "c3", s.k > 90 ? 1 : 0, "end") + tag(660, Y(taxA(100000) / 1000) + 18, "ART", "c2", s.k > 90 ? 1 : 0, "end");
  return o + [0, 20, 40, 60, 80, 100].map((v) => SV.text(X(v * 1000), 268, v + "k", "sm", { "text-anchor": "middle" })).join("");
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Marginal tax rate rising in steps and average tax rate rising smoothly below it">${mrDraw({ k: 100 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 290, label: "MRT and ART under a progressive income tax", base: { k: 0 }, draw: mrDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>The tax.</b> 0% on the first $10,000, 20% on the next $20,000 and 40% above $30,000.", s: { k: 0 } },
  { cap: "<b>Up to $10,000</b> both rates are zero: no tax is paid.", s: { k: 10 } },
  { cap: "<b>From $10,000 to $30,000</b> the marginal rate is 20% but the average rate is lower because part of the income is untaxed; the ART rises towards 13%.", s: { k: 30 } },
  { cap: "<b>Above $30,000</b> the marginal rate jumps to 40%. The average rate keeps rising, always below the MRT: the sign of a <b>progressive</b> tax.", s: { k: 100 } },
] });

/* ---------- tax and AD ---------- */
function taxAD(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: false }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A tax rise shifts AD to the left">${taxAD({ a: -20, n: 1 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A rise in income tax shifts AD to the left", base: { a: 0, n: 0 }, draw: taxAD, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, n: 0 } },
  { cap: "<b>Income tax rises.</b> Disposable income falls, so households spend less. AD shifts <b>left</b>: real output and the price level fall. This is <b>contractionary</b> fiscal policy and could be used to reduce inflation.", s: { a: -20, n: 1 } },
  { cap: "<b>An income tax cut</b> does the opposite: more disposable income, more spending, AD shifts right (<b>expansionary</b>).", s: { a: 20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!["inc", "r1x", "r2x"].every((i) => $("#" + i))) return;
  const y = +$("#inc").value, a = +$("#r1x").value / 100, b = +$("#r2x").value / 100, t = a * Math.max(0, Math.min(y, 30000) - 10000) + b * Math.max(0, y - 30000), art = y ? t / y * 100 : 0, mrt = (y < 10000 ? 0 : y < 30000 ? a : b) * 100;
  $("#r1").textContent = "$" + Lib.fmtN(t, 0); $("#r2").textContent = Lib.fmtN(art, 1) + "%"; $("#r3").textContent = Lib.fmtN(mrt, 0) + "%";
  $("#rv").textContent = `On $${Lib.fmtN(y, 0)} tax is $${Lib.fmtN(t, 0)}: ART = ${Lib.fmtN(art, 1)}%. The tax on the next dollar is ${Lib.fmtN(mrt, 0)}% (MRT). ${mrt > art + 0.05 ? "MRT is above ART, so the tax is progressive." : mrt === art ? "MRT equals ART: proportional." : "MRT is below ART."} ${mrt >= 40 ? "A high MRT may reduce the incentive to earn extra income." : ""}`;
  const X = (v) => 50 + v / 100000 * 340, Y = (v) => 250 - v * 5; let ar = "", mr = "", o = SV.line(50, 250, 400, 250) + SV.line(50, 250, 50, 40);
  for (let v = 0; v <= 100000; v += 2000) { const tt = a * Math.max(0, Math.min(v, 30000) - 10000) + b * Math.max(0, v - 30000); ar += (v ? " L" : "M") + X(v) + "," + Y(v ? tt / v * 100 : 0); mr += (v ? " L" : "M") + X(v) + "," + Y((v < 10000 ? 0 : v < 30000 ? a : b) * 100); }
  o += SV.path(mr, "c3", { fill: "none", "stroke-width": 2.5 }) + SV.path(ar, "c2", { fill: "none", "stroke-width": 3 }) + SV.circle(X(y), Y(art), 6, "dot2") + SV.circle(X(y), Y(mrt), 6, "dot3") + tag(390, 60, "MRT", "c3", 1, "end") + tag(390, 78, "ART", "c2", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "inc", label: "Income, $ ", min: 5000, max: 100000, step: 5000, value: 50000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labT });
Lib.slider($("#g2"), { id: "r1x", label: "Rate 1 (on $10k to $30k), % ", min: 5, max: 30, step: 5, value: 20, fmt: (v) => v + "%", onInput: labT });
Lib.slider($("#g3"), { id: "r2x", label: "Rate 2 (above $30k), % ", min: 10, max: 60, step: 5, value: 40, fmt: (v) => v + "%", onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labD() {
  if (!["lw", "hg"].every((i) => $("#" + i))) return;
  const sl = +$("#lw").value / 100, sh = +$("#hg").value / 100, lowY = 20000, highY = 100000, itL = Math.max(0, lowY - 10000) * 0.2 / lowY * 100, itH = (0.2 * 20000 + 0.4 * 70000) / highY * 100, saL = 10 * sl, saH = 10 * sh;
  $("#t1").textContent = "Low " + Lib.fmtN(itL, 1) + "%, high " + Lib.fmtN(itH, 1) + "%"; $("#t2").textContent = "Low " + Lib.fmtN(saL, 1) + "%, high " + Lib.fmtN(saH, 1) + "%"; $("#t3").textContent = saL > saH ? "Regressive" : saL < saH ? "Progressive" : "Proportional";
  $("#tv").textContent = `The income tax takes ${Lib.fmtN(itL, 1)}% of the low earner's income and ${Lib.fmtN(itH, 1)}% of the high earner's: progressive. A 10% sales tax on taxed goods bought with ${Lib.fmtN(sl * 100, 0)}% of the low earner's income and ${Lib.fmtN(sh * 100, 0)}% of the high earner's takes ${Lib.fmtN(saL, 1)}% and ${Lib.fmtN(saH, 1)}% of income: ${saL > saH ? "regressive, because the poorer household spends a larger share of its income" : saL < saH ? "progressive" : "proportional"}.`;
  const Y = (v) => 180 - v * 4; let o = SV.line(40, 180, 400, 180) + SV.line(40, 180, 40, 20);
  [["Income tax, low", itL, "f2"], ["Income tax, high", itH, "f2"], ["Sales tax, low", saL, "f3"], ["Sales tax, high", saH, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(60 + i * 85, Y(v), 60, 180 - Y(v), c, op(0.65)) + SV.text(90 + i * 85, 198, l, "sm", { "text-anchor": "middle" }) + SV.text(90 + i * 85, Y(v) - 6, Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "lw", label: "Share of the low earner's income spent on taxed goods, % ", min: 40, max: 100, step: 5, value: 90, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g5"), { id: "hg", label: "Share of the high earner's income spent on taxed goods, % ", min: 20, max: 100, step: 5, value: 50, fmt: (v) => v + "%", onInput: labD });
labD();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What kind of tax is it?", buckets: [{"label": "Direct"}, {"label": "Indirect"}], items: [{"text": "Income tax", "b": 0}, {"text": "VAT", "b": 1}, {"text": "Corporation tax", "b": 0}, {"text": "Fuel duty", "b": 1}, {"text": "Inheritance tax", "b": 0}, {"text": "A duty on tobacco", "b": 1}, {"text": "Capital gains tax", "b": 0}, {"text": "A sales tax on food", "b": 1}], done: "Direct taxes fall on income or wealth. Indirect taxes fall on spending." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Marginal rate of tax", "The proportion of extra income taken in tax"], ["Average rate of tax", "Total tax as a proportion of total income"], ["Progressive tax", "MRT above ART; share of income rises with income"], ["Regressive tax", "Share of income paid falls as income rises"], ["Direct tax", "Paid directly by the person or firm taxed"], ["Indirect tax", "Levied on spending and collected by sellers"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a rise in income tax on AD in order.", items: ["The government raises income tax", "Disposable income falls", "Consumption falls", "AD shifts to the left", "Real output and the price level fall"], done: "Higher tax reduces spending and AD." });
Lib.calc($("#c1"), { qs: [
  {"q": "A person earns $40,000 and pays $9,000 in tax. What is the average rate of tax (%)?", "a": 22.5, "unit": "%", "tol": 0.1, "hint": "9,000 ÷ 40,000.", "sol": "<b>22.5%</b>."},
  {"q": "Their income rises to $44,000 and tax to $10,600. What is the marginal rate (%)?", "a": 40, "unit": "%", "tol": 0.1, "hint": "1,600 ÷ 4,000.", "sol": "<b>40%</b>."},
  {"q": "Is the tax progressive? Answer 1 for yes, 0 for no.", "a": 1, "unit": "", "tol": 0.1, "hint": "Compare MRT with ART.", "sol": "<b>Yes (1)</b>: MRT (40%) is above ART (22.5%)."},
  {"q": "A household spends $20,000 of a $25,000 income on goods with a 10% sales tax. What share of income does the sales tax take (%)?", "a": 8, "unit": "%", "tol": 0.1, "hint": "2,000 ÷ 25,000.", "sol": "<b>8%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The marginal rate of tax is:", opts: ["The tax on extra income", "Total tax ÷ total income", "The lowest rate", "The sales tax rate"], a: 0, why: "Tax on the next dollar." },
  { q: "A regressive tax takes:", opts: ["A larger share of low incomes", "A larger share of high incomes", "The same share", "No tax"], a: 0, why: "Share falls as income rises." },
  { q: "Which is an indirect tax?", opts: ["VAT", "Income tax", "Corporation tax", "Inheritance tax"], a: 0, why: "On spending." },
  { q: "A reason governments tax is:", opts: ["To discourage demerit goods", "To increase AD always", "To lower revenue", "To raise imports"], a: 0, why: "Correct market failure." },
  { q: "An increase in income tax will usually:", opts: ["Shift AD left", "Shift AD right", "Shift LRAS right", "Raise exports"], a: 0, why: "Lower disposable income." },
] });
Lib.cards($("#fc1"), { cards: [
  ["MRT", "Tax on extra income."],
  ["ART", "Total tax ÷ income."],
  ["Progressive", "MRT > ART."],
  ["Regressive", "MRT < ART."],
  ["Direct", "On income and wealth."],
  ["Indirect", "On spending."],
  ["Reasons", "Revenue, equity, demerit, AD."],
  ["Tax rise", "AD shifts left."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A country uses an income tax under which the first $10 000 of income is tax-free, the next $20 000 is taxed at 20% and any income over $30 000 is taxed at a top rate of 40%. It also levies a sales tax of 10% on most products. Which combination of tax changes is most likely to create a more equal distribution of income? (Feb/March 2024 · 12 · Q14, reworded)", opts: ["a higher tax-free allowance and a higher rate of sales tax", "a higher top rate of income tax and a lower rate of sales tax", "a lower tax-free allowance and more goods exempt from sales tax", "a lower top rate of income tax and fewer goods exempt from sales tax"], a: 1, why: "A higher top rate takes more from high earners, and a lower sales tax helps the poor, who spend a larger share of their income." },
  { q: "What defines a progressive tax? (Feb/March 2025 · 12 · Q25, reworded)", opts: ["All taxpayers pay the same proportion of income in taxes", "Low-income earners pay a lower proportion of income in taxes than high-income earners", "Low-income earners pay less in taxes than high-income earners", "Low-income earners pay more in taxes than high-income earners"], a: 1, why: "The proportion of income paid rises with income." },
  { q: "Which combination of tax changes is most likely to be regressive in a developed economy? (May/June 2022 · 12 · Q14, reworded)", opts: ["increasing the rate of wealth tax and raising the rate of sales tax (VAT) on luxury products", "introducing a tax on owning property based on its sales value and increasing the rate of income tax", "reducing the basic rate of income tax and increasing the duty on fuel", "removing the tax-free allowance for income tax and extending sales tax (VAT) to include all food"], a: 3, why: "Removing the allowance and taxing food take a larger share of low incomes." },
  { q: "The table shows sources of government revenue: sale of government assets 100, tax on self employed 1000, carbon tax on goods produced 100, corporate taxes 500, capital gains tax 100, goods and services tax 1000, air passenger tax 100 ($ billions). What is the total amount of tax revenue raised by indirect taxes? (May/June 2021 · 12 · Q17, reworded)", opts: ["$1,200 billion", "$1,300 billion", "$1,400 billion", "$1,600 billion"], a: 0, why: "Indirect taxes: carbon tax 100 + goods and services tax 1000 + air passenger tax 100." },
  { q: "Three types of tax are listed: a sales tax (VAT) on fuel; a specific tax of 10% on cigarettes; the percentage of income tax on individual earnings increases as taxable income increases. Which combination describes the effect of each of these types of tax? (Feb/March 2022 · 12 · Q17, reworded)", opts: ["VAT progressive, specific tax progressive, income tax regressive", "VAT progressive, specific tax regressive, income tax progressive", "VAT regressive, specific tax progressive, income tax regressive", "VAT regressive, specific tax regressive, income tax progressive"], a: 3, why: "Sales taxes and duties are regressive, and an income tax with a rising rate is progressive." },
] });
