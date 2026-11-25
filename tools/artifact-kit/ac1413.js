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

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "Sender", "lbl bd") + SV.text(560, 22, "Receiver", "lbl bd");
    const order = [1, 2, 3, 4], arrive = [3, 1, 4, 2];
    if (k >= 0) order.forEach((n, i) => { o += SV.rect(30 + i * 60, 34, 50, 38, "f2", { rx: 6, ...op(k >= 1 ? 0.9 : 0.5) }) + SV.text(55 + i * 60, 58, k >= 1 ? "#" + n : "", "lbl bd", { "text-anchor": "middle" }); });
    if (k === 0) o += SV.rect(30, 34, 230, 38, "f2", { rx: 6, ...op(0.7) }) + SV.text(145, 58, "message", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) arrive.forEach((n, i) => { const lost = n === 4 && k === 3; if (k >= 4 && n === 4 && k < 5) return; o += SV.rect(330 + i * 60, 120, 50, 38, lost ? "cell-no" : "f3", { rx: 6, ...op(lost ? 0.5 : 0.9) }) + SV.text(355 + i * 60, 144, lost ? "✗" : "#" + n, "lbl bd", { "text-anchor": "middle" }); });
    if (k >= 2) o += SV.line(270, 55, 320, 135, "dash", op(0.6));
    if (k >= 5) o = SV.text(30, 22, "Sender", "lbl bd") + SV.text(560, 22, "Receiver", "lbl bd") + order.map((n, i) => SV.rect(30 + i * 60, 34, 50, 38, "f2", { rx: 6, ...op(0.5) }) + SV.text(55 + i * 60, 58, "#" + n, "lbl bd", { "text-anchor": "middle" })).join("") + order.map((n, i) => SV.rect(330 + i * 60, 120, 50, 38, "cell-ok", { rx: 6 }) + SV.text(355 + i * 60, 144, "#" + n, "lbl bd", { "text-anchor": "middle" })).join("") + SV.text(330, 190, "Put in order using the sequence numbers", "sm");
    if (k === 3) o += SV.text(330, 190, "Packet #4 is lost on the way", "lbl bd t2", { style: "font-size:14px" });
    if (k === 4) o += SV.text(330, 190, "Receiver notices #4 is missing and asks for it again", "lbl bd t4", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stT"), { w: 760, h: 205, label: "Transport layer: packets, sequence numbers, re-sending", base: { i: 0 }, draw, tween: 250, dwell: 2700, steps: [
    { cap: "The Transport layer receives the message from the Application layer.", s: { i: 0 } },
    { cap: "It <b>breaks the message into packets</b> and adds a <b>sequence number</b> to each header.", s: { i: 1 } },
    { cap: "The packets are sent. They may take different routes and <b>arrive out of order</b>.", s: { i: 2 } },
    { cap: "One packet is <b>lost</b> on the way.", s: { i: 3 } },
    { cap: "The destination's Transport layer sees a gap in the sequence numbers and <b>asks for that packet to be sent again</b>.", s: { i: 4 } },
    { cap: "With every packet present, the sequence numbers let the layer <b>reassemble the message in the right order</b> and pass it up.", s: { i: 5 } }] });
})();

