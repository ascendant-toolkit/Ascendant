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

function priceChart(s) {
  const mode = s.mode, yrs = 10, X = (t) => 80 + t * 60, Y = (v) => 330 - (v - 60) * 1.8;
  const vals = [100]; for (let t = 0; t < yrs; t++) { const r = mode === "inf" ? 4 : mode === "dis" ? 8 - 0.6 * t : -3; vals.push(vals[t] * (1 + r / 100)); }
  let o = SV.line(80, 340, 80, 30) + SV.line(80, 340, 700, 340) + SV.text(86, 40, "Price level (index)", "sm") + SV.text(700, 362, "Years", "sm", { "text-anchor": "end" });
  [80, 100, 120, 140, 160].forEach((v) => (o += SV.line(80, Y(v), 700, Y(v), "gr") + SV.text(72, Y(v) + 4, v, "sm", { "text-anchor": "end" })));
  const col = mode === "inf" ? "c2" : mode === "dis" ? "c1" : "c4", t1 = mode === "inf" ? "t2" : mode === "dis" ? "t1" : "t4";
  const n = Math.min(yrs, s.n), pts = []; for (let t = 0; t <= Math.floor(n); t++) pts.push([X(t), Y(vals[t])]);
  if (n > Math.floor(n)) { const t = Math.floor(n), f = n - t; pts.push([X(t + f), Y(vals[t] + (vals[t + 1] - vals[t]) * f)]); }
  if (pts.length > 1) o += SV.path(ptsPath(pts), col, { "stroke-width": 3 });
  pts.forEach((p, i) => (o += SV.circle(p[0], p[1], 4, mode === "inf" ? "dot2" : mode === "dis" ? "dot1" : "dot4")));
  if (s.n >= yrs) o += SV.text(X(yrs) - 6, Y(vals[yrs]) - 12, money(vals[yrs], 0), "lbl bd " + t1, { "text-anchor": "end" });
  o += SV.text(90, 62, mode === "inf" ? "Inflation: prices rise 4% a year" : mode === "dis" ? "Disinflation: inflation falls from 8% to 2%, prices still rise" : "Deflation: prices fall 3% a year", "lbl bd " + t1, { style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stI"), { w: 760, h: 400, label: "Inflation, disinflation and deflation", base: { mode: "inf", n: 0 }, draw: priceChart, steps: [
  { cap: "<b>Inflation:</b> the general price level rises. Here prices rise <b>4% a year</b>, so after 10 years a basket that cost 100 costs about 148.", s: { mode: "inf", n: 10 } },
  { cap: "<b>Disinflation:</b> prices rise by 8%, then 7.4%, then less each year, down to about 2%. The inflation <b>rate falls</b>, but the price level is <b>still rising</b>.", s: { mode: "dis", n: 10 } },
  { cap: "<b>Deflation:</b> the price level <b>falls</b> 3% a year. After 10 years the same basket costs about 74. Falling prices may look good, but they can discourage spending and lead to recession.", s: { mode: "def", n: 10 } },
] });
function powerChart(s) {
  const base = 320, k = 2.4, ys = [0, 5, 10, 15, 20], vs = ys.map((y) => 100 / Math.pow(1.05, y)); let o = SV.line(60, base, 710, base) + SV.text(60, 30, "What $100 buys, as a share of what it buys today (5% inflation)", "sm");
  vs.forEach((v, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 90 + i * 120, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 80, h, "", { style: "fill:var(--bad)", opacity: 0.8 }) + SV.text(x + 40, base - h - 8, money(v, 0) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 40, base + 20, i ? "Year " + ys[i] : "Today", "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stV"), { w: 760, h: 400, label: "Inflation reduces the value of money", base: { n: 0 }, draw: powerChart, steps: [
  { cap: "Today $100 buys one basket of goods.", s: { n: 1 } },
  { cap: "With <b>5% inflation</b> a year, in 5 years prices are about 28% higher, so $100 buys only about <b>78%</b> of the basket.", s: { n: 2 } },
  { cap: "After 10 years it buys about <b>61%</b>.", s: { n: 3 } },
  { cap: "After 20 years it buys under <b>40%</b>. Money that is saved or on a fixed income <b>loses its purchasing power</b>.", s: { n: 5 } },
] });

/* Lab 1 */
function labI() {
  if (!$("#ia") || !$("#ib")) return;
  const r = +$("#ia").value, n = +$("#ib").value, p = 100 * Math.pow(1 + r / 100, n), pp = 100 / Math.pow(1 + r / 100, n);
  $("#ia1").textContent = money(p, 1); $("#ia2").textContent = "$" + money(pp, 1); $("#ia3").textContent = r > 0.05 ? "Inflation" : r < -0.05 ? "Deflation" : "Stable";
  $("#iav").textContent = r > 0 ? `At ${r}% inflation a $100 basket costs $${money(p, 1)} after ${n} years, so $100 buys only the equivalent of $${money(pp, 1)} of goods today: its purchasing power has fallen.` : r < 0 ? `Prices fall ${-r}% a year: the basket costs $${money(p, 1)} after ${n} years and $100 buys the equivalent of $${money(pp, 1)}. Money gains purchasing power, but falling prices can discourage spending.` : "Prices do not change: stable purchasing power.";
  const base = 300, mx = Math.max(100, p), mn = Math.min(100, p), lo = Math.min(60, mn - 5), hi = Math.max(160, mx + 5), Y = (v) => base - ((v - lo) / (hi - lo)) * 250, X = (t) => 80 + (t / n) * 600; const pts = []; for (let t = 0; t <= n; t += n > 12 ? 0.5 : 1) pts.push([X(t), Y(100 * Math.pow(1 + r / 100, t))]);
  let o = SV.line(80, base, 700, base) + SV.line(80, base, 80, 30) + SV.text(86, 40, "Price of a $100 basket", "sm") + SV.line(80, Y(100), 700, Y(100), "dash", { style: "stroke:var(--muted);stroke-width:1.5" });
  o += SV.path(ptsPath(pts), r > 0 ? "c2" : "c4", { "stroke-width": 3 }) + SV.text(X(n) - 4, Y(p) - 10, "$" + money(p, 0), "lbl bd", { "text-anchor": "end" }) + SV.text(700, base + 22, n + " years", "sm", { "text-anchor": "end" });
  $("#labI").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ia", label: "Inflation rate each year", min: -5, max: 15, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g2"), { id: "ib", label: "Number of years", min: 1, max: 20, step: 1, value: 10, fmt: (v) => v + " years", onInput: labI });
