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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

$("#pic1").innerHTML = (() => {
  const B = [["State ownership", "Government owns resources and most firms", 20, "f1"], ["Central planning", "Targets and prices set from the centre", 270, "f2"], ["Allocation by plan", "Resources directed, not bought", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="State ownership, central planning and allocation by plan are features of a planned economy">${o}</svg>`;
})();
$("#pic2").innerHTML = (() => {
  const B = [["No price signals", "Planners lack information", 20, "f3"], ["Weak incentives", "Little reward for efficiency", 270, "f3"], ["Result", "Shortages, surpluses, little choice", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="No price signals and weak incentives lead to shortages and surpluses">${o}</svg>`;
})();
const plLab = { x: "Quantity", y: "Price", D1: "Demand", S1: "Cost of supply", P1: "P*", Q1: "Q*" };
function plDraw(q, p, k = 1) {
  const qd = (90 - p) / 0.8; let o = sdPlot({ d: 0, s: 0, g: 1, n: 0 }, plLab);
  o += SV.line(70, SDY(p), 720, SDY(p), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, SDY(p) - 6, "Planned price " + p, "c3", k, "end");
  o += SV.line(SDX(q), 270, SDX(q), SDY(100) + 20, "c4", { "stroke-width": 2.5, "stroke-dasharray": "6 4", ...op(k) }) + SV.text(SDX(q), 286, "Planned output " + q, "sm", { "text-anchor": "middle", ...op(k) });
  const gap = qd - q; if (Math.abs(gap) > 0.5) o += SV.line(SDX(Math.min(qd, q)), SDY(p) + 16, SDX(Math.max(qd, q)), SDY(p) + 16, "c4", { "stroke-width": 3, ...op(k) }) + SV.text(SDX((qd + q) / 2), SDY(p) + 34, (gap > 0 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(gap), 0), "sm", { "text-anchor": "middle", ...op(k) });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 300, label: "The planners' information problem", base: { q: 50, p: 50, k: 0 }, draw: (s) => plDraw(s.q, s.p, s.k), tween: 900, dwell: 5600, steps: [
  { cap: "<b>The market-clearing outcome</b> would be a price of 50 and an output of 50. Planners do not know this.", s: { q: 50, p: 50, k: 0 } },
  { cap: "<b>Planners guess:</b> they set the price at 30 (to keep it affordable) and an output of 30.", s: { q: 30, p: 30, k: 1 } },
  { cap: "<b>At 30, consumers want 75</b> but only 30 are produced: a <b>shortage</b> of 45. Queues and black markets appear.", s: { q: 30, p: 30, k: 1 } },
  { cap: "<b>If planners over-estimate</b> and produce 70 at a price of 60, consumers want only 37.5: a <b>surplus</b> of 32.5 is wasted.", s: { q: 70, p: 60, k: 1 } },
] });
chainStep("#stB", "Why incentives matter", ["Managers and workers are paid whatever the output", "There is no profit or reward for being efficient", "Little effort to cut costs or improve quality", "Low productivity and little innovation", "Output is poorer and consumers have limited choice"], [
  "<b>State ownership</b> removes the profit motive.", "<b>No reward</b> for good performance.", "<b>Quality and cost</b> suffer.", "<b>Innovation</b> is slow.", "<b>The result:</b> shortages and low-quality goods."]);
chainStep("#stC", "The costs and benefits of moving to a market", ["Prices are freed and state firms are privatised", "Competition and private enterprise grow", "Efficiency, choice and innovation improve", "But inefficient state firms close and unemployment rises", "Prices rise and inequality widens; some merit goods are under-provided"], [
  "<b>The transition</b> begins.", "<b>Incentives</b> change.", "<b>Possible long-run gains.</b>", "<b>A short-run cost</b> for workers.", "<b>Other costs:</b> a role for government remains."]);

function labP() {
  if (!["tq", "tp"].every((i) => $("#" + i))) return;
  const q = +$("#tq").value, p = +$("#tp").value, qd = (90 - p) / 0.8, gap = qd - q;
  $("#r1").textContent = Lib.fmtN(qd, 1); $("#r2").textContent = q; $("#r3").textContent = Math.abs(gap) < 0.5 ? "None" : (gap > 0 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(gap), 1);
  $("#rv").textContent = Math.abs(gap) < 0.5 ? `At a price of ${p} consumers want ${Lib.fmtN(qd, 1)}, exactly the planned output: the plan happens to clear the market.` : gap > 0 ? `At a price of ${p} consumers want ${Lib.fmtN(qd, 1)} but only ${q} are produced: a shortage of ${Lib.fmtN(gap, 1)}, with queues, rationing and black markets.` : `At a price of ${p} consumers want only ${qd} but ${q} are produced: a surplus of ${Lib.fmtN(-gap, 1)} that is wasted. Planners have no price signal to tell them.`;
  $("#labA").innerHTML = plDraw(q, p, 1);
}
Lib.slider($("#g1"), { id: "tq", label: "Planned output ", min: 10, max: 80, step: 5, value: 30, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "tp", label: "Planned price ", min: 20, max: 80, step: 5, value: 30, fmt: (v) => v, onInput: labP });
labP();

chooser("h", [
  ["Free provision of essentials", "Strength", "Everyone can access health and education", "Markets provide them only to those who can pay", 4],
  ["Long-term planning of big projects", "Strength", "Resources can be directed to long-term goals", "Markets may neglect projects with distant payoffs", 3],
  ["Greater equality of outcomes", "Strength", "Output is shared more evenly", "Markets reward ability to pay", 4],
  ["No price signals", "Weakness", "Planners cannot match output to preferences, causing shortages and surpluses", "Prices signal scarcity automatically", 5],
  ["Weak incentives", "Weakness", "No profit, so little reward for efficiency or innovation", "Profit motive encourages efficiency", 5],
  ["Limited consumer choice", "Weakness", "Planners decide what is produced", "Consumer spending decides what is produced", 4],
  ["Bureaucracy", "Weakness", "A large administration is costly and slow", "Decentralised decisions respond quickly", 3]
], (it) => `${it[0]}: a ${it[1].toLowerCase()} of planning. ${it[2]}. By contrast, in a market: ${it[3].toLowerCase()}.`, "Importance");
Lib.classify($("#cl1"), { prompt: "Which economic system does it best describe?", buckets: [{"label": "Planned"}, {"label": "Market"}], items: [{"text": "Output targets are set by a central authority", "b": 0}, {"text": "Prices are set by demand and supply", "b": 1}, {"text": "Most firms are owned by the state", "b": 0}, {"text": "Firms aim to make a profit", "b": 1}, {"text": "Resources are directed by an economic plan", "b": 0}, {"text": "Consumer spending decides what is produced", "b": 1}], done: "In a planned economy the state decides and owns most resources; in a market economy price and private firms decide." });
Lib.classify($("#cl2"), { prompt: "Strength or weakness of a planned economy?", buckets: [{"label": "Strength"}, {"label": "Weakness"}], items: [{"text": "Essentials are provided to everyone", "b": 0}, {"text": "Shortages and surpluses arise", "b": 1}, {"text": "Resources can be directed to long-term projects", "b": 0}, {"text": "Little incentive to innovate", "b": 1}, {"text": "Greater equality in distribution", "b": 0}, {"text": "Limited consumer choice", "b": 1}], done: "Strengths: equity, provision of essentials, long-term planning. Weaknesses: no price signals, weak incentives, limited choice." });
Lib.order($("#o1"), { prompt: "Put the effects of a planners' error in order.", items: ["Planners set an output target without price signals", "The target does not match consumers' demand", "Shortages or surpluses arise", "Queues, black markets or wasted output follow"], done: "No price signal, so mismatches." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Planned economy", "The state decides what, how and for whom"], ["Central planning", "Output targets set by a government authority"], ["State ownership", "Government owns the factors of production"], ["Shortage", "Demand exceeds supply at the set price"], ["Surplus", "Supply exceeds demand at the set price"], ["Transition", "The move from a planned to a market economy"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Demand is Q = (90 − P) ÷ 0.8. The planned price is 30. What quantity do consumers want?", "a": 75, "unit": "", "tol": 0.5, "hint": "(90 − 30) ÷ 0.8.", "sol": "<b>75</b>."},
  {"q": "Planned output at that price is 30. What is the shortage?", "a": 45, "unit": "", "tol": 0.5, "hint": "75 − 30.", "sol": "<b>45 units</b>."},
  {"q": "The planned price is 60 and planned output 70. What is the surplus? (Demand at 60 is 37.5.)", "a": 32.5, "unit": "", "tol": 0.5, "hint": "70 − 37.5.", "sol": "<b>32.5 units</b>."},
  {"q": "A plan targets output growth of 5% a year from 200. What is output after one year?", "a": 210, "unit": "", "tol": 0.5, "hint": "200 × 1.05.", "sol": "<b>210</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "In a planned economy resources are allocated by:", opts: ["The state", "Demand and supply", "Consumer choice only", "Private firms"], a: 0, why: "Central planning." },
  { q: "A weakness of a planned economy is:", opts: ["No price signals", "Competition", "Consumer sovereignty", "Profit incentives"], a: 0, why: "Planners lack information." },
  { q: "A strength of a planned economy is:", opts: ["Provision of essentials to all", "Wide consumer choice", "Strong profit incentive", "Rapid response to taste changes"], a: 0, why: "Equity and welfare." },
  { q: "A possible cost of transition to a market is:", opts: ["Structural unemployment", "Lower prices", "Less choice", "More state ownership"], a: 0, why: "State firms close." },
  { q: "Shortages in a planned economy arise because:", opts: ["Planners lack price signals", "Prices rise too fast", "Firms compete too much", "Consumers are too rich"], a: 0, why: "No information about demand." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Planned economy", "State decides and owns."],
  ["Central planning", "Output targets from the centre."],
  ["Strengths", "Equity, essentials, long-term goals."],
  ["Weaknesses", "No signals, weak incentives, little choice."],
  ["Shortage", "Demand above supply."],
  ["Surplus", "Supply above demand."],
  ["Transition", "Planned to market."],
  ["Reality", "No pure planned economy."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a planned economy, what will determine the allocation of scarce resources? (Oct/Nov 2022 · 12 · Q2, reworded)", opts: ["A mixture of private and central decision making", "The decisions of central government", "The forces of demand and supply", "The revenue generated from direct and indirect taxes"], a: 1, why: "In a planned economy the state decides, not the market." },
  { q: "What is the main characteristic of a planned economy? (May/June 2022 · 12 · Q2, reworded)", opts: ["All goods and services are produced by privately-owned firms", "All goods and services are produced by state-owned firms", "Private firms produce private goods and state firms produce public goods", "The price mechanism allocates scarce resources through buyers and sellers"], a: 1, why: "State ownership and state decision making are the main characteristics. Option C describes a mixed economy and D a market economy." },
  { q: "What is least likely to increase as a result of a transition from a planned economy to a free market economy? (Oct/Nov 2023 · 11 · Q4, reworded)", opts: ["Prices of goods and services", "Privately owned resources", "Provision of merit goods", "Structural unemployment"], a: 2, why: "A free market tends to under-provide merit goods; prices, private ownership and structural unemployment are likely to rise." },
] });
