/* ---------- LRAC geometry: AC(q) = 6 + 0.0008 (q - 100)^2, minimum efficient scale at q = 100 ---------- */
const MES = 100, AMIN = 6;
const AC = (q) => AMIN + 0.0008 * (q - MES) ** 2;
const CX = (q) => 70 + q * 3.1, CY = (c) => 320 - c * 17;
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
function cAxes() {
  return SV.line(70, 320, 700, 320) + SV.line(70, 320, 70, 40) + SV.text(700, 348, "Output (units per month)", "sm", { "text-anchor": "end" }) + SV.text(76, 40, "Long-run average cost ($)", "sm");
}
function curve(frac) {
  const pts = [];
  for (let q = 0; q <= 200 * frac + 0.01; q += 4) pts.push([CX(q), CY(AC(q))]);
  return pts.length > 1 ? SV.path(Lib.ptsPath(pts), "c1") : "";
}

/* ---------- Watch 2: types of integration ---------- */
function box(x, y, w, h, label, o = {}) {
  return SV.rect(x, y, w, h, "ax", { rx: 10, fill: "none", ...(o.op !== undefined ? op(o.op) : {}) }) + SV.text(x + w / 2, y + h / 2 + 5, label, "lbl bd", { "text-anchor": "middle", ...(o.op !== undefined ? op(o.op) : {}) });
}
function arrow(x1, y1, x2, y2, c, o) {
  const ang = Math.atan2(y2 - y1, x2 - x1), hx = x2, hy = y2, k = 11, p = 6;
  const ux = Math.cos(ang), uy = Math.sin(ang);
  return SV.line(x1, y1, x2 - ux * k, y2 - uy * k, c, o) + `<polygon points="${hx},${hy} ${hx - ux * k - uy * p},${hy - uy * k + ux * p} ${hx - ux * k + uy * p},${hy - uy * k - ux * p}" class="${c === "ax" ? "arr" : c.replace("c", "t")}"${at(o)}/>`;
}
const IB = { farm: [20, 150], mill: [170, 150], bak: [320, 150], shop: [470, 150], cust: [620, 150], rival: [320, 280], toy: [560, 280], branch: [320, 20] }, IW = 110, IH = 60;
function integ(s) {
  let o = "";
  const fill = (k, cl, v) => v > 0 ? SV.rect(IB[k][0], IB[k][1], IW, IH, cl, { rx: 10, ...op(v) }) : "";
  o += fill("rival", "f1", s.h) + fill("mill", "f4", s.b) + fill("shop", "f3", s.f) + fill("toy", "f2", s.c) + fill("branch", "f1", s.o);
  o += SV.rect(IB.bak[0], IB.bak[1], IW, IH, "f1", { rx: 10, opacity: 0.55 });
  o += box(...IB.farm, IW, IH, "Farm") + box(...IB.mill, IW, IH, "Flour mill") + box(...IB.bak, IW, IH, "Bakery X") + box(...IB.shop, IW, IH, "Shops") + box(...IB.cust, IW, IH, "Customers");
  o += box(IB.rival[0], IB.rival[1], IW, IH, "Rival bakery", { op: 0.35 + 0.65 * s.h }) + box(IB.toy[0], IB.toy[1], IW, IH, "Toy maker", { op: 0.35 + 0.65 * s.c }) + box(IB.branch[0], IB.branch[1], IW, IH, "New branch", { op: Math.max(0, s.o) });
  [["farm", "mill"], ["mill", "bak"], ["bak", "shop"], ["shop", "cust"]].forEach(([a, b]) => { o += arrow(IB[a][0] + IW + 2, 180, IB[b][0] - 2, 180, "ax"); });
  o += SV.text(380, 130, "supply chain flows left to right", "sm", { "text-anchor": "middle" });
  if (s.h > 0) o += arrow(375, 213, 375, 278, "c1", op(s.h)) + SV.text(385, 250, "HORIZONTAL: same stage", "lbl bd t1", op(s.h));
  if (s.b > 0) o += arrow(318, 168, 284, 168, "c4", op(s.b)) + SV.text(225, 252, "BACKWARD: buys its supplier", "lbl bd t4", { "text-anchor": "middle", ...op(s.b) }) + SV.text(225, 270, "(earlier in the chain)", "sm", { "text-anchor": "middle", ...op(s.b) });
  if (s.f > 0) o += arrow(432, 168, 468, 168, "c3", op(s.f)) + SV.text(525, 252, "FORWARD: buys its seller", "lbl bd t3", { "text-anchor": "middle", ...op(s.f) }) + SV.text(525, 270, "(later in the chain)", "sm", { "text-anchor": "middle", ...op(s.f) });
  if (s.c > 0) o += arrow(430, 205, 568, 284, "c2", op(s.c)) + SV.text(620, 360, "CONGLOMERATE: unrelated industry", "lbl bd t2", { "text-anchor": "middle", ...op(s.c) });
  if (s.o > 0) o += arrow(375, 148, 375, 84, "c1", op(s.o)) + SV.text(495, 55, "ORGANIC: built from own profit", "lbl bd t1", op(s.o));
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 380, label: "A supply chain with a bakery in the middle, showing horizontal, backward, forward and conglomerate integration and organic growth", base: { h: 0, b: 0, f: 0, c: 0, o: 0 }, draw: integ, tween: 800, dwell: 5200, steps: [
  { cap: "<b>The supply chain.</b> A farm grows wheat, a mill makes flour, <b>Bakery X</b> makes bread, shops sell it. Other bakeries compete with X.", s: {} },
  { cap: "<b>Horizontal integration.</b> X takes over a <b>rival bakery</b>: same industry, same stage. Possible gains: economies of scale and less competition. Possible harm: market power.", s: { h: 1 } },
  { cap: "<b>Backward vertical integration.</b> X buys the <b>mill that supplies it</b>. It secures supply and may cut a supplier mark-up.", s: { b: 1 } },
  { cap: "<b>Forward vertical integration.</b> X buys the <b>shops that sell its bread</b>. It secures outlets and keeps the retail margin.", s: { f: 1 } },
  { cap: "<b>Conglomerate integration.</b> X buys a <b>toy maker</b>. Unrelated industry, so risk is spread: a fall in demand for bread does not hit toys.", s: { c: 1 } },
  { cap: "<b>Organic growth.</b> No other firm is bought. X uses <b>its own profit</b> to open a new branch. Slower, but X keeps control and its culture.", s: { o: 1 } },
] });


