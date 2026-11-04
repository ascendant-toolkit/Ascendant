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
(function () { const SC = [[{"k": "code", "x": 20, "y": 20, "lines": ["MyPet = Pet(\"Rex\", 2021)", "def __init__(self, NewName, NewYear):", "self.__PetName = NewName", "self.__YearBorn = NewYear"], "hl": 0, "w": 340, "lh": 34}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet = Pet(\"Rex\", 2021)", "def __init__(self, NewName, NewYear):", "self.__PetName = NewName", "self.__YearBorn = NewYear"], "hl": 1, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "self (new, empty object)", "rows": ["__PetName: ?", "__YearBorn: ?"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet = Pet(\"Rex\", 2021)", "def __init__(self, NewName, NewYear):", "self.__PetName = NewName", "self.__YearBorn = NewYear"], "hl": 1, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "self (new, empty object)", "rows": ["__PetName: ?", "__YearBorn: ?"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 20, "y": 175, "s": "NewName = \"Rex\"   NewYear = 2021", "c": "sm", "m": 1}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet = Pet(\"Rex\", 2021)", "def __init__(self, NewName, NewYear):", "self.__PetName = NewName", "self.__YearBorn = NewYear"], "hl": 2, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "self (new, empty object)", "rows": ["__PetName: \"Rex\"", "__YearBorn: ?"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet = Pet(\"Rex\", 2021)", "def __init__(self, NewName, NewYear):", "self.__PetName = NewName", "self.__YearBorn = NewYear"], "hl": 3, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "self (new, empty object)", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet = Pet(\"Rex\", 2021)", "def __init__(self, NewName, NewYear):", "self.__PetName = NewName", "self.__YearBorn = NewYear"], "hl": 0, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "object stored in MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f3", "lh": 24}, {"k": "txt", "x": 420, "y": 165, "s": "MyPet refers to this object", "c": "lbl bd t3", "m": 0}]], CAPS = ["The statement <code>Pet(\"Rex\", 2021)</code> calls the class. Python makes a new, empty object.", "It runs <code>__init__</code> on the new object. Inside the constructor the object is called <b>self</b>.", "The arguments become the parameters: <code>NewName = \"Rex\"</code>, <code>NewYear = 2021</code>.", "<code>self.__PetName = NewName</code> creates the first attribute on the object.", "<code>self.__YearBorn = NewYear</code> creates the second. The constructor has finished and the parameters are forgotten.", "The finished object is stored in <code>MyPet</code>. Calling the class again would make a separate object with its own values."];
  Lib.stepper($("#stA"), { w: 760, h: 215, label: "Creating a Pet object", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "code", "x": 20, "y": 20, "lines": ["Vehicle(\"V1\", 120)", "self.__VehicleID = NewID", "self.__MaxSpeed = NewMax", "self.__CurrentSpeed = 0", "self.__HorizontalPosition = 0"], "hl": 0, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 310, "title": "self", "rows": ["__VehicleID: ?", "__MaxSpeed: ?", "__CurrentSpeed: ?", "__HorizontalPosition: ?"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["Vehicle(\"V1\", 120)", "self.__VehicleID = NewID", "self.__MaxSpeed = NewMax", "self.__CurrentSpeed = 0", "self.__HorizontalPosition = 0"], "hl": 1, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 310, "title": "self", "rows": ["__VehicleID: \"V1\"", "__MaxSpeed: ?", "__CurrentSpeed: ?", "__HorizontalPosition: ?"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["Vehicle(\"V1\", 120)", "self.__VehicleID = NewID", "self.__MaxSpeed = NewMax", "self.__CurrentSpeed = 0", "self.__HorizontalPosition = 0"], "hl": 2, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 310, "title": "self", "rows": ["__VehicleID: \"V1\"", "__MaxSpeed: 120", "__CurrentSpeed: ?", "__HorizontalPosition: ?"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["Vehicle(\"V1\", 120)", "self.__VehicleID = NewID", "self.__MaxSpeed = NewMax", "self.__CurrentSpeed = 0", "self.__HorizontalPosition = 0"], "hl": 3, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 310, "title": "self", "rows": ["__VehicleID: \"V1\"", "__MaxSpeed: 120", "__CurrentSpeed: 0", "__HorizontalPosition: ?"], "cls": "f2", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["Vehicle(\"V1\", 120)", "self.__VehicleID = NewID", "self.__MaxSpeed = NewMax", "self.__CurrentSpeed = 0", "self.__HorizontalPosition = 0"], "hl": 4, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 310, "title": "self", "rows": ["__VehicleID: \"V1\"", "__MaxSpeed: 120", "__CurrentSpeed: 0", "__HorizontalPosition: 0"], "cls": "f3", "lh": 24}]], CAPS = ["Two values are passed in: <code>\"V1\"</code> and <code>120</code>. The constructor has two parameters.", "The first parameter is copied into <code>__VehicleID</code>.", "The second is copied into <code>__MaxSpeed</code>.", "<code>CurrentSpeed</code> is not passed in. The constructor <b>sets it to 0</b>, so a new vehicle is standing still.", "The same for <code>HorizontalPosition</code>. Four attributes now exist, even though only two values were passed in."];
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "Vehicle: two parameters, four attributes", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();

(function () {
  const C = [
    { n: "Pet", p: [["NewName", "PetName", "Rex"], ["NewYear", "YearBorn", "2021"]], d: [] },
    { n: "Card", p: [["NewNumber", "Number", "7"], ["NewColour", "Colour", "Red"]], d: [] },
    { n: "Vehicle", p: [["NewID", "VehicleID", "V1"], ["NewMax", "MaxSpeed", "120"]], d: [["CurrentSpeed", "0"], ["HorizontalPosition", "0"]] }
  ];
  let cur = 0; const val = C.map((c) => c.p.map((p) => p[2]));
  const lit = (v) => (/^-?\d+$/.test(v) ? v : '"' + v + '"');
  const out = () => {
    const c = C[cur], v = val[cur];
    const L = [`Obj = ${c.n}(${v.map(lit).join(", ")})`, "", `def __init__(self, ${c.p.map((p) => p[0]).join(", ")}):`];
    c.p.forEach((p, i) => L.push(`    self.__${p[1]} = ${p[0]}    # ${p[0]} is ${lit(v[i])}`));
    c.d.forEach((d) => L.push(`    self.__${d[0]} = ${d[1]}    # fixed starting value`));
    $("#kO").innerHTML = codeHTML(L) + `<div class="verdict">${c.p.length} arguments passed in, ${c.p.length + c.d.length} attributes in the finished object.</div>`;
  };
  const paint = () => {
    const c = C[cur]; $$("#kB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#kI").innerHTML = '<div class="btnrow">' + c.p.map((p, i) => `<label>${p[0]} <input data-i="${i}" value="${esc(val[cur][i])}" size="8"></label>`).join(" ") + "</div>";
    $$("#kI input").forEach((x) => (x.oninput = () => { val[cur][+x.dataset.i] = x.value; out(); }));
    out();
  };
  $("#kB").innerHTML = C.map((c, i) => `<button class="b" data-i="${i}">${c.n}</button>`).join("");
  $$("#kB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); }));
  paint();
})();

btnTable("eB", "eO", [
  ["Missing self", "def __init__(NewName): self.__Name = NewName", "TypeError: Python passes the object in as the first argument and there is no parameter to receive it", "def __init__(self, NewName):"],
  ["Attribute without self", "def __init__(self, NewName): __Name = NewName", "A local variable is created and forgotten when the constructor ends. The object has no attribute", "self.__Name = NewName"],
  ["Wrong number of arguments", "Pet(\"Rex\")  # constructor needs two", "TypeError: the constructor is missing NewYear", "Pet(\"Rex\", 2021)"],
  ["Returning a value", "def __init__(self, n): self.__Name = n; return self", "__init__ must not return a value; the object is returned by the class call itself", "Remove the return"],
  ["Parameter used instead of attribute", "def GetName(self): return NewName", "NewName only exists while the constructor runs", "return self.__Name"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Is the value passed in as a parameter, or set to a fixed starting value?", buckets: [{"label": "Parameter (passed in)"}, {"label": "Fixed starting value"}], items: [{"text": "A vehicle's VehicleID", "b": 0}, {"text": "A vehicle's MaxSpeed", "b": 0}, {"text": "A vehicle's CurrentSpeed when it is created", "b": 1}, {"text": "A card's Number", "b": 0}, {"text": "A counter that always starts at 0", "b": 1}, {"text": "A pet's name", "b": 0}, {"text": "An empty list of Treatments for a new appointment", "b": 1}, {"text": "A patient's ID", "b": 0}], done: "If the question says the value is passed in, it is a parameter. If it says the attribute is initialised, or does not mention it as a parameter, set it inside the constructor." });
Lib.order($("#o1"), { prompt: "Put the steps of creating an object in order.", items: ["Write Pet(\"Rex\", 2021)", "A new, empty object is made", "The constructor runs on the new object", "The arguments are copied into the parameters", "The parameters are assigned to attributes", "The finished object is stored in the variable"], done: "Call, make, run, copy to parameters, assign to attributes, store." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Constructor", "Runs once when an object is created and sets its starting values"], ["__init__", "The name of the constructor in Python"], ["NEW", "The name of the constructor in exam pseudocode"], ["self", "The object being built"], ["Parameter", "A value passed to the constructor, only available while it runs"], ["Attribute", "A value stored in the object for as long as it exists"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "class Hand has a constructor __init__(self, Card1, Card2, Card3, Card4, Card5). How many arguments are in the call that creates a Hand?", "a": 5, "unit": "", "tol": 0.01, "hint": "One for each parameter after self.", "sol": "<b>5</b>."},
  {"q": "A Vehicle constructor takes NewID and NewMax and sets CurrentSpeed and HorizontalPosition to 0. How many attributes does the object have?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count every attribute, not just the parameters.", "sol": "<b>4</b>: two from parameters, two fixed."},
  {"q": "Same constructor: how many parameters does it have, not counting self?", "a": 2, "unit": "", "tol": 0.01, "hint": "Only the values passed in.", "sol": "<b>2</b>."},
  {"q": "A Parrot's parent constructor sets 4 attributes and the Parrot constructor sets 2 more. How many attributes does a Parrot object have?", "a": 6, "unit": "", "tol": 0.01, "hint": "Inherited plus its own.", "sol": "<b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What triggers the constructor?", opts: ["Calling GetName()", "Creating an object from the class", "Importing the class", "Printing the object"], a: 1, why: "Writing the class name with brackets runs it." },
  { q: "What is the first parameter of every Python method, including __init__?", opts: ["name", "self", "this", "object"], a: 1, why: "self refers to the object being worked on." },
  { q: "A constructor should...", opts: ["Return the object", "Return nothing and set the attributes", "Print the attributes", "Delete the old object"], a: 1, why: "It sets starting values; it does not return." },
  { q: "Which line creates a Pet attribute properly?", opts: ["PetName = NewName", "self.__PetName = NewName", "NewName = self.__PetName", "return NewName"], a: 1, why: "The attribute belongs to the object, so it needs self." },
  { q: "The question says 'the constructor takes the ID as a parameter and sets speed to 0'. How many parameters?", opts: ["0", "1", "2", "3"], a: 1, why: "Only the ID is passed in." },
  { q: "How many constructors does a class normally have?", opts: ["One", "One per attribute", "Two", "None"], a: 0, why: "One, called when an object is created." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Constructor", "Runs once when an object is created. Sets the starting values."],
  ["__init__(self, ...)", "Python's constructor."],
  ["NEW", "Pseudocode's constructor name."],
  ["Argument", "A value you pass in when you create the object."],
  ["Parameter", "The variable in the constructor that receives an argument."],
  ["Attribute", "A value stored in the object: self.__Name."],
  ["Fixed starting value", "An attribute set inside the constructor, not passed in."],
  ["Object", "One instance of a class, made by calling it."],
] });
