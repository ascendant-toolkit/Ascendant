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

const DF = ["The country runs a persistent current account deficit", "More of the currency is supplied than demanded", "The exchange rate falls", "Imports become dearer: imported inflation", "The deficit must be financed by borrowing or selling assets", "Debt and interest payments rise; the government may have to cut spending"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Consequences of a persistent deficit", base: { n: 0 }, draw: mkChain(DF, "--bad"), steps: chainSteps(["The country runs a <b>persistent current account deficit</b>.", "<b>More of the currency is supplied</b> than demanded (imports exceed exports).", "The <b>exchange rate falls</b>.", "Imports become dearer: <b>imported inflation</b>.", "The deficit must be <b>financed</b> by borrowing, selling assets or using reserves.", "<b>Debt and interest payments rise</b>; the government may have to cut spending, slowing growth."]) });
const SF = ["The country runs a persistent surplus", "Foreigners demand more of its currency", "The exchange rate rises", "Exports become dearer; imports cheaper: inflation falls", "Net exports add to AD: GDP and jobs rise", "But exporters may lose competitiveness and the surplus shrinks"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Consequences of a persistent surplus", base: { n: 0 }, draw: mkChain(SF, "--good"), steps: chainSteps(["The country runs a <b>persistent surplus</b>.", "Foreigners <b>demand more of its currency</b>.", "The <b>exchange rate rises</b>.", "Exports become dearer; <b>imports cheaper</b>: inflation falls.", "Net exports add to <b>AD</b>: GDP and jobs rise.", "But exporters may lose competitiveness and <b>the surplus shrinks</b>."]) });
function adChart2(s) {
  const nx = s.nx, c = 90 + 0.8 * nx; let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: Math.abs(nx) > 1 ? 0.4 : 1 } });
  if (Math.abs(nx) > 1) { const [y1, p1] = solveAD(nx); o += adLine(c, nx > 0 ? "c2" : "c4", nx > 0 ? "AD₁" : "AD₂", { t: nx > 0 ? "t2" : "t4" }) + hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, nx > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd"); }
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: Math.abs(nx) > 1 ? 0.45 : 1 });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Net exports and aggregate demand", base: { nx: 0 }, draw: adChart2, steps: [
  { cap: "AD = C + I + G + <b>(X − M)</b>. Net exports are part of aggregate demand.", s: { nx: 0 } },
  { cap: "A current account <b>surplus</b> (exports exceed imports) <b>raises net exports</b>: AD shifts right. Real GDP and jobs rise, and the price level rises.", s: { nx: 14 } },
  { cap: "A <b>deficit</b> reduces net exports: AD shifts <b>left</b>. Real GDP and employment fall, and inflationary pressure eases.", s: { nx: -14 } },
] });

