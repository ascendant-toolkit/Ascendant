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

/* ---------- spending composition ---------- */
function spDraw(s) {
  const Y = (v) => 250 - v * 3; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "% of government spending", "sm");
  const parts = [["Transfer payments", 35, "f1"], ["Current spending (wages, running costs)", 45, "f2"], ["Capital spending", 20, "f3"]]; let y = 250;
  parts.forEach(([n, v, c], i) => { const k = Math.max(0, Math.min(1, s.k - i)); if (k > 0) { const h = v * 3 * k; o += SV.rect(240, y - h, 170, h, c, op(0.65)) + SV.text(325, y - h / 2 + 5, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(430, y - h / 2 + 5, n, "sm"); y -= h; } });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Government spending split into transfer payments, current spending and capital spending">${spDraw({ k: 3 })}</svg>`;
function fpDraw(s) { return adasPlot({ a: s.a, s: 0, l: s.l, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Expansionary fiscal policy shifts AD to the right">${fpDraw({ a: 20, l: 0, n: 1 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Expansionary fiscal policy in a recession", base: { a: 0, l: 0, n: 0 }, draw: fpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A recession.</b> Equilibrium output (50) is well below potential output (75): spare capacity and cyclical unemployment.", s: { a: 0, l: 0, n: 0 } },
  { cap: "<b>The government cuts income tax and raises spending.</b> Disposable income and demand rise: AD shifts <b>right</b>. Real output rises towards potential and employment rises, with only a modest rise in the price level.", s: { a: 20, l: 0, n: 1 } },
  { cap: "<b>The cost.</b> The budget deficit and the national debt rise, and some of the extra spending leaks abroad as imports.", s: { a: 20, l: 0, n: 1 } },
] });
function cpDraw(s) { return adasPlot({ a: s.a, s: 0, l: -15, g: 1, n: s.n }); }
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary fiscal policy when the economy is overheating", base: { a: 25, n: 0 }, draw: cpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A boom.</b> AD has risen so that output (about 62) is above the sustainable level (the LRAS at 60) and prices are rising: an inflationary gap.", s: { a: 25, n: 0 } },
  { cap: "<b>The government raises taxes and cuts spending.</b> AD shifts <b>left</b>: output falls back to the sustainable level and the price level falls, reducing inflation.", s: { a: 8, n: 1 } },
  { cap: "<b>The cost.</b> Slower growth and some unemployment in the short run, but a smaller deficit.", s: { a: 8, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!["dg", "dt"].every((i) => $("#" + i))) return;
  const g = +$("#dg").value, t = +$("#dt").value, a = Math.max(-30, Math.min(40, 1.0 * g - 0.6 * t)), e = sdEq(a, 0), e0 = sdEq(0, 0), bal = -(g) + t;
  $("#r1").textContent = Math.abs(a) < 0.5 ? "No change" : a > 0 ? "Shifts right" : "Shifts left"; $("#r2").textContent = "Y " + Lib.fmtN(e.q, 1) + ", P " + Lib.fmtN(e.p, 1); $("#r3").textContent = (bal >= 0 ? "+" : "−") + "$" + Math.abs(bal) + "bn";
  $("#rv").textContent = Math.abs(a) < 0.5 ? "The changes offset each other (or are zero), so AD does not shift." : `${g > 0 ? "Spending rises by $" + g + "bn. " : g < 0 ? "Spending falls by $" + -g + "bn. " : ""}${t > 0 ? "Taxes rise by $" + t + "bn. " : t < 0 ? "Taxes fall by $" + -t + "bn. " : ""}AD shifts ${a > 0 ? "right (expansionary)" : "left (contractionary)"}: real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. The budget balance moves by ${bal >= 0 ? "+" : "−"}$${Math.abs(bal)}bn (before any change in tax revenue caused by the new output). (Government spending changes AD fully; a tax change affects it by less, because some of the extra income is saved.)`;
  $("#labA").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "dg", label: "Change in government spending, $bn ", min: -20, max: 30, step: 5, value: 20, fmt: (v) => v, onInput: labF });
