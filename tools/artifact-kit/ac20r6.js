const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}
function sceneItem(o) {
  if (o.k === "code") return codeList(o.x, o.y, o.lines, o.hl, 1, o.lh, o.w);
  if (o.k === "cls") return classBox(o.x, o.y, o.w, o.title, o.rows, 1, o.cls, o.lh);
  if (o.k === "txt") return SV.text(o.x, o.y, o.s, o.c, o.m ? { style: "font-family:var(--mono);font-size:14px" } : {});
  if (o.k === "arr") return arrow(o.a[0], o.a[1], o.a[2], o.a[3], o.d, "c1", 1);
  return "";
}
const codeHTML = (L) => '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
(function () { const SC = [[{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}], [{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 20, "y": 130, "s": "MyHand = Hand(C1, C2, C3, C4, C5)", "c": "sm", "m": 1}], [{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 20, "y": 140, "w": 700, "title": "MyHand", "rows": ["__Cards: [Card 1, Card 2, Card 3, Card 4, Card 5]"], "cls": "f3", "lh": 22}], [{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 20, "y": 140, "w": 700, "title": "MyHand has Cards", "rows": ["__Cards: [Card 1, Card 2, Card 3, Card 4, Card 5]"], "cls": "f3", "lh": 22}, {"k": "txt", "x": 20, "y": 235, "s": "has-a relationship", "c": "lbl bd t3", "m": 0}]], CAPS = ["Five Card objects are created first, one statement each.", "<code>Hand(C1, C2, C3, C4, C5)</code> passes the five Card objects to the Hand constructor.", "The constructor stores them in a list: <code>self.__Cards = [Card1, ..., Card5]</code>.", "The Hand now <b>has</b> five Cards. The cards are objects in their own right, with their own methods."];
  Lib.stepper($("#stA"), { w: 760, h: 250, label: "Five Cards, then a Hand", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 20, "y": 130, "s": "MyHand.GetCard(2).GetNumber()", "c": "lbl bd", "m": 1}], [{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f3", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 20, "y": 130, "s": "MyHand.GetCard(2)  ->  Card 3", "c": "sm", "m": 1}], [{"k": "cls", "x": 20, "y": 20, "w": 130, "title": "Card 1", "rows": ["4 Red"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 164, "y": 20, "w": 130, "title": "Card 2", "rows": ["9 Blue"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 308, "y": 20, "w": 130, "title": "Card 3", "rows": ["2 Red"], "cls": "f3", "lh": 22}, {"k": "cls", "x": 452, "y": 20, "w": 130, "title": "Card 4", "rows": ["7 Green"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 596, "y": 20, "w": 130, "title": "Card 5", "rows": ["1 Blue"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 20, "y": 130, "s": "Card 3 .GetNumber()  ->  2", "c": "lbl bd t3", "m": 1}, {"k": "txt", "x": 20, "y": 165, "s": "the Hand never needs to know how a Card stores its number", "c": "sm", "m": 0}]], CAPS = ["The whole call is <code>MyHand.GetCard(2).GetNumber()</code>. It is evaluated from left to right.", "<code>MyHand.GetCard(2)</code> asks the Hand for the card at position 2. It returns a Card object.", "<code>.GetNumber()</code> is now called on that Card, not on the Hand. The Card returns its number."];
  Lib.stepper($("#stB"), { w: 760, h: 250, label: "MyHand.GetCard(2).GetNumber()", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();

(function () {
  const cards = [[4, "Red"], [9, "Blue"], [2, "Red"], [7, "Green"], [1, "Blue"]]; let m = "N";
  const paint = () => {
    const p = +$("#hR").value; $("#hV").textContent = p;
    $("#hO").innerHTML = '<div class="btnrow">' + cards.map((c, i) => `<span class="b ${i === p ? "pri" : ""}" style="pointer-events:none">${i}: ${c[0]} ${c[1]}</span>`).join("") + "</div>";
    $("#hN").classList.toggle("pri", m === "N"); $("#hC").classList.toggle("pri", m === "C");
    const call = "MyHand.GetCard(" + p + ")." + (m === "N" ? "GetNumber()" : "GetColour()");
    $("#hC2").innerHTML = codeHTML(["print(" + call + ")"]);
    $("#hL").textContent = "GetCard(" + p + ") returns the card " + cards[p][0] + " " + cards[p][1] + ", then " + (m === "N" ? "GetNumber() returns " + cards[p][0] : "GetColour() returns " + cards[p][1]) + ".";
  };
  $("#hR").oninput = paint; $("#hN").onclick = () => { m = "N"; paint(); }; $("#hC").onclick = () => { m = "C"; paint(); }; paint();
})();

btnTable("aB", "aO", [
  ["Hand and Card", "A Hand has Cards", "A Hand is not a Card", "Containment: the Hand's attribute is an array of Card objects"],
  ["Parrot and Animal", "A Parrot is an Animal", "An Animal does not have a Parrot", "Inheritance: class Parrot(Animal)"],
  ["Car and Engine", "A Car has an Engine", "A Car is not an Engine", "Containment: Car holds an Engine object"],
  ["Dog and Animal", "A Dog is an Animal", "An Animal does not have a Dog", "Inheritance: class Dog(Animal)"],
  ["Library and Book", "A Library has Books", "A Library is not a Book", "Containment: a list of Book objects"],
  ["Manager and Employee", "A Manager is an Employee", "An Employee does not have a Manager", "Inheritance: class Manager(Employee)"]
], ["Pair", "Say it", "Check the other way", "Answer"]);

btnTable("eB", "eO", [
  ["Hand created first", "MyHand = Hand(C1, C2, C3, C4, C5)  # before the Cards exist", "NameError: C1 does not exist yet", "Create the five Cards, then the Hand"],
  ["Forgetting the position", "def GetCard(self): return self.__Cards", "Returns the whole list, not one card", "def GetCard(self, Position): return self.__Cards[Position]"],
  ["Chain in the wrong order", "MyHand.GetNumber().GetCard(2)", "The Hand has no GetNumber(); that method belongs to Card", "MyHand.GetCard(2).GetNumber()"],
  ["Using inheritance instead", "class Hand(Card): ...", "A Hand is not a Card; it has Cards", "Store Card objects in an attribute"],
  ["Reaching into the Card", "MyHand.GetCard(2).__Number", "Number is private to Card", "MyHand.GetCard(2).GetNumber()"],
  ["Counting from 1", "MyHand.GetCard(5)", "IndexError: positions 0 to 4 only", "MyHand.GetCard(4) for the last card"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Containment or inheritance?", buckets: [{"label": "Containment (has a)"}, {"label": "Inheritance (is a)"}], items: [{"text": "A Hand and its five Cards", "b": 0}, {"text": "A Parrot and an Animal", "b": 1}, {"text": "A Library and its Books", "b": 0}, {"text": "A Manager and an Employee", "b": 1}, {"text": "A Car and its Engine", "b": 0}, {"text": "A Dog and an Animal", "b": 1}, {"text": "A Playlist and its Songs", "b": 0}, {"text": "A Circle and a Shape", "b": 1}], done: "Say the sentence. A Hand has Cards (containment). A Parrot is an Animal (inheritance)." });
Lib.order($("#o1"), { prompt: "Put the steps in order: building a Hand.", items: ["Create the first Card", "Create the other four Cards", "Pass the five Cards to the Hand constructor", "The constructor stores them in a list attribute", "The Hand now has five Cards"], done: "Create the contained objects first, then the container." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Containment", "A class has an attribute that is an object of another class"], ["Aggregation", "Another name for containment"], ["has a", "The relationship in containment"], ["MyHand.GetCard(2).GetNumber()", "A chained call: the Hand returns a Card, then the Card is asked for its number"], ["Container", "The class that holds the other objects"], ["Contained object", "An object stored as an attribute of another object"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A Hand holds Cards numbered [4, 9, 2, 7, 1]. What does MyHand.GetCard(1).GetNumber() return?", "a": 9, "unit": "", "tol": 0.01, "hint": "Position 1 is the second card.", "sol": "<b>9</b>."},
  {"q": "Same Hand: what does MyHand.GetCard(4).GetNumber() return?", "a": 1, "unit": "", "tol": 0.01, "hint": "Position 4 is the last.", "sol": "<b>1</b>."},
  {"q": "How many Card objects must exist before the Hand constructor is called with five parameters?", "a": 5, "unit": "", "tol": 0.01, "hint": "One argument per parameter.", "sol": "<b>5</b>."},
  {"q": "A Library holds 12 Book objects. How many objects exist in total including the Library?", "a": 13, "unit": "", "tol": 0.01, "hint": "The 12 books plus the Library.", "sol": "<b>13</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is containment?", opts: ["A child class takes its parent's methods", "A class has an attribute that is an object of another class", "Data is hidden", "A method has many forms"], a: 1, why: "Has a." },
  { q: "Which is a containment relationship?", opts: ["Parrot and Animal", "Hand and Card", "Dog and Animal", "Manager and Employee"], a: 1, why: "A Hand has Cards." },
  { q: "Which must happen first?", opts: ["The Hand is created, then the Cards", "The Cards are created, then the Hand", "Either order", "The Hand is deleted"], a: 1, why: "The Cards are passed in to the Hand's constructor." },
  { q: "What does MyHand.GetCard(2).GetNumber() do?", opts: ["Asks the Hand for its number", "Gets the third Card, then asks that Card for its number", "Gets the second Card", "Creates a new Card"], a: 1, why: "Left to right." },
  { q: "Another name for containment is...", opts: ["Overriding", "Aggregation", "Polymorphism", "Instantiation"], a: 1, why: "The syllabus uses both names." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Containment", "A class has an attribute that is an object (or array of objects) of another class."],
  ["Aggregation", "Another name for containment."],
  ["has a", "The relationship: a Hand has Cards."],
  ["is a", "Inheritance, not containment."],
  ["Create contained first", "Cards first, then the Hand that holds them."],
  ["Chained call", "MyHand.GetCard(2).GetNumber()"],
  ["Container", "The class holding the objects, such as Hand."],
  ["Contained", "The objects held, such as Card."],
] });
