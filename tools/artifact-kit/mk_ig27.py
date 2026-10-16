"""Builds the three IGCSE Economics 2.7 Price elasticity of supply reviews (2.7.1 to 2.7.3).
Run: python3 tools/artifact-kit/mk_ig27.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"
DSJS = open(D / "mk_ig24.py").read().split("DSJS = '''")[1].split("'''")[0]
PESJS = '''
/* Supply curves through (50, 50). kind: 0 perfectly inelastic, 1 inelastic, 2 unitary, 3 elastic, 4 perfectly elastic */
function pesCurve(kind, cls, lab, t) {
  let o = "", lx = 0, ly = 0;
  if (kind === 0) { o = SV.line(X(50), Y(0), X(50), Y(105), cls || "c2"); lx = 50; ly = 100; }
  else if (kind === 4) { o = SV.line(X(0), Y(50), X(110), Y(50), cls || "c2"); lx = 112; ly = 50; }
  else { const k = kind === 1 ? 3 : kind === 2 ? 1 : 0.35; let qa = Math.max(0, 50 - 48 / k), qb = Math.min(108, 50 + 48 / k); const pa = 50 + k * (qa - 50), pb = 50 + k * (qb - 50); o = SV.line(X(qa), Y(pa), X(qb), Y(pb), cls || "c2"); lx = qb + 1; ly = pb; }
  return o + SV.text(X(lx) + 6, Y(ly), lab || "S", "lbl bd " + (t || "t2"));
}
function pesLabel(v) { if (v === 0) return "perfectly inelastic"; if (v === Infinity) return "perfectly elastic"; return v < 0.99 ? "inelastic" : v > 1.01 ? "elastic" : "unitary"; }
'''

# =========================================================== 2.7.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Price elasticity of supply (PES)</span> measures <b>how responsive the quantity supplied of a good is to a change in its price</b>. If a price rise lets producers increase output quickly and easily, supply is <b>elastic</b>. If producers cannot increase output much even when the price rises, supply is <b>inelastic</b>.</p></div>

  <h2>Elastic and inelastic supply</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Elastic supply</th><th>Inelastic supply</th></tr>
    <tr><td><b>Response</b></td><td>Quantity supplied changes by a <b>bigger percentage</b> than the price</td><td>Quantity supplied changes by a <b>smaller percentage</b> than the price</td></tr>
    <tr><td><b>Why</b></td><td>Spare capacity, stocks, flexible production, easy to hire</td><td>Production is slow, capacity is full, resources are specialised</td></tr>
    <tr><td><b>Examples</b></td><td>Mass-produced factory goods, T-shirts, services that need little equipment</td><td>Fresh farm crops during a season, housing, oil in the short run, fine art</td></tr>
  </table></div>

  <h2>Why it matters</h2>
  <ul>
    <li>PES shows <b>how quickly output can respond</b> when demand rises: if supply is elastic, prices rise less and output rises more; if inelastic, prices rise more.</li>
    <li>It helps firms plan production and governments predict the effects of policy.</li>
  </ul>
  <div class="formula">PES = % change in quantity supplied ÷ % change in price</div>
  <p class="note">PES is normally <b>positive</b> because supply curves slope upwards. The next review shows how to calculate it.</p>
'''
js = HEAD + COMMON + DSJS + PESJS + '''
Lib.stepper($("#stE"), { w: 760, h: 380, label: "Elastic vs inelastic supply", base: { n: 0 }, draw: (s) => {
  let o = axes() + pesCurve(3, "c2", "Elastic S", "t2") + SV.circle(X(50), Y(50), 6, "dot1");
  if (s.n >= 1) o += pesCurve(1, "c1", "Inelastic S", "t1");
  return o;
}, steps: [
  { cap: "A <b>flat</b> (elastic) supply curve: a small price change makes quantity supplied change a lot.", s: { n: 0 } },
  { cap: "A <b>steep</b> (inelastic) supply curve: quantity supplied hardly changes even when the price changes a lot.", s: { n: 1 } },
] });
const RS = ["Demand rises, so price rises 10%", "Producers want to supply more", "If they can raise output by more than 10% quickly: elastic", "If they can raise output by less than 10%: inelastic", "PES measures this response"];
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Responsiveness of supply", base: { n: 0 }, draw: mkChain(RS, "--accent"), steps: chainSteps(["Demand rises, so the <b>price rises</b> 10%.", "Producers want to <b>supply more</b>.", "If they can raise output by <b>more</b> than 10% quickly: <b>elastic</b>.", "If they can raise output by <b>less</b> than 10%: <b>inelastic</b>.", "<b>PES</b> measures this response."]) });

/* Lab 1 */
function labR() {
  if (!$("#ra") || !$("#rb")) return;
  const dp = +$("#ra").value, dq = +$("#rb").value, pes = dq / dp, lab = pesLabel(pes);
  $("#ra1").textContent = "+" + dq + "%"; $("#ra2").textContent = money(pes, 2); $("#ra3").textContent = lab.charAt(0).toUpperCase() + lab.slice(1);
  $("#rav").textContent = `A ${dp}% price rise increases quantity supplied by ${dq}%. The change in quantity (${dq}%) is ${dq > dp ? "bigger" : dq < dp ? "smaller" : "equal"} than the change in price (${dp}%), so supply is ${lab}.`;
  const q1 = 50 * (1 + dq / 100), p1 = 50 * (1 + dp / 100), k = (p1 - 50) / (q1 - 50), qa = Math.max(0, 50 + (5 - 50) / k), qb = Math.min(108, 50 + (95 - 50) / k), pa = 50 + k * (qa - 50), pb = 50 + k * (qb - 50);
  $("#labR").innerHTML = axes() + SV.line(X(qa), Y(pa), X(qb), Y(pb), "c2") + dsDrop(50, 50) + SV.circle(X(50), Y(50), 6, "dot1") + dsDrop(q1, p1) + SV.circle(X(q1), Y(p1), 7, "dot2") + SV.text(X(0) - 8, Y(50), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(50), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ra", label: "Price rise", min: 5, max: 40, step: 5, value: 10, fmt: (v) => "+" + v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Increase in quantity supplied", min: 2, max: 80, step: 2, value: 20, fmt: (v) => "+" + v + "%", onInput: labR });
const EL = [
  { n: "Factory-made T-shirts", t: "Elastic", w: "Easy to increase output; spare capacity; stocks." },
  { n: "Fresh strawberries in a season", t: "Inelastic", w: "Crops take months to grow; harvest is limited." },
  { n: "Housing", t: "Inelastic", w: "Building takes years; land is limited." },
  { n: "Fine art by a dead artist", t: "Perfectly inelastic", w: "Fixed supply." },
  { n: "Online software", t: "Elastic", w: "Copies cost almost nothing to supply." },
];
button_table("elBtns", "elOut", EL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Supply is</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is supply of each likely to be <b>elastic</b> or <b>inelastic</b>?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "Mass-produced plastic toys", b: 0 }, { text: "Online software", b: 0 }, { text: "A haircut", b: 0 },
  { text: "Housing in a city", b: 1 }, { text: "A farm crop between harvests", b: 1 }, { text: "Rare paintings", b: 1 },
], done: "Think about how quickly output can rise." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["PES", "Responsiveness of quantity supplied to a price change"],
  ["Elastic supply", "Quantity supplied changes by a bigger % than price"],
  ["Inelastic supply", "Quantity supplied changes by a smaller % than price"],
  ["Spare capacity", "Unused ability to produce more"],
  ["Stocks", "Goods held in storage ready to sell"],
  ["Flat supply curve", "Elastic"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why supply of strawberries is inelastic in the short run</b>.", items: [
  "The price of strawberries rises",
  "Farmers want to produce more",
  "Plants take months to grow",
  "Output can rise by only a small %",
  "Supply is inelastic",
], done: "Time limits supply." });
''' + calc_js([
    ("A 10% rise in price leads to a 5% rise in quantity supplied. What is the % change in quantity?", 5, "<b>5%</b>: smaller than 10%, so supply is inelastic.", None, None),
    ("A 5% rise in price raises quantity supplied by 15%. What is the % change in quantity?", 15, "<b>15%</b>: bigger than 5%, so supply is elastic.", None, None),
]) + mcq_js("qz1", [
    ("PES measures:", ["How price responds to quantity", "How quantity supplied responds to price", "Income and supply", "Demand and price"], 1, "Responsiveness of Qs to price."),
    ("Supply is elastic if:", ["Quantity changes by a smaller % than price", "Quantity changes by a bigger % than price", "Price does not change", "Quantity is fixed"], 1, "A big response."),
    ("Which is likely to have inelastic supply?", ["Online software", "Mass-produced goods", "Housing", "A haircut"], 2, "Takes years to build."),
    ("An elastic supply curve is:", ["Steep", "Flat", "Vertical", "Absent"], 1, "Flatter."),
    ("PES is normally:", ["Negative", "Positive", "Zero", "Infinite"], 1, "Supply slopes upwards."),
]) + "\n" + cards_js([("Price elasticity of supply", "A measure of the responsiveness of quantity supplied to a change in price."), ("Elastic supply", "Quantity supplied changes by a bigger percentage than price."), ("Inelastic supply", "Quantity supplied changes by a smaller percentage than price."), ("Spare capacity", "Unused ability to produce more."), ("Stocks", "Goods held in storage."), ("Responsiveness", "How much one variable reacts to another."), ("Output", "The quantity produced."), ("Short run", "A period too short to change capacity."), ("Long run", "A period long enough to change capacity.")]) + "labR(); \n"
explore = '''
  <h2>Lab 1 · How responsive is supply?</h2>
  <p>Set the price rise and the increase in quantity supplied and see whether supply is elastic or inelastic.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in quantity</small><strong id="ra1"></strong></div><div><small>PES</small><strong id="ra2"></strong></div><div><small>Supply is</small><strong id="ra3"></strong></div></div><div class="verdict" id="rav"></div></div></div>
    <svg id="labR" viewBox="0 0 760 340" role="img" aria-label="A supply curve showing responsiveness"></svg>
  </div>

  <h2>Lab 2 · Elastic or inelastic supply?</h2>
  <p>Pick a good to see its likely elasticity of supply and why.</p>
  <div class="card"><div class="row" id="elBtns"></div><div id="elOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define price elasticity of supply. (Oct/Nov 2022, P22 style)", "Responsiveness of quantity supplied to a price change.", "[K|Price elasticity of supply is a measure of the responsiveness] [K|of quantity supplied to a change in price.]"),
    Q(2, "Explain", 4, "Explain the difference between elastic and inelastic supply.", "Bigger vs smaller % change in quantity.",
      "[K|With elastic supply a change in price causes a bigger percentage change in quantity supplied.] [N|Producers can increase output quickly, for example using spare capacity.] [K|With inelastic supply quantity supplied changes by a smaller percentage than price.] [N|Producers cannot increase output easily, for example crops that take months to grow.]"),
    Q(3, "Identify", 2, "Identify two goods with inelastic supply.", "Housing, fresh crops, oil in the short run.", "[K|Housing.] [K|Fresh farm crops (or oil in the short run).]"),
)
tp = tips([
    ("PES = responsiveness of Qs to price.", "Say 'quantity supplied'."),
    ("Elastic = flat; inelastic = steep.", "For drawing."),
    ("Time and capacity decide it.", "Name them."),
    ("Compare % changes.", "Bigger or smaller."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.7.1 Definition of price elasticity of supply (PES)"), "Definition of Price Elasticity of Supply", "What PES measures and the difference between elastic and inelastic supply. Syllabus 2.7.1.",
    learn=learn, watch=watch(("Elastic vs inelastic supply", "stE"), ("Responsiveness of supply", "stR")), explore=explore,
    practise=practise(("Elastic or inelastic?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Housing supply", "Building takes years, so a rise in prices boosts output only slowly.", "Inelastic supply."),
        rw("Factory goods", "Firms with spare capacity can increase output of phones or shirts within weeks.", "Elastic supply."),
        rw("Seasonal fruit", "After a price rise growers cannot grow more until the next season.", "Inelastic in the short run."),
        rw("Digital goods", "Extra copies of software or music cost almost nothing to produce.", "Highly elastic supply.")),
    exam=ex, tips=tp)
write("q271", body, js, "Definition of Price Elasticity of Supply", "ig-pes-definition")

# =========================================================== 2.7.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>PES is calculated with the formula <b>PES = % change in quantity supplied ÷ % change in price</b>. Because supply slopes upwards, PES is <b>positive</b>. The value tells us whether supply is perfectly inelastic, inelastic, unitary, elastic or perfectly elastic.</p></div>

  <h2>Calculating PES</h2>
  <div class="formula">% change = (new − old) ÷ old × 100<br>PES = % change in quantity supplied ÷ % change in price</div>
  <p><b>Example:</b> price rises from $20 to $25 (+25%) and quantity supplied rises from 200 to 230 (+15%). PES = 15 ÷ 25 = <b>0.6</b>: <b>inelastic</b>.</p>

  <h2>Interpreting the value</h2>
  <div class="tw"><table class="t">
    <tr><th>PES</th><th>Name</th><th>Meaning</th><th>Curve</th></tr>
    <tr><td><b>0</b></td><td>Perfectly inelastic</td><td>Quantity supplied does not change at all</td><td>Vertical</td></tr>
    <tr><td><b>Between 0 and 1</b></td><td>Inelastic</td><td>Quantity changes by a smaller % than price</td><td>Steep; meets the quantity axis if extended</td></tr>
    <tr><td><b>1</b></td><td>Unitary</td><td>Quantity changes by the same % as price</td><td>Straight line from the origin</td></tr>
    <tr><td><b>Greater than 1</b></td><td>Elastic</td><td>Quantity changes by a bigger % than price</td><td>Flatter; meets the price axis if extended</td></tr>
    <tr><td><b>Infinity</b></td><td>Perfectly elastic</td><td>Producers will supply any quantity at one price; any lower price means none</td><td>Horizontal</td></tr>
  </table></div>
  <p class="note">Any straight-line supply curve through the <b>origin</b> has PES = 1 at every point, whatever its slope.</p>
'''
js = HEAD + COMMON + DSJS + PESJS + '''
const KN = [["Perfectly inelastic: PES = 0", 0], ["Inelastic: PES between 0 and 1", 1], ["Unitary: PES = 1", 2], ["Elastic: PES greater than 1", 3], ["Perfectly elastic: PES = infinity", 4]];
Lib.stepper($("#stK"), { w: 760, h: 380, label: "Five types of PES", base: { k: 0 }, draw: (s) => axes() + pesCurve(s.k, "c2", "S") + SV.text(X(3), Y(106), KN[s.k][0], "lbl bd t2"), steps: KN.map(([c, k]) => ({ cap: "<b>" + c + "</b>.", s: { k } })) });
const CL2 = ["Find the % change in quantity supplied", "Find the % change in price", "Divide: quantity ÷ price", "Compare with 1", "Say elastic or inelastic"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Calculating PES", base: { n: 0 }, draw: mkChain(CL2, "--accent"), steps: chainSteps(["Find the <b>% change in quantity supplied</b>.", "Find the <b>% change in price</b>.", "<b>Divide</b>: quantity ÷ price.", "<b>Compare with 1</b>.", "Say <b>elastic or inelastic</b>."]) });

/* Lab 1 */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc") || !$("#pd")) return;
  const p0 = +$("#pa").value, p1 = +$("#pb").value, q0 = +$("#pc").value, q1 = +$("#pd").value, dp = (p1 - p0) / p0 * 100, dq = (q1 - q0) / q0 * 100, pes = dp === 0 ? 0 : dq / dp;
  $("#pa1").textContent = money(dp, 1) + "%"; $("#pa2").textContent = money(dq, 1) + "%"; $("#pa3").textContent = money(pes, 2);
  $("#pav").textContent = `Price ${p0} → ${p1} is ${money(dp, 1)}%; quantity ${q0} → ${q1} is ${money(dq, 1)}%. PES = ${money(dq, 1)} ÷ ${money(dp, 1)} = ${money(pes, 2)}: supply is ${pes === 0 ? "perfectly inelastic" : pesLabel(pes)}.`;
  const k = pes < 0.01 ? 0 : pes < 0.99 ? 1 : pes < 1.01 ? 2 : 3;
  $("#labP").innerHTML = axes() + pesCurve(k, "c2", "S") + SV.circle(X(50), Y(50), 6, "dot1");
}
[["g1", "pa", "Old price ($)", 20, 5, 40], ["g2", "pb", "New price ($)", 25, 5, 40], ["g3", "pc", "Old quantity", 200, 50, 400], ["g4", "pd", "New quantity", 230, 50, 400]].forEach(([g, id, l, v, mn, mx]) => Lib.slider($("#" + g), { id, label: l, min: mn, max: mx, step: id === "pa" || id === "pb" ? 1 : 10, value: v, fmt: (x) => x, onInput: labP }));
const TY = [
  { n: "Perfectly inelastic", t: "Perfectly inelastic", c: "Vertical curve", e: "A one-off painting by a famous artist." },
  { n: "Inelastic", t: "Inelastic", c: "Steep curve", e: "Housing; farm crops in the short run." },
  { n: "Unitary", t: "Unitary", c: "Line through the origin", e: "Rare in practice." },
  { n: "Elastic", t: "Elastic", c: "Flat curve", e: "Factory goods with spare capacity." },
  { n: "Perfectly elastic", t: "Perfectly elastic", c: "Horizontal curve", e: "Producers supply any quantity at one price." },
];
button_table("tyBtns", "tyOut", TY, 0, (p) => `<div class="tw"><table class="t"><tr><th>Name</th><th>Curve</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.c}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of PES</b> is each value?", buckets: [{ label: "Inelastic (0 to 1)" }, { label: "Unitary (1)" }, { label: "Elastic (above 1)" }], items: [
  { text: "0.3", b: 0 }, { text: "0.8", b: 0 }, { text: "1.0", b: 1 }, { text: "1.5", b: 2 }, { text: "3.2", b: 2 }, { text: "0.5", b: 0 },
], done: "Compare the value with 1." });
Lib.classify($("#cl2"), { prompt: "Which <b>curve shape</b> matches each PES?", buckets: [{ label: "Vertical" }, { label: "Steep" }, { label: "Flat" }, { label: "Horizontal" }], items: [
  { text: "PES = 0", b: 0 }, { text: "PES = 0.4", b: 1 }, { text: "PES = 2.5", b: 2 }, { text: "PES = infinity", b: 3 },
], done: "Steeper means more inelastic." });
Lib.match($("#m1"), { prompt: "Match the term to its PES value.", pairs: [
  ["Perfectly inelastic", "PES = 0"],
  ["Inelastic", "PES between 0 and 1"],
  ["Unitary", "PES = 1"],
  ["Elastic", "PES greater than 1"],
  ["Perfectly elastic", "PES = infinity"],
  ["Formula", "% change in Qs ÷ % change in price"],
], done: "Learn the five." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>calculating PES</b>.", items: [
  "Calculate the % change in quantity supplied",
  "Calculate the % change in price",
  "Divide the first by the second",
  "State whether supply is elastic or inelastic",
], done: "Show every step." });
''' + calc_js([
    ("Price rises from $20 to $25 and quantity supplied rises from 200 to 230. Calculate PES (1 decimal place).", 0.6, "%ΔP = 25%, %ΔQ = 15%. PES = 15 ÷ 25 = <b>0.6</b>.", None, None),
    ("Price rises 10% and quantity supplied rises 25%. Calculate PES.", 2.5, "25 ÷ 10 = <b>2.5</b>: elastic.", None, None),
    ("PES is 0.5 and price rises 20%. By what percentage does quantity supplied rise?", 10, "0.5 × 20 = <b>10%</b>.", None, None),
    ("Price falls from $50 to $40 and quantity supplied falls from 100 to 90. Calculate PES.", 0.5, "%ΔP = −20%, %ΔQ = −10%. PES = −10 ÷ −20 = <b>0.5</b>.", None, None),
]) + mcq_js("qz1", [
    ("PES is calculated as:", ["%ΔP ÷ %ΔQs", "%ΔQs ÷ %ΔP", "ΔQ ÷ ΔP", "P ÷ Q"], 1, "Quantity supplied over price."),
    ("A PES of 2 means supply is:", ["Inelastic", "Unitary", "Elastic", "Perfectly inelastic"], 2, "Greater than 1."),
    ("A vertical supply curve shows:", ["Perfectly elastic supply", "Perfectly inelastic supply", "Unitary supply", "Elastic supply"], 1, "Quantity does not change."),
    ("A straight supply curve through the origin has PES:", ["Less than 1", "Equal to 1", "Greater than 1", "Zero"], 1, "Unitary."),
    ("A horizontal supply curve shows:", ["Perfectly inelastic supply", "Perfectly elastic supply", "Unitary supply", "No supply"], 1, "Infinite response."),
]) + "\n" + cards_js([("PES formula", "% change in quantity supplied ÷ % change in price."), ("Perfectly inelastic", "PES = 0: quantity does not change."), ("Inelastic", "PES between 0 and 1."), ("Unitary", "PES = 1."), ("Elastic", "PES above 1."), ("Perfectly elastic", "PES = infinity."), ("Percentage change", "(New − old) ÷ old × 100."), ("Origin", "The point where the axes meet."), ("Straight line through the origin", "Unitary PES everywhere.")]) + "labP(); \n"
explore = '''
  <h2>Lab 1 · PES calculator</h2>
  <p>Enter old and new price and quantity and see the PES and curve.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>% change in price</small><strong id="pa1"></strong></div><div><small>% change in quantity</small><strong id="pa2"></strong></div><div><small>PES</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 340" role="img" aria-label="A supply curve for the calculated PES"></svg>
  </div>

  <h2>Lab 2 · The five types</h2>
  <p>Pick a type to see its curve and an example.</p>
  <div class="card"><div class="row" id="tyBtns"></div><div id="tyOut"></div></div>
'''
ex = exam(
    Q(1, "Calculate", 3, "The price of a good rises from $20 to $25. Quantity supplied rises from 200 to 230. Calculate PES. (May/June 2023, P22 style)", "%ΔQs ÷ %ΔP.", "[A|%ΔP = 5 ÷ 20 × 100 = 25%; %ΔQs = 30 ÷ 200 × 100 = 15%.] [A|PES = 15 ÷ 25] [A|= 0.6 (inelastic).]"),
    Q(2, "Explain", 4, "Explain what a PES of 2.5 means.", "Elastic; quantity responds more than price.",
      "[K|A PES of 2.5 means supply is elastic.] [N|A 10% rise in price would cause quantity supplied to rise by 25%.] [N|Producers can respond strongly to price changes.]"),
    Q(3, "Identify", 2, "Identify the PES value for a perfectly inelastic supply curve.", "Zero.", "[K|Zero (0).] [K|Quantity supplied does not change.]"),
)
tp = tips([
    ("PES = %ΔQs ÷ %ΔP.", "Always use percentages."),
    ("Show every step.", "Percentage changes first."),
    ("PES is positive.", "Supply slopes up."),
    ("Through the origin: PES = 1.", "Whatever the slope."),
    ("State elastic or inelastic.", "Finish the answer."),
], cmds("Calculate", "Identify", "Explain"))
body = page(CL("2.7.2 Calculation of PES"), "Calculation and Interpretation of PES", "Calculating PES, interpreting its value and drawing supply curves for different elasticities. Syllabus 2.7.2.",
    learn=learn, watch=watch(("Five types of PES", "stK"), ("Calculating PES", "stC")), explore=explore,
    practise=practise(("Which type?", "cl1", "card"), ("Which curve?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the steps", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Housing in big cities", "PES is well below 1: price rises prompt little extra building in the short run.", "Inelastic supply."),
        rw("Garments", "Factories with spare capacity can scale output quickly.", "Elastic supply."),
        rw("Oil production", "Supply is inelastic in the short run because new wells take years.", "Inelastic supply."),
        rw("Taxi rides", "Surge pricing brings more drivers onto the road within minutes.", "Elastic supply.")),
    exam=ex, tips=tp)
write("q272", body, js, "Calculation and Interpretation of PES", "ig-pes-calculation")

# =========================================================== 2.7.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>How elastic or inelastic supply is depends mainly on <b>how quickly and easily producers can increase output</b> when the price rises. The key influences are <b>time</b>, <b>spare capacity</b>, <b>stocks</b>, <b>factor mobility</b> and the <b>nature of production</b>.</p></div>

  <h2>Determinants of PES</h2>
  <div class="tw"><table class="t">
    <tr><th>Determinant</th><th>Elastic supply</th><th>Inelastic supply</th></tr>
    <tr><td><b>Time period</b></td><td>Long run: firms can build factories, plant crops, train workers</td><td>Short run: capacity and resources are fixed</td></tr>
    <tr><td><b>Spare capacity</b></td><td>Firms have unused machines and workers</td><td>Firms already at full capacity</td></tr>
    <tr><td><b>Stocks (inventories)</b></td><td>Large stocks of finished goods can be sold quickly</td><td>No stocks (fresh or perishable goods)</td></tr>
    <tr><td><b>Mobility of factors</b></td><td>Resources can move easily from other uses</td><td>Resources are specialised and slow to move</td></tr>
    <tr><td><b>Ease of production</b></td><td>Simple, quick production; skilled labour readily available</td><td>Long production time (crops, houses, mines)</td></tr>
    <tr><td><b>Perishability</b></td><td>Goods can be stored</td><td>Fresh goods spoil, so supply cannot be stockpiled</td></tr>
    <tr><td><b>Availability of raw materials</b></td><td>Plentiful</td><td>Scarce or limited by nature</td></tr>
  </table></div>

  <h2>Examples</h2>
  <ul>
    <li><b>Mass-produced clothes:</b> elastic (spare capacity, stocks, simple production).</li>
    <li><b>Wheat in a year:</b> inelastic (growing season); <b>over several years</b> more elastic.</li>
    <li><b>Oil:</b> inelastic in the short run; wells take years to develop.</li>
    <li><b>Haircuts:</b> fairly elastic (easy to add stylists, though not stored).</li>
  </ul>
  <p class="note">An exam answer names the determinant, says whether it makes supply more or less elastic and links it to the <b>product in the question</b>.</p>
'''
js = HEAD + COMMON + DSJS + PESJS + '''
const SP = ["A firm has spare capacity and stocks", "Demand and price rise", "The firm uses idle machines and sells stocks", "Output rises quickly by a large %", "Supply is elastic"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Spare capacity and stocks", base: { n: 0 }, draw: mkChain(SP, "--good"), steps: chainSteps(["A firm has <b>spare capacity and stocks</b>.", "Demand and <b>price rise</b>.", "The firm uses <b>idle machines</b> and sells stocks.", "Output rises quickly by a <b>large %</b>.", "Supply is <b>elastic</b>."]) });
const FC = ["A farm's land and machinery are fixed", "Price of wheat rises", "Farmers cannot grow more until the next season", "Output rises only slightly", "Supply is inelastic in the short run"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "Fixed capacity", base: { n: 0 }, draw: mkChain(FC, "--bad"), steps: chainSteps(["A farm's <b>land and machinery are fixed</b>.", "The <b>price of wheat</b> rises.", "Farmers <b>cannot grow more</b> until the next season.", "Output rises only <b>slightly</b>.", "Supply is <b>inelastic</b> in the short run."]) });
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Time and elasticity", base: { k: 1 }, draw: (s) => axes() + pesCurve(s.k, "c2", s.k === 1 ? "Short-run S" : "Long-run S", "t2"), steps: [
  { cap: "In the <b>short run</b> firms are stuck with existing capacity: supply is <b>inelastic</b> (steep).", s: { k: 1 } },
  { cap: "In the <b>long run</b> firms can expand capacity: supply is <b>more elastic</b> (flatter).", s: { k: 3 } },
] });

/* Lab 1 */
function labD() {
  if (!$("#da") || !$("#db") || !$("#dc") || !$("#dd")) return;
  const t = +$("#da").value, c = +$("#db").value, s = +$("#dc").value, m = +$("#dd").value, score = t + c + s + m, pes = 0.1 + score * 0.14, lab = pesLabel(pes);
  $("#da1").textContent = money(pes, 2); $("#da2").textContent = lab.charAt(0).toUpperCase() + lab.slice(1); $("#da3").textContent = score + " / 20";
  $("#dav").textContent = `Time to adjust ${t}, spare capacity ${c}, stocks ${s} and factor mobility ${m} give a score of ${score}/20 and PES of about ${money(pes, 2)}: ${lab}. More time, more spare capacity, more stocks and more mobile resources make supply more elastic (illustrative model).`;
  const k = pes < 0.99 ? 1 : pes > 1.01 ? 3 : 2;
  $("#labD").innerHTML = axes() + pesCurve(k, "c2", "S") + SV.circle(X(50), Y(50), 6, "dot1");
}
Lib.slider($("#g1"), { id: "da", label: "Time to adjust (1 short, 5 long)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "Spare capacity (1 none, 5 lots)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g3"), { id: "dc", label: "Stocks of finished goods (1 none, 5 lots)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g4"), { id: "dd", label: "Mobility of resources (1 low, 5 high)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
const GD = [
  { n: "Fresh fruit (short run)", d: "Inelastic", w: "Perishable; limited by the growing season." },
  { n: "Housing", d: "Inelastic", w: "Takes years to build; land limited." },
  { n: "Mass-produced clothes", d: "Elastic", w: "Spare capacity and stocks; quick production." },
  { n: "Wheat (long run)", d: "More elastic", w: "Farmers can plant more acres over several seasons." },
  { n: "Online services", d: "Elastic", w: "Additional supply costs little." },
];
button_table("gdBtns", "gdOut", GD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Supply is</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each make supply more <b>elastic</b> or more <b>inelastic</b>?", buckets: [{ label: "More elastic" }, { label: "More inelastic" }], items: [
  { text: "Spare capacity", b: 0 }, { text: "Large stocks of goods", b: 0 }, { text: "A long time period", b: 0 }, { text: "Mobile, flexible resources", b: 0 },
  { text: "Firms at full capacity", b: 1 }, { text: "Perishable goods", b: 1 }, { text: "A short time period", b: 1 }, { text: "Specialised resources", b: 1 },
], done: "Time, capacity, stocks, mobility." });
Lib.classify($("#cl2"), { prompt: "Is supply of each likely to be <b>elastic</b> or <b>inelastic</b> in the short run?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "Factory-made shirts", b: 0 }, { text: "Online software", b: 0 },
  { text: "Housing", b: 1 }, { text: "A crop between harvests", b: 1 }, { text: "Fresh fish", b: 1 },
], done: "Apply the determinants." });
Lib.match($("#m1"), { prompt: "Match the determinant to its effect.", pairs: [
  ["Spare capacity", "More elastic"],
  ["Large stocks", "More elastic"],
  ["Long time period", "More elastic"],
  ["Perishable goods", "More inelastic"],
  ["Specialised factors", "More inelastic"],
  ["Full capacity", "More inelastic"],
], done: "Learn the determinants." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why housing supply is inelastic</b>.", items: [
  "House prices rise",
  "Builders want to build more",
  "Planning and construction take years and land is limited",
  "Output rises only slightly in the short run",
  "Supply is inelastic",
], done: "Time and land limits." });
''' + calc_js([
    ("A good has a PES of 2. Price rises 5%. By what percentage does quantity supplied rise?", 10, "2 × 5 = <b>10%</b>.", None, None),
    ("A firm at 90% capacity can raise output by at most 11% (to full capacity). Price rises 20%. What is the maximum PES (1 decimal place)?", 0.6, "11 ÷ 20 ≈ <b>0.6</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which makes supply more elastic?", ["Full capacity", "Spare capacity", "Perishable goods", "A short time period"], 1, "Easy to produce more."),
    ("Supply of fresh strawberries is inelastic in the short run because:", ["They are stored", "They take time to grow and spoil quickly", "Costs are zero", "Demand is high"], 1, "Growing season and perishability."),
    ("In the long run supply tends to be:", ["More inelastic", "More elastic", "Unchanged", "Zero"], 1, "Time to expand capacity."),
    ("Which good has the most elastic supply?", ["Housing", "Fresh fruit", "Factory-made clothes", "A rare painting"], 2, "Spare capacity and stocks."),
    ("Stocks of finished goods make supply:", ["More inelastic", "More elastic", "Zero", "Fixed"], 1, "Can be sold quickly."),
]) + "\n" + cards_js([("Determinants of PES", "Factors that decide how elastic or inelastic supply is."), ("Spare capacity", "Unused productive capacity."), ("Stocks", "Goods held in storage."), ("Mobility of factors", "How easily resources move between uses."), ("Perishable good", "A good that spoils quickly."), ("Time period", "Supply is more elastic in the long run."), ("Short run", "A period too short to change capacity."), ("Long run", "A period long enough to adjust."), ("Production time", "How long it takes to make more.")]) + "labD(); \n"
explore = '''
  <h2>Lab 1 · Score a good</h2>
  <p>Set the four determinants for a good and see its likely PES.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Likely PES</small><strong id="da1"></strong></div><div><small>Supply is</small><strong id="da2"></strong></div><div><small>Score</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 340" role="img" aria-label="A supply curve for the scored good"></svg>
  </div>

  <h2>Lab 2 · Goods and their elasticity</h2>
  <p>Pick a good to see why its supply is elastic or inelastic.</p>
  <div class="card"><div class="row" id="gdBtns"></div><div id="gdOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two influences on the price elasticity of supply of a good.", "Time, spare capacity, stocks, mobility.",
      "[K|The time period affects PES.] [N|In the short run firms cannot easily expand capacity so supply is inelastic, but in the long run they can build more so supply is more elastic.] [K|Spare capacity matters.] [N|Firms with unused machines and workers can raise output quickly, so supply is elastic.]"),
    Q(2, "Explain", 4, "Explain why the supply of fresh fruit is likely to be inelastic in the short run.", "Growing time; perishable; no stocks.",
      "[K|Fruit takes months to grow, so farmers cannot raise output quickly.] [N|It is perishable and cannot be stored,] [N|so supply cannot be increased by selling stocks: supply is inelastic.]"),
    Q(3, "Analyse", 6, "Analyse how the PES of a good could affect the change in price when demand rises.", "Elastic: price rises less, quantity more; inelastic: price rises more.",
      "[K|If supply is elastic, firms can raise output easily when demand rises.] [N|Quantity rises by a large amount and the price rises only a little.] [N|If supply is inelastic, output cannot rise much,] [N|so the price rises by more and quantity by less.] [E|The effect is larger in the short run.]", key=True),
)
tp = tips([
    ("Learn the determinants.", "Time, spare capacity, stocks, mobility, perishability."),
    ("Say elastic or inelastic.", "And name the good."),
    ("Link to the product.", "Don't just list."),
    ("Short run vs long run.", "Long run is more elastic."),
], cmds("Explain", "Analyse"))
body = page(CL("2.7.3 Determinants of PES"), "Determinants of PES", "The main influences on whether supply is elastic or inelastic. Syllabus 2.7.3.",
    learn=learn, watch=watch(("Spare capacity and stocks", "stS"), ("Fixed capacity", "stF"), ("Time and elasticity", "stT")), explore=explore,
    practise=practise(("More elastic or inelastic?", "cl1", "card"), ("Elastic or inelastic in the short run?", "cl2", "card"), ("Match the determinant", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Housing", "New homes take years to plan and build, so supply is inelastic.", "Time and land."),
        rw("Clothing factories", "With spare capacity, manufacturers can ramp up output within weeks.", "Spare capacity."),
        rw("Agriculture", "Growing seasons limit short-run supply of crops.", "Production time."),
        rw("Oil", "New fields take years to develop, so supply responds slowly.", "Long lead times.")),
    exam=ex, tips=tp)
write("q273", body, js, "Determinants of PES", "ig-pes-determinants")
