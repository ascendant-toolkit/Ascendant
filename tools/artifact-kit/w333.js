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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Why skilled workers earn more", base: { n: 0 }, draw: mkChain(["The job needs long training and rare talent", "Few people can do it: supply is low", "Firms value the high productivity: demand is high", "The wage is bid up", "Skilled workers earn more"], "--good"), steps: chainSteps(["The job needs long training and rare talent", "Few people can do it: supply is low", "Firms value the high productivity: demand is high", "The wage is bid up", "Skilled workers earn more"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Why unskilled workers earn less", base: { n: 0 }, draw: mkChain(["Many people can do the job", "Supply of labour is high", "Workers are easily replaced: weak bargaining power", "The wage is low", "Unskilled workers earn less"], "--bad"), steps: chainSteps(["Many people can do the job", "Supply of labour is high", "Workers are easily replaced: weak bargaining power", "The wage is low", "Unskilled workers earn less"]) });
function labA() {
  const ids = ["a0","a1","a2","a3"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const sc = v[0] * 1.2 + v[1] * 1.5 + (11 - v[2]) * 1.5 + v[3] * 0.8, lvl = sc > 28 ? 'High' : sc > 18 ? 'Medium' : 'Low', nm = ['Skills', 'Demand', 'Scarcity of workers', 'Bargaining strength'], contrib = [v[0] * 1.2, v[1] * 1.5, (11 - v[2]) * 1.5, v[3] * 0.8], top = nm[contrib.indexOf(Math.max(...contrib))]; return { r: [sc.toFixed(0), lvl, top], t: 'Skill ' + v[0] + ', demand ' + v[1] + ', supply of workers ' + v[2] + ' and bargaining strength ' + v[3] + ' give a wage score of ' + sc.toFixed(0) + ': likely a ' + lvl.toLowerCase() + ' wage. High demand and scarce skills push wages up; plentiful workers and weak bargaining hold wages down (illustrative model).', bars: nm.map((n, i) => [n, contrib[i], ['--accent', '--good', '--warn', '--bad'][i], contrib[i].toFixed(0)]) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Skill level required (1 low, 10 high)", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Demand for the worker (1 low, 10 high)", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Number of people able to do the job (1 few, 10 many)", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Bargaining strength (1 weak, 10 strong)", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "A heart surgeon", "a": "High", "b": "Rare skills, long training, high demand."}, {"n": "A supermarket cashier", "a": "Low", "b": "Many people can do the job."}, {"n": "A footballer", "a": "Very high", "b": "Scarce talent; huge revenue."}, {"n": "A public sector teacher", "a": "Medium", "b": "Set by government pay scales."}, {"n": "A female employee paid less than a male colleague", "a": "Lower", "b": "Discrimination."}, {"n": "An oil worker", "a": "High", "b": "Risk, skills, high demand."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Pay level</th><th>Main reason</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Which <b>reason</b> explains each wage difference?", buckets: [{"label": "Demand and supply"}, {"label": "Bargaining strength"}, {"label": "Discrimination"}, {"label": "Government policy"}], items: [{"text": "Surgeons are scarce and in high demand", "b": 0}, {"text": "A strong union wins higher pay", "b": 1}, {"text": "Women paid less for the same job", "b": 2}, {"text": "Public sector pay is set by the state", "b": 3}, {"text": "Cleaners are easily replaced", "b": 0}, {"text": "A minimum wage lifts the lowest pay", "b": 3}], done: "Reasons for wage differences." });
Lib.classify($("#cl2"), { prompt: "Is the wage likely to be <b>high</b> or <b>low</b>?", buckets: [{"label": "Higher wage"}, {"label": "Lower wage"}], items: [{"text": "Rare skills and high demand", "b": 0}, {"text": "Strong union", "b": 0}, {"text": "Many workers available", "b": 1}, {"text": "Easily replaced", "b": 1}, {"text": "Discrimination", "b": 1}, {"text": "Long training required", "b": 0}], done: "Think demand and supply." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Skilled worker", "A worker with specialist training"], ["Unskilled worker", "A worker needing little training"], ["Discrimination", "Unfair treatment based on a characteristic"], ["Public sector", "Government-run employment"], ["Private sector", "Employment in privately owned firms"], ["Tertiary sector", "Service industries"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a footballer earns more than a cashier</b>.", items: ["Few people have elite football skills", "Supply of such players is very low", "Clubs and fans value them highly: demand is high", "Clubs bid up wages", "Footballers earn far more than cashiers"], done: "Scarce talent and high demand." });
Lib.calc($("#c1"), { qs: [
  { q: "A surgeon earns $240,000 and a nurse $48,000. How many times larger is the surgeon's pay?", a: 5, sol: "240,000 ÷ 48,000 = <b>5</b>." },
  { q: "A woman earns $40,000 and a man in the same job $44,000. By what percentage is her pay lower than his (nearest whole number)?", a: 9, sol: "4,000 ÷ 44,000 × 100 ≈ <b>9%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Skilled workers usually earn more because:", opts: ["Supply is lower and demand higher", "They work fewer hours", "They have no unions", "Their jobs are unpleasant"], a: 0, why: "Scarce skills." },
  { q: "Which is a reason for wage differences?", opts: ["Weather", "Discrimination", "Gravity", "Tides"], a: 1, why: "Unequal treatment." },
  { q: "Public sector pay is set mainly by:", opts: ["Profit", "The government", "Customers", "Share prices"], a: 1, why: "State pay scales." },
  { q: "A strong union is likely to:", opts: ["Lower wages", "Raise wages", "Remove jobs", "Ban work"], a: 1, why: "Higher bargaining power." },
  { q: "Unskilled wages are low because:", opts: ["Few people can do the work", "Many people can do the work", "Training is long", "Demand is high"], a: 1, why: "Easily replaced." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Skilled worker", "A worker with specialist training."],
  ["Unskilled worker", "A worker needing little training."],
  ["Discrimination", "Unfair treatment based on a personal characteristic."],
  ["Bargaining strength", "The power to negotiate better pay."],
  ["Public sector", "Government-run employment."],
  ["Private sector", "Employment in privately owned firms."],
  ["Primary sector", "Extracting raw materials."],
  ["Secondary sector", "Manufacturing."],
  ["Tertiary sector", "Services."],
] });
labA(); 
