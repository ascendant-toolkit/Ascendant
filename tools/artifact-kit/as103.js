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
  const lines = ["Ann", "Ben", "Cy", "Di"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 14, "file", "sm"); lines.forEach((l, i) => o += SV.rect(20, 20 + i * 28, 140, 24, i === k - 1 ? "f3" : i < k - 1 ? "f1" : "cell", { rx: 4 }) + SV.text(28, 37 + i * 28, (i + 1) + "  " + l, "lbl", { style: "font-size:12px" })); o += SV.text(200, 50, k === 0 ? "OPENFILE ... FOR READ" : k <= 4 ? "READFILE: ThisLine = \"" + lines[k - 1] + "\"" : "EOF is TRUE: leave the loop, CLOSEFILE", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 140, label: "Reading", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Open the file in read mode.", "Read line 1.", "Read line 2.", "Read line 3.", "Read line 4.", "No more lines: EOF is true."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const old = ["Ann", "Ben"]; let o = SV.text(20, 14, k === 0 ? "file before" : k === 1 ? "after WRITE \"Cy\"" : "after APPEND \"Cy\"", "lbl bd", { style: "font-size:13px" }); const L = k === 0 ? old : k === 1 ? ["Cy"] : [...old, "Cy"]; L.forEach((l, i) => o += SV.rect(20, 24 + i * 28, 160, 24, l === "Cy" ? "f3" : "cell", { rx: 4 }) + SV.text(28, 41 + i * 28, l, "lbl", { style: "font-size:12px" })); o += SV.text(220, 60, k === 1 ? "old data overwritten" : k === 2 ? "old data kept" : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 440, h: 110, label: "Write and append", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The file holds two names.", "<b>WRITE</b> replaces everything.", "<b>APPEND</b> adds to the end."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const L = ["l1", "l2", "l3", "l4", "l5"]; const draw = (s) => { const k = Math.round(s.i); const x = k >= 1 ? L[k - 1] : "", y = k >= 2 ? L[k - 2] : "", z = k >= 3 ? L[k - 3] : ""; const v = k >= 3 ? [L[k - 3], L[k - 2], L[k - 1]] : ["", "", k >= 1 ? L[k - 1] : ""]; let o = ""; ["LineX", "LineY", "LineZ"].forEach((n, i) => o += SV.rect(20 + i * 100, 20, 92, 36, "cell", { rx: 5 }) + SV.text(66 + i * 100, 34, n, "sm", { "text-anchor": "middle" }) + SV.text(66 + i * 100, 50, v[i], "lbl bd", { "text-anchor": "middle" }));
    o += SV.text(20, 88, k === 0 ? "start: all empty" : "read " + L[k - 1] + ": shuffle LineX ← LineY, LineY ← LineZ, LineZ ← new line", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 420, h: 105, label: "Shuffle", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["Three variables start empty.", "Line 1 read.", "Line 2 read.", "Line 3 read.", "Line 4 read: the earliest line drops out.", "Line 5 read: LineX, LineY, LineZ hold the last three, in order."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let st; const reset = () => { st = ["Ann", "Ben", "Cy"]; paint("The file holds Ann, Ben, Cy."); }; const paint = (m) => { $("#wmV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>line</th><th>data</th></tr>' + st.map((l, i) => `<tr><td>${i + 1}</td><td>${l}</td></tr>`).join("") + `</table></div><div class="verdict">${m}</div>`; };
  $("#wm_w").onclick = () => { st = ["Dee"]; paint("WRITE overwrote the file: Ann, Ben and Cy are lost."); }; $("#wm_a").onclick = () => { st.push("Dee"); paint("APPEND added Dee at the end: the old names are kept."); }; $("#wm_r").onclick = reset; reset();
})();
(function () {
  const words = ["apple", "bread", "cheese", "dates", "eggs", "flour", "grapes"]; let target = "eggs", k = 0, found = 0; const paint = () => { $("#fsV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>line</th><th>word</th></tr>' + words.slice(0, k).map((w, i) => `<tr><td>${i + 1}</td><td>${w}${w === target ? " ← found" : ""}</td></tr>`).join("") + `</table></div><div class="verdict">${found ? `Found "${target}" on line <b>${found}</b> after reading ${k} line(s). The loop stops at once.` : k >= words.length ? `End of file: output "Not Found".` : "Press Read next line."}</div>`; };
  const bar = $("#sS"); words.forEach((w) => { const b = document.createElement("button"); b.textContent = w; b.onclick = () => { target = w; bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); k = 0; found = 0; paint(); }; if (w === target) b.className = "on"; bar.appendChild(b); });
  $("#fs_step").onclick = () => { if (found || k >= words.length) return; k++; if (words[k - 1] === target) found = k; paint(); }; $("#fs_reset").onclick = () => { k = 0; found = 0; paint(); }; paint();
})();
btnTable("mB", "mO", [
  ["Read a stock file line by line", "READ", "Only looking"],
  ["Create TestData.001", "WRITE", "A new file"],
  ["AddItem() adds a line to Stock.txt", "APPEND", "Keep the old items"],
  ["Add names to a support list that has earlier group tests", "APPEND", "WRITE would overwrite them"]
], ["Task", "Mode", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which file mode is needed?", buckets: [{"label": "READ"}, {"label": "WRITE"}, {"label": "APPEND"}], items: [{"text": "Searching a file for a value", "b": 0}, {"text": "Creating a brand new file", "b": 1}, {"text": "Adding an item to the end of Stock.txt", "b": 2}, {"text": "Counting the lines in a file", "b": 0}, {"text": "Replacing all the data in a file", "b": 1}, {"text": "Adding names to a file that already has other group tests", "b": 2}], done: "Read: look. Write: replace. Append: add." });
Lib.classify($("#cl2"), { prompt: "Is a file or an array the better store?", buckets: [{"label": "File"}, {"label": "Array"}], items: [{"text": "The data must be saved after the computer is switched off", "b": 0}, {"text": "A small, fixed number of values used while the program runs", "b": 1}, {"text": "The data must be used by another program", "b": 0}, {"text": "Fast access by index in a loop", "b": 1}, {"text": "The number of values is unknown and may be large", "b": 0}, {"text": "Temporary values that can be lost at the end", "b": 1}], done: "Permanent: file. Temporary: array." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["OPENFILE", "Opens a file in a mode"], ["READFILE", "Reads the next line"], ["WRITEFILE", "Writes a line"], ["EOF", "True at the end of the file"], ["CLOSEFILE", "Closes the file"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the file-search steps in order.", items: ["Open the file in read mode", "Repeat until the value is found or the end of the file", "Read a line and extract the field", "Compare it with the search value", "Close the file and report whether it was found"], done: "Open, loop, read, compare, close." });
Lib.calc($("#c1"), { qs: [
  {"q": "A file has 10 000 lines. A linear search finds a word on line 4321. How many lines are read?", "a": 4321, "unit": "", "tol": 0.01, "hint": "Up to and including that line.", "sol": "<b>4321</b>."},
  {"q": "A file has 12 lines. After APPEND of 3 lines, how many lines?", "a": 15, "unit": "", "tol": 0.01, "hint": "12 + 3.", "sol": "<b>15</b>."},
  {"q": "A file has 12 lines. After WRITE of 3 lines (overwriting), how many lines?", "a": 3, "unit": "", "tol": 0.01, "hint": "The old lines are gone.", "sol": "<b>3</b>."},
  {"q": "A suffix is always three characters. The file number 7 gives the suffix 007. How many zeros are added?", "a": 2, "unit": "", "tol": 0.01, "hint": "3 − 1.", "sol": "<b>2</b>."},
  {"q": "The record is <Field1><Field2><Field3> with lengths 4, 5 and 12. Field 2 starts at which character?", "a": 5, "unit": "", "tol": 0.01, "hint": "4 + 1.", "sol": "<b>5</b> (MID(Line, 5, 5))."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "APPEND mode:", opts: ["Adds to the end and keeps old data", "Deletes old data", "Only reads", "Closes the file"], a: 0, why: "Adds." },
  { q: "WRITE mode:", opts: ["Overwrites existing data", "Keeps old data", "Only reads", "Appends"], a: 0, why: "Overwrites." },
  { q: "EOF is true at:", opts: ["The end of the file", "The start", "Line 1", "Never"], a: 0, why: "End." },
  { q: "A file is better than an array when:", opts: ["Data must be kept after switch-off", "The data is tiny", "Speed only", "No data"], a: 0, why: "Permanent." },
  { q: "Before writing a number to a file you:", opts: ["Convert it to a string", "Round it", "Close it", "Sort it"], a: 0, why: "Convert to string." },
  { q: "Always:", opts: ["Close the file after use", "Leave it open", "Use WRITE", "Use EOF only"], a: 0, why: "Close." },
] });
Lib.cards($("#fc1"), { cards: [
  ["OPENFILE", "Mode: READ, WRITE or APPEND."],
  ["READFILE", "Next line into a variable."],
  ["WRITEFILE", "A line to the file."],
  ["EOF", "True at the end."],
  ["APPEND", "Add; keep old data."],
  ["WRITE", "Overwrite."],
  ["Search", "Loop until found or EOF."],
  ["Why a file", "Permanent; shared; unlimited."],
] });
