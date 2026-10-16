"""Builds the three IGCSE Economics 2.2 Demand reviews (2.2.1 to 2.2.3).
Run: python3 tools/artifact-kit/mk_ig22.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# Shared demand-diagram helpers. Demand: P = 100 - (Q - s), i.e. shifted right by s.
DEMJS = '''
const DX = (q) => 90 + q * 4.6, DYP = (p) => 310 - p * 2.7;
function dAxes() { return SV.line(DX(0), DYP(0), DX(0), DYP(108)) + SV.line(DX(0), DYP(0), DX(135), DYP(0)) + SV.text(DX(0) + 8, 14, "Price ($)", "sm") + SV.text(DX(135), DYP(0) + 24, "Quantity demanded", "sm", { "text-anchor": "end" }); }
function dLine(s, cls, lab, tcls) {
  const q0 = Math.max(0, s), p0 = Math.min(100, 100 + s), pEnd = 100 - Math.max(0, 130 - s - 100) * 0, x1 = 100 + s;
  const a = s >= 0 ? [s, 100] : [0, 100 + s], b = [100 + s, 0];
  return SV.line(DX(a[0]), DYP(a[1]), DX(b[0]), DYP(b[1]), cls || "c1") + SV.text(DX(b[0]) + 6, DYP(b[1]) - 8, lab || "D", "lbl bd " + (tcls || "t1"));
}
function dDrop(q, p) { return SV.line(DX(0), DYP(p), DX(q), DYP(p), "gr") + SV.line(DX(q), DYP(p), DX(q), DYP(0), "gr"); }
function dDot(q, p, lab, cl, side) { return SV.circle(DX(q), DYP(p), 7, cl || "dot1") + SV.text(DX(q) + (side === "l" ? -12 : 12), DYP(p) + 4, lab, "lbl bd", { "text-anchor": side === "l" ? "end" : "start" }); }
'''

# =========================================================== 2.2.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Demand</span> is the <b>quantity of a good or service that consumers are willing and able to buy at a given price in a given period</b>. The <b>law of demand</b>: as the price of a good rises, the quantity demanded falls (and vice versa), <b>ceteris paribus</b> (other things unchanged). The demand curve therefore <b>slopes downwards</b> from left to right. <b>Market demand</b> is the sum of all individual demands.</p></div>

  <h2>Why the demand curve slopes downwards</h2>
  <ul>
    <li><b>Income effect:</b> a lower price means consumers' money buys more, so they can afford more.</li>
    <li><b>Substitution effect:</b> a lower price makes the good cheaper compared with substitutes, so consumers switch to it.</li>
    <li><b>Diminishing marginal utility:</b> each extra unit gives less satisfaction, so consumers will only buy more if the price is lower.</li>
  </ul>

  <h2>Individual and market demand</h2>
  <div class="tw"><table class="t">
    <tr><th>Price ($)</th><th>Consumer A</th><th>Consumer B</th><th>Consumer C</th><th>Market demand (A+B+C)</th></tr>
    <tr><td>10</td><td>8</td><td>6</td><td>10</td><td><b>24</b></td></tr>
    <tr><td>8</td><td>10</td><td>8</td><td>12</td><td><b>30</b></td></tr>
    <tr><td>6</td><td>12</td><td>10</td><td>14</td><td><b>36</b></td></tr>
    <tr><td>4</td><td>14</td><td>12</td><td>16</td><td><b>42</b></td></tr>
  </table></div>
  <p>The market demand curve is found by <b>adding up the quantities</b> every consumer wants at each price (adding horizontally). More consumers in the market means more demand at every price.</p>

  <h2>The demand diagram</h2>
  <ul>
    <li>Price on the <b>vertical</b> axis, quantity demanded on the <b>horizontal</b> axis.</li>
    <li>A downward-sloping line labelled <b>D</b>.</li>
    <li>Read it: at price <b>P</b> the quantity demanded is <b>Q</b>.</li>
  </ul>
  <p class="note">Demand is not the same as <b>want</b>: it must be backed by the ability to pay. A demand curve assumes everything except price is unchanged.</p>
'''
js = HEAD + COMMON + DEMJS + '''
Lib.stepper($("#stD"), { w: 760, h: 380, label: "Drawing a demand curve", base: { n: 0 }, draw: (s) => {
  let o = dAxes();
  if (s.n >= 1) o += SV.text(DX(0) - 8, DYP(80), "$80", "sm", { "text-anchor": "end" }) + SV.text(DX(0) - 8, DYP(40), "$40", "sm", { "text-anchor": "end" }) + dDot(20, 80, "", "dot1") + dDot(60, 40, "", "dot1");
  if (s.n >= 2) o += dLine(0, "c1", "D");
  if (s.n >= 3) o += dDrop(20, 80) + dDrop(60, 40) + SV.text(DX(20), DYP(0) + 18, "20", "sm", { "text-anchor": "middle" }) + SV.text(DX(60), DYP(0) + 18, "60", "sm", { "text-anchor": "middle" });
  return o;
}, steps: [
  { cap: "Price on the vertical axis; quantity demanded on the horizontal axis.", s: { n: 0 } },
  { cap: "At $80 consumers buy 20; at $40 they buy 60. Plot the two points.", s: { n: 1 } },
  { cap: "Join them: a <b>downward-sloping demand curve</b>, labelled D.", s: { n: 2 } },
  { cap: "Read across and down: a <b>lower price</b> means a <b>higher quantity demanded</b>.", s: { n: 3 } },
] });
const LW = ["The price of a good falls", "It is cheaper than substitutes: substitution effect", "Consumers' money buys more: income effect", "Each extra unit gives less satisfaction, but is now worth buying", "Quantity demanded rises: demand slopes downwards"];
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Why demand slopes down", base: { n: 0 }, draw: mkChain(LW, "--accent"), steps: chainSteps(["The <b>price</b> of a good falls.", "It is cheaper than substitutes: <b>substitution effect</b>.", "Consumers' money buys more: <b>income effect</b>.", "Each extra unit gives less satisfaction (<b>diminishing marginal utility</b>) but is now worth buying.", "<b>Quantity demanded rises</b>: the curve slopes downwards."]) });

/* Lab 1: individual to market demand */
function labD() {
  if (!$("#da") || !$("#db")) return;
  const n = +$("#da").value, p = +$("#db").value, qi = Math.max(0, 100 - p), qm = n * qi / 1, scale = Math.max(1, n);
  $("#da1").textContent = qi; $("#da2").textContent = n; $("#da3").textContent = qm;
  $("#dav").textContent = `At a price of $${p} one consumer buys ${qi}. With ${n} identical consumers in the market, market demand is ${n} × ${qi} = ${qm}. More consumers shift the market demand curve to the right (more bought at every price).`;
  const X = (q) => 90 + q * (500 / Math.max(100, 100 * n)), Y = (pp) => 310 - pp * 2.7;
  let d = SV.line(90, Y(0), 90, Y(108)) + SV.line(90, Y(0), 640, Y(0)) + SV.text(98, 14, "Price ($)", "sm") + SV.text(640, Y(0) + 24, "Quantity demanded", "sm", { "text-anchor": "end" });
  d += SV.line(X(0), Y(100), X(100), Y(0), "c1") + SV.text(X(100) + 6, Y(0) - 8, "Individual", "sm bd t1");
  d += SV.line(X(0), Y(100), X(100 * n), Y(0), "c2") + SV.text(X(100 * n) - 6, Y(0) - 26, n > 1 ? "Market" : "", "sm bd t2", { "text-anchor": "end" });
  d += SV.line(X(0), Y(p), X(qm), Y(p), "gr") + SV.circle(X(qi), Y(p), 6, "dot1") + SV.circle(X(qm), Y(p), 7, "dot2") + SV.text(X(qm), Y(0) + 18, qm, "sm bd", { "text-anchor": "middle" });
  $("#labD").innerHTML = d;
}
Lib.slider($("#g1"), { id: "da", label: "Number of identical consumers in the market", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "Price", min: 10, max: 90, step: 10, value: 50, fmt: (v) => "$" + v, onInput: labD });
const AD = [
  { n: "Price falls", d: "Quantity demanded rises", w: "Substitution and income effects." },
  { n: "Price rises", d: "Quantity demanded falls", w: "Dearer than substitutes; less affordable." },
  { n: "More consumers", d: "Market demand rises", w: "Add up individual quantities at each price." },
  { n: "Fewer consumers", d: "Market demand falls", w: "Less bought at each price." },
  { n: "Consumers' incomes rise", d: "Demand curve shifts right", w: "(Covered in 2.2.3.)" },
];
button_table("adBtns", "adOut", AD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each statement <b>true</b> or <b>false</b>?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "A demand curve slopes downwards", b: 0 }, { text: "Demand means willing AND able to pay", b: 0 }, { text: "Market demand is the sum of individual demands", b: 0 }, { text: "A fall in price raises quantity demanded", b: 0 },
  { text: "Demand is just what people want", b: 1 }, { text: "A higher price raises quantity demanded", b: 1 }, { text: "Price is on the horizontal axis", b: 1 },
], done: "Law of demand: price up, quantity demanded down." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Demand", "Quantity willing and able to buy at a given price"],
  ["Law of demand", "Higher price, lower quantity demanded"],
  ["Market demand", "Sum of all individual demands"],
  ["Substitution effect", "Switching to a cheaper good"],
  ["Income effect", "Money buys more when price falls"],
  ["Ceteris paribus", "All other things unchanged"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a price fall increases quantity demanded</b>.", items: [
  "The price of the good falls",
  "It is cheaper relative to substitutes",
  "Consumers' money goes further",
  "Consumers buy more",
  "Quantity demanded rises",
], done: "The law of demand." });
''' + calc_js([
    ("At $6 consumer A demands 12, B demands 10 and C demands 14. What is market demand?", 36, "12 + 10 + 14 = <b>36</b>.", None, None),
    ("Market demand at $10 is 24 and at $8 it is 30. By what percentage does quantity demanded rise?", 25, "6 ÷ 24 × 100 = <b>25%</b>.", None, None),
    ("10 identical consumers each buy 3 units at $5. What is market demand?", 30, "10 × 3 = <b>30</b>.", None, None),
]) + mcq_js("qz1", [
    ("What does a demand curve show?", ["Quantities supplied at each price", "Quantities demanded at each price", "Costs", "Profit"], 1, "Demand at each price."),
    ("Which describes the law of demand?", ["Price up, quantity demanded up", "Price up, quantity demanded down", "Income up, price up", "Supply up, price down"], 1, "Inverse relationship."),
    ("Market demand is found by:", ["Adding individual demands", "Subtracting", "Averaging prices", "Multiplying price"], 0, "Add quantities."),
    ("The demand curve slopes downwards because of:", ["Substitution and income effects", "Rising costs", "Taxes", "Advertising"], 0, "Cheaper means more affordable."),
    ("Demand requires consumers to be:", ["Willing only", "Willing and able to pay", "Wealthy", "Able only"], 1, "Both."),
]) + "\n" + cards_js([("Demand", "The quantity consumers are willing and able to buy at a given price in a given period."), ("Law of demand", "As price rises, quantity demanded falls, ceteris paribus."), ("Demand curve", "A curve showing the quantity demanded at each price."), ("Market demand", "The sum of all individual demands."), ("Quantity demanded", "The amount bought at one specific price."), ("Substitution effect", "Switching to a good that has become relatively cheaper."), ("Income effect", "A change in real income when a price changes."), ("Diminishing marginal utility", "Each extra unit gives less satisfaction."), ("Ceteris paribus", "All other things remaining unchanged.")]) + "labD(); \n"
explore = '''
  <h2>Lab 1 · From individual to market demand</h2>
  <p>Add identical consumers to the market. The market demand curve moves right.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>One consumer buys</small><strong id="da1"></strong></div><div><small>Consumers</small><strong id="da2"></strong></div><div><small>Market demand</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 340" role="img" aria-label="Individual and market demand"></svg>
  </div>

  <h2>Lab 2 · What happens to demand?</h2>
  <p>Pick a change to see its effect on quantity demanded or on the demand curve.</p>
  <div class="card"><div class="row" id="adBtns"></div><div id="adOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define demand. (Oct/Nov 2022, P22 style)", "Quantity willing and able to buy at a price.", "[K|Demand is the quantity of a good or service consumers are willing and able to buy] [K|at a given price in a given period.]"),
    Q(2, "Explain", 4, "Explain why a demand curve slopes downwards.", "Substitution, income, diminishing utility.",
      "[K|When the price falls the good becomes cheaper compared with substitutes,] [N|so consumers switch to it (substitution effect).] [K|Consumers' incomes buy more at lower prices,] [N|so they can afford to buy more (income effect). The quantity demanded therefore rises.]"),
    Q(3, "Explain", 4, "Explain how individual demand is linked to market demand.", "Add up all individual demands at each price.",
      "[K|Market demand is the total demand of all consumers in the market.] [N|It is found by adding up the quantities every consumer wants at each price.] [N|More consumers means more demand at every price.]"),
    Q(4, "Identify", 2, "Identify how the effect of a rise in the price of a good would be shown on its demand curve.", "A movement along: a contraction.", "[K|A movement up along the demand curve] [K|(a contraction in demand).]"),
)
tp = tips([
    ("Demand = willing AND able to pay.", "At a given price."),
    ("Price on the vertical axis.", "Label D, price, quantity."),
    ("Market demand = sum of individuals.", "Add horizontally."),
    ("Explain with substitution and income effects.", "Name them."),
    ("Say ceteris paribus.", "Other things unchanged."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.2.1 Individual and market demand"), "Individual and Market Demand", "What demand is, why the curve slopes downwards, and how individual demands add to market demand. Syllabus 2.2.1.",
    learn=learn, watch=watch(("Drawing a demand curve", "stD"), ("Why demand slopes down", "stL")), explore=explore,
    practise=practise(("True or false?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Sales and discounts", "Shops cut prices in sales and sell more, an example of the law of demand.", "Price down, quantity demanded up."),
        rw("Concert tickets", "When ticket prices rise, fewer people buy; at lower prices venues sell out.", "Demand slopes downwards."),
        rw("More consumers", "A rise in a city's population raises market demand for housing and transport.", "Market demand."),
        rw("Fuel prices", "Higher petrol prices lead some drivers to switch to public transport or cycling.", "Substitution effect.")),
    exam=ex, tips=tp)
write("d221", body, js, "Individual and Market Demand", "ig-demand-definition")

# =========================================================== 2.2.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <b>change in the price of a good</b> causes a <b>movement along</b> its demand curve. A <b>fall</b> in price causes an <b>extension of demand</b> (quantity demanded rises: a move down the curve). A <b>rise</b> in price causes a <b>contraction of demand</b> (quantity demanded falls: a move up the curve). The curve itself does <b>not</b> move.</p></div>

  <h2>Extension and contraction</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Extension in demand</th><th>Contraction in demand</th></tr>
    <tr><td><b>Cause</b></td><td>A fall in the price of the good</td><td>A rise in the price of the good</td></tr>
    <tr><td><b>Effect</b></td><td>Quantity demanded rises</td><td>Quantity demanded falls</td></tr>
    <tr><td><b>On the diagram</b></td><td>Movement <b>down</b> along the curve</td><td>Movement <b>up</b> along the curve</td></tr>
    <tr><td><b>Curve</b></td><td colspan="2">The same curve: no shift</td></tr>
  </table></div>

  <h2>Reasons for the move</h2>
  <ul>
    <li><b>Substitution effect:</b> consumers switch towards or away from the good as its relative price changes.</li>
    <li><b>Income effect:</b> a lower price raises real income, so consumers can buy more.</li>
    <li><b>Diminishing marginal utility:</b> consumers buy more only if the price falls.</li>
  </ul>
  <h2>Examples of a price change</h2>
  <ul>
    <li>A shop's <b>sale</b> reduces the price: extension.</li>
    <li>A rise in <b>tax</b> on cigarettes raises the price: contraction.</li>
    <li>A fall in the <b>cost of production</b> lowers the price: extension.</li>
  </ul>
  <p class="note">The exam trap: <b>extension/contraction</b> (price of the good itself changes, movement along the curve) versus <b>increase/decrease in demand</b> (other factors change, the curve shifts).</p>
'''
js = HEAD + COMMON + DEMJS + '''
Lib.stepper($("#stX"), { w: 760, h: 380, label: "Extension and contraction", base: { n: 0 }, draw: (s) => {
  let o = dAxes() + dLine(0, "c1", "D");
  const pts = [[40, 60], [70, 30], [20, 80]];
  o += dDrop(40, 60) + dDot(40, 60, "A", "dot1", "r");
  if (s.n === 1) o += dDrop(70, 30) + dDot(70, 30, "B", "dot2", "r") + SV.line(DX(40), DYP(60), DX(70), DYP(30), "c3") + SV.text(DX(0) - 8, DYP(30), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(DX(70), DYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  if (s.n === 2) o += dDrop(20, 80) + dDot(20, 80, "C", "dot4", "r") + SV.line(DX(40), DYP(60), DX(20), DYP(80), "c3") + SV.text(DX(0) - 8, DYP(80), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(DX(20), DYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(DX(0) - 8, DYP(60), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(DX(40), DYP(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}, steps: [
  { cap: "Demand curve D. At price P₁ quantity demanded is Q₁ (point A).", s: { n: 0 } },
  { cap: "The price <b>falls</b> to P₂. Move <b>down</b> the same curve to B: an <b>extension in demand</b> (quantity demanded rises to Q₂).", s: { n: 1 } },
  { cap: "The price <b>rises</b> to P₂. Move <b>up</b> the same curve to C: a <b>contraction in demand</b> (quantity demanded falls to Q₂).", s: { n: 2 } },
] });
const SP = ["The price of a good falls (for example a shop sale)", "Quantity demanded rises", "Move down along the same demand curve", "An extension in demand", "The demand curve has not shifted"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "A sale", base: { n: 0 }, draw: mkChain(SP, "--good"), steps: chainSteps(["The <b>price of a good falls</b> (for example a shop sale).", "<b>Quantity demanded rises</b>.", "Move <b>down</b> along the same demand curve.", "An <b>extension in demand</b>.", "The demand curve has <b>not shifted</b>."]) });

/* Lab 1: move along */
function labX() {
  if (!$("#xa")) return;
  const p = +$("#xa").value, q = 100 - p, p0 = 60, q0 = 100 - p0, dq = q - q0, pct = (dq / q0) * 100, ch = p < p0 ? "Extension" : p > p0 ? "Contraction" : "No change";
  $("#xa1").textContent = q; $("#xa2").textContent = ch; $("#xa3").textContent = (dq >= 0 ? "+" : "−") + Math.abs(Math.round(pct)) + "%";
  $("#xav").textContent = `Price moves from $60 to $${p}: quantity demanded moves from ${q0} to ${q} (${dq >= 0 ? "+" : "−"}${Math.abs(Math.round(pct))}%). ${ch === "No change" ? "No movement." : ch + " in demand: a movement " + (p < p0 ? "down" : "up") + " the same demand curve."} The curve has not shifted.`;
  $("#labX").innerHTML = dAxes() + dLine(0, "c1", "D") + dDrop(q0, p0) + SV.circle(DX(q0), DYP(p0), 6, "dot1") + (p !== p0 ? dDrop(q, p) + SV.circle(DX(q), DYP(p), 7, p < p0 ? "dot2" : "dot4") + SV.line(DX(q0), DYP(p0), DX(q), DYP(p), "c3") : "") + SV.text(DX(0) - 8, DYP(p0), "$60", "sm", { "text-anchor": "end" }) + SV.text(DX(q), DYP(0) + 18, q, "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "xa", label: "New price (starting at $60)", min: 10, max: 90, step: 5, value: 40, fmt: (v) => "$" + v, onInput: labX });
const XM = [
  { n: "A shop holds a sale", d: "Extension", w: "The price falls." },
  { n: "A tax raises the price of cigarettes", d: "Contraction", w: "The price rises." },
  { n: "Cheaper production lowers the price", d: "Extension", w: "The price falls." },
  { n: "An increase in income", d: "Not a movement: a shift", w: "A factor other than price." },
  { n: "A successful advertising campaign", d: "Not a movement: a shift", w: "A factor other than price." },
];
button_table("xmBtns", "xmOut", XM, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the demand curve</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>extension</b> or a <b>contraction</b> in demand?", buckets: [{ label: "Extension" }, { label: "Contraction" }], items: [
  { text: "A shop cuts the price of trainers", b: 0 }, { text: "A fall in the cost of production lowers the price", b: 0 }, { text: "A sale on coats", b: 0 },
  { text: "A tax raises the price of cigarettes", b: 1 }, { text: "A bad harvest raises the price of rice", b: 1 }, { text: "A firm increases its price", b: 1 },
], done: "Price down: extension. Price up: contraction." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>movement along</b> the demand curve or a <b>shift</b>?", buckets: [{ label: "Movement along" }, { label: "Shift of the curve" }], items: [
  { text: "A fall in the good's own price", b: 0 }, { text: "A rise in the good's own price", b: 0 },
  { text: "Consumers' incomes rise", b: 1 }, { text: "A fashion change", b: 1 }, { text: "A rise in the price of a substitute", b: 1 },
], done: "Only the good's own price causes a movement along." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Extension in demand", "Quantity demanded rises because the price falls"],
  ["Contraction in demand", "Quantity demanded falls because the price rises"],
  ["Movement along the curve", "Caused by a change in the good's own price"],
  ["Shift of the curve", "Caused by a change in a factor other than price"],
  ["Quantity demanded", "The amount bought at one price"],
  ["Demand", "The whole relationship between price and quantity"],
], done: "Extension and contraction are movements." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a price rise leads to a contraction in demand</b>.", items: [
  "The price of the good rises",
  "It is dearer than substitutes",
  "Consumers can afford less",
  "Quantity demanded falls",
  "Move up along the demand curve: a contraction",
], done: "A movement along the curve." });
''' + calc_js([
    ("Price falls from $60 to $40 and quantity demanded rises from 40 to 60. By what percentage does quantity demanded rise?", 50, "20 ÷ 40 × 100 = <b>50%</b>.", None, None),
    ("Price rises from $20 to $25. What is the percentage change in price?", 25, "5 ÷ 20 × 100 = <b>25%</b>.", None, None),
]) + mcq_js("qz1", [
    ("A fall in the price of a good causes:", ["A shift to the right", "An extension in demand", "A contraction in demand", "A shift to the left"], 1, "Move down the curve."),
    ("A contraction in demand is shown by:", ["A move up along the curve", "A shift right", "A shift left", "A move down along the curve"], 0, "Price rises."),
    ("What causes a movement along a demand curve?", ["A change in income", "A change in the good's own price", "A change in tastes", "Advertising"], 1, "Own price."),
    ("An extension in demand means:", ["Demand shifts right", "Quantity demanded rises", "Price rises", "Quantity demanded falls"], 1, "Price down."),
    ("The difference between extension and increase in demand is:", ["Extension is a movement; increase is a shift", "No difference", "Extension is a shift", "Increase is a price change"], 0, "Movement vs shift."),
]) + "\n" + cards_js([("Extension in demand", "A rise in quantity demanded caused by a fall in price."), ("Contraction in demand", "A fall in quantity demanded caused by a rise in price."), ("Movement along the demand curve", "A change in quantity demanded caused by a change in the good's own price."), ("Quantity demanded", "The amount bought at one specific price."), ("Own price", "The price of the good itself."), ("Substitution effect", "Switching to a cheaper good."), ("Income effect", "A change in purchasing power."), ("Increase in demand", "A shift of the curve to the right."), ("Decrease in demand", "A shift of the curve to the left.")]) + "labX(); \n"
explore = '''
  <h2>Lab 1 · Move along the curve</h2>
  <p>Start at $60. Change the price and watch the movement along the same demand curve.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Quantity demanded</small><strong id="xa1"></strong></div><div><small>Change</small><strong id="xa2"></strong></div><div><small>% change</small><strong id="xa3"></strong></div></div><div class="verdict" id="xav"></div></div></div>
    <svg id="labX" viewBox="0 0 760 340" role="img" aria-label="A movement along a demand curve"></svg>
  </div>

  <h2>Lab 2 · Movement or shift?</h2>
  <p>Pick a change to see whether it moves along the curve or shifts it.</p>
  <div class="card"><div class="row" id="xmBtns"></div><div id="xmOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define an extension in demand. (Oct/Nov 2021, P22 style)", "Quantity demanded rises because of a fall in price.", "[K|An extension in demand is a rise in quantity demanded] [K|caused by a fall in the price of the good.]"),
    Q(2, "Identify", 2, "Identify how the effect of a fall in the price of gold would be shown on a demand curve for gold. (May/June 2022, P22 style)", "A movement down along the curve: an extension.", "[K|A movement down along the demand curve] [K|(an extension in demand).]"),
    Q(3, "Explain", 4, "Explain the difference between an extension in demand and an increase in demand. (Feb/Mar 2021, P22 style)", "Extension: price change, movement along. Increase: other factor, shift right.",
      "[K|An extension in demand is caused by a fall in the good's own price] [N|and is shown by a movement down along the same demand curve.] [K|An increase in demand is caused by a change in another factor such as income] [N|and is shown by a shift of the whole curve to the right.]"),
    Q(4, "Explain", 4, "Explain how a rise in the price of cigarettes will affect the quantity demanded.", "Contraction; substitution; income; addiction may limit.",
      "[K|A rise in price causes a contraction in demand: a movement up along the demand curve.] [N|Cigarettes are dearer, so some smokers cut down or quit and affordability falls.] [E|The fall may be small because of addiction.]"),
)
tp = tips([
    ("Own price changes = movement along.", "Anything else = shift."),
    ("Extension = price falls.", "Contraction = price rises."),
    ("The curve does not move.", "Say 'a movement along the same curve'."),
    ("Draw and label P₁, Q₁, P₂, Q₂.", "Show the arrows."),
    ("Know the difference from increase and decrease.", "A classic question."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.2.2 Movements along a demand curve"), "Movements Along a Demand Curve", "Extensions and contractions in demand and how they are shown on the diagram. Syllabus 2.2.2.",
    learn=learn, watch=watch(("Extension and contraction", "stX"), ("A sale", "stS")), explore=explore,
    practise=practise(("Extension or contraction?", "cl1", "card"), ("Movement or shift?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Black Friday", "Big discounts push prices down, and shops sell far larger quantities.", "Extension in demand."),
        rw("Tobacco taxes", "Higher taxes raise cigarette prices and cut the quantity demanded, though not by much.", "Contraction in demand."),
        rw("Cheaper flights", "Budget airlines cut fares, and more people choose to fly.", "A price fall."),
        rw("Fuel price spikes", "When petrol prices jump, some people drive less.", "Contraction.")),
    exam=ex, tips=tp)
write("d222", body, js, "Movements Along a Demand Curve", "ig-demand-movements")

# =========================================================== 2.2.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A change in <b>any factor other than the good's own price</b> shifts the whole demand curve. A shift to the <b>right</b> is an <b>increase in demand</b> (more is demanded at every price). A shift to the <b>left</b> is a <b>decrease in demand</b> (less at every price).</p></div>

  <h2>Causes of a shift</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Increase in demand (right)</th><th>Decrease in demand (left)</th></tr>
    <tr><td><b>Income</b></td><td>Income rises (normal goods)</td><td>Income falls (normal goods); income rises for an <b>inferior good</b></td></tr>
    <tr><td><b>Tastes and fashion</b></td><td>The good becomes fashionable; a successful advertising campaign</td><td>The good goes out of fashion; bad publicity or health warnings</td></tr>
    <tr><td><b>Price of substitutes</b></td><td>A rise in the price of a substitute (e.g. tea up, coffee demand up)</td><td>A fall in the price of a substitute</td></tr>
    <tr><td><b>Price of complements</b></td><td>A fall in the price of a complement (e.g. cheaper printers, more ink demanded)</td><td>A rise in the price of a complement</td></tr>
    <tr><td><b>Population</b></td><td>A rising population or more people in the target group</td><td>A falling population</td></tr>
    <tr><td><b>Expectations</b></td><td>Prices expected to rise in future</td><td>Prices expected to fall in future</td></tr>
    <tr><td><b>Season and weather</b></td><td>Hot weather: ice cream demand up</td><td>Cold weather: ice cream demand down</td></tr>
    <tr><td><b>Credit, taxes and interest rates</b></td><td>Lower income tax, cheaper credit</td><td>Higher income tax, dearer credit</td></tr>
  </table></div>

  <h2>Key terms</h2>
  <ul>
    <li><b>Substitutes:</b> goods used in place of each other (butter and margarine). Their demands move in the <b>same</b> direction as the other's price.</li>
    <li><b>Complements:</b> goods used together (cars and petrol). Their demands move in the <b>opposite</b> direction to the other's price.</li>
    <li><b>Normal good:</b> demand rises as income rises. <b>Inferior good:</b> demand falls as income rises (e.g. cheap own-brand goods).</li>
  </ul>
  <p class="note">On a diagram: shift right D to D₁ for an increase; left D to D₂ for a decrease. Always label the axes and both curves. Remember: <b>a price change of the good itself moves along; everything else shifts.</b></p>
'''
js = HEAD + COMMON + DEMJS + '''
Lib.stepper($("#stH"), { w: 760, h: 380, label: "Shifts of demand", base: { s: 0 }, draw: (s) => {
  let o = dAxes() + dLine(0, s.s === 0 ? "c1" : "c3", "D");
  if (s.s !== 0) o += dLine(s.s, s.s > 0 ? "c2" : "c4", s.s > 0 ? "D₁" : "D₂", s.s > 0 ? "t2" : "t4") + dDrop(50, 50) + dDot(50, 50, "", "dot1") + dDot(50 + s.s * 0.5 + 0, 50, "", s.s > 0 ? "dot2" : "dot4") + SV.line(DX(50), DYP(50), DX(50 + s.s), DYP(50), "c3");
  return o + SV.text(DX(0) - 8, DYP(50), "P", "sm bd", { "text-anchor": "end" });
}, steps: [
  { cap: "Demand curve D.", s: { s: 0 } },
  { cap: "Incomes rise, or a good becomes fashionable: demand <b>increases</b> and the curve shifts <b>right</b> to D₁. <b>More is demanded at every price</b>.", s: { s: 30 } },
  { cap: "The good goes out of fashion: demand <b>decreases</b> and the curve shifts <b>left</b> to D₂. <b>Less is demanded at every price</b>.", s: { s: -30 } },
] });
const IN = ["Consumers' incomes rise", "They can afford more of a normal good", "More is demanded at every price", "The demand curve shifts right", "An increase in demand"];
Lib.stepper($("#stI"), { w: 760, h: 380, label: "A rise in income", base: { n: 0 }, draw: mkChain(IN, "--good"), steps: chainSteps(["Consumers' <b>incomes rise</b>.", "They can afford more of a <b>normal good</b>.", "<b>More is demanded at every price</b>.", "The demand curve <b>shifts right</b>.", "An <b>increase in demand</b>."]) });
const SB = ["The price of tea rises", "Tea is now dearer relative to coffee", "Consumers switch to coffee", "Demand for coffee rises at every price", "The coffee demand curve shifts right"];
Lib.stepper($("#stB"), { w: 760, h: 380, label: "A substitute's price rises", base: { n: 0 }, draw: mkChain(SB, "--accent"), steps: chainSteps(["The <b>price of tea</b> rises.", "Tea is dearer relative to coffee.", "Consumers <b>switch to coffee</b>.", "Demand for coffee rises <b>at every price</b>.", "The coffee demand curve <b>shifts right</b>."]) });

/* Lab 1: factors */
const FACT = [
  { n: "Income rises (normal good)", s: 25 }, { n: "Income rises (inferior good)", s: -25 }, { n: "Becomes fashionable", s: 30 }, { n: "Goes out of fashion", s: -30 },
  { n: "Substitute becomes dearer", s: 20 }, { n: "Complement becomes dearer", s: -20 }, { n: "Population grows", s: 20 }, { n: "Expected price rise", s: 15 },
];
function labF() {
  const i = +($("#fa") ? $("#fa").value : 0), f = FACT[i]; if (!$("#fa")) return;
  const s = f.s;
  $("#fa1").textContent = s > 0 ? "Increase" : "Decrease"; $("#fa2").textContent = s > 0 ? "Right" : "Left"; $("#fa3").textContent = (s > 0 ? "+" : "−") + Math.abs(s);
  $("#fav").textContent = `${f.n}: demand ${s > 0 ? "increases" : "decreases"} and the curve shifts ${s > 0 ? "right" : "left"}. At the same price of $50 the quantity demanded changes from 50 to ${50 + s}.`;
  $("#labF").innerHTML = dAxes() + dLine(0, "c3", "D") + dLine(s, s > 0 ? "c2" : "c4", s > 0 ? "D₁" : "D₂", s > 0 ? "t2" : "t4") + dDrop(50, 50) + SV.circle(DX(50), DYP(50), 6, "dot1") + SV.circle(DX(50 + s), DYP(50), 7, s > 0 ? "dot2" : "dot4") + SV.line(DX(50), DYP(50), DX(50 + s), DYP(50), "c3");
}
Lib.slider($("#g1"), { id: "fa", label: "Choose a factor (0 to 7)", min: 0, max: 7, step: 1, value: 0, fmt: (v) => FACT[v].n, onInput: labF });
const SH = [
  { n: "Substitutes", d: "Butter and margarine", e: "A rise in the price of one raises demand for the other." },
  { n: "Complements", d: "Cars and petrol", e: "A rise in the price of one lowers demand for the other." },
  { n: "Normal good", d: "Restaurant meals", e: "Demand rises as income rises." },
  { n: "Inferior good", d: "Own-brand cheap bread", e: "Demand falls as income rises." },
  { n: "Advertising", d: "A successful campaign", e: "Raises demand at every price." },
];
button_table("shBtns", "shOut", SH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Example</th><th>Effect</th></tr><tr><td>${p.d}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each <b>increase</b> or <b>decrease</b> demand for the good named?", buckets: [{ label: "Increase in demand" }, { label: "Decrease in demand" }], items: [
  { text: "Incomes rise: demand for holidays", b: 0 }, { text: "A successful advertising campaign for a drink", b: 0 }, { text: "The price of tea rises: demand for coffee", b: 0 }, { text: "Hot weather: demand for ice cream", b: 0 },
  { text: "A fall in the price of a substitute", b: 1 }, { text: "A rise in the price of a complement", b: 1 }, { text: "A health warning about a snack", b: 1 }, { text: "Population falls", b: 1 },
], done: "Right means increase; left means decrease." });
Lib.classify($("#cl2"), { prompt: "Are the two goods <b>substitutes</b> or <b>complements</b>?", buckets: [{ label: "Substitutes" }, { label: "Complements" }], items: [
  { text: "Tea and coffee", b: 0 }, { text: "Butter and margarine", b: 0 }, { text: "Buses and trains", b: 0 },
  { text: "Cars and petrol", b: 1 }, { text: "Printers and ink", b: 1 }, { text: "Bread and butter", b: 1 },
], done: "Substitutes replace; complements go together." });
Lib.match($("#m1"), { prompt: "Match the cause to the effect on demand.", pairs: [
  ["Income rises (normal good)", "Demand shifts right"],
  ["Income rises (inferior good)", "Demand shifts left"],
  ["Price of a substitute rises", "Demand shifts right"],
  ["Price of a complement rises", "Demand shifts left"],
  ["Good goes out of fashion", "Demand shifts left"],
  ["Population rises", "Demand shifts right"],
], done: "Learn the pairs." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how advertising increases demand</b>.", items: [
  "A successful advertising campaign runs",
  "Consumers' tastes change in favour of the good",
  "More is demanded at every price",
  "The demand curve shifts right",
  "An increase in demand",
], done: "A change in tastes." });
''' + calc_js([
    ("Demand at $50 rises from 50 to 80 units after an advertising campaign. What is the percentage increase?", 60, "30 ÷ 50 × 100 = <b>60%</b>.", None, None),
    ("A good is dearer by 10% and demand for its substitute rises by 8%. What is the new demand for the substitute if it was 200?", 216, "200 × 1.08 = <b>216</b>.", None, None),
]) + mcq_js("qz1", [
    ("A shift of the demand curve to the right shows:", ["A fall in price", "An increase in demand", "A decrease in demand", "A contraction"], 1, "More at every price."),
    ("Which would shift a demand curve to the left?", ["Rising incomes (normal good)", "A fall in the price of a substitute", "A successful advert", "Population growth"], 1, "Consumers switch away."),
    ("A rise in the price of a complement:", ["Raises demand for the good", "Lowers demand for the good", "Has no effect", "Raises supply"], 1, "They are used together."),
    ("An inferior good is one whose demand:", ["Rises as income rises", "Falls as income rises", "Is unaffected by income", "Is zero"], 1, "Consumers switch to better goods."),
    ("A shift of a demand curve is caused by:", ["A change in the good's own price", "A change in a factor other than price", "A tax on supply", "A movement along"], 1, "Non-price factors."),
]) + "\n" + cards_js([("Increase in demand", "A shift of the demand curve to the right."), ("Decrease in demand", "A shift of the demand curve to the left."), ("Substitute", "A good that can be used in place of another."), ("Complement", "A good used together with another."), ("Normal good", "A good for which demand rises as income rises."), ("Inferior good", "A good for which demand falls as income rises."), ("Tastes", "Consumers' preferences and fashion."), ("Expectations", "Beliefs about future prices or incomes."), ("Non-price factor", "A factor other than the good's own price that affects demand.")]) + "labF(); \n"
explore = '''
  <h2>Lab 1 · What shifts demand?</h2>
  <p>Choose a factor to see which way the curve shifts and by how much (illustrative).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Effect</small><strong id="fa1"></strong></div><div><small>Direction</small><strong id="fa2"></strong></div><div><small>Change at $50</small><strong id="fa3"></strong></div></div><div class="verdict" id="fav"></div></div></div>
    <svg id="labF" viewBox="0 0 760 340" role="img" aria-label="A shift of the demand curve"></svg>
  </div>

  <h2>Lab 2 · Related goods and income</h2>
  <p>Pick a term to see an example and its effect.</p>
  <div class="card"><div class="row" id="shBtns"></div><div id="shOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two causes of a shift to the right in the demand curve for fish. (Feb/Mar 2022, P22 style)", "Income, tastes/health campaign, price of substitute, population.",
      "[K|A rise in consumers' incomes could increase demand for fish,] [N|because they can afford more at every price.] [K|A health campaign promoting fish could change tastes,] [N|so more is demanded at every price.]"),
    Q(2, "Explain", 4, "Explain two causes of a shift of a product's demand curve to the left. (Oct/Nov 2023, P22 style)", "A fall in income, a rise in the price of a complement, bad publicity, a fall in the price of a substitute.",
      "[K|A fall in consumers' incomes could reduce demand for a normal good,] [N|so less is demanded at every price.] [K|A fall in the price of a substitute could make consumers switch,] [N|so demand for the product falls at every price.]"),
    Q(3, "Explain", 4, "Explain why a rise in the price of petrol may reduce the demand for cars.", "Complements; running costs; demand shifts left.",
      "[K|Petrol and cars are complements, used together.] [N|A rise in the price of petrol makes running a car dearer,] [N|so fewer people want to buy cars and the demand curve shifts left.]"),
    Q(4, "Analyse", 6, "Analyse how a rise in incomes may affect the demand for different types of good.", "Normal vs inferior; luxury; shifts.",
      "[K|A rise in incomes increases demand for normal goods such as holidays and restaurant meals,] [N|so their demand curves shift right.] [N|It reduces demand for inferior goods, such as cheap own-brand products, as consumers switch to better alternatives,] [N|so their demand curves shift left.] [E|The size of the shift depends on how sensitive demand is to income.]", key=True),
)
tp = tips([
    ("Shifts are caused by factors other than own price.", "Name the factor."),
    ("Right = increase; left = decrease.", "Say 'more at every price'."),
    ("Substitutes: same direction; complements: opposite.", "Be careful."),
    ("Normal vs inferior goods.", "Income effects differ."),
    ("Draw D and D₁ and label axes.", "Marks for the diagram."),
], cmds("Explain", "Analyse"))
body = page(CL("2.2.3 Shifts of a demand curve"), "Shifts of a Demand Curve", "Causes of increases and decreases in demand and how they are shown on the diagram. Syllabus 2.2.3.",
    learn=learn, watch=watch(("Shifts of demand", "stH"), ("A rise in income", "stI"), ("A substitute's price rises", "stB")), explore=explore,
    practise=practise(("Increase or decrease?", "cl1", "card"), ("Substitutes or complements?", "cl2", "card"), ("Match the cause", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Hot summers", "Demand for ice cream, fans and cold drinks rises at every price.", "Weather as a cause."),
        rw("Health campaigns", "Campaigns against sugar have shifted demand for sugary drinks to the left.", "Tastes and information."),
        rw("Electric vehicles", "Subsidies and rising petrol prices have shifted demand towards electric cars.", "Related goods."),
        rw("Rising incomes in emerging markets", "Demand for cars, phones and holidays has risen as incomes grew.", "Normal goods.")),
    exam=ex, tips=tp)
write("d223", body, js, "Shifts of a Demand Curve", "ig-demand-shifts")
