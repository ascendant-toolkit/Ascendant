const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;

/* ---------- Watch 1: circular flow diagram ---------- */
function flowDraw(s) {
  const box = (x, y, w, h, t, c, v) => SV.rect(x, y, w, h, c, { opacity: 0.9 * v, rx: 10 }) + SV.text(x + w / 2, y + h / 2 + 5, t, "lbl bd", { "text-anchor": "middle", ...halo, ...op(v) });
  let o = box(60, 130, 150, 70, "Households", "f1", 1) + box(600, 130, 150, 70, "Firms", "f4", 1);
  o += arrow(600, 150, 210, 150, "l", "c1", 1) + SV.text(405, 140, "income Y (wages, rent, interest, profit)", "sm bd", { "text-anchor": "middle", ...halo });
  o += arrow(210, 185, 600, 185, "r", "c1", 1) + SV.text(405, 173, "consumption spending C", "sm bd", { "text-anchor": "middle", ...halo });
  const sec = [["Financial sector", "S", "I", 270, s.f], ["Government", "T", "G", 420, s.g], ["Foreign sector", "M", "X", 570, s.x]];
  sec.forEach(([n, w, j, cx, v]) => {
    if (v <= 0) return;
    o += box(cx - 55, 290, 110, 50, n, "f3", v) + arrow(cx - 20, 190, cx - 20, 290, "d", "c2", v) + SV.text(cx - 32, 245, w, "lbl bd t2", { "text-anchor": "end", ...halo, ...op(v) }) + arrow(cx + 20, 290, cx + 20, 190, "u", "c3", v) + SV.text(cx + 32, 245, j, "lbl bd t3", { ...halo, ...op(v) });
  });
  if (s.t > 0) o += SV.text(405, 372, "Withdrawals S + T + M (red)   ·   Injections I + G + X (green)", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.t) });
  if (s.u > 0) o += SV.text(405, 110, "J > W: spending exceeds income, so income, output and jobs rise", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.u) });
  if (s.e > 0) o += SV.text(405, 110, "J = W: national income is in equilibrium", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.e) });
  return o;
}
Lib.stepper($("#stF"), { w: 780, h: 385, label: "Circular flow of income with saving, taxes and imports leaving and investment, government spending and exports entering", base: { f: 0, g: 0, x: 0, t: 0, u: 0, e: 0 }, draw: flowDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Two sectors.</b> Firms pay <b>income (Y)</b> to households for the factors they supply. Households spend it on firms' output as <b>consumption (C)</b>. If everything is spent, the flow is the same size every round.", s: {} },
  { cap: "<b>The financial sector.</b> Households may <b>save (S)</b>: a <b>withdrawal</b> that leaves the flow. Firms may borrow savings to <b>invest (I)</b>: an <b>injection</b> that adds to spending.", s: { f: 1 } },
  { cap: "<b>The government.</b> Households and firms pay <b>taxes (T)</b>, a withdrawal. The government spends on goods, services and benefits (<b>G</b>), an injection.", s: { f: 1, g: 1 } },
  { cap: "<b>The foreign sector.</b> Residents buy <b>imports (M)</b>, a withdrawal. Foreigners buy the country's <b>exports (X)</b>, an injection.", s: { f: 1, g: 1, x: 1, t: 1 } },
  { cap: "<b>Equilibrium.</b> When total injections equal total withdrawals (I + G + X = S + T + M), the flow neither grows nor shrinks and national income is stable.", s: { f: 1, g: 1, x: 1, t: 1, e: 1 } },
  { cap: "<b>A rise in injections.</b> If exports (or investment, or government spending) rise so that J exceeds W, spending is above income. Firms produce more and hire more, and national income rises until withdrawals have grown to match.", s: { f: 1, g: 1, x: 1, t: 1, u: 1 } },
] });

