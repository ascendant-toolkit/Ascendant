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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.path("M30,100 H570", "ax", { style: "stroke-width:5" }); [[100, "A"], [300, "B"], [500, "C"]].forEach(([x, n]) => { o += SV.rect(x - 28, 30, 56, 36, k >= 1 && (n === "A" || n === "C") ? "cell-warn" : "cell", { rx: 6 }) + SV.text(x, 53, n, "lbl bd", { "text-anchor": "middle" }) + SV.path("M" + x + ",66 V100", "ax"); });
    if (k === 0) o += SV.text(30, 150, "A and C both want to send to B. Both listen to the line.", "lbl bd", { style: "font-size:13px" }); if (k === 1) o += SV.text(30, 150, "The line is idle: both start sending at the same moment.", "lbl bd", { style: "font-size:13px" });
    if (k >= 2) o += SV.circle(300, 100, 14, "dot2") + SV.text(300, 135, "collision!", "lbl bd t2", { "text-anchor": "middle" }); if (k === 3) o += SV.text(30, 165, "Both stop (abort) and send a jamming signal.", "lbl bd", { style: "font-size:13px" }); if (k >= 4) o += SV.text(30, 165, "A waits 2 slots, C waits 5 slots (random).", "lbl bd t3", { style: "font-size:13px" }); if (k >= 5) o += SV.circle(200, 100, 8, "dot3") + SV.text(30, 190, "A resends first and the frame gets through. C then sees the line busy and waits.", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 205, label: "CSMA/CD", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "<b>Carrier sense</b>: both A and C listen to the shared line before sending.", s: { i: 0 } }, { cap: "The line is idle, so both begin to send at the same time.", s: { i: 1 } }, { cap: "The signals <b>collide</b>.", s: { i: 2 } }, { cap: "<b>Collision detected</b>: both devices stop and send a jamming signal.", s: { i: 3 } }, { cap: "Each waits a <b>random time</b> before trying again. Random times make another collision unlikely.", s: { i: 4 } }, { cap: "The device with the shorter wait sends first and succeeds. If there were more collisions the random wait would be increased.", s: { i: 5 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 50, 120, 60, "cell", { rx: 8 }) + SV.text(80, 85, "LAN device", "lbl bd", { "text-anchor": "middle" }) + SV.rect(240, 40, 120, 80, "f3", { rx: 10 }) + SV.text(300, 70, "Router", "lbl bd", { "text-anchor": "middle" }) + SV.text(300, 92, "routing table", "sm", { "text-anchor": "middle" }) + SV.rect(460, 50, 120, 60, "cell", { rx: 8 }) + SV.text(520, 85, "Internet", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M140,80 H240", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(190, 70, "packet", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.text(300, 150, "destination IP 93.184.x.x read", "lbl bd", { "text-anchor": "middle", style: "font-size:12.5px" }); if (k >= 3) o += SV.text(300, 170, "looked up in the routing table: best route found", "lbl bd t3", { "text-anchor": "middle", style: "font-size:12.5px" }); if (k >= 4) o += SV.path("M360,80 H460", "ax", { style: "stroke:var(--good);stroke-width:3" }) + SV.text(410, 70, "forwarded", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 185, label: "Router", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A device on the LAN wants to reach something on the internet.", s: { i: 0 } }, { cap: "The router <b>receives the packet</b> from the device.", s: { i: 1 } }, { cap: "It <b>analyses the destination IP address</b>.", s: { i: 2 } }, { cap: "It looks the address up in its <b>routing table</b> and chooses the most efficient route.", s: { i: 3 } }, { cap: "It <b>forwards</b> the packet towards its destination.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(250, 70, 100, 50, "f3", { rx: 10 }) + SV.text(300, 100, "Switch", "lbl bd", { "text-anchor": "middle" });
    [[80, 40, "A"], [80, 150, "B"], [520, 40, "C"], [520, 150, "D"]].forEach(([x, y, n]) => { const to = k >= 3 && n === "D", from = k >= 1 && n === "A"; o += SV.path("M" + x + "," + y + " L300,95", "ax", { style: "stroke:" + (to || from ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (to || from ? 4 : 2) }); o += SV.rect(x - 26, y - 16, 52, 32, to ? "cell-ok" : from ? "cell-warn" : "cell", { rx: 6 }) + SV.text(x, y + 5, n, "lbl bd", { "text-anchor": "middle" }); });
    if (k >= 2) o += SV.text(300, 150, "MAC table: D is on port 4", "lbl bd", { "text-anchor": "middle", style: "font-size:12.5px" }); if (k >= 3) o += SV.text(300, 175, "B and C do not receive the frame", "lbl bd t3", { "text-anchor": "middle", style: "font-size:12.5px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 190, label: "Switch", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A wants to send a frame to D. All devices connect to the switch.", s: { i: 0 } }, { cap: "A sends the frame to the switch.", s: { i: 1 } }, { cap: "The switch checks the <b>destination MAC address</b> against its table.", s: { i: 2 } }, { cap: "It forwards the frame <b>only to D</b>. A hub would have sent it to everyone.", s: { i: 3 } }] });
})();

