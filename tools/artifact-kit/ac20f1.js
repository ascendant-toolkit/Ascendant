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
(function () { const C = {"ps": ["Line <- NUM_TO_STR(S.StudentID) & \",\"", "Line <- Line & S.Name & \",\"", "Line <- Line & NUM_TO_STR(S.Mark)", "OPENFILE \"Students.txt\" FOR APPEND", "WRITEFILE \"Students.txt\", Line", "CLOSEFILE \"Students.txt\""], "py": ["Line = str(S.StudentID) + \",\"", "Line = Line + S.Name + \",\"", "Line = Line + str(S.Mark)", "File = open(\"Students.txt\", \"a\")", "File.write(Line + \"\\n\")", "File.close()"], "lh": 22, "vw": 150}, ST = [{"c": "The record <code>S</code> holds 104, Aria and 72. <code>Students.txt</code> already holds two records, in the order they were added.", "p": -1, "y": -1, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81"]}]}, {"c": "The first field is converted to a string and the separator added.", "p": 0, "y": 0, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", "104,"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81"]}]}, {"c": "The name and a second separator are joined on.", "p": 1, "y": 1, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", "104,Aria,"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81"]}]}, {"c": "The mark is converted and joined on. <code>Line</code> now holds the whole record as text.", "p": 2, "y": 2, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", "104,Aria,72"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81"]}]}, {"c": "<code>FOR APPEND</code> opens the file and puts the pointer at the <b>end</b>. The old records are kept.", "p": 3, "y": 3, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", "104,Aria,72"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81"], "ptr": 2, "ptrLabel": "next write goes here"}]}, {"c": "The line is written at the pointer, as a new last line.", "p": 4, "y": 4, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", "104,Aria,72"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "nw": 2}]}, {"c": "The file is closed so the data is saved. The records are in the order they arrived (118, 102, 104). That is a serial file: no sorting was done.", "p": 5, "y": 5, "v": [["S.StudentID", "104"], ["S.Name", "Aria"], ["S.Mark", "72"], ["Line", "104,Aria,72"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "ok": [2]}]}];
  Lib.stepper($("#stA"), { w: 760, h: 355, label: "Appending to a serial file", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3200, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "Four records arrive, in this order: 130, 104, 160, 118.", "f": [{"x": 20, "y": 20, "t": "Order of arrival", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]}], "t": [[260, 40, "Both files are built from these four records.", "sm"]]}, {"c": "<b>Serial:</b> each record is appended as it arrives. The file holds them in arrival order.", "f": [{"x": 20, "y": 20, "t": "Order of arrival", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]}, {"x": 260, "y": 20, "t": "Serial file", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"], "nw": 3}]}, {"c": "<b>Sequential:</b> the records are first sorted on the key field, <code>StudentID</code>, in memory.", "f": [{"x": 20, "y": 20, "t": "Order of arrival", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]}, {"x": 260, "y": 20, "t": "Serial file", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]}, {"x": 500, "y": 20, "t": "Sorted on StudentID", "r": ["104,Aria,72", "118,Ben,55", "130,Dev,64", "160,Eli,90"], "hl": 0}]}, {"c": "The sorted records are written from the start of a new file. Each key is larger than the one before.", "f": [{"x": 20, "y": 20, "t": "Order of arrival", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]}, {"x": 260, "y": 20, "t": "Serial file", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]}, {"x": 500, "y": 20, "t": "Sequential file", "r": ["104,Aria,72", "118,Ben,55", "130,Dev,64", "160,Eli,90"], "ok": [0, 1, 2, 3]}]}, {"c": "Reading from the top: the serial file gives 130 first. The sequential file gives 104 first and the keys then rise: 104, 118, 130, 160.", "f": [{"x": 260, "y": 20, "t": "Serial file", "r": ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"], "hl": 0}, {"x": 500, "y": 20, "t": "Sequential file", "r": ["104,Aria,72", "118,Ben,55", "130,Dev,64", "160,Eli,90"], "hl": 0}]}];
  Lib.stepper($("#stB"), { w: 760, h: 158, label: "Serial and sequential order", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3600, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["OPENFILE \"Students.txt\" FOR READ", "WHILE NOT EOF(\"Students.txt\")", "   READFILE \"Students.txt\", Line", "   Key <- STR_TO_NUM(LEFT(Line, 3))", "   OUTPUT Key", "ENDWHILE", "CLOSEFILE \"Students.txt\""], "py": ["File = open(\"Students.txt\", \"r\")", "for Line in File:", "    Key = int(Line.split(\",\")[0])", "    print(Key)", "File.close()"], "lh": 22, "vw": 150}, ST = [{"c": "The file is opened for reading. The pointer is at the first line.", "p": 0, "y": 0, "v": [["Line", ""], ["Key", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "ptr": 0, "ptrLabel": "next read"}]}, {"c": "Not at the end of the file, so the loop runs. <code>READFILE</code> reads line 1 into <code>Line</code> and moves the pointer on.", "p": 2, "y": 1, "v": [["Line", "118,Ben,55"], ["Key", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "hl": 0, "ptr": 1, "ptrLabel": "next read"}], "t": [[380, 14, "Output so far: none", "sm"]]}, {"c": "The first three characters are converted to a number and output: <b>118</b>.", "p": 4, "y": 3, "v": [["Line", "118,Ben,55"], ["Key", "118"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "hl": 0, "ptr": 1, "ptrLabel": "next read"}], "t": [[380, 14, "Output so far: 118", "sm"]]}, {"c": "Not at the end of the file, so the loop runs. <code>READFILE</code> reads line 2 into <code>Line</code> and moves the pointer on.", "p": 2, "y": 1, "v": [["Line", "102,Cho,81"], ["Key", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "hl": 1, "ptr": 2, "ptrLabel": "next read"}], "t": [[380, 14, "Output so far: 118", "sm"]]}, {"c": "The first three characters are converted to a number and output: <b>102</b>.", "p": 4, "y": 3, "v": [["Line", "102,Cho,81"], ["Key", "102"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "hl": 1, "ptr": 2, "ptrLabel": "next read"}], "t": [[380, 14, "Output so far: 118, 102", "sm"]]}, {"c": "Not at the end of the file, so the loop runs. <code>READFILE</code> reads line 3 into <code>Line</code> and moves the pointer on.", "p": 2, "y": 1, "v": [["Line", "104,Aria,72"], ["Key", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "hl": 2, "ptr": 3, "ptrLabel": "next read"}], "t": [[380, 14, "Output so far: 118, 102", "sm"]]}, {"c": "The first three characters are converted to a number and output: <b>104</b>.", "p": 4, "y": 3, "v": [["Line", "104,Aria,72"], ["Key", "104"]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "hl": 2, "ptr": 3, "ptrLabel": "next read"}], "t": [[380, 14, "Output so far: 118, 102, 104", "sm"]]}, {"c": "<code>EOF</code> is now true, so the loop ends. Records come back in the order they are stored.", "p": 1, "y": 1, "v": [["Line", ""], ["Key", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"], "eof": true}], "t": [[380, 14, "Output: 118, 102, 104", "sm"]]}, {"c": "The file is closed.", "p": 6, "y": 4, "v": [["Line", ""], ["Key", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt", "r": ["118,Ben,55", "102,Cho,81", "104,Aria,72"]}], "t": [[380, 14, "Output: 118, 102, 104", "sm"]]}];
  Lib.stepper($("#stC"), { w: 760, h: 397, label: "Reading records until the end of the file", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 2800, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

(function () {
  const g = (id) => $("#" + id).value;
  const paint = () => {
    const id = g("lI").trim(), nm = g("lN"), mk = g("lM").trim(), line = id + "," + nm + "," + mk;
    $("#lO").innerHTML = lineHTML([
      'Line = str(' + id + ') + "," + "' + nm + '" + "," + str(' + mk + ')', 'Line <- NUM_TO_STR(' + id + ') & "," & "' + nm + '" & "," & NUM_TO_STR(' + mk + ')', "", "Written to the file:  " + line, line.length + " characters, plus the new line"]);
    const w = [];
    if (nm.includes(",")) w.push("The name contains a comma, so the line now has " + line.split(",").length + " parts instead of 3. Reading it back would cut it in the wrong place.");
    if (!/^\d{3}$/.test(id)) w.push("StudentID is not 3 digits, so LEFT(Line, 3) would not pick out the key correctly.");
    if (!/^-?\d+$/.test(mk)) w.push("Mark is not a whole number, so int() would fail when the line is read back.");
    $("#lV").textContent = w.length ? w.join(" ") : "Three fields, two commas: this line can be cut back into its fields.";
  };
  ["lI", "lN", "lM"].forEach((i) => ($("#" + i).oninput = paint)); paint();
})();

(function () {
  const start = [118, 102];
  let ser, seq;
  const reset = () => { ser = start.slice(); seq = start.slice().sort((a, b) => a - b); paint("Starting files: 118 and 102."); };
  const tbl = (t, rows, mark) => '<div class="tw"><table class="t mono"><tr><th>' + t + "</th></tr>" + rows.map((r, i) => `<tr><td${i === mark ? ' style="background:var(--ok-soft);font-weight:700"' : ""}>${r}</td></tr>`).join("") + "</table></div>";
  const paint = (msg, ms, mq) => { $("#aS").innerHTML = tbl("Serial file (order added)", ser, ms); $("#aQ").innerHTML = tbl("Sequential file (key order)", seq, mq); $("#aV").textContent = msg; };
  $("#aB").onclick = () => {
    const k = parseInt($("#aK").value, 10); if (isNaN(k)) { $("#aV").textContent = "Enter a whole number."; return; }
    ser.push(k); let p = 0; while (p < seq.length && seq[p] < k) p++; seq.splice(p, 0, k);
    const after = seq.length - 1 - p;
    paint("Serial: " + k + " was appended to the end, nothing else moved. Sequential: " + k + " belongs at position " + (p + 1) + ", so " + (after ? after + " record" + (after > 1 ? "s" : "") + " after it must move down (the file is rewritten)." : "it goes at the end, so nothing needs to move."), ser.length - 1, p);
  };
  $("#aR").onclick = reset; reset();
})();
Lib.classify($("#cl1"), { prompt: "Which kind of file does each statement describe?", buckets: [{"label": "Serial"}, {"label": "Sequential"}, {"label": "Both"}], items: [{"text": "Records are in the order they were added", "b": 0}, {"text": "Records are in order of a key field", "b": 1}, {"text": "A new record is written with FOR APPEND", "b": 0}, {"text": "Records are sorted on the key before they are written", "b": 1}, {"text": "Each record is stored as one line of text", "b": 2}, {"text": "It is read from the start until EOF", "b": 2}, {"text": "Suits a log of transactions", "b": 0}, {"text": "Suits a payroll run that processes staff in key order", "b": 1}], done: "Serial is chronological, sequential is by key. Both are text files read from the start." });
Lib.order($("#o1"), { prompt: "Put the steps for storing one record in a serial file in order.", items: ["Put the values into a record variable", "Convert each number to a string", "Join the fields into one line with commas", "Open the file FOR APPEND", "WRITEFILE the line", "CLOSEFILE"], done: "Build the record, build the line, open for append, write, close." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Record", "A group of related fields, such as ID, name and mark"], ["Field", "One item of data inside a record"], ["Key field", "The field that identifies a record and decides the order in a sequential file"], ["Separator", "The character, such as a comma, that divides the fields in a line"], ["Serial file", "Records stored in the order they were added"], ["Sequential file", "Records stored in key field order"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A record is stored as the line 104,Aria,72. How many characters are in the line, not counting the new line?", "a": 11, "unit": "", "tol": 0.01, "hint": "3 + 1 + 4 + 1 + 2.", "sol": "<b>11</b>."},
  {"q": "A serial file holds 40 records. One more is added with FOR APPEND. How many records does it hold?", "a": 41, "unit": "", "tol": 0.01, "hint": "Append keeps the old ones.", "sol": "<b>41</b>."},
  {"q": "The same file (40 records) is opened FOR WRITE by mistake and one record is written. How many records does it hold afterwards?", "a": 1, "unit": "", "tol": 0.01, "hint": "WRITE replaces the old contents.", "sol": "<b>1</b>."},
  {"q": "Records with keys 130, 104, 160 and 118 are sorted and written to a sequential file. What is the key of the third record in the file?", "a": 130, "unit": "", "tol": 0.01, "hint": "Sorted order: 104, 118, 130, 160.", "sol": "<b>130</b>."},
  {"q": "A file holds 250 records, one per line. A loop reads until EOF. How many times does READFILE run?", "a": 250, "unit": "", "tol": 0.01, "hint": "One read for each line.", "sol": "<b>250</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which open mode adds a record to a serial file without losing the existing ones?", opts: ["READ", "WRITE", "APPEND", "RANDOM"], a: 2, why: "APPEND adds at the end and keeps the old records." },
  { q: "In a serial file the records are stored...", opts: ["In key order", "In the order they were added", "At a calculated address", "In random order of size"], a: 1, why: "Serial means chronological." },
  { q: "Why is a separator needed when a record is stored as a line?", opts: ["To make the file smaller", "So the fields can be cut apart when read back", "To sort the record", "To close the file"], a: 1, why: "Without it the fields run together." },
  { q: "What must be done to a number before it is joined to a string in a line?", opts: ["Rounded", "Converted to a string", "Sorted", "Deleted"], a: 1, why: "str() in Python, NUM_TO_STR() in pseudocode." },
  { q: "Which is needed to build a sequential file from unsorted records?", opts: ["Sort them on the key first", "Open the file FOR RANDOM", "Use SEEK", "Append them in any order"], a: 0, why: "Sequential files are in key order." },
  { q: "What does write() NOT do for you in Python?", opts: ["Write text", "Add the new line at the end of the record", "Use the open file", "Send text to the file"], a: 1, why: "Add \"\\n\" yourself." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Record", "A group of related fields."],
  ["Field", "One item inside a record."],
  ["Serial file", "Records in the order added. Append new ones."],
  ["Sequential file", "Records in key order. Sort before writing."],
  ["FOR APPEND", "Open and add to the end."],
  ["FOR WRITE", "Open and replace everything."],
  ["Separator", "A comma between fields in the line."],
  ["EOF", "True when nothing more can be read."],
] });
