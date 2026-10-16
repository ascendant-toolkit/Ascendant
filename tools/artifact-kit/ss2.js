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

const SKILL = ["The government funds more education and training", "Workers gain skills and qualifications", "Labour becomes more productive and more mobile", "Firms can produce more per worker; skill gaps narrow", "AS shifts right: more output and lower unemployment, after a lag"];
const INCENT = ["The government cuts income tax and trims unemployment benefit", "Take-home pay from working rises relative to benefits", "More people look for work or work longer hours", "Firms have more workers to hire; costs may fall", "AS shifts right: more output and employment"];
const EFFIC = ["The government privatises a firm and deregulates the market", "Private owners seek profit and face competition", "Firms cut waste and costs, and new firms enter", "Prices may fall and quality and choice may rise", "Productivity and AS rise; the sale also raises revenue"];
Lib.stepper($("#stK"), { w: 760, h: 400, label: "Education and training", base: { n: 0 }, draw: mkChain(SKILL, "--good"), steps: chainSteps(["Step 1: the government <b>funds education and training</b>.", "Workers gain <b>skills and qualifications</b>.", "Labour is <b>more productive and more mobile</b>: workers can move into vacancies.", "Firms can produce more per worker, and <b>structural unemployment</b> may fall.", "<b>AS shifts right</b>. <b>Evaluate:</b> it takes years, costs money and only works if the skills match employers' needs."]) });
Lib.stepper($("#stI"), { w: 760, h: 400, label: "Lower taxes and better incentives", base: { n: 0 }, draw: mkChain(INCENT, "--accent"), steps: chainSteps(["The government <b>cuts income tax</b> and reduces unemployment benefit.", "<b>Take-home pay from working rises</b> compared with life on benefits.", "More people <b>look for work or work longer</b>.", "Firms find it easier to hire, and <b>labour costs may fall</b>.", "<b>AS shifts right.</b> <b>Evaluate:</b> some people may not change behaviour, revenue may fall, and cutting benefits can hurt the poor and reduce spending."]) });
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Privatisation and deregulation", base: { n: 0 }, draw: mkChain(EFFIC, "--warn"), steps: chainSteps(["The government <b>privatises</b> a state-owned firm and <b>deregulates</b> the market.", "The firm now has <b>private owners seeking profit</b> and faces competition.", "Firms <b>cut waste and costs</b>; new firms can enter the market.", "Prices may fall and quality and choice may rise.", "<b>Productivity and AS rise</b>. <b>Evaluate:</b> a private monopoly could charge high prices, and jobs or services may be lost."]) });

