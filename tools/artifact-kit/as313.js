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
  const draw = (s) => { const k = Math.round(s.i); const lvl = [0, 1, 0.5, 0.15, 1][k]; let o = SV.rect(60, 40, 90, 24, "f3", { rx: 4 }) + SV.text(105, 57, "transistor", "sm", { "text-anchor": "middle" }) + SV.rect(200, 30, 50, 90, "cell", { rx: 4 }) + SV.rect(200, 120 - 90 * lvl, 50, 90 * lvl, "f1", { rx: 4 }) + SV.text(225, 140, "capacitor", "sm", { "text-anchor": "middle" }) + SV.path("M150,52 H200", "ax");
    o += SV.text(340, 60, k === 0 ? "empty cell" : k === 1 ? "charged: stores a 1" : k === 2 ? "charge leaking..." : k === 3 ? "almost lost!" : "refreshed: back to 1", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 170, label: "DRAM cell", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A DRAM cell is a transistor and a capacitor.", s: { i: 0 } }, { cap: "The capacitor is charged to store a 1.", s: { i: 1 } }, { cap: "The charge leaks away over time.", s: { i: 2 } }, { cap: "If nothing happens the 1 is lost.", s: { i: 3 } }, { cap: "A refresh circuit rewrites it before it is lost. It repeats constantly.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(150, 20, "EPROM", "lbl bd", { "text-anchor": "middle" }) + SV.text(450, 20, "EEPROM", "lbl bd", { "text-anchor": "middle" }) + SV.rect(80, 40, 140, 60, k >= 2 ? "cell" : "f3", { rx: 6 }) + SV.rect(380, 40, 140, 60, k >= 3 ? "f2" : "f3", { rx: 6 });
    if (k >= 1) o += SV.text(150, 125, "removed from the board", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.text(150, 145, "UV light erases the whole chip", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); if (k >= 3) o += SV.text(450, 125, "stays in the circuit", "sm", { "text-anchor": "middle" }) + SV.text(450, 145, "voltage erases just a byte", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 165, label: "Erasing", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Both can be programmed and reprogrammed.", s: { i: 0 } }, { cap: "<b>EPROM</b> must be taken out of the device.", s: { i: 1 } }, { cap: "UV light erases <b>everything</b> on the chip.", s: { i: 2 } }, { cap: "<b>EEPROM</b> is erased electrically <b>in situ</b>, and parts can be erased.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 50, 100, 46, k >= 1 ? "f3" : "cell", { rx: 8 }) + SV.text(70, 78, "ROM boot", "lbl bd", { "text-anchor": "middle" }) + SV.rect(250, 50, 100, 46, k >= 2 ? "f3" : "cell", { rx: 8 }) + SV.text(300, 78, "Storage", "lbl bd", { "text-anchor": "middle" }) + SV.rect(480, 50, 100, 46, k >= 3 ? "f3" : "cell", { rx: 8 }) + SV.text(530, 78, "RAM", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) o += SV.path("M120,73 H250", "ax"); if (k >= 3) o += SV.path("M350,73 H480", "ax"); o += SV.text(300, 140, ["power on", "ROM runs the start-up program", "it finds the operating system", "the OS is copied into RAM and runs", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 160, label: "Start-up", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The computer is switched on. RAM is empty.", s: { i: 0 } }, { cap: "The processor runs the <b>start-up instructions in ROM</b>.", s: { i: 1 } }, { cap: "They locate the operating system on secondary storage.", s: { i: 2 } }, { cap: "The OS is copied into <b>RAM</b> and takes over.", s: { i: 3 } }] });
})();

(function () {
  let iv = 40; const leak = 64; const paint = () => { let d = ""; for (let t = 0; t <= 200; t++) { const tt = t % iv; const q = Math.max(0, 1 - tt / leak); d += (t ? "L" : "M") + (30 + t * 1.8) + "," + (130 - q * 100) + " "; } const lost = iv > leak;
    $("#rG").innerHTML = `<svg viewBox="0 0 420 160" style="width:420px;max-width:100%;display:block"><path d="M30,20 V130 H400" class="ax"/><path d="${d}" fill="none" stroke="${lost ? "var(--bad)" : "var(--accent)"}" stroke-width="2.5"/><text x="400" y="152" class="sm" text-anchor="end" style="font-size:11px">time</text><text x="34" y="16" class="sm" style="font-size:11px">charge</text></svg>`;
    $("#rV").innerHTML = lost ? `Refreshing every <b>${iv} ms</b> is too slow: the charge leaks away (in ${leak} ms) before it is rewritten, so the <b>1 is lost</b>.` : `Refreshing every <b>${iv} ms</b> rewrites the charge before it is lost, so the data is kept. This constant refreshing is why DRAM is slower than SRAM.`; };
  Lib.slider($("#rS1"), { id: "r1", label: "Refresh interval (ms) ", min: 10, max: 120, value: iv, fmt: (x) => x, onInput: (v) => { iv = v; paint(); } }); paint();
})();
btnTable("sB", "sO", [
  ["CPU cache", "SRAM", "Fastest; no refresh; expensive"],
  ["Main memory of a PC", "DRAM", "Cheap and dense"],
  ["Printer buffer of 1 GB", "DRAM", "Speed not critical; lots of capacity"],
  ["Needs refreshing constantly", "DRAM", "Capacitor leaks"],
  ["Uses flip-flops", "SRAM", "Stays set until changed"]
], ["Use or feature", "Type", "Why"]);
btnTable("rB", "rO", [
  ["Router firmware that is updated by the maker", "EEPROM", "Rewritable in situ"],
  ["Data written at the factory and never changed", "PROM or ROM", "Once only is enough"],
  ["Chip taken out and put under UV light to erase", "EPROM", "UV and removed"],
  ["Erase one byte only", "EEPROM", "Partial erase"],
  ["BIOS that is fixed", "ROM", "Boot instructions"]
], ["Description", "Type", "Why"]);
Lib.classify($("#cl1"), { prompt: "SRAM or DRAM?", buckets: [{"label": "SRAM"}, {"label": "DRAM"}], items: [{"text": "Flip-flops", "b": 0}, {"text": "Transistor and capacitor", "b": 1}, {"text": "No refresh needed", "b": 0}, {"text": "Higher bit density per chip", "b": 1}, {"text": "Used for cache", "b": 0}, {"text": "Cheaper per bit", "b": 1}], done: "SRAM: fast and costly. DRAM: cheap and dense." });
Lib.classify($("#cl2"), { prompt: "Which statement describes EPROM and which EEPROM?", buckets: [{"label": "EPROM"}, {"label": "EEPROM"}], items: [{"text": "Erased with ultraviolet light", "b": 0}, {"text": "Erased electrically in situ", "b": 1}, {"text": "Must be removed from the circuit board", "b": 0}, {"text": "Can erase just a byte", "b": 1}, {"text": "Whole chip is erased", "b": 0}, {"text": "Firmware in a VR headset", "b": 1}], done: "UV and removal against electrical and in place." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Volatile", "Contents are lost when power is switched off"], ["Refresh", "Rewriting a DRAM capacitor's charge"], ["Flip-flop", "SRAM cell"], ["BIOS", "Start-up instructions in ROM"], ["PROM", "Can be programmed only once"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the DRAM refresh steps in order.", items: ["A capacitor is charged to store a 1", "The charge slowly leaks away", "A refresh circuit reads the value before the charge is lost", "The value is rewritten to the capacitor", "The cycle repeats constantly"], done: "Charge, leak, read, rewrite, repeat." });
Lib.calc($("#c1"), { qs: [
  {"q": "A DRAM cell has 1 transistor and 1 capacitor. How many transistors are in 8 cells (one byte)?", "a": 8, "unit": "", "tol": 0.01, "hint": "1 per cell.", "sol": "<b>8</b>."},
  {"q": "A DRAM chip must be refreshed every 64 ms. How many refreshes per second?", "a": 15.625, "unit": "", "tol": 0.01, "hint": "1000 ÷ 64.", "sol": "<b>15.625</b>."},
  {"q": "A 1 GB DRAM buffer holds 1024 MB. How many 8 MB print jobs fit?", "a": 128, "unit": "", "tol": 0.01, "hint": "1024 ÷ 8.", "sol": "<b>128</b>."},
  {"q": "A ROM holds 4 KiB. How many bytes?", "a": 4096, "unit": "bytes", "tol": 0.5, "hint": "4 × 1024.", "sol": "<b>4096</b>."},
  {"q": "A PROM can be programmed 1 time and an EEPROM thousands of times. How many times more flexible is 1000 programmes than 1?", "a": 1000, "unit": "times", "tol": 0.5, "hint": "1000 ÷ 1.", "sol": "<b>1000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which memory is volatile?", opts: ["RAM", "ROM", "PROM", "EPROM"], a: 0, why: "RAM." },
  { q: "Which uses a capacitor?", opts: ["DRAM", "SRAM", "ROM", "PROM"], a: 0, why: "DRAM." },
  { q: "Which needs UV light to erase?", opts: ["EPROM", "EEPROM", "DRAM", "SRAM"], a: 0, why: "EPROM." },
  { q: "Which is used for cache?", opts: ["SRAM", "DRAM", "PROM", "EPROM"], a: 0, why: "SRAM." },
  { q: "Which can be erased in situ?", opts: ["EEPROM", "EPROM", "PROM", "ROM"], a: 0, why: "EEPROM." },
  { q: "DRAM compared with SRAM:", opts: ["Cheaper and denser", "Faster", "No refresh", "Flip-flops"], a: 0, why: "Cheaper, denser." },
] });
Lib.cards($("#fc1"), { cards: [
  ["RAM", "Volatile; running programs and data."],
  ["ROM", "Non-volatile; boot instructions."],
  ["SRAM", "Flip-flops; fast; no refresh; cache."],
  ["DRAM", "Transistor and capacitor; refresh; cheaper."],
  ["PROM", "Programmed once."],
  ["EPROM", "UV erase; removed; whole chip."],
  ["EEPROM", "Electrical; in situ; partial."],
  ["Volatile", "Lost when power is off."],
] });
