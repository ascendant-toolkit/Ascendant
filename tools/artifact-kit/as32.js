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

const incEq = (m, n, t) => { const q = 50 - t / (m + n), pc = 50 + m * (t / (m + n)); return { q, pc, pp: pc - t, sc: m / (m + n) }; };
function incPlot(x0, w, m, n, t, k, name, o = {}) {
  const X = (q) => x0 + q * (w / 110), Y = (p) => 250 - p * 1.7, e = incEq(m, n, t), ax = Math.abs(t) > 0.05, dEnd = Math.min(100, 50 + 45 / m);
  let s = SV.line(x0, 250, x0 + w, 250) + SV.line(x0, 250, x0, 50) + SV.text(x0 + 6, 46, "Price", "sm") + SV.text(x0 + w, 270, "Quantity", "sm", { "text-anchor": "end" });
  if (name) s += SV.text(x0 + w / 2, 30, name, "lbl bd", { "text-anchor": "middle" });
  s += SV.line(X(0), Y(50 + 50 * m), X(dEnd), Y(50 + m * (50 - dEnd)), "c2", { "stroke-width": 3 }) + tag(X(dEnd) + 4, Y(50 + m * (50 - dEnd)) + 4, "D", "c2");
  s += SV.line(X(0), Y(50 - 50 * n), X(100), Y(50 + 50 * n), "c1", { "stroke-width": 3, ...op(ax && k > 0 ? 0.4 : 1) }) + tag(X(100) + 4, Y(50 + 50 * n), "S", "c1", ax && k > 0 ? 0.4 : 1);
  s += SV.circle(X(50), Y(50), 5, "dot1", op(ax && k > 0 ? 0.6 : 1)) + SV.line(x0, Y(50), X(50), Y(50), "dash", op(0.6)) + SV.line(X(50), Y(50), X(50), 250, "dash", op(0.6)) + SV.text(x0 - 6, Y(50) + 4, "50", "sm", { "text-anchor": "end" });
  if (ax && k > 0) {
    s += SV.line(X(0), Y(50 - 50 * n + t), X(100), Y(50 + 50 * n + t), "c3", { "stroke-width": 3, ...op(k) }) + tag(X(100) + 4, Y(50 + 50 * n + t), t > 0 ? "S + tax" : "S + subsidy", "c3", k);
    const mid = 50;
    s += SV.rect(X(0), Math.min(Y(e.pc), Y(mid)), X(e.q) - X(0), Math.abs(Y(mid) - Y(e.pc)), "f3", op(0.45 * k)) + SV.rect(X(0), Math.min(Y(e.pp), Y(mid)), X(e.q) - X(0), Math.abs(Y(e.pp) - Y(mid)), "f2", op(0.45 * k));
    s += SV.circle(X(e.q), Y(e.pc), 6, "dot3", op(k)) + SV.circle(X(e.q), Y(e.pp), 5, "dot2", op(k)) + SV.line(x0, Y(e.pc), X(e.q), Y(e.pc), "dash", op(k)) + SV.line(x0, Y(e.pp), X(e.q), Y(e.pp), "dash", op(k)) + SV.line(X(e.q), Y(e.pc), X(e.q), 250, "dash", op(k));
    s += SV.text(x0 - 6, Y(e.pc) + 4, Lib.fmtN(e.pc, 1), "sm", { "text-anchor": "end", ...op(k) }) + SV.text(x0 - 6, Y(e.pp) + 4, Lib.fmtN(e.pp, 1), "sm", { "text-anchor": "end", ...op(k) }) + SV.text(X(e.q), 268, Lib.fmtN(e.q, 1), "sm", { "text-anchor": "middle", ...op(k) });
  }
  return s;
}

