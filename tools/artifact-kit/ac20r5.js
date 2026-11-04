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
(function () { const SC = [[{"k": "cls", "x": 30, "y": 40, "w": 215, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 265, "y": 40, "w": 215, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 500, "y": 40, "w": 215, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "for Item in Zoo:  print(Item.Description())", "c": "sm", "m": 1}], [{"k": "cls", "x": 30, "y": 40, "w": 215, "title": "Animal", "rows": ["Description()"], "cls": "f3", "lh": 22}, {"k": "cls", "x": 265, "y": 40, "w": 215, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 500, "y": 40, "w": 215, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "Item.Description()  ->  Generic is an animal", "c": "lbl bd t3", "m": 0}], [{"k": "cls", "x": 30, "y": 40, "w": 215, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 265, "y": 40, "w": 215, "title": "Parrot", "rows": ["Description()"], "cls": "f3", "lh": 22}, {"k": "cls", "x": 500, "y": 40, "w": 215, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "Item.Description()  ->  Polly is a parrot that squawks", "c": "lbl bd t3", "m": 0}], [{"k": "cls", "x": 30, "y": 40, "w": 215, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 265, "y": 40, "w": 215, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 500, "y": 40, "w": 215, "title": "Dog", "rows": ["Description()"], "cls": "f3", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "Item.Description()  ->  Rex is a dog that barks", "c": "lbl bd t3", "m": 0}], [{"k": "cls", "x": 30, "y": 40, "w": 215, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 265, "y": 40, "w": 215, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 500, "y": 40, "w": 215, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "same call, different behaviour", "c": "lbl bd t3", "m": 0}]], CAPS = ["A list holds three objects of different classes. The loop calls <code>Item.Description()</code> on each.", "First object is an Animal: its <code>Description()</code> runs.", "Second is a Parrot. The same call, but Parrot's version runs.", "Third is a Dog. Same call again, Dog's version.", "One line of code, three different results: that is polymorphism."];
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "A loop over a list of objects", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "cls", "x": 30, "y": 40, "w": 213, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 263, "y": 40, "w": 213, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 496, "y": 40, "w": 213, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "for Item in Zoo:  print(Item.Description())", "c": "sm", "m": 1}], [{"k": "cls", "x": 30, "y": 40, "w": 155, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 205, "y": 40, "w": 155, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 380, "y": 40, "w": 155, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 555, "y": 40, "w": 155, "title": "Cat", "rows": ["Description()"], "cls": "f3", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "for Item in Zoo:  print(Item.Description())", "c": "sm", "m": 1}], [{"k": "cls", "x": 30, "y": 40, "w": 155, "title": "Animal", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 205, "y": 40, "w": 155, "title": "Parrot", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 380, "y": 40, "w": 155, "title": "Dog", "rows": ["Description()"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 555, "y": 40, "w": 155, "title": "Cat", "rows": ["Description()"], "cls": "f3", "lh": 22}, {"k": "txt", "x": 30, "y": 150, "s": "Item.Description()  ->  Tilly is a cat that purrs", "c": "lbl bd t3", "m": 0}, {"k": "txt", "x": 30, "y": 185, "s": "loop code unchanged", "c": "sm", "m": 0}]], CAPS = ["The loop works for Animal, Parrot and Dog.", "A new class <code>Cat(Animal)</code> is written with its own <code>Description()</code>.", "A Cat is added to the list. The loop code is exactly the same."];
  Lib.stepper($("#stB"), { w: 760, h: 225, label: "A new class, the loop unchanged", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();

(function () {
  const say = { Animal: " is an animal", Parrot: " is a parrot that squawks", Dog: " is a dog that barks", Cat: " is a cat that purrs" };
  const names = { Animal: "Generic", Parrot: "Polly", Dog: "Rex", Cat: "Tilly" }; let zoo = [];
  const paint = () => { $("#zL").innerHTML = codeHTML(["Zoo = [" + zoo.map((k) => k + '("' + names[k] + '")').join(", ") + "]", "for Item in Zoo:", "    print(Item.Description())"]); };
  [["zA", "Animal"], ["zP", "Parrot"], ["zD", "Dog"], ["zC", "Cat"]].forEach(([id, k]) => ($("#" + id).onclick = () => { zoo.push(k); paint(); }));
  $("#zR").onclick = () => { zoo = []; $("#zO").innerHTML = ""; paint(); };
  $("#zGo").onclick = () => { $("#zO").innerHTML = '<div class="verdict">' + (zoo.length ? zoo.map((k) => esc(names[k] + say[k])).join("<br>") : "The list is empty, so nothing is printed.") + "</div>"; };
  paint();
})();

btnTable("eB", "eO", [
  ["Different method names", "Parrot.ParrotDescription() and Dog.DogDescription()", "No polymorphism: the caller has to know which name to use for which class", "Same name, Description(), in each class"],
  ["Testing the type", "if type(Item) == Parrot: ... elif type(Item) == Dog: ...", "The code has to change for every new class", "Item.Description() and let the object decide"],
  ["Misspelling the name", "def Descripton(self): ...  # in Parrot", "The spelling differs, so it is a new method and the parent's still runs", "Match the name exactly"],
  ["Confusing it with inheritance", "'Polymorphism is when a class takes its parent's methods'", "That is inheritance", "Same method name, different behaviour per class"],
  ["Only one class", "A single Animal class with Description()", "There is no variety, so nothing is polymorphic", "At least two classes with the method"]
], ["Mistake", "Code or answer", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Which idea is described?", buckets: [{"label": "Inheritance"}, {"label": "Overriding"}, {"label": "Polymorphism"}], items: [{"text": "A Parrot gets Name and Sound from Animal", "b": 0}, {"text": "Parrot defines Description() with the same name as Animal's", "b": 1}, {"text": "One loop calls Description() on a list holding Animals, Parrots and Dogs", "b": 2}, {"text": "class Dog(Animal):", "b": 0}, {"text": "The same call gives different results depending on the object", "b": 2}, {"text": "A child redefines a parent's method", "b": 1}, {"text": "A child class is written without repeating the shared attributes", "b": 0}, {"text": "A new class is added and the loop is not changed", "b": 2}], done: "Inheritance shares code; overriding replaces a method; polymorphism is the effect of one call giving different behaviours." });
Lib.order($("#o1"), { prompt: "Put the steps in order: what happens when the loop calls Item.Description() on a Dog.", items: ["The loop takes the next object from the list", "It calls Item.Description()", "Python looks in the object's own class, Dog", "Dog has a Description(), so it runs", "The Dog's text is printed"], done: "Take, call, look in own class, run, print." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Polymorphism", "The same method call behaves differently for objects of different classes"], ["Overriding", "A child redefines a method with the same name as the parent's"], ["Inheritance", "A child takes the parent's attributes and methods"], ["Base class", "The class that inherited methods come from"], ["Same name, different behaviour", "The key idea of polymorphism"]], done: "Learn these terms." });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does polymorphism mean?", opts: ["One class inside another", "Same method name, different behaviour in different classes", "Hiding data", "Copying a class"], a: 1, why: "Many forms." },
  { q: "Which makes polymorphism possible in the exam?", opts: ["Overriding a method in a child class", "Making attributes public", "A longer constructor", "Using print"], a: 0, why: "The child redefines the parent's method." },
  { q: "A list holds Animal, Parrot and Dog objects. Item.Description() is called for each. What happens?", opts: ["An error", "Each object runs its own class's version", "Only Animal's version runs", "The first object's version runs for all"], a: 1, why: "That is polymorphism." },
  { q: "What is the main advantage?", opts: ["Faster programs", "New classes can be added without changing the calling code", "Data is hidden", "Less memory"], a: 1, why: "The loop does not need to know the type." },
  { q: "Which is an example of the same method name in two classes with different behaviour?", opts: ["GetName in Animal and Dog, inherited", "Description in Parrot and Dog, each written differently", "__init__ in Animal only", "Fetch in Dog only"], a: 1, why: "Same name, different behaviour." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Polymorphism", "Same method name; each class behaves in its own way."],
  ["Overriding", "A child redefines a parent's method."],
  ["Inheritance", "Child takes the parent's attributes and methods."],
  ["Why use polymorphism?", "One loop works for many classes; new classes need no changes."],
  ["Description() example", "Animal, Parrot and Dog each print their own text."],
  ["Not polymorphism", "Different method names for each class."],
  ["Not polymorphism", "A chain of IFs testing the class."],
  ["Many forms", "The meaning of the word polymorphism."],
] });
