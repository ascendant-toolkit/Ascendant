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
  const draw = (s) => { const k = Math.round(s.i); const hz = [2.1, 4.2][k]; let o = SV.rect(20, 40, 160, 50, "cell", { rx: 8 }) + SV.text(100, 70, hz + " GHz", "lbl bd", { "text-anchor": "middle" });
    for (let i = 0; i < 20; i++) o += SV.rect(220 + i * 15, 54, 4, 22, i < (k ? 20 : 10) ? "f1" : "cell", { rx: 1 }); o += SV.text(220, 110, (k ? "about 4 billion" : "about 2 billion") + " timing signals a second", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 130, label: "Clock speed", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "At 2.1 GHz the CPU runs about 2.1 billion fetch-execute steps a second.", s: { i: 0 } }, { cap: "At 4.2 GHz it runs nearly <b>twice as many</b> cycles per second.", s: { i: 1 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 100, 46, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 50, 68, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, "CPU", true) + B(190, "Cache", k >= 1) + B(360, "RAM", k >= 2) + SV.path("M120,63 H190", "ax") + SV.path("M290,63 H360", "ax");
    o += SV.text(240, 130, ["", "cache: very fast, holds frequently used data", "slower RAM: used if the cache misses", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 480, h: 150, label: "Cache", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "The CPU needs data.", s: { i: 0 } }, { cap: "It looks in the <b>cache</b> first: fast, close to the CPU.", s: { i: 1 } }, { cap: "If it is not there, it must be fetched from <b>RAM</b>, which takes longer.", s: { i: 2 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 110, 46, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 55, 68, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, "USB device", k >= 0) + B(220, "Computer / OS", k >= 2) + SV.path("M130,63 H220", "ax", { style: k >= 1 ? "stroke:var(--accent);stroke-width:3" : "" }); o += SV.text(240, 130, ["plug in", "voltage change", "computer detects the voltage change", "the device's code is sent to the OS", "the OS finds the code in its list and loads the device driver"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 150, label: "USB", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The device is plugged in.", s: { i: 0 } }, { cap: "A <b>voltage change</b> occurs.", s: { i: 1 } }, { cap: "The computer <b>detects</b> the change.", s: { i: 2 } }, { cap: "The device's <b>code</b> is transferred to the computer.", s: { i: 3 } }, { cap: "The OS finds the code in its list of devices and loads the <b>device driver</b>.", s: { i: 4 } }] });
})();

(function () {
  let cores = 4, par = 70; const paint = () => { const f = par / 100; const sp = 1 / ((1 - f) + f / cores);
    let h = ""; for (let c = 1; c <= 16; c++) { const s = 1 / ((1 - f) + f / c); h += `<rect x="${30 + c * 22}" y="${130 - s * 7}" width="16" height="${s * 7}" fill="${c === cores ? "var(--accent)" : "var(--muted)"}" opacity="${c === cores ? 1 : 0.35}"/>`; }
    $("#cG").innerHTML = `<svg viewBox="0 0 420 150" style="width:420px;max-width:100%;display:block"><path d="M30,10 V130 H400" class="ax"/>${h}<text x="400" y="146" class="sm" text-anchor="end" style="font-size:11px">number of cores (1 to 16)</text><text x="34" y="14" class="sm" style="font-size:11px">speed-up</text></svg>`;
    $("#cV").innerHTML = `With <b>${cores}</b> cores and <b>${par}%</b> of the program able to run in parallel, the program runs about <b>${sp.toFixed(1)}</b> times faster, not ${cores} times. The part that cannot be shared (${100 - par}%) and the overheads limit the gain.`; };
  Lib.slider($("#cS1"), { id: "c1", label: "Cores ", min: 1, max: 16, value: cores, fmt: (x) => x, onInput: (v) => { cores = v; paint(); } });
  Lib.slider($("#cS2"), { id: "c2", label: "% of the program that can run in parallel ", min: 0, max: 100, value: par, fmt: (x) => x + "%", onInput: (v) => { par = v; paint(); } }); paint();
})();
(function () {
  let h = 90; const paint = () => { const avg = (h / 100) * 2 + (1 - h / 100) * 100; $("#hV").innerHTML = `A cache hit takes <b>2 ns</b> and a miss (fetch from RAM) takes <b>100 ns</b>. With a <b>${h}%</b> hit rate the average access time is <b>${avg.toFixed(1)} ns</b>. A larger cache holds more frequently used data, so the hit rate rises and the CPU waits less.`; };
  Lib.slider($("#hS"), { id: "h1", label: "Cache hit rate ", min: 0, max: 100, value: h, fmt: (x) => x + "%", onInput: (v) => { h = v; paint(); } }); paint();
})();
btnTable("pB", "pO", [
  ["Fast data to a storage drive, auto-detected", "USB", "Voltage change, code, driver"],
  ["Laptop to a modern monitor with built-in speakers, one cable", "HDMI", "Digital audio and video together"],
  ["Older projector that needs a separate sound cable", "VGA", "Analogue video only"],
  ["A VR headset needing fast data and video", "USB or HDMI", "Fast transfer; audio and video on one cable"],
  ["Needs no conversion from digital to analogue", "HDMI", "Fully digital"]
], ["Need", "Port", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which performance factor does the effect describe?", buckets: [{"label": "Clock speed"}, {"label": "Cores"}, {"label": "Cache"}, {"label": "RAM"}, {"label": "Bus width"}], items: [{"text": "More fetch-execute cycles per second", "b": 0}, {"text": "More instructions at the same time", "b": 1}, {"text": "Frequently used data held close to the CPU", "b": 2}, {"text": "Fewer fetches from secondary storage", "b": 3}, {"text": "More data moved each time", "b": 4}, {"text": "Fewer waits for data from main memory", "b": 2}], done: "Match the effect." });
Lib.classify($("#cl2"), { prompt: "Why might two cores not give twice the speed?", buckets: [{"label": "A real reason"}, {"label": "Not a reason"}], items: [{"text": "The cores must communicate with each other", "b": 0}, {"text": "Software may not use both cores", "b": 0}, {"text": "The cores always run at half speed", "b": 1}, {"text": "Memory may not keep up with the cores", "b": 0}, {"text": "Each core has a different clock", "b": 1}, {"text": "There is extra overhead sharing the work", "b": 0}], done: "Overhead, idle cores, memory." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Clock speed", "Number of fetch-execute cycles per second"], ["Cache", "Fast memory close to the CPU"], ["Data bus width", "How much data is transferred at once"], ["Address bus width", "How many memory locations can be addressed"], ["Cores", "Number of processing units working in parallel"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the USB automatic connection steps in order.", items: ["The device is plugged in", "A voltage change occurs", "The computer detects the voltage change", "The device's code is sent to the computer", "The OS finds the code and loads the device driver"], done: "Plug, voltage, detect, code, driver." });
Lib.calc($("#c1"), { qs: [
  {"q": "A CPU is upgraded from 2.1 GHz to 4.2 GHz. How many times more timing signals per second?", "a": 2, "unit": "times", "tol": 0.01, "hint": "4.2 ÷ 2.1.", "sol": "<b>2</b> times."},
  {"q": "A 3 GHz CPU needs 4 clock ticks for one fetch-execute cycle. How many cycles per second, in millions?", "a": 750, "unit": "million", "tol": 0.5, "hint": "3000 ÷ 4.", "sol": "<b>750</b> million."},
  {"q": "A monitor is 2560 × 1600 pixels. How many pixels in millions (1 d.p.)?", "a": 4.1, "unit": "million", "tol": 0.05, "hint": "2560 × 1600 = 4 096 000.", "sol": "<b>4.1</b> million."},
  {"q": "A data bus is 64 bits wide. How many bytes can be transferred at once?", "a": 8, "unit": "bytes", "tol": 0.01, "hint": "64 ÷ 8.", "sol": "<b>8</b> bytes."},
  {"q": "A cache hit takes 2 ns and a miss 100 ns. With a 90% hit rate, what is the average access time in ns (1 d.p.)?", "a": 11.8, "unit": "ns", "tol": 0.05, "hint": "0.9 × 2 + 0.1 × 100.", "sol": "<b>11.8</b> ns."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A wider data bus:", opts: ["Transfers more data at the same time", "Addresses more memory", "Raises the clock speed", "Adds cores"], a: 0, why: "More data at once." },
  { q: "Cache stores:", opts: ["Frequently used instructions and data", "The OS", "The BIOS", "Backups"], a: 0, why: "Frequently used." },
  { q: "HDMI differs from VGA because it:", opts: ["Carries digital video and audio together", "Is analogue only", "Needs a separate sound cable", "Is slower"], a: 0, why: "Digital, audio and video." },
  { q: "More RAM reduces:", opts: ["Use of slower secondary storage", "The clock speed", "The number of buses", "The ALU size"], a: 0, why: "Fewer fetches from disk." },
  { q: "USB loads a:", opts: ["Device driver", "Compiler", "Utility", "Firewall"], a: 0, why: "Driver." },
  { q: "Doubling cores does not double speed because:", opts: ["Of overheads and software limits", "The clock halves", "The bus is shorter", "Cache is bigger"], a: 0, why: "Overheads." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Clock speed", "Fetch-execute cycles per second."],
  ["Cores", "Instructions in parallel; overheads."],
  ["Cache", "Fast memory for frequently used data."],
  ["RAM", "More running programs, less disk use."],
  ["Data bus", "Wider: more data at once."],
  ["Address bus", "Wider: more locations."],
  ["USB", "Serial; auto-detected; driver."],
  ["HDMI", "Digital video and audio, one cable."],
] });