/* Lab 1: is it worth working */
function labW() {
  if (!$("#wa") || !$("#wb")) return;
  const t = +$("#wa").value, b = +$("#wb").value, take = 400 * (1 - t / 100), gain = take - b;
  $("#wa1").textContent = "$" + Math.round(take); $("#wa2").textContent = "$" + b; $("#wa3").textContent = (gain >= 0 ? "+$" : "−$") + Math.round(Math.abs(gain));
  $("#wav").textContent = gain < 50 ? "Working pays little more than benefits: there is a weak incentive to take a job, which can keep people unemployed (an unemployment trap)." : gain > 200 ? "Working pays much more than benefits: a strong incentive to work." : "Working pays more than benefits, but the gap is modest.";
  const base = 300, k = 0.6;
  let o = SV.line(100, base, 680, base);
  [["Take-home pay", take, "--accent"], ["Unemployment benefit", b, "--warn"]].forEach(([n, v, c], i) => {
    const x = 170 + i * 250, h = v * k;
    o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  $("#labW").innerHTML = o + SV.text(100, 30, "Per week", "sm");
}
Lib.slider($("#g1"), { id: "wa", label: "Income tax rate on a $400 weekly wage", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labW });
Lib.slider($("#g2"), { id: "wb", label: "Weekly unemployment benefit", min: 0, max: 350, step: 25, value: 150, fmt: (v) => "$" + v, onInput: labW });

/* Lab 2: measure picker */
const MS = [
  { n: "Education and training", how: "Raises skills, productivity and mobility of workers.", as: "Quality of labour: AS shifts right (long run).", gain: "Workers, firms, and the government through tax revenue.", lag: "Slow (years)", catch: "Costly; skills must match jobs." },
  { n: "Infrastructure", how: "Roads, rail, power and broadband cut firms' costs and travel times.", as: "Better capital for all firms: AS shifts right.", gain: "Firms, regions and consumers.", lag: "Slow (years)", catch: "Big cost, borrowing, delays and possible environmental damage." },
  { n: "Labour market reforms", how: "Easier hiring and firing, weaker union power, reduced benefits, help with job search.", as: "More people willing to work and lower labour costs.", gain: "Firms and people who find work.", lag: "Medium", catch: "Job insecurity, lower wages for some, inequality." },
  { n: "Lower direct taxes", how: "Income tax cuts raise take-home pay; corporation tax cuts raise retained profit.", as: "More work effort and more investment.", gain: "Workers, entrepreneurs, firms.", lag: "Medium", catch: "Revenue may fall; high earners gain most; behaviour may not change much." },
  { n: "Deregulation", how: "Removes rules and barriers so new firms can enter.", as: "More competition, lower costs, more output.", gain: "Consumers and new firms.", lag: "Medium", catch: "Less protection for consumers, workers and the environment." },
  { n: "Incentives to work and invest", how: "Tax breaks for investment, grants and subsidies, lower benefits.", as: "More employment, investment and start-ups.", gain: "Firms and workers.", lag: "Medium", catch: "Cost to the government; may not be well targeted." },
  { n: "Privatisation", how: "Sells state firms to private owners who seek profit and face competition.", as: "Lower costs and higher efficiency; sale raises revenue.", gain: "Government (sale), consumers if prices fall, owners.", lag: "Medium", catch: "Private monopolies may raise prices; jobs and services may be lost." },
];
button_table("msBtns", "msOut", MS, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it works</th><th>Effect on AS</th><th>Who gains</th><th>Time lag</th><th>The catch</th></tr><tr><td>${p.how}</td><td>${p.as}</td><td>${p.gain}</td><td>${p.lag}</td><td>${p.catch}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>kind of supply-side measure</b> is each?", buckets: [{ label: "Raise skills (education, training)" }, { label: "Improve incentives (tax, benefits)" }, { label: "Raise efficiency (privatisation, deregulation)" }, { label: "Better capital (infrastructure)" }], items: [
  { text: "Fund apprenticeships", b: 0 }, { text: "Retraining for workers in declining industries", b: 0 },
  { text: "Cut income tax rates", b: 1 }, { text: "Reduce unemployment benefit for those able to work", b: 1 },
  { text: "Sell a state-owned airline", b: 2 }, { text: "Remove licence rules that block new firms", b: 2 },
  { text: "Build a new railway", b: 3 }, { text: "Roll out national broadband", b: 3 },
], done: "Seven measures, four ideas: skills, incentives, efficiency, capital." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>supply-side measure</b> or <b>not</b>?", buckets: [{ label: "Supply-side" }, { label: "Not supply-side" }], items: [
  { text: "Cut corporation tax to encourage investment", b: 0 }, { text: "Privatise the state telephone company", b: 0 }, { text: "Fund training for the unemployed", b: 0 }, { text: "Deregulate bus services", b: 0 },
  { text: "Cut interest rates to boost spending", b: 1 }, { text: "Raise government spending on a stimulus package", b: 1 }, { text: "Allow the exchange rate to fall", b: 1 }, { text: "Raise VAT to cut the deficit", b: 1 },
], done: "Supply-side raises productive capacity; the others work on demand." });
Lib.match($("#m1"), { prompt: "Match the measure to how it raises AS.", pairs: [
  ["Education and training", "Raises skills and productivity of workers"],
  ["Infrastructure spending", "Cuts firms' costs and improves transport and communications"],
  ["Labour market reforms", "Makes hiring easier and raises willingness to work"],
  ["Lower direct taxes", "Raises take-home pay and retained profit"],
  ["Deregulation", "Removes barriers so more firms can compete"],
  ["Privatisation", "Transfers firms to private owners seeking profit"],
], done: "Link each measure to a mechanism." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how lower income tax could raise AS</b>.", items: [
  "The government cuts income tax rates",
  "Take-home pay from working rises",
  "More people choose to work, or work longer hours",
  "The labour force and output potential grow",
  "AS shifts to the right",
], done: "An incentive-based supply-side chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A worker earns $500 a week and pays income tax of 20%. What is take-home pay ($)?", a: 400, sol: "500 × 0.8 = <b>$400</b>." },
  { q: "The tax rate falls to 15%. What is take-home pay now ($)?", a: 425, sol: "500 × 0.85 = <b>$425</b>." },
  { q: "Unemployment benefit is $300 a week. Take-home pay from a job is $420. How much better off is the worker in work ($)?", a: 120, sol: "420 − 300 = <b>$120</b>." },
  { q: "A government sells a state firm for $2bn. The firm made a loss of $0.1bn a year. If the government no longer pays that subsidy, how much does it save in 5 years ($bn)?", a: 0.5, sol: "0.1 × 5 = <b>$0.5bn</b> (plus the $2bn sale revenue)." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which supply-side measure would help to match the skills of workers to job vacancies?", opts: ["Lower interest rates", "Education and training", "Higher VAT", "Higher government spending on benefits"], a: 1, why: "Training raises skills and mobility." },
  { q: "Privatisation is most likely to:", opts: ["Transfer firms to private owners", "Raise government ownership of firms", "Reduce competition by law", "Raise tax rates"], a: 0, why: "State-owned firms are sold to private owners." },
  { q: "Which is deregulation?", opts: ["Removing rules that restrict firms entering a market", "Building new roads", "Cutting income tax", "Raising the minimum wage"], a: 0, why: "Deregulation reduces barriers to competition." },
  { q: "A cut in income tax may be a supply-side measure because it:", opts: ["Reduces the deficit", "May raise the incentive to work", "Reduces productivity", "Raises AD only"], a: 1, why: "More take-home pay can raise labour supply." },
  { q: "Which is a possible disadvantage of privatisation?", opts: ["A private monopoly could raise prices", "Firms always become less efficient", "It always raises government spending", "It reduces the incentive to cut costs"], a: 0, why: "Without competition, private owners may exploit market power." },
  { q: "Which measure is most likely to raise the quality of capital?", opts: ["Spending on infrastructure", "Cutting unemployment benefit", "Cutting the exchange rate", "Raising interest rates"], a: 0, why: "Roads, rail and broadband are capital." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Education and training", "Spending on schools, colleges and training to raise workers' skills and productivity."],
  ["Infrastructure", "The roads, rail, ports, energy and broadband networks an economy relies on."],
  ["Labour market reforms", "Changes to make labour markets more flexible, such as easier hiring and weaker union power."],
  ["Direct tax cuts", "Lower income tax or corporation tax to raise incentives to work and invest."],
  ["Deregulation", "Removing rules and barriers that restrict competition."],
  ["Privatisation", "Selling state-owned firms to private owners."],
  ["Incentive", "A reward that encourages people or firms to act in a particular way."],
  ["Unemployment trap", "When benefits are so close to wages that working pays little more than being unemployed."],
  ["Mobility of labour", "How easily workers can move between jobs, industries or places."],
] });
labW();
