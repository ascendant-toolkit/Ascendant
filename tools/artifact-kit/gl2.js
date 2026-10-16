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

const TR = ["Governments cut tariffs and quotas; join trade agreements", "Imports become cheaper and exports face fewer barriers", "Firms sell to bigger markets and source cheaper inputs", "More specialisation and international trade", "Supply chains spread across countries", "Globalisation increases"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Lower trade restrictions", base: { n: 0 }, draw: mkChain(TR, "--accent"), steps: chainSteps(["Governments <b>cut tariffs and quotas</b> and join trade agreements.", "Imports become <b>cheaper</b> and exports face <b>fewer barriers</b>.", "Firms sell to <b>bigger markets</b> and source cheaper inputs.", "There is more <b>specialisation</b> and trade.", "<b>Supply chains</b> spread across countries.", "<b>Globalisation increases</b>. If restrictions rise instead, it slows."]) });
const TC = ["Container ships, big freighters and air freight cut shipping costs", "Internet and mobile networks cut the cost of communicating", "It is cheaper to move goods and coordinate production abroad", "Firms spread production across countries to cut costs", "More goods and services are traded; MNCs expand", "Globalisation increases"];
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Lower transport and communication costs", base: { n: 0 }, draw: mkChain(TC, "--good"), steps: chainSteps(["<b>Container ships, bigger freighters and air freight</b> cut shipping costs.", "The <b>internet and mobile networks</b> cut the cost of communicating.", "It is <b>cheaper to move goods</b> and run production abroad.", "Firms <b>spread production</b> across countries to cut costs.", "More goods and services are <b>traded</b>; MNCs expand.", "<b>Globalisation increases</b>. Higher fuel costs or disruptions can reverse this."]) });
const IN = ["Globalisation raises demand for skilled workers and capital", "Skilled workers and owners see higher pay and profits", "Low-skilled workers face competition from cheaper labour abroad", "Their wages may stagnate or jobs may be lost", "The gap between rich and poor within the country may widen", "Evaluation: gains elsewhere may reduce poverty; policy can share gains"];
Lib.stepper($("#stI"), { w: 760, h: 400, label: "Globalisation and income distribution", base: { n: 0 }, draw: mkChain(IN, "--warn"), steps: chainSteps(["Globalisation raises demand for <b>skilled workers</b> and capital.", "Skilled workers and owners see <b>higher pay and profits</b>.", "<b>Low-skilled workers</b> face competition from cheaper labour abroad.", "Their <b>wages may stagnate</b> or jobs may be lost.", "The <b>gap between rich and poor</b> within the country may widen.", "<b>Evaluate:</b> jobs and incomes rose in developing countries, and taxes and education can share the gains."]) });

/* Lab 1: landed price */
function labL() {
  if (!$("#la") || !$("#lb")) return;
  const c = +$("#la").value, t = +$("#lb").value, price = (50 + c) * (1 + t / 100), qty = Math.max(0, 100 - price), base = (50 + 10) * 1.1, bq = 100 - base;
  $("#la1").textContent = "$" + money(price, 1); $("#la2").textContent = money(qty, 0); $("#la3").textContent = (qty - bq >= 0 ? "+" : "−") + money(Math.abs(qty - bq), 0);
  $("#lav").textContent = `A good costs $50 to make abroad. With transport costs of $${c} and a tariff of ${t}%, the landed price is ($50 + $${c}) × ${1 + t / 100} = $${money(price, 1)}. Consumers import ${money(qty, 0)} units. Lower transport costs or tariffs cut the price and raise trade: that is how they cause globalisation. Raising them does the reverse.`;
  const base0 = 290, k = 2.6; let o = SV.line(60, base0, 700, base0);
  [["Landed price ($)", price, "--warn", 1.5], ["Units imported", qty, "--accent", 2.6]].forEach(([n, v, cc, kk], i) => { const x = 160 + i * 250, h = v * kk; o += SV.rect(x, base0 - h, 150, h, "", { style: `fill:var(${cc})`, opacity: 0.85 }) + SV.text(x + 75, base0 - h - 8, money(v, i ? 0 : 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base0 + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labL").innerHTML = o;
}
Lib.slider($("#g1"), { id: "la", label: "Transport cost per unit", min: 0, max: 30, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Tariff on imports", min: 0, max: 40, step: 5, value: 10, fmt: (v) => v + "%", onInput: labL });
const EF = [
  { n: "International trade", p: "More trade, specialisation, lower prices and choice.", c: "Dependence on other countries; shocks spread quickly." },
  { n: "Competition", p: "Prices fall, quality and innovation rise; consumers gain.", c: "Weaker domestic firms close; jobs lost; large MNCs may dominate." },
  { n: "The environment", p: "Green technology spreads; higher standards in some countries.", c: "More transport emissions, pollution and resource use; production moves to weakly regulated countries." },
  { n: "Migration", p: "Skills reach where needed; migrants earn more and send remittances.", c: "Brain drain from poorer countries; pressure on housing and services." },
  { n: "Income distribution", p: "Jobs and incomes rise in developing countries; poverty may fall.", c: "Gap between skilled and unskilled, rich and poor may widen within countries." },
  { n: "Economic development", p: "FDI, technology and export markets raise growth and development.", c: "Dependence on a few exports or MNCs; benefits may not reach the poor." },
];
button_table("efBtns", "efOut", EF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible positive effects</th><th>Possible negative effects</th></tr><tr><td>${p.p}</td><td>${p.c}</td></tr></table></div>`);
const RV = [
  { n: "Trade war: tariffs rise", e: "Imports dearer, trade falls; firms rethink supply chains.", t: "Slows globalisation" },
  { n: "Oil price spike", e: "Shipping costs rise; long supply chains become dearer.", t: "Slows globalisation" },
  { n: "Pandemic", e: "Borders and factories close; firms hold more local stocks.", t: "Slows globalisation" },
  { n: "New free trade agreement", e: "Tariffs fall; trade between members increases.", t: "Speeds globalisation" },
  { n: "Faster internet and cheaper video calls", e: "Easier to run offices and services abroad.", t: "Speeds globalisation" },
  { n: "A large MNC builds factories abroad", e: "Jobs, technology and exports grow in the host country.", t: "Speeds globalisation" },
];
button_table("rvBtns", "rvOut", RV, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect</th><th>Impact on globalisation</th></tr><tr><td>${p.e}</td><td><b>${p.t}</b></td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each <b>increase</b> or <b>reduce</b> globalisation?", buckets: [{ label: "Increases globalisation" }, { label: "Reduces globalisation" }], items: [
  { text: "Lower tariffs", b: 0 }, { text: "Cheaper shipping", b: 0 }, { text: "Cheaper internet and phone calls", b: 0 }, { text: "MNCs building factories abroad", b: 0 },
  { text: "Higher tariffs and quotas", b: 1 }, { text: "Rising fuel and shipping costs", b: 1 }, { text: "MNCs moving production back home", b: 1 }, { text: "Trade wars", b: 1 },
], done: "Four causes: restrictions, transport, communication, MNCs." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>positive</b> or <b>negative</b> effect of globalisation?", buckets: [{ label: "Positive" }, { label: "Negative" }], items: [
  { text: "Lower prices for consumers", b: 0 }, { text: "More jobs and FDI in developing countries", b: 0 }, { text: "Spread of technology and ideas", b: 0 }, { text: "More choice of goods", b: 0 },
  { text: "Job losses in industries facing imports", b: 1 }, { text: "More pollution from transport", b: 1 }, { text: "Wider gap between skilled and unskilled", b: 1 }, { text: "Brain drain from poorer countries", b: 1 },
], done: "Always weigh both sides." });
Lib.match($("#m1"), { prompt: "Match the cause to how it increases globalisation.", pairs: [
  ["Lower tariffs and quotas", "Imports cheaper and exports face fewer barriers"],
  ["Cheaper transport", "Cost of moving goods falls, so more is traded"],
  ["Cheaper communication", "Easier to coordinate production and sell abroad"],
  ["MNCs moving abroad", "FDI, technology and supply chains spread"],
  ["Trade agreements", "Countries agree to cut barriers"],
  ["Container shipping", "Goods moved cheaply in standard boxes"],
], done: "Link each cause to the effect." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how cheaper transport increases trade</b>.", items: [
  "Shipping and air freight costs fall",
  "The cost of getting goods to foreign markets falls",
  "Imports and exports become cheaper",
  "Firms sell more abroad and buy more inputs abroad",
  "International trade rises: globalisation increases",
], done: "A cause chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A good costs $40 to make and $10 to ship. A 20% tariff is charged on the total. What is the landed price ($)?", a: 60, sol: "(40 + 10) × 1.2 = <b>$60</b>." },
  { q: "Shipping costs fall from $10 to $4 on a good that costs $40. By what percentage does the shipped price fall (1 d.p.)?", a: 12, sol: "From $50 to $44: 6 ÷ 50 × 100 = <b>12%</b>." },
  { q: "A firm's exports to a market rise from 200 to 260 units after tariffs are cut. By what percentage did exports rise?", a: 30, sol: "60 ÷ 200 × 100 = <b>30%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a cause of globalisation?", opts: ["Higher tariffs", "Lower transport costs", "Higher shipping costs", "Fewer MNCs"], a: 1, why: "Cheaper movement of goods." },
  { q: "Globalisation is most likely to cause:", opts: ["Less competition", "More competition between firms", "Fewer exports", "Less migration"], a: 1, why: "Firms face foreign rivals." },
  { q: "Which is a possible negative effect of globalisation on the environment?", opts: ["More green technology", "More transport pollution", "Fewer emissions", "Less resource use"], a: 1, why: "More shipping and production." },
  { q: "Which could widen income inequality within a country?", opts: ["Falling demand for skilled workers", "Greater competition for low-skilled workers from abroad", "A rise in the minimum wage", "More tax on the rich"], a: 1, why: "Unskilled wages may stagnate." },
  { q: "An increase in tariffs would most likely:", opts: ["Speed up globalisation", "Slow globalisation", "Reduce all prices", "Increase migration"], a: 1, why: "Trade becomes dearer." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Trade restrictions", "Measures such as tariffs and quotas that limit trade."],
  ["Transport costs", "The cost of moving goods between countries."],
  ["Communication costs", "The cost of sending information between countries."],
  ["Brain drain", "The emigration of skilled and educated workers."],
  ["Remittances", "Money sent home by migrants working abroad."],
  ["Income distribution", "How a country's income is shared among its people."],
  ["Competition", "Rivalry between firms for customers."],
  ["Trade agreement", "A deal between countries to reduce barriers to trade."],
  ["World Trade Organization (WTO)", "An organisation that sets rules for international trade and settles disputes."],
] });
labL(); 
