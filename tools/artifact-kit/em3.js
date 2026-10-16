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
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

Lib.stepper($("#stC"), { w: 760, h: 400, label: "Cyclical unemployment", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b> with most people in work.", s: { sh: 0, a: 0 } },
  { cap: "A recession: confidence falls, so <b>AD shifts left</b>. Firms sell less.", s: { sh: -16, a: 0 } },
  { cap: "Real GDP falls to Y₁. Firms need fewer workers and <b>lay people off</b>: <b>cyclical unemployment</b> rises. There are not enough jobs for everyone who wants one.", s: { sh: -16, a: 0 } },
] });
function strChart(s) {
  const base = 320, k = 3.2; let o = SV.line(60, base, 700, base);
  const bars = [["Jobs lost: declining industry", s.l, "--bad", s.a], ["Vacancies: new industry or place", s.v, "--good", s.b], ["Still unemployed", Math.max(0, s.l - Math.min(s.l, s.v * s.m)), "--warn", s.c]];
  bars.forEach(([n, v, c, op], i) => { if (op <= 0.01) return; const x = 90 + i * 210, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 140, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 70, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 70, base + 22, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }) + "</g>"; });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Structural unemployment", base: { l: 60, v: 40, m: 0, a: 0, b: 0, c: 0, t: "" }, draw: strChart, steps: [
  { cap: "A coal mine closes because demand for coal falls: <b>60 jobs are lost</b>.", s: { l: 60, v: 40, m: 0, a: 1, b: 0, c: 0, t: "" } },
  { cap: "Meanwhile a new industry (solar installation) has <b>40 vacancies</b> in another region, needing different skills.", s: { l: 60, v: 40, m: 0, a: 1, b: 1, c: 0, t: "" } },
  { cap: "The miners lack the skills and cannot move easily. <b>No match</b>: all 60 stay unemployed while 40 vacancies go unfilled. This is <b>structural unemployment</b>.", s: { l: 60, v: 40, m: 0, a: 1, b: 1, c: 1, t: "Mismatch: 60 unemployed, 40 vacancies" } },
  { cap: "With <b>retraining and help to move</b> (75% matched), 30 find jobs. Structural unemployment falls to 30. <b>Supply-side policy</b> works on the mismatch.", s: { l: 60, v: 40, m: 0.75, a: 1, b: 1, c: 1, t: "After retraining" } },
] });
function seasonChart(s) {
  const mths = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"], r = [3, 3, 4, 6, 8, 9, 9, 9, 8, 6, 4, 3], base = 320, k = 22; let o = SV.line(50, base, 710, base) + SV.text(50, 30, "Unemployment rate in a ski resort (%)", "sm");
  r.forEach((v, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 70 + i * 52, h = v * k, hot = v >= 7; o += `<g opacity="${op}">` + SV.rect(x, base - h, 38, h, "", { style: `fill:var(${hot ? "--bad" : "--good"})`, opacity: 0.85 }) + SV.text(x + 19, base - h - 6, v, "sm bd", { "text-anchor": "middle" }) + SV.text(x + 19, base + 20, mths[i], "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Seasonal unemployment", base: { n: 0 }, draw: seasonChart, steps: [
  { cap: "In a ski resort <b>winter is the busy season</b>. From January to March resorts, hotels and lifts employ many workers, so unemployment is <b>low (3 to 4%)</b>.", s: { n: 3 } },
  { cap: "In spring and summer the resort is quiet: instructors, lift staff and hotel workers lose their work and <b>unemployment rises to about 9%</b>.", s: { n: 8 } },
  { cap: "Autumn brings the next season and unemployment falls again. This is <b>seasonal unemployment</b>: predictable and temporary, because it depends on the <b>time of year</b>.", s: { n: 12 } },
  { cap: "<b>Evaluate:</b> it is short term and can be planned for, but still costs workers income. Resorts can reduce it by diversifying (summer hiking, conferences).", s: { n: 12 } },
] });

/* Lab 1: mismatch */
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc")) return;
  const l = +$("#ma").value, v = +$("#mb").value, m = +$("#mc").value / 100, matched = Math.min(l, v * m), u = l - matched, unfilled = v - matched;
  $("#ma1").textContent = money(matched, 0); $("#ma2").textContent = money(u, 0); $("#ma3").textContent = money(unfilled, 0);
  $("#mav").textContent = u === 0 ? "Every lost job has been matched to a vacancy: no structural unemployment." : `Of the ${l} jobs lost, only ${money(matched, 0)} workers can fill the ${v} vacancies. ${money(u, 0)} stay unemployed while ${money(unfilled, 0)} vacancies stay empty. The more the skills and locations match, the lower structural unemployment.`;
  $("#labM").innerHTML = strChart({ l, v, m, a: 1, b: 1, c: 1, t: "" });
}
Lib.slider($("#g1"), { id: "ma", label: "Jobs lost in a declining industry", min: 10, max: 100, step: 5, value: 60, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Vacancies in growing industries", min: 10, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Workers able to fill vacancies (skills and location match)", min: 0, max: 100, step: 5, value: 0, fmt: (v) => v + "%", onInput: labM });
const TY = [
  { n: "Frictional", c: "Time to search, imperfect information, new entrants.", t: "Short term", p: "Better job information, job centres, online job boards.", e: "Graduate looking for a first job" },
  { n: "Structural", c: "Industries decline, technology, globalisation, immobile labour.", t: "Long term", p: "Training and retraining, help with relocation, regional policy, education.", e: "Miners after pit closures" },
  { n: "Cyclical", c: "Fall in aggregate demand in a recession.", t: "Medium term, tied to the cycle", p: "Expansionary fiscal and monetary policy.", e: "Car factory layoffs in a slump" },
  { n: "Seasonal", c: "Demand and supply of labour change with the time of year.", t: "Short and predictable", p: "Diversify the local economy, extend the season, retraining for off-season work.", e: "Ski instructors in summer" },
];
button_table("tyBtns", "tyOut", TY, 0, (p) => `<div class="tw"><table class="t"><tr><th>Causes</th><th>Length</th><th>Best response</th><th>Example</th></tr><tr><td>${p.c}</td><td>${p.t}</td><td>${p.p}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of unemployment</b> is each?", buckets: [{ label: "Frictional" }, { label: "Structural" }, { label: "Cyclical" }, { label: "Seasonal" }], items: [
  { text: "A graduate searching for a first job", b: 0 }, { text: "A worker between two jobs", b: 0 },
  { text: "Steelworkers whose plant closed because demand for steel fell", b: 1 }, { text: "Bank clerks replaced by online banking", b: 1 },
  { text: "Factory workers laid off in a recession", b: 2 }, { text: "Builders unemployed because spending has fallen across the economy", b: 2 },
  { text: "Fruit pickers out of work after the harvest", b: 3 }, { text: "Beach hotel staff in the off-season", b: 3 },
], done: "Name the type, then its cause." });
Lib.classify($("#cl2"), { prompt: "What is the <b>cause</b> of each type? Match each cause to the type of unemployment.", buckets: [{ label: "Frictional" }, { label: "Structural" }, { label: "Cyclical" }], items: [
  { text: "People take time to find a new job", b: 0 }, { text: "Poor information about vacancies", b: 0 },
  { text: "Skills do not match the jobs available", b: 1 }, { text: "An industry declines and workers cannot move", b: 1 }, { text: "Technology replaces workers", b: 1 },
  { text: "Aggregate demand falls", b: 2 }, { text: "The economy is in a recession", b: 2 },
], done: "Frictional: search. Structural: mismatch. Cyclical: low demand." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Frictional unemployment", "Temporary unemployment while workers move between jobs"],
  ["Structural unemployment", "Unemployment from a mismatch between workers' skills or location and available jobs"],
  ["Cyclical unemployment", "Unemployment due to a fall in aggregate demand in a recession"],
  ["Seasonal unemployment", "Unemployment due to the time of year"],
  ["Occupational immobility", "Workers lack the skills to move to other jobs"],
  ["Geographical immobility", "Workers find it hard to move to where jobs are"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the decline of an industry causes structural unemployment</b>.", items: [
  "Demand for an industry's product falls",
  "Firms in the industry close or cut output",
  "Workers lose their jobs",
  "Their skills do not suit vacancies elsewhere",
  "They find it hard to move to where the jobs are",
  "Unemployment remains high for a long time",
], done: "Skills and location mismatch." });
Lib.calc($("#c1"), { qs: [
  { q: "In a recession, 800,000 workers are laid off from a labour force of 20 million. By how many percentage points could unemployment rise?", a: 4, sol: "800,000 ÷ 20m × 100 = <b>4 percentage points</b>." },
  { q: "A closing mine puts 500 workers out of work. 200 find jobs in a new industry. How many remain unemployed?", a: 300, sol: "500 − 200 = <b>300</b>." },
  { q: "Unemployment in a resort is 12% in the off-season and 3% in season. What is the percentage point difference?", a: 9, sol: "12 − 3 = <b>9 percentage points</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which type of unemployment is caused by a recession?", opts: ["Frictional", "Structural", "Cyclical", "Seasonal"], a: 2, why: "Demand-deficient unemployment follows a fall in AD." },
  { q: "A worker who has left one job and is looking for another is:", opts: ["Structurally unemployed", "Frictionally unemployed", "Cyclically unemployed", "Seasonally unemployed"], a: 1, why: "Short-term, between jobs." },
  { q: "Unemployment caused by the decline of an industry is:", opts: ["Structural", "Frictional", "Seasonal", "Cyclical only"], a: 0, why: "Skills and location mismatch." },
  { q: "Which type of unemployment is most likely to be reduced by better job information?", opts: ["Frictional", "Structural", "Cyclical", "None"], a: 0, why: "People find jobs faster." },
  { q: "Tourist guides out of work in winter are an example of:", opts: ["Frictional", "Structural", "Cyclical", "Seasonal"], a: 3, why: "It depends on the time of year." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Frictional unemployment", "Temporary unemployment while workers move between jobs."],
  ["Structural unemployment", "Unemployment from a mismatch between skills or location and available jobs."],
  ["Cyclical unemployment", "Unemployment caused by a fall in total demand, often in a recession."],
  ["Seasonal unemployment", "Unemployment that depends on the time of year."],
  ["Technological unemployment", "Unemployment caused by machines or software replacing workers."],
  ["Occupational immobility", "Difficulty moving between jobs because of lack of skills."],
  ["Geographical immobility", "Difficulty moving to where jobs are."],
  ["Demand-deficient unemployment", "Another name for cyclical unemployment."],
  ["Vacancy", "A job opening that an employer wants to fill."],
] });
labM();
