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

/* ---------- labour force bars ---------- */
function lfDraw(s) {
  const Y = (v) => 250 - v * 3; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Millions", "sm");
  const bar = (x, v, c, l, k) => k > 0 ? SV.rect(x, Y(v), 90, 250 - Y(v), c, op(0.65 * k)) + SV.text(x + 45, 270, l, "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 45, Y(v) - 6, v, "lbl bd", { "text-anchor": "middle", ...op(k) }) : "";
  o += bar(80, 80, "f1", "Population", s.a) + bar(200, 56, "f2", "Working age", s.b) + bar(320, 46, "f2", "Labour force", s.c);
  if (s.d > 0) o += SV.rect(440, Y(42), 90, 250 - Y(42), "f1", op(0.65 * s.d)) + SV.rect(440, Y(46), 90, Y(42) - Y(46), "f3", op(0.75 * s.d)) + SV.text(485, 270, "Employed 42 + unemployed 4", "sm", { "text-anchor": "middle", ...op(s.d) });
  if (s.e > 0) o += tag(380, 66, "Unemployment rate = 4 ÷ 46 × 100 = 8.7%", "c3", s.e, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Population, working age, labour force and the split between employed and unemployed">${lfDraw({ a: 1, b: 1, c: 1, d: 1, e: 1 })}</svg>`;
Lib.stepper($("#stU"), { w: 760, h: 290, label: "From population to the unemployment rate", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: lfDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Population</b> of 80 million.", s: { a: 1 } },
  { cap: "<b>Working age</b> population: 56 million. Children and the very old are excluded.", s: { a: 1, b: 1 } },
  { cap: "<b>The labour force</b> is those in work or actively seeking it: 46 million. Students, carers and those who have given up looking are outside it.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Employed</b> 42 million and <b>unemployed</b> 4 million make up the labour force.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>The unemployment rate</b> is the unemployed as a percentage of the labour force: 4 ÷ 46 × 100 = 8.7%.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

function cuDraw(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in AD reduces real output below potential, creating cyclical unemployment">${cuDraw({ a: -20, n: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "A fall in AD creates cyclical unemployment", base: { a: 0, n: 0 }, draw: cuDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Real output is 50, with potential output at 75 (LRAS). Some spare capacity exists.", s: { a: 0, n: 0 } },
  { cap: "<b>A recession.</b> Consumers and firms cut spending, so AD shifts left. Real output falls (to about 40) and firms need fewer workers: <b>cyclical unemployment</b>.", s: { a: -20, n: 1 } },
  { cap: "<b>Recovery.</b> When AD recovers, output rises and cyclical unemployment falls. This is the key difference from structural unemployment, which stays even when demand recovers.", s: { a: 10, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labU() {
  if (!["em", "un", "dc"].every((i) => $("#" + i))) return;
  const e = +$("#em").value, u = +$("#un").value, d = +$("#dc").value, lf = e + u, r = u / lf * 100, r2 = (u + d) / (lf + d) * 100;
  $("#r1").textContent = lf + "m"; $("#r2").textContent = Lib.fmtN(r, 1) + "%"; $("#r3").textContent = Lib.fmtN(r2, 1) + "%";
  $("#rv").textContent = `Labour force = ${e} + ${u} = ${lf} million. Unemployment rate = ${u} ÷ ${lf} × 100 = ${Lib.fmtN(r, 1)}%. The ${d} million discouraged workers who have given up looking are not in the labour force; counting them as unemployed would raise the rate to ${Lib.fmtN(r2, 1)}%, so the official rate understates joblessness.`;
  const Y = (v) => 250 - v * 4; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30);
  [["Employed", e, "f2"], ["Unemployed", u, "f3"], ["Discouraged", d, "f1"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, Y(v), 80, 250 - Y(v), c, op(0.65)) + SV.text(110 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, Y(v) - 6, v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "em", label: "Employed, millions ", min: 20, max: 60, step: 1, value: 42, fmt: (v) => v, onInput: labU });
Lib.slider($("#g2"), { id: "un", label: "Unemployed (seeking work), millions ", min: 0, max: 15, step: 1, value: 4, fmt: (v) => v, onInput: labU });
Lib.slider($("#g3"), { id: "dc", label: "Discouraged workers (stopped looking), millions ", min: 0, max: 10, step: 1, value: 2, fmt: (v) => v, onInput: labU });
labU();

/* ---------- Lab 2 ---------- */
const SIT = [["A graduate searching for a first job", "Frictional", "Short", "Better job information and matching", "Time is needed to search and match; the problem is information and search costs."], ["A coal mine closes in a town with few other employers", "Structural", "Long", "Retraining and help to relocate", "Skills no longer match the jobs available, and workers are occupationally and geographically immobile."], ["Spending falls in a recession and firms cut staff", "Cyclical", "While demand is weak", "Expansionary fiscal or monetary policy", "Demand-deficient: AD has fallen, so output and jobs fall across industries."], ["Fruit pickers lose work after harvest", "Seasonal", "Recurs each year", "Diversify local work, off-season jobs", "Demand for labour depends on the time of year."], ["Robots replace assembly-line workers", "Technological", "Long", "Retraining and investment in new industries", "New technology replaces labour, a form of structural change."], ["A worker rejects an offer to look for better pay", "Frictional", "Short", "Reduce search costs", "Voluntary search between jobs."]];
function showS(i) {
  const [n, t, d, p, why] = SIT[i]; $$("#sB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = t; $("#t2").textContent = d; $("#t3").textContent = p; $("#tv").textContent = `${n}: this is ${t.toLowerCase()} unemployment. ${why}`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f3", { rx: 12, ...op(0.45) }) + SV.text(210, 105, t + " unemployment", "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(210, 170, "Duration: " + d, "sm", { "text-anchor": "middle" });
}
$("#sB").innerHTML = SIT.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
$$("#sB button").forEach((b) => (b.onclick = () => showS(+b.dataset.i)));
showS(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What type of unemployment is it?", buckets: [{"label": "Frictional"}, {"label": "Structural"}, {"label": "Cyclical"}, {"label": "Seasonal"}], items: [{"text": "A graduate searching for the right first job", "b": 0}, {"text": "A steelworks closes and its skills are no longer needed", "b": 1}, {"text": "Jobs are lost across the economy in a recession", "b": 2}, {"text": "Hotel staff laid off after the holiday season", "b": 3}, {"text": "A worker leaves a job to look for a better one", "b": 0}, {"text": "Manufacturing declines as services grow", "b": 1}, {"text": "A fall in AD causes firms to cut output", "b": 2}, {"text": "Fruit pickers out of work in winter", "b": 3}], done: "Frictional: searching. Structural: mismatch after industries decline. Cyclical: lack of demand. Seasonal: time of year." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Unemployment rate", "Unemployed as a percentage of the labour force"], ["Labour force", "Employed plus unemployed"], ["Claimant count", "People claiming unemployment benefit"], ["Labour force survey", "A sample survey of who is looking for work"], ["Discouraged worker", "Someone who has stopped looking for a job"], ["Technological unemployment", "Machines replace workers"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the causes of structural unemployment in order.", items: ["An industry declines or closes", "Workers lose their jobs", "Their skills do not match the jobs available", "They are unable or unwilling to move or retrain quickly", "Unemployment persists for a long period"], done: "Decline plus mismatch plus immobility means long-term unemployment." });
Lib.calc($("#c1"), { qs: [
  {"q": "Employed 38 million, unemployed 2 million. What is the unemployment rate (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "2 ÷ 40.", "sol": "<b>5%</b>."},
  {"q": "The same economy has a working-age population of 52 million. What share of the working-age population is in the labour force (%)?", "a": 76.9, "unit": "%", "tol": 0.2, "hint": "40 ÷ 52.", "sol": "<b>76.9%</b>."},
  {"q": "A further 2 million discouraged workers are counted as unemployed (and as part of the labour force). What is the new rate (%)?", "a": 9.5, "unit": "%", "tol": 0.2, "hint": "4 ÷ 42.", "sol": "<b>9.5%</b>."},
  {"q": "Unemployment falls from 8% to 6% of a labour force of 50 million. How many fewer people are unemployed (millions)?", "a": 1, "unit": "million", "tol": 0.05, "hint": "2% of 50.", "sol": "<b>1 million</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The unemployment rate is the unemployed as a percentage of:", opts: ["The labour force", "The population", "The employed", "The working-age population"], a: 0, why: "The labour force." },
  { q: "Cyclical unemployment is caused by:", opts: ["A lack of aggregate demand", "Skill mismatch", "The time of year", "Job search"], a: 0, why: "Demand-deficient." },
  { q: "Which method of measuring unemployment is based on a survey?", opts: ["The labour force survey", "The claimant count", "The CPI", "GDP"], a: 0, why: "Sample of households." },
  { q: "A discouraged worker is:", opts: ["Not counted as unemployed", "Counted as employed", "Always a claimant", "Part of seasonal unemployment"], a: 0, why: "They have stopped looking." },
  { q: "Which type tends to last longest?", opts: ["Structural", "Frictional", "Seasonal", "Short-term cyclical"], a: 0, why: "Skills mismatch and immobility." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Unemployment rate", "Unemployed ÷ labour force."],
  ["Labour force", "Employed + unemployed."],
  ["Survey", "Labour force survey."],
  ["Claimant count", "Counts benefit claimants."],
  ["Frictional", "Between jobs."],
  ["Structural", "Mismatch after decline."],
  ["Cyclical", "Lack of demand."],
  ["Seasonal / technological", "Time of year / machines."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "To calculate the unemployment rate, the number unemployed is related to which of the following? (Feb/March 2024 · 12 · Q18, reworded)", opts: ["the total adult population aged 18–65", "the number of unemployed who are seeking work", "the total number in full-time employment", "the total population in the labour force"], a: 3, why: "The rate is the number unemployed as a percentage of the labour force." },
  { q: "Asha is currently unemployed. She has been offered a job but has decided to decline the offer and search for a better paid job. Which type of unemployment is this? (May/June 2024 · 11 · Q17, reworded)", opts: ["cyclical", "frictional", "seasonal", "structural"], a: 1, why: "Time spent searching between jobs is frictional unemployment." },
  { q: "An economy's manufacturing share of real GDP fell from 30% in 1990 to 12% in 2023. Which type of unemployment would have resulted from this? (May/June 2025 · 11 · Q18, reworded)", opts: ["cyclical", "frictional", "structural", "voluntary"], a: 2, why: "The decline of a whole industry creates structural unemployment." },
  { q: "The table shows the types of unemployment and their possible solutions: technological (introduce minimum wage legislation), cyclical (raise government spending), frictional (increase advertising of job vacancies), structural (retrain workers). Which combination is not correct? (May/June 2023 · 12 · Q22, reworded)", opts: ["technological: introduce minimum wage legislation", "cyclical: raise government spending", "frictional: increase advertising of job vacancies", "structural: retrain workers"], a: 0, why: "A minimum wage does not solve technological unemployment. Retraining and new investment do." },
  { q: "What is most likely to decrease if a government uses expansionary fiscal policy? (May/June 2024 · 11 · Q22, reworded)", opts: ["a balance of payments deficit", "cyclical unemployment", "the level of wages", "the rate of inflation"], a: 1, why: "Higher AD creates jobs, reducing cyclical unemployment. It may worsen the balance of payments and raise inflation." },
  { q: "What is a cost of negative economic growth? (May/June 2024 · 13 · Q18, reworded)", opts: ["deteriorating balance of payments", "higher inflation", "higher unemployment", "increased pollution"], a: 2, why: "A falling real GDP means falling output and rising unemployment." },
] });
