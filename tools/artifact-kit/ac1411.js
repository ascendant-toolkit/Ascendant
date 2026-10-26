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
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const stack = (x, title, hl) => { let t = SV.text(x + 90, 20, title, "lbl bd", { "text-anchor": "middle" }); LAYERS.forEach((l, i) => (t += SV.rect(x, 30 + i * 46, 180, 40, hl === i ? "cell-warn" : l[1], { rx: 6, ...op(hl === i ? 1 : 0.6) }) + SV.text(x + 90, 55 + i * 46, l[0], "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }))); return t; };
    const hlS = k >= 1 && k <= 4 ? k - 1 : -1, hlR = k >= 6 && k <= 9 ? 9 - k : -1;
    o += stack(40, "Sender", hlS) + stack(540, "Receiver", hlR);
    o += SV.line(220, 175, 540, 175, "dash", op(k >= 5 && k <= 5 ? 1 : 0.3)) + SV.text(380, 168, k === 5 ? "frames cross the network" : "network and routers", "sm", { "text-anchor": "middle" });
    if (k >= 1 && k <= 4) o += SV.text(260, 55 + (k - 1) * 46, "◀ " + ["creates the message", "adds sequence number, port", "adds IP addresses", "makes frames, sends"][k - 1], "sm");
    if (k >= 6 && k <= 9) o += SV.text(330, 55 + (9 - k) * 46, ["receives the frames ▶", "checks the IP address ▶", "orders and checks packets ▶", "gives message to the program ▶"][k - 6], "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "A message through the TCP/IP stack", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "Two hosts, each with the same four-layer stack. A message is sent from the left to the right.", s: { i: 0 } },
    { cap: "<b>Application layer</b>: the user's program creates the message using a protocol such as HTTP.", s: { i: 1 } },
    { cap: "<b>Transport layer</b>: breaks it into packets and adds a header with a sequence number.", s: { i: 2 } },
    { cap: "<b>Internet layer</b>: adds the source and destination IP addresses.", s: { i: 3 } },
    { cap: "<b>Link layer</b>: formats the packets into frames with MAC addresses and sends them over the physical network.", s: { i: 4 } },
    { cap: "The frames travel across the network, passing through routers.", s: { i: 5 } },
    { cap: "At the receiver the <b>Link layer</b> receives the frames, the first step on the way <b>up</b>.", s: { i: 6 } },
    { cap: "The <b>Internet layer</b> checks the destination IP address and passes the packets up.", s: { i: 7 } },
    { cap: "The <b>Transport layer</b> puts the packets in order using the sequence numbers and checks for loss or errors.", s: { i: 8 } },
    { cap: "The <b>Application layer</b> gives the complete message to the program.", s: { i: 9 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "On the way down: each layer wraps what it receives", "lbl bd");
    const widths = [220, 300, 380, 460];
    for (let i = 0; i <= 3; i++) { const lv = i, v = k >= lv ? 1 : 0; if (!v) continue; const w = widths[3 - lv] + 160, x = 30 + (3 - lv) * 0; o += SV.rect(30 + lv * 22, 34 + lv * 34, 700 - lv * 44, 160 - lv * 34 - 0, LAYERS[lv][1], { rx: 8, ...op(0.32) }) + SV.text(44 + lv * 22, 52 + lv * 34, [ "Application: message", "Transport header: seq, port", "Internet header: IP addresses", "Link header: MAC addresses" ][lv], "lbl bd", { style: "font-size:13px" }); }
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "Encapsulation", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "The Application layer produces the <b>message</b> (the data).", s: { i: 0 } },
    { cap: "The Transport layer adds a <b>header</b> in front: the sequence number and port.", s: { i: 1 } },
    { cap: "The Internet layer adds its own header with the <b>source and destination IP addresses</b>.", s: { i: 2 } },
    { cap: "The Link layer adds the <b>MAC addresses</b> to make a frame. Each layer treats everything from the layer above as its data. The receiver removes the headers in the opposite order.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    LAYERS.forEach((l, i) => { o += SV.rect(240, 20 + i * 48, 280, 40, k === 1 && i === 1 ? "cell-warn" : l[1], { rx: 6, ...op(0.7) }) + SV.text(380, 46 + i * 48, l[0], "lbl bd", { "text-anchor": "middle" }); });
    if (k >= 1) { o += arrow(380, 68, 380, 108, "d", "c2", 0) ; }
    if (k === 1) o += SV.text(30, 208, "Transport talks only to Application (above) and Internet (below)", "lbl bd", { style: "font-size:14px" });
    if (k === 2) o += SV.text(30, 208, "Application never talks straight to Internet or Link", "lbl bd t2", { style: "font-size:14px" }) + SV.path("M 240 40 C 190 40 190 112 240 112", "c3", { fill: "none", "stroke-width": 2.5, "stroke-dasharray": "6 4" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 225, label: "Adjacent layers", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The four layers form a stack. Each has its own functionality.", s: { i: 0 } },
    { cap: "A layer can only accept input from the <b>next higher</b> or <b>next lower</b> layer. The Transport layer exchanges data only with the Application and Internet layers, through the interface between them.", s: { i: 1 } },
    { cap: "The Application layer cannot skip a layer and talk straight to the Link layer. Each layer relies on the one below it.", s: { i: 2 } }] });
})();

/* Lab 1 */
(function () {
  let cur = 0;
  const rows = [["Application", "GET /index.html", "The message from the program", "HTTP"], ["Transport", "[seq 1, port 80] GET /index.html", "Packets numbered and ported", "TCP"], ["Internet", "[src 192.168.1.5, dst 93.184.216.34] [seq 1, port 80] GET ...", "IP addresses added", "IP"], ["Link", "[MAC AA:01 → BB:02] [IP addresses] [seq, port] GET ...", "A frame for the local network", "Ethernet / Wi-Fi"]];
  const paint = () => {
    $$("#pB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#pO").innerHTML = rows.slice(0, cur + 1).map((r, i) => `<div class="tw"><table class="t mono"><tr><th>${r[0]} layer</th><td style="${i === cur ? "background:var(--warn-soft)" : ""}">${r[1]}</td></tr></table></div>`).join("");
    $("#pV").textContent = rows[cur][0] + " layer: " + rows[cur][2] + " (protocols: " + rows[cur][3] + ").";
  };
  $("#pB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#pB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); paint();
})();

/* Lab 2 */
(function () {
  const jobs = [["Adds the source and destination IP addresses to a packet", 2], ["Splits the data into numbered packets and re-sends lost ones", 1], ["Provides the interface a web browser uses to fetch a page", 0], ["Formats packets into frames and uses MAC addresses", 3], ["Chooses the best route for each packet", 2], ["Controls the flow of packets so the receiver is not overwhelmed", 1]];
  let cur = 0, pick = null;
  const paint = () => {
    $$("#wB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const j = jobs[cur]; $("#wO").innerHTML = `<p><b>${j[0]}</b></p><div class="btnrow">` + LAYERS.map((l, i) => `<button class="b${pick === i ? " pri" : ""}" data-i="${i}">${l[0]}</button>`).join("") + '</div><div class="verdict">' + (pick === null ? "Choose a layer." : pick === j[1] ? "Correct: the " + LAYERS[j[1]][0] + " layer." : "Not the " + LAYERS[pick][0] + " layer. It is the " + LAYERS[j[1]][0] + " layer.") + "</div>";
    $$("#wO button").forEach((b) => (b.onclick = () => { pick = +b.dataset.i; paint(); }));
  };
  $("#wB").innerHTML = jobs.map((j, i) => `<button class="b" data-i="${i}">Job ${i + 1}</button>`).join("");
  $$("#wB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Application", "Services and interface to the user; the programs that exchange data", "HTTP(S), FTP, SMTP, POP3, IMAP, BitTorrent", "The message", "Describing it as the 'physical' layer"],
  ["Transport", "End-to-end delivery: packets, sequence numbers, flow control, error recovery", "TCP, UDP", "Segments / packets", "Giving it IP addresses"],
  ["Internet", "Identifies the network and host; IP addresses; routes packets", "IP", "Packets / datagrams", "Giving it re-sending of lost packets"],
  ["Link", "Frames, MAC addresses, the next hop, the physical medium", "Ethernet, Wi-Fi", "Frames", "Calling it the 'Network' layer"]
], ["Layer", "Purpose and function", "Protocols", "Data unit", "Trap"]);
Lib.classify($("#cl1"), { prompt: "Which layer does each job belong to?", buckets: [{"label": "Application"}, {"label": "Transport"}, {"label": "Internet"}, {"label": "Link"}], items: [{"text": "Provides an interface to the user's programs", "b": 0}, {"text": "Adds a sequence number to each packet", "b": 1}, {"text": "Adds the source and destination IP address", "b": 2}, {"text": "Formats datagrams into frames", "b": 3}, {"text": "Controls the flow of packets", "b": 1}, {"text": "Routes each packet by the best route", "b": 2}, {"text": "Maps IP addresses to MAC addresses", "b": 3}, {"text": "Defines the protocols programs use to exchange data", "b": 0}], done: "Application: user. Transport: packets and sequence. Internet: IP and routing. Link: frames and MAC." });
Lib.classify($("#cl2"), { prompt: "Is the statement about a protocol or about the stack?", buckets: [{"label": "About a protocol"}, {"label": "About the stack"}], items: [{"text": "A standard set of rules for communication", "b": 0}, {"text": "Layers that can only talk to adjacent layers", "b": 1}, {"text": "Allows devices from different manufacturers to communicate", "b": 0}, {"text": "Headers are added on the way down", "b": 1}, {"text": "Makes communication independent of hardware and software", "b": 0}, {"text": "User interaction at the top, hardware access at the bottom", "b": 1}], done: "A protocol is the rules. The stack is the layered way of implementing them." });
Lib.order($("#o1"), { prompt: "Put the layers in order, from the top (nearest the user) to the bottom.", items: ["Application", "Transport", "Internet", "Link"], done: "Application, Transport, Internet, Link." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Protocol", "A set of rules for communication between devices"], ["Stack", "Layers of protocols, each with its own function"], ["Header", "Information added to data by a layer"], ["Interface", "The only point of interaction between adjacent layers"], ["Packet", "A small chunk of a message sent independently"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many layers are in the TCP/IP protocol suite as used in the exam?", "a": 4, "unit": "", "tol": 0.01, "hint": "Application, Transport, Internet, Link.", "sol": "<b>4</b>."},
  {"q": "A message goes down the stack. How many headers have been added by the time it leaves the Link layer (one for each layer below the Application layer)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Transport, Internet and Link.", "sol": "<b>3</b>."},
  {"q": "A message of 4000 bytes is split into packets of 500 bytes. How many packets?", "a": 8, "unit": "", "tol": 0.01, "hint": "4000 ÷ 500.", "sol": "<b>8</b>."},
  {"q": "How many layers can the Transport layer exchange data with directly?", "a": 2, "unit": "", "tol": 0.01, "hint": "The adjacent layers above and below.", "sol": "<b>2</b>."},
  {"q": "How many layers can the Application layer exchange data with directly?", "a": 1, "unit": "", "tol": 0.01, "hint": "It is the top: only the Transport layer below.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which layer breaks data into packets and adds sequence numbers?", opts: ["Application", "Transport", "Internet", "Link"], a: 1, why: "That is the Transport layer." },
  { q: "Which layer adds source and destination IP addresses?", opts: ["Internet", "Link", "Application", "Transport"], a: 0, why: "Internet." },
  { q: "Which is the bottom layer of the TCP/IP stack?", opts: ["Application", "Transport", "Internet", "Link"], a: 3, why: "Link." },
  { q: "Why are protocols used?", opts: ["To make computers faster", "To provide a standard so different devices can communicate", "To store data", "To encrypt data"], a: 1, why: "A standard set of rules." },
  { q: "A layer can only interact with...", opts: ["any other layer", "the adjacent layers", "the top layer", "the bottom layer"], a: 1, why: "Above and below." },
  { q: "Where does user interaction take place?", opts: ["Link layer", "Internet layer", "Application layer", "Transport layer"], a: 2, why: "At the top of the stack." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Protocol", "A standard set of rules for communication."],
  ["Application", "User services; HTTP, FTP, SMTP, POP3, IMAP, BitTorrent."],
  ["Transport", "Packets, sequence numbers, flow control, error recovery."],
  ["Internet", "IP addresses and routing."],
  ["Link", "Frames, MAC addresses, the physical medium."],
  ["Adjacent", "A layer interacts only with the layer above and below."],
  ["Sending", "Down the stack; headers added."],
  ["Receiving", "Up the stack; headers removed."],
] });