$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A subsidy shifts supply down, lowering the price consumers pay and raising the price producers receive">${incPlot(70, 640, 0.8, 0.8, -10, 1, "")}</svg>`;
function s1Draw(s) { const e = incEq(0.8, 0.8, -10); return incPlot(70, 640, 0.8, 0.8, -10, s.k, "") + (s.v > 0 ? SV.text(380, 292, "Cost to government = $10 × " + Lib.fmtN(e.q, 1) + " = $" + Lib.fmtN(10 * e.q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.v) }) : ""); }
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A subsidy of $10 per unit", base: { k: 0, v: 0 }, draw: s1Draw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before.</b> The market is in equilibrium at $50 and 50 units.", s: { k: 0, v: 0 } },
  { cap: "<b>A subsidy of $10 per unit</b> lowers each firm's costs. The supply curve shifts down (right) by $10.", s: { k: 1, v: 0 } },
  { cap: "<b>The new equilibrium.</b> Consumers pay $45 (down $5). Producers receive $45 + $10 = $55 (up $5). Quantity rises to 56.25. Here the benefit is shared equally.", s: { k: 1, v: 0 } },
  { cap: "<b>The cost</b> to the government is the subsidy per unit times the quantity: the rectangle between the two prices, over the new quantity.", s: { k: 1, v: 1 } },
] });
function sTwo(s) { return incPlot(30, 330, 1.2, 0.6, -10, s.k, "Inelastic demand (steep)") + incPlot(400, 330, 0.4, 0.6, -10, s.k, "Elastic demand (flat)") + (s.k > 0.5 ? SV.text(195, 288, "Quantity " + Lib.fmtN(incEq(1.2, 0.6, -10).q, 1) + ", cost $" + Lib.fmtN(10 * incEq(1.2, 0.6, -10).q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.k) }) + SV.text(565, 288, "Quantity " + Lib.fmtN(incEq(0.4, 0.6, -10).q, 1) + ", cost $" + Lib.fmtN(10 * incEq(0.4, 0.6, -10).q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.k) }) : ""); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="The same subsidy with inelastic demand and with elastic demand, and the cost of each">${sTwo({ k: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "The same subsidy with inelastic and with elastic demand", base: { k: 0 }, draw: sTwo, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Two markets</b> with the same supply curve. Demand is steep (inelastic) on the left and flat (elastic) on the right.", s: { k: 0 } },
  { cap: "<b>The same $10 subsidy.</b> With <b>elastic</b> demand the price fall brings a bigger rise in quantity (60 units), so the subsidy costs more ($600) and does more to raise consumption. With <b>inelastic</b> demand quantity rises less (55.6 units), the cost is $556, and consumers gain more per unit.", s: { k: 1 } },
] });

function labS() {
  if (!$("#sb") || !$("#dm") || !$("#sn")) return;
  const t = -(+$("#sb").value), m = +$("#dm").value / 10, n = +$("#sn").value / 10, e = incEq(m, n, t), cost = -t * e.q;
  $("#r1").textContent = "$" + Lib.fmtN(e.pc, 1) + " (" + Lib.fmtN(e.pc - 50, 1) + ")"; $("#r2").textContent = "$" + Lib.fmtN(e.pp, 1) + " (+" + Lib.fmtN(e.pp - 50, 1) + ")"; $("#r3").textContent = "$" + Lib.fmtN(cost, 0);
  $("#rv").textContent = t === 0 ? "No subsidy, so nothing changes." : `Of the $${-t} subsidy per unit, consumers gain $${Lib.fmtN(50 - e.pc, 1)} (${Lib.fmtN(e.sc * 100, 0)}%) and producers $${Lib.fmtN(e.pp - 50, 1)} (${Lib.fmtN((1 - e.sc) * 100, 0)}%). Quantity rises from 50 to ${Lib.fmtN(e.q, 1)} and the government pays $${Lib.fmtN(cost, 0)}. ${m > n ? "Demand is steeper than supply, so consumers gain more." : m < n ? "Supply is steeper than demand, so producers gain more." : "The gain is shared equally."}`;
  $("#labA").innerHTML = incPlot(70, 640, m, n, t, 1, "");
}
Lib.slider($("#g1"), { id: "sb", label: "Subsidy per unit, $ ", min: 0, max: 20, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labS });
Lib.slider($("#g2"), { id: "dm", label: "Steepness of demand (3 = flat and elastic, 12 = steep and inelastic) ", min: 3, max: 12, step: 1, value: 8, fmt: (v) => v, onInput: labS });
Lib.slider($("#g3"), { id: "sn", label: "Steepness of supply (3 = flat and elastic, 10 = steep and inelastic) ", min: 3, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labS });
labS();

