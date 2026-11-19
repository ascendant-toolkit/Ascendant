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

const LAYERS = [["Application", "f1", "HTTP request / the message", "message"], ["Transport", "f2", "seq number, port", "segments"], ["Internet", "f3", "source and destination IP address", "packets"], ["Link", "f4", "MAC addresses, frame check", "frames"]];


(function () {
  const dev = (x, y, name, rule, k, bad) => SV.rect(x, y, 170, 70, bad ? "cell-no" : k ? "cell-ok" : "f1", { rx: 10, ...op(0.8) }) + SV.text(x + 85, y + 28, name, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 85, y + 52, rule, "sm", { "text-anchor": "middle" });
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const same = k >= 4, sent = k >= 1;
    o += dev(30, 40, "Device A", same ? "Rules: protocol X" : "Rules: made-up set 1", same, false) + dev(560, 40, "Device B", same ? "Rules: protocol X" : "Rules: made-up set 2", same, k === 2 || k === 3);
    if (sent) o += SV.line(200, 75, 560, 75, "ax", { "stroke-width": 2.5 }) + SV.arrowHead(560, 75, "r", "dot1");
    if (k === 1 || k === 4 || k === 5) o += SV.text(380, 62, "HELLO", "lbl bd", { "text-anchor": "middle" });
    if (k === 2 || k === 3) o += SV.text(380, 62, "01001000 01000101 …", "sm", { "text-anchor": "middle", style: "font-family:var(--mono)" });
    if (k === 3) o += SV.text(645, 150, "?@#% ¿", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(645, 175, "not understood", "sm", { "text-anchor": "middle" });
    if (k === 5) o += SV.text(645, 150, "HELLO", "lbl bd t3", { "text-anchor": "middle" }) + SV.text(645, 175, "understood", "sm", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 200, label: "Two devices with different rules and then the same rules", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "Two devices from different manufacturers. Each has its own idea of how data should look.", s: { i: 0 } },
    { cap: "Device A sends the word HELLO using <b>its</b> rules.", s: { i: 1 } },
    { cap: "The bits arrive intact, but Device B follows <b>different rules</b> for reading them.", s: { i: 2 } },
    { cap: "Device B cannot interpret the data. The message is <b>not understood</b>, so the devices cannot communicate.", s: { i: 3 } },
    { cap: "Now both devices follow the <b>same protocol</b>.", s: { i: 4 } },
    { cap: "Device B reads the data exactly as Device A meant it. The protocol is a <b>standard</b> that makes communication possible.", s: { i: 5 } }] });
})();

(function () {
  const rows = [["Client", "Server"]];
  const msgs = ["Request: 'send me the page'", "Acknowledge: 'request received'", "Data: the page, in the agreed format", "Check: 'did it arrive undamaged?'", "Close: 'finished'"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(110, 22, "Client", "lbl bd", { "text-anchor": "middle" }) + SV.text(650, 22, "Server", "lbl bd", { "text-anchor": "middle" });
    o += SV.line(110, 34, 110, 250, "ax", { "stroke-dasharray": "5 4" }) + SV.line(650, 34, 650, 250, "ax", { "stroke-dasharray": "5 4" });
    msgs.forEach((m, i) => {
      if (i >= k) return; const y = 62 + i * 42;
      const toRight = [true, false, false, true, true][i];
      o += (toRight ? arrow(110, y, 650, y, "r", "c1", 1) : arrow(650, y, 110, y, "l", "c3", 1)) + SV.text(380, y - 8, m, "sm", { "text-anchor": "middle", ...halo });
    });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 270, label: "Order of messages in a simple exchange", base: { i: 0 }, draw, tween: 250, dwell: 2400, steps: [
    { cap: "Before any message, the protocol has decided <b>who speaks first</b> and what the reply must look like.", s: { i: 0 } },
    { cap: "The client sends a <b>request</b> in the agreed format.", s: { i: 1 } },
    { cap: "The server <b>acknowledges</b> it, as the protocol says it must.", s: { i: 2 } },
    { cap: "The server sends the <b>data</b> in the format both ends expect.", s: { i: 3 } },
    { cap: "The client <b>checks</b> the data and reports any problem, so errors are handled in a set way.", s: { i: 4 } },
    { cap: "Either end can <b>close</b> the exchange. Every step followed a rule that both devices already knew.", s: { i: 5 } }] });
})();

