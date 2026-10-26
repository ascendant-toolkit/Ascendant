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
    const lanes = [40, 110, 180];
    o += SV.rect(20, 80, 90, 60, "f2", { rx: 8 }) + SV.text(65, 115, "Sender", "lbl bd", { "text-anchor": "middle" }) + SV.rect(650, 80, 90, 60, "f2", { rx: 8 }) + SV.text(695, 115, "Receiver", "lbl bd", { "text-anchor": "middle" });
    lanes.forEach((y, i) => (o += SV.line(110, 110, 380, y, "ax") + SV.line(380, y, 650, 110, "ax") + SV.rect(340, y - 16, 80, 32, "f3", { rx: 6 }) + SV.text(380, y + 5, "Router " + "ABC"[i], "lbl", { "text-anchor": "middle", style: "font-size:12px" })));
    const lane = [0, 1, 2, 0, 1, 2], pk = ["HE", "LL", "O ", "WO", "RL", "D!"];
    pk.forEach((d, i) => {
      if (k === 0) return;
      let x, y;
      if (k === 1) { x = 130; y = 50 + i * 22; }
      else if (k === 2) { x = 330 + (i > 2 ? 0 : 0) + (i % 3) * 0; y = lanes[lane[i]] + (i > 2 ? 22 : -22); x = 360 + (i > 2 ? 60 : 0); }
      else { x = 560 + (i % 3) * 32; y = 100 + (i > 2 ? 24 : 0) - 6; }
      if (k <= 3) o += SV.rect(x - 22, y - 10, 44, 20, "cell-warn", { rx: 3 }) + SV.text(x, y + 4, (i + 1) + ":" + d, "lbl bd", { "text-anchor": "middle", style: "font-size:11px;font-family:var(--mono)" });
    });
    if (k === 0) o += SV.text(115, 170, "HELLO WORLD!", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" });
    if (k === 3) o += SV.text(380, 232, "arrival order: 2, 1, 3, 5, 4, 6 (out of order)", "lbl bd t2", { "text-anchor": "middle", style: "font-size:14px" });
    if (k === 4) o += SV.text(380, 232, "reassembled by sequence number: 1 2 3 4 5 6 = HELLO WORLD!", "lbl bd t3", { "text-anchor": "middle", style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 245, label: "A message split into packets", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "The message \"HELLO WORLD!\" is to be sent. It is <b>divided</b> into equal-sized packets.", s: { i: 0 } },
    { cap: "Each packet gets a <b>header</b> (source and destination IP addresses, sequence number) and is sent <b>independently</b>.", s: { i: 1 } },
    { cap: "The packets take <b>different routes</b> through different routers, chosen by the routers at the time.", s: { i: 2 } },
    { cap: "They <b>arrive out of order</b>, because the routes differ in length and congestion.", s: { i: 3 } },
    { cap: "The receiver uses the <b>sequence numbers</b> to put them in order and <b>reassemble</b> the message.", s: { i: 4 } }] });
})();

