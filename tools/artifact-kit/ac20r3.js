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
(function () { const SC = [[{"k": "code", "x": 20, "y": 20, "lines": ["print(MyPet.GetPetName())", "def GetPetName(self):", "    return self.__PetName"], "hl": 0, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["print(MyPet.GetPetName())", "def GetPetName(self):", "    return self.__PetName"], "hl": 1, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["print(MyPet.GetPetName())", "def GetPetName(self):", "    return self.__PetName"], "hl": 2, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f3", "lh": 24}, {"k": "txt", "x": 20, "y": 150, "s": "returns \"Rex\"", "c": "lbl bd t3", "m": 0}], [{"k": "code", "x": 20, "y": 20, "lines": ["print(MyPet.GetPetName())", "def GetPetName(self):", "    return self.__PetName"], "hl": 0, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 20, "y": 150, "s": "Rex", "c": "lbl bd t3", "m": 0}]], CAPS = ["<code>print(MyPet.GetPetName())</code>: outside code asks the object for its name.", "The method runs inside the class.", "It reads <code>self.__PetName</code> and returns the value. The attribute is not changed.", "<code>print</code> shows the returned value. The getter itself printed nothing."];
  Lib.stepper($("#stA"), { w: 760, h: 215, label: "GetPetName()", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "code", "x": 20, "y": 20, "lines": ["MyPet.SetPetName(\"Max\")", "def SetPetName(self, NewName):", "    self.__PetName = NewName"], "hl": 0, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f1", "lh": 24}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet.SetPetName(\"Max\")", "def SetPetName(self, NewName):", "    self.__PetName = NewName"], "hl": 1, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Rex\"", "__YearBorn: 2021"], "cls": "f1", "lh": 24}, {"k": "txt", "x": 20, "y": 150, "s": "NewName = \"Max\"", "c": "sm", "m": 1}], [{"k": "code", "x": 20, "y": 20, "lines": ["MyPet.SetPetName(\"Max\")", "def SetPetName(self, NewName):", "    self.__PetName = NewName"], "hl": 2, "w": 340, "lh": 34}, {"k": "cls", "x": 420, "y": 20, "w": 300, "title": "MyPet", "rows": ["__PetName: \"Max\"", "__YearBorn: 2021"], "cls": "f3", "lh": 24}]], CAPS = ["<code>MyPet.SetPetName(\"Max\")</code>: outside code passes in a new name.", "The argument is copied into the parameter <code>NewName</code>.", "The assignment replaces the old value. Nothing is returned."];
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "SetPetName(\"Max\")", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();
(function () { const SC = [[{"k": "txt", "x": 20, "y": 40, "s": "self.__Cards", "c": "lbl bd", "m": 0}, {"k": "cls", "x": 20, "y": 70, "w": 132, "title": "Card A", "rows": ["index 0"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 164, "y": 70, "w": 132, "title": "Card B", "rows": ["index 1"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 308, "y": 70, "w": 132, "title": "Card C", "rows": ["index 2"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 452, "y": 70, "w": 132, "title": "Card D", "rows": ["index 3"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 596, "y": 70, "w": 132, "title": "Card E", "rows": ["index 4"], "cls": "f1", "lh": 20}], [{"k": "txt", "x": 20, "y": 40, "s": "self.__Cards", "c": "lbl bd", "m": 0}, {"k": "cls", "x": 20, "y": 70, "w": 132, "title": "Card A", "rows": ["index 0"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 164, "y": 70, "w": 132, "title": "Card B", "rows": ["index 1"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 308, "y": 70, "w": 132, "title": "Card C", "rows": ["index 2"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 452, "y": 70, "w": 132, "title": "Card D", "rows": ["index 3"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 596, "y": 70, "w": 132, "title": "Card E", "rows": ["index 4"], "cls": "f1", "lh": 20}, {"k": "txt", "x": 20, "y": 190, "s": "GetCard(2):  Position = 2", "c": "sm", "m": 1}], [{"k": "txt", "x": 20, "y": 40, "s": "self.__Cards", "c": "lbl bd", "m": 0}, {"k": "cls", "x": 20, "y": 70, "w": 132, "title": "Card A", "rows": ["index 0"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 164, "y": 70, "w": 132, "title": "Card B", "rows": ["index 1"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 308, "y": 70, "w": 132, "title": "Card C", "rows": ["index 2"], "cls": "f3", "lh": 20}, {"k": "cls", "x": 452, "y": 70, "w": 132, "title": "Card D", "rows": ["index 3"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 596, "y": 70, "w": 132, "title": "Card E", "rows": ["index 4"], "cls": "f1", "lh": 20}, {"k": "txt", "x": 20, "y": 190, "s": "returns Card C", "c": "lbl bd t3", "m": 0}], [{"k": "txt", "x": 20, "y": 40, "s": "self.__Cards", "c": "lbl bd", "m": 0}, {"k": "cls", "x": 20, "y": 70, "w": 132, "title": "Card A", "rows": ["index 0"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 164, "y": 70, "w": 132, "title": "Card B", "rows": ["index 1"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 308, "y": 70, "w": 132, "title": "Card C", "rows": ["index 2"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 452, "y": 70, "w": 132, "title": "Card D", "rows": ["index 3"], "cls": "f1", "lh": 20}, {"k": "cls", "x": 596, "y": 70, "w": 132, "title": "Card E", "rows": ["index 4"], "cls": "f3", "lh": 20}, {"k": "txt", "x": 20, "y": 190, "s": "GetCard(4) returns Card E", "c": "lbl bd t3", "m": 0}]], CAPS = ["A Hand holds five cards in a list. A getter with no parameter could only return the whole list.", "<code>MyHand.GetCard(2)</code>: the argument 2 is copied into the parameter <code>Position</code>.", "<code>return self.__Cards[Position]</code> picks index 2, the third card, and returns it.", "A different argument, a different card: <code>GetCard(4)</code> returns the last one."];
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "GetCard(Position)", base: { i: 0 }, draw: (s) => SC[Math.round(s.i)].map(sceneItem).join(""), tween: 400, dwell: 3600, steps: CAPS.map((c, i) => ({ cap: c, s: { i } })) }); })();

(function () {
  const o = { n: "Rex", y: 2021 }; let last = ["", "Press a button."];
  const paint = () => {
    $("#gO").innerHTML = codeHTML(['MyPet.__PetName = "' + o.n + '"', "MyPet.__YearBorn = " + o.y]);
    $("#gC").innerHTML = codeHTML([last[0] || " "]);
    $("#gL").textContent = last[1];
  };
  $("#g1").onclick = () => { last = ["print(MyPet.GetPetName())", 'Returned "' + o.n + '". The object is unchanged.']; paint(); };
  $("#g2").onclick = () => { last = ["print(MyPet.GetYearBorn())", "Returned " + o.y + ". The object is unchanged."]; paint(); };
  $("#g3").onclick = () => { o.n = $("#gN").value; last = ['MyPet.SetPetName("' + o.n + '")', "Nothing returned. The name has changed."]; paint(); };
  $("#g4").onclick = () => { const v = parseInt($("#gY").value, 10); if (isNaN(v)) last = ["MyPet.SetYearBorn(" + $("#gY").value + ")", "That is not a whole number, so it was not stored."]; else { o.y = v; last = ["MyPet.SetYearBorn(" + v + ")", "Nothing returned. The year has changed."]; } paint(); };
  paint();
})();

(function () {
  const cards = ["Card A", "Card B", "Card C", "Card D", "Card E"];
  const paint = () => {
    const p = +$("#pR").value; $("#pV").textContent = p;
    $("#pO").innerHTML = '<div class="btnrow">' + cards.map((c, i) => `<span class="b ${i === p ? "pri" : ""}" style="pointer-events:none">${i}: ${c}</span>`).join("") + "</div>";
    $("#pC").innerHTML = codeHTML(["MyHand.GetCard(" + p + ")", "", "def GetCard(self, Position):", "    return self.__Cards[Position]   # index " + p]);
    $("#pL").textContent = "Returns " + cards[p] + ". The first card is index 0, so the last is index 4.";
  };
  $("#pR").oninput = paint; paint();
})();

btnTable("eB", "eO", [
  ["Printing in a getter", "def GetName(self): print(self.__Name)", "Shows the value but returns None, so the caller gets nothing to use", "return self.__Name"],
  ["Returning in a setter", "def SetAge(self, a): return a", "The attribute is never changed", "self.__Age = a"],
  ["Setter with no parameter", "def SetAge(self): self.__Age = 5", "Always stores 5; the caller cannot choose the value", "def SetAge(self, NewAge):"],
  ["Parameter ignored", "def GetCard(self, Position): return self.__Cards", "Returns the whole list, not the card asked for", "return self.__Cards[Position]"],
  ["Parameter in a simple getter", "def GetName(self, x): return self.__Name", "The caller has to pass something that is never used", "def GetName(self):"],
  ["Overwriting instead of adding", "self.__X = XChange", "The object jumps to the new value instead of moving by it", "self.__X = self.__X + XChange"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Getter, setter or neither?", buckets: [{"label": "Getter"}, {"label": "Setter"}, {"label": "Neither"}], items: [{"text": "def GetAge(self): return self.__Age", "b": 0}, {"text": "def SetAge(self, a): self.__Age = a", "b": 1}, {"text": "def GetCard(self, Position): return self.__Cards[Position]", "b": 0}, {"text": "def SetCard(self, Position, c): self.__Cards[Position] = c", "b": 1}, {"text": "def __init__(self, n): self.__Name = n", "b": 2}, {"text": "def IncreaseSpeed(self): ...", "b": 2}, {"text": "def GetName(self): print(self.__Name)", "b": 2}, {"text": "def Description(self): return 'Pet'", "b": 2}], done: "A getter returns an attribute; a setter assigns one. The constructor, and methods that do a calculation or just report text, are neither. A method that prints instead of returning is not a getter." });
Lib.order($("#o1"), { prompt: "Put the lines of a setter for Pet's name in order.", items: ["def SetPetName(self, NewName):", "    self.__PetName = NewName"], done: "Header with the new value as a parameter, then the assignment." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Getter", "Returns the value of a private attribute"], ["Setter", "Changes the value of a private attribute"], ["Position parameter", "Selects which item of a list attribute to return or change"], ["return", "Used in a getter, not in a setter"], ["self.__X = NewX", "The body of a simple setter"], ["Validation", "Checking the new value in a setter before storing it"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A Hand holds cards [4, 9, 2, 7, 1] in positions 0 to 4. What is the number returned by GetCard(3)?", "a": 7, "unit": "", "tol": 0.01, "hint": "Positions start at 0.", "sol": "<b>7</b>."},
  {"q": "Same Hand: which position holds the card with number 2?", "a": 2, "unit": "", "tol": 0.01, "hint": "Count from 0.", "sol": "<b>2</b>."},
  {"q": "A Character is at x = 10. SetXPosition(25) is called. What does GetXPosition() return?", "a": 25, "unit": "", "tol": 0.01, "hint": "A setter replaces the value.", "sol": "<b>25</b>."},
  {"q": "A Character is at x = 10. ChangePosition(4) adds to the x coordinate. What is x afterwards?", "a": 14, "unit": "", "tol": 0.01, "hint": "Add, not replace.", "sol": "<b>14</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A getter should...", opts: ["Change the attribute", "Return the attribute's value", "Print the attribute", "Delete the attribute"], a: 1, why: "It returns without changing." },
  { q: "A setter for a single attribute normally has...", opts: ["No parameters", "One parameter, the new value", "Two parameters", "A return statement"], a: 1, why: "The new value arrives as a parameter." },
  { q: "Why does GetCard(self, Position) have a parameter?", opts: ["Getters must have parameters", "The attribute holds several values and it must say which", "It is a setter", "To make it private"], a: 1, why: "Position selects one item of the list." },
  { q: "Which statement is false?", opts: ["Setters do not return a value", "Getters change the attribute", "Getters return a value", "Setters assign a value"], a: 1, why: "Getters do not change the attribute." },
  { q: "How many getters should you write?", opts: ["One per attribute always", "Those the question asks for", "None", "Two per attribute"], a: 1, why: "Follow the question." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Getter", "Returns the value of a private attribute."],
  ["Setter", "Changes the value of a private attribute."],
  ["def GetX(self)", "return self.__X"],
  ["def SetX(self, NewX)", "self.__X = NewX"],
  ["GetCard(self, Position)", "A getter that needs an index because the attribute is a list."],
  ["Setter validation", "If the value is valid, assign it."],
  ["Getter: never print", "It returns; the caller prints."],
  ["Setter: never return", "It assigns."],
] });
