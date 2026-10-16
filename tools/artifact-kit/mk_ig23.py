"""Builds the three IGCSE Economics 2.3 Supply reviews (2.3.1 to 2.3.3).
Run: python3 tools/artifact-kit/mk_ig23.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# Supply: P = Q - s (s>0 shifts right/increase; s<0 shifts left/decrease), drawn for 0<=P<=100.
SUPJS = '''
const SX = (q) => 90 + q * 4.6, SYP = (p) => 310 - p * 2.7;
function sAxes() { return SV.line(SX(0), SYP(0), SX(0), SYP(108)) + SV.line(SX(0), SYP(0), SX(135), SYP(0)) + SV.text(SX(0) + 8, 14, "Price ($)", "sm") + SV.text(SX(135), SYP(0) + 24, "Quantity supplied", "sm", { "text-anchor": "end" }); }
function sLine(s, cls, lab, tcls) {
  const a = s >= 0 ? [s, 0] : [0, -s], b = [100 + s, 100];
  return SV.line(SX(a[0]), SYP(a[1]), SX(b[0]), SYP(b[1]), cls || "c2") + SV.text(SX(b[0]) + 6, SYP(b[1]) + 4, lab || "S", "lbl bd " + (tcls || "t2"));
}
function sDrop(q, p) { return SV.line(SX(0), SYP(p), SX(q), SYP(p), "gr") + SV.line(SX(q), SYP(p), SX(q), SYP(0), "gr"); }
function sDot(q, p, lab, cl, side) { return SV.circle(SX(q), SYP(p), 7, cl || "dot1") + SV.text(SX(q) + (side === "l" ? -12 : 12), SYP(p) + 4, lab, "lbl bd", { "text-anchor": side === "l" ? "end" : "start" }); }
'''

# =========================================================== 2.3.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Supply</span> is the <b>quantity of a good or service that producers are willing and able to sell at a given price in a given period</b>. The <b>law of supply</b>: as the price of a good rises, the quantity supplied rises (and vice versa), <b>ceteris paribus</b>. The supply curve therefore <b>slopes upwards</b> from left to right. <b>Market supply</b> is the sum of all individual firms' supplies.</p></div>

  <h2>Why the supply curve slopes upwards</h2>
  <ul>
    <li><b>Profit motive:</b> a higher price means a higher profit per unit, so firms want to produce more.</li>
    <li><b>Rising marginal costs:</b> producing more usually costs more per extra unit (overtime, less suitable resources), so firms need a higher price to cover them.</li>
    <li><b>New entrants:</b> higher prices attract more firms into the market.</li>
  </ul>

  <h2>Individual and market supply</h2>
  <div class="tw"><table class="t">
    <tr><th>Price ($)</th><th>Firm A</th><th>Firm B</th><th>Firm C</th><th>Market supply (A+B+C)</th></tr>
    <tr><td>4</td><td>8</td><td>6</td><td>10</td><td><b>24</b></td></tr>
    <tr><td>6</td><td>10</td><td>8</td><td>12</td><td><b>30</b></td></tr>
    <tr><td>8</td><td>12</td><td>10</td><td>14</td><td><b>36</b></td></tr>
    <tr><td>10</td><td>14</td><td>12</td><td>16</td><td><b>42</b></td></tr>
  </table></div>
  <p>The market supply curve is found by <b>adding up the quantities</b> all firms will supply at each price. More firms in the market means more supply at every price.</p>

  <h2>The supply diagram</h2>
  <ul>
    <li>Price on the <b>vertical</b> axis, quantity supplied on the <b>horizontal</b> axis.</li>
    <li>An <b>upward-sloping</b> line labelled <b>S</b>.</li>
    <li>At price <b>P</b> producers supply quantity <b>Q</b>.</li>
  </ul>
  <p class="note">Supply means <b>willing and able</b> to sell: producers need the resources and capacity as well as the wish to sell. A supply curve assumes everything except price is unchanged.</p>
'''
js = HEAD + COMMON + SUPJS + '''
Lib.stepper($("#stD"), { w: 760, h: 380, label: "Drawing a supply curve", base: { n: 0 }, draw: (s) => {
  let o = sAxes();
  if (s.n >= 1) o += SV.text(SX(0) - 8, SYP(40), "$40", "sm", { "text-anchor": "end" }) + SV.text(SX(0) - 8, SYP(80), "$80", "sm", { "text-anchor": "end" }) + sDot(40, 40, "", "dot1") + sDot(80, 80, "", "dot1");
  if (s.n >= 2) o += sLine(0, "c2", "S");
  if (s.n >= 3) o += sDrop(40, 40) + sDrop(80, 80) + SV.text(SX(40), SYP(0) + 18, "40", "sm", { "text-anchor": "middle" }) + SV.text(SX(80), SYP(0) + 18, "80", "sm", { "text-anchor": "middle" });
  return o;
}, steps: [
  { cap: "Price on the vertical axis; quantity supplied on the horizontal axis.", s: { n: 0 } },
  { cap: "At $40 firms supply 40; at $80 they supply 80. Plot the points.", s: { n: 1 } },
  { cap: "Join them: an <b>upward-sloping supply curve</b>, labelled S.", s: { n: 2 } },
  { cap: "A <b>higher price</b> means a <b>higher quantity supplied</b>.", s: { n: 3 } },
] });
const LS = ["The price of a good rises", "Profit per unit rises", "Firms want to produce more; new firms may enter", "Higher price covers rising marginal cost", "Quantity supplied rises: supply slopes upwards"];
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Why supply slopes up", base: { n: 0 }, draw: mkChain(LS, "--warn"), steps: chainSteps(["The <b>price</b> of a good rises.", "<b>Profit per unit</b> rises.", "Firms want to <b>produce more</b>; new firms may enter.", "The higher price covers <b>rising marginal costs</b>.", "<b>Quantity supplied rises</b>: the curve slopes upwards."]) });

/* Lab 1: individual to market supply */
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const n = +$("#sa").value, p = +$("#sb").value, qi = p, qm = n * qi;
  $("#sa1").textContent = qi; $("#sa2").textContent = n; $("#sa3").textContent = qm;
  $("#sav").textContent = `At a price of $${p} one firm supplies ${qi}. With ${n} identical firms in the market, market supply is ${n} × ${qi} = ${qm}. More firms shift the market supply curve to the right (more supplied at every price).`;
  const X = (q) => 90 + q * (500 / Math.max(100, 100 * n)), Y = (pp) => 310 - pp * 2.7;
  let d = SV.line(90, Y(0), 90, Y(108)) + SV.line(90, Y(0), 640, Y(0)) + SV.text(98, 14, "Price ($)", "sm") + SV.text(640, Y(0) + 24, "Quantity supplied", "sm", { "text-anchor": "end" });
  d += SV.line(X(0), Y(0), X(100), Y(100), "c2") + SV.text(X(100) + 6, Y(100) + 4, "Individual", "sm bd t2");
  d += SV.line(X(0), Y(0), X(100 * n), Y(100), "c1") + SV.text(X(85 * n) - 8, Y(85) - 10, n > 1 ? "Market" : "", "sm bd t1", { "text-anchor": "end" });
  d += SV.line(X(0), Y(p), X(qm), Y(p), "gr") + SV.circle(X(qi), Y(p), 6, "dot1") + SV.circle(X(qm), Y(p), 7, "dot2") + SV.text(X(qm), Y(0) + 18, qm, "sm bd", { "text-anchor": "middle" });
  $("#labS").innerHTML = d;
}
Lib.slider($("#g1"), { id: "sa", label: "Number of identical firms in the market", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Price", min: 10, max: 90, step: 10, value: 50, fmt: (v) => "$" + v, onInput: labS });
const AS = [
  { n: "Price rises", d: "Quantity supplied rises", w: "Higher profit per unit." },
  { n: "Price falls", d: "Quantity supplied falls", w: "Lower profit; some firms leave." },
  { n: "More firms", d: "Market supply rises", w: "Add up individual quantities at each price." },
  { n: "Fewer firms", d: "Market supply falls", w: "Less supplied at each price." },
  { n: "Costs fall", d: "Supply curve shifts right", w: "(Covered in 2.3.3.)" },
];
button_table("asBtns", "asOut", AS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each statement <b>true</b> or <b>false</b>?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "A supply curve slopes upwards", b: 0 }, { text: "Supply means willing AND able to sell", b: 0 }, { text: "Market supply is the sum of individual supplies", b: 0 }, { text: "A rise in price raises quantity supplied", b: 0 },
  { text: "A supply curve slopes downwards", b: 1 }, { text: "A higher price lowers quantity supplied", b: 1 }, { text: "Quantity supplied is on the vertical axis", b: 1 },
], done: "Law of supply: price up, quantity supplied up." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Supply", "Quantity willing and able to sell at a given price"],
  ["Law of supply", "Higher price, higher quantity supplied"],
  ["Market supply", "Sum of all individual supplies"],
  ["Profit motive", "Higher prices give higher profit per unit"],
  ["Marginal cost", "Cost of producing one more unit"],
  ["Ceteris paribus", "All other things unchanged"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a price rise increases quantity supplied</b>.", items: [
  "The price of the good rises",
  "Profit per unit rises",
  "Firms want to produce more",
  "Firms supply more",
  "Quantity supplied rises",
], done: "The law of supply." });
''' + calc_js([
    ("At $6 firm A supplies 10, B supplies 8 and C supplies 12. What is market supply?", 30, "10 + 8 + 12 = <b>30</b>.", None, None),
    ("Market supply at $4 is 24 and at $6 it is 30. By what percentage does quantity supplied rise?", 25, "6 ÷ 24 × 100 = <b>25%</b>.", None, None),
    ("20 identical farms each supply 50 tonnes at $200. What is market supply (tonnes)?", 1000, "20 × 50 = <b>1,000</b>.", None, None),
]) + mcq_js("qz1", [
    ("What does a supply curve show?", ["Quantities demanded", "Quantities supplied at each price", "Costs", "Taxes"], 1, "Supply at each price."),
    ("Which describes the law of supply?", ["Price up, quantity supplied up", "Price up, quantity supplied down", "Income up, price up", "Demand up, supply down"], 0, "Direct relationship."),
    ("Market supply is found by:", ["Adding individual supplies", "Subtracting", "Averaging", "Multiplying price"], 0, "Add quantities."),
    ("The supply curve slopes upwards because:", ["Higher prices give higher profit per unit", "Costs fall", "Demand falls", "Taxes rise"], 0, "Incentive to produce more."),
    ("Supply requires producers to be:", ["Willing only", "Willing and able to sell", "Large", "Foreign"], 1, "Both."),
]) + "\n" + cards_js([("Supply", "The quantity producers are willing and able to sell at a given price in a given period."), ("Law of supply", "As price rises, quantity supplied rises, ceteris paribus."), ("Supply curve", "A curve showing the quantity supplied at each price."), ("Market supply", "The sum of all individual firms' supplies."), ("Quantity supplied", "The amount supplied at one specific price."), ("Profit motive", "The aim of earning profit."), ("Marginal cost", "The cost of producing one extra unit."), ("New entrants", "Firms that enter a market."), ("Ceteris paribus", "All other things remaining unchanged.")]) + "labS(); \n"
explore = '''
  <h2>Lab 1 · From individual to market supply</h2>
  <p>Add identical firms to the market. The market supply curve moves right.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>One firm supplies</small><strong id="sa1"></strong></div><div><small>Firms</small><strong id="sa2"></strong></div><div><small>Market supply</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 340" role="img" aria-label="Individual and market supply"></svg>
  </div>

  <h2>Lab 2 · What happens to supply?</h2>
  <p>Pick a change to see its effect on quantity supplied or on the supply curve.</p>
  <div class="card"><div class="row" id="asBtns"></div><div id="asOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define supply. (Oct/Nov 2022, P22 style)", "Quantity willing and able to sell at a price.", "[K|Supply is the quantity of a good or service producers are willing and able to sell] [K|at a given price in a given period.]"),
    Q(2, "Explain", 4, "Explain why a supply curve slopes upwards.", "Profit; rising marginal cost; new entrants.",
      "[K|A higher price means a higher profit for each unit sold,] [N|so firms are willing to produce and sell more.] [K|Producing more usually raises marginal costs,] [N|so a higher price is needed to cover them; new firms may also enter.]"),
    Q(3, "Explain", 4, "Explain how individual supply is linked to market supply.", "Add up all firms' supplies at each price.",
      "[K|Market supply is the total supply of all firms in the market.] [N|It is found by adding up the quantities all firms will supply at each price.] [N|More firms in the market means more supplied at every price.]"),
    Q(4, "Identify", 2, "Identify how the effect of a fall in the price of a good would be shown on its supply curve.", "A movement down: a contraction.", "[K|A movement down along the supply curve] [K|(a contraction in supply).]"),
)
tp = tips([
    ("Supply = willing AND able to sell.", "At a given price."),
    ("Price on the vertical axis.", "Label S, price, quantity."),
    ("Market supply = sum of individuals.", "Add horizontally."),
    ("Explain with profit and rising marginal cost.", "Name them."),
    ("Say ceteris paribus.", "Other things unchanged."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.3.1 Individual and market supply"), "Individual and Market Supply", "What supply is, why the curve slopes upwards, and how individual supplies add to market supply. Syllabus 2.3.1.",
    learn=learn, watch=watch(("Drawing a supply curve", "stD"), ("Why supply slopes up", "stL")), explore=explore,
    practise=practise(("True or false?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Farmers and crop prices", "When the price of wheat rises, farmers plant more and supply more.", "Price up, quantity supplied up."),
        rw("Surge pricing", "Taxis and ride apps pay drivers more at busy times, and more drivers come online.", "Higher price, more supplied."),
        rw("More firms", "As a new industry grows more firms enter, raising market supply at every price.", "Market supply."),
        rw("Oil production", "Higher oil prices make expensive wells profitable, so output rises.", "Rising marginal cost.")),
    exam=ex, tips=tp)
write("s231", body, js, "Individual and Market Supply", "ig-supply-definition")

# =========================================================== 2.3.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <b>change in the price of a good</b> causes a <b>movement along</b> its supply curve. A <b>rise</b> in price causes an <b>extension of supply</b> (quantity supplied rises: a move up the curve). A <b>fall</b> in price causes a <b>contraction of supply</b> (quantity supplied falls: a move down the curve). The curve itself does <b>not</b> move.</p></div>

  <h2>Extension and contraction</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Extension in supply</th><th>Contraction in supply</th></tr>
    <tr><td><b>Cause</b></td><td>A rise in the price of the good</td><td>A fall in the price of the good</td></tr>
    <tr><td><b>Effect</b></td><td>Quantity supplied rises</td><td>Quantity supplied falls</td></tr>
    <tr><td><b>On the diagram</b></td><td>Movement <b>up</b> along the curve</td><td>Movement <b>down</b> along the curve</td></tr>
    <tr><td><b>Curve</b></td><td colspan="2">The same curve: no shift</td></tr>
  </table></div>

  <h2>Reasons for the move</h2>
  <ul>
    <li><b>Higher price, higher profit per unit:</b> firms produce more.</li>
    <li><b>Lower price, lower profit:</b> some firms cut output or stop production; marginal cost may exceed the price.</li>
    <li>Higher prices may also <b>attract new firms</b> into the market.</li>
  </ul>
  <h2>Examples of a price change</h2>
  <ul>
    <li>Higher world demand raises the <b>price of coffee</b>: coffee farmers extend supply.</li>
    <li>A <b>fall in the price of oil</b> leads high-cost oil wells to close: contraction.</li>
  </ul>
  <p class="note">Extension/contraction is caused by the <b>good's own price</b>. A change in <b>costs, technology or taxes</b> shifts the curve (see 2.3.3).</p>
'''
js = HEAD + COMMON + SUPJS + '''
Lib.stepper($("#stX"), { w: 760, h: 380, label: "Extension and contraction", base: { n: 0 }, draw: (s) => {
  let o = sAxes() + sLine(0, "c2", "S") + sDrop(40, 40) + sDot(40, 40, "A", "dot1", "l");
  if (s.n === 1) o += sDrop(70, 70) + sDot(70, 70, "B", "dot2", "l") + SV.line(SX(40), SYP(40), SX(70), SYP(70), "c3") + SV.text(SX(0) - 8, SYP(70), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(SX(70), SYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  if (s.n === 2) o += sDrop(20, 20) + sDot(20, 20, "C", "dot4", "r") + SV.line(SX(40), SYP(40), SX(20), SYP(20), "c3") + SV.text(SX(0) - 8, SYP(20), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(SX(20), SYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(SX(0) - 8, SYP(40), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(SX(40), SYP(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}, steps: [
  { cap: "Supply curve S. At price P₁ quantity supplied is Q₁ (point A).", s: { n: 0 } },
  { cap: "The price <b>rises</b> to P₂. Move <b>up</b> the same curve to B: an <b>extension in supply</b>.", s: { n: 1 } },
  { cap: "The price <b>falls</b> to P₂. Move <b>down</b> the same curve to C: a <b>contraction in supply</b>.", s: { n: 2 } },
] });
const SP = ["The price of coffee rises", "Growers earn more profit per tonne", "They produce more coffee", "Move up along the same supply curve", "An extension in supply (the curve has not shifted)"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "A price rise", base: { n: 0 }, draw: mkChain(SP, "--warn"), steps: chainSteps(["The <b>price of coffee rises</b>.", "Growers earn <b>more profit</b> per tonne.", "They <b>produce more</b> coffee.", "Move <b>up</b> along the same supply curve.", "An <b>extension in supply</b> (the curve has not shifted)."]) });

/* Lab 1 */
function labX() {
  if (!$("#xa")) return;
  const p = +$("#xa").value, q = p, p0 = 40, q0 = p0, dq = q - q0, pct = (dq / q0) * 100, ch = p > p0 ? "Extension" : p < p0 ? "Contraction" : "No change";
  $("#xa1").textContent = q; $("#xa2").textContent = ch; $("#xa3").textContent = (dq >= 0 ? "+" : "−") + Math.abs(Math.round(pct)) + "%";
  $("#xav").textContent = `Price moves from $40 to $${p}: quantity supplied moves from ${q0} to ${q} (${dq >= 0 ? "+" : "−"}${Math.abs(Math.round(pct))}%). ${ch === "No change" ? "No movement." : ch + " in supply: a movement " + (p > p0 ? "up" : "down") + " the same supply curve."} The curve has not shifted.`;
  $("#labX").innerHTML = sAxes() + sLine(0, "c2", "S") + sDrop(q0, p0) + SV.circle(SX(q0), SYP(p0), 6, "dot1") + (p !== p0 ? sDrop(q, p) + SV.circle(SX(q), SYP(p), 7, p > p0 ? "dot2" : "dot4") + SV.line(SX(q0), SYP(p0), SX(q), SYP(p), "c3") : "") + SV.text(SX(0) - 8, SYP(p0), "$40", "sm", { "text-anchor": "end" }) + SV.text(SX(q), SYP(0) + 18, q, "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "xa", label: "New price (starting at $40)", min: 10, max: 90, step: 5, value: 60, fmt: (v) => "$" + v, onInput: labX });
const XM = [
  { n: "The price of the good rises", d: "Extension", w: "Higher profit per unit." },
  { n: "The price of the good falls", d: "Contraction", w: "Lower profit; some firms cut output." },
  { n: "Costs of production fall", d: "Not a movement: a shift", w: "A factor other than price." },
  { n: "New technology", d: "Not a movement: a shift", w: "A factor other than price." },
  { n: "A tax on the good", d: "Not a movement: a shift", w: "A factor other than price." },
];
button_table("xmBtns", "xmOut", XM, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the supply curve</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>extension</b> or a <b>contraction</b> in supply?", buckets: [{ label: "Extension" }, { label: "Contraction" }], items: [
  { text: "The price of wheat rises and farmers grow more", b: 0 }, { text: "Higher oil prices lead wells to produce more", b: 0 }, { text: "A rise in the price of coffee", b: 0 },
  { text: "The price of milk falls and dairy farms cut output", b: 1 }, { text: "Falling oil prices close high-cost wells", b: 1 }, { text: "A fall in the price of steel", b: 1 },
], done: "Price up: extension. Price down: contraction." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>movement along</b> the supply curve or a <b>shift</b>?", buckets: [{ label: "Movement along" }, { label: "Shift of the curve" }], items: [
  { text: "A rise in the good's own price", b: 0 }, { text: "A fall in the good's own price", b: 0 },
  { text: "A fall in wage costs", b: 1 }, { text: "New technology", b: 1 }, { text: "A new tax on producers", b: 1 },
], done: "Only the good's own price causes a movement along." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Extension in supply", "Quantity supplied rises because the price rises"],
  ["Contraction in supply", "Quantity supplied falls because the price falls"],
  ["Movement along the curve", "Caused by a change in the good's own price"],
  ["Shift of the curve", "Caused by a change in a non-price factor"],
  ["Quantity supplied", "The amount supplied at one price"],
  ["Supply", "The whole relationship between price and quantity"],
], done: "Extension and contraction are movements." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a price fall causes a contraction in supply</b>.", items: [
  "The price of the good falls",
  "Profit per unit falls",
  "Some firms cut output or leave",
  "Quantity supplied falls",
  "Move down along the supply curve: a contraction",
], done: "A movement along the curve." });
''' + calc_js([
    ("Price rises from $40 to $60 and quantity supplied rises from 40 to 60. By what percentage does quantity supplied rise?", 50, "20 ÷ 40 × 100 = <b>50%</b>.", None, None),
    ("Price falls from $50 to $40. What is the percentage change in price?", 20, "10 ÷ 50 × 100 = <b>20%</b>.", None, None),
]) + mcq_js("qz1", [
    ("A rise in the price of a good causes:", ["A shift to the right", "An extension in supply", "A contraction in supply", "A shift to the left"], 1, "Move up the curve."),
    ("A contraction in supply is shown by:", ["A move up along the curve", "A shift right", "A shift left", "A move down along the curve"], 3, "Price falls."),
    ("What causes a movement along a supply curve?", ["A change in costs", "A change in the good's own price", "New technology", "A tax"], 1, "Own price."),
    ("An extension in supply means:", ["Supply shifts right", "Quantity supplied rises", "Price falls", "Quantity supplied falls"], 1, "Price up."),
    ("The difference between extension and increase in supply is:", ["Extension is a movement; increase is a shift", "No difference", "Extension is a shift", "Increase is a price change"], 0, "Movement vs shift."),
]) + "\n" + cards_js([("Extension in supply", "A rise in quantity supplied caused by a rise in price."), ("Contraction in supply", "A fall in quantity supplied caused by a fall in price."), ("Movement along the supply curve", "A change in quantity supplied caused by a change in the good's own price."), ("Quantity supplied", "The amount supplied at one price."), ("Own price", "The price of the good itself."), ("Profit per unit", "Price minus cost per unit."), ("Increase in supply", "A shift of the curve to the right."), ("Decrease in supply", "A shift of the curve to the left."), ("Marginal cost", "The cost of producing one more unit.")]) + "labX(); \n"
explore = '''
  <h2>Lab 1 · Move along the curve</h2>
  <p>Start at $40. Change the price and watch the movement along the same supply curve.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Quantity supplied</small><strong id="xa1"></strong></div><div><small>Change</small><strong id="xa2"></strong></div><div><small>% change</small><strong id="xa3"></strong></div></div><div class="verdict" id="xav"></div></div></div>
    <svg id="labX" viewBox="0 0 760 340" role="img" aria-label="A movement along a supply curve"></svg>
  </div>

  <h2>Lab 2 · Movement or shift?</h2>
  <p>Pick a change to see whether it moves along the curve or shifts it.</p>
  <div class="card"><div class="row" id="xmBtns"></div><div id="xmOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define an extension in supply.", "Quantity supplied rises because of a rise in price.", "[K|An extension in supply is a rise in quantity supplied] [K|caused by a rise in the price of the good.]"),
    Q(2, "Identify", 2, "Identify how the effect of a rise in the price of coffee would be shown on its supply curve.", "A move up along the curve: an extension.", "[K|A movement up along the supply curve] [K|(an extension in supply).]"),
    Q(3, "Explain", 4, "Explain the difference between an extension in supply and an increase in supply.", "Extension: price change, movement along. Increase: other factor, shift right.",
      "[K|An extension in supply is caused by a rise in the good's own price] [N|and is shown by a movement up along the same supply curve.] [K|An increase in supply is caused by a change in another factor such as costs] [N|and is shown by a shift of the whole curve to the right.]"),
    Q(4, "Explain", 4, "Explain why a fall in the price of oil may reduce the quantity supplied.", "Lower profit; high-cost wells close; contraction.",
      "[K|A fall in price reduces the profit for each barrel.] [N|High-cost wells may no longer cover their costs, so they close or reduce output,] [N|which causes a contraction in supply: a movement down the curve.]"),
)
tp = tips([
    ("Own price changes = movement along.", "Anything else = shift."),
    ("Extension = price rises.", "Contraction = price falls."),
    ("The curve does not move.", "Say 'a movement along the same curve'."),
    ("Draw and label P₁, Q₁, P₂, Q₂.", "Show the arrows."),
    ("Know the difference from increase and decrease.", "A classic question."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.3.2 Movements along a supply curve"), "Movements Along a Supply Curve", "Extensions and contractions in supply and how they are shown on the diagram. Syllabus 2.3.2.",
    learn=learn, watch=watch(("Extension and contraction", "stX"), ("A price rise", "stS")), explore=explore,
    practise=practise(("Extension or contraction?", "cl1", "card"), ("Movement or shift?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Coffee prices", "When coffee prices climb, growers expand planting and harvest more.", "Extension in supply."),
        rw("Oil wells", "When oil prices fall sharply, high-cost producers cut output or shut wells.", "Contraction in supply."),
        rw("Seasonal produce", "Farmers bring more to market when prices are high.", "A price rise."),
        rw("Housing", "Rising house prices encourage builders to build more homes.", "Extension in supply.")),
    exam=ex, tips=tp)
write("s232", body, js, "Movements Along a Supply Curve", "ig-supply-movements")

# =========================================================== 2.3.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A change in <b>any factor other than the good's own price</b> shifts the whole supply curve. A shift to the <b>right</b> is an <b>increase in supply</b> (more is supplied at every price). A shift to the <b>left</b> is a <b>decrease in supply</b> (less at every price).</p></div>

  <h2>Causes of a shift</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Increase in supply (right)</th><th>Decrease in supply (left)</th></tr>
    <tr><td><b>Costs of production</b> (wages, raw materials, energy, rent)</td><td>Costs fall</td><td>Costs rise</td></tr>
    <tr><td><b>Technology</b></td><td>New technology raises productivity and cuts costs</td><td>(Rarely: loss of technology)</td></tr>
    <tr><td><b>Taxes and subsidies</b></td><td>A subsidy or a cut in taxes on producers</td><td>A tax on producers (such as VAT or an excise tax)</td></tr>
    <tr><td><b>Weather and natural disasters</b></td><td>Good harvest weather</td><td>Drought, flood, disease (for agriculture)</td></tr>
    <tr><td><b>Number of firms</b></td><td>New firms enter the market</td><td>Firms leave the market</td></tr>
    <tr><td><b>Prices of other goods</b> (producers' alternatives)</td><td>The price of a good they could produce instead falls</td><td>The price of an alternative rises, so resources switch</td></tr>
    <tr><td><b>Government regulation</b></td><td>Fewer regulations</td><td>New environmental or safety regulations raise costs</td></tr>
    <tr><td><b>Expectations</b></td><td>Prices expected to fall in future: sell now</td><td>Prices expected to rise: hold back stock</td></tr>
  </table></div>

  <h2>Key terms</h2>
  <ul>
    <li><b>Subsidy:</b> a payment by the government to producers to lower their costs: increases supply.</li>
    <li><b>Indirect tax:</b> a tax on goods and services that raises producers' costs: decreases supply.</li>
    <li><b>Productivity:</b> output per worker; technology raises it and lowers cost per unit.</li>
  </ul>
  <p class="note">On a diagram: shift right S to S₁ for an increase; left S to S₂ for a decrease. Always label the axes and both curves. <b>A price change of the good itself moves along; everything else shifts.</b></p>
'''
js = HEAD + COMMON + SUPJS + '''
Lib.stepper($("#stH"), { w: 760, h: 380, label: "Shifts of supply", base: { s: 0 }, draw: (s) => {
  let o = sAxes() + sLine(0, s.s === 0 ? "c2" : "c3", "S", s.s === 0 ? "t2" : "t3");
  if (s.s !== 0) o += sLine(s.s, s.s > 0 ? "c1" : "c4", s.s > 0 ? "S₁" : "S₂", s.s > 0 ? "t1" : "t4") + sDrop(50, 50) + sDot(50, 50, "", "dot1") + SV.circle(SX(50 + s.s), SYP(50), 7, s.s > 0 ? "dot2" : "dot4") + SV.line(SX(50), SYP(50), SX(50 + s.s), SYP(50), "c3");
  return o + SV.text(SX(0) - 8, SYP(50), "P", "sm bd", { "text-anchor": "end" });
}, steps: [
  { cap: "Supply curve S.", s: { s: 0 } },
  { cap: "Costs fall, or technology improves: supply <b>increases</b> and the curve shifts <b>right</b> to S₁. <b>More is supplied at every price</b>.", s: { s: 30 } },
  { cap: "A tax is placed on producers, or costs rise: supply <b>decreases</b> and the curve shifts <b>left</b> to S₂. <b>Less is supplied at every price</b>.", s: { s: -30 } },
] });
const TC = ["New technology is adopted", "Productivity rises and unit costs fall", "Firms can supply more at each price", "The supply curve shifts right", "An increase in supply"];
Lib.stepper($("#stT"), { w: 760, h: 380, label: "New technology", base: { n: 0 }, draw: mkChain(TC, "--good"), steps: chainSteps(["<b>New technology</b> is adopted.", "<b>Productivity rises</b> and unit costs fall.", "Firms can supply <b>more at each price</b>.", "The supply curve <b>shifts right</b>.", "An <b>increase in supply</b>."]) });
const TX = ["The government puts a tax on producers", "Production costs rise", "Firms supply less at each price", "The supply curve shifts left", "A decrease in supply"];
Lib.stepper($("#stX"), { w: 760, h: 380, label: "A tax on producers", base: { n: 0 }, draw: mkChain(TX, "--bad"), steps: chainSteps(["The government puts a <b>tax</b> on producers.", "<b>Production costs rise</b>.", "Firms supply <b>less at each price</b>.", "The supply curve <b>shifts left</b>.", "A <b>decrease in supply</b>."]) });

/* Lab 1 */
const FACT = [
  { n: "Costs of production fall", s: 25 }, { n: "Costs of production rise", s: -25 }, { n: "New technology", s: 30 }, { n: "A subsidy is introduced", s: 20 },
  { n: "A tax on producers", s: -20 }, { n: "Bad weather ruins harvest", s: -30 }, { n: "New firms enter", s: 20 }, { n: "More regulations", s: -15 },
];
function labF() {
  if (!$("#fa")) return; const f = FACT[+$("#fa").value], s = f.s;
  $("#fa1").textContent = s > 0 ? "Increase" : "Decrease"; $("#fa2").textContent = s > 0 ? "Right" : "Left"; $("#fa3").textContent = (s > 0 ? "+" : "−") + Math.abs(s);
  $("#fav").textContent = `${f.n}: supply ${s > 0 ? "increases" : "decreases"} and the curve shifts ${s > 0 ? "right" : "left"}. At the same price of $50 the quantity supplied changes from 50 to ${50 + s}.`;
  $("#labF").innerHTML = sAxes() + sLine(0, "c3", "S", "t3") + sLine(s, s > 0 ? "c1" : "c4", s > 0 ? "S₁" : "S₂", s > 0 ? "t1" : "t4") + sDrop(50, 50) + SV.circle(SX(50), SYP(50), 6, "dot1") + SV.circle(SX(50 + s), SYP(50), 7, s > 0 ? "dot2" : "dot4") + SV.line(SX(50), SYP(50), SX(50 + s), SYP(50), "c3");
}
Lib.slider($("#g1"), { id: "fa", label: "Choose a factor (0 to 7)", min: 0, max: 7, step: 1, value: 0, fmt: (v) => FACT[v].n, onInput: labF });
const SH = [
  { n: "Subsidy", d: "A payment to producers", e: "Lowers costs: supply shifts right." },
  { n: "Indirect tax", d: "A tax on goods", e: "Raises costs: supply shifts left." },
  { n: "Technology", d: "Faster, cheaper machines", e: "Raises productivity: supply shifts right." },
  { n: "Weather", d: "Drought for a farm good", e: "Cuts output: supply shifts left." },
  { n: "More firms", d: "New entrants", e: "More supply at each price: shifts right." },
];
button_table("shBtns", "shOut", SH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Example</th><th>Effect</th></tr><tr><td>${p.d}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each <b>increase</b> or <b>decrease</b> supply?", buckets: [{ label: "Increase in supply" }, { label: "Decrease in supply" }], items: [
  { text: "New technology cuts costs", b: 0 }, { text: "A government subsidy", b: 0 }, { text: "Good weather for crops", b: 0 }, { text: "New firms enter the market", b: 0 },
  { text: "A new tax on producers", b: 1 }, { text: "Wages for workers rise", b: 1 }, { text: "A drought hits farms", b: 1 }, { text: "Tighter safety regulations", b: 1 },
], done: "Right means increase; left means decrease." });
Lib.classify($("#cl2"), { prompt: "Does each <b>raise</b> or <b>lower</b> producers' costs?", buckets: [{ label: "Raises costs" }, { label: "Lowers costs" }], items: [
  { text: "A rise in the price of raw materials", b: 0 }, { text: "A higher minimum wage", b: 0 }, { text: "An indirect tax", b: 0 },
  { text: "A subsidy", b: 1 }, { text: "New technology", b: 1 }, { text: "Cheaper energy", b: 1 },
], done: "Costs drive supply." });
Lib.match($("#m1"), { prompt: "Match the cause to the effect on supply.", pairs: [
  ["Subsidy", "Supply shifts right"],
  ["Tax on producers", "Supply shifts left"],
  ["New technology", "Supply shifts right"],
  ["Rising wages", "Supply shifts left"],
  ["Drought", "Supply shifts left"],
  ["New firms enter", "Supply shifts right"],
], done: "Learn the pairs." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a subsidy increases supply</b>.", items: [
  "The government pays producers a subsidy",
  "Producers' costs fall",
  "Firms can supply more at every price",
  "The supply curve shifts right",
  "An increase in supply",
], done: "Subsidies lower costs." });
''' + calc_js([
    ("Supply at $50 rises from 50 to 80 units after new technology. What is the percentage increase?", 60, "30 ÷ 50 × 100 = <b>60%</b>.", None, None),
    ("A firm's cost per unit is $10 and a subsidy of $2 per unit is introduced. What is the cost per unit now ($)?", 8, "10 − 2 = <b>$8</b>.", None, None),
]) + mcq_js("qz1", [
    ("A shift of the supply curve to the right shows:", ["A fall in price", "An increase in supply", "A decrease in supply", "A contraction"], 1, "More at every price."),
    ("Which would shift a supply curve to the left?", ["A subsidy", "New technology", "A rise in wages", "More firms"], 2, "Costs rise."),
    ("A subsidy:", ["Raises costs", "Lowers costs and increases supply", "Reduces supply", "Raises demand"], 1, "Lower production costs."),
    ("A tax on producers causes:", ["An increase in supply", "A decrease in supply", "An extension", "A contraction"], 1, "Costs rise."),
    ("A shift of a supply curve is caused by:", ["The good's own price", "A change in a non-price factor", "A change in demand", "A movement along"], 1, "Costs, technology, taxes etc."),
]) + "\n" + cards_js([("Increase in supply", "A shift of the supply curve to the right."), ("Decrease in supply", "A shift of the supply curve to the left."), ("Subsidy", "A payment by the government to producers to lower costs."), ("Indirect tax", "A tax on goods and services, raising producers' costs."), ("Productivity", "Output per worker."), ("Technology", "Knowledge and methods that raise productivity."), ("Costs of production", "What firms pay to produce: wages, materials, energy, rent."), ("Regulation", "Government rules that firms must follow."), ("Non-price factor", "A factor other than the good's own price.")]) + "labF(); \n"
explore = '''
  <h2>Lab 1 · What shifts supply?</h2>
  <p>Choose a factor to see which way the curve shifts and by how much (illustrative).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Effect</small><strong id="fa1"></strong></div><div><small>Direction</small><strong id="fa2"></strong></div><div><small>Change at $50</small><strong id="fa3"></strong></div></div><div class="verdict" id="fav"></div></div></div>
    <svg id="labF" viewBox="0 0 760 340" role="img" aria-label="A shift of the supply curve"></svg>
  </div>

  <h2>Lab 2 · Subsidies, taxes and technology</h2>
  <p>Pick a term to see an example and its effect.</p>
  <div class="card"><div class="row" id="shBtns"></div><div id="shOut"></div></div>
'''
ex = exam(
    Q(1, "Analyse", 6, "Analyse the causes of a shift to the right in the supply curve of chocolate. (Feb/Mar 2023, P22 style)", "Costs fall, technology, subsidy, good weather for cocoa, more firms.",
      "[K|A fall in the cost of cocoa or other inputs reduces producers' costs,] [N|so chocolate firms can supply more at every price.] [K|New technology could raise productivity and lower unit costs,] [N|so supply increases.] [K|A government subsidy lowers costs.] [N|It encourages firms to produce more at each price.] [E|The size of the shift depends on how much costs fall.]", key=True),
    Q(2, "Explain", 4, "Explain two causes of a shift to the left in the supply curve of a good.", "A tax, rising costs, a drought, new regulations.",
      "[K|A tax on producers raises costs,] [N|so firms supply less at every price.] [K|A rise in wages or raw material costs reduces profit,] [N|so supply decreases at each price.]"),
    Q(3, "Explain", 4, "Explain how a subsidy would affect the supply of a good.", "Lowers costs; supply shifts right.",
      "[K|A subsidy is a payment from the government to producers.] [N|It lowers their costs of production,] [N|so they can supply more at every price and the supply curve shifts right.]"),
    Q(4, "Analyse", 6, "Analyse how advances in technology could affect the supply of a good.", "Productivity, cost, quality; supply right.",
      "[K|New technology can raise productivity and lower the cost of production.] [N|Firms can supply more at each price, so the supply curve shifts to the right.] [N|Lower costs may also lead to lower prices.] [E|The benefit depends on how quickly firms adopt the technology and the cost of investing.]", key=True),
)
tp = tips([
    ("Shifts are caused by non-price factors.", "Name the factor."),
    ("Right = increase; left = decrease.", "Say 'more at every price'."),
    ("Link to costs.", "Most supply shifts work through costs."),
    ("Subsidy increases supply; tax decreases it.", "Know both."),
    ("Draw S and S₁ and label axes.", "Marks for the diagram."),
], cmds("Explain", "Analyse"))
body = page(CL("2.3.3 Shifts of a supply curve"), "Shifts of a Supply Curve", "Causes of increases and decreases in supply and how they are shown on the diagram. Syllabus 2.3.3.",
    learn=learn, watch=watch(("Shifts of supply", "stH"), ("New technology", "stT"), ("A tax on producers", "stX")), explore=explore,
    practise=practise(("Increase or decrease?", "cl1", "card"), ("Raises or lowers costs?", "cl2", "card"), ("Match the cause", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Solar panels", "Better technology and cheaper production have lowered costs and increased supply.", "Technology."),
        rw("Fuel taxes", "Taxes on producers or suppliers raise costs and reduce supply at each price.", "Taxes."),
        rw("Droughts", "A drought cuts crop output and shifts the supply of the crop left.", "Weather."),
        rw("Agricultural subsidies", "Government payments to farmers lower costs and raise supply.", "Subsidies.")),
    exam=ex, tips=tp)
write("s233", body, js, "Shifts of a Supply Curve", "ig-supply-shifts")
