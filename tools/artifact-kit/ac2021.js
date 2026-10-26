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
  const lines = ["Ana", "Ben", "Cho", "Dev", "Eli"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "Names.txt", "sm");
    lines.forEach((l, i) => { o += SV.rect(30, 30 + i * 40, 160, 34, i === k - 1 ? "cell-warn" : i < k - 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(46, 53 + i * 40, l, "lbl", { style: "font-family:var(--mono);font-size:15px" }); });
    if (k >= 1 && k <= 5) o += SV.text(200, 53 + (k - 1) * 40, "◀ file pointer", "sm");
    o += SV.text(300, 22, "Names array", "sm");
    for (let i = 0; i < 5; i++) o += memCell(300, 30 + i * 40, i, i < k ? lines[i] : "", i === k - 1 ? "cell-warn" : "f3", 1, 160, 34);
    o += SV.text(520, 60, "Line", "sm") + SV.rect(520, 66, 140, 40, "f2", { rx: 6, ...op(0.55) }) + SV.text(590, 93, k >= 1 && k <= 5 ? lines[k - 1] : "", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" });
    if (k >= 6) o += SV.text(520, 150, "end of file", "lbl bd t3") + SV.text(520, 172, "the loop stops", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 250, label: "Reading a text file into an array", base: { i: 0 }, draw, tween: 400, dwell: 2600, steps: [
    { cap: "<code>OPENFILE \"Names.txt\" FOR READ</code>: the pointer is at the start. The array is empty.", s: { i: 0 } },
    { cap: "<code>READFILE</code> reads line 1 into <code>Line</code> and moves the pointer on. <code>Line</code> is added to the array.", s: { i: 1 } },
    { cap: "The loop reads line 2, then adds it. One line each time round.", s: { i: 2 } },
    { cap: "Line 3.", s: { i: 3 } },
    { cap: "Line 4.", s: { i: 4 } },
    { cap: "Line 5. The pointer is now at the end.", s: { i: 5 } },
    { cap: "<code>EOF(\"Names.txt\")</code> is now true, so <code>WHILE NOT EOF</code> stops. <code>CLOSEFILE</code> then closes the file.", s: { i: 6 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const box = (x, title, rows, cls) => SV.text(x, 22, title, "sm") + rows.map((r, i) => SV.rect(x, 30 + i * 36, 150, 30, cls, { rx: 6 }) + SV.text(x + 14, 51 + i * 36, r, "lbl", { style: "font-family:var(--mono);font-size:14px" })).join("");
    o += box(20, "Before", ["Ana", "Ben", "Cho"], "cell");
    const w = k >= 2 ? ["Dev"] : ["Ana", "Ben", "Cho"], a = k >= 1 ? ["Ana", "Ben", "Cho", "Dev"] : ["Ana", "Ben", "Cho"];
    o += box(230, "After FOR WRITE \"Dev\"", k >= 2 ? ["Dev"] : ["(open)"], k >= 2 ? "cell-no" : "cell");
    o += box(480, "After FOR APPEND \"Dev\"", k >= 1 ? ["Ana", "Ben", "Cho", "Dev"] : ["(open)"], k >= 1 ? "cell-ok" : "cell");
    if (k >= 2) o += SV.text(230, 190, "old lines lost", "lbl bd t2") + SV.text(480, 190, "old lines kept, Dev added at the end", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "Write against append", base: { i: 0 }, draw, tween: 350, dwell: 3000, steps: [
    { cap: "The file Names.txt already holds Ana, Ben and Cho. The program wants to add the line Dev.", s: { i: 0 } },
    { cap: "Opened <b>FOR APPEND</b>, the existing lines are kept and <code>WRITEFILE</code> adds Dev at the <b>end</b>.", s: { i: 1 } },
    { cap: "Opened <b>FOR WRITE</b>, the file is emptied first, so after writing Dev only <b>Dev</b> is left. Choose WRITE only when the whole file is being replaced.", s: { i: 2 } }] });
})();

(function () {
  const src = ["Eli", "", "Fay", "", "Gus"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "ActiveFile.txt", "sm") + SV.text(330, 22, "ArchiveFile.txt", "sm");
    src.forEach((l, i) => { o += SV.rect(30, 30 + i * 38, 220, 32, i === k - 1 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(44, 52 + i * 38, l === "" ? "(blank)" : l, "lbl", { style: "font-family:var(--mono);font-size:14px" }); });
    for (let i = 0; i < Math.min(5, k); i++) { const t = src[i] === "" ? "Account not present" : src[i]; o += SV.rect(330, 30 + i * 38, 260, 32, src[i] === "" ? "cell-ok" : "f3", { rx: 6 }) + SV.text(344, 52 + i * 38, t, "lbl", { style: "font-family:var(--mono);font-size:14px" }); }
    if (k >= 1 && k <= 5) o += SV.text(620, 52 + (k - 1) * 38, "READFILE: " + (src[k - 1] === "" ? "\"\"" : src[k - 1]), "sm");
    if (k >= 6) o += SV.text(330, 240, "EOF reached: both files closed", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 255, label: "Copying a file and replacing blank lines", base: { i: 0 }, draw, tween: 300, dwell: 2400, steps: [
    { cap: "Both files are opened: Active for READ, Archive for WRITE. The loop runs until <code>EOF(\"ActiveFile.txt\")</code>.", s: { i: 0 } },
    { cap: "Line 1 is not blank: <code>WRITEFILE</code> copies it.", s: { i: 1 } },
    { cap: "Line 2 is blank, so the IF is true: <code>WRITEFILE ... \"Account not present\"</code>.", s: { i: 2 } },
    { cap: "Line 3 is copied.", s: { i: 3 } },
    { cap: "Line 4 is blank: replaced.", s: { i: 4 } },
    { cap: "Line 5 is copied.", s: { i: 5 } },
    { cap: "The end of the file is reached. Both files must be closed: <code>CLOSEFILE</code> twice.", s: { i: 6 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.text(30, 30, "Serial / sequential: read from the start", "lbl bd") + SV.rect(30, 40, 700, 26, "cell", { rx: 6 });
    const w = k >= 1 ? Math.min(1, s.p) * 600 : 0;
    o += SV.rect(30, 40, w + 2, 26, "f3", { rx: 6, ...op(0.7) }) + SV.text(30, 90, k >= 1 ? "records read: " + Math.round(s.p * 600) + " before record 600 is reached" : "", "sm");
    o += SV.text(30, 140, "Random: SEEK straight to the position", "lbl bd") + SV.rect(30, 150, 700, 26, "cell", { rx: 6 });
    if (k >= 2) o += SV.rect(30 + 600 - 2, 150, 6, 26, "cell-ok", { rx: 3 }) + arrow(632, 200, 632, 180, "u", "c2", 1) + SV.text(730, 222, "SEEK 600, then GETRECORD: 1 record read", "lbl bd t3", { "text-anchor": "end" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "Serial against random access", base: { i: 0, p: 0 }, draw, tween: 1200, dwell: 3500, steps: [
    { cap: "The temperature at position <b>600</b> is wanted from a file of 1440 records.", s: { i: 0, p: 0 } },
    { cap: "In a <b>serial</b> or <b>sequential</b> file the program reads from the start: 599 records are read and thrown away before the 600th.", s: { i: 1, p: 1 } },
    { cap: "In a <b>random</b> file, <code>SEEK</code> moves the pointer straight to position 600 and <code>GETRECORD</code> reads it. One read.", s: { i: 2, p: 1 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.text(30, 28, "AccountNumber = 4719", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 1) o += SV.text(30, 62, "Location ← Hash(4719) = 4719 MOD 11 = 6", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 92, "SEEK AccountFile, 6", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    for (let i = 0; i < 11; i++) o += memCell(430, 20 + i * 21, i, i === 6 && k >= 3 ? "4719 Hall" : i === 2 ? "1202 Ito" : i === 9 ? "7745 Ray" : "", i === 6 && k >= 2 ? "cell-warn" : "f3", 1, 280, 19);
    if (k >= 3) o += SV.text(30, 122, "GETRECORD AccountFile, Customer", "lbl", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(30, 152, "Customer = 4719 Hall", "lbl bd t3", { style: "font-family:var(--mono);font-size:16px" });
    return o;
  };
  Lib.stepper($("#stE"), { w: 760, h: 260, label: "Finding a record in a random file with a hash", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "A customer enters an account number. The file has 11 locations, numbered 0 to 10.", s: { i: 0 } },
    { cap: "The hash function turns the key into a location: 4719 MOD 11 = <b>6</b>.", s: { i: 1 } },
    { cap: "<code>SEEK</code> moves the file pointer to location 6.", s: { i: 2 } },
    { cap: "<code>GETRECORD</code> reads the record there into <code>Customer</code>. No other record was read.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let mode = 0, exists = true;
  const modes = ["READ", "WRITE", "APPEND"];
  const paint = () => {
    $$("#mB button").forEach((b, i) => b.classList.toggle("pri", i === mode)); $$("#mE button").forEach((b, i) => b.classList.toggle("pri", (i === 0) === exists));
    let rows, msg;
    if (mode === 0) { rows = exists ? ["Ana", "Ben", "Cho"] : null; msg = exists ? "FOR READ: the contents are unchanged. WRITEFILE is not allowed on a file opened for reading, so Dev is not added." : "FOR READ: the file does not exist, so the OPENFILE fails. This is the case exception handling is for."; }
    if (mode === 1) { rows = ["Dev"]; msg = exists ? "FOR WRITE: the old lines are lost. Only Dev is in the file." : "FOR WRITE: a new file is created containing only Dev."; }
    if (mode === 2) { rows = exists ? ["Ana", "Ben", "Cho", "Dev"] : ["Dev"]; msg = exists ? "FOR APPEND: the old lines are kept and Dev is added at the end." : "FOR APPEND: the file is created, and Dev is its first line."; }
    $("#mO").innerHTML = rows ? '<div class="tw"><table class="t mono"><tr><th>Names.txt afterwards</th></tr>' + rows.map((r) => `<tr><td>${r}</td></tr>`).join("") + "</table></div>" : '<div class="tw"><table class="t mono"><tr><th>Names.txt afterwards</th></tr><tr><td>error: file not found</td></tr></table></div>';
    $("#mV").textContent = msg;
  };
  $("#mB").innerHTML = modes.map((m, i) => `<button class="b" data-i="${i}">FOR ${m}</button>`).join(""); $("#mE").innerHTML = '<button class="b">File exists (Ana, Ben, Cho)</button><button class="b">File does not exist</button>';
  $$("#mB button").forEach((b) => (b.onclick = () => { mode = +b.dataset.i; paint(); })); $$("#mE button").forEach((b, i) => (b.onclick = () => { exists = i === 0; paint(); }));
  paint();
})();

/* Lab 2 */
(function () {
  const data = [12, 7, 30, 5, 18]; let st;
  const reset = () => { st = { pc: 0, ptr: 0, line: "", total: 0, open: false, msg: "Press Step to run the first statement." }; paint(); };
  const prog = ["OPENFILE \"Scores.txt\" FOR READ", "WHILE NOT EOF(\"Scores.txt\")", "   READFILE \"Scores.txt\", Line", "   Total ← Total + Line", "ENDWHILE", "CLOSEFILE \"Scores.txt\"", "OUTPUT Total"];
  const paint = () => {
    $("#rS").innerHTML = '<div class="code"><pre class="cp">' + prog.map((l, i) => `<span class="ln${i === st.pc ? " on" : ""}">${l.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</span>`).join("") + '</pre></div><div class="tw"><table class="t mono"><tr><th>pointer</th><th>Line</th><th>Total</th><th>EOF?</th></tr><tr><td>' + st.ptr + " of 5</td><td>" + st.line + "</td><td>" + st.total + "</td><td>" + (st.open ? (st.ptr >= 5) : "-") + "</td></tr></table></div>";
    $("#rV").textContent = st.msg;
  };
  $("#rN").onclick = () => {
    const p = st.pc;
    if (p === 0) { st.open = true; st.msg = "File opened for reading, pointer at the start."; st.pc = 1; }
    else if (p === 1) { if (st.ptr >= 5) { st.msg = "EOF is true: leave the loop."; st.pc = 5; } else { st.msg = "Not at the end of the file: enter the loop."; st.pc = 2; } }
    else if (p === 2) { st.line = data[st.ptr]; st.ptr++; st.msg = "READFILE reads " + st.line + " and moves the pointer on."; st.pc = 3; }
    else if (p === 3) { st.total += st.line; st.msg = "Total is now " + st.total + "."; st.pc = 1; }
    else if (p === 5) { st.open = false; st.msg = "File closed."; st.pc = 6; }
    else if (p === 6) { st.msg = "OUTPUT " + st.total + ": the sum of 12 + 7 + 30 + 5 + 18."; st.pc = 7; }
    paint();
  };
  $("#rR").onclick = reset; reset();
})();

/* Lab 3 */
(function () {
  let key = 4719;
  const slots = { 2: "1202 Ito", 9: "7745 Ray", 6: "4719 Hall" };
  const paint = () => {
    const loc = key % 11;
    $("#hT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location</th>' + Array.from({ length: 11 }, (_, i) => `<td${i === loc ? ' style="background:var(--warn-soft);font-weight:700"' : ""}>${i}</td>`).join("") + "</tr><tr><th>Stored</th>" + Array.from({ length: 11 }, (_, i) => `<td>${slots[i] ? slots[i].split(" ")[0] : ""}</td>`).join("") + "</tr></table></div>";
    const occ = slots[loc];
    $("#hV").innerHTML = `Hash(${key}) = ${key} MOD 11 = <b>${loc}</b>. ` + (occ ? (occ.startsWith(key + " ") ? "SEEK " + loc + " finds the record for this account." : `Location ${loc} is already used by account ${occ.split(" ")[0]}: a <b>collision</b>, so another method is needed to place this record.`) : `Location ${loc} is empty, so a new record would be stored here.`);
  };
  Lib.slider($("#hS"), { id: "hsl", label: "Account number ", min: 1000, max: 9999, value: key, fmt: (x) => x, onInput: (v) => { key = v; paint(); } });
  paint();
})();
Lib.classify($("#cl1"), { prompt: "Which open mode or file command fits?", buckets: [{"label": "Read a text file"}, {"label": "Replace a text file"}, {"label": "Add to a text file"}, {"label": "Random file"}], items: [{"text": "OPENFILE \"Data.txt\" FOR READ", "b": 0}, {"text": "OPENFILE \"Out.txt\" FOR WRITE", "b": 1}, {"text": "OPENFILE \"Log.txt\" FOR APPEND", "b": 2}, {"text": "SEEK \"Stock.dat\", 25", "b": 3}, {"text": "GETRECORD \"Stock.dat\", Item", "b": 3}, {"text": "READFILE \"Data.txt\", Line", "b": 0}, {"text": "open(\"Log.txt\", \"a\")", "b": 2}, {"text": "open(\"Data.txt\", \"r\")", "b": 0}, {"text": "open(\"Out.txt\", \"w\")", "b": 1}], done: "r reads, w replaces, a adds. SEEK, GETRECORD and PUTRECORD are for random files." });
Lib.classify($("#cl2"), { prompt: "Is it serial, sequential or random?", buckets: [{"label": "Serial"}, {"label": "Sequential"}, {"label": "Random"}], items: [{"text": "Records are stored in the order they were added", "b": 0}, {"text": "Records are stored in order of a key field", "b": 1}, {"text": "The record's location is calculated from its key", "b": 2}, {"text": "A new record is simply appended to the end", "b": 0}, {"text": "Adding a record means writing a new file with it in the right place", "b": 1}, {"text": "SEEK takes you straight to the record", "b": 2}], done: "Serial: order added. Sequential: key order. Random: direct access by address." });
Lib.order($("#o1"), { prompt: "Put the steps for processing a text file in order.", items: ["Open the file in the correct mode", "Read the first line", "Process it (add, copy, compare)", "Repeat until the end of the file", "Close the file"], done: "Open, read, process, repeat to EOF, close." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["EOF", "True when there is nothing more to read"], ["SEEK", "Moves the file pointer to a record"], ["GETRECORD", "Reads the record at the pointer"], ["PUTRECORD", "Writes a record at the pointer"], ["CLOSEFILE", "Ends file use and saves written data"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A text file has 25 lines. How many times does READFILE run in a loop that reads until the end of the file?", "a": 25, "unit": "", "tol": 0.01, "hint": "One read for each line.", "sol": "<b>25</b>."},
  {"q": "A random file has 500 records and you want record 350. How many records does GETRECORD read after SEEK 350?", "a": 1, "unit": "", "tol": 0.01, "hint": "SEEK moves straight there.", "sol": "<b>1</b>."},
  {"q": "A serial file has 500 records. How many records are read to reach record 350 from the start (including it)?", "a": 350, "unit": "", "tol": 0.01, "hint": "Read 1, 2, ... 350.", "sol": "<b>350</b>."},
  {"q": "Hash(Key) = Key MOD 11. At which location is account number 5000 stored?", "a": 6, "unit": "", "tol": 0.01, "hint": "11 × 454 = 4994, so the remainder is 5000 - 4994.", "sol": "<b>6</b> (5000 MOD 11 = 6)."},
  {"q": "A file is opened FOR APPEND. It has 8 lines. Two WRITEFILE statements run. How many lines does it have after?", "a": 10, "unit": "", "tol": 0.01, "hint": "8 + 2.", "sol": "<b>10</b>."},
  {"q": "A file with 8 lines is opened FOR WRITE and two lines are written. How many lines does it have after?", "a": 2, "unit": "", "tol": 0.01, "hint": "WRITE replaces the old contents.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement must come before GETRECORD in a random file?", opts: ["READFILE", "SEEK", "EOF", "OPENFILE FOR APPEND"], a: 1, why: "SEEK moves the pointer to the record." },
  { q: "A program must add new lines to the end of an existing log. Which mode?", opts: ["READ", "WRITE", "APPEND", "RANDOM"], a: 2, why: "APPEND keeps the old lines." },
  { q: "What does EOF tell you?", opts: ["The file is empty", "There is nothing more to read", "The file is closed", "The file is full"], a: 1, why: "End of file." },
  { q: "What type is a line read from a text file in Python?", opts: ["integer", "string", "boolean", "real"], a: 1, why: "Convert with int() if you need a number." },
  { q: "Why must a file be closed?", opts: ["To delete it", "So written data is saved and the file can be reused", "To make it random", "To sort it"], a: 1, why: "Closing finishes the writes." },
  { q: "Which file organisation stores records in order of a key?", opts: ["Serial", "Sequential", "Random", "Text"], a: 1, why: "Sequential files are ordered by key." },
] });
Lib.cards($("#fc1"), { cards: [
  ["OPENFILE ... FOR READ", "Open an existing file to read from the start."],
  ["... FOR WRITE", "Create or overwrite the file."],
  ["... FOR APPEND", "Add to the end of the file."],
  ["... FOR RANDOM", "Open for direct access to records."],
  ["READFILE / WRITEFILE", "Read or write one line of a text file."],
  ["EOF(File)", "True when no more data to read."],
  ["SEEK / GETRECORD / PUTRECORD", "Random access: move, read, write."],
  ["CLOSEFILE", "Always close what you open."],
] });
