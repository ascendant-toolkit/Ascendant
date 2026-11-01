// Data: unit n has MB = 110 - 10n and MC = 20 + 5n, so MB = MC at 6 units
const N = 10, MBv = [], MCv = [], NB = [], CUM = [];
for (let n = 1; n <= N; n++) { MBv.push(110 - 10 * n); MCv.push(20 + 5 * n); NB.push(MBv[n - 1] - MCv[n - 1]); CUM.push((CUM[n - 2] || 0) + NB[n - 1]); }
const EFF = 6, MAXS = CUM[EFF - 1];
const surplus = (q) => (q ? CUM[q - 1] : 0);

const dollars = (v) => (v < 0 ? "−$" + -v : "$" + v);
$("#dataT").innerHTML = `<tr><th>Output (units)</th><th>MB ($)</th><th>MC ($)</th><th>Net benefit (MB − MC)</th><th>Total surplus ($)</th><th>Verdict</th></tr>` +
  MBv.map((m, i) => `<tr${i + 1 === EFF ? ' style="background:var(--good-soft)"' : ""}><td>${i + 1}</td><td>${m}</td><td>${MCv[i]}</td><td>${dollars(NB[i])}</td><td>${CUM[i]}</td><td>${NB[i] > 0 ? "Worth producing" : NB[i] === 0 ? "Efficient point" : "Costs more than it is worth"}</td></tr>`).join("");
$("#lossT").innerHTML = `<tr><th>Output held at</th><th>Total surplus ($)</th><th>Welfare loss ($)</th><th>Units left out</th></tr>` +
  [5, 4, 3, 2, 1].map((q) => `<tr><td>${q} units</td><td>${surplus(q)}</td><td><b>${MAXS - surplus(q)}</b></td><td>${q + 1} to ${EFF}</td></tr>`).join("");

