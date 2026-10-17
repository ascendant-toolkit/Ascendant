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

function slDraw(s) { return adasPlot({ a: s.a, s: s.s, l: s.l, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="LRAS and SRAS shifting right, raising output and lowering the price level">${slDraw({ a: 0, s: 15, l: 15, n: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifts right first, then supply shifts right">${slDraw({ a: 10, s: 15, l: 15, n: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "A supply-side policy shifts LRAS and SRAS to the right", base: { a: 0, s: 0, l: 0, n: 0 }, draw: slDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD and SRAS meet at output 50 and price level 50. Potential output (LRAS) is 75.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Supply-side policy.</b> Better training, infrastructure and technology raise productivity and capacity. SRAS and LRAS shift <b>right</b>.", s: { a: 0, s: 15, l: 15, n: 1 } },
  { cap: "<b>The result:</b> real output rises, the price level falls and employment rises. Potential output has increased: long-run economic growth.", s: { a: 0, s: 15, l: 15, n: 1 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 300, label: "The short-run demand effect and the long-run supply effect", base: { a: 0, s: 0, l: 0, n: 0 }, draw: slDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Short run.</b> The government spends on roads and training. This is government spending, so <b>AD shifts right</b> first: output rises but so may the price level.", s: { a: 10, s: 0, l: 0, n: 1 } },
  { cap: "<b>Long run.</b> As workers become more productive and transport improves, <b>SRAS and LRAS shift right</b>. Output rises further and the price level is held down.", s: { a: 10, s: 15, l: 15, n: 1 } },
] });
chainStep("#stU", "Why supply-side policy may not cure cyclical unemployment", ["Unemployment is high because spending has fallen (AD is weak)", "The government provides training to raise skills", "Workers are better qualified, but firms cannot sell more goods", "Firms do not hire, because demand has not risen", "Unemployment stays high: demand-side policy is needed as well"], [
  "<b>Cyclical unemployment:</b> the problem is a lack of demand.", "<b>A supply-side response:</b> improve skills.", "<b>Capacity is not the constraint</b>: sales are.", "<b>No extra jobs</b> without extra demand.", "<b>A mix of policies:</b> raise AD and improve the supply side."]);

function labP() {
  if (!["tr", "in", "rd", "dr"].every((i) => $("#" + i))) return;
  const [t, f, r, d] = ["tr", "in", "rd", "dr"].map((k) => +$("#" + k).value), raw = 0.5 * t + 0.4 * f + 0.5 * r + 0.3 * d, sh = Math.min(25, raw), cost = t + f + r + d * 0.5;
  $("#r1").textContent = Lib.fmtN(sh, 1) + " units right"; $("#r2").textContent = Lib.fmtN(75 + sh, 1); $("#r3").textContent = "$" + Lib.fmtN(cost, 0) + "bn";
  $("#rv").textContent = sh < 0.5 ? "No spending on the tools, so LRAS stays at 75." : `Spending of $${Lib.fmtN(cost, 0)}bn shifts LRAS right by ${Lib.fmtN(sh, 1)} to ${Lib.fmtN(75 + sh, 1)}. The effect takes years and has diminishing returns (it is capped at 25). In the short run the spending also raises AD, so inflation could rise before capacity grows.`;
  $("#labA").innerHTML = adasPlot({ a: 0, s: sh * 0.6, l: sh, g: 1, n: 1 });
}
[["g1", "tr", "Education and training, $bn ", 10], ["g2", "in", "Infrastructure, $bn ", 10], ["g3", "rd", "Technology and R&D support, $bn ", 5], ["g4", "dr", "Deregulation and reforms (effort), index ", 10]].forEach(([el, id, lab, v]) => Lib.slider($("#" + el), { id, label: lab, min: 0, max: 30, step: 5, value: v, fmt: (z) => z, onInput: labP }));
labP();

chooser("h", [
  ["Structural unemployment", "Retraining, mobility, information", "Well suited, but slow", "Time and funding; some demand support", 4],
  ["Cyclical unemployment", "Little direct effect on AD", "Poorly suited", "Fiscal or monetary policy to raise AD", 1],
  ["Cost-push inflation", "Lower unit costs shift SRAS right", "Well suited in the long run", "Short-run measures for urgent cases", 4],
  ["Demand-pull inflation", "Raises capacity over time", "Slow", "Contractionary monetary or fiscal policy", 2],
  ["Low long-run growth", "Raises potential output (LRAS)", "Best suited", "Enough AD to use the capacity", 5],
  ["Current account deficit", "Improves competitiveness", "Slow but addresses the cause", "Exchange rate or expenditure-reducing policy for the short run", 3]
], (it) => `${it[0]}: supply-side policy ${it[1].toLowerCase()}. It is ${it[2].toLowerCase()}. What else may be needed: ${it[3].toLowerCase()}.`, "How well suited supply-side policy is");
chooser("k", [
  ["Time lags", "Capacity takes years to build", "Training and school reform take a generation to work", "Start early; target quick-acting measures", 5],
  ["Cost and opportunity cost", "Money spent here cannot be spent elsewhere", "A low-income country cannot afford large programmes", "Inward investment, private sector partnerships", 5],
  ["Uncertainty", "Results are not guaranteed", "Workers may not take part or skills may not match jobs", "Consult employers; target schemes", 4],
  ["Side effects", "Policies can harm some groups", "Tax cuts widen inequality; deregulation harms consumers", "Safeguards and targeted help", 3],
  ["Weak demand", "Extra capacity needs demand", "No hiring if firms cannot sell", "Combine with fiscal or monetary policy", 4]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. Example: ${it[2].toLowerCase()}. It may be reduced by: ${it[3].toLowerCase()}.`, "How strongly it limits the policy");
Lib.classify($("#cl1"), { prompt: "Short-run demand effect or long-run supply effect?", buckets: [{"label": "Short-run demand effect"}, {"label": "Long-run supply effect"}], items: [{"text": "Government spending on schools raises AD", "b": 0}, {"text": "Workers' skills and productivity rise", "b": 1}, {"text": "Construction of roads creates jobs and income", "b": 0}, {"text": "Firms' unit costs fall", "b": 1}, {"text": "The price level may rise at first", "b": 0}, {"text": "LRAS shifts to the right", "b": 1}, {"text": "Potential output increases", "b": 1}, {"text": "Total spending in the economy rises", "b": 0}], done: "In the short run, spending raises AD; in the long run, productivity and capacity raise AS." });
Lib.classify($("#cl2"), { prompt: "Is supply-side policy well suited or poorly suited?", buckets: [{"label": "Well suited"}, {"label": "Poorly suited"}], items: [{"text": "Structural unemployment", "b": 0}, {"text": "Cyclical (demand-deficient) unemployment", "b": 1}, {"text": "Cost-push inflation", "b": 0}, {"text": "A sudden fall in spending", "b": 1}, {"text": "Low long-run growth", "b": 0}, {"text": "A short-term shortage of demand for exports", "b": 1}], done: "Supply-side policy tackles capacity and structure; it does little when AD is the problem." });
Lib.order($("#o1"), { prompt: "Put the short-run and long-run effects of road and training spending in order.", items: ["The government spends on roads and training", "AD shifts right and output rises", "The price level may rise in the short run", "Productivity and capacity increase over time", "LRAS shifts right and the price level falls"], done: "AD first, then AS." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["LRAS", "Potential output; shifted by supply-side policy"], ["Structural unemployment", "Unemployment from a mismatch of skills or location"], ["Cyclical unemployment", "Unemployment from a lack of aggregate demand"], ["Time lag", "Delay before supply improvements appear"], ["Cost-push inflation", "Inflation from rising costs of production"], ["Potential output", "The maximum sustainable output of the economy"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Potential output is 800 and a supply-side package raises it by 5%. What is the new potential output?", "a": 840, "unit": "", "tol": 0.5, "hint": "800 × 1.05.", "sol": "<b>840</b>."},
  {"q": "Actual output is 760. What is the output gap before the policy (potential minus actual)?", "a": 40, "unit": "", "tol": 0.5, "hint": "800 − 760.", "sol": "<b>40</b>."},
  {"q": "After the policy potential output is 840 and actual output is 800. What is the output gap now?", "a": 40, "unit": "", "tol": 0.5, "hint": "840 − 800.", "sol": "<b>40</b>: capacity has grown, but demand must also grow to use it."},
  {"q": "A government spends $20bn on training and AD rises by 1.5 times that amount in the short run. By how much does AD rise ($bn)?", "a": 30, "unit": "$bn", "tol": 0.5, "hint": "20 × 1.5.", "sol": "<b>$30bn</b>."},
  {"q": "A firm's unit cost is $50 and falls 8% after a productivity gain. What is the new unit cost ($)?", "a": 46, "unit": "$", "tol": 0.1, "hint": "50 × 0.92.", "sol": "<b>$46</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A successful supply-side policy shifts:", opts: ["LRAS to the right", "AD to the right only", "LRAS to the left", "SRAS to the left"], a: 0, why: "More capacity." },
  { q: "In the short run, government spending on training:", opts: ["Raises AD", "Lowers AD", "Raises LRAS immediately", "Has no effect"], a: 0, why: "Government spending is a component of AD." },
  { q: "Supply-side policy is best suited to:", opts: ["Structural unemployment", "Cyclical unemployment", "A sudden fall in AD", "A trade surplus"], a: 0, why: "Skills and mobility." },
  { q: "A limit of supply-side policy is:", opts: ["It takes a long time to work", "It reduces productivity", "It always raises inflation", "It has no cost"], a: 0, why: "Time lags." },
  { q: "Extra capacity is fully used only if:", opts: ["AD is high enough", "Interest rates are zero", "Taxes rise", "Exports fall"], a: 0, why: "Demand must match capacity." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Effect", "Output up, price level down."],
  ["Short run", "Spending raises AD."],
  ["Long run", "LRAS shifts right."],
  ["Suits", "Structural unemployment, cost-push, growth."],
  ["Poor for", "Cyclical unemployment."],
  ["Limits", "Lags, cost, uncertainty, side effects."],
  ["Needs", "Demand to use the capacity."],
  ["Evaluate", "Mix of policies."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A government decides to use supply-side policy to increase long-run aggregate supply (LRAS). What is the most likely reason why this policy tool will not lead to a fall in the price level? (Feb/March 2025 · 12 · Q24, reworded)", opts: ["Aggregate demand will also increase.", "Labour productivity levels will increase.", "Workers will save any extra wages they earn.", "Workers will spend any extra wages on imports."], a: 0, why: "Policies such as spending on training also raise AD, which offsets the downward effect of higher supply on prices." },
  { q: "Under which current conditions will supply-side policy measures be most likely to achieve a country's key macroeconomic goals? (unemployment, price level) (Feb/March 2023 · 12 · Q26, reworded)", opts: ["high, stable", "high, rising", "low, stable", "low, rising"], a: 1, why: "Supply-side policy can reduce unemployment and ease price rises at the same time, so it is most useful when unemployment is high and prices are rising." },
  { q: "Other things being equal, what is most likely to be reduced by falling labour productivity? (Feb/March 2021 · 12 · Q29, reworded)", opts: ["the balance of trade deficit", "the internal value of money", "the level of unemployment", "the rate of domestic inflation"], a: 1, why: "Lower productivity raises unit costs and prices, so the internal value of money falls." },
] });