Lib.slider($("#g2"), { id: "dt", label: "Change in taxes, $bn ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
const SIT = [["A deep recession with high unemployment", "Expansionary", "Raise spending, cut taxes", "Higher deficit and debt", "AD is far below capacity, so a boost to demand raises output and jobs with little inflation."], ["A boom with rising inflation", "Contractionary", "Cut spending, raise taxes", "Slower growth, rising unemployment", "AD is above capacity, so reducing it lowers inflation."], ["Deflation and falling spending", "Expansionary", "Tax cuts, infrastructure spending", "May not raise confidence", "More spending counters falling prices and demand."], ["A large budget deficit and high debt, steady growth", "Contractionary", "Gradual spending cuts, tax rises", "May slow growth", "The aim is to reduce borrowing and debt over time."], ["Weak growth but low spare capacity", "Supply-side focused", "Spending on education and infrastructure", "Takes years to work", "Capital spending raises productive capacity (LRAS), not only AD."]];
function showS(i) {
  const [n, st, tl, rk, why] = SIT[i]; $$("#sB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = st; $("#t2").textContent = tl; $("#t3").textContent = rk; $("#tv").textContent = `${n}: ${why}`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, st === "Expansionary" ? "f2" : st === "Contractionary" ? "f3" : "f1", { rx: 12, ...op(0.45) }) + SV.text(210, 105, st, "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(210, 170, tl, "sm", { "text-anchor": "middle" });
}
$("#sB").innerHTML = SIT.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
$$("#sB button").forEach((b) => (b.onclick = () => showS(+b.dataset.i)));
showS(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Expansionary or contractionary fiscal policy?", buckets: [{"label": "Expansionary"}, {"label": "Contractionary"}], items: [{"text": "A cut in income tax", "b": 0}, {"text": "Higher government spending on roads", "b": 0}, {"text": "A rise in VAT", "b": 1}, {"text": "Cutting public sector spending", "b": 1}, {"text": "A tax rise to reduce the deficit", "b": 1}, {"text": "Increasing welfare payments", "b": 0}, {"text": "A government stimulus package", "b": 0}, {"text": "Reducing a budget deficit to curb inflation", "b": 1}], done: "Expansionary: more spending or lower taxes. Contractionary: less spending or higher taxes." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Fiscal policy", "Use of government spending and taxation"], ["Capital expenditure", "Spending on lasting assets such as roads"], ["Current expenditure", "Day-to-day spending such as wages"], ["Expansionary fiscal policy", "Raises AD through higher spending or lower taxes"], ["Crowding out", "Government borrowing reduces private spending"], ["Time lag", "Delay between a problem and the effect of a policy"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a cut in income tax in order.", items: ["The government cuts income tax", "Disposable income rises", "Consumption rises", "AD shifts to the right", "Real output and employment rise"], done: "Tax cut raises spending and AD." });
Lib.calc($("#c1"), { qs: [
  {"q": "Government spending is $500bn, of which $90bn is capital spending. What share is capital spending (%)?", "a": 18, "unit": "%", "tol": 0.1, "hint": "90 ÷ 500.", "sol": "<b>18%</b>."},
  {"q": "Spending rises by $20bn and taxes are unchanged. What is the change in the budget balance ($bn)?", "a": -20, "unit": "$bn", "tol": 0.5, "hint": "More spending, same revenue.", "sol": "<b>−$20bn</b>: the deficit rises."},
  {"q": "A tax cut of $10bn raises consumption by $6bn (the rest is saved). By how much does AD rise at first ($bn)?", "a": 6, "unit": "$bn", "tol": 0.1, "hint": "Only the spent part.", "sol": "<b>$6bn</b>."},
  {"q": "Real GDP is $800bn and rises 2.5% after a stimulus. What is the new real GDP ($bn)?", "a": 820, "unit": "$bn", "tol": 0.5, "hint": "800 × 1.025.", "sol": "<b>$820bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an expansionary fiscal measure?", opts: ["A cut in income tax", "A rise in interest rates", "A cut in government spending", "A rise in VAT"], a: 0, why: "Lower taxes raise AD." },
  { q: "Contractionary fiscal policy would be used to:", opts: ["Reduce inflation", "Reduce unemployment", "Raise AD", "Raise the deficit"], a: 0, why: "It lowers AD." },
  { q: "Capital expenditure is:", opts: ["Spending on lasting assets", "Spending on wages", "Benefits", "Interest on debt"], a: 0, why: "Roads, schools, hospitals." },
  { q: "A limit of fiscal policy is:", opts: ["Time lags", "Always works immediately", "No effect on the deficit", "Lowers debt always"], a: 0, why: "Delays." },
  { q: "Expansionary fiscal policy most likely:", opts: ["Raises the budget deficit", "Cuts the national debt", "Reduces AD", "Raises unemployment"], a: 0, why: "More spending, less tax." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Fiscal policy", "Spending and taxes."],
  ["Expansionary", "AD right."],
  ["Contractionary", "AD left."],
  ["Capital spending", "Raises capacity."],
  ["Current spending", "Day-to-day."],
  ["Use in recession", "Expansionary."],
  ["Use in boom", "Contractionary."],
  ["Limits", "Lags, debt, crowding out."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is an example of fiscal policy aimed at increasing aggregate demand in an economy? (Feb/March 2020 · 12 · Q29, reworded)", opts: ["increasing expenditure by firms on skills training programmes for unskilled workers", "increasing the commercial banks' lending ability", "reducing the rate of income tax for all income earners", "reducing the rate of interest on loans to manufacturing companies"], a: 2, why: "A lower rate of income tax is a fiscal policy measure that raises disposable income and spending. The others are firm spending or monetary policy." },
  { q: "What is least likely to rise as a result of the use of expansionary fiscal policy? (Feb/March 2023 · 12 · Q28, reworded)", opts: ["aggregate demand", "budget surplus", "nominal income", "inflation"], a: 1, why: "Higher spending or lower taxes reduce a surplus (or raise the deficit)." },
  { q: "What is most likely to decrease if a government uses expansionary fiscal policy? (May/June 2024 · 11 · Q22, reworded)", opts: ["a balance of payments deficit", "cyclical unemployment", "the level of wages", "the rate of inflation"], a: 1, why: "Higher AD creates jobs and reduces cyclical unemployment." },
  { q: "Which combination of fiscal policy measures will reduce both the inflation rate and income inequality? (subsidies on food and public transport, direct taxes, indirect taxes) (Feb/March 2025 · 12 · Q22, reworded)", opts: ["decrease, decrease, increase", "decrease, increase, increase", "increase, decrease, increase", "increase, increase, decrease"], a: 3, why: "Higher direct taxes and lower indirect taxes cut AD (lower inflation) and are progressive, while higher subsidies help the poor." },
  { q: "Which combination of fiscal and monetary policies is most likely to be effective in the short run for tackling deflation in a closed economy? (fiscal policy, monetary policy) (May/June 2020 · 13 · Q29, reworded)", opts: ["decreasing the budget deficit, decreasing the interest rate", "decreasing the budget deficit, decreasing the money supply", "increasing the budget deficit, decreasing the interest rate", "increasing the budget deficit, decreasing the money supply"], a: 2, why: "A bigger deficit and a lower interest rate both raise AD and so counter deflation." },
  { q: "Which policy will not cause a reduction in the rate of inflation? (May/June 2021 · 12 · Q30, reworded)", opts: ["increasing income tax", "reducing government spending", "reducing interest rates", "removing subsidies"], a: 2, why: "Lower interest rates raise AD. The other policies are contractionary or raise costs." },
  { q: "Which combination correctly classifies an expansionary fiscal measure and its impact on a budget deficit? (fiscal policy, budget deficit) (May/June 2020 · 12 · Q28, reworded)", opts: ["increased quantitative easing, unchanged", "increased welfare spending, increased", "lower income tax, reduced", "lower interest rates, unchanged"], a: 1, why: "Higher welfare spending is fiscal and raises the deficit. Quantitative easing and interest rates are monetary policy, and a lower income tax would raise the deficit." },
  { q: "A government decides to build additional public sector housing to be rented to people receiving low incomes. What is most likely to fall as a result of this increase in public sector housing? (May/June 2021 · 13 · Q17, reworded)", opts: ["employment in the construction industry", "land prices in towns and cities", "rents of houses in the private sector", "total government spending"], a: 2, why: "More public rental housing increases supply of rented homes and lowers private sector rents." },
] });
