const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const D = (b) => [-b, 50 + 50 * b], S = (d, shift = 0) => [d, 50 - 50 * d + shift];
const fmtSteep = (v) => (v < 0.8 ? "flat (elastic)" : v > 1.4 ? "steep (inelastic)" : "medium");
const money = (v, d = 1) => Lib.fmtN(v, d);
/* ---------- 1. budget bars ---------- */
function budgetChart(s) {
  const base = 340, k = 1.75, r = s.rev, sp = s.spend, d = r - sp;
  let o = SV.line(70, base, 570, base);
  o += SV.rect(120, base - r * k, 150, r * k, "", { style: "fill:var(--accent)", opacity: 0.85 });
  o += SV.rect(330, base - sp * k, 150, sp * k, "", { style: "fill:var(--warn)", opacity: 0.85 });
  if (d < -0.5) o += SV.rect(120, base - sp * k, 150, -d * k, "", { style: "fill:none;stroke:var(--bad);stroke-width:2.5;stroke-dasharray:6 4" }) + SV.text(195, base - sp * k + (-d * k) / 2 + 5, "Gap " + money(-d, 0), "lbl bd t2", { "text-anchor": "middle" });
  if (d > 0.5) o += SV.rect(330, base - r * k, 150, d * k, "", { style: "fill:none;stroke:var(--good);stroke-width:2.5;stroke-dasharray:6 4" }) + SV.text(405, base - r * k + (d * k) / 2 + 5, "Spare " + money(d, 0), "lbl bd t3", { "text-anchor": "middle" });
  const inbar = { "text-anchor": "middle", style: "font-size:15px;paint-order:stroke;stroke:var(--surface);stroke-width:4px" };
  o += SV.text(195, base - r * k + 24, "$" + money(r, 0) + "bn", "lbl bd", inbar) + SV.text(405, base - sp * k + 24, "$" + money(sp, 0) + "bn", "lbl bd", inbar);
  o += SV.text(195, base + 22, "Government revenue", "lbl", { "text-anchor": "middle" }) + SV.text(405, base + 22, "Government spending", "lbl", { "text-anchor": "middle" });
  const verdict = Math.abs(d) < 0.5 ? "Balanced budget: revenue = spending" : d < 0 ? "Budget deficit of $" + money(-d, 0) + "bn: the government must borrow" : "Budget surplus of $" + money(d, 0) + "bn: revenue exceeds spending";
  o += SV.text(300, 52, verdict, "lbl bd " + (Math.abs(d) < 0.5 ? "" : d < 0 ? "t2" : "t3"), { "text-anchor": "middle", style: "font-size:16px" });
  o += SV.rect(620, base - s.debt * k, 90, s.debt * k, "", { style: "fill:var(--bad)", opacity: 0.6 });
  o += SV.text(665, base - s.debt * k - 8, "$" + money(s.debt, 0) + "bn", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(665, base + 22, "National debt", "lbl", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 400, label: "Budget deficit, surplus and national debt", base: { rev: 100, spend: 100, debt: 60 }, draw: budgetChart, steps: [
  { cap: "A government's <b>budget</b> compares what it raises (revenue, mostly tax) with what it spends. Here both are <b>$100bn</b>: a <b>balanced budget</b>, which is less common than the other two. Past borrowing has built up a <b>national debt</b> of $60bn.", s: { rev: 100, spend: 100, debt: 60 } },
  { cap: "The government raises spending to <b>$120bn</b> but revenue stays at $100bn. Spending is higher than revenue: a <b>budget deficit</b> of $20bn.", s: { spend: 120 } },
  { cap: "To pay for the gap the government has to <b>borrow</b> $20bn. The <b>national debt</b>, the total borrowed over time, rises from $60bn to $80bn. A deficit adds to the debt; the debt is the running total.", s: { spend: 120, debt: 80 } },
  { cap: "Now the government raises tax revenue to <b>$125bn</b> and brings spending back to $100bn. Revenue is higher than spending: a <b>budget surplus</b> of $25bn.", s: { rev: 125, spend: 100, debt: 80 } },
  { cap: "A surplus can be used to <b>repay debt</b>, which also cuts the interest the government has to pay. The debt falls to $55bn. <b>Budget deficit or surplus = revenue − spending</b> (a negative answer is a deficit).", s: { rev: 125, spend: 100, debt: 55 } },
] });

/* ================= LABS ================= */
/* Lab 1: budget, with automatic stabilisers (New Zealand 2016 table, NZ$bn) */
const SPEND = [["Healthcare", 16.2, "--accent"], ["Education", 13.5, "--good"], ["Pensions", 12.9, "--n"], ["Unemployment and other benefits", 12.3, "--bad"], ["Law and order", 3.8, "--warn"], ["Other", 18.8, "--muted"]];
const REV = [["Income tax", 32.5, "--accent"], ["GST", 19.1, "--good"], ["Other indirect tax", 6.5, "--n"], ["Corporate tax", 11.6, "--warn"], ["Other revenue", 8.8, "--muted"]];
function stack(items, x, base, k, w) {
  let y = base, o = "";
  items.forEach(([name, v, col]) => {
    const h = v * k;
    y -= h;
    o += SV.rect(x, y, w, h, "", { style: `fill:var(${col});stroke:var(--surface);stroke-width:2`, opacity: 0.85 });
    if (h > 17) o += SV.text(x + w / 2, y + h / 2 + 4, name + " " + money(v, 1), "sm bd", { "text-anchor": "middle", style: "font-size:11px;paint-order:stroke;stroke:var(--surface);stroke-width:3px" });
  });
  return o;
}
function labA() {
  if (!$("#ba") || !$("#bb") || !$("#bc")) return;
  const act = +$("#ba").value, dH = +$("#bb").value, dT = +$("#bc").value;
  const rev = [["Income tax", 32.5 * (1 + (1.5 * act) / 100) + dT, "--accent"], ["GST", 19.1 * (1 + act / 100), "--good"], ["Other indirect tax", 6.5 * (1 + act / 100), "--n"], ["Corporate tax", 11.6 * (1 + (2 * act) / 100), "--warn"], ["Other revenue", 8.8, "--muted"]];
  const sp = [["Healthcare", 16.2 + dH, "--accent"], ["Education", 13.5, "--good"], ["Pensions", 12.9, "--n"], ["Unemployment and other benefits", 12.3 * (1 - (2 * act) / 100), "--bad"], ["Law and order", 3.8, "--warn"], ["Other", 18.8, "--muted"]];
  const tr = rev.reduce((a, x) => a + x[1], 0), ts = sp.reduce((a, x) => a + x[1], 0), bal = tr - ts;
  $("#ba1").textContent = "$" + money(ts) + "bn"; $("#ba2").textContent = "$" + money(tr) + "bn";
  $("#ba3").textContent = (bal >= 0 ? "+" : "−") + "$" + money(Math.abs(bal)) + "bn"; $("#ba4").textContent = money((rev[0][1] / tr) * 100, 1) + "%";
  $("#bav").textContent = Math.abs(bal) < 0.05 ? "A balanced budget." : bal > 0 ? `Revenue is higher than spending: a budget surplus of $${money(bal)}bn.` : `Spending is higher than revenue: a budget deficit of $${money(-bal)}bn, which has to be borrowed.`;
  const note = act !== 0 && dH === 0 && dT === 0 ? (act < 0 ? " In a slump tax revenue falls and benefit spending rises automatically, so the budget moves towards deficit with no change in policy: that is an automatic stabiliser." : " In a boom tax revenue rises and benefit spending falls automatically, which moves the budget towards surplus and helps cool demand.") : "";
  $("#bav").textContent += note;
  const k = 3.1, base = 372;
  $("#labA").innerHTML = SV.line(60, base, 700, base) + stack(rev, 90, base, k, 230) + stack(sp, 420, base, k, 230) +
    SV.text(205, base + 22, "Revenue: $" + money(tr), "lbl bd", { "text-anchor": "middle" }) + SV.text(535, base + 22, "Spending: $" + money(ts), "lbl bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ba", label: "State of the economy (change in national income)", min: -10, max: 10, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v + "%" + (v < 0 ? " slump" : v > 0 ? " boom" : ""), onInput: labA });
Lib.slider($("#g2"), { id: "bb", label: "Policy: change in healthcare spending", min: -5, max: 10, step: 0.5, value: 0, fmt: (v) => (v > 0 ? "+$" : v < 0 ? "−$" : "$") + Math.abs(v) + "bn", onInput: labA });
Lib.slider($("#g3"), { id: "bc", label: "Policy: change in income tax revenue (rate change)", min: -10, max: 10, step: 0.5, value: 0, fmt: (v) => (v > 0 ? "+$" : v < 0 ? "−$" : "$") + Math.abs(v) + "bn", onInput: labA });


function labD() {
  if (!$("#da") || !$("#db")) return;
  const bal = +$("#da").value, n = +$("#db").value, d0 = 60, GDP = 200;
  const debt = [d0]; for (let i = 1; i <= n; i++) debt.push(Math.max(0, debt[i - 1] - bal));
  const end = debt[n];
  $("#da1").textContent = "$" + money(end, 0) + "bn"; $("#da2").textContent = (end - d0 >= 0 ? "+" : "−") + "$" + money(Math.abs(end - d0), 0) + "bn"; $("#da3").textContent = money((end / GDP) * 100, 1) + "%";
  $("#dav").textContent = bal < 0 ? `A deficit of $${-bal}bn a year is borrowed every year, so the debt rises by $${-bal * n}bn over ${n} years. The debt is the running total of past deficits.` : bal > 0 ? `A surplus of $${bal}bn a year can repay debt, so the debt falls (it cannot go below zero).` : "A balanced budget leaves the debt unchanged: no new borrowing is needed.";
  const base = 320, mx = Math.max(100, ...debt), k = 250 / mx, w = Math.min(54, 600 / (n + 1)), gap = w * 0.25;
  let o = SV.line(40, base, 730, base);
  debt.forEach((v, i) => {
    const x = 50 + i * (w + gap);
    o += SV.rect(x, base - v * k, w, v * k, "", { style: "fill:var(--bad)", opacity: 0.6 }) + SV.text(x + w / 2, base - v * k - 6, money(v, 0), "sm bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, base + 18, i ? "Yr " + i : "Now", "sm", { "text-anchor": "middle" });
  });
  $("#labD").innerHTML = o + SV.text(40, 24, "National debt ($bn)", "sm");
}
Lib.slider($("#g9"), { id: "da", label: "Budget position each year", min: -30, max: 30, step: 5, value: -10, fmt: (v) => (v < 0 ? "deficit $" + -v : v > 0 ? "surplus $" + v : "balanced") + (v ? "bn" : ""), onInput: labD });
Lib.slider($("#g10"), { id: "db", label: "Number of years", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v + " years", onInput: labD });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Deficit, surplus or balanced? Revenue first, spending second.", buckets: [{ label: "Budget deficit" }, { label: "Budget surplus" }, { label: "Balanced budget" }], items: [
  { text: "Revenue $90bn, spending $100bn", b: 0 }, { text: "Revenue $52bn, spending $60bn", b: 0 }, { text: "Revenue $120bn, spending $110bn", b: 1 }, { text: "Revenue $75bn, spending $70bn", b: 1 },
  { text: "Revenue $80bn, spending $80bn", b: 2 }, { text: "Spending is higher than revenue, so the government borrows", b: 0 }, { text: "Revenue exceeds spending, so debt can be repaid", b: 1 }, { text: "Spending and revenue are equal", b: 2 },
], done: "Compare revenue with spending: whichever is higher decides it." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Government budget", "A plan of what the government expects to raise and spend"],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Budget surplus", "Government revenue is higher than spending"],
  ["Balanced budget", "Government spending and revenue are equal"],
  ["National debt", "Total amount the government has borrowed over time"],
  ["Automatic stabilisers", "Spending and taxes that change with the economy without a new policy"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the steps in order: how a <b>recession</b> widens the deficit with no change in policy.", items: [
  "The economy slows and firms lay off workers",
  "Household incomes and spending fall",
  "Income tax and sales tax revenue fall",
  "More people claim unemployment benefit, so spending rises",
  "Spending rises while revenue falls: the budget deficit widens",
  "The government borrows more, adding to the national debt",
], done: "That is how automatic stabilisers work." });
Lib.calc($("#c1"), { qs: [
  { q: "The Maldives forecast a budget deficit of $200m and government revenue of $1.4bn ($1,400m). How much did it plan to spend ($m)?", a: 1600, hint: "Deficit = spending − revenue.", sol: "Spending = revenue + deficit = 1,400 + 200 = <b>$1,600m</b> ($1.6bn)." },
  { q: "A government has revenue of $85bn and spending of $92bn. What is its budget balance ($bn)? Use a minus sign for a deficit.", a: -7, hint: "Budget balance = revenue − spending.", sol: "85 − 92 = <b>−$7bn</b>, a budget deficit of $7bn." },
  { q: "New Zealand 2016: revenue was NZ$78.5bn and spending NZ$77.5bn. What is the budget position (NZ$bn; positive for a surplus)?", a: 1, sol: "78.5 − 77.5 = <b>+NZ$1.0bn</b>, a small budget surplus." },
  { q: "Income tax was NZ$32.5bn out of total revenue of NZ$78.5bn. What percentage of revenue came from income tax? (1 d.p.)", a: 41.4, tol: 0.1, sol: "32.5 ÷ 78.5 × 100 = <b>41.4%</b>." },
  { q: "An economy has a budget deficit of $5bn and GDP of $100bn. What is the deficit as a percentage of GDP?", a: 5, sol: "5 ÷ 100 × 100 = <b>5%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a budget deficit?", opts: ["Revenue is higher than spending", "Spending is higher than revenue", "The total amount borrowed over time", "Revenue and spending are equal"], a: 1, why: "A deficit means the government spends more than it raises in that period." },
  { q: "A government has revenue of $60bn and spending of $68bn. What is its budget position?", opts: ["Surplus of $8bn", "Surplus of $128bn", "Deficit of $8bn", "Balanced"], a: 2, why: "60 − 68 = −8: a deficit of $8bn." },
  { q: "What is the national debt?", opts: ["The yearly budget deficit", "The total the government has borrowed over time", "Spending on imports", "The gap between exports and imports"], a: 1, why: "Deficits add to the debt each year; the debt is the running total." },
  { q: "A recession is likely to cause the deficit to:", opts: ["Narrow, as tax revenue rises", "Widen, as tax revenue falls and benefit spending rises", "Disappear", "Stay unchanged whatever the government does"], a: 1, why: "Automatic stabilisers move the budget towards deficit in a slump." },
  { q: "Which is most likely to happen if a government runs a budget surplus?", opts: ["It has to borrow more", "It can repay some debt", "The national debt must rise", "Taxes must fall"], a: 1, why: "A surplus gives spare money which can repay debt." },
  { q: "Which is an opportunity cost of a large national debt?", opts: ["Higher interest payments each year", "Larger tax revenues", "Fewer imports", "More workers employed"], a: 0, why: "Interest on the debt uses money that could have paid for services." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Budget", "The relationship between government revenue and government spending."],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Budget deficit", "Government spending is higher than government revenue. Budget balance = revenue − spending is negative."],
  ["Budget surplus", "Government revenue is higher than spending"],
  ["Budget surplus", "Government revenue is higher than government spending."],
  ["Balanced budget", "Government spending and revenue are equal."],
  ["National debt", "Total amount the government has borrowed over time"],
  ["National debt", "The total amount the government has borrowed over time."],
  ["Automatic stabilisers", "Spending and taxes that cushion booms and slumps with no policy change"],
  ["Automatic stabilisers", "Government spending and taxation that reduce fluctuations in economic activity with no change in policy."],
  ["Tax burden", "The amount of tax paid, often shown as a percentage of GDP."],
  ["Government budget", "A plan of what the government expects to raise in revenue and spend over a year."],
  ["Borrowing", "Money a government raises, usually by selling bonds, to cover a deficit."],
] });
labA(); labD();
