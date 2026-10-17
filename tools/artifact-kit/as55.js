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

/* ---------- Lab 1 ---------- */
function labP() {
  if (!["tr", "in", "rd", "dr"].every((i) => $("#" + i))) return;
  const [t, f, r, d] = ["tr", "in", "rd", "dr"].map((k) => +$("#" + k).value), raw = 0.5 * t + 0.4 * f + 0.5 * r + 0.3 * d, sh = Math.min(25, raw), cost = t + f + r + d * 0.5;
  $("#r1").textContent = Lib.fmtN(sh, 1) + " units right"; $("#r2").textContent = Lib.fmtN(75 + sh, 1); $("#r3").textContent = "$" + Lib.fmtN(cost, 0) + "bn";
  $("#rv").textContent = sh < 0.5 ? "No spending on the tools, so LRAS stays at 75." : `Spending of $${Lib.fmtN(cost, 0)}bn shifts LRAS right by ${Lib.fmtN(sh, 1)} to ${Lib.fmtN(75 + sh, 1)}. The effect takes years and has diminishing returns (it is capped at 25). In the short run the spending also raises AD, so inflation could rise before capacity grows.`;
  $("#labA").innerHTML = adasPlot({ a: 0, s: sh * 0.6, l: sh, g: 1, n: 1 });
}
[["g1", "tr", "Education and training, $bn ", 10], ["g2", "in", "Infrastructure, $bn ", 10], ["g3", "rd", "Technology and R&D support, $bn ", 5], ["g4", "dr", "Deregulation and reforms (effort), index ", 10]].forEach(([el, id, lab, v]) => Lib.slider($("#" + el), { id, label: lab, min: 0, max: 30, step: 5, value: v, fmt: (z) => z, onInput: labP }));
labP();