const SQ = [
  { n: "Prices: 100, 104, 108, 112", a: "Inflation", w: "The price level is rising by about 4% a year." },
  { n: "Inflation rate: 9%, 6%, 4%, 3%", a: "Disinflation", w: "The rate is falling but each figure is positive, so prices are still rising." },
  { n: "Prices: 100, 98, 96, 94", a: "Deflation", w: "The price level is falling." },
  { n: "Inflation rate: −1%, −2%, −1%", a: "Deflation", w: "Negative inflation means the price level is falling." },
  { n: "Inflation rate rises from 2% to 5%", a: "Higher inflation", w: "Prices still rise, and faster. Not deflation or disinflation." },
  { n: "The price of one product rises 20%", a: "Not inflation", w: "Inflation is about the general price level, not one price." },
];
button_table("sqBtns", "sqOut", SQ, 0, (p) => `<div class="tw"><table class="t"><tr><th>It is</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>inflation</b>, <b>disinflation</b> or <b>deflation</b>?", buckets: [{ label: "Inflation" }, { label: "Disinflation" }, { label: "Deflation" }], items: [
  { text: "Prices rise by 3% a year", b: 0 }, { text: "The price level rises for several years in a row", b: 0 },
  { text: "Inflation falls from 6% to 3%", b: 1 }, { text: "The rate of price rises slows but prices still rise", b: 1 },
  { text: "The price level falls by 2%", b: 2 }, { text: "The inflation rate is −1%", b: 2 },
], done: "Deflation needs prices to fall. A lower inflation rate is disinflation." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Inflation", "A sustained rise in the general price level over time"],
  ["Deflation", "A sustained fall in the general price level"],
  ["Disinflation", "A fall in the rate of inflation: prices still rise"],
  ["Purchasing power", "What a unit of money can buy"],
  ["Hyperinflation", "Extremely rapid inflation"],
  ["Price stability", "Low and stable inflation"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "The price level was 120 last year and is 126 this year. What is the inflation rate (%)?", a: 5, sol: "(126 − 120) ÷ 120 × 100 = <b>5%</b>." },
  { q: "The price level falls from 200 to 190. What is the rate of inflation (%)?", a: -5, sol: "(190 − 200) ÷ 200 × 100 = <b>−5%</b>: deflation." },
  { q: "Inflation is 10% a year. A basket costs $50 today. What will it cost in a year ($)?", a: 55, sol: "50 × 1.10 = <b>$55</b>." },
  { q: "Roughly how many years does it take for prices to double at 5% inflation (70 ÷ rate)?", a: 14, sol: "70 ÷ 5 = <b>14 years</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is inflation?", opts: ["A rise in the price of one good", "A sustained rise in the general price level", "A rise in output", "A fall in unemployment"], a: 1, why: "Inflation is a persistent rise in the general price level." },
  { q: "What is deflation?", opts: ["A fall in the rate of inflation", "A sustained fall in the general price level", "A fall in output", "A rise in interest rates"], a: 1, why: "The price level itself falls." },
  { q: "The inflation rate falls from 8% to 3%. This is:", opts: ["Deflation", "Disinflation", "Hyperinflation", "Stability"], a: 1, why: "Prices still rise, but more slowly." },
  { q: "When there is inflation, the value of money:", opts: ["Rises", "Falls", "Stays the same", "Doubles"], a: 1, why: "Each unit buys less." },
  { q: "Which is not inflation?", opts: ["Rise in the general price level", "Rise in the price of one product only", "Persistent price rises", "Prices rising faster each year"], a: 1, why: "One price is not the general price level." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Inflation", "A sustained rise in the general price level over time."],
  ["Deflation", "A sustained fall in the general price level."],
  ["Disinflation", "A fall in the rate of inflation: prices still rise, but more slowly."],
  ["Inflation rate", "The percentage rise in the price level over a period, usually a year."],
  ["Price level", "The average level of prices in an economy."],
  ["Purchasing power", "The amount of goods and services that a unit of money can buy."],
  ["Hyperinflation", "Extremely rapid inflation, when money loses its value very quickly."],
  ["Price stability", "Low and stable inflation, a macroeconomic aim."],
] });
labI();