/* Lab 1: financing */
function labF() {
  if (!$("#fa") || !$("#fb") || !$("#fc")) return;
  const def = +$("#fa").value, yrs = +$("#fb").value, rate = +$("#fc").value / 100, gdp = 400; let debt = 0; const ds = [0]; for (let i = 1; i <= yrs; i++) { debt = debt * (1 + rate) + def; ds.push(debt); }
  $("#fa1").textContent = "$" + money(debt, 0) + "bn"; $("#fa2").textContent = money((debt / gdp) * 100, 0) + "%"; $("#fa3").textContent = "$" + money(debt * rate, 1) + "bn";
  $("#fav").textContent = `A deficit of $${def}bn a year for ${yrs} years, financed by borrowing at ${Math.round(rate * 100)}%, builds up foreign debt of $${money(debt, 0)}bn (${money((debt / gdp) * 100, 0)}% of a $${gdp}bn GDP). Interest payments are now $${money(debt * rate, 1)}bn a year, which are a primary income outflow that makes the current account worse. This is why persistent, large deficits are a concern.`;
  const base = 290, mx = Math.max(...ds, 10), k = 220 / mx, w = Math.min(50, 600 / (ds.length + 1)); let o = SV.line(60, base, 700, base);
  ds.forEach((v, i) => { const x = 80 + i * (w + 8), h = Math.max(2, v * k); o += SV.rect(x, base - h, w, h, "", { style: "fill:var(--bad)", opacity: 0.75 }) + SV.text(x + w / 2, base + 18, i, "sm", { "text-anchor": "middle" }); if (i % Math.max(1, Math.floor(ds.length / 8)) === 0 || i === ds.length - 1) o += SV.text(x + w / 2, base - h - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:10px" }); });
  $("#labF").innerHTML = o + SV.text(60, 24, "Foreign debt after each year ($bn)", "sm");
}
Lib.slider($("#g1"), { id: "fa", label: "Current account deficit per year ($bn)", min: 5, max: 40, step: 5, value: 20, fmt: (v) => "$" + v, onInput: labF });
Lib.slider($("#g2"), { id: "fb", label: "Number of years", min: 1, max: 15, step: 1, value: 8, fmt: (v) => v + " years", onInput: labF });
Lib.slider($("#g3"), { id: "fc", label: "Interest rate on the borrowing", min: 1, max: 10, step: 1, value: 4, fmt: (v) => v + "%", onInput: labF });
const EC = [
  { n: "GDP", d: "Net exports reduce AD, so GDP growth may slow; but imported capital goods can raise future output.", s: "Net exports add to AD, so GDP rises." },
  { n: "Employment", d: "Jobs may be lost in industries hit by imports; the government may have to cut demand.", s: "More jobs in export industries." },
  { n: "Inflation", d: "A falling currency raises import prices: imported inflation. Weaker AD may reduce demand-pull pressure.", s: "More demand-pull pressure, but a strong currency lowers import prices." },
  { n: "Exchange rate", d: "More supply of the currency than demand: it tends to fall.", s: "More demand for the currency: it tends to rise." },
  { n: "Financing and reserves", d: "Borrowing, selling assets or using reserves; debt and interest rise.", s: "Reserves and overseas assets grow; the country can lend abroad." },
];
button_table("ecBtns", "ecOut", EC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Persistent deficit</th><th>Persistent surplus</th></tr><tr><td>${p.d}</td><td>${p.s}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each effect more likely with a <b>deficit</b> or a <b>surplus</b>?", buckets: [{ label: "Current account deficit" }, { label: "Current account surplus" }], items: [
  { text: "Downward pressure on the exchange rate", b: 0 }, { text: "Need to borrow or use reserves", b: 0 }, { text: "Lower AD from net exports", b: 0 }, { text: "Risk of imported inflation", b: 0 },
  { text: "Upward pressure on the exchange rate", b: 1 }, { text: "Reserves and overseas assets grow", b: 1 }, { text: "Net exports add to AD and jobs", b: 1 }, { text: "Risk of demand-pull inflation near full capacity", b: 1 },
], done: "Know the effects on AD, the exchange rate, financing and inflation." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>reason a deficit may not be a problem</b> or a <b>reason it is</b>?", buckets: [{ label: "May not be a problem" }, { label: "Is a problem" }], items: [
  { text: "It is small relative to GDP", b: 0 }, { text: "It is caused by imports of machinery that raise future output", b: 0 }, { text: "It is financed by foreign investment", b: 0 }, { text: "It is temporary", b: 0 },
  { text: "It is large and lasts for many years", b: 1 }, { text: "It is financed by borrowing at high interest", b: 1 }, { text: "It puts pressure on the currency to fall", b: 1 }, { text: "It reflects uncompetitive exports", b: 1 },
], done: "Size, duration and cause decide." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Net exports", "Exports minus imports: part of AD"],
  ["Financing a deficit", "Borrowing, selling assets or using reserves to pay for it"],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency"],
  ["Imported inflation", "A rise in prices from dearer imports"],
  ["Persistent deficit", "A deficit lasting for many years"],
  ["Hot money", "Funds that move to earn the highest return"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a persistent deficit could cause a fall in the exchange rate</b>.", items: [
  "Imports exceed exports for many years",
  "Residents sell more of their currency than foreigners buy",
  "Supply of the currency exceeds demand",
  "The exchange rate depreciates",
  "Imports become dearer: inflation may rise",
], done: "The link from a deficit to the exchange rate." });
Lib.calc($("#c1"), { qs: [
  { q: "A deficit of $20bn a year is financed by borrowing for 5 years with no interest. How much foreign debt builds up ($bn)?", a: 100, sol: "20 × 5 = <b>$100bn</b>." },
  { q: "Foreign debt is $120bn and the interest rate is 5%. What are the interest payments ($bn)?", a: 6, sol: "5% × 120 = <b>$6bn</b>." },
  { q: "A country's net exports rise from −$10bn to +$5bn in an economy with GDP $300bn. By what percentage of GDP does AD rise?", a: 5, sol: "15 ÷ 300 × 100 = <b>5%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A current account deficit is most likely to put the exchange rate under pressure to:", opts: ["Rise", "Fall", "Stay the same", "Double"], a: 1, why: "More supply of the currency." },
  { q: "Net exports are part of:", opts: ["Consumption", "Aggregate demand", "Government spending only", "Investment only"], a: 1, why: "AD = C + I + G + (X − M)." },
  { q: "A surplus is most likely to:", opts: ["Reduce AD", "Raise AD", "Reduce reserves", "Cut employment"], a: 1, why: "Net exports add to AD." },
  { q: "A deficit must be financed by:", opts: ["Selling more goods", "Borrowing, selling assets or using reserves", "Raising exports only", "Cutting taxes"], a: 1, why: "Capital must flow in." },
  { q: "A fall in the exchange rate after a deficit could cause:", opts: ["Imported inflation", "Lower import prices", "Fewer exports", "Lower inflation"], a: 0, why: "Dearer imports." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Net exports", "Exports minus imports; part of aggregate demand."],
  ["Financing a deficit", "Paying for a deficit by borrowing, selling assets or using reserves."],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency."],
  ["Imported inflation", "A rise in prices caused by dearer imports, often after a fall in the exchange rate."],
  ["Persistent deficit", "A current account deficit that lasts for many years."],
  ["Debt servicing", "Making interest and capital payments on debts."],
  ["Sustainable deficit", "A deficit that can be financed without causing problems."],
  ["Competitiveness", "How attractive a country's goods are compared with rivals'."],
  ["Hot money", "Short-term funds that move between countries seeking higher returns."],
] });
labF(); 