/* ---------- Lab 2 ---------- */
const PL = [["Education and training", "Human capital", "More skilled, productive workers", "Takes years; may not match skills needed"], ["Infrastructure spending", "Capital and technology", "Lower costs; better access to markets", "High cost; long delay; raises the deficit"], ["Lower income tax", "Incentive", "More work effort and enterprise", "May widen inequality; reduces revenue"], ["Deregulation", "Market reform", "Easier entry, more competition and efficiency", "Weaker consumer or environmental protection"], ["Privatisation", "Market reform", "Profit motive and competition cut costs", "Possible private monopoly power"], ["Cutting benefits for the long-term unemployed", "Incentive", "Encourages people to seek work", "Hardship; may not create jobs"]];
function showP(i) {
  const [n, t, h, d] = PL[i]; $$("#pB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = t; $("#t2").textContent = h; $("#t3").textContent = d; $("#tv").textContent = `${n}: it raises supply through "${h.toLowerCase()}", shifting LRAS right over time. The main drawback is that it ${d.toLowerCase()}.`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f2", { rx: 12, ...op(0.45) }) + SV.text(210, 105, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(210, 170, "Type: " + t, "sm", { "text-anchor": "middle" });
}
$("#pB").innerHTML = PL.map((p, i) => `<button class="b" data-i="${i}">${p[0]}</button>`).join("");
$$("#pB button").forEach((b) => (b.onclick = () => showP(+b.dataset.i)));
showP(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Supply-side policy or not?", buckets: [{"label": "Supply-side"}, {"label": "Demand-side"}], items: [{"text": "Funding apprenticeships", "b": 0}, {"text": "Cutting interest rates", "b": 1}, {"text": "Building new ports", "b": 0}, {"text": "A cut in VAT to boost spending", "b": 1}, {"text": "Tax relief for R&D", "b": 0}, {"text": "Deregulating industries", "b": 0}, {"text": "Higher government spending on benefits", "b": 1}, {"text": "Privatising state industries", "b": 0}], done: "Supply-side policies raise capacity and productivity; demand-side policies change spending." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Supply-side policy", "Measures to increase aggregate supply"], ["LRAS", "Potential output; shifted by supply-side policy"], ["Human capital", "Skills and knowledge of the workforce"], ["Deregulation", "Removing rules to increase competition and efficiency"], ["Privatisation", "Transferring state industries to private ownership"], ["Time lag", "Delay before supply improvements appear"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the long-run effect of training in order.", items: ["The government funds training", "Workers' skills and productivity rise", "Unit costs fall and capacity rises", "LRAS shifts to the right", "Real output rises and the price level falls"], done: "Training raises productivity, shifting LRAS right." });
Lib.calc($("#c1"), { qs: [
  {"q": "Potential output is 800 and a supply-side package raises it by 5%. What is the new potential output?", "a": 840, "unit": "", "tol": 0.5, "hint": "800 × 1.05.", "sol": "<b>840</b>."},
  {"q": "A training programme costs $30m and raises output per worker by $200 for 100,000 workers. What is the extra output ($m)?", "a": 20, "unit": "$m", "tol": 0.1, "hint": "200 × 100,000.", "sol": "<b>$20m</b> a year."},
  {"q": "How many years does it take for the extra output to cover the cost?", "a": 1.5, "unit": "years", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "<b>1.5 years</b>."},
  {"q": "A firm's labour costs are 50% of its costs. Productivity rises 10%, so labour cost per unit falls 9.1%. By roughly how much do total unit costs fall (%)?", "a": 4.5, "unit": "%", "tol": 0.2, "hint": "0.5 × 9.1.", "sol": "<b>4.5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A supply-side policy aims to:", opts: ["Increase aggregate supply", "Reduce aggregate supply", "Raise interest rates", "Cut government spending only"], a: 0, why: "Raise capacity." },
  { q: "Which is a supply-side policy?", opts: ["Spending on education and training", "A cut in interest rates", "A rise in VAT", "A rise in the money supply"], a: 0, why: "Human capital." },
  { q: "Supply-side policy shifts:", opts: ["LRAS to the right", "AD to the right only", "LRAS to the left", "SRAS to the left"], a: 0, why: "More capacity." },
  { q: "A limit of supply-side policy is:", opts: ["It takes a long time to work", "It reduces productivity", "It always raises inflation", "It has no cost"], a: 0, why: "Time lags." },
  { q: "Privatisation may:", opts: ["Increase efficiency through competition", "Lower the quality always", "Raise unemployment always", "Reduce supply"], a: 0, why: "Profit motive." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Supply-side", "Raise AS and LRAS."],
  ["Tools", "Education, infrastructure, tech, incentives, reforms."],
  ["Effect", "Output up, price level down."],
  ["Short run", "Spending raises AD."],
  ["Long run", "LRAS shifts right."],
  ["Limits", "Lags, cost, uncertainty."],
  ["Suits", "Structural unemployment, cost-push."],
  ["Evaluate", "Mix of policies."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What can be considered an expansionary supply-side policy? (Feb/March 2024 · 12 · Q23, reworded)", opts: ["an increase in government expenditure on training", "an increase in sales tax", "an increase in the rate of interest", "an increase of the exchange rate"], a: 0, why: "Training raises productivity and capacity, shifting aggregate supply right." },
  { q: "What is not an example of an expansionary supply-side policy? (May/June 2025 · 11 · Q24, reworded)", opts: ["a reduction in government spending on training", "an increase in support for technological improvement", "a reduction in payments to the unemployed", "an increase in privatisation of industry"], a: 0, why: "Cutting training would reduce skills. The others aim to raise supply." },
  { q: "A government cuts income tax. Why might this be seen as an example of a supply-side policy? (Feb/March 2025 · 12 · Q21, reworded)", opts: ["Real incomes are increased", "The costs of businesses are reduced", "The opportunity cost of unemployment has increased", "The standard of living has improved"], a: 2, why: "Lower income tax raises the reward for working, so the opportunity cost of not working rises, encouraging people into work." },
  { q: "What is most likely to occur when the government privatises public sector organisations? (May/June 2020 · 13 · Q14, reworded)", opts: ["Consumer choice will increase", "Employment will increase in the short run", "Innovation will be discouraged", "The production of public goods will increase"], a: 0, why: "Privatisation usually increases competition and choice." },
  { q: "Which combination identifies a main aim of supply-side policy and a measure used to achieve this target? (main aim, policy measure) (May/June 2021 · 13 · Q28, reworded)", opts: ["economic growth, deregulation", "full employment, increasing the money supply", "income equality, more progressive taxation", "stable prices, decreasing interest rates"], a: 0, why: "Deregulation is a supply-side measure aimed at growth. The others are demand-side or distribution policies." },
  { q: "A country increases its spending on education and training. It pays for this by reducing unemployment benefit payments and increasing taxes on imports of machinery. What is the likely effect of these changes on human capital and physical capital? (May/June 2025 · 12 · Q4, reworded)", opts: ["human capital decreases, physical capital decreases", "human capital decreases, physical capital increases", "human capital increases, physical capital decreases", "human capital increases, physical capital increases"], a: 2, why: "Education and training raise human capital. Taxes on imported machinery make capital goods dearer, so physical capital is likely to fall." },
] });
