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

function asmVal(t) { t = t.trim(); if (t[0] === "#") return +t.slice(1); if (t[0] === "B") return parseInt(t.slice(1), 2); if (t[0] === "&") return parseInt(t.slice(1), 16); return null; }
function asmRun(prog, mem, acc, ix, maxs) {
  const keys = Object.keys(prog).map(Number).sort((a, b) => a - b); let pc = keys[0], m = Object.assign({}, mem), flag = false, rows = [];
  for (let n = 0; n < (maxs || 200); n++) {
    const ins = prog[pc], sp = ins.split(" "), op = sp[0], a = sp[1]; let nxt = keys[keys.indexOf(pc) + 1]; const imm = a ? asmVal(a) : null; let out = "";
    const rd = () => m[+a];
    if (op === "LDM") acc = imm; else if (op === "LDD") acc = rd(); else if (op === "LDI") acc = m[m[+a]]; else if (op === "LDX") acc = m[+a + ix]; else if (op === "LDR") ix = imm; else if (op === "MOV") ix = acc;
    else if (op === "STO") m[+a] = acc; else if (op === "ADD") acc += imm !== null ? imm : rd(); else if (op === "SUB") acc -= imm !== null ? imm : rd(); else if (op === "INC") { a === "IX" ? ix++ : acc++; } else if (op === "DEC") { a === "IX" ? ix-- : acc--; }
    else if (op === "CMP") flag = acc === (imm !== null ? imm : rd()); else if (op === "JPE") { if (flag) nxt = +a; } else if (op === "JPN") { if (!flag) nxt = +a; } else if (op === "JMP") nxt = +a;
    else if (op === "OUT") out = String.fromCharCode(acc); else if (op === "END") nxt = undefined;
    rows.push({ addr: pc, ins, acc, ix, mem: Object.assign({}, m), out });
    if (nxt === undefined) break; pc = nxt;
  }
  return rows;
}
(function () {
  const draw = (s) => { const k = Math.round(s.i); const mem = [[100, 101], [101, 67], [102, 104], [103, 100], [104, 68]]; const hot = { 1: [], 2: [102], 3: [103], 4: [103, 100] }[k] || []; let o = "";
    mem.forEach(([a, d], i) => { o += SV.rect(30, 20 + i * 30, 160, 26, hot.includes(a) ? (k === 4 && a === 100 ? "f3" : "f1") : "cell", { rx: 4 }) + SV.text(40, 38 + i * 30, a + "   " + d, "lbl"); });
    o += SV.text(240, 80, ["", "ACC = 103", "ACC = 104", "address 103 holds 100", "ACC = 101"][k], "lbl bd t3"); return o; };
  Lib.stepper($("#stA"), { w: 500, h: 190, label: "Addressing", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "Main memory, with data in 100 to 104.", s: { i: 0 } }, { cap: "<b>LDM #103</b>: <b>immediate</b>, the operand is the data. ACC = 103.", s: { i: 1 } }, { cap: "<b>LDD 102</b>: <b>direct</b>, the contents of address 102 are 104. ACC = 104.", s: { i: 2 } }, { cap: "<b>LDI 103</b>: <b>indirect</b>, address 103 holds 100, so use address 100.", s: { i: 3 } }, { cap: "Address 100 holds 101. ACC = <b>101</b>.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 130, 40, "cell", { rx: 6 }) + SV.text(85, 45, "LDX 100", "lbl bd", { "text-anchor": "middle" }) + SV.rect(200, 20, 100, 40, k >= 1 ? "f3" : "cell", { rx: 6 }) + SV.text(250, 45, "IX = 2", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) o += SV.rect(350, 20, 180, 40, "f1", { rx: 6 }) + SV.text(440, 45, "100 + 2 = 102", "lbl bd", { "text-anchor": "middle" }); if (k >= 3) o += SV.rect(350, 80, 180, 40, "f2", { rx: 6 }) + SV.text(440, 105, "ACC ← contents of 102", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 140, label: "Indexed addressing", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "<b>LDX 100</b>: indexed addressing.", s: { i: 0 } }, { cap: "The index register IX holds 2.", s: { i: 1 } }, { cap: "The address is the operand plus IX: <b>102</b>.", s: { i: 2 } }, { cap: "The contents of address 102 are loaded into the ACC.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const accs = [1, 1, 1, 2, 2, 2, 2]; const mem = [1, 1, 1, 1, 2, 2, 2]; let o = SV.text(20, 20, "Loop: LDD 365, CMP 366, JPE 209, INC ACC, STO 365, ...", "sm"); ["ACC", "mem 365"].forEach((n, r) => { o += SV.rect(30, 40 + r * 44, 130, 34, "cell", { rx: 6 }) + SV.text(95, 62 + r * 44, n + " = " + (r ? mem[k] : accs[k]), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); });
    o += SV.text(220, 90, ["start: ACC = 1 from LDD 365", "CMP 366: 1 ≠ 3, JPE does not jump", "go on to INC ACC", "INC ACC: ACC = 2", "STO 365: location 365 = 2", "MOV IX: IX = 2, LDX 365 uses 367", "JMP 200: the loop runs again"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 130, label: "Trace", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3, 4, 5, 6].map((i) => ({ cap: ["Memory 365 holds 1, 366 holds 3.", "CMP compares ACC (1) with 3: not equal.", "JPE is not taken: the next instruction runs.", "INC ACC adds 1.", "STO puts the ACC in 365.", "The index register becomes 2, so LDX 365 will load from 367 (the letter A).", "JMP 200 sends the program back to the start."][i], s: { i } })) });
})();

(function () {
  const M = { 100: 101, 101: 67, 102: 104, 103: 100, 104: 68 }; let mode = "LDM", opd = 103, ix = 2;
  const paint = () => { let addr = null, data, how; if (mode === "LDM") { data = opd; how = `Immediate: the operand ${opd} is the data.`; } else if (mode === "LDD") { addr = opd; data = M[addr]; how = data === undefined ? `Direct: address ${addr}.` : `Direct: address ${addr} holds ${data}.`; } else if (mode === "LDI") { const a1 = M[opd]; addr = a1; data = M[a1]; how = `Indirect: address ${opd} holds ${a1}, an address` + (data === undefined ? "." : `; address ${a1} holds ${data}.`); } else { addr = opd + ix; data = M[addr]; how = `Indexed: ${opd} + IX (${ix}) = ${addr}` + (data === undefined ? "." : `; address ${addr} holds ${data}.`); }
    $("#mV").innerHTML = `<b>${mode} ${mode === "LDM" ? "#" : ""}${opd}</b>: ` + how + (data === undefined ? " That address is not in this memory table." : ` ACC = <b>${data}</b>.`); };
  const bar = $("#mB"); ["LDM", "LDD", "LDI", "LDX"].forEach((m) => { const b = document.createElement("button"); b.textContent = m; b.onclick = () => { mode = m; bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (m === "LDM") b.className = "on"; bar.appendChild(b); });
  Lib.slider($("#mS"), { id: "m1", label: "Operand ", min: 98, max: 104, value: opd, fmt: (x) => x, onInput: (v) => { opd = v; paint(); } }); paint();
})();
(function () {
  const prog = { 200: "LDD 365", 201: "CMP 366", 202: "JPE 209", 203: "INC ACC", 204: "STO 365", 205: "MOV IX", 206: "LDX 365", 207: "OUT", 208: "JMP 200", 209: "END" }, mem0 = { 365: 1, 366: 3, 367: 65, 368: 66 };
  let rows, k;
  const reset = () => { rows = asmRun(prog, mem0, 0, 0); k = 0; paint(); };
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Instruction</th><th>ACC</th><th>365</th><th>366</th><th>367</th><th>368</th><th>IX</th><th>Output</th></tr>'; let pm = mem0, pa = null, pix = 0;
    rows.slice(0, k).forEach((r, i) => { const hl = (c) => (c ? ' style="background:var(--accent-soft);font-weight:700"' : ""); h += `<tr><td>${r.addr}</td><td>${r.ins}</td><td${hl(r.acc !== pa)}>${r.acc}</td>` + [365, 366, 367, 368].map((a) => `<td${hl(r.mem[a] !== pm[a])}>${r.mem[a]}</td>`).join("") + `<td${hl(r.ix !== pix)}>${r.ix}</td><td>${r.out}</td></tr>`; pm = r.mem; pa = r.acc; pix = r.ix; });
    $("#trT").innerHTML = h + "</table></div>" + (k >= rows.length ? '<div class="verdict">The program has finished: it outputs A then B (ASCII 65 and 66).</div>' : ""); };
  $("#tr_step").onclick = () => { if (k < rows.length) { k++; paint(); } }; $("#tr_reset").onclick = reset; reset();
})();
btnTable("wB", "wO", [
  ["LDM #5", "Immediate", "The operand is the data"],
  ["LDD 100", "Direct", "The operand is the address"],
  ["LDI 100", "Indirect", "Address of the address"],
  ["LDX 100", "Indexed", "100 plus IX"],
  ["Jump 3 instructions back", "Relative", "Offset from the current instruction"]
], ["Instruction", "Mode", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which addressing mode is it?", buckets: [{"label": "Immediate"}, {"label": "Direct"}, {"label": "Indirect"}, {"label": "Indexed"}], items: [{"text": "LDM #7", "b": 0}, {"text": "LDD 100", "b": 1}, {"text": "LDI 100", "b": 2}, {"text": "LDX 100", "b": 3}, {"text": "The operand is the data itself", "b": 0}, {"text": "The address is the operand plus the index register", "b": 3}], done: "Immediate: data. Direct: address. Indirect: address of address. Indexed: plus IX." });
Lib.classify($("#cl2"), { prompt: "With memory 100: 101, 101: 67, 102: 104, 103: 100, 104: 68 what does it load into the ACC?", buckets: [{"label": "101"}, {"label": "104"}, {"label": "68"}], items: [{"text": "LDI 103", "b": 0}, {"text": "LDD 102", "b": 1}, {"text": "LDD 104", "b": 2}, {"text": "LDI 102", "b": 2}, {"text": "LDM #101", "b": 0}, {"text": "LDD 100", "b": 0}], done: "LDI 103: 103 holds 100, 100 holds 101. LDI 102: 102 holds 104, 104 holds 68." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Immediate", "The operand is the number to use"], ["Direct", "The operand is the address of the data"], ["Indirect", "The operand is the address of the address"], ["Indexed", "Operand plus contents of IX gives the address"], ["Relative", "Offset from the current instruction address"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of LDI 103 in order.", items: ["Read the operand 103", "Read the contents of address 103", "Use that value as an address", "Read the contents of that second address", "Place the value in the ACC"], done: "Operand, contents, as address, contents, ACC." });
Lib.calc($("#c1"), { qs: [
  {"q": "IX = 2. What address does LDX 100 use?", "a": 102, "unit": "", "tol": 0.01, "hint": "100 + 2.", "sol": "<b>102</b>."},
  {"q": "Memory 50 holds 70 and 70 holds 9. What does LDI 50 put in the ACC?", "a": 9, "unit": "", "tol": 0.01, "hint": "50 → 70 → 9.", "sol": "<b>9</b>."},
  {"q": "ACC = 5 and memory 200 holds 6. What is the ACC after ADD 200?", "a": 11, "unit": "", "tol": 0.01, "hint": "5 + 6.", "sol": "<b>11</b>."},
  {"q": "ACC = 10 after LDM #10. What is ACC after INC ACC then SUB #3?", "a": 8, "unit": "", "tol": 0.01, "hint": "10 + 1 − 3.", "sol": "<b>8</b>."},
  {"q": "The ASCII code for A is 65. What is the ASCII code of the character output by OUT when ACC = 67?", "a": 67, "unit": "", "tol": 0.01, "hint": "67 outputs C.", "sol": "<b>67</b> (the character C)."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "LDM #5 uses:", opts: ["Immediate addressing", "Direct addressing", "Indirect addressing", "Indexed addressing"], a: 0, why: "Immediate." },
  { q: "LDX needs:", opts: ["The index register", "A stack", "A queue", "A label only"], a: 0, why: "IX." },
  { q: "CMP:", opts: ["Compares ACC with a value", "Loads ACC", "Jumps", "Stores"], a: 0, why: "Compares." },
  { q: "JPE jumps when:", opts: ["The compare was true", "The compare was false", "Always", "Never"], a: 0, why: "True." },
  { q: "LDI uses:", opts: ["An address stored in another location", "The number given", "The PC", "IX only"], a: 0, why: "Address of address." },
  { q: "INC IX:", opts: ["Adds 1 to the index register", "Adds 1 to ACC", "Clears IX", "Loads IX"], a: 0, why: "IX + 1." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Immediate", "Operand is the data: LDM #5."],
  ["Direct", "Operand is the address: LDD 100."],
  ["Indirect", "Address of the address: LDI 100."],
  ["Indexed", "Operand + IX: LDX 100."],
  ["Relative", "Offset from the current instruction."],
  ["CMP", "Compare only; JPE/JPN use the result."],
  ["OUT", "Outputs the ASCII character in ACC."],
  ["Trace", "One row per instruction; record changes."],
] });
