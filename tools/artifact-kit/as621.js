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
  const draw = (s) => { const k = Math.round(s.i); const v = [4, 12, 25][k]; const ok = v >= 5 && v <= 18; let o = SV.rect(30, 40, 360, 30, "cell", { rx: 4 }) + SV.rect(30 + (5 - 0) * 12, 40, 13 * 12, 30, "f1", { rx: 4 }) + SV.text(30 + 5 * 12, 34, "5", "sm", { "text-anchor": "middle" }) + SV.text(30 + 18 * 12, 34, "18", "sm", { "text-anchor": "middle" }) + SV.circle(30 + v * 12, 55, 8, ok ? "f2" : "f3");
    o += SV.text(30, 105, ["age entered: 4", "age entered: 12", "age entered: 25"][k] + (ok ? " → accepted" : " → rejected: outside the range 5 to 18"), "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 440, h: 130, label: "Range check", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A range check accepts ages from 5 to 18 inclusive. 4 is below the range: <b>rejected</b>.", "12 is inside the range: <b>accepted</b>.", "25 is above the range: <b>rejected</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const checks = ["presence", "format", "length", "range", "type"]; let o = SV.rect(20, 20, 200, 30, "cell", { rx: 4 }) + SV.text(30, 40, "05/07/2010", "lbl bd"); checks.forEach((c, i) => { o += SV.rect(260, 14 + i * 28, 240, 24, i < k ? "f1" : "cell", { rx: 4 }) + SV.text(270, 31 + i * 28, c + " check" + (i < k ? " ✓" : ""), "lbl", { style: "font-size:12px" }); }); o += SV.text(20, 160, k >= 5 ? "Valid: reasonable and in the right format (not proof it is correct)" : "", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 175, label: "Several checks", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The date of birth 05/07/2010 is entered.", "Presence: it is not blank.", "Format: it matches dd/mm/yyyy.", "Length: exactly 10 characters.", "Range: between 1900 and today.", "Type: it is a valid DATE."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lines = ["4 1 6 2", "sum: 4 + 1 + 6 + 2 = 13", "13 MOD 10 = 3: check digit 3", "new number 41623", "entered as 41633: recalculated digit 4 ≠ 3: rejected"]; let o = ""; lines.slice(0, k + 1).forEach((l, i) => { o += SV.text(30, 30 + i * 28, l, i === k ? "lbl bd t3" : "lbl", { style: "font-size:14px" }); }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 160, label: "Check digit", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The original number is 4162.", "Sum the digits.", "Take the remainder when divided by 10.", "Append it to get the new number.", "A single-digit error changes the sum, so the number is rejected."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const inp = $("#vIn"); const paint = () => { const t = inp.value; const m = t.match(/^(\d\d)\/(\d\d)\/(\d{4})$/); const d = m ? new Date(+m[3], +m[2] - 1, +m[1]) : null; const real = d && d.getDate() === +m[1] && d.getMonth() === +m[2] - 1;
    const rows = [["Presence", t.length > 0], ["Length (10 characters)", t.length === 10], ["Format (dd/mm/yyyy)", !!m], ["Type (a real date)", !!real], ["Range (1900 to today)", !!real && d.getFullYear() >= 1900 && d <= new Date()]];
    $("#vOut").innerHTML = '<div class="tw"><table class="t"><tr><th>Check</th><th>Result</th></tr>' + rows.map(([n, ok]) => `<tr><td>${n}</td><td style="color:var(${ok ? "--good" : "--bad"})"><b>${ok ? "pass" : "fail"}</b></td></tr>`).join("") + "</table></div>" + `<div class="verdict">${rows.every((r) => r[1]) ? "Valid: it passes every check, but validation cannot tell whether it is the person's real date of birth." : "Rejected by at least one check."}</div>`; };
  inp.oninput = paint; paint();
})();
(function () {
  let n = 4162; const paint = () => { const dg = String(n).split("").map(Number), sum = dg.reduce((a, b) => a + b, 0), cd = sum % 10; $("#cV").innerHTML = `Original <b>${n}</b>: digits sum to <b>${dg.join(" + ")} = ${sum}</b>; ${sum} MOD 10 = <b>${cd}</b>, so the new number is <b>${n}${cd}</b>. If a single digit is mistyped the sum changes, so the recalculated check digit will not match and the entry is rejected.`; };
  Lib.slider($("#cS"), { id: "c1", label: "Original number ", min: 100, max: 9999, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("wB", "wO", [
  ["The password must be at least 8 characters", "Length check", "Counts characters"],
  ["Percentage must be 0 to 100", "Range check", "Two limits"],
  ["Email must contain @", "Format check", "Pattern of characters"],
  ["A name must not be left empty", "Presence check", "Entered or not"],
  ["Choose from Mon, Tue, Wed...", "Existence check", "List of allowed values"],
  ["Last digit of a barcode", "Check digit", "Calculated from the others"]
], ["Rule", "Check", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which validation check does it describe?", buckets: [{"label": "Range"}, {"label": "Presence"}, {"label": "Length"}, {"label": "Format"}, {"label": "Existence"}], items: [{"text": "The date of birth must be between 1900 and today", "b": 0}, {"text": "The name field cannot be left blank", "b": 1}, {"text": "The password must be exactly 8 characters", "b": 2}, {"text": "A code must be two letters, a number then a symbol", "b": 3}, {"text": "The colour must be Red, Yellow or Blue", "b": 4}, {"text": "A mark must be from 0 to 100", "b": 0}], done: "Range, presence, length, format, existence." });
Lib.classify($("#cl2"), { prompt: "Validation or verification?", buckets: [{"label": "Validation"}, {"label": "Verification"}], items: [{"text": "Presence check", "b": 0}, {"text": "Double entry", "b": 1}, {"text": "Range check", "b": 0}, {"text": "Visual check", "b": 1}, {"text": "Format check", "b": 0}, {"text": "Comparing entered data with the original document", "b": 1}], done: "Validation: sensible. Verification: same as the original." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Range check", "Between a lower and an upper limit"], ["Limit check", "Above or below one limit only"], ["Length check", "Correct number of characters"], ["Presence check", "Data has been entered"], ["Check digit", "A digit calculated from the others"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the check digit steps in order.", items: ["Add the digits of the original number", "Divide the sum by 10 and take the remainder", "Append the remainder to the number", "On entry, recalculate from the original digits", "Reject the input if the digits do not match"], done: "Sum, remainder, append, recalculate, compare." });
Lib.calc($("#c1"), { qs: [
  {"q": "Find the check digit for 5384 (sum of digits, remainder when divided by 10).", "a": 0, "unit": "", "tol": 0.01, "hint": "5 + 3 + 8 + 4 = 20.", "sol": "<b>0</b>: the new number is 53840."},
  {"q": "Find the check digit for 4162 (the worked example).", "a": 3, "unit": "", "tol": 0.01, "hint": "13 mod 10.", "sol": "<b>3</b>."},
  {"q": "A range check allows ages 5 to 18 inclusive. How many whole-number ages are allowed?", "a": 14, "unit": "", "tol": 0.01, "hint": "18 − 5 + 1.", "sol": "<b>14</b>."},
  {"q": "A length check requires exactly 10 characters. How many of 'dd/mm/yyyy' characters is that?", "a": 10, "unit": "", "tol": 0.01, "hint": "2 + 1 + 2 + 1 + 4.", "sol": "<b>10</b>."},
  {"q": "The number 41633 is entered. Its first four digits are 4163. What check digit should it have (and is 41633 accepted? Answer the correct check digit).", "a": 4, "unit": "", "tol": 0.01, "hint": "4 + 1 + 6 + 3 = 14.", "sol": "<b>4</b>: 41633 has 3, so it is rejected."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A range check tests:", opts: ["Between two limits", "Blank fields", "Data type only", "Spelling"], a: 0, why: "Between limits." },
  { q: "A presence check ensures:", opts: ["Data has been entered", "The data is correct", "The data matches the paper", "A back-up exists"], a: 0, why: "Entered." },
  { q: "Validation checks the data is:", opts: ["Reasonable", "The same as the original", "Encrypted", "Copied"], a: 0, why: "Reasonable." },
  { q: "A check digit detects:", opts: ["Single-digit errors", "All errors", "Viruses", "Copying"], a: 0, why: "Single-digit errors." },
  { q: "A format check tests:", opts: ["The pattern of characters", "The number of rows", "The speed", "The author"], a: 0, why: "Pattern." },
  { q: "Valid data can still be:", opts: ["Wrong", "Impossible", "Blank", "Encrypted"], a: 0, why: "Wrong." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Presence", "Not left blank."],
  ["Range", "Between two limits."],
  ["Limit", "One limit only."],
  ["Length", "Number of characters."],
  ["Format", "Pattern of characters."],
  ["Type", "Right data type."],
  ["Existence", "In a list of values."],
  ["Check digit", "Sum of digits mod 10, appended."],
] });