/* bar diagram: unit n spans x from n-1 to n; green strip = net benefit kept, red = forgone (under), amber = overproduction */
function draw(s, W, H) {
  const lim = Math.round(s.lim), x0 = 70, x1 = W - 20, top = 30, bot = H - 60;
  const X = (q) => x0 + (q / N) * (x1 - x0), Y = (v) => bot - (v / 120) * (bot - top), bw = (x1 - x0) / N;
  let o = SV.line(x0, bot, x1, bot) + SV.line(x0, bot, x0, top) + SV.text(x1, bot + 40, "Output (units)", "sm", { "text-anchor": "end" }) + SV.text(x0 - 8, top - 8, "$ per unit", "sm");
  for (let v = 20; v <= 100; v += 20) o += SV.line(x0, Y(v), x1, Y(v), "gr") + SV.text(x0 - 8, Y(v) + 4, v, "sm", { "text-anchor": "end" });
  for (let n = 1; n <= N; n++) {
    const lo = Math.min(MBv[n - 1], MCv[n - 1]), hi = Math.max(MBv[n - 1], MCv[n - 1]), gx = X(n - 1) + 3, w = bw - 6, made = n <= lim;
    if (NB[n - 1] > 0) {
      if (made) o += SV.rect(gx, Y(hi), w, Y(lo) - Y(hi), "f3", { opacity: 0.85 });
      else if (s.loss) o += SV.rect(gx, Y(hi), w, Y(lo) - Y(hi), "f2", { opacity: 0.8 });
    } else if (NB[n - 1] < 0 && made && s.loss) o += SV.rect(gx, Y(hi), w, Y(lo) - Y(hi), "f4", { opacity: 0.9 });
    o += SV.line(gx, Y(MBv[n - 1]), gx + w, Y(MBv[n - 1]), "c1", { "stroke-width": 4 }) + SV.line(gx, Y(MCv[n - 1]), gx + w, Y(MCv[n - 1]), "c2", { "stroke-width": 4 });
    o += SV.text(X(n - 0.5), bot + 17, n, "sm", { "text-anchor": "middle" });
  }
  o += SV.text(X(0.5) - 2, Y(MBv[0]) - 8, "MB", "lbl bd t1") + SV.text(X(N - 0.5), Y(MBv[N - 1]) + 20, "MB", "lbl bd t1", { "text-anchor": "middle" }) + SV.text(X(0.5), Y(MCv[0]) + 20, "MC", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(X(N - 0.5), Y(MCv[N - 1]) - 8, "MC", "lbl bd t2", { "text-anchor": "middle" });
  if (s.eff) o += SV.line(X(EFF), top + 10, X(EFF), bot, "dash t3", { stroke: "var(--good)", "stroke-width": 2 }) + SV.text(X(EFF) + 6, top + 22, "Efficient: MB = MC = $50", "sm bd t3");
  if (lim > 0 && lim < N) o += SV.line(X(lim), top + 10, X(lim), bot, "dash", { stroke: "var(--ink)", "stroke-width": 2 });
  const sp = surplus(lim);
  o += SV.text(x1, H - 6, `Output ${lim}: surplus $${sp}${s.loss ? " · welfare loss $" + (MAXS - sp) : ""}`, "lbl bd", { "text-anchor": "end" });
  return o;
}
$("#picS").innerHTML = draw({ lim: 3, loss: 1, eff: 1 }, 780, 400);

Lib.stepper($("#stA"), { w: 780, h: 400, label: "Bar diagram showing the net benefit forgone as output is cut below the efficient level", base: { lim: 0, loss: 0, eff: 0 }, draw: (s) => draw(s, 780, 400), tween: 700, dwell: 5600, steps: [
  { s: { lim: 0, loss: 0, eff: 0 }, cap: "Each pair of bars is one unit. Blue is what consumers would pay for it (MB). Red is what it costs to make (MC). Early units are worth far more than they cost." },
  { s: { lim: 6, loss: 1, eff: 1 }, cap: "Produce up to the 6th unit and every unit is worth at least its cost. The green strips are the net benefit. Total surplus is at its maximum of $225, at MB = MC." },
  { s: { lim: 3, loss: 0, eff: 1 }, cap: "Now suppose output is cut to 3 units, for example by a firm with market power. Surplus kept falls to $180." },
  { s: { lim: 3, loss: 1, eff: 1 }, cap: "The 4th unit is worth $70 to buyers and costs $40 to make: $30 of net benefit lost. The 5th loses $15 and the 6th loses $0. The red strips total <b>$45</b>, the welfare loss." },
  { s: { lim: 1, loss: 1, eff: 1 }, cap: "Cut output to 1 unit and units 2 to 6 are left out. The welfare loss grows to <b>$150</b>. The bigger the cut, the bigger the loss." },
  { s: { lim: 8, loss: 1, eff: 1 }, cap: "The mistake can go the other way. Beyond 6 units, MC is above MB (amber), so extra output wastes resources. Allocative efficiency needs the right output, not just more or less." },
] });

let pr = 6;
function lab(q) {
  pr = q;
  $("#r1").textContent = q ? MBv[q - 1] : "–"; $("#r2").textContent = q ? MCv[q - 1] : "–"; $("#r3").textContent = surplus(q); $("#r4").textContent = MAXS - surplus(q);
  $("#rv").textContent = q < EFF ? `Underproduction: units ${q + 1} to ${EFF} are worth more than they cost, so $${MAXS - surplus(q)} of surplus is not gained.`
    : q === EFF ? "Allocatively efficient: MB = MC. Total surplus is at its maximum." : `Overproduction: units ${EFF + 1} to ${q} cost more than they are worth, losing $${MAXS - surplus(q)}.`;
  $("#labA").innerHTML = draw({ lim: q, loss: 1, eff: 1 }, 780, 400);
}
Lib.slider($("#g1"), { id: "qq", label: "Units produced: ", min: 0, max: 10, step: 1, value: 3, fmt: (v) => v, onInput: lab });

Lib.calc($("#c1"), { qs: [
  { q: "What is the allocatively efficient output (units)?", a: 6, sol: "MB = MC at the 6th unit: both are <b>$50</b>." },
  { q: "What is the net benefit of the 3rd unit ($)?", a: 45, hint: "MB − MC for the 3rd unit: 80 − 35.", sol: "80 − 35 = <b>$45</b>." },
  { q: "Output is 4 units. What is the total surplus ($)?", a: 210, sol: "75 + 60 + 45 + 30 = <b>$210</b>." },
  { q: "Output is held at 2 units. What is the welfare loss ($)?", a: 90, hint: "Maximum surplus is $225. Surplus at 2 units is 75 + 60.", sol: "225 − 135 = <b>$90</b>." },
  { q: "By how much does the welfare loss increase when output falls from 3 units to 1 unit ($)?", a: 105, sol: "Loss at 1 unit = 225 − 75 = 150. Loss at 3 units = 225 − 180 = 45. Increase = <b>$105</b>." },
  { q: "Output is 8 units. What is the welfare loss from overproduction ($)?", a: 45, hint: "Surplus at 8 units is 180.", sol: "225 − 180 = <b>$45</b> (units 7 and 8 lose $15 and $30)." },
] });
Lib.classify($("#cl1"), { prompt: "Place each situation in the right bucket (use the table: efficient output is 6 units).", buckets: [{ label: "Underproduction" }, { label: "Allocatively efficient" }, { label: "Overproduction" }], items: [
  { text: "Output 2: MB $90, MC $30", b: 0 }, { text: "Output 4: MB $70, MC $40", b: 0 }, { text: "Output 6: MB $50, MC $50", b: 1 },
  { text: "Output 8: MB $30, MC $60", b: 2 }, { text: "Output 10: MB $10, MC $70", b: 2 }, { text: "A cartel holds output below the competitive level", b: 0 },
], done: "Compare MB with MC at the last unit." });
Lib.order($("#o1"), { prompt: "Put the explanation of why a cut in output reduces allocative efficiency in order.", items: [
  "Output is held below the level where MB = MC",
  "At the last unit produced, marginal benefit is greater than marginal cost",
  "The units that are left out would each have added more to benefit than to cost",
  "The net benefit on those missing units is forgone, creating a welfare loss",
  "Total surplus is below its maximum, so resources are not allocated efficiently",
  "Evaluate: externalities, finite resources or reinvested profit could change the overall judgement",
], done: "This chain works for a 6 to 12 mark answer." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Marginal benefit", "Extra benefit from one more unit, shown by willingness to pay"],
  ["Marginal cost", "Extra cost of producing one more unit"],
  ["Net benefit", "MB minus MC on a unit"],
  ["Total surplus", "Consumer surplus plus producer surplus"],
  ["Welfare loss", "Fall in total surplus when output is not at the efficient level"],
], done: "Five words to use in every answer." });
Lib.quiz($("#qz1"), { qs: [
  { q: "A market produces where MB is greater than MC on the last unit. This means:", opts: ["it is allocatively efficient", "it is producing too much", "it is producing too little", "profit is zero"], a: 2, why: "Another unit would be worth more than it costs, so output is below the efficient level." },
  { q: "Why does the welfare loss rise as output is cut further below the efficient level?", opts: ["MC falls as output falls", "more units with positive net benefit are left out", "consumer surplus rises", "price falls"], a: 1, why: "Each extra unit left out removes a positive net benefit." },
  { q: "At the efficient output the net benefit of the last unit is:", opts: ["positive and at its maximum", "negative", "zero", "equal to total surplus"], a: 2, why: "MB = MC, so MB − MC = 0, and total surplus has stopped rising." },
  { q: "A monopolist restricts output to raise price. Which is most likely?", opts: ["Total surplus rises", "Price is above marginal cost and there is a welfare loss", "Allocative efficiency improves", "Marginal benefit falls to zero"], a: 1, why: "Output below MB = MC leaves price above MC and creates a welfare loss." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Welfare loss", "The fall in total surplus when output is not at the allocatively efficient level."],
  ["Allocative efficiency", "Output where MB = MC (P = MC with no externalities): resources go to the goods consumers value most."],
  ["Net benefit of a unit", "Marginal benefit minus marginal cost. Positive means the unit is worth producing."],
  ["Underproduction", "Output below the efficient level: MB is above MC on the last unit."],
] });
