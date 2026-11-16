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
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "A new account arrives: number 16, name Fay. The file has 7 locations, two of them empty.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26}], "t": [[330, 50, "NewAccount = 16 Fay", "lbl bd"]]}, {"c": "The hash function turns the key into a location: 16 MOD 7 = <b>2</b>.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 2}], "t": [[330, 50, "NewAccount = 16 Fay", "lbl bd"], [330, 80, "Location = 16 MOD 7 = 2", "lbl bd t3"]]}, {"c": "<code>SEEK \"Accounts.dat\", 2</code> moves the file pointer to location 2.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 2, "ptr": 2, "ptrLabel": "pointer"}], "t": [[330, 50, "NewAccount = 16 Fay", "lbl bd"], [330, 80, "Location = 16 MOD 7 = 2", "lbl bd t3"]]}, {"c": "<code>GETRECORD</code> reads location 2 into <code>Current</code>. Its account number is 0, so the location is empty and safe to use.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 2, "ptr": 2, "ptrLabel": "pointer"}], "t": [[330, 50, "Current.AccountNumber = 0", "lbl bd t3"], [330, 80, "empty: store here", "sm"]]}, {"c": "<code>PUTRECORD</code> writes the new record at the pointer. No other location was touched.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "16 Fay", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "nw": 2}], "t": [[330, 50, "Stored", "lbl bd t3"]]}];
  Lib.stepper($("#stA"), { w: 760, h: 243, label: "Storing 16 at its hashed location", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["OPENFILE \"Accounts.dat\" FOR RANDOM", "Stored <- FALSE", "Location <- Hash(NewAccount.AccountNumber)", "Start <- Location", "REPEAT", "   SEEK \"Accounts.dat\", Location", "   GETRECORD \"Accounts.dat\", Current", "   IF Current.AccountNumber = 0 THEN", "      PUTRECORD \"Accounts.dat\", NewAccount", "      Stored <- TRUE", "   ELSE", "      Location <- (Location + 1) MOD 7", "   ENDIF", "UNTIL Stored OR Location = Start", "CLOSEFILE \"Accounts.dat\""], "py": ["File = open(\"Accounts.dat\", \"r+b\")", "Stored = False", "Location = Hash(NewAccount.AccountNumber)", "Start = Location", "while True:", "    File.seek(Location * RecSize)", "    Current = GetRecord(File)", "    if Current.AccountNumber == 0:", "        File.seek(Location * RecSize)", "        PutRecord(File, NewAccount)", "        Stored = True", "    else:", "        Location = (Location + 1) % 7", "    if Stored or Location == Start:", "        break", "File.close()"], "lh": 20, "vw": 170}, ST = [{"c": "The file is opened for random access. Empty locations hold account number 0.", "p": 0, "y": 0, "v": [["Location", ""], ["Start", ""], ["Current.AccountNumber", ""], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>Stored</code> starts FALSE: the record has not been written yet.", "p": 1, "y": 1, "v": [["Location", ""], ["Start", ""], ["Current.AccountNumber", ""], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "The hash function gives the first location to try: 24 MOD 7 = <b>3</b>.", "p": 2, "y": 2, "v": [["Location", "3"], ["Start", ""], ["Current.AccountNumber", ""], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 3}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>Start</code> remembers 3. If the loop ever comes back to it, every location has been tried.", "p": 3, "y": 3, "v": [["Location", "3"], ["Start", "3"], ["Current.AccountNumber", ""], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 3}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>SEEK</code> moves to location 3 and <code>GETRECORD</code> reads it. Account <b>10</b> (Ray) is stored here.", "p": 6, "y": 6, "v": [["Location", "3"], ["Start", "3"], ["Current.AccountNumber", "10"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 3, "ptr": 3, "ptrLabel": "pointer"}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "10 is not 0, so the location is taken. <b>Collision.</b> <code>Location</code> becomes (3 + 1) MOD 7 = 4. <code>UNTIL</code> is false, so the loop repeats.", "p": 11, "y": 12, "v": [["Location", "4"], ["Start", "3"], ["Current.AccountNumber", "10"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "no": [3]}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>SEEK</code> moves to location 4 and <code>GETRECORD</code> reads it. Account <b>18</b> (Cho) is stored here.", "p": 6, "y": 6, "v": [["Location", "4"], ["Start", "3"], ["Current.AccountNumber", "18"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 4, "ptr": 4, "ptrLabel": "pointer"}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "18 is not 0, so the location is taken. <b>Collision.</b> <code>Location</code> becomes (4 + 1) MOD 7 = 5. <code>UNTIL</code> is false, so the loop repeats.", "p": 11, "y": 12, "v": [["Location", "5"], ["Start", "3"], ["Current.AccountNumber", "18"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "no": [4]}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>SEEK</code> moves to location 5 and <code>GETRECORD</code> reads it. Account <b>5</b> (Dev) is stored here.", "p": 6, "y": 6, "v": [["Location", "5"], ["Start", "3"], ["Current.AccountNumber", "5"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 5, "ptr": 5, "ptrLabel": "pointer"}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "5 is not 0, so the location is taken. <b>Collision.</b> <code>Location</code> becomes (5 + 1) MOD 7 = 6. <code>UNTIL</code> is false, so the loop repeats.", "p": 11, "y": 12, "v": [["Location", "6"], ["Start", "3"], ["Current.AccountNumber", "5"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "no": [5]}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>SEEK</code> moves to location 6 and <code>GETRECORD</code> reads it. It is empty (account number 0).", "p": 6, "y": 6, "v": [["Location", "6"], ["Start", "3"], ["Current.AccountNumber", "0"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "(empty)"], "addr": true, "lh": 26, "hl": 6, "ptr": 6, "ptrLabel": "pointer"}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "The location is empty, so <code>PUTRECORD</code> writes the new record here.", "p": 8, "y": 9, "v": [["Location", "6"], ["Start", "3"], ["Current.AccountNumber", "0"], ["Stored", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "nw": 6}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>Stored</code> becomes TRUE.", "p": 9, "y": 10, "v": [["Location", "6"], ["Start", "3"], ["Current.AccountNumber", "0"], ["Stored", "TRUE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "nw": 6}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "<code>UNTIL Stored OR Location = Start</code> is true, so the loop ends.", "p": 13, "y": 13, "v": [["Location", "6"], ["Start", "3"], ["Current.AccountNumber", "0"], ["Stored", "TRUE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [6]}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}, {"c": "The file is closed. Account 24 ended up at location 6, not at its hashed location 3, because of the collisions on the way.", "p": 14, "y": 15, "v": [["Location", "6"], ["Start", "3"], ["Current.AccountNumber", "0"], ["Stored", "TRUE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [6]}], "t": [[330, 20, "NewAccount = 24 Eli", "lbl bd"]]}];
  Lib.stepper($("#stB"), { w: 760, h: 653, label: "Adding 24 with collisions", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3000, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "Every location now holds a record. A new account arrives: 8 Gus. 8 MOD 7 = 1, so <code>Start</code> is 1.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "16 Fay", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 1}], "t": [[330, 30, "NewAccount = 8 Gus", "lbl bd"], [330, 60, "Location = Start = 1", "sm"]]}, {"c": "Location 1 is taken, so the program moves to 2. Then 3, 4, 5 and 6, which are all taken too.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "16 Fay", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [1, 2, 3, 4, 5, 6]}], "t": [[330, 30, "NewAccount = 8 Gus", "lbl bd"], [330, 60, "Location goes 1, 2, 3, 4, 5, 6", "sm"]]}, {"c": "From 6, <code>(Location + 1) MOD 7</code> wraps round to <b>0</b>. The program has not run off the end of the file. Location 0 is taken as well.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "16 Fay", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [0, 1, 2, 3, 4, 5, 6]}], "t": [[330, 30, "NewAccount = 8 Gus", "lbl bd"], [330, 60, "(6 + 1) MOD 7 = 0", "sm"]]}, {"c": "<code>Location</code> becomes 1 again, which equals <code>Start</code>. <code>UNTIL Stored OR Location = Start</code> is true while <code>Stored</code> is FALSE.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "16 Fay", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 1}], "t": [[330, 30, "Location = 1 = Start", "lbl bd t2"], [330, 60, "Stored = FALSE", "lbl bd t2"]]}, {"c": "<code>IF NOT Stored</code> is true, so the program outputs <b>File full</b>. The new record is not stored and no existing record was overwritten.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "16 Fay", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26}], "t": [[330, 30, "OUTPUT \"File full\"", "lbl bd t2"]]}];
  Lib.stepper($("#stC"), { w: 760, h: 243, label: "A full file", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3600, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

(function () {
  const START = [[14, "Hall"], [22, "Ito"], null, [10, "Ray"], [18, "Cho"], [5, "Dev"], null];
  let sl = START.slice();
  const show = (trail, loc, msg) => {
    $("#aF").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location</th><th>Record</th></tr>' + sl.map((s, i) => `<tr${i === loc ? ' style="background:var(--ok-soft);font-weight:700"' : ""}><td>${i}</td><td>${s ? s[0] + " " + s[1] : "(empty)"}</td></tr>`).join("") + "</table></div>";
    $("#aT").innerHTML = trail ? '<div class="tw"><table class="t mono"><tr><th>Look at location</th><th>GETRECORD finds</th><th>Action</th></tr>' + trail.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>" : "";
    $("#aV").textContent = msg;
  };
  $("#aB").onclick = () => {
    const k = parseInt($("#aK").value, 10);
    if (isNaN(k) || k < 1) { show(null, -1, "Enter a whole number above 0."); return; }
    if (sl.some((s) => s && s[0] === k)) { show(null, -1, "Account " + k + " is already stored."); return; }
    const start = k % 7; let loc = start, trail = [], done = false, steps = 0;
    while (!done) {
      steps++;
      if (!sl[loc]) { sl[loc] = [k, "New"]; trail.push([loc, "0 (empty)", "PUTRECORD: stored"]); done = true; break; }
      const nxt = (loc + 1) % 7;
      trail.push([loc, sl[loc][0] + " " + sl[loc][1], "taken: try " + nxt]); loc = nxt;
      if (loc === start) break;
    }
    if (done) show(trail, loc, `Hash(${k}) = ${k} MOD 7 = ${start}. ` + (steps === 1 ? "No collision: stored at its own location with one GETRECORD." : `${steps - 1} collision${steps > 2 ? "s" : ""}, so the record went to location ${loc} after ${steps} GETRECORDs.`));
    else show(trail, -1, `Hash(${k}) = ${start}. Every location was checked and none was empty: the file is full, so the program outputs "File full".`);
  };
  $("#aR").onclick = () => { sl = START.slice(); show(null, -1, "File reset."); };
  show(null, -1, "Press Add.");
})();

(function () {
  let m = 5; const M = [5, 7, 11];
  const paint = () => {
    $$("#hM button").forEach((b, i) => b.classList.toggle("pri", M[i] === m));
    const keys = $("#hK").value.split(",").map((s) => parseInt(s.trim(), 10)).filter((x) => !isNaN(x));
    const by = {}; keys.forEach((k) => { const h = k % m; (by[h] = by[h] || []).push(k); });
    $("#hO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Key</th><th>Key MOD ' + m + '</th><th></th></tr>' + keys.map((k) => { const h = k % m, c = by[h].length > 1; return `<tr${c ? ' style="background:var(--warn-soft)"' : ""}><td>${k}</td><td>${h}</td><td>${c ? "collision with " + by[h].filter((x) => x !== k).join(", ") : ""}</td></tr>`; }).join("") + "</table></div>";
    const n = Object.values(by).filter((a) => a.length > 1).length;
    $("#hV").textContent = n ? `${n} location${n > 1 ? "s are" : " is"} shared by more than one key. The second key to arrive at each would have to use the next free location.` : "Every key has its own location, so there are no collisions with this set of keys.";
  };
  $("#hM").innerHTML = M.map((x) => `<button class="b" data-m="${x}">MOD ${x}</button>`).join("");
  $$("#hM button").forEach((b) => (b.onclick = () => { m = +b.dataset.m; paint(); }));
  $("#hK").oninput = paint; paint();
})();
Lib.classify($("#cl1"), { prompt: "Which part of adding a record to a random file is this?", buckets: [{"label": "Hash function"}, {"label": "Collision handling"}, {"label": "File commands"}], items: [{"text": "Location <- Key MOD 7", "b": 0}, {"text": "Turns the key into a location", "b": 0}, {"text": "Two keys give the same location", "b": 1}, {"text": "Move to the next location, wrapping round", "b": 1}, {"text": "Stop when the location is back at Start", "b": 1}, {"text": "SEEK", "b": 2}, {"text": "GETRECORD", "b": 2}, {"text": "PUTRECORD", "b": 2}], done: "Hash finds the first location. Collision handling finds a free one. SEEK, GETRECORD and PUTRECORD do the file work." });
Lib.order($("#o1"), { prompt: "Put the steps for adding a record to a random file in order.", items: ["Open the file FOR RANDOM", "Calculate the location with the hash function", "SEEK to the location", "GETRECORD to see what is there", "If it is empty, PUTRECORD the new record", "If it is taken, move to the next location and repeat", "CLOSEFILE"], done: "Open, hash, seek, read, store if empty or try the next, close." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Hash function", "Turns a key into a location"], ["Collision", "Two keys giving the same location"], ["Linear probing", "Trying the next location until a free one is found"], ["Empty location", "A record with AccountNumber 0"], ["MOD", "Wraps the location back to 0 after the last one"], ["SEEK", "Moves the pointer to a location before GETRECORD or PUTRECORD"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Hash(Key) = Key MOD 7. At which location is account 24 first tried?", "a": 3, "unit": "", "tol": 0.01, "hint": "7 × 3 = 21, so 24 − 21.", "sol": "<b>3</b>."},
  {"q": "Locations 3, 4 and 5 are taken and 6 is empty. Account 24 hashes to 3. How many GETRECORD statements run before it is stored?", "a": 4, "unit": "", "tol": 0.01, "hint": "One for each location looked at, including the empty one.", "sol": "<b>4</b> (locations 3, 4, 5, 6)."},
  {"q": "Hash is Key MOD 5. What is the hash value of 1029?", "a": 4, "unit": "", "tol": 0.01, "hint": "1029 = 5 × 205 + 4.", "sol": "<b>4</b>."},
  {"q": "Hash is Key MOD 5. What is the hash value of 7630?", "a": 0, "unit": "", "tol": 0.01, "hint": "7630 divides exactly by 5.", "sol": "<b>0</b>."},
  {"q": "A file has 7 locations and all are taken. How many locations are looked at before the program decides the file is full?", "a": 7, "unit": "", "tol": 0.01, "hint": "It goes all the way round, back to Start.", "sol": "<b>7</b>."},
  {"q": "In the Python version each record is 24 bytes. At which byte does File.seek go for location 5?", "a": 120, "unit": "", "tol": 0.01, "hint": "5 × 24.", "sol": "<b>120</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which file mode is used to store records at calculated locations?", opts: ["FOR APPEND", "FOR WRITE", "FOR RANDOM", "FOR READ"], a: 2, why: "Random access needs FOR RANDOM." },
  { q: "What must come before PUTRECORD so the record goes in the right place?", opts: ["READFILE", "EOF", "SEEK", "CLOSEFILE"], a: 2, why: "SEEK moves the pointer to the location." },
  { q: "What is a collision?", opts: ["The file is full", "Two keys hash to the same location", "A record is deleted", "The file is closed"], a: 1, why: "The location is already used by a different record." },
  { q: "Why is MOD used when moving to the next location?", opts: ["To make it faster", "To wrap round to 0 after the last location", "To sort the records", "To empty the location"], a: 1, why: "(Location + 1) MOD 7 never reaches 7." },
  { q: "How does the program know a location is empty?", opts: ["EOF is true", "The record's key is 0", "The pointer is at 0", "GETRECORD returns an error"], a: 1, why: "Blank records have AccountNumber 0." },
  { q: "What does the loop compare Location with, to detect a full file?", opts: ["MaxSize", "Start", "0", "The key"], a: 1, why: "Back at Start means every location has been tried." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Random file", "Equal-sized records at numbered locations. Jump with SEEK."],
  ["Hash function", "Key MOD 7 gives a location from 0 to 6."],
  ["Collision", "Two keys with the same hashed location."],
  ["Linear probing", "Try the next location, wrapping with MOD."],
  ["Empty location", "A blank record: AccountNumber 0."],
  ["Start", "Where the search began. Back at Start means the file is full."],
  ["SEEK then PUTRECORD", "Move first, then write at the pointer."],
  ["FOR RANDOM", "The open mode for random access."],
] });
