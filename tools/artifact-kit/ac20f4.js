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
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "A customer gives account number <b>18</b>. The file has 7 locations.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26}], "t": [[330, 20, "SearchKey = 18", "lbl bd"]]}, {"c": "The hash function gives the location: 18 MOD 7 = <b>4</b>.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 4}], "t": [[330, 20, "SearchKey = 18", "lbl bd"], [330, 50, "Location = 18 MOD 7 = 4", "lbl bd t3"]]}, {"c": "<code>SEEK \"Accounts.dat\", 4</code> jumps straight to location 4. Locations 0 to 3 are not read.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 4, "ptr": 4, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 18", "lbl bd"], [330, 50, "Location = 4", "lbl bd t3"]]}, {"c": "<code>GETRECORD</code> reads the record at the pointer: 18 Cho. Its account number equals <code>SearchKey</code>, so it is the record wanted.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [4], "ptr": 4, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 18", "lbl bd"], [330, 50, "Rec = 18 Cho", "lbl bd t3"], [330, 80, "Found after 1 record read", "sm"]]}, {"c": "A serial file would have had to read from the start until it reached account 18. Here one record was read.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [4]}], "t": [[330, 20, "1 record read", "lbl bd t3"], [330, 50, "no other record was touched", "sm"]]}];
  Lib.stepper($("#stA"), { w: 760, h: 243, label: "Finding account 18 directly", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["OPENFILE \"Accounts.dat\" FOR RANDOM", "Location <- Hash(SearchKey)", "Count <- 0", "Found <- FALSE", "REPEAT", "   SEEK \"Accounts.dat\", Location", "   GETRECORD \"Accounts.dat\", Rec", "   IF Rec.AccountNumber = SearchKey THEN", "      Found <- TRUE", "   ELSE", "      Location <- (Location + 1) MOD 7", "      Count <- Count + 1", "   ENDIF", "UNTIL Found OR Rec.AccountNumber = 0 OR Count = 7", "CLOSEFILE \"Accounts.dat\""], "py": ["File = open(\"Accounts.dat\", \"rb\")", "Location = Hash(SearchKey)", "Count = 0", "Found = False", "while True:", "    File.seek(Location * RecSize)", "    Rec = GetRecord(File)", "    if Rec.AccountNumber == SearchKey:", "        Found = True", "    else:", "        Location = (Location + 1) % 7", "        Count = Count + 1", "    if Found or Rec.AccountNumber == 0 or Count == 7:", "        break", "File.close()"], "lh": 20, "vw": 170}, ST = [{"c": "The file is opened for random access.", "p": 0, "y": 0, "v": [["Location", ""], ["Count", ""], ["Rec.AccountNumber", ""], ["Found", ""]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26}], "t": [[330, 20, "SearchKey = 24", "lbl bd"]]}, {"c": "The first location to try is the hash of the key: 24 MOD 7 = <b>3</b>.", "p": 1, "y": 1, "v": [["Location", "3"], ["Count", ""], ["Rec.AccountNumber", ""], ["Found", ""]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 3}], "t": [[330, 20, "SearchKey = 24", "lbl bd"]]}, {"c": "<code>Count</code> will count the locations checked, so the search cannot go round forever. <code>Found</code> starts FALSE.", "p": 3, "y": 3, "v": [["Location", "3"], ["Count", "0"], ["Rec.AccountNumber", ""], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 3}], "t": [[330, 20, "SearchKey = 24", "lbl bd"]]}, {"c": "<code>SEEK</code> to location 3, then <code>GETRECORD</code>: it holds account <b>10</b> (Ray).", "p": 6, "y": 6, "v": [["Location", "3"], ["Count", "0"], ["Rec.AccountNumber", "10"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 3, "ptr": 3, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 1", "sm"]]}, {"c": "10 is not 24. <code>Location</code> becomes 4 and <code>Count</code> becomes 1. <code>UNTIL</code> is false, so the loop repeats.", "p": 11, "y": 11, "v": [["Location", "4"], ["Count", "1"], ["Rec.AccountNumber", "10"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [3]}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 1", "sm"]]}, {"c": "<code>SEEK</code> to location 4, then <code>GETRECORD</code>: it holds account <b>18</b> (Cho).", "p": 6, "y": 6, "v": [["Location", "4"], ["Count", "1"], ["Rec.AccountNumber", "18"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 4, "ptr": 4, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 2", "sm"]]}, {"c": "18 is not 24. <code>Location</code> becomes 5 and <code>Count</code> becomes 2. <code>UNTIL</code> is false, so the loop repeats.", "p": 11, "y": 11, "v": [["Location", "5"], ["Count", "2"], ["Rec.AccountNumber", "18"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [4]}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 2", "sm"]]}, {"c": "<code>SEEK</code> to location 5, then <code>GETRECORD</code>: it holds account <b>5</b> (Dev).", "p": 6, "y": 6, "v": [["Location", "5"], ["Count", "2"], ["Rec.AccountNumber", "5"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 5, "ptr": 5, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 3", "sm"]]}, {"c": "5 is not 24. <code>Location</code> becomes 6 and <code>Count</code> becomes 3. <code>UNTIL</code> is false, so the loop repeats.", "p": 11, "y": 11, "v": [["Location", "6"], ["Count", "3"], ["Rec.AccountNumber", "5"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [5]}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 3", "sm"]]}, {"c": "<code>SEEK</code> to location 6, then <code>GETRECORD</code>: it holds account <b>24</b> (Eli).", "p": 6, "y": 6, "v": [["Location", "6"], ["Count", "3"], ["Rec.AccountNumber", "24"], ["Found", "FALSE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 6, "ptr": 6, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 4", "sm"]]}, {"c": "24 equals 24, so <code>Found</code> becomes TRUE.", "p": 8, "y": 8, "v": [["Location", "6"], ["Count", "3"], ["Rec.AccountNumber", "24"], ["Found", "TRUE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [6]}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 4", "sm"]]}, {"c": "<code>UNTIL Found ...</code> is true, so the loop ends. Account 24 was found after <b>4</b> records were read.", "p": 13, "y": 12, "v": [["Location", "6"], ["Count", "3"], ["Rec.AccountNumber", "24"], ["Found", "TRUE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [6]}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 4", "sm"]]}, {"c": "The file is closed. The program outputs the record, or \"Not found\" if <code>Found</code> is FALSE.", "p": 14, "y": 14, "v": [["Location", "6"], ["Count", "3"], ["Rec.AccountNumber", "24"], ["Found", "TRUE"]], "f": [{"x": 20, "y": 0, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [6]}], "t": [[330, 20, "SearchKey = 24", "lbl bd"], [330, 50, "records read: 4", "sm"]]}];
  Lib.stepper($("#stB"), { w: 760, h: 633, label: "Finding 24 after a collision", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3000, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "A customer gives account number <b>9</b>. 9 MOD 7 = <b>2</b>.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 2}], "t": [[330, 20, "SearchKey = 9", "lbl bd"], [330, 50, "Location = 9 MOD 7 = 2", "lbl bd t3"]]}, {"c": "<code>SEEK</code> and <code>GETRECORD</code> read location 2. It is <b>empty</b>.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 2, "ptr": 2, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchKey = 9", "lbl bd"], [330, 50, "Rec.AccountNumber = 0", "lbl bd t2"]]}, {"c": "If account 9 had been added, it would have been stored at location 2, or earlier in the chain. Location 2 is empty, so it is not in the file. The program outputs \"Not found\" after <b>1</b> read.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [2]}], "t": [[330, 20, "OUTPUT \"Not found\"", "lbl bd t2"], [330, 50, "1 record read", "sm"]]}, {"c": "A key like 17 also hashes to 3 and has to follow the chain 3, 4, 5, 6, 0, 1 before reaching the empty location 2: 7 reads. The empty location is what stops the search.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "no": [3, 4, 5, 6, 0, 1], "hl": 2}], "t": [[330, 20, "SearchKey = 17", "lbl bd"], [330, 50, "17 MOD 7 = 3", "sm"], [330, 80, "chain: 3, 4, 5, 6, 0, 1, then 2", "sm"]]}];
  Lib.stepper($("#stC"), { w: 760, h: 243, label: "A key that is not in the file", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3600, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "The customer is known by name only: <b>Cho</b>. The hash function works on account numbers, so it cannot give a location for a name. The search starts at location 0.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26}], "t": [[330, 20, "SearchName = Cho", "lbl bd"]]}, {"c": "Location 0: <code>GETRECORD</code> reads 14 Hall. Hall is not Cho, so <code>Location</code> becomes 1.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 0, "ok": null, "no": null, "ptr": 0, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchName = Cho", "lbl bd"], [330, 50, "records read: 1", "sm"]]}, {"c": "Location 1: <code>GETRECORD</code> reads 22 Ito. Ito is not Cho, so <code>Location</code> becomes 2.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 1, "ok": null, "no": [0], "ptr": 1, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchName = Cho", "lbl bd"], [330, 50, "records read: 2", "sm"]]}, {"c": "Location 2: <code>GETRECORD</code> reads an empty record. Not Cho, so move on.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": null, "ok": null, "no": [0, 1], "ptr": 2, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchName = Cho", "lbl bd"], [330, 50, "records read: 3", "sm"]]}, {"c": "Location 3: <code>GETRECORD</code> reads 10 Ray. Ray is not Cho, so <code>Location</code> becomes 4.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": 3, "ok": null, "no": [0, 1, 2], "ptr": 3, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchName = Cho", "lbl bd"], [330, 50, "records read: 4", "sm"]]}, {"c": "Location 4: <code>GETRECORD</code> reads 18 Cho. The name matches, so <code>Found</code> is TRUE and the loop stops.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "hl": null, "ok": [4], "no": [0, 1, 2, 3], "ptr": 4, "ptrLabel": "pointer"}], "t": [[330, 20, "SearchName = Cho", "lbl bd"], [330, 50, "records read: 5", "sm"]]}, {"c": "Cho was found after <b>5</b> reads. Searching by key would have taken 1. If the name were not in the file, all 7 locations would be read before the loop ended.", "f": [{"x": 20, "y": 20, "t": "Accounts.dat", "r": ["14 Hall", "22 Ito", "(empty)", "10 Ray", "18 Cho", "5 Dev", "24 Eli"], "addr": true, "lh": 26, "ok": [4]}], "t": [[330, 20, "5 reads by name", "lbl bd t2"], [330, 50, "1 read by key", "lbl bd t3"]]}];
  Lib.stepper($("#stD"), { w: 760, h: 243, label: "Searching by name", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3000, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

const FILE = [[14, "Hall"], [22, "Ito"], null, [10, "Ray"], [18, "Cho"], [5, "Dev"], [24, "Eli"]];
(function () {
  const table = (loc) => '<div class="tw"><table class="t mono"><tr><th>Location</th>' + FILE.map((s, i) => `<td${i === loc ? ' style="background:var(--ok-soft);font-weight:700"' : ""}>${i}</td>`).join("") + "</tr><tr><th>Record</th>" + FILE.map((s) => `<td>${s ? s[0] + " " + s[1] : "(empty)"}</td>`).join("") + "</tr></table></div>";
  const find = () => {
    const k = parseInt($("#fK").value, 10);
    if (isNaN(k) || k < 1) { $("#fF").innerHTML = table(-1); $("#fT").innerHTML = ""; $("#fV").textContent = "Enter a whole number above 0."; return; }
    let loc = k % 7, count = 0, trail = [], found = -1;
    while (true) {
      const r = FILE[loc];
      if (r && r[0] === k) { trail.push([loc, r[0] + " " + r[1], "key matches: Found"]); found = loc; break; }
      if (!r) { trail.push([loc, "(empty)", "empty: not in the file"]); break; }
      trail.push([loc, r[0] + " " + r[1], "not " + k + ": try " + ((loc + 1) % 7)]); loc = (loc + 1) % 7; count++;
      if (count === 7) break;
    }
    $("#fF").innerHTML = table(found);
    $("#fT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>SEEK location</th><th>GETRECORD finds</th><th>Result</th></tr>' + trail.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>";
    $("#fV").textContent = `Hash(${k}) = ${k} MOD 7 = ${k % 7}. ` + (found >= 0 ? `Found at location ${found} after ${trail.length} record${trail.length > 1 ? "s" : ""} read.` : `Not found after ${trail.length} record${trail.length > 1 ? "s" : ""} read. ` + (count === 7 ? "Every location was tried." : "An empty location ended the search."));
  };
  $("#fB").onclick = find; $$("[data-k]").forEach((b) => (b.onclick = () => { $("#fK").value = b.dataset.k; find(); })); find();
})();

(function () {
  const names = ["Hall", "Ray", "Cho", "Eli", "Zed"];
  $("#nB").innerHTML = names.map((n, i) => `<button class="b" data-i="${i}">${n}</button>`).join("");
  const show = (i) => {
    $$("#nB button").forEach((b, k) => b.classList.toggle("pri", k === i));
    const n = names[i]; let loc = 0, rows = [], hit = -1;
    while (loc < 7) { const r = FILE[loc]; rows.push([loc, r ? r[0] + " " + r[1] : "(empty)", r && r[1] === n ? "name matches: Found" : "no match"]); if (r && r[1] === n) { hit = loc; break; } loc++; }
    $("#nT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location read</th><th>Record</th><th>Result</th></tr>' + rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>";
    const acc = hit >= 0 ? FILE[hit][0] : null;
    const viaKey = (a) => { let l = a % 7, c = 1; while (FILE[l][0] !== a) { l = (l + 1) % 7; c++; } return c; };
    $("#nV").textContent = hit >= 0 ? `${n} was found after ${rows.length} read${rows.length > 1 ? "s" : ""}. Knowing the account number (${acc}), the hash would have found it in ${viaKey(acc)} read${viaKey(acc) > 1 ? "s" : ""}.` : `${n} is not in the file. All 7 locations were read before the program could say so.`;
  };
  $$("#nB button").forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(2);
})();
Lib.classify($("#cl1"), { prompt: "Is the search done by key (using the hash) or by another field (reading every location)?", buckets: [{"label": "By key (hash)"}, {"label": "By another field (scan)"}], items: [{"text": "Location <- Hash(SearchKey)", "b": 0}, {"text": "Start at location 0 and read each location in turn", "b": 1}, {"text": "Usually one GETRECORD", "b": 0}, {"text": "May read every location in the file", "b": 1}, {"text": "Compares Rec.Name with SearchName", "b": 1}, {"text": "Compares Rec.AccountNumber with SearchKey", "b": 0}, {"text": "Needs the same hash function that stored the record", "b": 0}, {"text": "Stops when Found is TRUE or the last location has been read", "b": 1}], done: "The hash only works on the key field. Any other field has to be searched for." });
Lib.order($("#o1"), { prompt: "Put the steps for finding a record by its key in a random file in order.", items: ["Open the file FOR RANDOM", "Calculate the location with the hash function", "SEEK to the location", "GETRECORD the record there", "Compare its key with the key wanted", "If it does not match and is not empty, move on to the next location", "CLOSEFILE and output the record or Not found"], done: "Open, hash, seek, read, compare, follow the chain, close and report." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Direct access", "Reaching a record without reading the ones before it"], ["Hash function", "Turns the key into the location to look at first"], ["Empty location", "Where a search by key can stop: the record is not in the file"], ["Count", "Counts locations checked so a full file cannot loop forever"], ["Found", "A flag that becomes TRUE when the key matches"], ["Scan", "Reading each location in turn when searching by a field that is not the key"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Account 18 is stored at its hashed location (18 MOD 7). How many records are read to find it?", "a": 1, "unit": "", "tol": 0.01, "hint": "SEEK goes straight there.", "sol": "<b>1</b>."},
  {"q": "Account 24 hashes to 3 and is stored at 6, because 3, 4 and 5 were taken. How many records are read to find it?", "a": 4, "unit": "", "tol": 0.01, "hint": "Locations 3, 4, 5 and 6.", "sol": "<b>4</b>."},
  {"q": "Account 9 hashes to location 2, which is empty. How many records are read before the program concludes it is not in the file?", "a": 1, "unit": "", "tol": 0.01, "hint": "An empty location ends the search.", "sol": "<b>1</b>."},
  {"q": "A name is not in the file, which has 7 locations. How many records are read in a search by name?", "a": 7, "unit": "", "tol": 0.01, "hint": "Every location is read.", "sol": "<b>7</b>."},
  {"q": "A serial file has 500 records and the one wanted is the 350th. How many records are read to reach it?", "a": 350, "unit": "", "tol": 0.01, "hint": "From the start, one at a time.", "sol": "<b>350</b>."},
  {"q": "In the Python version each record is 24 bytes. At which byte does File.seek go to read location 6?", "a": 144, "unit": "", "tol": 0.01, "hint": "6 × 24.", "sol": "<b>144</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement must come before GETRECORD when finding a record in a random file?", opts: ["READFILE", "SEEK", "EOF", "OPENFILE FOR APPEND"], a: 1, why: "SEEK moves the pointer to the location." },
  { q: "Why compare the key of the record read with the key wanted?", opts: ["To sort the file", "The location may hold a different record because of a collision", "To close the file", "To find the end of the file"], a: 1, why: "The record at the hashed location may belong to another key." },
  { q: "What does reaching an empty location tell a search by key?", opts: ["The file is full", "The record is not in the file", "The record is at the next location", "The hash is wrong"], a: 1, why: "It would have been stored there or earlier." },
  { q: "A customer is searched for by name. Which method?", opts: ["Hash the name", "Read each location from the start until the name matches", "SEEK 0 only", "Append the name"], a: 1, why: "The hash is built from the key field only." },
  { q: "Which is the usual number of records read to find a record by key with no collisions?", opts: ["1", "Half the file", "All of the file", "The location number"], a: 0, why: "SEEK then one GETRECORD." },
  { q: "What is Count for in the search loop?", opts: ["Counting matches", "Stopping the loop after every location has been tried", "Counting bytes", "Counting empty records"], a: 1, why: "If Count reaches the number of locations, the key is not in the file." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Direct access", "Go straight to a record with SEEK."],
  ["Search by key", "Hash, SEEK, GETRECORD, compare, follow the chain."],
  ["Stop conditions", "Found, an empty location, or every location tried."],
  ["Search by name", "Read from location 0 until it matches or the end is reached."],
  ["Rec.AccountNumber = 0", "An empty location."],
  ["Found flag", "Stops a WHILE loop when the record is found."],
  ["Not found", "Always output a message if the record was not found."],
  ["SEEK first", "SEEK before every GETRECORD."],
] });
