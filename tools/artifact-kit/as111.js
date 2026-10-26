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
  const draw = (s) => { const k = Math.round(s.i); const L = [["(Total * DepRate) + 1.5", ""], ["(124.00 * 2.00) + 1.5", "replace the variables"], ["248.00 + 1.5", "brackets first"], ["249.50", "add: the answer is a REAL"]]; let o = SV.rect(10, 8, 330, 34, "cell", { rx: 6 }) + SV.text(24, 31, L[k][0], "lbl bd", { style: "font-size:14px;font-family:monospace" }); o += SV.text(24, 64, L[k][1], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 350, h: 80, label: "Evaluate", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The expression.", "Put the values in.", "Evaluate the brackets.", "Finish the calculation."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const str = "JFMAMJJASOND"; const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < str.length; i++) { const pos = i + 1; const hl = k === 1 ? pos >= 1 && pos <= 3 : k === 2 ? pos >= 10 : k === 3 ? pos === 9 : false; o += SV.rect(14 + i * 28, 30, 26, 26, hl ? "f3" : "cell", { rx: 3 }) + SV.text(27 + i * 28, 48, str[i], "lbl bd", { "text-anchor": "middle" }) + SV.text(27 + i * 28, 22, pos, "sm", { "text-anchor": "middle" }); } o += SV.text(14, 84, ["\"JFMAMJJASOND\" with positions 1 to 12", "LEFT(s, 3) = \"JFM\"", "RIGHT(s, 3) = \"OND\"", "MID(s, 9, 1) = \"S\"  (position 9, one character)"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 360, h: 98, label: "Substrings", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["A string with its positions.", "LEFT takes from the start.", "RIGHT takes from the end.", "MID takes from a position."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["17 divided by 5", "17 / 5 = 3.4 (REAL)", "17 DIV 5 = 3 (whole number of 5s)", "17 MOD 5 = 2 (what is left: 3 × 5 = 15, 17 − 15)"]; let o = ""; for (let i = 0; i < 17; i++) o += SV.rect(10 + i * 18, 20, 15, 15, Math.floor(i / 5) < 3 && k >= 2 ? "f3" : (i >= 15 && k === 3 ? "f2" : "cell"), { rx: 3 }); o += SV.text(10, 62, L[k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 330, h: 80, label: "DIV and MOD", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["Seventeen items, shared in fives.", "/ gives the real result.", "DIV counts the complete groups.", "MOD is the remainder."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const sS = $("#sf_s"), sN = $("#sf_n"), sT = $("#sf_st"); const q = (x) => '"' + x + '"';
  const paint = () => { const s = sS.value, n = Math.max(0, +sN.value || 0), st = Math.max(1, +sT.value || 1); $("#sfV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Expression</th><th>Result</th></tr>' + [["LENGTH(s)", s.length], [`LEFT(s, ${n})`, q(s.slice(0, n))], [`RIGHT(s, ${n})`, q(n ? s.slice(-n) : "")], [`MID(s, ${st}, ${n})`, q(s.substr(st - 1, n))], ["UCASE(s)", q(s.toUpperCase())], ["LCASE(s)", q(s.toLowerCase())], ["IS_NUM(s)", s.trim() !== "" && !isNaN(+s) ? "TRUE" : "FALSE"]].map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td></tr>`).join("") + "</table></div>"; };
  [sS, sN, sT].forEach((e) => e.oninput = paint); paint();
})();
(function () {
  const E = [["(Total * DepRate) + 1.5", "249.50", "124.00 × 2.00 = 248.00, + 1.5"], ["Index MOD 30", "10", "100 = 3 × 30 + 10"], ["INT(Result) + 1 > 6", "FALSE", "INT(5.42) = 5, 5 + 1 = 6, 6 > 6 is FALSE"], ["NUM_TO_STR(LENGTH(MonthLetter))", "\"12\"", "LENGTH = 12, converted to a string"], ["NUM_TO_STR(Result + \"3.2\")", "ERROR", "a real plus a string is invalid"], ["MID(MonthLetter, MONTH(Birthday) - 2, 1)", "\"S\"", "MONTH = 11, 11 − 2 = 9, the 9th letter is S"], ["Available AND NOT(Index > 100)", "TRUE", "NOT(FALSE) = TRUE; TRUE AND TRUE"]];
  const bar = $("#evB"); E.forEach((e, i) => { const b = document.createElement("button"); b.className = "mono"; b.textContent = e[0]; b.onclick = () => { bar.querySelectorAll("button").forEach((x) => x.className = "mono" + (x === b ? " on" : "")); $("#evV").innerHTML = `<div class="verdict mono">${e[0]} = <b>${e[1]}</b></div><p>${e[2]}.</p>`; }; bar.appendChild(b); });
})();
btnTable("erB", "erO", [
  ["Result ← 2 & 4", "Error", "& joins strings; 2 and 4 are numbers"],
  ["SubString ← MID(\"pseudocode\", 4, 1)", "NO ERROR", "valid: gives \"u\""],
  ["IF x = 3 OR 4 THEN", "Error", "4 is not a Boolean: write x = 3 OR x = 4"],
  ["Result ← IS_NUM(-27.3)", "Error", "IS_NUM needs a string"],
  ["Message ← \"Done\" + LENGTH(MyString)", "Error", "cannot add a string and a number"],
  ["Y ← STR_TO_NUM(\"37\") + 5", "NO ERROR", "gives 42"]
], ["Statement", "Verdict", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which data type?", buckets: [{"label": "INTEGER"}, {"label": "REAL"}, {"label": "STRING"}, {"label": "BOOLEAN"}, {"label": "DATE"}], items: [{"text": "The number of items in an order (3)", "b": 0}, {"text": "The deposit paid, 15.75", "b": 1}, {"text": "A customer name, \"Mr Khan\"", "b": 2}, {"text": "Whether a customer is new (TRUE)", "b": 3}, {"text": "A membership start date, 19/02/1983", "b": 4}, {"text": "A postcode, \"CB2 1TN\"", "b": 2}], done: "Whole number, decimal, text, two-state, date." });
Lib.classify($("#cl2"), { prompt: "Does each statement contain a type error?", buckets: [{"label": "No error"}, {"label": "Error"}], items: [{"text": "Result ← 2 + 4", "b": 0}, {"text": "Result ← 2 & 4", "b": 1}, {"text": "Status ← TRUE AND FALSE", "b": 0}, {"text": "IF LENGTH(\"Password\") < \"10\" THEN", "b": 1}, {"text": "X ← STR_TO_NUM(\"37\") + 5", "b": 0}, {"text": "Message ← \"Done\" + LENGTH(MyString)", "b": 1}], done: "Operators and functions need the right types." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["LENGTH", "Number of characters"], ["MID", "Characters from a given position"], ["INT", "Whole-number part"], ["NUM_TO_STR", "Number into a string"], ["IS_NUM", "Tests if a string is a number"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for evaluating INT(DepRate * 10) & '%' in order.", items: ["Replace DepRate with its value 2.00", "Evaluate DepRate * 10 = 20.0", "Apply INT to give 20", "Convert to a string with NUM_TO_STR as needed: \"20\"", "Join with & '%' to give \"20%\""], done: "Innermost first." });
Lib.calc($("#c1"), { qs: [
  {"q": "What is 29 DIV 6?", "a": 4, "unit": "", "tol": 0.01, "hint": "Whole number of times 6 goes into 29.", "sol": "<b>4</b>."},
  {"q": "What is 100 MOD 30?", "a": 10, "unit": "", "tol": 0.01, "hint": "Remainder after dividing by 30.", "sol": "<b>10</b>."},
  {"q": "What is LENGTH(\"AB12345:Cleaning Brush (small)\") − 8?", "a": 22, "unit": "", "tol": 0.01, "hint": "Count the characters: 30.", "sol": "<b>22</b> (the length is 30)."},
  {"q": "MONTH(15/11/2009) − 2 is which position in \"JFMAMJJASOND\"?", "a": 9, "unit": "", "tol": 0.01, "hint": "11 − 2.", "sol": "<b>9</b>, which is 'S'."},
  {"q": "INT(5.42) + 1 gives what?", "a": 6, "unit": "", "tol": 0.01, "hint": "INT drops the decimal part.", "sol": "<b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The data type of a flag that is TRUE or FALSE:", opts: ["BOOLEAN", "STRING", "CHAR", "INTEGER"], a: 0, why: "Two states." },
  { q: "RIGHT(\"AB12345\", 3) gives:", opts: ["\"345\"", "\"AB1\"", "\"123\"", "345"], a: 0, why: "Last three characters, still a string." },
  { q: "Which is an error?", opts: ["NUM_TO_STR(5 + \"3\")", "STR_TO_NUM(\"37\") + 5", "INT(4.9)", "LENGTH(\"cat\")"], a: 0, why: "Number plus string." },
  { q: "An identifier table may include:", opts: ["The scope and an example value", "The program output only", "The mark scheme", "Nothing but the names"], a: 0, why: "Name, type, purpose, example." },
  { q: "17 MOD 5 =", opts: ["2", "3", "3.4", "12"], a: 0, why: "Remainder." },
  { q: "A constant:", opts: ["Is set once and not changed", "Changes every loop", "Is a type of loop", "Stores only strings"], a: 0, why: "Fixed value." },
] });
Lib.cards($("#fc1"), { cards: [
  ["INTEGER", "Whole number."],
  ["REAL", "Number with a decimal part."],
  ["STRING", "Text in double quotes."],
  ["BOOLEAN", "TRUE or FALSE."],
  ["DIV / MOD", "Quotient / remainder."],
  ["MID(s, a, n)", "n characters from position a."],
  ["NUM_TO_STR", "Number to string."],
  ["IS_NUM", "Needs a string."],
] });