(function () {
  const P = [[380, 30], [570, 90], [500, 195], [260, 195], [190, 90]], names = ["A", "B", "C", "D", "E"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    if (k <= 1) { for (let a = 0; a < 5; a++) for (let b = a + 1; b < 5; b++) o += SV.line(P[a][0], P[a][1] + 18, P[b][0], P[b][1] + 18, "c2", { "stroke-width": 2, ...op(0.55) }); }
    if (k >= 2) { P.forEach((p) => (o += SV.line(p[0], p[1] + 18, 380, 125, "c3", { "stroke-width": 2.5 }))); o += SV.rect(325, 103, 110, 44, "cell-ok", { rx: 10 }) + SV.text(380, 131, "Protocol", "lbl bd", { "text-anchor": "middle" }); }
    P.forEach((p, i) => (o += SV.circle(p[0], p[1] + 18, 20, "dot1", op(0.9)) + SV.text(p[0], p[1] + 25, names[i], "lbl bd", { "text-anchor": "middle", style: "fill:#fff" })));
    o += SV.text(30, 268, k === 0 ? "5 makers, no standard" : k === 1 ? "10 separate arrangements needed (5 × 4 ÷ 2)" : "5 makers, one shared protocol: each builds to 1 standard", "lbl bd", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 280, label: "Many private arrangements against one shared standard", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "Five manufacturers, each with its own way of communicating.", s: { i: 0 } },
    { cap: "For all five to work together, every pair needs its own arrangement: <b>10</b> links, and every new maker adds more.", s: { i: 1 } },
    { cap: "With one <b>shared protocol</b>, each maker follows the same rules once and every device can talk to every other.", s: { i: 2 } }] });
})();

(function () {
  const fmt = ["ASCII (8 bit)", "Unicode (16 bit)"], spd = ["9600 bit/s", "115200 bit/s"], err = ["Parity check", "No checking"];
  const st = { A: [0, 0, 0], B: [0, 0, 0] };
  const sel = (who, idx, opts) => `<label>${who === "A" ? "Device A" : "Device B"}: <select data-w="${who}" data-i="${idx}">${opts.map((o, j) => `<option value="${j}"${st[who][idx] === j ? " selected" : ""}>${o}</option>`).join("")}</select></label>`;
  const paint = () => {
    const bad = [0, 1, 2].filter((i) => st.A[i] !== st.B[i]), ok = bad.length === 0;
    const rules = [["Data format", fmt], ["Speed", spd], ["Error handling", err]];
    $("#lab1").innerHTML = rules.map((r, i) => `<div style="margin-bottom:8px"><b>${r[0]}</b><br>${sel("A", i, r[1])} &nbsp; ${sel("B", i, r[1])}</div>`).join("") +
      `<div class="verdict ${ok ? "ok" : "no"}">${ok ? "Every rule matches. Device B reads: HELLO. The devices communicate." : "Rules that do not match: " + bad.map((i) => rules[i][0]).join(", ") + ". Device B reads: ?@#% ¿  The data arrives but is not understood."}</div>`;
    $$("#lab1 select").forEach((s) => (s.onchange = () => { st[s.dataset.w][+s.dataset.i] = +s.value; paint(); }));
  };
  paint();
})();

(function () {
  Lib.slider($("#lab2s"), { id: "nm", label: "Number of manufacturers: ", min: 2, max: 30, value: 5, onInput: (n) => {
    const pairs = n * (n - 1) / 2;
    $("#lab2o").innerHTML = `<div class="tw"><table class="t"><tr><th>Without a standard</th><th>With one shared protocol</th></tr><tr><td><b>${pairs}</b> separate arrangements (${n} × ${n - 1} ÷ 2)</td><td><b>${n}</b> makers each follow <b>1</b> standard</td></tr></table></div><div class="verdict">A shared protocol saves ${pairs - n > 0 ? pairs - n : 0} arrangements at ${n} manufacturers.</div>`;
  } });
})();