/* ---------- Watch 2: injections and withdrawals graph ---------- */
const GX = (y) => 70 + y * 0.85, GY = (v) => 330 - v * 0.75;
function jwDraw(s) {
  let o = SV.line(70, 330, 760, 330) + SV.line(70, 330, 70, 30) + SV.text(760, 370, "National income Y ($m)", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Injections and withdrawals ($m)", "sm");
  [0, 200, 400, 600, 800].forEach((y) => { o += SV.text(GX(y), 346, y, "sm", { "text-anchor": "middle" }); });
  if (s.w > 0) o += SV.line(GX(0), GY(0), GX(800), GY(400), "c2", op(s.w)) + SV.text(GX(800) - 4, GY(400) - 8, "W = 0.5Y", "lbl bd t2", { "text-anchor": "end", ...op(s.w) });
  if (s.j > 0) o += SV.line(GX(0), GY(200), GX(800), GY(200), "c3", op(s.j)) + SV.text(GX(800) - 4, GY(200) - 8, "J = $200m", "lbl bd t3", { "text-anchor": "end", ...op(s.j) });
  if (s.e > 0) o += SV.line(GX(400), GY(200), GX(400), 330, "gr", op(s.e)) + SV.circle(GX(400), GY(200), 7, "dot1", op(s.e)) + SV.text(GX(400), 372, "Y = 400", "lbl bd", { "text-anchor": "middle", ...op(s.e) });
  if (s.lo > 0) o += SV.line(GX(200), GY(200), GX(300), GY(200), "c4", { "stroke-width": 4, ...op(s.lo) }) + SV.text(GX(250), GY(200) - 40, "J > W: income rises", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.lo) }) + SV.circle(GX(200), GY(100), 5, "dot2", op(s.lo)) + SV.text(GX(200) - 8, GY(100) + 20, "W = 100", "sm bd t2", { "text-anchor": "end", ...halo, ...op(s.lo) });
  if (s.hi > 0) o += SV.circle(GX(600), GY(300), 5, "dot2", op(s.hi)) + SV.text(GX(600) + 8, GY(300) - 10, "W = 300 > J: income falls", "lbl bd t2", { ...halo, ...op(s.hi) });
  if (s.n > 0) o += SV.line(GX(0), GY(280), GX(800), GY(280), "c4", { "stroke-dasharray": "6 5", ...op(s.n) }) + SV.text(GX(790), GY(280) - 8, "J1 = $280m", "lbl bd t4", { "text-anchor": "end", ...halo, ...op(s.n) }) + SV.circle(GX(560), GY(280), 7, "dot4", op(s.n)) + SV.line(GX(560), GY(280), GX(560), 330, "gr", op(s.n)) + SV.text(GX(560), 372, "Y1 = 560", "lbl bd t4", { "text-anchor": "middle", ...op(s.n) });
  return o;
}
Lib.stepper($("#stG"), { w: 780, h: 385, label: "Withdrawals rising with income, fixed injections, equilibrium national income and a rise in injections", base: { w: 0, j: 0, e: 0, lo: 0, hi: 0, n: 0 }, draw: jwDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Withdrawals.</b> Saving, taxes and imports all rise with income, so the withdrawals curve slopes up. Here <b>W = 0.5Y</b>: half of any extra income leaks out.", s: { w: 1 } },
  { cap: "<b>Injections.</b> Investment, government spending and exports do not depend on current income in this simple model, so <b>J is a horizontal line</b> at $200m.", s: { w: 1, j: 1 } },
  { cap: "<b>Equilibrium.</b> J = W where 200 = 0.5Y, so equilibrium national income is <b>Y = $400m</b>.", s: { w: 1, j: 1, e: 1 } },
  { cap: "<b>Below equilibrium</b> (Y = 200) withdrawals are only $100m, so J is greater than W: spending exceeds income, firms expand output and income rises towards 400.", s: { w: 1, j: 1, e: 1, lo: 1 } },
  { cap: "<b>Above equilibrium</b> (Y = 600) withdrawals are $300m, more than J: spending falls short, firms cut output and income falls back towards 400.", s: { w: 1, j: 1, e: 1, hi: 1 } },
  { cap: "<b>A rise in injections</b> to $280m shifts J up. The new equilibrium is where 280 = 0.5Y: <b>Y1 = $560m</b>. Injections rose by $80m but income rose by $160m, the multiplier effect (part 2).", s: { w: 1, j: 1, e: 0.4, n: 1 } },
] });

