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
(function () { const SC = [[{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "Pet object (private data)", "rows": ["__PetName: \"Rex\"", "__Age: 3"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 30, "y": 150, "s": "outside code", "c": "lbl bd", "m": 0}, {"k": "txt", "x": 30, "y": 175, "s": "MyPet = Pet(\"Rex\", 3)", "c": "sm", "m": 1}], [{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "Pet object (private data)", "rows": ["__PetName: \"Rex\"", "__Age: 3"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 380, "y": 60, "s": "print(MyPet.__Age)", "c": "lbl bd", "m": 1}, {"k": "arr", "a": [375, 55, 335, 55], "d": "l"}, {"k": "txt", "x": 380, "y": 100, "s": "blocked: AttributeError", "c": "lbl bd t3", "m": 0}], [{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "Pet object (private data)", "rows": ["__PetName: \"Rex\"", "__Age: 3"], "cls": "f1", "lh": 24}, {"k": "cls", "x": 380, "y": 20, "w": 330, "title": "public methods", "rows": ["GetAge()", "SetAge(NewAge)"], "cls": "f2", "lh": 24}, {"k": "txt", "x": 380, "y": 150, "s": "print(MyPet.GetAge())", "c": "lbl bd", "m": 1}], [{"k": "cls", "x": 30, "y": 20, "w": 300, "title": "Pet object (private data)", "rows": ["__PetName: \"Rex\"", "__Age: 3"], "cls": "f3", "lh": 24}, {"k": "cls", "x": 380, "y": 20, "w": 330, "title": "public methods", "rows": ["GetAge()", "SetAge(NewAge)"], "cls": "f2", "lh": 24}, {"k": "arr", "a": [375, 90, 335, 90], "d": "l"}, {"k": "txt", "x": 380, "y": 150, "s": "returns 3", "c": "lbl bd t3", "m": 0}]], CAPS = ["A Pet object holds two private attributes. They are inside the class boundary.", "Outside code tries <code>print(MyPet.__Age)</code>. It reaches straight for the attribute.", "Instead it calls the public method <code>GetAge()</code>. The call goes to the object's own code.", "The method is inside the class, so it can read <code>self.__Age</code> and return the value."];
  Lib.stepper($("#stA"), { w: 760, h: 235, label: "Direct access against a method call", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "code", "x": 20, "y": 20, "lines": ["SetAge(5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"], "hl": 0, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "Pet", "rows": ["__PetName: \"Rex\"", "__Age: 3"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["SetAge(5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"], "hl": 1, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "Pet", "rows": ["__PetName: \"Rex\"", "__Age: 3"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 20, "y": 150, "s": "0 <= 5 <= 40: True", "c": "lbl bd t3", "m": 0}], [{"k": "code", "x": 20, "y": 20, "lines": ["SetAge(5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"], "hl": 2, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "Pet", "rows": ["__PetName: \"Rex\"", "__Age: 5"], "cls": "f3", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["SetAge(-5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"], "hl": 1, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "Pet", "rows": ["__PetName: \"Rex\"", "__Age: 5"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 20, "y": 150, "s": "0 <= -5 <= 40: False", "c": "lbl bd t3", "m": 0}], [{"k": "code", "x": 20, "y": 20, "lines": ["SetAge(-5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"], "hl": -1, "w": 330, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "Pet", "rows": ["__PetName: \"Rex\"", "__Age: 5"], "cls": "f3", "lh": 24}]], CAPS = ["<code>MyPet.SetAge(5)</code>: the setter checks the value before changing anything.", "5 is between 0 and 40, so the test passes.", "The age is stored.", "<code>MyPet.SetAge(-5)</code>: the test fails, so the assignment is skipped.", "The age is still 5. The object cannot be put into an invalid state from outside."];
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "SetAge only accepts 0 to 40", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();

(function () {
  let priv = true, age = 3, msg = "Press Set the age.";
  const paint = () => {
    $("#nP").classList.toggle("pri", priv); $("#nU").classList.toggle("pri", !priv);
    $("#nV").textContent = $("#nR").value;
    $("#nC").innerHTML = codeHTML(priv
      ? ["MyPet.SetAge(" + $("#nR").value + ")", "", "def SetAge(self, NewAge):", "    if NewAge >= 0 and NewAge <= 40:", "        self.__Age = NewAge"]
      : ["MyPet.Age = " + $("#nR").value, "", "# Age is public: any code can set any value"]);
    $("#nL").textContent = "Age is now " + age + ". " + msg;
  };
  const set = () => { const v = +$("#nR").value; if (!priv) { age = v; msg = v < 0 || v > 40 ? "The object now holds an impossible age, and nothing stopped it." : "Accepted."; } else if (v >= 0 && v <= 40) { age = v; msg = "The setter accepted the value."; } else msg = "The setter rejected " + v + ", so the age did not change."; paint(); };
  $("#nP").onclick = () => { priv = true; age = 3; msg = "Press Set the age."; paint(); };
  $("#nU").onclick = () => { priv = false; age = 3; msg = "Press Set the age."; paint(); };
  $("#nR").oninput = paint; $("#nGo").onclick = set; paint();
})();

btnTable("eB", "eO", [
  ["Making the attribute public", "self.Age = NewAge  # then MyPet.Age = -5", "Any code can set an invalid value; the data is not protected", "self.__Age = NewAge, with GetAge and SetAge"],
  ["Printing the private attribute", "print(MyPet.__Age)", "AttributeError from outside the class", "print(MyPet.GetAge())"],
  ["Making methods private", "def __GetAge(self): ...", "Outside code cannot call it, so the doorway is shut", "def GetAge(self): ..."],
  ["Setter with no check", "def SetAge(self, a): self.__Age = a", "Hidden, but anything is accepted, so the hiding achieves little", "Test the value before assigning"],
  ["Confusing it with inheritance", "'Encapsulation is when a child class takes the parent's methods'", "That is inheritance. Encapsulation is bundling and hiding", "Bundle attributes and methods; hide the data"]
], ["Mistake", "Code or answer", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Should it be private or public?", buckets: [{"label": "Private"}, {"label": "Public"}], items: [{"text": "self.__Age", "b": 0}, {"text": "def GetAge(self):", "b": 1}, {"text": "self.__PetName", "b": 0}, {"text": "def SetAge(self, NewAge):", "b": 1}, {"text": "The attribute MaxSpeed", "b": 0}, {"text": "The method IncreaseSpeed()", "b": 1}, {"text": "An attribute holding a patient's treatments", "b": 0}, {"text": "A method that returns the patient's ID", "b": 1}], done: "Attributes are normally private; the methods that other code needs are public." });
Lib.order($("#o1"), { prompt: "Put these in order: how outside code safely changes a private attribute.", items: ["Outside code calls the public setter", "The setter receives the new value", "The setter checks the value is valid", "If valid, the setter assigns it to the private attribute", "The object now holds the new value"], done: "Call, receive, check, assign, updated." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Encapsulation", "Bundling attributes and methods in a class and hiding the data"], ["Private", "Can only be used by code inside the class"], ["Public", "Can be used by any code"], ["Data hiding", "Outside code cannot read or change an attribute directly"], ["__Age", "A Python private attribute"], ["PRIVATE", "Pseudocode keyword for a private attribute"]], done: "Learn these terms." });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does encapsulation mean?", opts: ["A child takes the parent's methods", "Bundling attributes and methods together and hiding the data", "Many classes with one method name", "One class containing another"], a: 1, why: "Bundle and hide." },
  { q: "Why are attributes usually private?", opts: ["To make the program faster", "So they can only change through the class's methods", "So they use less memory", "Because Python requires it"], a: 1, why: "Protects the data and lets the class check values." },
  { q: "MyPet.__Age raises an error from outside the class. Why?", opts: ["The pet does not exist", "The attribute is private", "Age is a string", "It needs brackets"], a: 1, why: "Private attributes are not accessible directly." },
  { q: "Which is the best way to read a private attribute?", opts: ["Make it public", "Call a getter method", "Copy the class", "Use print on the class"], a: 1, why: "Go through a public method." },
  { q: "A setter checks the new value. What does this protect?", opts: ["The method name", "The object from holding an invalid value", "The constructor", "The class name"], a: 1, why: "Validation keeps the object valid." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Encapsulation", "Attributes and methods bundled in a class; data hidden behind methods."],
  ["Private", "Only code inside the class can use it."],
  ["Public", "Any code can use it."],
  ["Data hiding", "The data is reached only through the class's methods."],
  ["self.__Name", "Python private attribute."],
  ["PRIVATE / PUBLIC", "Pseudocode access keywords."],
  ["Validation in a setter", "Check the value before storing it."],
  ["Why encapsulate?", "Protect data, change the inside safely, simpler to use."],
] });