(function () {
  const rows = ["1 Read the destination IP address in the packet header", "2 Look it up in the routing table", "3 Decide the next hop (the best route)", "4 Reduce the hop count by 1", "5 Send the packet on its next hop"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.rect(30, 20, 120, 44, "f2", { rx: 6 }) + SV.text(90, 48, "packet in", "lbl bd", { "text-anchor": "middle" }) + SV.rect(610, 20, 120, 44, "f2", { rx: 6 }) + SV.text(670, 48, "packet out", "lbl bd", { "text-anchor": "middle" });
    rows.forEach((r, i) => (o += SV.rect(180, 20 + i * 38, 400, 32, k === i + 1 ? "cell-warn" : k > i + 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(194, 41 + i * 38, r, "lbl", { style: "font-size:13px" })));
    if (k >= 2) o += SV.text(30, 200, "routing table entry used:", "sm") + SV.text(30, 218, "172.16.0.0/16 → Router C", "lbl", { style: "font-family:var(--mono);font-size:12px" });
    if (k >= 4) o += SV.text(610, 130, "hop count 8 → 7", "lbl bd", { style: "font-family:var(--mono);font-size:13px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "The function of a router", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A packet arrives at a router.", s: { i: 0 } },
    { cap: "The router <b>reads the destination IP address</b> from the packet header.", s: { i: 1 } },
    { cap: "It looks the address up in its <b>routing table</b> (hops, netmask, gateway, status of routes).", s: { i: 2 } },
    { cap: "It decides the <b>next hop</b>: the best route at that moment.", s: { i: 3 } },
    { cap: "It <b>reduces the hop count by 1</b>. If it reaches 0 the packet is discarded.", s: { i: 4 } },
    { cap: "It sends the packet to the next router. Each router repeats this, hop by hop.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "Packets received:", "lbl bd");
    for (let i = 1; i <= 5; i++) { const lost = i === 3 && k < 3; o += SV.rect(30 + (i - 1) * 90, 44, 80, 40, lost ? "cell-no" : "f3", { rx: 6 }) + SV.text(70 + (i - 1) * 90, 70, lost ? "?" : "P" + i, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); }
    if (k >= 1) o += SV.text(30, 120, "The receiver checks the sequence numbers: packet 3 is missing", "lbl bd t2", { style: "font-size:14px" });
    if (k >= 2) o += SV.text(30, 150, "It sends a re-send request for packet 3", "lbl", { style: "font-size:14px" });
    if (k >= 3) o += SV.text(30, 180, "Packet 3 arrives (by any route): the message is complete", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 205, label: "Re-sending a missing packet", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Five packets were sent. They are checked on arrival.", s: { i: 0 } },
    { cap: "Packet 3 did not arrive, or arrived damaged. The receiver notices a gap in the sequence numbers.", s: { i: 1 } },
    { cap: "It sends a <b>re-send request</b>. Only that packet needs to be sent again.", s: { i: 2 } },
    { cap: "The missing packet arrives and the message is reassembled complete.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const run = () => {
    const msg = "HELLO WORLD!", size = 2, pk = []; for (let i = 0; i < msg.length; i += size) pk.push(msg.slice(i, i + size));
    const delays = [5, 2, 7, 3, 6, 1], route = ["A", "B", "C", "A", "B", "C"], lose = $("#pL").checked;
    const arr = pk.map((d, i) => ({ n: i + 1, d, t: delays[i % 6], r: route[i % 6] })).filter((p) => !(lose && p.n === 3)).sort((a, b) => a.t - b.t);
    let h = '<div class="tw"><table class="t mono"><tr><th>Arrival</th><th>Packet</th><th>Data</th><th>Route</th></tr>' + arr.map((p, i) => `<tr><td>${i + 1}</td><td>${p.n}</td><td>"${p.d}"</td><td>${p.r}</td></tr>`).join("") + "</table></div>";
    const ordered = arr.slice().sort((a, b) => a.n - b.n);
    h += '<div class="tw"><table class="t mono"><tr><th>Reassembled by sequence number</th></tr><tr><td>' + ordered.map((p) => p.d).join("") + (lose ? " …(packet 3 missing)" : "") + "</td></tr></table></div>";
    $("#pO").innerHTML = h;
    $("#pV").textContent = lose ? "Packet 3 is missing, so the receiver sends a re-send request. Only packet 3 is sent again, then the message is complete: HELLO WORLD!" : "The packets took three routes and arrived out of order, but the sequence numbers let the receiver reassemble HELLO WORLD!";
  };
  $("#pG").onclick = run; $("#pL").onchange = run; run();
})();

/* Lab 2 */
(function () {
  const addrs = [["172.16.4.9", "Router C"], ["10.2.3.4", "Router B"], ["192.168.1.20", "deliver locally"], ["8.8.8.8", "Router D (default route)"]]; let cur = 0, hop = 8;
  const table = [["10.0.0.0 / 8", "Router B"], ["172.16.0.0 / 16", "Router C"], ["192.168.1.0 / 24", "deliver locally"], ["default", "Router D (default route)"]];
  const paint = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const a = addrs[cur], hit = table.findIndex((t) => t[1] === a[1]);
    $("#rO").innerHTML = '<p>Destination IP address in the header: <b class="mono">' + a[0] + '</b>, hop count ' + hop + '</p><div class="tw"><table class="t mono"><tr><th>Network</th><th>Next hop</th></tr>' + table.map((t, i) => `<tr style="${i === hit ? "background:var(--warn-soft);font-weight:700" : ""}"><td>${t[0]}</td><td>${t[1]}</td></tr>`).join("") + "</table></div><div class=\"verdict\">The router reads " + a[0] + ", finds the matching entry, reduces the hop count to " + (hop - 1) + " and sends the packet to: " + a[1] + ".</div>";
  };
  $("#rB").innerHTML = addrs.map((a) => `<button class="b">${a[0]}</button>`).join("");
  $$("#rB button").forEach((b, i) => (b.onclick = () => { cur = i; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Path", "A dedicated circuit set up first", "No dedicated path; each packet finds its own", "Set up before or sent straight away"],
  ["Data", "A continuous stream, message intact", "Split into packets with headers", "Segmented or not"],
  ["Route", "All the data follows the same route", "Packets can follow different routes", "Same or different routes"],
  ["Order", "Arrives in order sent", "May arrive out of order: reassembled", "Reordering delay"],
  ["Bandwidth", "Whole bandwidth, not shared", "Shared with other traffic", "Wasted or shared"],
  ["Faults", "The transmission ends if the route fails", "Re-routed; individual packets re-sent", "Resilience"]
], ["Feature", "Circuit switching", "Packet switching", "Point to make"]);
Lib.classify($("#cl1"), { prompt: "Circuit switching or packet switching?", buckets: [{"label": "Circuit switching"}, {"label": "Packet switching"}], items: [{"text": "A dedicated path is set up before sending", "b": 0}, {"text": "Data is split into packets with headers", "b": 1}, {"text": "All data follows the same route", "b": 0}, {"text": "Packets may arrive out of order", "b": 1}, {"text": "Bandwidth is shared between users", "b": 1}, {"text": "The whole bandwidth is reserved", "b": 0}, {"text": "A router reads the destination IP address", "b": 1}, {"text": "Individual lost packets can be re-sent", "b": 1}], done: "Dedicated and continuous: circuit. Packets, headers, routers: packet." });
Lib.classify($("#cl2"), { prompt: "Benefit or drawback of packet switching?", buckets: [{"label": "Benefit"}, {"label": "Drawback"}], items: [{"text": "Packets can be re-routed around a fault", "b": 0}, {"text": "Packets have to be reassembled at the destination", "b": 1}, {"text": "Bandwidth can be shared", "b": 0}, {"text": "Needs a complex algorithm and lots of RAM", "b": 1}, {"text": "A lost packet can be re-sent on its own", "b": 0}, {"text": "Not suitable for real-time transmission", "b": 1}], done: "Benefits: re-routing, sharing, resending one packet. Drawbacks: delay, complexity." });
Lib.order($("#o1"), { prompt: "Put the steps of packet switching in order.", items: ["The message is divided into packets", "Each packet is given a header with the IP addresses and a sequence number", "Each packet is sent independently by routers, possibly on different routes", "The packets arrive at the destination, possibly out of order", "The packets are reassembled in order and missing ones are re-sent"], done: "Divide, header, send independently, arrive, reassemble." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Packet", "A small chunk of a message with a header"], ["Header", "Holds the IP addresses and sequence number"], ["Router", "Reads the destination IP address and chooses the next hop"], ["Routing table", "Information the router uses to choose the next hop"], ["Hop count", "Reduced by 1 at each router so a packet cannot circulate forever"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 6000-byte message is sent in packets of 500 bytes. How many packets?", "a": 12, "unit": "", "tol": 0.01, "hint": "6000 ÷ 500.", "sol": "<b>12</b>."},
  {"q": "A packet starts with a hop count of 10 and passes through 4 routers. What is the hop count after?", "a": 6, "unit": "", "tol": 0.01, "hint": "10 − 4.", "sol": "<b>6</b>."},
  {"q": "12 packets are sent and packets 5 and 9 are lost. How many arrive?", "a": 10, "unit": "", "tol": 0.01, "hint": "12 − 2.", "sol": "<b>10</b>."},
  {"q": "How many packets have to be re-sent in the example above?", "a": 2, "unit": "", "tol": 0.01, "hint": "Only the lost ones.", "sol": "<b>2</b>."},
  {"q": "A packet has a hop count of 3 and needs 5 hops to reach its destination. Does it arrive? Enter 1 for yes, 0 for no.", "a": 0, "unit": "", "tol": 0.01, "hint": "The count reaches 0 after 3 hops: the packet is discarded.", "sol": "<b>0</b>: it is discarded."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does a router read to decide where to send a packet?", opts: ["The payload", "The destination IP address in the header", "The MAC address of the sender", "The file name"], a: 1, why: "The header's destination IP address." },
  { q: "Which is a benefit of packet switching?", opts: ["The data always arrives in order", "Packets can be re-routed around a fault", "A dedicated circuit is reserved", "No reassembly is needed"], a: 1, why: "Resilience." },
  { q: "Which is a drawback of packet switching?", opts: ["The bandwidth cannot be shared", "Packets must be reordered and reassembled", "A circuit must be set up", "There is no alternative route"], a: 1, why: "Delay." },
  { q: "What is used to reassemble the packets?", opts: ["The hop count", "The sequence number", "The MAC address", "The payload"], a: 1, why: "Sequence numbers." },
  { q: "Packets of one message...", opts: ["must take the same route", "may take different routes", "are never re-sent", "always arrive in order"], a: 1, why: "Each is sent independently." },
  { q: "What happens to a packet whose hop count reaches 0?", opts: ["It is delivered", "It is discarded", "It is copied", "It is encrypted"], a: 1, why: "It is discarded." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Packet switching", "Message split into packets sent independently, reassembled at the destination."],
  ["Header", "Source and destination IP addresses, sequence number."],
  ["Router", "Reads the destination IP, uses the routing table, sends the packet on its next hop."],
  ["Hop count", "Reduced at each router; at 0 the packet is discarded."],
  ["Benefits", "Re-routing, resending one packet, shared bandwidth, security."],
  ["Drawbacks", "Delay reordering, complex, RAM, not real time."],
  ["Versus circuit", "No dedicated path, packets, different routes, shared bandwidth."],
  ["Complete message", "Check on arrival, request re-send, re-route."],
] });
