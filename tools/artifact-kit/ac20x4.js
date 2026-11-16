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

const MONO = "font-family:var(--mono);font-size:13px";
function codeLines(x, y, lines, hl, w, lh) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 3, i === hl ? "cell-warn" : "cell", { rx: 4 }) + SV.text(x + 8, y + i * lh + lh / 2 + 3, l, "lbl", { style: "font-family:var(--mono);font-size:11px;white-space:pre" })).join("");
}
function vbox(x, y, name, val, cls, w) {
  return SV.text(x, y - 7, name, "sm") + SV.rect(x, y, w, 34, cls || "f2", { rx: 6, ...op(0.6) }) + SV.rect(x, y, w, 34, "ax", { rx: 6, fill: "none" }) + SV.text(x + w / 2, y + 22, String(val), "lbl bd", { "text-anchor": "middle", style: MONO });
}
/* a column of file rows. o: x,y,t,r + optional w, lh, hl (warn row), ok[], no[], nw (new row), ptr (pointer row), ptrLabel, addr (show row numbers), eof */
function fcol(o) {
  const w = o.w || 210, lh = o.lh || 28, rows = o.r || [];
  let s = SV.text(o.x, o.y - 8, o.t, "sm");
  if (!rows.length) s += SV.rect(o.x, o.y, w, lh - 4, "cell", { rx: 5, ...op(0.5) }) + SV.text(o.x + 10, o.y + lh / 2 + 3, "(empty)", "sm");
  rows.forEach((r, i) => {
    let c = "cell";
    if (o.ok && o.ok.includes(i)) c = "cell-ok";
    if (o.no && o.no.includes(i)) c = "cell-no";
    if (o.nw === i) c = "f3";
    if (o.hl === i) c = "cell-warn";
    s += SV.rect(o.x, o.y + i * lh, w, lh - 4, c, { rx: 5 });
    if (o.addr) s += SV.text(o.x + 10, o.y + i * lh + lh / 2 + 3, String(i), "sm", { style: MONO }) + SV.text(o.x + 36, o.y + i * lh + lh / 2 + 3, r, "lbl", { style: MONO });
    else s += SV.text(o.x + 10, o.y + i * lh + lh / 2 + 3, r, "lbl", { style: MONO });
  });
  if (o.ptr !== undefined && o.ptr !== null && o.ptr >= 0) s += SV.text(o.x + w + 8, o.y + o.ptr * lh + lh / 2 + 3, "◀ " + (o.ptrLabel || "pointer"), "sm");
  if (o.eof) s += SV.text(o.x, o.y + rows.length * lh + 12, "end of file", "sm");
  return s;
}
function stepDraw(C, t) {
  let o = "", y = 8;
  if (C.ps) {
    o += SV.text(8, 14, "Pseudocode", "sm");
    const wa = Math.max(...C.ps.map((l) => l.length)) * 6.6 + 18, wb = Math.max(...C.py.map((l) => l.length)) * 6.6 + 18, ex = Math.max(0, (744 - wa - wb - 14) / 2), xb = 8 + wa + ex + 14;
    o += SV.text(xb, 14, "Python", "sm") + codeLines(8, 22, C.ps, t.p, wa + ex, C.lh) + codeLines(xb, 22, C.py, t.y, wb + ex, C.lh);
    y = 22 + Math.max(C.ps.length, C.py.length) * C.lh + 14;
  }
  if (t.v && t.v.length) { t.v.forEach((v, j) => { o += vbox(8 + j * C.vw, y + 16, v[0], v[1], v[2], C.vw - 12); }); y += 82; }
  (t.f || []).forEach((f) => { o += fcol({ ...f, y: y + f.y }); });
  (t.t || []).forEach((q) => { o += SV.text(q[0], y + q[1], q[2], q[3] || "sm"); });
  return o;
}
const lineHTML = (L) => '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
(function () { const C = {"ps": ["TRY", "   OPENFILE \"Data.txt\" FOR READ", "   WHILE NOT EOF(\"Data.txt\")", "      READFILE \"Data.txt\", Line", "      DataArray[Index] <- STR_TO_NUM(Line)", "      Index <- Index + 1", "   ENDWHILE", "   CLOSEFILE \"Data.txt\"", "EXCEPT", "   OUTPUT \"Could not find file\"", "ENDTRY"], "py": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except IOError:", "    print(\"Could not find file\")"], "lh": 22, "vw": 190}, ST = [{"c": "The program is about to read <code>Data.txt</code>, but the user's folder has no file with that name.", "p": -1, "y": -1, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Folder", "r": ["Notes.txt", "Scores.txt"], "w": 200}]}, {"c": "The try block starts.", "p": 0, "y": 0, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Folder", "r": ["Notes.txt", "Scores.txt"], "w": 200}]}, {"c": "The open fails: there is no file called <code>Data.txt</code>. A <b>FileNotFoundError</b> is raised.", "p": 1, "y": 1, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Folder", "r": ["Notes.txt", "Scores.txt"], "w": 200, "no": [0, 1]}], "t": [[330, 10, "FileNotFoundError", "lbl bd t2"]]}, {"c": "The loop and the close are <b>skipped</b>: they are inside the try block, after the failing statement.", "p": -1, "y": -1, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Folder", "r": ["Notes.txt", "Scores.txt"], "w": 200}], "t": [[330, 10, "FileNotFoundError", "lbl bd t2"], [330, 34, "loop and close skipped", "sm"]]}, {"c": "<code>except IOError</code> matches (FileNotFoundError is an IOError), so the response runs.", "p": 8, "y": 5, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Folder", "r": ["Notes.txt", "Scores.txt"], "w": 200}], "t": [[330, 10, "FileNotFoundError", "lbl bd t2"]]}, {"c": "The user sees a meaningful message and the program carries on, instead of halting.", "p": 9, "y": 6, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Folder", "r": ["Notes.txt", "Scores.txt"], "w": 200}], "t": [[330, 10, "Could not find file", "lbl bd t3"], [330, 34, "the program carries on", "sm"]]}];
  Lib.stepper($("#stA"), { w: 760, h: 430, label: "Opening a file that does not exist", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3200, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["TRY", "   OPENFILE \"Data.txt\" FOR READ", "   WHILE NOT EOF(\"Data.txt\")", "      READFILE \"Data.txt\", Line", "      DataArray[Index] <- STR_TO_NUM(Line)", "      Index <- Index + 1", "   ENDWHILE", "   CLOSEFILE \"Data.txt\"", "EXCEPT", "   OUTPUT \"Could not find file\"", "ENDTRY"], "py": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except IOError:", "    print(\"Could not find file\")"], "lh": 22, "vw": 190}, ST = [{"c": "<code>Data.txt</code> exists. Its lines are 12, 7 and <b>abc</b>. The handler is <code>except IOError</code>.", "p": -1, "y": -1, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": null, "ok": null, "no": null, "ptr": null, "ptrLabel": "next read"}]}, {"c": "The file opens without a problem.", "p": 1, "y": 1, "v": [["Line", ""], ["DataArray", "[]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": null, "ok": null, "no": null, "ptr": 0, "ptrLabel": "next read"}]}, {"c": "Line 1 is read and <code>int(\"12\")</code> works. 12 is stored.", "p": 4, "y": 3, "v": [["Line", "12"], ["DataArray", "[12]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": 0, "ok": null, "no": null, "ptr": 1, "ptrLabel": "next read"}]}, {"c": "Line 2: 7 is stored.", "p": 4, "y": 3, "v": [["Line", "7"], ["DataArray", "[12, 7]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": 1, "ok": [0], "no": null, "ptr": 2, "ptrLabel": "next read"}]}, {"c": "Line 3: <code>int(\"abc\")</code> cannot be converted. A <b>ValueError</b> is raised.", "p": 4, "y": 3, "v": [["Line", "abc"], ["DataArray", "[12, 7]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": null, "ok": [0, 1], "no": [2], "ptr": null, "ptrLabel": "next read"}], "t": [[330, 10, "ValueError", "lbl bd t2"]]}, {"c": "Python looks for a matching except. <code>except IOError</code> does <b>not</b> match a ValueError.", "p": 8, "y": 5, "v": [["Line", "abc"], ["DataArray", "[12, 7]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": null, "ok": [0, 1], "no": [2], "ptr": null, "ptrLabel": "next read"}], "t": [[330, 10, "ValueError: no match", "lbl bd t2"]]}, {"c": "Nothing handles it, so the program <b>halts</b>, with the file still open. A bare <code>except:</code> or <code>except (IOError, ValueError):</code> would have caught it.", "p": -1, "y": -1, "v": [["Line", "abc"], ["DataArray", "[12, 7]"]], "f": [{"x": 20, "y": 0, "t": "Data.txt", "r": ["12", "7", "abc"], "w": 200, "hl": null, "ok": [0, 1], "no": [2], "ptr": null, "ptrLabel": "next read"}], "t": [[330, 10, "Program halted", "lbl bd t2"]]}];
  Lib.stepper($("#stB"), { w: 760, h: 460, label: "A bad line with except IOError", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "Two versions of the same file read. The left one puts the <code>try</code> round the <code>open</code> only.", "f": [{"x": 20, "y": 20, "t": "Try round open only", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "except IOError:", "    print(\"No file\")", "for Line in DataFile:", "    DataArray.append(int(Line))"], "w": 350}, {"x": 390, "y": 20, "t": "Try round open, loop and close", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except:", "    print(\"Problem with the file\")"], "w": 350}]}, {"c": "On the left, if the file is missing the <code>open</code> fails and is caught. Good so far.", "f": [{"x": 20, "y": 20, "t": "Try round open only", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "except IOError:", "    print(\"No file\")", "for Line in DataFile:", "    DataArray.append(int(Line))"], "w": 350, "ok": [1, 2, 3]}, {"x": 390, "y": 20, "t": "Try round open, loop and close", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except:", "    print(\"Problem with the file\")"], "w": 350}]}, {"c": "But if a line is <code>abc</code>, the failing <code>int()</code> is <b>outside</b> the try. Nothing catches it, so the program halts.", "f": [{"x": 20, "y": 20, "t": "Try round open only", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "except IOError:", "    print(\"No file\")", "for Line in DataFile:", "    DataArray.append(int(Line))"], "w": 350, "no": [5]}, {"x": 390, "y": 20, "t": "Try round open, loop and close", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except:", "    print(\"Problem with the file\")"], "w": 350}]}, {"c": "On the right the loop and the close are inside the try, so a failure at <b>any</b> stage reaches the except block.", "f": [{"x": 20, "y": 20, "t": "Try round open only", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "except IOError:", "    print(\"No file\")", "for Line in DataFile:", "    DataArray.append(int(Line))"], "w": 350}, {"x": 390, "y": 20, "t": "Try round open, loop and close", "r": ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except:", "    print(\"Problem with the file\")"], "w": 350, "ok": [1, 2, 3, 4, 5, 6]}]}];
  Lib.stepper($("#stC"), { w: 760, h: 223, label: "Where the try goes", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3600, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

(function () {
  const files = [["File with 12, 7, 30", [12, 7, 30], false], ["File missing", null, true], ["File with 12, 7, abc", [12, 7, "abc"], false]];
  const hs = ["No handling", "except IOError", "except (bare)"];
  let f = 0, h = 1;
  const paint = () => {
    $$("#fB button").forEach((b, i) => b.classList.toggle("pri", i === f)); $$("#hB button").forEach((b, i) => b.classList.toggle("pri", i === h));
    const d = files[f][1]; let out = [], arr = [], msg = "";
    const caught = (kind) => h === 2 || (h === 1 && kind === "io");
    if (d === null) { if (caught("io")) { out.push('"Could not find file"'); msg = "FileNotFoundError is an IOError, so the handler catches it and the program carries on."; } else { out.push("Program halted: FileNotFoundError"); msg = "Nothing handles the exception, so the program halts."; } }
    else {
      for (const v of d) { if (typeof v === "string") { if (caught("value")) { out.push('"Problem reading the file"'); msg = "The ValueError was caught, and the program carries on with the numbers read so far."; } else { out.push("Program halted: ValueError"); msg = h === 1 ? "except IOError does not match a ValueError, so the program halts." : "Nothing handles the exception, so the program halts."; } break; } arr.push(v); }
      if (!out.length) msg = "No exception was raised, so the handler is not used.";
    }
    $("#fO").innerHTML = lineHTML(["DataArray = " + (d === null ? "[]" : "[" + arr.join(", ") + "]"), ...out.map((o) => "Output: " + o)]);
    $("#fV").textContent = msg;
  };
  $("#fB").innerHTML = files.map((x, i) => `<button class="b" data-i="${i}">${x[0]}</button>`).join(""); $("#hB").innerHTML = hs.map((x, i) => `<button class="b" data-i="${i}">${x}</button>`).join("");
  $$("#fB button").forEach((b) => (b.onclick = () => { f = +b.dataset.i; paint(); })); $$("#hB button").forEach((b) => (b.onclick = () => { h = +b.dataset.i; paint(); })); paint();
})();
btnTable("mB", "mO", [
  ["Try only round open", "try:\n    F = open(\"Data.txt\")\nexcept IOError: ...\nfor L in F: ...", "A bad line or failed read is outside the try, so the program can still halt", "Put the loop and close inside the try"],
  ["No message", "except IOError:\n    pass", "The user is told nothing and the message mark is lost", "print(\"Could not find file\")"],
  ["Close outside", "try: ... \nexcept: ...\nF.close()", "If the open failed, F does not exist and close() raises an error", "Close inside the try, or in a finally that checks the file opened"],
  ["Wrong exception", "except IOError:  # for int(Line)", "A ValueError does not match IOError", "except: or except (IOError, ValueError):"],
  ["No conversion", "DataArray.append(Line)", "The array holds strings, not integers", "DataArray.append(int(Line))"],
  ["Wrong mode", "open(\"Data.txt\", \"w\")  # to read", "Opening to write erases the file instead of reading it", "open(\"Data.txt\", \"r\")"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Where does each part of a file read go?", buckets: [{"label": "Inside the try"}, {"label": "In the except block"}, {"label": "Outside the structure"}], items: [{"text": "Opening the file", "b": 0}, {"text": "The loop that reads each line", "b": 0}, {"text": "int(Line) to convert", "b": 0}, {"text": "Closing the file after reading", "b": 0}, {"text": "The message Could not find file", "b": 1}, {"text": "DataArray = [] before the try", "b": 2}, {"text": "The program carrying on afterwards", "b": 2}, {"text": "print(\"Problem with the file\")", "b": 1}], done: "The file work goes inside the try, the message goes in the except, and set-up lines sit before the structure." });
Lib.order($("#o1"), { prompt: "Put the steps in order for reading a file with exception handling.", items: ["Start the try block", "Open the file for reading", "Read each line and convert it", "Close the file", "If anything fails, the except block runs", "Output an appropriate message"], done: "Try, open, read and convert, close; on failure, except and message." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["FileNotFoundError", "Raised when the file to be opened does not exist"], ["IOError", "A file input or output problem; the usual except for file work"], ["ValueError", "Raised when int(Line) is given text that is not a number"], ["finally", "Runs whatever happened, so it can close the file"], ["Bare except", "Catches every exception, including a bad line"], ["Appropriate message", "A mark point: tell the user what went wrong"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A file has 25 lines. The 10th is abc and the handler is a bare except. How many numbers are in the array when the handler runs?", "a": 9, "unit": "", "tol": 0.01, "hint": "Lines 1 to 9 were converted.", "sol": "<b>9</b>."},
  {"q": "The file is missing. How many lines are read before the except block runs?", "a": 0, "unit": "", "tol": 0.01, "hint": "The open fails, so nothing is read.", "sol": "<b>0</b>."},
  {"q": "A file of 100 numbers has a blank line as line 60 and the handler is a bare except. int(\"\") fails. How many numbers are stored?", "a": 59, "unit": "", "tol": 0.01, "hint": "Lines 1 to 59.", "sol": "<b>59</b>."},
  {"q": "The handler is except IOError and line 5 is abc. How many numbers are stored when the program halts?", "a": 4, "unit": "", "tol": 0.01, "hint": "Lines 1 to 4.", "sol": "<b>4</b>."},
  {"q": "A file of 50 numbers is read with no problems. How many times does the except block run?", "a": 0, "unit": "", "tol": 0.01, "hint": "No exception is raised.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Where should the file open, loop and close be placed?", opts: ["Before the try", "Inside the try block", "Inside the except block", "After the program"], a: 1, why: "A problem at any stage is then caught." },
  { q: "What does except IOError NOT catch?", opts: ["A missing file", "A damaged file", "int(\"abc\") failing", "A disk error"], a: 2, why: "That is a ValueError." },
  { q: "What is an appropriate message?", opts: ["Nothing", "A statement telling the user what went wrong", "The array", "The file name only"], a: 1, why: "For example Could not find file." },
  { q: "Why might a file be left open after an exception?", opts: ["Python never closes files", "The close line was skipped when the exception happened", "Files close themselves", "except closes files"], a: 1, why: "A finally block closes it either way." },
  { q: "A question says use exception handling. What is lost if you do not?", opts: ["Nothing", "The marks for try and except", "The marks for the loop", "The marks for the open"], a: 1, why: "It is a mark point." },
  { q: "Which mode opens a file to read?", opts: ["\"w\"", "\"a\"", "\"r\"", "\"x\""], a: 2, why: "r is read." },
] });
Lib.cards($("#fc1"), { cards: [
  ["try round the file work", "Open, loop and close all go inside the try."],
  ["except IOError", "Catches file problems, including a missing file."],
  ["Bare except", "Catches everything, including a bad line."],
  ["Message", "Tell the user what went wrong."],
  ["finally", "Close the file whatever happened."],
  ["int(Line)", "Lines are strings: convert them."],
  ["FileNotFoundError", "The file does not exist."],
  ["ValueError", "int() was given text that is not a number."],
] });