/* ---------- Lab 1: equilibrium ---------- */
function labEq() {
  if (!$("#jj") || !$("#ww")) return;
  const J = +$("#jj").value, w = +$("#ww").value, Y = J / w, F = { x: (v) => 40 + v * 0.34, y: (v) => 270 - v * 0.26 };
  $("#e1").textContent = "$" + Lib.fmtN(Y, 0) + "m"; $("#e2").textContent = "$" + Lib.fmtN(J, 0) + "m"; $("#e3").textContent = Lib.fmtN(1 / w, 2);
  $("#ev").textContent = `Withdrawals are ${Math.round(w * 100)}% of income, so they equal injections of $${J}m when Y = ${J} ÷ ${w} = $${Lib.fmtN(Y, 0)}m. A smaller share of income leaking out (a lower w) means a higher equilibrium income for the same injections.`;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "National income Y ($m)", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "J, W ($m)", "sm");
  o += SV.line(F.x(0), F.y(0), F.x(1000), F.y(w * 1000), "c2") + SV.line(F.x(0), F.y(J), F.x(1000), F.y(J), "c3") + SV.line(F.x(Y), F.y(J), F.x(Y), 270, "gr") + SV.circle(F.x(Y), F.y(J), 6, "dot1") + SV.text(F.x(Y), 288, Lib.fmtN(Y, 0), "sm bd", { "text-anchor": "middle" }) + SV.text(396, F.y(w * 1000) + 16, "W", "sm bd t2", { "text-anchor": "end" }) + SV.text(396, F.y(J) - 6, "J", "sm bd t3", { "text-anchor": "end" });
  $("#labJ").innerHTML = o;
}
Lib.slider($("#g1"), { id: "jj", label: "Injections J ($m): ", min: 100, max: 300, step: 20, value: 200, fmt: (v) => v, onInput: labEq });
Lib.slider($("#g2"), { id: "ww", label: "Withdrawal rate w (share of income): ", min: 0.3, max: 0.8, step: 0.05, value: 0.5, fmt: (v) => Lib.fmtN(v, 2), onInput: labEq });

