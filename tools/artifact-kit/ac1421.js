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
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const nodes = [[60, 100, "Caller"], [220, 60, "Switch 1"], [380, 140, "Switch 2"], [540, 60, "Switch 3"], [700, 100, "Receiver"]];
    for (let i = 0; i < 4; i++) o += SV.line(nodes[i][0], nodes[i][1], nodes[i + 1][0], nodes[i + 1][1], k >= 1 && k <= 3 ? "c1" : "dash", { "stroke-width": k >= 1 && k <= 3 ? 5 : 2, ...op(k >= 1 && k <= 3 ? 1 : 0.5) });
    nodes.forEach((n, i) => (o += SV.rect(n[0] - 46, n[1] - 18, 92, 36, i === 0 || i === 4 ? "f2" : "f3", { rx: 8 }) + SV.text(n[0], n[1] + 5, n[2], "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })));
    if (k === 1) o += SV.text(30, 200, "1 Set up: a dedicated path is reserved BEFORE any data is sent", "lbl bd t3", { style: "font-size:14px" });
    if (k === 2) o += SV.text(30, 200, "2 Transmit: continuous stream, same route, whole bandwidth, in order", "lbl bd t3", { style: "font-size:14px" });
    if (k === 3) { for (let i = 0; i < 4; i++) o += SV.circle((nodes[i][0] + nodes[i + 1][0]) / 2, (nodes[i][1] + nodes[i + 1][1]) / 2, 7, "dot2"); o += SV.text(30, 200, "data flows along the reserved path", "lbl bd", { style: "font-size:14px" }); }
    if (k === 4) o += SV.text(30, 200, "3 Release: the circuit is closed and can be used by someone else", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 215, label: "Phases of circuit switching", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "A caller wants to speak to a receiver through three switches.", s: { i: 0 } },
    { cap: "<b>Set up</b>: before any data is sent, a dedicated circuit is established through the switches and reserved.", s: { i: 1 } },
    { cap: "<b>Transmit</b>: the voice travels as a <b>continuous stream</b> along the same route, using the whole bandwidth, and arrives in order.", s: { i: 2 } },
    { cap: "Data flows the whole time the circuit is open, even if the two people are silent.", s: { i: 3 } },
    { cap: "<b>Release</b>: when the call ends the circuit is closed.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.rect(280, 70, 200, 70, "f3", { rx: 8 }) + SV.text(380, 100, "circuit in use by", "lbl", { "text-anchor": "middle", style: "font-size:14px" }) + SV.text(380, 125, "call 1", "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
    o += SV.rect(30, 80, 170, 50, "f2", { rx: 8 }) + SV.text(115, 111, "Call 1", "lbl bd", { "text-anchor": "middle" }) + SV.line(200, 105, 280, 105, "c1", { "stroke-width": 5 });
    o += SV.rect(30, 150, 170, 50, k >= 1 ? "cell-no" : "cell", { rx: 8 }) + SV.text(115, 181, "Call 2", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M 200 175 C 240 175 250 140 280 130", "c3", { fill: "none", "stroke-width": 3, "stroke-dasharray": "6 4" }) + SV.text(500, 170, "blocked: the circuit is busy", "lbl bd t2", { style: "font-size:15px" });
    if (k >= 2) o += SV.text(500, 110, "even though call 1 is silent", "lbl", { style: "font-size:14px" }) + SV.text(500, 195, "bandwidth cannot be shared", "sm");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "A dedicated circuit cannot be shared", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "Call 1 has a dedicated circuit.", s: { i: 0 } },
    { cap: "A second call tries to use the same circuit and is <b>blocked</b>: the circuit is reserved for call 1.", s: { i: 1 } },
    { cap: "Even if call 1 goes quiet, the bandwidth <b>cannot be shared</b>: it is wasted.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const nodes = [[60, 100], [220, 60], [380, 140], [540, 60], [700, 100]];
    for (let i = 0; i < 4; i++) o += SV.line(nodes[i][0], nodes[i][1], nodes[i + 1][0], nodes[i + 1][1], i === 1 && k >= 1 ? "dash" : "c1", { "stroke-width": i === 1 && k >= 1 ? 2 : 5, ...op(i === 1 && k >= 1 ? 0.5 : 1) });
    nodes.forEach((n) => (o += SV.circle(n[0], n[1], 14, "dot1")));
    if (k >= 1) o += SV.text(300, 80, "✗ cable fault", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
    if (k >= 2) o += SV.text(30, 200, "no other route is reserved: the transmission ends and the circuit must be set up again", "lbl bd t2", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "A fault on the route", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The circuit follows one route all the way.", s: { i: 0 } },
    { cap: "A fault occurs on one link of that route.", s: { i: 1 } },
    { cap: "There is <b>no alternative route</b>: the transmission ends. The circuit has to be set up again.", s: { i: 2 } }] });
})();

/* Lab 1 */
(function () {
  let calls, n;
  const reset = () => { calls = []; n = 0; paint("Three circuits are free."); };
  const paint = (msg) => {
    $("#cS").innerHTML = '<div class="tw"><table class="t"><tr><th>Circuit 1</th><th>Circuit 2</th><th>Circuit 3</th></tr><tr>' + [0, 1, 2].map((i) => `<td style="${calls[i] ? "background:var(--warn-soft);font-weight:700" : ""}">${calls[i] ? "Call " + calls[i] + " (using the whole circuit)" : "free"}</td>`).join("") + "</tr></table></div>";
    $("#cV").textContent = msg;
  };
  $("#cN").onclick = () => { n++; if (calls.length >= 3) { paint("Call " + n + " is BLOCKED: all three circuits are busy. Dedicated circuits cannot be shared."); return; } calls.push(n); paint("Call " + n + " gets its own dedicated circuit."); };
  $("#cE").onclick = () => { if (!calls.length) return; const c = calls.shift(); paint("Call " + c + " ends and releases its circuit."); };
  $("#cR").onclick = reset; reset();
})();

/* Lab 2 */
(function () {
  let talk = 4;
  const paint = () => { $("#u1").textContent = "10 min"; $("#u2").textContent = talk + " min"; $("#u3").textContent = 10 - talk + " min (" + (100 - talk * 10) + "%)"; };
  Lib.slider($("#uS"), { id: "uss", label: "Minutes of actual talking ", min: 0, max: 10, value: talk, fmt: (x) => x + " min", onInput: (v) => { talk = v; paint(); } });
  paint();
})();

btnTable("eB", "eO", [
  ["Whole bandwidth", "Benefit", "The whole bandwidth of the circuit is available: a steady, high data rate", "Real-time communication"],
  ["Data arrives in order", "Benefit", "Everything follows the same route, so no reordering or reassembly is needed", "No delay to put data back in order"],
  ["Cannot be shared", "Drawback", "The circuit is reserved even when idle, and no other transmission can use it", "Wasted bandwidth"],
  ["Set-up time", "Drawback", "The circuit has to be established before sending starts", "A delay before the call connects"],
  ["No alternative route", "Drawback", "If the route fails, the transmission ends", "A call drops if a cable is cut"]
], ["Feature", "Benefit or drawback", "What it means", "Example"]);
Lib.classify($("#cl1"), { prompt: "Is this true of circuit switching?", buckets: [{"label": "True of circuit switching"}, {"label": "Not circuit switching"}], items: [{"text": "A dedicated circuit is set up before sending", "b": 0}, {"text": "Data is split into packets sent by different routes", "b": 1}, {"text": "All data follows the same route", "b": 0}, {"text": "Packets can arrive out of order", "b": 1}, {"text": "The whole bandwidth is reserved", "b": 0}, {"text": "Data arrives in the order it was sent", "b": 0}], done: "Dedicated, same route, in order: circuit switching. Packets and different routes: packet switching." });
Lib.classify($("#cl2"), { prompt: "Is it a benefit or a drawback of circuit switching?", buckets: [{"label": "Benefit"}, {"label": "Drawback"}], items: [{"text": "The whole bandwidth is available", "b": 0}, {"text": "The circuit cannot be used by others when idle", "b": 1}, {"text": "Data arrives in order", "b": 0}, {"text": "It takes time to set up", "b": 1}, {"text": "Suitable for real-time transmission", "b": 0}, {"text": "No alternative route if a fault occurs", "b": 1}], done: "Benefits: bandwidth, order, real time. Drawbacks: not shared, set-up, no alternative route." });
Lib.order($("#o1"), { prompt: "Put the phases of circuit switching in order.", items: ["A dedicated circuit is established between the two ends", "Data is transmitted as a continuous stream along the same route", "The communication ends", "The circuit is released for others to use"], done: "Establish, transmit, end, release." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Circuit switching", "A dedicated path reserved for the whole communication"], ["Dedicated circuit", "A path used by one communication only"], ["Continuous stream", "Data sent steadily along one route"], ["Real-time", "Data must arrive as it is sent, with no delay"], ["Release", "Closing the circuit at the end"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A network has 4 circuits and each call takes one whole circuit. How many calls can be in progress at once?", "a": 4, "unit": "", "tol": 0.01, "hint": "One call per circuit.", "sol": "<b>4</b>."},
  {"q": "5 calls are started on a network with 4 circuits. How many are blocked?", "a": 1, "unit": "", "tol": 0.01, "hint": "5 − 4.", "sol": "<b>1</b>."},
  {"q": "A call lasts 20 minutes and the people talk for 12 minutes. For how many minutes is the circuit idle but still reserved?", "a": 8, "unit": "min", "tol": 0.01, "hint": "20 − 12.", "sol": "<b>8</b> minutes."},
  {"q": "A circuit takes 2 seconds to set up and the data takes 8 seconds to send. What is the total time?", "a": 10, "unit": "s", "tol": 0.01, "hint": "Set-up plus transfer.", "sol": "<b>10</b> seconds."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "When is the circuit set up?", opts: ["After the data is sent", "Before any data is sent", "Packet by packet", "Never"], a: 1, why: "Before transmission starts." },
  { q: "Which is a benefit of circuit switching?", opts: ["Bandwidth can be shared", "Data arrives in order", "No set-up time", "Alternative routes"], a: 1, why: "All data follows the same route." },
  { q: "Which is a drawback?", opts: ["The data is reordered", "The circuit cannot be used by others while open", "Packets are lost", "It needs headers"], a: 1, why: "It cannot be shared." },
  { q: "Which is a suitable use?", opts: ["Sending email", "A voice call", "Downloading a web page in pieces", "Sending a large file by many routes"], a: 1, why: "A call needs a dedicated path." },
  { q: "What happens if the route fails?", opts: ["The data takes another route", "The transmission ends", "Packets are resent", "Nothing"], a: 1, why: "There is no alternative route." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Circuit switching", "Dedicated circuit set up before sending, kept for the whole transmission."],
  ["Route", "The same route for all the data."],
  ["Bandwidth", "The whole bandwidth is reserved."],
  ["Benefit", "Steady rate, in order, real time."],
  ["Drawback", "Cannot be shared; set-up time; no alternative route."],
  ["Use", "Voice calls, live video, private networks."],
  ["Order", "Data arrives in the order sent."],
  ["Not", "Not split into packets."],
] });