(function () {
  const N = [["Laptop", 40, "192.168.1.5"], ["Home router", 230, ""], ["ISP router", 420, ""], ["Web server", 610, "93.184.216.34"]];
  const MAC = [["AA:01", "BB:02"], ["BB:03", "CC:04"], ["CC:05", "DD:06"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    N.forEach((n, i) => { o += SV.rect(n[1], 60, 110, 46, i === 0 || i === 3 ? "f1" : "f3", { rx: 8, ...op(0.8) }) + SV.text(n[1] + 55, 88, n[0], "lbl bd", { "text-anchor": "middle" }); if (i < 3) o += SV.line(n[1] + 110, 83, N[i + 1][1], 83, "ax", { "stroke-width": 2 }); });
    o += SV.text(30, 30, "Internet layer (IP): source 192.168.1.5  →  destination 93.184.216.34, the same on every hop", "sm bd t1");
    if (k >= 1 && k <= 3) { const h = k - 1, x = N[h][1] + 110, w = N[h + 1][1] - x; o += SV.rect(x + 8, 128, w - 16, 54, "cell-warn", { rx: 8 }) + SV.text(x + w / 2, 150, "Link layer frame", "sm bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, 170, MAC[h][0] + " → " + MAC[h][1], "sm", { "text-anchor": "middle", style: "font-family:var(--mono)" }); o += SV.circle(x + w / 2, 83, 7, "dot4"); }
    if (k === 4) o += SV.text(380, 160, "Arrived: IP addresses unchanged, three different pairs of MAC addresses used", "lbl bd t3", { "text-anchor": "middle", style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stH"), { w: 760, h: 200, label: "IP addresses stay the same, MAC addresses change at each hop", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A laptop sends to a web server. The <b>Internet layer</b> puts both IP addresses in the header. They will not change.", s: { i: 0 } },
    { cap: "Hop 1: the <b>Link layer</b> frames the packet with the laptop's and the home router's <b>MAC addresses</b>.", s: { i: 1 } },
    { cap: "Hop 2: the home router removes the frame, reads the destination IP, and makes a <b>new frame</b> with new MAC addresses.", s: { i: 2 } },
    { cap: "Hop 3: the ISP router does the same, framing the packet for the web server.", s: { i: 3 } },
    { cap: "The IP addresses stayed the same for the whole journey; the MAC addresses changed at every hop.", s: { i: 4 } }] });
})();
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
  let n = 4, order = [];
  const paint = () => {
    const shuffled = order.slice();
    $("#rb").innerHTML = `<div class="btnrow">${[3, 4, 5, 6].map((c) => `<button class="b${c === n ? " pri" : ""}" data-n="${c}">${c} packets</button>`).join("")}<button class="b" id="rbs">Shuffle arrival</button></div>` +
      `<p>Arrived in this order: <b>${shuffled.map((i) => "#" + (i + 1)).join("  ")}</b></p><p>After the Transport layer sorts them by sequence number: <b>${shuffled.slice().sort((a, b) => a - b).map((i) => "#" + (i + 1)).join("  ")}</b></p>`;
    $$("#rb button[data-n]").forEach((b) => (b.onclick = () => { n = +b.dataset.n; order = [...Array(n).keys()]; shuf(); }));
    $("#rbs").onclick = shuf;
  };
  const shuf = () => { order = [...Array(n).keys()]; for (let i = n - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; } paint(); };
  shuf();
})();
Lib.classify($("#cl1"), { prompt: "Which layer does each job belong to?", buckets: [{"label": "Application"}, {"label": "Transport"}, {"label": "Internet"}, {"label": "Link"}], items: [{"text": "Provides an interface to the user's programs", "b": 0}, {"text": "Adds a sequence number to each packet", "b": 1}, {"text": "Adds the source and destination IP address", "b": 2}, {"text": "Formats datagrams into frames", "b": 3}, {"text": "Controls the flow of packets", "b": 1}, {"text": "Routes each packet by the best route", "b": 2}, {"text": "Maps IP addresses to MAC addresses", "b": 3}, {"text": "Defines the protocols programs use to exchange data", "b": 0}], done: "Application: user. Transport: packets and sequence. Internet: IP and routing. Link: frames and MAC." });
Lib.classify($("#cl2"), { prompt: "Which layer does this belong to?", buckets: [{"label": "Transport"}, {"label": "Internet"}, {"label": "Link"}], items: [{"text": "Sequence number", "b": 0}, {"text": "Destination IP address", "b": 1}, {"text": "Source MAC address", "b": 2}, {"text": "Re-sending a lost packet", "b": 0}, {"text": "Routing", "b": 1}, {"text": "Wi-Fi or Ethernet", "b": 2}, {"text": "Putting packets back in order", "b": 0}, {"text": "A datagram", "b": 1}], done: "Sequence and re-sending are Transport. IP and routing are Internet. MAC, frames and Wi-Fi are Link." });
Lib.order($("#o1"), { prompt: "Put the layers in order, from the top (nearest the user) to the bottom.", items: ["Application", "Transport", "Internet", "Link"], done: "Application, Transport, Internet, Link." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Application", "Services for the user's programs and the protocols they use"], ["Transport", "End-to-end delivery in numbered packets"], ["Internet", "IP addresses and routing"], ["Link", "Frames, MAC addresses and the physical medium"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A message of 4000 bytes is split into packets of 500 bytes. How many packets?", "a": 8, "unit": "", "tol": 0.01, "hint": "4000 ÷ 500.", "sol": "<b>8</b>."},
  {"q": "A file of 2 MB is split into packets of 1000 bytes (take 1 MB as 1 000 000 bytes). How many packets?", "a": 2000, "unit": "", "tol": 0.01, "hint": "2 000 000 ÷ 1000.", "sol": "<b>2000</b>."},
  {"q": "A packet passes through 3 routers between two hosts. How many separate frames (hops) are used?", "a": 4, "unit": "", "tol": 0.01, "hint": "Host to router 1, 1 to 2, 2 to 3, 3 to host.", "sol": "<b>4</b>."},
  {"q": "Packets 1 to 6 are sent and packet 4 is lost. How many packets must be sent again?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the missing one.", "sol": "<b>1</b>."},
  {"q": "How many layers have a header added or removed that the Application layer never sees (Transport, Internet and Link)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Everything below the top.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which layer breaks data into packets and adds sequence numbers?", opts: ["Application", "Transport", "Internet", "Link"], a: 1, why: "Transport." },
  { q: "Which layer adds source and destination IP addresses?", opts: ["Internet", "Link", "Application", "Transport"], a: 0, why: "Internet." },
  { q: "Which is the bottom layer of the TCP/IP stack?", opts: ["Application", "Transport", "Internet", "Link"], a: 3, why: "Link." },
  { q: "Which layer maps IP addresses to MAC addresses?", opts: ["Internet", "Link", "Application", "Transport"], a: 1, why: "Link." },
  { q: "Which layer routes packets by the best route?", opts: ["Transport", "Link", "Internet", "Application"], a: 2, why: "Internet." },
  { q: "Which layer defines HTTP and SMTP?", opts: ["Application", "Transport", "Internet", "Link"], a: 0, why: "Application." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Application", "User services; HTTP, FTP, SMTP, POP3, IMAP, BitTorrent."],
  ["Transport", "Packets, sequence numbers, flow control, error recovery."],
  ["Internet", "IP addresses and routing."],
  ["Link", "Frames, MAC addresses, the physical medium."],
  ["Datagram", "A packet with IP addresses in the header."],
  ["Frame", "A packet with MAC addresses, ready for the physical medium."],
  ["Hop", "One step from one device to the next."],
  ["Next hop", "The next device on the route, prepared by the Link layer."],
] });

Lib.match($("#m2"), {"prompt": "Match the key word to its meaning.", "pairs": [["Port number", "Says which application the data is for"], ["Sequence number", "Lets the data be put back in order"], ["Datagram", "A packet carrying IP addresses"], ["Frame", "The unit sent over one local segment"], ["Routing table", "A router's list of where to send packets next"], ["Acknowledgement", "A message saying data has arrived"]], "done": "Use these words in your answers."});