function labW() {
  if (!$("#eb") || !$("#sx")) return;
  const E = +$("#eb").value, s = +$("#sx").value, k = 1.6, dq = s / k, cost = s * (50 + dq), net = dq * (E - s / 2);
  $("#t1").textContent = Lib.fmtN(dq, 1); $("#t2").textContent = "$" + Lib.fmtN(cost, 0); $("#t3").textContent = (net >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(net), 1);
  $("#tv").textContent = s === 0 ? "No subsidy, so there is no extra consumption and no gain. The best subsidy equals the external benefit, $" + E + "." : `The subsidy raises output by ${Lib.fmtN(dq, 1)} units. Each extra unit brings an external benefit of $${E}, but costs the government a subsidy of $${s} on top of private gains, so the net gain is ${Lib.fmtN(net, 1)}. ${s === E ? "The subsidy equals the external benefit, so the net gain is at its maximum." : s > E ? "The subsidy is larger than the external benefit, so too much is paid and the net gain falls." : "The subsidy is smaller than the external benefit, so it could be raised for a bigger net gain."}`;
  const X = (v) => 40 + v * 17, Y = (v) => 250 - v * 1; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 40) + SV.text(400, 272, "Subsidy per unit", "sm", { "text-anchor": "end" }) + SV.text(46, 36, "Net gain", "sm"), pts = [];
  for (let v = 0; v <= 20; v += 1) pts.push([X(v), Math.min(290, 250 - (v / k) * (E - v / 2) * 2)]);
  o += SV.path("M" + pts.map((p) => p.join(",")).join(" L"), "c2", { fill: "none", "stroke-width": 3 }) + SV.circle(X(s), 250 - dq * (E - s / 2) * 2, 7, "dot3") + SV.line(X(E), 250, X(E), 250 - (E / k) * (E / 2) * 2, "dash") + SV.text(X(E), 268, "best = " + E, "sm", { "text-anchor": "middle" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "eb", label: "External benefit per unit, $ ", min: 4, max: 16, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labW });