/* ---------- Lab 1: type of deal ---------- */
function labDeal() {
  if (!$("#tg")) return;
  const t = +$("#tg").value, names = ["A flour mill (a supplier)", "A rival bakery", "A chain of cafés (a customer)", "A mobile phone maker"], types = ["Backward vertical", "Horizontal", "Forward vertical", "Conglomerate"], mot = ["Secure supplies and cut input costs", "Economies of scale and market share", "Secure outlets for the bakery's products", "Spread risk by diversifying"];
  const why = ["The target is earlier in the supply chain.", "The target is in the same industry at the same stage.", "The target is later in the supply chain, closer to the customer.", "The target is in an unrelated industry."];
  $("#a1").textContent = ["Flour mill", "Rival bakery", "Café chain", "Phone maker"][t]; $("#a2").textContent = types[t]; $("#a3").textContent = ["Secure supplies", "Economies of scale", "Secure outlets", "Spread risk"][t];
  $("#av").textContent = `The bakery buys ${names[t].toLowerCase()}. ${why[t]} This is ${types[t].toLowerCase()} integration. Typical motive: ${mot[t].toLowerCase()}.`;
  const box = (x, y, w, h, l, on, c) => SV.rect(x, y, w, h, on ? c : "f1", { opacity: on ? 0.95 : 0.35, rx: 8 }) + SV.text(x + w / 2, y + h / 2 + 4, l, "lbl bd", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
  let o = box(20, 100, 100, 50, "Flour mill", t === 0, "f4") + box(160, 100, 100, 50, "Bakery", true, "f1") + box(300, 100, 100, 50, "Cafés", t === 2, "f3") + box(160, 10, 100, 50, "Rival bakery", t === 1, "f2") + box(160, 200, 100, 50, "Phone maker", t === 3, "f4");
  o += SV.line(120, 125, 160, 125, "gr", { "stroke-width": 2 }) + SV.line(260, 125, 300, 125, "gr", { "stroke-width": 2 }) + SV.text(70, 175, "backward", "sm", { "text-anchor": "middle" }) + SV.text(350, 175, "forward", "sm", { "text-anchor": "middle" }) + SV.text(110, 40, "horizontal", "sm", { "text-anchor": "end" }) + SV.text(110, 232, "conglomerate", "sm", { "text-anchor": "end" });
  $("#labV").innerHTML = o;
}
Lib.slider($("#g8"), { id: "tg", label: "Who does the bakery buy? (0 supplier, 1 rival, 2 café chain, 3 unrelated firm): ", min: 0, max: 3, step: 1, value: 0, fmt: (v) => v, onInput: labDeal });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Put each takeover or merger in the right bucket.",
  buckets: [{ label: "Horizontal" }, { label: "Backward vertical" }, { label: "Forward vertical" }, { label: "Conglomerate" }],
  items: [
    { text: "A supermarket chain buys a rival supermarket chain", b: 0 }, { text: "Two banks merge", b: 0 },
    { text: "A bakery buys a flour mill", b: 1 }, { text: "A steel maker buys an iron-ore mine", b: 1 }, { text: "A phone maker buys a company that designs its chips", b: 1 },
    { text: "A car maker buys a chain of showrooms", b: 2 }, { text: "A brewery buys pubs", b: 2 }, { text: "A film studio buys a cinema chain", b: 2 },
    { text: "A mobile phone company buys a chocolate maker", b: 3 }, { text: "A tobacco company buys a snack-food company", b: 3 },
  ], done: "Test: who supplies whom? The supplier is backward, the seller is forward, the same stage is horizontal, and unrelated is conglomerate.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Organic growth", "Growth using the firm's own resources"],
  ["Merger", "Two firms agree to join and form one new company"],
  ["Takeover", "One firm buys another, usually by buying its shares"],
  ["Horizontal integration", "Joining with a firm in the same industry at the same stage"],
  ["Backward vertical integration", "Buying a firm earlier in the supply chain, such as a supplier"],
  ["Forward vertical integration", "Buying a firm later in the supply chain, such as a retailer"],
  ["Conglomerate integration", "Joining with a firm in an unrelated industry"],
  ["Demerger", "A firm splits into separate businesses"],
], done: "Eight words for the types of growth." });
Lib.calc($("#c1"), { qs: [
  { q: "A company has 10 million shares priced at $5. A bidder offers a 40% premium. What is the total value of the bid ($ million)?", a: 70, sol: "Offer per share = 5 × 1.4 = $7. Total = 10 million × $7 = <b>$70 million</b>." },
  { q: "A firm's sales rise from $20 million to $23 million through organic growth. What is the growth rate (%)?", a: 15, sol: "(23 − 20) ÷ 20 × 100 = <b>15%</b>." },
  { q: "A bidder offers $12 a share for a company with 5 million shares. What is the total value of the bid ($ million)?", a: 60, sol: "12 × 5 = <b>$60 million</b>." },
  { q: "A firm's sales rise from $50 million to $55 million through organic growth. What is the growth rate (%)?", a: 10, sol: "(55 − 50) ÷ 50 × 100 = <b>10%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is organic growth?", opts: ["A firm buys a rival", "A firm merges with a supplier", "A firm opens new outlets using its own retained profit", "A firm is taken over"], a: 2, why: "Organic (internal) growth uses the firm's own resources. The others are external growth." },
  { q: "A clothing retailer buys a textile factory that supplies its cloth. This is:", opts: ["horizontal integration", "backward vertical integration", "forward vertical integration", "conglomerate integration"], a: 1, why: "The factory is earlier in the chain: it supplies the retailer." },
  { q: "A demerger is:", opts: ["Two firms joining", "A takeover paid for in shares", "A firm splitting into separate businesses", "A firm closing down"], a: 2, why: "A demerger undoes a merger, for example when the parts work better apart." },
  { q: "A takeover is best described as:", opts: ["two firms agreeing to form a new company", "one firm buying another", "a firm growing by retained profit", "a firm closing down"], a: 1, why: "One firm buys another, usually by acquiring a majority of its shares." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Organic (internal) growth", "Growth using the firm's own resources: retained profit, investment, new products or outlets."],
  ["External growth", "Growth by joining with another firm: a merger or a takeover."],
  ["Merger", "Two firms agree to join and form one new company."],
  ["Takeover (acquisition)", "One firm buys another, usually by buying its shares."],
  ["Horizontal integration", "Joining with a firm in the same industry at the same stage of production."],
  ["Backward vertical integration", "Buying a firm earlier in the supply chain, such as a supplier."],
  ["Forward vertical integration", "Buying a firm later in the supply chain, such as a distributor or retailer."],
  ["Conglomerate integration", "Joining with a firm in an unrelated industry. Also called diversification."],
  ["Diversification", "Spreading into different products or markets to reduce risk."],
  ["Demerger", "A firm splits into separate businesses."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2021 · 31 · Q7] Why might a firm adopt a policy of diversification?", opts: ["to achieve cost economies of scale", "to agree common prices with rivals", "to ensure greater ability to spread investment risks", "to increase productivity of labour"], a: 2, why: "Diversification means operating in several markets, so a fall in one is less damaging. B is collusion." },
  { q: "[May/June 2024 · 32 · Q10] What is an example of backward vertical integration?", opts: ["a bakery buying a wheat farm", "a car manufacturer buying a car showroom", "a vineyard buying an apple orchard", "two rival supermarkets joining together"], a: 0, why: "The wheat farm supplies the bakery (earlier in the chain). B is forward, C is unrelated, D is horizontal." },
  { q: "[Oct/Nov 2021 · 31 · Q6] Firm X, which currently specialises in producing cars, takes over firm Y, which owns a number of car retail outlets. How may this be described?", opts: ["horizontal integration", "the formation of a cartel", "vertical integration backwards", "vertical integration forwards"], a: 3, why: "The retailer is later in the chain, selling X's cars: forward integration." },
  { q: "[May/June 2020 · 31 · Q9] An electronics firm began as a semiconductor firm making memory chips. It used continuous research and investment to become an industry leader and applied its research to enter televisions and mobile phones. What has taken place?", opts: ["external growth and diversification", "external growth and sales revenue maximisation", "internal growth and diversification", "internal growth and sales revenue maximisation"], a: 2, why: "No firm was bought, so growth is internal (organic). Entering other markets is diversification." },
  { q: "[Feb/March 2024 · 32 · Q9] Company R manufactures steel, S produces ships, T operates oil tankers, V operates cruise liners. Which statement is correct?", opts: ["If R takes over S, this is an example of forwards vertical integration.", "If S takes over V, this is an example of backwards vertical integration.", "If T takes over S, this is an example of diversification.", "If V takes over S, this is an example of horizontal integration."], a: 0, why: "S buys R's steel, so S is later in the chain: forward. S taking over V is forward (V buys ships); T taking over S is backward; V taking over S is backward too." },
  { q: "[Oct/Nov 2024 · 31 · Q10] Firms X and Y merge in a horizontal integration. What must be true about the industry and the stage of production in which X and Y operate? (industry / stage)", opts: ["different / different", "different / same", "same / different", "same / same"], a: 3, why: "Horizontal integration joins firms in the same industry at the same stage of production." },
  { q: "[May/June 2024 · 31 · Q9] A major UK chemical firm was bought by its rival, a Dutch chemical firm. What definitely occurred when the Dutch firm bought the UK firm?", opts: ["a partnership", "economies of scale", "horizontal integration", "increased profits"], a: 2, why: "Both firms are in the same industry at the same stage, so it is horizontal integration. Economies of scale and higher profits are possible but not certain." },
] });
