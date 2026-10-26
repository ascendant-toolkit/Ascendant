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

(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const B = (x, y, t, on) => SV.rect(x, y, 90, 26, on ? "f3" : "cell", { rx: 3 }) + SV.text(x + 45, y + 17, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); o += B(140, 6, "Head()", k === 0); if (k >= 1) { ["Mod_W", "Mod_X", "Mod_V"].forEach((t, i) => o += SV.line(185, 32, 40 + i * 140 + 45 - (i === 1 ? 0 : 0), 80, "w") + B(10 + i * 140, 80, t, k === 1)); } if (k >= 2) o += SV.text(14, 140, "arrows show the parameters", "lbl bd t3", { style: "font-size:11px" }); if (k >= 3) o += SV.text(14, 156, "curved arrow: Head repeats the calls", "lbl bd t2", { style: "font-size:11px" }); return o; };
  Lib.stepper($("#stA"), { w: 430, h: 170, label: "Chart", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The top module.", "The modules it calls, in order.", "Add the parameter arrows.", "Add selection or repetition."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(110, 6, 90, 26, "cell", { rx: 3 }) + SV.text(155, 23, "Menu()", "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); ["Add()", "Remove()", "Show()"].forEach((t, i) => { const hit = k === 1 ? i === 1 : k === 2 ? true : false; o += SV.line(155, 32, 45 + i * 110, 84, "w") + SV.rect(i * 110, 84, 90, 26, hit ? "f3" : "cell", { rx: 3 }) + SV.text(45 + i * 110, 101, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); }); o += SV.text(10, 136, k === 0 ? "Menu() calls one of three modules, or all three" : k === 1 ? "Diamond: this run calls only Remove()" : "Curved arrow: all three, in order, repeatedly", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 148, label: "Selection and repetition", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Menu() has three lower modules.", "Selection: only one is called.", "Repetition: all are called, in order, again and again."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const H = [["PROCEDURE Show(Name : STRING, Age : INTEGER)", "Two arrows down (Name, Age); none up."], ["FUNCTION IsValid(Number : INTEGER) RETURNS BOOLEAN", "One arrow down (Number); one arrow up with a filled circle (Boolean)."], ["PROCEDURE Sort(BYREF P2 : BOOLEAN)", "One arrow with a head at both ends and a filled circle."], ["FUNCTION Update(Key : STRING) RETURNS INTEGER", "Key down; an integer up."]];
  const bar = $("#hdB"); H.forEach((h) => { const b = document.createElement("button"); b.className = "mono"; b.textContent = h[0].split("(")[0]; b.onclick = () => { bar.querySelectorAll("button").forEach((x) => x.className = "mono" + (x === b ? " on" : "")); $("#hdV").innerHTML = `<div class="verdict mono">${h[0]}</div><p>${h[1]}</p>`; }; bar.appendChild(b); });
})();
btnTable("syB", "syO", [
  ["Diamond on a calling module", "Selection", "one lower module is called"],
  ["Curved arrow under a calling module", "Repetition", "the lower modules are called repeatedly, left to right"],
  ["Arrow up from a module", "A returned value", "the lower module is a function"],
  ["Arrow with two heads", "BYREF", "the value is passed in and changed"],
  ["Filled circle on an arrow", "A flag", "a Boolean value"]
], ["Symbol", "Meaning", "Detail"]);
Lib.classify($("#cl1"), { prompt: "Is the module a procedure or a function, from the chart?", buckets: [{"label": "Procedure"}, {"label": "Function"}], items: [{"text": "Arrow down only", "b": 0}, {"text": "Arrow down and an arrow up", "b": 1}, {"text": "Only an arrow up", "b": 1}, {"text": "No arrows at all", "b": 0}, {"text": "A two-headed arrow only", "b": 0}, {"text": "Header ends with RETURNS BOOLEAN", "b": 1}], done: "An upward arrow means a returned value." });
Lib.classify($("#cl2"), { prompt: "What does the symbol show?", buckets: [{"label": "Selection"}, {"label": "Repetition"}, {"label": "BYREF parameter"}], items: [{"text": "A diamond on the calling module", "b": 0}, {"text": "A curved arrow under the calling module", "b": 1}, {"text": "An arrow with a head at both ends", "b": 2}, {"text": "One of the lower modules is called", "b": 0}, {"text": "Lower modules are called repeatedly in order", "b": 1}, {"text": "A value passed in and changed", "b": 2}], done: "Diamond: choose. Curve: repeat. Two heads: in and out." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Rectangle", "A module"], ["Down arrow", "A parameter passed in"], ["Up arrow", "A value returned"], ["Diamond", "Selection"], ["Curved arrow", "Repetition"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for drawing a structure chart in order.", items: ["Put the calling module at the top", "Put the called modules below, in order", "Join each pair with a line", "Add the parameter arrows with circles", "Add the diamond or curved arrow"], done: "Boxes, lines, arrows, symbols." });
Lib.calc($("#c1"), { qs: [
  {"q": "A calling module has 3 lower modules. How many lines join it to them?", "a": 3, "unit": "", "tol": 0.01, "hint": "One each.", "sol": "<b>3</b>."},
  {"q": "PROCEDURE Mod_Y(W3 : REAL, Z8 : INTEGER) needs how many down arrows?", "a": 2, "unit": "", "tol": 0.01, "hint": "One per parameter.", "sol": "<b>2</b>."},
  {"q": "FUNCTION Mod_V(S2 : INTEGER) RETURNS BOOLEAN needs how many arrows in total?", "a": 2, "unit": "", "tol": 0.01, "hint": "One down, one up.", "sol": "<b>2</b>."},
  {"q": "PROCEDURE Mod_X(T4 : INTEGER, BYREF P3 : REAL): how many arrows?", "a": 2, "unit": "", "tol": 0.01, "hint": "T4 down, P3 two-headed.", "sol": "<b>2</b>."},
  {"q": "A chart has 6 modules. How many lines join them in the hierarchy?", "a": 5, "unit": "", "tol": 0.01, "hint": "Every module except the top has one line above it.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An arrow pointing up beside a line shows:", opts: ["A value returned to the caller", "A parameter passed down", "Selection", "Repetition"], a: 0, why: "Returned." },
  { q: "A diamond on a module means:", opts: ["One of the lower modules is called", "All are called repeatedly", "It is a function", "It is a library"], a: 0, why: "Selection." },
  { q: "A curved arrow under a module means:", opts: ["Repetition of the lower modules in order", "Selection", "A function", "A return"], a: 0, why: "Repetition." },
  { q: "A two-headed arrow shows:", opts: ["A BYREF parameter", "A function return", "Selection", "A library"], a: 0, why: "In and out." },
  { q: "A structure chart is produced in:", opts: ["The design stage", "The testing stage", "The analysis stage", "Maintenance"], a: 0, why: "Design." },
  { q: "A benefit of decomposition:", opts: ["Modules can be given to different teams", "Programs run faster", "No testing is needed", "No parameters are needed"], a: 0, why: "Teams." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Module", "A procedure or function."],
  ["Parameter", "A value passed to a module."],
  ["Diamond", "Selection."],
  ["Curved arrow", "Repetition."],
  ["Up arrow", "Returned value: a function."],
  ["Two-headed arrow", "BYREF."],
  ["Filled circle", "A Boolean flag."],
  ["Decomposition", "Breaking a problem into sub-problems."],
] });
