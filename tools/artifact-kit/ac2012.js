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

/* class box: x, y, w, title, rows (strings), v (opacity), cls fill */
function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}

(function () {
  const objs = [["Rex", "Dog", "2021"], ["Tilly", "Cat", "2023"], ["Kiwi", "Parrot", "2024"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = classBox(20, 30, 210, "class Pet", ["PetName : STRING", "PetType : STRING", "YearBorn : INTEGER", "Constructor()", "GetPetName()"], 1, "f1");
    objs.forEach((ob, n) => {
      const v = k > n ? 1 : 0, x = 280 + n * 160;
      if (v) { o += classBox(x, 60, 140, n === 1 && k === 4 ? "object p2" : "object p" + (n + 1), ["PetName: " + (n === 1 && k === 4 ? "Mittens" : ob[0]), "PetType: " + ob[1], "YearBorn: " + ob[2]], 1, "f2", 24) + SV.line(230, 100, x, 110, "dash", op(0.6)); }
    });
    if (k >= 1) o += SV.text(20, 22, "template", "sm");
    if (k >= 4) o += SV.text(440, 38, "p2 changed; p1 and p3 are not affected", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 230, label: "One class and three objects", base: { i: 0 }, draw, tween: 500, dwell: 3800, steps: [
    { cap: "The <b>class</b> Pet is a template: it lists the properties and methods every pet will have. It holds no particular pet's data.", s: { i: 0 } },
    { cap: "<code>p1 ← NEW Pet(\"Rex\", \"Dog\", 2021)</code> runs the <b>constructor</b> and creates an <b>object</b>, an <b>instance</b> of Pet, with its own values.", s: { i: 1 } },
    { cap: "A second instance with different values. Each object has its own copy of the properties.", s: { i: 2 } },
    { cap: "A third. Creating objects from a class is called <b>instantiation</b>.", s: { i: 3 } },
    { cap: "Changing p2's name changes only p2. The objects share the class's methods but not their data.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.rect(30, 50, 170, 140, "cell", { rx: 8 }) + SV.text(115, 40, "rest of the program", "sm", { "text-anchor": "middle" }) + SV.text(115, 110, "main program", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(390, 30, 340, 195, "f2", { rx: 10, ...op(0.18) }) + SV.rect(390, 30, 340, 195, "ax", { rx: 10, fill: "none" }) + SV.text(560, 22, "object of class Pet", "sm", { "text-anchor": "middle" });
    o += memCell(440, 60, "Age", k >= 3 ? 12 : 4, k >= 1 ? "cell-ok" : "f3", 1, 160) + SV.text(440, 52, "PRIVATE Age : INTEGER", "sm");
    o += SV.rect(360, 60, 18, 40, "cell-no", { rx: 3, ...op(k >= 1 ? 1 : 0) });
    o += SV.rect(440, 112, 170, 34, "f1", { rx: 6, ...op(0.55) }) + SV.text(525, 134, "GetAge()", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
    o += SV.rect(440, 156, 170, 34, "f1", { rx: 6, ...op(0.55) }) + SV.text(525, 178, "SetAge(n)", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
    if (k === 2) o += arrow(200, 90, 355, 80, "r", "c3", 1) + SV.text(210, 80, "pet.Age ✗", "lbl bd c3") + SV.text(210, 130, "blocked: the property is private", "sm");
    if (k === 3) o += arrow(200, 120, 440, 128, "r", "c1", 1) + SV.text(210, 112, "pet.GetAge()", "lbl bd") + arrow(525, 100, 525, 110, "d", "c2", 1);
    if (k === 4) o += arrow(200, 120, 440, 172, "r", "c1", 1) + SV.text(210, 112, "pet.SetAge(12)", "lbl bd") + SV.text(560, 212, "SetAge checks 0 to 30, then stores 12", "sm", { "text-anchor": "middle" });
    if (k === 5) o += arrow(200, 120, 440, 172, "r", "c1", 1) + SV.text(210, 112, "pet.SetAge(-3)", "lbl bd") + SV.text(560, 212, "rejected: -3 is not valid, Age stays 12", "sm", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 240, label: "Encapsulation with a getter and a setter", base: { i: 0 }, draw, tween: 500, dwell: 3800, steps: [
    { cap: "A Pet object stores an <b>Age</b>. The programmer declares it <code>PRIVATE</code> and writes two public methods.", s: { i: 0 } },
    { cap: "Because Age is private, a wall surrounds it. Only methods of the class can reach it.", s: { i: 1 } },
    { cap: "Code outside the class that tries to read or write <code>Age</code> directly is <b>blocked</b>.", s: { i: 2 } },
    { cap: "The <b>getter</b> <code>GetAge()</code> is the allowed way to read the value.", s: { i: 3 } },
    { cap: "The <b>setter</b> <code>SetAge(n)</code> is the allowed way to change it. The method can check the value first.", s: { i: 4 } },
    { cap: "A silly value is rejected, so the data stays valid. That is the point of <b>encapsulation</b>.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(230, 10, 300, "Yarn (parent)", ["Name, Colour, BatchCode : STRING", "Weight, NumberBalls : INTEGER", "Type : STRING", "Constructor()  EditNumberBalls()", "YarnInfo()"], 1, "f1", 19);
    const kids = [["Acrylic", "Soft : BOOLEAN", "Constructor()", "YarnInfo()"], ["Wool", "WoolType : STRING", "Constructor()", "YarnInfo()"], ["Mix", "Percentage : INTEGER", "Constructor()", "YarnInfo()  (overrides)"]];
    kids.forEach((c, n) => {
      const v = k > n ? 1 : 0, x = 20 + n * 245; if (!v) return;
      o += classBox(x, 160, 225, c[0] + " (child)", [c[1], c[2], c[3]], 1, ["f2", "f3", "f4"][n], 19) + arrow(x + 112, 160, 380, 142, "u", "c1", 1);
    });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 270, label: "Inheritance with three child classes", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "The <b>parent class</b> Yarn holds everything the three types share: name, colour, batch code, weight, number of balls, type, and the methods.", s: { i: 0 } },
    { cap: "<b>Acrylic</b> inherits all of it and adds only what is new: <code>Soft : BOOLEAN</code>. The arrow points from the child to the parent.", s: { i: 1 } },
    { cap: "<b>Wool</b> inherits the same and adds its own <code>WoolType</code> (lamb, merino or alpaca).", s: { i: 2 } },
    { cap: "<b>Mix</b> adds <code>Percentage</code> of acrylic. Each child has its own constructor and its own <code>YarnInfo()</code> because each shows extra data. Nothing in Yarn is written three times.", s: { i: 3 } }] });
})();

(function () {
  const animals = [["Dog", "Woof"], ["Cat", "Meow"], ["Cow", "Moo"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += codeList(20, 30, ["FOR EACH a IN Animals", "   OUTPUT a.Speak()", "NEXT a"], k === 0 ? -1 : 1, 1, 34, 230);
    animals.forEach((a, n) => {
      const x = 310 + n * 140, on = k === n + 1;
      o += classBox(x, 40, 120, a[0], ["Speak()"], 1, on ? "f3" : "f1", 20);
      if (k > n) o += SV.text(x + 60, 140, '"' + a[1] + '"', "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + arrow(x + 60, 100, x + 60, 124, "d", "c2", 1);
    });
    if (k === 4) o += SV.text(310, 190, "one call, three different results", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 215, label: "Polymorphism: the same method call", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "Dog, Cat and Cow each <b>redefine</b> the method <code>Speak()</code>. The loop calls the same method name on every object.", s: { i: 0 } },
    { cap: "On the Dog object, <code>Speak()</code> runs the Dog version.", s: { i: 1 } },
    { cap: "On the Cat object, the same call runs the Cat version.", s: { i: 2 } },
    { cap: "On the Cow object, the Cow version.", s: { i: 3 } },
    { cap: "That is <b>polymorphism</b>: the same method name, redefined in derived classes, behaves differently depending on the object.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(30, 20, 200, "Card", ["Number : INTEGER", "Colour : STRING", "GetNumber()", "GetColour()"], 1, "f2");
    if (k >= 1) {
      o += SV.rect(300, 20, 430, 150, "cell", { rx: 8 }) + SV.rect(300, 20, 430, 28, "f1", { rx: 8, ...op(0.6) }) + SV.text(515, 39, "object of class Hand", "lbl bd", { "text-anchor": "middle", style: "font-size:15px" });
      for (let c = 0; c < 5; c++) o += SV.rect(315 + c * 82, 64, 70, 70, "f2", { rx: 6, ...op(0.45) }) + SV.text(350 + c * 82, 92, "Card", "sm", { "text-anchor": "middle" }) + SV.text(350 + c * 82, 112, (c + 1) + " red", "sm", { "text-anchor": "middle", style: "font-size:11px" });
      o += SV.text(315, 156, "Cards : ARRAY[0:9] OF Card", "sm", { style: "font-family:var(--mono);font-size:11.5px" });
    }
    if (k >= 2) o += SV.text(30, 200, "Hand HAS Cards: containment (aggregation)", "lbl bd t3") + SV.text(30, 226, "Parrot IS AN Animal: inheritance", "lbl bd t1", op(k >= 3 ? 1 : 0.3));
    return o;
  };
  Lib.stepper($("#stE"), { w: 760, h: 240, label: "Containment: a hand of cards", base: { i: 0 }, draw, tween: 500, dwell: 3800, steps: [
    { cap: "A <b>Card</b> class stores a number and a colour.", s: { i: 0 } },
    { cap: "A <b>Hand</b> object holds an array of <b>Card</b> objects. The Hand class has a property whose type is another class.", s: { i: 1 } },
    { cap: "This is <b>containment (aggregation)</b>: a Hand <i>has</i> cards.", s: { i: 2 } },
    { cap: "Compare inheritance: a Parrot <i>is an</i> Animal. Ask 'has a' or 'is a' to choose between them.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let priv = true, age = 4;
  const paint = (msg) => {
    $$("#vB button").forEach((b, i) => b.classList.toggle("pri", (i === 0) === priv));
    $("#v1").textContent = age; $("#vv").textContent = msg || (priv ? "Age is PRIVATE: only GetAge() and SetAge() can reach it." : "Age is PUBLIC: any code can reach it directly.");
  };
  $("#vB").innerHTML = '<button class="b">PRIVATE Age</button><button class="b">PUBLIC Age</button>';
  $$("#vB button").forEach((b, i) => (b.onclick = () => { priv = i === 0; paint(); }));
  $("#vR").onclick = () => paint(priv ? "Blocked: Age is private, so outside code cannot read it directly." : "Read directly: " + age + ". It works, but nothing protects the data.");
  $("#vG").onclick = () => paint("GetAge() returns " + age + ". This is the allowed way to read a private property.");
  $("#vN").onclick = () => { if (priv) return paint("Blocked: outside code cannot set a private property directly."); age = 25; paint("Age is now 25. Directly set, so no check was made."); };
  $("#vS").onclick = () => { age = 25; paint("SetAge(25): checked (0 to 30 is allowed) and stored. Age is 25."); };
  $("#vC").onclick = () => paint(priv ? "SetAge(-3): the setter rejects it, so Age stays " + age + ". The setter protects the data." : "SetAge(-3): the setter rejects it. But with a PUBLIC Age, outside code could still set -3 directly, which is why properties are made private.");
  paint();
})();

/* Lab 2 */
(function () {
  const parent = ["Name, Colour, BatchCode : STRING", "Weight, NumberBalls, Type", "EditNumberBalls()"];
  const rows = [
    ["Yarn (parent)", "Everything: Name, Colour, BatchCode, Weight, NumberBalls, Type and the methods Constructor(), EditNumberBalls(), YarnInfo()", "Nothing: this is the parent class", "Nothing to override"],
    ["Acrylic", "All of Yarn: " + parent.join("; "), "Soft : BOOLEAN; its own Constructor()", "YarnInfo(), to show the Soft value as well"],
    ["Wool", "All of Yarn: " + parent.join("; "), "WoolType : STRING; its own Constructor()", "YarnInfo(), to show the wool type"],
    ["Mix", "All of Yarn: " + parent.join("; "), "Percentage : INTEGER; its own Constructor()", "YarnInfo(), to show the percentage of acrylic"]
  ];
  btnTable("iB", "iO", rows, ["Class", "Inherited", "Adds", "Overrides"]);
})();

btnTable("eB", "eO", [
  ["Class", "A template that defines the properties and methods of its objects", "Pet", "Calling it 'an object'"],
  ["Object / instance", "One occurrence of a class, with its own values", "p1 ← NEW Pet(...)", "Saying an instance is a class"],
  ["Constructor", "The method that runs when an object is created and sets its starting values", "PUBLIC PROCEDURE NEW(...)", "Forgetting it takes parameters for the values"],
  ["Encapsulation", "Properties and methods together in one class; data private and reached only through the class's own methods", "PRIVATE Age : INTEGER", "'Hiding' without saying how it is accessed"],
  ["Getter / setter", "A getter returns the value of a property; a setter updates it", "GetAge() / SetAge(n)", "Giving a getter a parameter"],
  ["Inheritance", "A derived class takes the properties and methods of a parent class", "CLASS Parrot INHERITS Animal", "Arrows the wrong way round"],
  ["Polymorphism", "A method with the same name is redefined in derived classes, so behaviour differs by class", "Speak() in Dog and Cat", "Writing 'many forms' only"],
  ["Containment (aggregation)", "A class contains objects of another class: 'has a'", "Hand contains Cards", "Confusing it with inheritance"]
], ["Term", "Meaning", "Example", "Trap"]);
Lib.classify($("#cl1"), { prompt: "What kind of class member is each item?", buckets: [{"label": "Attribute"}, {"label": "Constructor"}, {"label": "Getter"}, {"label": "Setter"}, {"label": "Method (other)"}], items: [{"text": "PetName : STRING", "b": 0}, {"text": "NEW(NewName : STRING)", "b": 1}, {"text": "GetPetName()", "b": 2}, {"text": "SetPetName(NewName : STRING)", "b": 3}, {"text": "EditNumberBalls()", "b": 4}, {"text": "YearBorn : INTEGER", "b": 0}, {"text": "__init__(self, name)", "b": 1}, {"text": "GetYearBorn()", "b": 2}, {"text": "SetPriority(Urgency : INTEGER)", "b": 3}, {"text": "Description()", "b": 4}], done: "Attributes have a data type and no brackets. Getters start Get and take nothing. Setters start Set and take the new value. The constructor creates the object." });
Lib.classify($("#cl2"), { prompt: "Is the relationship inheritance (is a) or containment (has a)?", buckets: [{"label": "Inheritance"}, {"label": "Containment"}], items: [{"text": "A Parrot and an Animal", "b": 0}, {"text": "A Hand and its Cards", "b": 1}, {"text": "A Manager and an Employee", "b": 0}, {"text": "A Library and its Books", "b": 1}, {"text": "A Car and its Engine", "b": 1}, {"text": "A Helicopter and a Vehicle", "b": 0}, {"text": "A Garage and its Cars", "b": 1}, {"text": "A Circle and a Shape", "b": 0}], done: "Try 'is a': a Parrot is an Animal. Try 'has a': a Hand has Cards." });
Lib.order($("#o1"), { prompt: "Put the steps for designing classes in order.", items: ["Find the things the problem describes: each kind is a class", "List the data each class stores, with data types", "List the actions each class performs: its methods", "Look for shared parts and put them in a parent class", "Make the properties private and add getters and setters where needed"], done: "Things, data, actions, sharing, access." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Constructor", "Sets up a new object when it is created"], ["Getter", "Returns the value of a property"], ["Setter", "Updates the value of a property"], ["Polymorphism", "The same method redefined in derived classes"], ["Instance", "An occurrence of an object made from a class"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A class has 6 properties, all private, all of which must be readable from outside. How many getters are needed?", "a": 6, "unit": "", "tol": 0.01, "hint": "One getter per readable property.", "sol": "<b>6</b>."},
  {"q": "A class has 6 properties. The ID never changes; the other 5 can be updated. How many setters?", "a": 5, "unit": "", "tol": 0.01, "hint": "No setter for the ID.", "sol": "<b>5</b>."},
  {"q": "Yarn has 6 properties and 3 methods. Mix inherits from Yarn and adds 1 property. How many properties does a Mix object have?", "a": 7, "unit": "", "tol": 0.01, "hint": "Inherited plus new.", "sol": "<b>7</b>."},
  {"q": "A Hand contains 5 Card objects. Each Card has 2 properties. How many Card properties exist across the hand?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 2.", "sol": "<b>10</b>."},
  {"q": "Classes: Animal, Dog, Cat, Cow, with Dog, Cat and Cow inheriting from Animal. How many inheritance arrows are drawn?", "a": 3, "unit": "", "tol": 0.01, "hint": "One from each child.", "sol": "<b>3</b>."},
  {"q": "Three objects are created from the class Pet. How many classes are there?", "a": 1, "unit": "", "tol": 0.01, "hint": "Many objects, one class.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is encapsulation?", opts: ["Writing code in a class", "Keeping data private so it can only be accessed through the class's own methods", "Creating an object", "Copying a class"], a: 1, why: "Data and methods together, with the data reached only through methods." },
  { q: "What is a setter?", opts: ["A method that returns a property", "A method that updates the value of a property", "A method that creates an object", "A private property"], a: 1, why: "A setter updates; a getter returns." },
  { q: "In a class diagram, which is a getter?", opts: ["SetPriority(Urgency : INTEGER)", "GetPriority()", "Priority : INTEGER", "Constructor()"], a: 1, why: "Getters take no parameter and start with Get." },
  { q: "What does polymorphism mean?", opts: ["A class has many objects", "A method is redefined in derived classes, behaving differently", "A class has many properties", "A property has many types"], a: 1, why: "Same method name, different behaviour." },
  { q: "Which relationship is containment?", opts: ["A Parrot is an Animal", "A Hand has Cards", "A Manager is an Employee", "A Circle is a Shape"], a: 1, why: "Has a." },
  { q: "What is an instance?", opts: ["A template", "A type of method", "An occurrence of an object created from a class", "A private property"], a: 2, why: "Instances are created from classes." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Class", "A template for objects: their properties and methods."],
  ["Object / instance", "One occurrence of a class, with its own values."],
  ["Constructor", "Sets up a new object. NEW in pseudocode, __init__ in Python."],
  ["Encapsulation", "Data private; accessed only by the class's own methods."],
  ["Getter", "Method that returns the value of a property."],
  ["Setter", "Method that updates the value of a property."],
  ["Inheritance", "A derived class takes properties and methods of a parent class."],
  ["Polymorphism", "Same method name redefined in derived classes."],
  ["Containment", "One class holds objects of another: has a."],
] });
