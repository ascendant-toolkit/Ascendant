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
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "The sequential file holds four records in key order: 101, 115, 142, 160.", "f": [{"x": 20, "y": 20, "t": "Students.txt", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3]}]}, {"c": "A new record with key 130 arrives. If it is appended it goes after 160.", "f": [{"x": 20, "y": 20, "t": "Students.txt", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49", "130,Dev,64"], "no": [4]}], "t": [[300, 62, "130 comes after 160: out of order", "lbl bd t2"]]}, {"c": "The file is no longer in key order. A search that stops when it passes the key would give the wrong answer.", "f": [{"x": 20, "y": 20, "t": "Students.txt", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49", "130,Dev,64"], "no": [4]}], "t": [[300, 62, "A search for 130 stops at 142 and says it is missing", "lbl bd t2"]]}, {"c": "It belongs between 115 and 142. A text file cannot have a line pushed into the middle, so the whole file is copied into a new one with 130 in the right place.", "f": [{"x": 20, "y": 20, "t": "Students.txt", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3]}, {"x": 300, "y": 20, "t": "NewStudents.txt", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": 2}]}];
  Lib.stepper($("#stA"), { w: 760, h: 178, label: "Appending breaks the key order", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3600, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["Placed <- FALSE", "OPENFILE \"Students.txt\" FOR READ", "OPENFILE \"NewStudents.txt\" FOR WRITE", "WHILE NOT EOF(\"Students.txt\")", "   READFILE \"Students.txt\", Line", "   Key <- STR_TO_NUM(LEFT(Line, 3))", "   IF NOT Placed AND Key > NewKey THEN", "      WRITEFILE \"NewStudents.txt\", NewLine", "      Placed <- TRUE", "   ENDIF", "   WRITEFILE \"NewStudents.txt\", Line", "ENDWHILE", "IF NOT Placed THEN", "   WRITEFILE \"NewStudents.txt\", NewLine", "ENDIF", "CLOSEFILE \"Students.txt\"", "CLOSEFILE \"NewStudents.txt\"", "// delete the old file, rename the new one"], "py": ["Placed = False", "Old = open(\"Students.txt\", \"r\")", "New = open(\"NewStudents.txt\", \"w\")", "for Line in Old:", "    Key = int(Line.split(\",\")[0])", "    if not Placed and Key > NewKey:", "        New.write(NewLine)", "        Placed = True", "    New.write(Line)", "if not Placed:", "    New.write(NewLine)", "Old.close()", "New.close()", "os.replace(\"NewStudents.txt\", \"Students.txt\")"], "lh": 20, "vw": 150}, ST = [{"c": "The new record has key <b>130</b>. <code>Placed</code> starts FALSE because it has not been written yet.", "p": 0, "y": 0, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", ""], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": null, "ptr": 0, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "The old file is opened to read and the new file to write. The new file is empty.", "p": 2, "y": 2, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", ""], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": null, "ptr": 0, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "<code>READFILE</code> reads 101 and <code>Key</code> is set. 101 &gt; 130 is false, so the IF is skipped.", "p": 6, "y": 5, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", "101"], ["Line", "101,Ana,58"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 0, "ptr": 1, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "The record just read (101) is copied to the new file.", "p": 10, "y": 8, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", "101"], ["Line", "101,Ana,58"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 0, "ptr": 1, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": 0}]}, {"c": "<code>READFILE</code> reads 115 and <code>Key</code> is set. 115 &gt; 130 is false, so the IF is skipped.", "p": 6, "y": 5, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", "115"], ["Line", "115,Bo,66"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 1, "ptr": 2, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "The record just read (115) is copied to the new file.", "p": 10, "y": 8, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", "115"], ["Line", "115,Bo,66"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 1, "ptr": 2, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": 1}]}, {"c": "<code>READFILE</code> reads 142 and <code>Key</code> is set. 142 &gt; 130 is <b>true</b>: this is the first larger key.", "p": 6, "y": 5, "v": [["NewKey", "130"], ["Placed", "FALSE"], ["Key", "142"], ["Line", "142,Cy,71"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 2, "ptr": 3, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "The new record is written <b>first</b>, then <code>Placed</code> becomes TRUE. Nothing has been lost: record 142 is still to be copied.", "p": 7, "y": 6, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "142"], ["Line", "142,Cy,71"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 2, "ptr": 3, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": 2}]}, {"c": "The record just read (142) is copied to the new file.", "p": 10, "y": 8, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "142"], ["Line", "142,Cy,71"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 2, "ptr": 3, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": 3}]}, {"c": "<code>READFILE</code> reads 160 and <code>Key</code> is set. <code>Placed</code> is already TRUE, so the IF is skipped.", "p": 6, "y": 5, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "160"], ["Line", "160,Di,49"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 3, "ptr": 4, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "The record just read (160) is copied to the new file.", "p": 10, "y": 8, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "160"], ["Line", "160,Di,49"]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 3, "ptr": 4, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": 4}]}, {"c": "<code>EOF</code> is true, so the loop ends.", "p": 11, "y": 3, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "160"], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": null, "ptr": null, "ptrLabel": "next read", "eof": true}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "<code>Placed</code> is TRUE, so nothing more is written. The new record was placed inside the loop.", "p": 12, "y": 9, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "160"], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": null, "ptr": null, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "Both files are closed.", "p": 15, "y": 11, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "160"], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": null, "ptr": null, "ptrLabel": "next read", "eof": false}, {"x": 390, "y": 0, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "nw": null}]}, {"c": "The old file is deleted and the new one renamed. The file is in key order again, with one more record.", "p": 17, "y": 13, "v": [["NewKey", "130"], ["Placed", "TRUE"], ["Key", "160"], ["Line", ""]], "f": [{"x": 20, "y": 0, "t": "Students.txt (now)", "r": ["101,Ana,58", "115,Bo,66", "130,Dev,64", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3, 4]}]}];
  Lib.stepper($("#stB"), { w: 760, h: 668, label: "Inserting 130", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3000, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "The new record has key <b>100</b>. The first record read is 101, and 101 &gt; 100.", "f": [{"x": 20, "y": 20, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 0, "ptr": 1, "ptrLabel": "read"}, {"x": 390, "y": 20, "t": "NewStudents.txt (new)", "r": []}]}, {"c": "The IF is true on the very first record, so the new record is written <b>before anything else</b>. <code>Placed</code> becomes TRUE.", "f": [{"x": 20, "y": 20, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "hl": 0, "ptr": 1, "ptrLabel": "read"}, {"x": 390, "y": 20, "t": "NewStudents.txt (new)", "r": ["100,Zed,50"], "nw": 0}]}, {"c": "Record 101 and every other record are then copied in turn. The IF is never true again.", "f": [{"x": 20, "y": 20, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3]}, {"x": 390, "y": 20, "t": "NewStudents.txt (new)", "r": ["100,Zed,50", "101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "nw": 0}]}, {"c": "The new file replaces the old one. 100 is now the first record.", "f": [{"x": 20, "y": 20, "t": "Students.txt (now)", "r": ["100,Zed,50", "101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3, 4]}]}];
  Lib.stepper($("#stC"), { w: 760, h: 183, label: "Smaller than every key", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "The new record has key <b>200</b>. No record in the file has a key larger than 200.", "f": [{"x": 20, "y": 20, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ptr": 0, "ptrLabel": "read"}, {"x": 390, "y": 20, "t": "NewStudents.txt (new)", "r": []}]}, {"c": "Each record fails <code>Key &gt; NewKey</code>, so each is just copied. After the loop <code>Placed</code> is still FALSE.", "f": [{"x": 20, "y": 20, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3], "eof": true}, {"x": 390, "y": 20, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"]}]}, {"c": "<code>IF NOT Placed</code> is true, so the new record is written <b>after the loop</b>, at the end. Without this check the record would be lost.", "f": [{"x": 20, "y": 20, "t": "Students.txt (old)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"], "ok": [0, 1, 2, 3]}, {"x": 390, "y": 20, "t": "NewStudents.txt (new)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49", "200,Max,77"], "nw": 4}]}, {"c": "The new file replaces the old one. 200 is now the last record.", "f": [{"x": 20, "y": 20, "t": "Students.txt (now)", "r": ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49", "200,Max,77"], "ok": [0, 1, 2, 3, 4]}]}];
  Lib.stepper($("#stD"), { w: 760, h: 183, label: "Larger than every key", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

(function () {
  const start = [101, 115, 142, 160];
  let keys = start.slice();
  const nameOf = (k) => k + ",N" + (k % 100) + "," + (50 + (k % 40));
  const paint = (rows, newFile, msg) => {
    $("#iT").innerHTML = rows ? '<div class="tw"><table class="t mono"><tr><th>Record read</th><th>Key &gt; NewKey and not Placed?</th><th>What is written</th></tr>' + rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>" : "";
    $("#iN").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Students.txt now</th></tr>' + (newFile || keys).map((k) => `<tr><td>${nameOf(k)}</td></tr>`).join("") + "</table></div>";
    $("#iV").textContent = msg;
  };
  $("#iB").onclick = () => {
    const nk = parseInt($("#iK").value, 10);
    if (isNaN(nk) || nk < 100 || nk > 999) { paint(null, null, "Enter a 3-digit whole number (100 to 999)."); return; }
    const rows = [], out = []; let placed = false;
    keys.forEach((k) => {
      const t = !placed && k > nk;
      if (t) { out.push(nk); placed = true; }
      out.push(k);
      rows.push([nameOf(k), (placed && !t) ? "no: already Placed" : (t ? k + " &gt; " + nk + ": yes" : k + " &gt; " + nk + ": no"), t ? "new record " + nk + ", then " + k : k]);
    });
    if (!placed) { out.push(nk); rows.push(["(end of file)", "-", "IF NOT Placed: new record " + nk]); }
    const dup = keys.includes(nk);
    const reads = keys.length, writes = out.length;
    keys = out;
    paint(rows, null, `${reads} records read, ${writes} written. ` + (dup ? "That key was already in the file, so it now appears twice; a real program would check for a duplicate first." : "The file is still in key order."));
  };
  $("#iR").onclick = () => { keys = start.slice(); paint(null, null, "File reset."); };
  paint(null, null, "Press Insert.");
})();

(function () {
  const ser = [142, 101, 160, 115], seq = [101, 115, 142, 160];
  const tbl = (t, rows, hit, stop) => '<div class="tw"><table class="t mono"><tr><th>' + t + "</th></tr>" + rows.map((r, i) => `<tr><td${i === hit ? ' style="background:var(--ok-soft);font-weight:700"' : (i === stop ? ' style="background:var(--warn-soft)"' : "")}>${r}${i === hit ? " found" : (i === stop ? " too big: stop" : "")}</td></tr>`).join("") + "</table></div>";
  $("#sB").onclick = () => {
    const k = parseInt($("#sK").value, 10); if (isNaN(k)) { $("#sV").textContent = "Enter a whole number."; return; }
    let a = ser.indexOf(k), ra = a >= 0 ? a + 1 : ser.length;
    let b = seq.indexOf(k), stop = -1, rb;
    if (b >= 0) rb = b + 1; else { stop = seq.findIndex((x) => x > k); rb = stop >= 0 ? stop + 1 : seq.length; }
    $("#sS").innerHTML = tbl("Serial: records read " + ra, ser.slice(0, ra), a, -1);
    $("#sQ").innerHTML = tbl("Sequential: records read " + rb, seq.slice(0, rb), b, stop);
    $("#sV").textContent = b >= 0 ? `Both find ${k}. The sequential file needed ${rb} read${rb > 1 ? "s" : ""}; the serial file needed ${ra}.` : `${k} is not in either file. The serial file has to read all ${ra} records to be sure; the sequential file stopped after ${rb} because the key was passed.`;
  };
  $("#sB").onclick();
})();
Lib.classify($("#cl1"), { prompt: "Does the statement describe a serial file or a sequential file?", buckets: [{"label": "Serial file"}, {"label": "Sequential file"}], items: [{"text": "A new record is added by appending it", "b": 0}, {"text": "A new record is added by copying to a new file with the record in its key position", "b": 1}, {"text": "Two files are open during the update", "b": 1}, {"text": "The old file is replaced by the new one afterwards", "b": 1}, {"text": "A search can stop once it has passed the key", "b": 1}, {"text": "A search that fails must read to the end of the file", "b": 0}, {"text": "FOR APPEND is enough to store the record", "b": 0}], done: "Serial: append, and search to the end. Sequential: rebuild in key order, and search can stop early." });
Lib.order($("#o1"), { prompt: "Put the steps for adding a record to a sequential file in order.", items: ["Open the old file for reading and a new file for writing", "Read a record from the old file", "If its key is larger than the new key, and the new record is not written yet, write the new record", "Write the record that was read", "Repeat until the end of the old file", "If the new record has still not been written, write it", "Close both files and replace the old file with the new one"], done: "Open both, read, place the new record at the first larger key, copy, repeat, catch the end case, close and replace." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Placed", "A flag that records whether the new record has been written yet"], ["NewStudents.txt", "The new version of the file that the records are copied into"], ["Key > NewKey", "True at the first record that belongs after the new one"], ["IF NOT Placed after the loop", "Writes the new record when its key is the largest"], ["os.replace", "Deletes the old file and gives its name to the new file"], ["Sequential file", "Records in order of a key field"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A sequential file has keys 101, 115, 142, 160. A record with key 130 is inserted. How many records does the new file hold?", "a": 5, "unit": "", "tol": 0.01, "hint": "All four old records plus the new one.", "sol": "<b>5</b>."},
  {"q": "Same file, inserting 130. How many records are written to the new file before the new record is written?", "a": 2, "unit": "", "tol": 0.01, "hint": "101 and 115 are smaller than 130.", "sol": "<b>2</b>."},
  {"q": "Same file, inserting 100. How many records are written before the new record?", "a": 0, "unit": "", "tol": 0.01, "hint": "101 is already larger than 100.", "sol": "<b>0</b>."},
  {"q": "Same file, inserting 200. How many records are written before the new record?", "a": 4, "unit": "", "tol": 0.01, "hint": "Every old record is copied first.", "sol": "<b>4</b>."},
  {"q": "A sequential file holds 1000 records. One is inserted using the copy method. How many times does READFILE run in total?", "a": 1000, "unit": "", "tol": 0.01, "hint": "Every old record is read once, whatever its position.", "sol": "<b>1000</b>."},
  {"q": "Same file (1000 records). How many WRITEFILE statements run in total?", "a": 1001, "unit": "", "tol": 0.01, "hint": "1000 copies plus the new record.", "sol": "<b>1001</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Why is a new record not simply appended to a sequential file?", opts: ["Appending is too slow", "It would break the key order", "The file would be deleted", "Append cannot be used on text files"], a: 1, why: "A sequential file must stay in key order." },
  { q: "Which statement stops the new record being written more than once?", opts: ["EOF", "The Placed flag", "CLOSEFILE", "The new line"], a: 1, why: "Placed becomes TRUE after the first write." },
  { q: "What is needed after the loop if the new key is the largest?", opts: ["Nothing", "IF NOT Placed, write the new record", "Another loop", "SEEK"], a: 1, why: "Otherwise the record would be lost." },
  { q: "How is the file updated?", opts: ["By editing the middle of the old file", "By writing a new version and replacing the old file", "By using SEEK", "By appending then sorting in place"], a: 1, why: "Text files cannot have lines inserted, so a new version is made." },
  { q: "Which open modes are used for the old and new files?", opts: ["READ and WRITE", "WRITE and READ", "APPEND and APPEND", "RANDOM and RANDOM"], a: 0, why: "Read the old, write the new." },
  { q: "What does the key comparison in the loop look for?", opts: ["The last record", "The first record with a larger key than the new one", "A duplicate key", "An empty line"], a: 1, why: "That is where the new record belongs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Sequential file", "Records in key order."],
  ["New version", "Records are copied to a new file with the new one inserted."],
  ["Placed", "Flag: has the new record been written yet?"],
  ["Key > NewKey", "Find the first record that goes after the new one."],
  ["IF NOT Placed (after loop)", "The new key was the largest: write it at the end."],
  ["Replace", "Delete the old file and rename the new file."],
  ["Two files", "READ the old, WRITE the new."],
  ["Amend or delete", "Same copy pattern: change the record or leave it out."],
] });
