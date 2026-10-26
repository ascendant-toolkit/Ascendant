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

(function () {
  const L = ["MyPet = Pet(\"Rex\", 2021)", "", "def __init__(self, NewName, NewYear):", "    self.__PetName = NewName", "    self.__YearBorn = NewYear"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = codeList(20, 20, [L[0], L[2], L[3], L[4]], k === 0 ? 0 : k === 1 ? 1 : k === 2 ? 2 : k === 3 ? 3 : -1, 1, 34, 350);
    if (k >= 1) o += classBox(420, 20, 300, k >= 5 ? "object stored in MyPet" : "self (a new, empty object)", ["__PetName: " + (k >= 3 ? "\"Rex\"" : "?"), "__YearBorn: " + (k >= 4 ? "2021" : "?")], 1, k >= 5 ? "f3" : "f1", 24);
    if (k >= 2) o += SV.text(20, 175, "parameters: NewName = \"Rex\", NewYear = 2021", "sm", { style: "font-family:var(--mono)" });
    if (k >= 5) o += SV.text(420, 165, "MyPet now refers to the object", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 200, label: "Creating an object from a class", base: { i: 0 }, draw, tween: 450, dwell: 3600, steps: [
    { cap: "The statement <code>Pet(\"Rex\", 2021)</code> calls the class like a function. Python makes a new, empty object.", s: { i: 0 } },
    { cap: "It runs <code>__init__</code> on the new object. Inside, the object is called <b>self</b>.", s: { i: 1 } },
    { cap: "The arguments become the parameters <code>NewName</code> and <code>NewYear</code>.", s: { i: 2 } },
    { cap: "<code>self.__PetName = NewName</code> creates the first private attribute on the object.", s: { i: 3 } },
    { cap: "<code>self.__YearBorn = NewYear</code> creates the second. The constructor has finished.", s: { i: 4 } },
    { cap: "The finished object is stored in <code>MyPet</code>. Each time the class is called a separate object is made.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(20, 20, 300, "Parrot.__init__ (child)", ["super().__init__(...)  # call parent", "self.WingSpan = pWingSpan", "self.NumberWords = pNumberWords"], 1, k === 1 || k === 4 ? "f3" : "f1", 20);
    if (k >= 2 && k <= 2) o += classBox(20, 140, 300, "Animal.__init__ (parent)", ["self.Name = pName", "self.Sound = pSound", "self.Size = pSize", "self.Intelligence = pIntelligence"], 1, "f3", 20) + arrow(170, 100, 170, 136, "d", "c1", 1);
    const rows = ["Name: " + (k >= 2 ? "\"Chewie\"" : "?"), "Sound: " + (k >= 2 ? "\"Squawk\"" : "?"), "Size: " + (k >= 2 ? "1" : "?"), "Intelligence: " + (k >= 2 ? "10" : "?"), "WingSpan: " + (k >= 4 ? "30" : "?"), "NumberWords: " + (k >= 4 ? "29" : "?")];
    o += classBox(440, 20, 290, k >= 5 ? "complete Parrot object" : "self (Parrot object)", rows, 1, k >= 5 ? "f3" : "f2", 24);
    if (k >= 2) o += SV.text(440, 226, "inherited attributes (from Animal) set first", "sm") + SV.text(440, 244, "then the Parrot's own attributes", "sm", op(k >= 4 ? 1 : 0.3));
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 262, label: "Building a Parrot object", base: { i: 0 }, draw, tween: 450, dwell: 3800, steps: [
    { cap: "<code>Parrot(\"Chewie\", \"Squawk\", 1, 10, 30, 29)</code> makes an empty Parrot object and runs Parrot's constructor on it.", s: { i: 0 } },
    { cap: "The first line of the child's constructor calls the <b>parent's constructor</b> with the four inherited values.", s: { i: 1 } },
    { cap: "<code>Animal.__init__</code> runs on the same object and sets Name, Sound, Size and Intelligence.", s: { i: 2 } },
    { cap: "It finishes, and control returns to the Parrot constructor.", s: { i: 3 } },
    { cap: "Now the child sets its <b>own</b> attributes: WingSpan and NumberWords.", s: { i: 4 } },
    { cap: "One object has all six attributes. If the parent constructor were never called, the first four would not exist.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(30, 20, 250, "class Animal", ["Description()  # version A"], 1, k === 2 ? "f3" : "f1", 20);
    o += classBox(330, 20, 380, "class Parrot(Animal)", k === 3 ? ["# no Description() here", "ChangeNumberWords()"] : ["Description()  # version B", "ChangeNumberWords()"], 1, k === 1 ? "f3" : "f2", 20);
    o += arrow(330, 52, 284, 52, "l", "c1", 0.8);
    const call = k === 1 ? "bird.Description()" : k === 2 ? "animal.Description()" : k === 3 ? "bird.Description()" : "";
    if (call) o += SV.text(30, 160, call, "lbl bd", { style: "font-family:var(--mono);font-size:17px" });
    if (k === 1) o += SV.text(30, 190, "bird is a Parrot: look in Parrot first, found: run version B", "lbl bd t3");
    if (k === 2) o += SV.text(30, 190, "animal is an Animal: run version A", "lbl bd t3");
    if (k === 3) o += SV.text(30, 190, "not in Parrot: look in the parent, Animal: run version A", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "Method lookup when a child overrides a method", base: { i: 0 }, draw, tween: 400, dwell: 3600, steps: [
    { cap: "Animal defines <code>Description()</code>. Parrot inherits from Animal.", s: { i: 0 } },
    { cap: "Parrot defines its own <code>Description()</code>, so it <b>overrides</b> the parent's. A call on a Parrot object finds the child's version first.", s: { i: 1 } },
    { cap: "A call on a plain Animal object runs the Animal version.", s: { i: 2 } },
    { cap: "If Parrot did not define the method, Python would search up to the parent and <b>inherit</b> that version.", s: { i: 3 } }] });
})();

(function () {
  const L = ["speed = speed + 40", "if speed > 100:", "    speed = 100", "position = position + speed"];
  const rows = [["1", "40", "no", "40", "40"], ["2", "80", "no", "80", "120"], ["3", "120", "yes", "100", "220"], ["4", "140", "yes", "100", "320"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = codeList(20, 20, L, k === 0 ? -1 : (k % 2 === 1 ? 0 : 3), 1, 34, 250);
    o += SV.text(310, 36, "call", "sm") + SV.text(360, 36, "speed + 40", "sm") + SV.text(470, 36, "over 100?", "sm") + SV.text(570, 36, "speed", "sm") + SV.text(650, 36, "position", "sm");
    rows.forEach((r, i) => {
      if (k < i + 1) return;
      const on = k === i + 1; r.forEach((c, j) => { o += SV.text([310, 360, 470, 570, 650][j], 66 + i * 34, c, on ? "lbl bd" : "lbl", { style: "font-family:var(--mono);font-size:15px", ...(r[2] === "yes" && j === 3 ? { fill: "var(--warn)" } : {}) }); });
    });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 215, label: "Four calls of IncreaseSpeed", base: { i: 0 }, draw, tween: 300, dwell: 2800, steps: [
    { cap: "Start: speed 0, position 0, <code>MaxSpeed</code> 100, <code>IncreaseAmount</code> 40. Each call runs the four lines.", s: { i: 0 } },
    { cap: "Call 1: 0 + 40 = 40, not over 100, speed 40. Position 0 + 40 = <b>40</b>.", s: { i: 1 } },
    { cap: "Call 2: 80. Position 40 + 80 = <b>120</b>.", s: { i: 2 } },
    { cap: "Call 3: 80 + 40 = 120, over 100, so the speed is limited to <b>100</b>. The position still grows: 120 + 100 = <b>220</b>.", s: { i: 3 } },
    { cap: "Call 4: the speed stays at 100 and the position goes up by 100 again: <b>320</b>. The limit applies to the speed, never to the position.", s: { i: 4 } }] });
})();

/* Lab 1 */
(function () {
  let max = 100, inc = 40, heli = false, vch = 15, mh = 40, spd, hp, vp, calls;
  const reset = () => { spd = 0; hp = 0; vp = 0; calls = []; paint(); };
  const paint = () => {
    $("#lH").textContent = "Helicopter: " + (heli ? "on" : "off"); $("#lH").classList.toggle("pri", heli);
    $("#lV").style.display = heli ? "" : "none"; $("#lX").style.display = heli ? "" : "none";
    $("#lT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Call</th><th>CurrentSpeed</th><th>HorizontalPosition</th>' + (heli ? "<th>VerticalPosition</th>" : "") + "</tr>" + calls.map((c, i) => `<tr><td>${i + 1}</td><td>${c[0]}${c[3] ? " (limited)" : ""}</td><td>${c[1]}</td>${heli ? `<td>${c[2]}${c[4] ? " (limited)" : ""}</td>` : ""}</tr>`).join("") + "</table></div>";
    $("#lv").textContent = calls.length ? "The speed stops rising at MaxSpeed (" + max + "), but the position keeps increasing by the current speed each call." : "Press Call IncreaseSpeed() to run the method.";
  };
  $("#lGo").onclick = () => {
    spd += inc; let lim = false; if (spd > max) { spd = max; lim = true; }
    hp += spd; let vlim = false; if (heli) { vp += vch; if (vp > mh) { vp = mh; vlim = true; } }
    calls.push([spd, hp, vp, lim, vlim]); if (calls.length > 10) calls.shift(); paint();
  };
  $("#lRe").onclick = reset; $("#lH").onclick = () => { heli = !heli; reset(); };
  Lib.slider($("#lM"), { id: "lms", label: "MaxSpeed ", min: 20, max: 200, value: max, fmt: (x) => x, onInput: (v) => { max = v; reset(); } });
  Lib.slider($("#lI"), { id: "lis", label: "IncreaseAmount ", min: 5, max: 80, value: inc, fmt: (x) => x, onInput: (v) => { inc = v; reset(); } });
  Lib.slider($("#lV"), { id: "lvs", label: "VerticalChange ", min: 1, max: 30, value: vch, fmt: (x) => x, onInput: (v) => { vch = v; reset(); } });
  Lib.slider($("#lX"), { id: "lxs", label: "MaxHeight ", min: 10, max: 100, value: mh, fmt: (x) => x, onInput: (v) => { mh = v; reset(); } });
  reset();
})();

/* Lab 2: class builder */
(function () {
  const sc = [
    { name: "Pet", attrs: [["PetID", "STRING"], ["PetName", "STRING"], ["DateRegistered", "DATE"]] },
    { name: "Card", attrs: [["Number", "INTEGER"], ["Colour", "STRING"]] },
    { name: "Appointment", attrs: [["DateSeen", "DATE"], ["PatientID", "INTEGER"], ["Doctor", "STRING"], ["Treatments", "STRING"]] }
  ];
  let cur = 0, pick = {};
  const key = (i, t) => cur + "_" + i + t;
  const paint = () => {
    $$("#gB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const s = sc[cur];
    $("#gC").innerHTML = '<div class="tw"><table class="t"><tr><th>Attribute</th><th>Getter</th><th>Setter</th></tr>' + s.attrs.map((a, i) => `<tr><td><code>${a[0]} : ${a[1]}</code></td><td><label><input type="checkbox" data-k="${i}g" ${pick[key(i, "g")] ? "checked" : ""}> Get${a[0]}</label></td><td><label><input type="checkbox" data-k="${i}s" ${pick[key(i, "s")] ? "checked" : ""}> Set${a[0]}</label></td></tr>`).join("") + "</table></div>";
    $$("#gC input").forEach((c) => (c.onchange = () => { pick[cur + "_" + c.dataset.k] = c.checked; paint(); }));
    const par = (a) => "New" + a[0], L = [`class ${s.name}:`];
    s.attrs.forEach((a) => L.push(`    # ${a[0]} : ${a[1]}`));
    L.push(`    def __init__(self, ${s.attrs.map(par).join(", ")}):`);
    s.attrs.forEach((a) => L.push(`        self.__${a[0]} = New${a[0]}`));
    s.attrs.forEach((a, i) => {
      if (pick[key(i, "g")]) L.push("", `    def Get${a[0]}(self):`, `        return self.__${a[0]}`);
      if (pick[key(i, "s")]) L.push("", `    def Set${a[0]}(self, New${a[0]}):`, `        self.__${a[0]} = New${a[0]}`);
    });
    const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    $("#gO").innerHTML = '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
  };
  $("#gB").innerHTML = sc.map((s, i) => `<button class="b" data-i="${i}">${s.name}</button>`).join("");
  $$("#gB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); }));
  paint();
})();

btnTable("eB", "eO", [
  ["Missing self", "def GetName(): return self.__Name", "TypeError: the method is given the object but has nowhere to put it", "def GetName(self):"],
  ["No parent constructor", "class Parrot(Animal): def __init__(self, n, w): self.WingSpan = w", "AttributeError when Name is used: the inherited attributes were never set", "super().__init__(n) as the first line of the child's constructor"],
  ["Attribute without self", "def __init__(self, NewName): __Name = NewName", "The value is a local variable, forgotten when the constructor ends", "self.__Name = NewName"],
  ["Number joined to text", "return \"Size \" + self.Size", "TypeError: cannot join a string and an integer", "return \"Size \" + str(self.Size)"],
  ["Return in a setter", "def SetAge(self, a): return a", "The attribute is never changed", "self.__Age = a"],
  ["Calling private from outside", "print(MyPet.__Name)", "AttributeError: a private attribute is not directly reachable", "print(MyPet.GetName())"],
  ["Overwriting instead of adding", "self.__X = XChange", "The object jumps to the new value instead of moving by it", "self.__X = self.__X + XChange"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "What does each line of Python do?", buckets: [{"label": "Declare a class"}, {"label": "Constructor"}, {"label": "Getter"}, {"label": "Setter"}, {"label": "Create an object"}, {"label": "Call the parent constructor"}, {"label": "Override a method"}], items: [{"text": "class Vehicle:", "b": 0}, {"text": "def __init__(self, NewID, NewMax):", "b": 1}, {"text": "def GetMaxSpeed(self):", "b": 2}, {"text": "def SetCurrentSpeed(self, CSP):", "b": 3}, {"text": "Car1 = Vehicle(\"V1\", 120)", "b": 4}, {"text": "super().__init__(pName, pSound)", "b": 5}, {"text": "class Parrot(Animal):", "b": 0}, {"text": "def Description(self): # in Parrot, also in Animal", "b": 6}, {"text": "return self.__HorizontalPosition", "b": 2}, {"text": "self.__CurrentSpeed = CSP", "b": 3}], done: "class declares, __init__ is the constructor, Get returns, Set assigns, calling the class creates, super().__init__ calls the parent, and the same method name in the child overrides." });
Lib.order($("#o1"), { prompt: "Put the steps for writing a child class in order.", items: ["Write the class header with the parent in brackets", "Add attribute comments for the new attributes only", "Write the constructor taking the parent's values and the new ones", "Call the parent constructor with the inherited values", "Assign the new attributes", "Write or override the methods that are different"], done: "Header, comments, constructor, parent call, new attributes, methods." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["self", "The object the method is running on"], ["__init__", "The constructor, called when an object is created"], ["self.__Name", "A private attribute"], ["super().__init__(...)", "Calls the parent class constructor"], ["Same method name in the child", "Overrides the parent's method"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A vehicle starts with speed 0 and position 0, IncreaseAmount 30 and MaxSpeed 100. After 2 calls to IncreaseSpeed(), what is the CurrentSpeed?", "a": 60, "unit": "", "tol": 0.01, "hint": "30, then 60.", "sol": "<b>60</b>."},
  {"q": "Same vehicle: what is the HorizontalPosition after 2 calls?", "a": 90, "unit": "", "tol": 0.01, "hint": "Position 30, then 30 + 60.", "sol": "<b>90</b>."},
  {"q": "Same vehicle: what is the CurrentSpeed after 5 calls?", "a": 100, "unit": "", "tol": 0.01, "hint": "30, 60, 90, 120 limited to 100, 100.", "sol": "<b>100</b>."},
  {"q": "Same vehicle: what is the HorizontalPosition after 4 calls?", "a": 280, "unit": "", "tol": 0.01, "hint": "30 + 60 + 90 + 100.", "sol": "<b>280</b>."},
  {"q": "NumberWords is 29. ChangeNumberWords(5) is called twice. What is NumberWords?", "a": 39, "unit": "", "tol": 0.01, "hint": "29 + 5 + 5.", "sol": "<b>39</b>."},
  {"q": "A Character is at x = 10. ChangePosition(4, 0) then ChangePosition(-7, 3) are called. What is the x coordinate?", "a": 7, "unit": "", "tol": 0.01, "hint": "10 + 4 - 7.", "sol": "<b>7</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the constructor in Python called?", opts: ["__new__", "__init__", "constructor", "init"], a: 1, why: "__init__ with two underscores each side." },
  { q: "What makes an attribute private?", opts: ["The word private", "Two underscores at the start of its name", "Capital letters", "A comment"], a: 1, why: "self.__Name is private." },
  { q: "What does super().__init__(...) do?", opts: ["Deletes the parent", "Calls the parent constructor", "Creates a new class", "Overrides a method"], a: 1, why: "It sets the inherited attributes." },
  { q: "What is wrong with: def GetAge(): return self.__Age", opts: ["Nothing", "It is missing self as a parameter", "It should print", "__Age is public"], a: 1, why: "Every method needs self." },
  { q: "A child class has a method with the same name as its parent's. What is this called?", opts: ["Inheritance", "Overriding", "Encapsulation", "Containment"], a: 1, why: "The child version runs for child objects." },
  { q: "How is an object created from the class Hand?", opts: ["Hand.new()", "MyHand = Hand(Card1, Card2, Card3, Card4, Card5)", "class MyHand", "create Hand"], a: 1, why: "Call the class like a function with the constructor's arguments." },
] });
Lib.cards($("#fc1"), { cards: [
  ["class Name:", "Declares a class."],
  ["__init__(self, ...)", "The constructor. Assigns the parameters to attributes."],
  ["self.__Attr", "A private attribute."],
  ["Getter", "def GetX(self): return self.__X"],
  ["Setter", "def SetX(self, v): self.__X = v"],
  ["class Child(Parent):", "Child inherits from Parent."],
  ["super().__init__(...)", "Calls the parent constructor."],
  ["Override", "Same method name in the child class."],
] });