Lib.slider($("#g5"), { id: "sx", label: "Subsidy per unit, $ ", min: 0, max: 20, step: 1, value: 6, fmt: (v) => "$" + v, onInput: labW });
labW();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What does a subsidy do?", buckets: [{"label": "Shifts supply right"}, {"label": "Shifts supply left"}, {"label": "Neither"}], items: [{"text": "A grant lowers farmers' costs", "b": 0}, {"text": "An indirect tax on the good", "b": 1}, {"text": "A government payment per unit to producers", "b": 0}, {"text": "A fall in the price of the good itself", "b": 2}, {"text": "Cheaper inputs for producers", "b": 0}, {"text": "A rise in wages", "b": 1}, {"text": "Removing an existing subsidy", "b": 1}, {"text": "Advertising by consumers' groups", "b": 2}], done: "A subsidy lowers costs and shifts supply right. Removing it shifts supply left." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Subsidy", "Payment to producers that lowers costs"], ["Cost of a subsidy", "Subsidy per unit × quantity sold"], ["Merit good", "Under-consumed good that a subsidy may help"], ["Opportunity cost", "Other spending given up to pay for the subsidy"], ["Poor targeting", "Benefits go to people who would have bought anyway"], ["Transfer payment", "Payment to individuals with no output in return"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a subsidy in order.", items: ["The government pays a subsidy per unit", "Producers' costs fall and supply shifts to the right", "The price paid by consumers falls", "Quantity sold rises", "Consumer and producer surplus rise but the government bears the cost"], done: "Subsidy, supply shifts right, price falls, quantity rises." });
Lib.calc($("#c1"), { qs: [
  {"q": "A subsidy of $4 per unit lowers the price from $20 to $17 and quantity rises from 100 to 120. What is the cost to the government ($)?", "a": 480, "unit": "$", "tol": 1, "hint": "4 × 120.", "sol": "<b>$480</b>."},
  {"q": "How much per unit do consumers gain?", "a": 3, "unit": "$", "tol": 0.05, "hint": "20 − 17.", "sol": "<b>$3</b>."},
  {"q": "How much per unit do producers gain?", "a": 1, "unit": "$", "tol": 0.05, "hint": "Subsidy minus the consumers' gain: 4 − 3.", "sol": "<b>$1</b>."},
  {"q": "What percentage of the subsidy goes to consumers?", "a": 75, "unit": "%", "tol": 0.5, "hint": "3 ÷ 4.", "sol": "<b>75%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A subsidy shifts the supply curve:", opts: ["To the right", "To the left", "Not at all", "Vertically upward only"], a: 0, why: "Costs fall." },
  { q: "A subsidy to producers will usually:", opts: ["Lower the price and raise quantity", "Raise the price and lower quantity", "Raise both", "Lower both"], a: 0, why: "Supply moves right." },
  { q: "The cost of a subsidy rises if demand is more:", opts: ["Elastic", "Inelastic", "Unit inelastic", "Fixed"], a: 0, why: "Quantity rises more." },
  { q: "The opportunity cost of a subsidy is:", opts: ["The other spending or tax cuts forgone", "The price fall", "The rise in quantity", "The producer's profit"], a: 0, why: "Best alternative given up." },
  { q: "A subsidy is most justified for a:", opts: ["Merit good with external benefits", "Demerit good", "Free good", "Good with no substitutes"], a: 0, why: "To correct under-consumption." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Subsidy", "Payment that lowers costs."],
  ["Supply", "Shifts right."],
  ["Price", "Consumers pay less."],
  ["Quantity", "Rises."],
  ["Cost", "Subsidy × quantity."],
  ["Elastic demand", "Bigger rise and cost."],
  ["Opportunity cost", "Other spending lost."],
  ["Merit goods", "Main reason to subsidise."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Why do some local governments subsidise the provision of bicycles to encourage their use? (Feb/March 2023 · 12 · Q13, reworded)", opts: ["Consumers are afraid of having car accidents", "Consumers are unable to afford bicycles", "Consumers are not aware of the external benefits of using bicycles", "Consumers ignore the external costs of using bicycles"], a: 2, why: "Cycling brings external benefits that consumers do not fully take into account, a merit good problem." },
  { q: "Which measure would not be part of a government subsidy to protect domestic producers from competition? (May/June 2020 · 12 · Q17, reworded)", opts: ["import quotas", "interest-free loans provided by the government", "reductions in profits (business) taxes", "transfer payments"], a: 0, why: "Quotas restrict imports. They are a protectionist measure, not a subsidy." },
  { q: "What is not a producer subsidy? (May/June 2022 · 13 · Q18, reworded)", opts: ["a grant given to cover losses in an essential industry, such as the rail industry", "a guaranteed minimum price paid to farmers to ensure the long run supply of food", "financial assistance given to a pharmaceutical company to develop a new vaccine", "a payment made to the unemployed to allow them to buy essential goods and services"], a: 3, why: "A payment to unemployed people is a transfer payment, not a subsidy to producers." },
  { q: "What is most likely to increase the quantity of houses supplied? (May/June 2020 · 13 · Q6, reworded)", opts: ["a policy to help house buyers on modest incomes", "a restriction on the level of rent that can be charged", "a rise in the tax on materials used for building houses", "the removal of a subsidy to house builders"], a: 0, why: "Help to buyers raises demand and the price, so quantity supplied rises. A rent limit, a tax and removing a subsidy all cut supply." },
  { q: "What will increase the producer surplus of farmers that grow carrots? (May/June 2022 · 11 · Q6, reworded)", opts: ["a decrease in the demand for carrots", "a decrease in the price of carrot seed", "a decrease in the price of cabbage", "a decrease in the subsidy on carrots"], a: 1, why: "Cheaper seed lowers costs, which raises supply and the producer surplus at a given price." },
  { q: "A government wishes to raise the incomes of farmers without raising the price of food to consumers. Which policy should it use? (May/June 2024 · 11 · Q13, reworded)", opts: ["a maximum price below the market price for food", "a minimum price below the market price for food", "a payment of a subsidy to farmers to produce food", "a release of government food stocks onto the market"], a: 2, why: "A subsidy lifts what farmers receive while the price paid by consumers does not rise." },
  { q: "Which combination of government measures is most likely to increase the consumption of a merit good? (May/June 2023 · 12 · Q16, reworded)", opts: ["effective maximum price and a subsidy to producers", "effective maximum price and an indirect tax on producers", "effective minimum price and a subsidy to producers", "effective minimum price and an indirect tax on producers"], a: 0, why: "A maximum price and a subsidy both push the price consumers pay down, raising consumption." },
] });
