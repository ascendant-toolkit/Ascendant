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

function rateChart(s) {
  const base = 330, k = 17, w = 160; let o = SV.line(60, base, 700, base);
  const L = s.l, U = s.u, h = L * k, hu = Math.max(U * k, 4);
  o += SV.rect(130, base - h, w, h - hu, "", { style: "fill:var(--good)", opacity: 0.8 }) + SV.rect(130, base - hu, w, hu, "", { style: "fill:var(--bad)", opacity: 0.9 });
  o += SV.text(130 + w / 2, base - h - 10, "Labour force " + money(L, 1) + "m", "lbl bd", { "text-anchor": "middle" });
  if (s.show) o += SV.text(130 + w + 14, base - hu / 2 + 4, "Unemployed " + money(U, 2) + "m", "lbl bd t2");
  if (s.f) o += SV.text(380, 60, "Unemployment rate = " + money(U, 2) + " ÷ " + money(L, 1) + " × 100 = " + money((U / L) * 100, 1) + "%", "lbl bd t3", { style: "font-size:18px" });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Calculating the unemployment rate", base: { l: 14, u: 0.56, show: 0, f: 0 }, draw: rateChart, steps: [
  { cap: "Australia's <b>labour force</b> in 2021 was <b>14.0 million</b>: everyone in work or looking for work.", s: { l: 14, u: 0.56, show: 0, f: 0 } },
  { cap: "Of these, <b>0.56 million</b> had no job but were willing, able and looking: the <b>unemployed</b>.", s: { l: 14, u: 0.56, show: 1, f: 0 } },
  { cap: "<b>Unemployment rate = 0.56 ÷ 14.0 × 100 = 4%</b>.", s: { l: 14, u: 0.56, show: 1, f: 1 } },
  { cap: "The 2026 forecast: labour force <b>14.8m</b>, unemployed <b>0.62m</b>. The rate is about <b>4.2%</b>: slightly higher, even though the labour force grew.", s: { l: 14.8, u: 0.62, show: 1, f: 1 } },
] });
function methodChart(s) {
  const base = 330, k = 260, bars = [["Labour Force Survey", 0.56, "--accent", clamp(s.n, 0, 1)], ["Claimant count", 0.4, "--warn", clamp(s.n - 1, 0, 1)]]; let o = SV.line(60, base, 700, base);
  bars.forEach(([n, v, c, op], i) => { if (op <= 0) return; const x = 150 + i * 250, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 2) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  if (s.n > 2) o += SV.text(380, 40, "The gap: unemployed people not claiming benefit", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "Two measures of unemployment", base: { n: 0 }, draw: methodChart, steps: [
  { cap: "The <b>Labour Force Survey</b> asks a sample of households about work and job search. It estimates <b>0.56 million</b> unemployed.", s: { n: 1 } },
  { cap: "The <b>claimant count</b> only counts people claiming unemployment benefit: <b>0.40 million</b>.", s: { n: 2 } },
  { cap: "The claimant count is lower because some unemployed people <b>are not eligible or do not claim</b> (for example young people or partners of earners). Some claimants may also be working. The LFS is usually the better measure.", s: { n: 3 } },
] });

/* Lab 1: discouraged workers */
function labD() {
  if (!$("#da") || !$("#db") || !$("#dc")) return;
  const L = +$("#da").value, U = +$("#db").value, d = +$("#dc").value, Ud = Math.max(0, U - d), Ld = L - d, r0 = (U / L) * 100, r1 = (Ud / Ld) * 100;
  $("#da1").textContent = money(r0, 1) + "%"; $("#da2").textContent = money(r1, 1) + "%"; $("#da3").textContent = money(d, 2) + "m";
  $("#dav").textContent = d === 0 ? `Unemployment rate = ${money(U, 2)} ÷ ${money(L, 1)} × 100 = ${money(r0, 1)}%. Now slide the discouraged workers up.` : `If ${money(d, 2)}m unemployed people give up looking, they leave the labour force. The official rate falls from ${money(r0, 1)}% to ${money(r1, 1)}% even though not one new job has been created. This is hidden unemployment.`;
  const base = 300, k = 14; let o = SV.line(60, base, 700, base);
  [["Rate if they keep looking", r0, "--bad"], ["Official rate", r1, "--accent"]].forEach(([n, v, c], i) => { const x = 160 + i * 260, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g1"), { id: "da", label: "Labour force (millions)", min: 10, max: 20, step: 0.5, value: 14, fmt: (v) => v + "m", onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "Unemployed (millions)", min: 0.2, max: 2, step: 0.02, value: 0.8, fmt: (v) => v.toFixed(2) + "m", onInput: labD });
Lib.slider($("#g3"), { id: "dc", label: "Unemployed who give up looking (millions)", min: 0, max: 0.4, step: 0.02, value: 0, fmt: (v) => v.toFixed(2) + "m", onInput: labD });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a feature of the <b>Labour Force Survey</b> or the <b>claimant count</b>?", buckets: [{ label: "Labour Force Survey" }, { label: "Claimant count" }], items: [
  { text: "Asks a sample of households about work and job search", b: 0 }, { text: "Follows an international (ILO) definition", b: 0 }, { text: "Includes unemployed people who do not claim benefit", b: 0 }, { text: "Based on a sample, so there are sampling errors", b: 0 },
  { text: "Counts people claiming unemployment benefit", b: 1 }, { text: "Cheap and quick, from official records", b: 1 }, { text: "Misses unemployed people who are not eligible", b: 1 }, { text: "Changes when benefit rules change", b: 1 },
], done: "Know both measures and a for/against of each." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Unemployment rate", "Number unemployed as a percentage of the labour force"],
  ["Labour Force Survey", "A household survey of people's work and job search"],
  ["Claimant count", "The number of people claiming unemployment benefit"],
  ["Hidden unemployment", "People who would work but have stopped looking"],
  ["Underemployment", "Working fewer hours than wanted or in a job below one's skills"],
  ["Discouraged worker", "A jobseeker who has given up looking after failing to find work"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "0.56 million are unemployed in a labour force of 14.0 million. Calculate the unemployment rate (%). (Australia, past paper)", a: 4, sol: "0.56 ÷ 14 × 100 = <b>4%</b>." },
  { q: "A country has 2.4 million unemployed and a labour force of 20 million. What is the unemployment rate (%)?", a: 12, sol: "2.4 ÷ 20 × 100 = <b>12%</b>." },
  { q: "The unemployment rate is 8% and the labour force is 25 million. How many people are unemployed (millions)?", a: 2, sol: "8% × 25m = <b>2 million</b>." },
  { q: "Unemployment rises from 1.0 million to 1.2 million in a labour force of 20 million. By how many percentage points does the unemployment rate rise?", a: 1, sol: "From 5% to 6%: <b>1 percentage point</b>." },
  { q: "The unemployment rate is 24% in a labour force of 10 million. How many are unemployed (millions)?", a: 2.4, sol: "24% × 10m = <b>2.4 million</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Unemployment rate is calculated as:", opts: ["Unemployed ÷ population × 100", "Unemployed ÷ labour force × 100", "Employed ÷ labour force × 100", "Unemployed ÷ employed × 100"], a: 1, why: "The denominator is the labour force." },
  { q: "Which method counts only people receiving benefit?", opts: ["Labour Force Survey", "Claimant count", "Census", "Household budget"], a: 1, why: "The claimant count uses benefit records." },
  { q: "Which is a limitation of the claimant count?", opts: ["It misses unemployed people not claiming benefit", "It uses a sample", "It follows ILO rules", "It counts students"], a: 0, why: "Not everyone unemployed claims." },
  { q: "The unemployment rate falls because discouraged workers leave the labour force. This is an example of:", opts: ["Falling hidden unemployment", "Hidden unemployment hiding the true level", "Full employment", "Cyclical unemployment"], a: 1, why: "The figure falls without more jobs." },
  { q: "Which statement is correct?", opts: ["The Labour Force Survey is based on a sample of households", "The claimant count is based on a sample", "Both count students", "Neither uses a definition"], a: 0, why: "The LFS surveys a sample." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Unemployment rate", "The number of unemployed as a percentage of the labour force."],
  ["Labour Force Survey", "A survey of households that measures employment and unemployment using an international definition."],
  ["Claimant count", "The number of people claiming unemployment benefit."],
  ["Labour force", "The employed plus the unemployed."],
  ["Hidden unemployment", "People who would work but have stopped looking, so are not counted."],
  ["Discouraged worker", "A jobseeker who has given up looking for work."],
  ["Underemployment", "Working fewer hours than wanted or in a job below one's skills."],
  ["ILO", "The International Labour Organization, which defines unemployment for international comparison."],
] });
labD();