/* ---------- Lab 2: net injection ---------- */
function labNet() {
  if (!$("#fi") || !$("#fs") || !$("#fg") || !$("#ft") || !$("#fx") || !$("#fm")) return;
  const I = +$("#fi").value, S = +$("#fs").value, G = +$("#fg").value, T = +$("#ft").value, X = +$("#fx").value, M = +$("#fm").value, J = I + G + X, W = S + T + M, net = J - W;
  $("#n1").textContent = "$" + J + "m"; $("#n2").textContent = "$" + W + "m"; $("#n3").textContent = (net > 0 ? "+" : net < 0 ? "−" : "") + "$" + Math.abs(net) + "m"; $("#n4").textContent = net > 0 ? "Rises" : net < 0 ? "Falls" : "Stable";
  const pr = I - S, gv = G - T, fo = X - M;
  $("#nv").textContent = net === 0 ? "Injections equal withdrawals: national income is in equilibrium."
    : `${net > 0 ? "Injections exceed withdrawals" : "Withdrawals exceed injections"} by $${Math.abs(net)}m, so national income ${net > 0 ? "rises" : "falls"}. Private sector (I − S): ${pr >= 0 ? "+" : "−"}${Math.abs(pr)}; government (G − T): ${gv >= 0 ? "+" : "−"}${Math.abs(gv)}; foreign (X − M): ${fo >= 0 ? "+" : "−"}${Math.abs(fo)}.`;
  const H = (v) => v * 0.9, base = 250;
  let o = SV.line(30, base, 400, base);
  [[70, [I, G, X], "Injections", ["I", "G", "X"]], [240, [S, T, M], "Withdrawals", ["S", "T", "M"]]].forEach(([x, vals, l, nm]) => {
    let y = base; const cl = ["f1", "f3", "f4"];
    vals.forEach((v, i) => { const h = H(v); o += SV.rect(x, y - h, 100, h, cl[i]) + (h > 14 ? SV.text(x + 50, y - h / 2 + 4, nm[i] + " " + v, "sm bd", { "text-anchor": "middle", ...halo }) : ""); y -= h; });
    o += SV.text(x + 50, y - 8, "$" + vals.reduce((a, b) => a + b, 0) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 272, l, "sm", { "text-anchor": "middle" });
  });
  $("#labK").innerHTML = o;
}
[["#g3", "fi", "Investment I"], ["#g4", "fs", "Saving S"], ["#g5", "fg", "Government spending G"], ["#g6", "ft", "Taxes T"], ["#g7", "fx", "Exports X"], ["#g8", "fm", "Imports M"]].forEach(([sel, id, lab], k) => Lib.slider($(sel), { id, label: lab + " ($m): ", min: 0, max: 100, step: 10, value: [60, 50, 80, 70, 40, 50][k], fmt: (v) => v, onInput: labNet }));

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each flow an injection into, a withdrawal from, or neither in the circular flow of income?",
  buckets: [{ label: "Injection" }, { label: "Withdrawal" }, { label: "Neither (stays inside the flow)" }],
  items: [
    { text: "Firms buying new machinery", b: 0 }, { text: "Government spending on hospitals", b: 0 }, { text: "Foreign tourists spending in hotels", b: 0 }, { text: "Exports of manufactured goods", b: 0 },
    { text: "Households saving in a bank", b: 1 }, { text: "Income tax paid", b: 1 }, { text: "Spending on imported cars", b: 1 }, { text: "Residents holidaying abroad", b: 1 },
    { text: "A household buying domestic groceries", b: 2 }, { text: "Wages paid to workers by firms", b: 2 }, { text: "Moving money between two bank accounts", b: 2 },
  ], done: "Injections are I, G and X; withdrawals are S, T and M. Spending on domestic goods and wages stay inside the flow.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Circular flow of income", "A model of money moving between households, firms and other sectors"],
  ["Injection", "Spending that enters the circular flow: I, G or X"],
  ["Withdrawal (leakage)", "Income that leaves the circular flow: S, T or M"],
  ["Equilibrium national income", "The level of income at which injections equal withdrawals"],
  ["Net injection", "Total injections greater than total withdrawals"],
  ["Full employment level of income", "The level of national income when all resources are fully employed"],
  ["Transfer payment", "A payment such as a benefit with no good or service in return (a negative tax)"],
], done: "Seven words for the circular flow." });
Lib.order($("#o1"), { prompt: "Put the effects of a rise in exports in order.", items: [
  "Foreign demand for the country's exports rises",
  "Injections (X) are greater than withdrawals",
  "Spending on domestic output rises above income",
  "Firms increase output and take on more workers",
  "National income rises, and withdrawals (saving, taxes, imports) rise with it",
  "A new equilibrium is reached where injections again equal withdrawals",
], done: "A reliable chain for any change in injections." });
Lib.calc($("#c1"), { qs: [
  { q: "Investment is $60m, government spending $80m and exports $40m. What are total injections ($m)?", a: 180, sol: "60 + 80 + 40 = <b>$180m</b>." },
  { q: "Saving is $50m, taxes $70m and imports $50m. What are total withdrawals ($m)?", a: 170, sol: "50 + 70 + 50 = <b>$170m</b>." },
  { q: "Using those figures, what is the net injection ($m)?", a: 10, sol: "180 − 170 = <b>+$10m</b>: national income is likely to rise." },
  { q: "Withdrawals are W = 0.25Y and injections are $150m. What is equilibrium national income ($m)?", a: 600, hint: "Set 0.25Y = 150.", sol: "Y = 150 ÷ 0.25 = <b>$600m</b>." },
  { q: "Injections rise to $180m with W = 0.25Y. What is the new equilibrium income ($m)?", a: 720, sol: "Y = 180 ÷ 0.25 = <b>$720m</b>." },
  { q: "By how much did income rise when injections rose from $150m to $180m ($m)?", a: 120, sol: "720 − 600 = <b>$120m</b>, four times the $30m rise in injections." },
  { q: "A government spends $100m and collects $80m in taxes. Is the government a net injection or withdrawal, and by how much ($m, positive for injection)?", a: 20, sol: "G − T = 100 − 80 = <b>+$20m</b>: a net injection." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an injection into the circular flow?", opts: ["saving", "taxation", "imports", "investment"], a: 3, why: "Injections are investment, government spending and exports." },
  { q: "Which is a withdrawal from the circular flow?", opts: ["government spending", "exports", "saving", "investment"], a: 2, why: "Withdrawals are saving, taxes and imports." },
  { q: "National income is in equilibrium when:", opts: ["saving equals investment only", "injections equal withdrawals", "exports equal imports only", "government spending equals zero"], a: 1, why: "J = W: the flow is neither growing nor shrinking." },
  { q: "If injections exceed withdrawals, national income will:", opts: ["rise", "fall", "stay the same", "become zero"], a: 0, why: "Spending is above income, so firms produce and employ more." },
  { q: "A rise in the rate of interest is likely to:", opts: ["raise saving and cut investment", "cut saving and raise investment", "raise exports directly", "have no effect on J or W"], a: 0, why: "Saving rewards rise and borrowing costs rise." },
  { q: "Spending by foreign tourists in a country is:", opts: ["an import", "an export, so an injection", "a withdrawal", "a transfer payment"], a: 1, why: "Foreigners buying the country's services are buying exports." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Circular flow of income", "Money flows from firms to households as income and back as spending, with withdrawals and injections."],
  ["Injection", "Spending added to the flow: investment, government spending and exports."],
  ["Withdrawal (leakage)", "Income taken out of the flow: saving, taxes and imports."],
  ["J = I + G + X", "Total injections."],
  ["W = S + T + M", "Total withdrawals."],
  ["Equilibrium", "National income is stable where injections equal withdrawals."],
  ["Net injection", "J greater than W: income rises."],
  ["Net withdrawal", "W greater than J: income falls."],
  ["Full employment level of income", "The level of income when all resources are fully employed."],
  ["Transfer payment", "A benefit with no good or service in return; treated as a negative tax."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2021 · 32 · Q27] Which row correctly identifies injections into a country's circular flow of income? (private sector S > I, public sector T > G, trade sector X > M)", opts: ['no, no, no', 'no, no, yes', 'yes, no, no', 'yes, yes, yes'], a: 1, why: 'Net injections come from the trade sector when X > M. S > I and T > G are net withdrawals.' },
  { q: '[May/June 2021 · 31 · Q27] What would be an increase in leakages or withdrawals from the circular flow of income?', opts: ['increase in government spending on anti-smoking campaigns', 'increase in spending on imports of luxury cars', 'increase in spending on transfer payments', 'increase in wages paid to government employees'], a: 1, why: 'Imports are a withdrawal. Government spending, transfers and public wages are injections or neutral.' },
  { q: '[May/June 2022 · 32 · Q25] What does not change the level of withdrawals from the circular flow of income?', opts: ['households having more of their income taken in tax following a rise in the rate of income tax', 'households spending more on imported cars following a currency appreciation', 'households taking money from their savings to spend on a celebration', 'households transferring money from an account in one bank to a different bank'], a: 3, why: 'Moving money between banks does not change saving, taxes or imports. A, B and C change T, M and S.' },
  { q: '[May/June 2022 · 32 · Q27] What could be used to offset a leakage from the circular flow of income?', opts: ['a reduction in domestic consumption', 'a reduction in government expenditure', 'an increase in the rate of interest', 'an increase in investment'], a: 3, why: 'Investment is an injection, so it offsets a leakage such as saving.' },
  { q: "[Oct/Nov 2020 · 31 · Q25] Which correctly identifies net leakages from a country's circular flow of income? (private sector S > I, government sector T > G, trade sector X > M)", opts: ['no, no, no', 'no, no, yes', 'yes, yes, no', 'yes, yes, yes'], a: 2, why: "Net leakages need S > I and T > G, but X > M would be a net injection, so the trade sector is 'no'." },
  { q: '[Oct/Nov 2021 · 33 · Q23] What is not considered to be an injection into the circular flow of income of an economy?', opts: ['a rise in exports of financial services', 'firms investing in new production techniques', 'increased government spending on health services', 'spending on hotels and entertainment by tourists visiting another country'], a: 3, why: 'Spending by residents visiting another country is an import for their home economy, not an injection.' },
  { q: "[Oct/Nov 2021 · 33 · Q25] What identifies net injections into a country's circular flow of income? (I > S, X < M, G < T)", opts: ['yes, no, no', 'yes, no, yes', 'no, yes, no', 'no, yes, yes'], a: 0, why: "Net injections need I > S, X > M and G > T. So I > S is 'yes', while X < M and G < T are 'no'." },
] });
