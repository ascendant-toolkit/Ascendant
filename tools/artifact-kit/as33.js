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
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, "P1", "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, "P2", "Q2", g * n);
  return o;
}

/* ---------- free provision ---------- */
function fpDraw(s) {
  const cap = 50, p = s.p, qd = Math.max(0, (90 - p) / 0.8); let o = axes(70, 270, 720, 25, "Treatments", "Price charged");
  o += SV.line(SDX(0), SDY(90), SDX(100), SDY(10), "c2", { "stroke-width": 3 }) + tag(SDX(100) + 4, SDY(10) - 4, "Demand", "c2") + SV.line(SDX(cap), SDY(0), SDX(cap), SDY(100), "c1", { "stroke-width": 3 }) + tag(SDX(cap) + 6, SDY(98), "Capacity (supply)", "c1");
  o += SV.line(70, SDY(p), SDX(Math.max(qd, cap)), SDY(p), "dash") + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.circle(SDX(cap), SDY(p), 6, "dot1") + SV.text(62, SDY(p) + 4, "$" + Lib.fmtN(p, 0), "sm", { "text-anchor": "end" });
  if (qd - cap > 1) o += SV.rect(SDX(cap), SDY(p) - 8, SDX(qd) - SDX(cap), 16, "f3", op(0.7)) + tag(SDX(qd) + 8, SDY(p) - 12, "waiting list " + Lib.fmtN(qd - cap, 0), "c3");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="At a price of zero, demand exceeds fixed capacity so there is a waiting list">${fpDraw({ p: 0 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 300, label: "A service with fixed capacity, priced and then free", base: { p: 50 }, draw: fpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>With a market price of $50</b> demand equals the capacity of 50 treatments. The service clears with no waiting list.", s: { p: 50 } },
  { cap: "<b>The price is cut to $25.</b> Quantity demanded rises to 81 but capacity is fixed at 50, so a waiting list of 31 appears.", s: { p: 25 } },
  { cap: "<b>Free at the point of use ($0).</b> Quantity demanded rises to 112, over twice capacity. With no price to ration, <b>waiting lists</b> or other rules decide who is treated, and taxpayers meet the cost.", s: { p: 0 } },
] });

/* ---------- information ---------- */
function infDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Information about a demerit good shifts demand to the left, lowering price and quantity">${infDraw({ d: -20, n: 1 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 300, label: "Information shifts the demand curve", base: { d: 0, n: 0 }, draw: infDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A demerit good.</b> Consumers underestimate the harm, so demand is higher than it would be with full information.", s: { d: 0, n: 0 } },
  { cap: "<b>Health warnings and a campaign</b> raise awareness of the harm. Demand shifts to the <b>left</b>: price and quantity fall.", s: { d: -20, n: 1 } },
  { cap: "<b>For a merit good</b> (such as vaccination) information has the opposite effect: demand shifts to the <b>right</b> and consumption rises.", s: { d: 20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#pr") || !$("#cp")) return;
  const p = +$("#pr").value, cap = +$("#cp").value, qd = (90 - p) / 0.8, wl = Math.max(0, qd - cap), served = Math.min(qd, cap), cost = 30 * served - p * served;
  $("#r1").textContent = Lib.fmtN(qd, 0); $("#r2").textContent = Lib.fmtN(wl, 0); $("#r3").textContent = "$" + Lib.fmtN(cost, 0);
  $("#rv").textContent = wl > 0 ? `At $${p} patients want ${Lib.fmtN(qd, 0)} treatments but capacity is ${cap}, so ${Lib.fmtN(wl, 0)} wait. Taxpayers pay $${Lib.fmtN(cost, 0)} (cost of $30 each minus the $${p} charge). Free provision removes the price rationing, so queues ration instead.` : `At $${p} demand (${Lib.fmtN(qd, 0)}) is within capacity (${cap}), so everyone is treated. Taxpayers pay $${Lib.fmtN(cost, 0)}${p >= 30 ? ", or nothing if the charge covers the cost" : ""}.`;
  const dEnd = cap; let o = axes(70, 270, 720, 25, "Treatments", "Price charged");
  o += SV.line(SDX(0), SDY(90), SDX(100), SDY(10), "c2", { "stroke-width": 3 }) + SV.line(SDX(cap), SDY(0), SDX(cap), SDY(100), "c1", { "stroke-width": 3 }) + SV.line(70, SDY(p), SDX(Math.max(qd, cap)), SDY(p), "dash") + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.text(62, SDY(p) + 4, "$" + p, "sm", { "text-anchor": "end" });
  if (wl > 0.5) o += SV.rect(SDX(cap), SDY(p) - 8, SDX(qd) - SDX(cap), 16, "f3", op(0.7));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pr", label: "Price charged to patients, $ ", min: 0, max: 50, step: 5, value: 0, fmt: (v) => "$" + v, onInput: labF });
Lib.slider($("#g2"), { id: "cp", label: "Capacity of the service, treatments ", min: 30, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labC() {
  if (!$("#rc") || !$("#st")) return;
  const reach = +$("#rc").value / 100, str = +$("#st").value / 100, d = -30 * reach * str, e = sdEq(d, 0), e0 = sdEq(0, 0), dq = (e.q - e0.q) / e0.q * 100;
  $("#t1").textContent = d === 0 ? "None" : "Left " + Lib.fmtN(-d, 1); $("#t2").textContent = "$" + Lib.fmtN(e.p, 1); $("#t3").textContent = Lib.fmtN(e.q, 1);
  $("#tv").textContent = d === 0 ? "The campaign reaches no one or changes no minds, so demand stays put." : `${Lib.fmtN(reach * 100, 0)}% of consumers see the campaign and it changes ${Lib.fmtN(str * 100, 0)}% of their minds, shifting demand left by ${Lib.fmtN(-d, 1)}. Price falls to $${Lib.fmtN(e.p, 1)} and quantity by ${Lib.fmtN(-dq, 1)}%. Information is cheap, but the effect is small unless many people notice it and respond.`;
  $("#labB").innerHTML = sdPlot({ d, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g3"), { id: "rc", label: "Share of consumers reached, % ", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g4"), { id: "st", label: "Share who change their minds, % ", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + "%", onInput: labC });
labC();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Direct provision or information?", buckets: [{"label": "Direct provision"}, {"label": "Provision of information"}], items: [{"text": "State schools funded by taxes", "b": 0}, {"text": "Health warnings on cigarette packs", "b": 1}, {"text": "A public hospital", "b": 0}, {"text": "An anti-smoking advert campaign", "b": 1}, {"text": "A government-run flood barrier", "b": 0}, {"text": "Calorie labels on menus", "b": 1}, {"text": "State-run police service", "b": 0}, {"text": "Education about healthy eating", "b": 1}], done: "Direct provision: the state supplies the good. Information: the state informs consumers so they choose differently." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Direct provision", "The government supplies a good or service itself"], ["Information failure", "Consumers lack or misjudge relevant information"], ["Waiting list", "Rationing when a free service has fixed capacity"], ["Opportunity cost", "Other spending given up to fund provision"], ["Health warning", "Information that shifts demand for a demerit good left"], ["Crowding out", "State provision reducing private investment"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the problem with free provision in order.", items: ["The government provides a service free at the point of use", "The price falls to zero", "Quantity demanded rises above capacity", "A waiting list forms", "Taxpayers meet the cost, which has an opportunity cost"], done: "Free provision removes price rationing, so queues ration instead." });
Lib.calc($("#c1"), { qs: [
  {"q": "A clinic treats 80 patients at a cost of $40 each, charging $10 per visit. What is the cost to taxpayers ($)?", "a": 2400, "unit": "$", "tol": 1, "hint": "(40 − 10) × 80.", "sol": "<b>$2,400</b>."},
  {"q": "At a price of $0, demand is Qd = 112 and capacity is 50. What is the waiting list?", "a": 62, "unit": "", "tol": 0.5, "hint": "112 − 50.", "sol": "<b>62</b>."},
  {"q": "A campaign reduces demand for a demerit good from 200 to 170 units. What is the percentage fall?", "a": 15, "unit": "%", "tol": 0.3, "hint": "30 ÷ 200.", "sol": "<b>15%</b>."},
  {"q": "A government spends $3m on a campaign that cuts consumption by 50 000 units. What is the cost per unit reduction ($)?", "a": 60, "unit": "$", "tol": 0.5, "hint": "3,000,000 ÷ 50,000.", "sol": "<b>$60</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Direct provision means:", opts: ["The government supplies the good itself", "The government taxes a good", "The government sets a price limit", "A firm subsidises output"], a: 0, why: "State supplies." },
  { q: "Provision of information is most likely to correct:", opts: ["Information failure", "A public good", "Income inequality", "Monopoly power"], a: 0, why: "Cause of the problem." },
  { q: "A free service with fixed capacity will tend to create:", opts: ["Waiting lists", "Surpluses", "Lower costs", "Higher prices"], a: 0, why: "Demand exceeds capacity." },
  { q: "Information about a demerit good shifts demand:", opts: ["To the left", "To the right", "Not at all", "Vertically"], a: 0, why: "Harm is better understood." },
  { q: "A valid disadvantage of direct provision is:", opts: ["Opportunity cost", "Lower tax need", "More consumer sovereignty", "More competition"], a: 0, why: "Uses tax money." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Direct provision", "State supplies it."],
  ["Public goods", "Provided because markets will not."],
  ["Merit goods", "Provided to ensure access."],
  ["Free service", "Queues and waiting lists."],
  ["Information", "Corrects information failure."],
  ["Merit: demand", "Shifts right."],
  ["Demerit: demand", "Shifts left."],
  ["Limits", "Slow, cost, may be ignored."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What would be categorised as direct government provision of goods and services? (Feb/March 2020 · 12 · Q16, reworded)", opts: ["a government grant to a firm to provide healthcare services", "a government regulation on the amount of sugar in soft drinks", "a government subsidy to a firm that operates a regional train service", "a government takeover of a local bus service"], a: 3, why: "Direct provision means the government itself supplies the service, as when it takes over a bus service." },
  { q: "What is an example of direct provision by a government? (May/June 2020 · 13 · Q18, reworded)", opts: ["The government introduces a subsidy on renewable fuels to help the environment", "The government introduces a unit tax on cigarettes to discourage consumption", "The government sets a maximum rent on housing to protect tenants", "The government takes over a private library to improve local services"], a: 3, why: "Taking over a library to run it is direct provision. The other options are a subsidy, a tax and a price control." },
  { q: "A government may use a range of methods to intervene in a market to affect both demand and supply. What is a method which will shift the demand curve for a good? (Feb/March 2025 · 12 · Q12, reworded)", opts: ["an indirect tax", "a subsidy", "direct provision", "provision of information"], a: 3, why: "Information changes tastes and awareness, so it shifts demand. Taxes and subsidies shift supply." },
  { q: "The demand and supply curves show healthcare in a private market. What would happen if the government provides the same amount of healthcare free of charge? (Oct/Nov 2020 · 11 · Q16, reworded)", opts: ["Healthcare will become a public good", "Healthcare will no longer have external benefits", "There will be over-consumption of healthcare", "There will need to be rationing"], a: 3, why: "At a zero price quantity demanded exceeds the fixed amount provided, so rationing by other means is needed. It stays a private good." },
  { q: "What would be a valid objection to the government provision of goods and services? (May/June 2022 · 14 · Q15, reworded)", opts: ["There will be an increase in consumer sovereignty", "Only the private sector can provide merit goods", "Tax rates and tax income are likely to fall", "Investment in the private sector might be reduced"], a: 3, why: "State provision can crowd out private investment. It does not increase consumer sovereignty or reduce tax needs." },
] });
