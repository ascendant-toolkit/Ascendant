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
(function () { const SC = [[{"k": "cls", "x": 20, "y": 20, "w": 330, "title": "Parrot.__init__ (child)", "rows": ["super().__init__(pName, pSound)", "self.__WingSpan = pWingSpan"], "cls": "f1", "lh": 24}, {"k": "cls", "x": 440, "y": 20, "w": 290, "title": "self (Parrot object)", "rows": ["Name: ?", "Sound: ?", "WingSpan: ?"], "cls": "f1", "lh": 24}], [{"k": "cls", "x": 20, "y": 20, "w": 330, "title": "Parrot.__init__ (child)", "rows": ["super().__init__(pName, pSound)", "self.__WingSpan = pWingSpan"], "cls": "f3", "lh": 24}, {"k": "cls", "x": 440, "y": 20, "w": 290, "title": "self (Parrot object)", "rows": ["Name: ?", "Sound: ?", "WingSpan: ?"], "cls": "f1", "lh": 24}, {"k": "arr", "a": [180, 100, 180, 138], "d": "d"}, {"k": "cls", "x": 20, "y": 140, "w": 330, "title": "Animal.__init__ (parent)", "rows": ["self.__Name = pName", "self.__Sound = pSound"], "cls": "f2", "lh": 24}], [{"k": "cls", "x": 20, "y": 20, "w": 330, "title": "Parrot.__init__ (child)", "rows": ["super().__init__(pName, pSound)", "self.__WingSpan = pWingSpan"], "cls": "f1", "lh": 24}, {"k": "cls", "x": 440, "y": 20, "w": 290, "title": "self (Parrot object)", "rows": ["Name: \"Polly\"", "Sound: \"Squawk\"", "WingSpan: ?"], "cls": "f2", "lh": 24}, {"k": "cls", "x": 20, "y": 140, "w": 330, "title": "Animal.__init__ (parent)", "rows": ["self.__Name = pName", "self.__Sound = pSound"], "cls": "f3", "lh": 24}], [{"k": "cls", "x": 20, "y": 20, "w": 330, "title": "Parrot.__init__ (child)", "rows": ["super().__init__(pName, pSound)", "self.__WingSpan = pWingSpan"], "cls": "f3", "lh": 24}, {"k": "cls", "x": 440, "y": 20, "w": 290, "title": "self (Parrot object)", "rows": ["Name: \"Polly\"", "Sound: \"Squawk\"", "WingSpan: 30"], "cls": "f3", "lh": 24}], [{"k": "cls", "x": 440, "y": 20, "w": 290, "title": "complete Parrot object", "rows": ["Name: \"Polly\"", "Sound: \"Squawk\"", "WingSpan: 30"], "cls": "f3", "lh": 24}, {"k": "txt", "x": 30, "y": 70, "s": "inherited: Name, Sound", "c": "lbl bd", "m": 0}, {"k": "txt", "x": 30, "y": 100, "s": "new in Parrot: WingSpan", "c": "lbl bd", "m": 0}]], CAPS = ["<code>Parrot(\"Polly\", \"Squawk\", 30)</code> makes an empty Parrot object and runs the Parrot constructor.", "The first line calls the <b>parent's constructor</b> with the two inherited values.", "<code>Animal.__init__</code> runs on the same object and sets Name and Sound.", "Control returns to the child, which sets <b>its own</b> attribute.", "One object has all three attributes. Without the parent call, Name and Sound would never exist."];
  Lib.stepper($("#stA"), { w: 760, h: 250, label: "Building a Parrot object", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "class Animal", "rows": ["GetName()", "Description()  # version A"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 400, "y": 20, "w": 320, "title": "class Parrot(Animal)", "rows": ["Description()  # version B"], "cls": "f2", "lh": 22}, {"k": "arr", "a": [398, 55, 334, 55], "d": "l"}], [{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "class Animal", "rows": ["GetName()", "Description()  # version A"], "cls": "f1", "lh": 22}, {"k": "cls", "x": 400, "y": 20, "w": 320, "title": "class Parrot(Animal)", "rows": ["Description()  # version B"], "cls": "f3", "lh": 22}, {"k": "arr", "a": [398, 55, 334, 55], "d": "l"}, {"k": "txt", "x": 30, "y": 170, "s": "polly.Description()  runs B", "c": "lbl bd t3", "m": 0}], [{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "class Animal", "rows": ["GetName()", "Description()  # version A"], "cls": "f3", "lh": 22}, {"k": "cls", "x": 400, "y": 20, "w": 320, "title": "class Parrot(Animal)", "rows": ["Description()  # version B"], "cls": "f1", "lh": 22}, {"k": "arr", "a": [398, 55, 334, 55], "d": "l"}, {"k": "txt", "x": 30, "y": 170, "s": "polly.GetName()  runs Animal's", "c": "lbl bd t3", "m": 0}], [{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "class Animal", "rows": ["GetName()", "Description()  # version A"], "cls": "f3", "lh": 22}, {"k": "cls", "x": 400, "y": 20, "w": 320, "title": "class Parrot(Animal)", "rows": ["Description()  # version B"], "cls": "f2", "lh": 22}, {"k": "arr", "a": [398, 55, 334, 55], "d": "l"}, {"k": "txt", "x": 30, "y": 170, "s": "super().Description()  runs A", "c": "lbl bd t3", "m": 0}]], CAPS = ["Animal has <code>GetName()</code> and <code>Description()</code>. Parrot inherits from Animal and overrides <code>Description()</code> only.", "<code>polly.Description()</code>: Python looks in Parrot first and finds version B, so it runs.", "<code>polly.GetName()</code>: not in Parrot, so Python looks in the parent and finds it. The method is <b>inherited</b>.", "Inside Parrot's version, <code>super().Description()</code> can still run the parent's version and add to it."];
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "Method lookup with inheritance", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();

(function () {
  const objs = ["Animal", "Parrot", "Dog"], meths = ["GetName()", "Description()", "Fetch()"];
  const has = { Animal: ["GetName()", "Description()"], Parrot: ["Description()"], Dog: ["Fetch()"] }, parent = { Parrot: "Animal", Dog: "Animal" };
  let o = "Parrot", m = "Description()";
  const find = () => { const path = []; let c = o; while (c) { path.push(c); if (has[c].includes(m)) return { path, found: c }; c = parent[c]; } return { path, found: null }; };
  const paint = () => {
    $$("#iO button").forEach((b) => b.classList.toggle("pri", b.textContent === o)); $$("#iM button").forEach((b) => b.classList.toggle("pri", b.textContent === m));
    const r = find();
    $("#iC").innerHTML = codeHTML(["x = " + o + "(...)", "x." + m]);
    $("#iL").textContent = r.found ? "Looked in " + r.path.join(" then ") + ": found in " + r.found + (r.found === o ? " (the object's own class)." : " (inherited from the parent).") : "Looked in " + r.path.join(" then ") + ": not found. AttributeError.";
  };
  $("#iO").innerHTML = objs.map((x) => `<button class="b">${x}</button>`).join(""); $("#iM").innerHTML = meths.map((x) => `<button class="b">${x}</button>`).join("");
  $$("#iO button").forEach((b) => (b.onclick = () => { o = b.textContent; paint(); })); $$("#iM button").forEach((b) => (b.onclick = () => { m = b.textContent; paint(); }));
  paint();
})();

(function () {
  const paint = () => {
    const w = $("#bW").checked, n = $("#bN").checked, d = $("#bD").checked, c = $("#bC").checked;
    const at = [w && ["WingSpan", "INTEGER"], n && ["NumberWords", "INTEGER"]].filter(Boolean);
    const L = ["class Parrot(Animal):"]; at.forEach((a) => L.push(`    # ${a[0]} : ${a[1]}`));
    L.push(`    def __init__(self, pName, pSound${at.map((a) => ", p" + a[0]).join("")}):`, "        super().__init__(pName, pSound)"); at.forEach((a) => L.push(`        self.__${a[0]} = p${a[0]}`));
    if (d) L.push("", "    def Description(self):", '        return super().Description() + " (a parrot)"');
    if (c) L.push("", "    def ChangeNumberWords(self, Amount):", "        self.__NumberWords = self.__NumberWords + Amount");
    $("#bO").innerHTML = codeHTML(L) + (c && !n ? '<div class="verdict">ChangeNumberWords uses NumberWords, so the Parrot needs that attribute: tick it.</div>' : "");
  };
  $$("#bW, #bN, #bD, #bC").forEach((x) => (x.onchange = paint)); paint();
})();

btnTable("eB", "eO", [
  ["No parent constructor", "class Parrot(Animal): def __init__(self, n, w): self.__WingSpan = w", "The inherited attributes are never set, so GetName() fails or returns nothing useful", "super().__init__(n, s) as the first line"],
  ["Parent not named", "class Parrot: ...", "Parrot does not inherit anything", "class Parrot(Animal):"],
  ["Using the parent's private attribute", "return self.__Name  # inside Parrot", "Private to Animal, so Parrot cannot reach it directly", "return self.GetName()"],
  ["Repeating inherited attributes in the comments", "# Name : STRING  # inside Parrot's list", "They belong to Animal. Only list the new ones", "List only WingSpan"],
  ["Misspelling the override", "def Descripton(self): ...", "A new method, not an override; the parent's version still runs", "Same name as the parent's method"],
  ["Saying 'a copy'", "'The child makes a copy of the parent'", "The child is linked to the parent's code, not a copy", "'The child inherits the parent's attributes and methods'"]
], ["Mistake", "Code or answer", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "For a Parrot that inherits from Animal, where does each come from?", buckets: [{"label": "Inherited from Animal"}, {"label": "New in Parrot"}, {"label": "Overridden in Parrot"}], items: [{"text": "Name", "b": 0}, {"text": "Sound", "b": 0}, {"text": "WingSpan", "b": 1}, {"text": "GetName()", "b": 0}, {"text": "A Description() written again in Parrot", "b": 2}, {"text": "ChangeNumberWords()", "b": 1}, {"text": "NumberWords", "b": 1}, {"text": "A method in Parrot with the same name as one in Animal", "b": 2}], done: "Inherited items come from the parent; new items exist only in the child; an override is a child method with the parent's name." });
Lib.order($("#o1"), { prompt: "Put the steps for writing a child class in order.", items: ["Write the class header with the parent in brackets", "Add attribute comments for the new attributes only", "Write the constructor taking the parent's values and the new ones", "Call the parent constructor with the inherited values", "Assign the new attributes", "Write or override the methods that are different"], done: "Header, comments, constructor, parent call, new attributes, methods." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Parent class", "The class that is inherited from; also base or super class"], ["Child class", "The class that inherits; also derived class or subclass"], ["Inheritance", "A child takes the parent's attributes and methods"], ["Override", "A child method with the same name as the parent's"], ["super().__init__(...)", "Calls the parent's constructor"], ["is a", "The relationship between a child and its parent"]], done: "Learn these terms." });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement describes inheritance?", opts: ["A class contains objects of another class", "A class takes the attributes and methods of another class", "Data is hidden in a class", "A method has many forms"], a: 1, why: "Child takes from parent." },
  { q: "How is a Python child class declared?", opts: ["class Parrot inherits Animal", "class Parrot(Animal):", "class Animal(Parrot):", "Parrot = Animal"], a: 1, why: "Parent in brackets after the child's name." },
  { q: "What should the first line of the child's constructor usually do?", opts: ["Print a message", "Call the parent's constructor", "Delete the parent", "Create a new parent"], a: 1, why: "It sets the inherited attributes." },
  { q: "Which describes 'is a'?", opts: ["A Hand is a Card", "A Parrot is an Animal", "An Animal is a Parrot", "A Card is a Hand"], a: 1, why: "Inheritance is 'is a'; containment is 'has a'." },
  { q: "Why use inheritance?", opts: ["To hide data", "To avoid rewriting shared code", "To make methods private", "To print objects"], a: 1, why: "Write once, reuse." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Inheritance", "A child class takes the parent's attributes and methods."],
  ["Parent / base / super class", "The class that is inherited from."],
  ["Child / derived / subclass", "The class that inherits."],
  ["class Child(Parent):", "Python's inheritance header."],
  ["super().__init__(...)", "Calls the parent constructor."],
  ["Override", "Same method name in the child, so the child's version runs."],
  ["is a", "A Parrot is an Animal."],
  ["INHERITS / SUPER", "Pseudocode keywords."],
] });