(function () {
  let st = { a: 0, b: 0 }, tries = 0, log = []; const b = $("#cB"); const rnd = () => Math.floor(Math.random() * 4);
  const paint = () => { $("#cT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Attempt</th><th>A waits</th><th>C waits</th><th>Result</th></tr>' + log.map((r, i) => `<tr><td>${i + 1}</td><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>"; $("#cV").innerHTML = log.length ? (log[log.length - 1][2].startsWith("sent") ? "A frame got through after <b>" + log.length + "</b> attempt" + (log.length > 1 ? "s" : "") + ". The random waits are what avoided a repeat collision." : "Collision again: the wait range grows after each collision.") : "Both devices send at once and collide. Press Retry to give each a random wait."; };
  const step = () => { const range = Math.min(8, 2 + log.length * 2), a = Math.floor(Math.random() * range), c = Math.floor(Math.random() * range); log.push([a + " slots", c + " slots", a === c ? "collision again" : "sent by " + (a < c ? "A" : "C") + " first"]); if (log.length > 8) log.shift(); paint(); };
  [["Retry", step], ["Start again", () => { log = []; paint(); }]].forEach(([t, f]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = f; b.appendChild(x); }); paint();
})();
btnTable("dB", "dO", [
  ["Gives a laptop a wireless connection", "WNIC", "Interface and antenna to the wireless network"],
  ["Connects the LAN to the internet", "Router", "Routes packets between networks by IP address"],
  ["Connects 30 classroom computers", "Switch", "Forwards frames only to the intended computer"],
  ["Lets phones join the wired LAN by Wi-Fi", "WAP", "Radio communication to the wired network"],
  ["Joins two LANs that use the same protocol", "Bridge", "Transmits data between the networks"],
  ["Strengthens a signal on a long cable", "Repeater", "Restores the digital signal"]
], ["Task", "Device", "Purpose"]);
(function () {
  let mode = "switch", from = "A", to = "D"; const b = $("#hB"), s = $("#hS"), g = $("#hG"); const nodes = { A: [60, 40], B: [60, 150], C: [540, 40], D: [540, 150] };
  const paint = () => { let o = '<svg viewBox="0 0 600 190" style="width:600px;max-width:100%;display:block">' + SV.rect(250, 70, 100, 50, "f3", { rx: 10 }) + SV.text(300, 100, mode === "switch" ? "Switch" : "Hub", "lbl bd", { "text-anchor": "middle" }); const got = from === to ? [] : mode === "hub" ? Object.keys(nodes).filter((n) => n !== from) : [to];
    Object.entries(nodes).forEach(([n, [x, y]]) => { const rx = got.includes(n); o += SV.path("M" + x + "," + y + " L300,95", "ax", { style: "stroke:" + (rx || n === from ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (rx || n === from ? 4 : 2) }) + SV.rect(x - 26, y - 16, 52, 32, n === from ? "cell-warn" : rx ? "cell-ok" : "cell", { rx: 6 }) + SV.text(x, y + 5, n, "lbl bd", { "text-anchor": "middle" }); });
    g.innerHTML = o + "</svg>"; $("#hV").innerHTML = from === to ? "Choose different devices." : `${mode === "hub" ? "A hub" : "A switch"} sends the frame from ${from} to <b>${got.join(", ")}</b>. ` + (mode === "hub" ? "Every device receives it, so more traffic and more collisions." : "Only the intended device receives it.");
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === mode ? "on" : "")); s.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === from + to ? "on" : "")); };
  [["switch", "Switch"], ["hub", "Hub"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { mode = k; paint(); }; b.appendChild(x); });
  [["A", "D"], ["B", "C"], ["C", "A"]].forEach(([f, t]) => { const x = document.createElement("button"); x.textContent = f + " to " + t; x.dataset.k = f + t; x.onclick = () => { from = f; to = t; paint(); }; s.appendChild(x); }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which device does the description match?", buckets: [{"label": "NIC / WNIC"}, {"label": "Switch"}, {"label": "Bridge"}, {"label": "Repeater"}], items: [{"text": "Provides a MAC address to identify the device on the network", "b": 0}, {"text": "Forwards packets only to the intended recipient", "b": 1}, {"text": "Restores the signal for greater distances", "b": 3}, {"text": "Joins two LANs that use the same protocol", "b": 2}, {"text": "Acts as an antenna for a laptop", "b": 0}, {"text": "Stores the MAC addresses of connected devices", "b": 1}], done: "NIC identifies, switch forwards, bridge joins, repeater restores." });
Lib.classify($("#cl2"), { prompt: "Is it done by a router or by a switch?", buckets: [{"label": "Router"}, {"label": "Switch"}], items: [{"text": "Joins the LAN to the internet", "b": 0}, {"text": "Connects devices inside a LAN by MAC address", "b": 1}, {"text": "Reads the destination IP address and uses a routing table", "b": 0}, {"text": "Allocates private IP addresses", "b": 0}, {"text": "Forwards a frame only to the receiving device on the LAN", "b": 1}, {"text": "Finds the most efficient route to the destination", "b": 0}], done: "Router: between networks, IP. Switch: inside a LAN, MAC." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Router", "Forwards packets between networks using IP addresses"], ["Switch", "Sends packets only to the intended device"], ["WAP", "Lets wireless devices join a wired network"], ["CSMA/CD", "Listen, send when idle, detect collisions"], ["Jamming signal", "Sent when a collision is detected"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the CSMA/CD steps in order.", items: ["The device listens to the channel", "It sends data when the line is idle", "A collision is detected", "A jamming signal is sent and transmission aborted", "Each device waits a random time and resends"], done: "Listen, send, collision, jam, random wait." });
Lib.calc($("#c1"), { qs: [
  {"q": "Two devices collide. Device A waits 3 slots and device B waits 5 slots. How many slots after the collision does A resend?", "a": 3, "unit": "", "tol": 0.01, "hint": "A's own wait.", "sol": "<b>3</b>."},
  {"q": "In the same case, how many slots later than A does B resend?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b>."},
  {"q": "A hub sends a frame to every connected device. A 6-port hub with one sender: how many devices receive it?", "a": 5, "unit": "", "tol": 0.01, "hint": "All the others.", "sol": "<b>5</b>."},
  {"q": "A switch with one sender and one intended receiver: how many devices receive the frame?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the receiver.", "sol": "<b>1</b>."},
  {"q": "How many items make up the Ethernet frame description in the Learn tab (source, destination, error-check)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Source address, destination address, error checking.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A switch forwards packets:", opts: ["To all devices", "Only to the intended recipient", "To the internet", "Nowhere"], a: 1, why: "Only to the recipient." },
  { q: "A router uses:", opts: ["A routing table", "A keyboard", "A monitor", "A pen"], a: 0, why: "A routing table." },
  { q: "When a collision is detected, devices:", opts: ["Send faster", "Abort and wait a random time", "Switch off", "Change topology"], a: 1, why: "Abort and wait." },
  { q: "A repeater:", opts: ["Restores the signal", "Allocates IP addresses", "Stores files", "Prints"], a: 0, why: "Restores the signal." },
  { q: "A bridge joins:", opts: ["Two LANs with the same protocol", "A PC and a printer", "Two monitors", "A network and a battery"], a: 0, why: "Two LANs, same protocol." },
  { q: "The NIC's MAC address:", opts: ["Identifies the device on the network", "Is the internet speed", "Is the monitor size", "Is a password"], a: 0, why: "Identifies the device." },
] });
Lib.cards($("#fc1"), { cards: [
  ["NIC", "Interface to the network; has a MAC address."],
  ["Switch", "Forwards only to the recipient; stores MAC addresses."],
  ["Router", "Connects networks; routing table; IP addresses."],
  ["WAP", "Wireless devices to a wired network."],
  ["Bridge", "Joins two LANs, same protocol."],
  ["Repeater", "Restores the signal."],
  ["Ethernet", "Wired LAN protocol using frames and CSMA/CD."],
  ["CSMA/CD", "Listen, send if idle, detect, jam, random wait."],
] });