btnTable("eB", "eO", [
  ["Data format", "How the bits are arranged and what they mean", "Text in a set layout; the same character codes", "The receiver reads nonsense"],
  ["Addressing", "How the sender names the receiver", "An address on every packet", "Data goes to the wrong place"],
  ["Order of messages", "Who sends first, what the reply is", "Request then response", "Both ends wait or both talk at once"],
  ["Speed and timing", "How fast to send, how long to wait", "Slow down if the receiver is busy", "Data is lost because the receiver cannot keep up"],
  ["Error handling", "How to spot and recover from a problem", "Ask for lost data to be sent again", "Damaged data is accepted"]
], ["Rule", "What it decides", "Example", "If devices disagree"]);
Lib.classify($("#cl1"), { prompt: "Does a protocol set this?", buckets: [{"label": "Set by a protocol"}, {"label": "Not set by a protocol"}], items: [{"text": "The format of the data", "b": 0}, {"text": "The order of the messages", "b": 0}, {"text": "The colour of the monitor", "b": 1}, {"text": "What to do if data is lost", "b": 0}, {"text": "How fast the user types", "b": 1}, {"text": "The brand of the computer", "b": 1}, {"text": "How devices are addressed", "b": 0}, {"text": "The size of the hard drive", "b": 1}], done: "A protocol sets the rules of the communication: format, order, addressing, timing and errors." });
Lib.classify($("#cl2"), { prompt: "Good reason or wrong reason for using protocols?", buckets: [{"label": "Correct reason"}, {"label": "Wrong reason"}], items: [{"text": "So devices from different manufacturers can communicate", "b": 0}, {"text": "So communication is independent of the hardware and software", "b": 0}, {"text": "To make the files smaller", "b": 1}, {"text": "Without one, devices might not understand each other's data", "b": 0}, {"text": "To make every connection faster", "b": 1}, {"text": "To set a standard set of rules", "b": 0}, {"text": "To stop all hackers", "b": 1}], done: "Protocols are about a standard that makes communication possible. They do not compress data or guarantee speed or security." });
Lib.order($("#o1"), { prompt: "Put this simple exchange in the order the protocol requires.", items: ["The client sends a request", "The server acknowledges the request", "The server sends the data", "The client checks the data for errors", "The exchange is closed"], done: "Request, acknowledge, data, check, close." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Protocol", "A standard set of rules for communication"], ["Standard", "An agreed, shared specification anyone can follow"], ["Platform", "The hardware and operating system a device runs on"], ["Manufacturer", "The company that makes a device"], ["Compatible", "Able to work together because the same rules are followed"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "4 manufacturers each need to connect to all of the others without a standard. How many separate arrangements?", "a": 6, "unit": "", "tol": 0.01, "hint": "4 × 3 ÷ 2.", "sol": "<b>6</b>."},
  {"q": "10 manufacturers, no standard. How many separate arrangements?", "a": 45, "unit": "", "tol": 0.01, "hint": "10 × 9 ÷ 2.", "sol": "<b>45</b>."},
  {"q": "20 manufacturers, no standard. How many separate arrangements?", "a": 190, "unit": "", "tol": 0.01, "hint": "20 × 19 ÷ 2.", "sol": "<b>190</b>."},
  {"q": "10 manufacturers all follow one shared protocol. How many standards does each maker build to?", "a": 1, "unit": "", "tol": 0.01, "hint": "The same one.", "sol": "<b>1</b>."},
  {"q": "A device must follow 3 rules (format, speed, error handling) and the other device matches on 2 of them. How many rules do not match?", "a": 1, "unit": "", "tol": 0.01, "hint": "3 − 2.", "sol": "<b>1</b>. One mismatch is enough to stop the data being understood."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a protocol?", opts: ["A type of cable", "A standard set of rules for communication", "A program that stores data", "A kind of network card"], a: 1, why: "A set of rules." },
  { q: "Why is a protocol essential?", opts: ["It makes data smaller", "It lets devices from different manufacturers communicate", "It stops viruses", "It makes the screen brighter"], a: 1, why: "A shared standard makes communication possible." },
  { q: "Two devices follow different protocols. What is most likely?", opts: ["Faster transfer", "The data is not understood", "The data is automatically fixed", "Nothing changes"], a: 1, why: "The receiver cannot interpret the data." },
  { q: "Which is NOT normally set by a protocol?", opts: ["Data format", "Order of messages", "Error handling", "The colour of the case"], a: 3, why: "Case colour is not communication." },
  { q: "A protocol makes communication independent of...", opts: ["the data", "the hardware and software in use", "the receiver", "the sender"], a: 1, why: "Hardware and software independence." },
  { q: "A protocol is best described as...", opts: ["a program", "a piece of hardware", "a set of rules", "an operating system"], a: 2, why: "Rules." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Protocol", "A standard set of rules for communication between devices."],
  ["Standard", "An agreed specification anyone can follow."],
  ["Why essential", "Devices from different manufacturers and platforms can communicate."],
  ["Independence", "Communication does not depend on the hardware and software used."],
  ["Without one", "The data would not be understood."],
  ["Sets", "Format, addressing, order of messages, timing, error handling."],
  ["Not a program", "Software implements the rules; the protocol is the rules."],
  ["Interoperable", "Able to work with devices from other makers."],
] });
