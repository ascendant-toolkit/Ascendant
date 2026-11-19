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


(function () {
  const L = ["Application", "Transport", "Internet", "Link"];
  let a = null, b = null;
  const paint = () => {
    const pick = (who, sel) => `<div class="btnrow">` + L.map((l, i) => `<button class="b${sel === i ? " pri" : ""}" data-w="${who}" data-i="${i}">${l}</button>`).join("") + `</div>`;
    let v = "Choose a layer in each row.";
    if (a !== null && b !== null) v = a === b ? "That is the same layer. Pick two different layers." : Math.abs(a - b) === 1 ? L[a] + " and " + L[b] + " are <b>adjacent</b>: they can exchange data through their interface." : L[a] + " and " + L[b] + " are <b>not adjacent</b>. Data has to pass through " + (Math.abs(a - b) === 2 ? "the " + L[Math.min(a, b) + 1] + " layer" : "the layers between them") + " first.";
    $("#adj").innerHTML = "<p><b>First layer</b></p>" + pick("a", a) + "<p><b>Second layer</b></p>" + pick("b", b) + `<div class="verdict">${v}</div>`;
    $$("#adj button").forEach((x) => (x.onclick = () => { if (x.dataset.w === "a") a = +x.dataset.i; else b = +x.dataset.i; paint(); }));
  };
  paint();
})();

(function () {
  const opts = [["Ethernet cable", "Ethernet frames"], ["Wi-Fi", "Wi-Fi frames"], ["Mobile data", "mobile network frames"]];
  const rows = [["Application", "Web browser using HTTP"], ["Transport", "Numbered packets"], ["Internet", "IP addresses"]];
  let cur = 0;
  const paint = () => {
    $$("#swB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#swO").innerHTML = '<div class="tw"><table class="t"><tr><th>Layer</th><th>What it uses</th><th>Changed?</th></tr>' + rows.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>No</td></tr>`).join("") + `<tr><td><b>Link</b></td><td style="background:var(--warn-soft)">${opts[cur][1]} over ${opts[cur][0].toLowerCase()}</td><td>${cur === 0 ? "No (starting point)" : "<b>Yes</b>"}</td></tr></table></div>`;
  };
  $("#swB").innerHTML = opts.map((o, i) => `<button class="b" data-i="${i}">${o[0]}</button>`).join("");
  $$("#swB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); paint();
})();
Lib.classify($("#cl1"), { prompt: "Does this happen on the way down (sending) or on the way up (receiving)?", buckets: [{"label": "Down the stack"}, {"label": "Up the stack"}], items: [{"text": "A header is added", "b": 0}, {"text": "A header is removed", "b": 1}, {"text": "The data starts at the Application layer", "b": 0}, {"text": "The data ends at the Application layer", "b": 1}, {"text": "Data is passed to the next lower layer", "b": 0}, {"text": "Data is passed to the next higher layer", "b": 1}, {"text": "The Link layer sends the frames onto the network", "b": 0}, {"text": "The Link layer receives the frames from the network", "b": 1}], done: "Sending: down, headers added. Receiving: up, headers removed." });
Lib.classify($("#cl2"), { prompt: "Is the statement about a protocol or about the stack?", buckets: [{"label": "About a protocol"}, {"label": "About the stack"}], items: [{"text": "A standard set of rules for communication", "b": 0}, {"text": "Layers that can only talk to adjacent layers", "b": 1}, {"text": "Allows devices from different manufacturers to communicate", "b": 0}, {"text": "Headers are added on the way down", "b": 1}, {"text": "Makes communication independent of hardware and software", "b": 0}, {"text": "User interaction at the top, hardware access at the bottom", "b": 1}], done: "A protocol is the rules. The stack is the layered way of implementing them." });
Lib.order($("#o1"), { prompt: "Put the layers in order, from the top (nearest the user) to the bottom.", items: ["Application", "Transport", "Internet", "Link"], done: "Application, Transport, Internet, Link." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Stack", "Layers of protocols, each with its own function"], ["Layer", "One level of the stack with one specific job"], ["Interface", "The only point of interaction between adjacent layers"], ["Header", "Information added to the data by a layer"], ["Adjacent", "The layer directly above or directly below"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many layers are in the TCP/IP protocol suite as used in the exam?", "a": 4, "unit": "", "tol": 0.01, "hint": "Application, Transport, Internet, Link.", "sol": "<b>4</b>."},
  {"q": "A message goes down the stack. How many headers have been added by the time it leaves the bottom layer (one for each layer below the top)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Transport, Internet and Link.", "sol": "<b>3</b>."},
  {"q": "How many layers can the second layer from the top exchange data with directly?", "a": 2, "unit": "", "tol": 0.01, "hint": "The adjacent layers above and below.", "sol": "<b>2</b>."},
  {"q": "How many layers can the top layer exchange data with directly?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the layer below it.", "sol": "<b>1</b>."},
  {"q": "A message passes down 4 layers, across the network and up 4 layers. How many layers does it pass through in total?", "a": 8, "unit": "", "tol": 0.01, "hint": "4 + 4.", "sol": "<b>8</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Where does user interaction take place in a protocol stack?", opts: ["The bottom layer", "The top layer", "Every layer", "The middle layers only"], a: 1, why: "At the top." },
  { q: "Where does direct access to the hardware take place?", opts: ["The top layer", "The bottom layer", "Every layer", "None"], a: 1, why: "At the bottom." },
  { q: "A layer can only interact with...", opts: ["any other layer", "the adjacent layers", "the top layer", "the bottom layer"], a: 1, why: "Above and below." },
  { q: "What happens to the header as data passes down the stack?", opts: ["It is removed", "Data is added to it", "It is encrypted", "Nothing"], a: 1, why: "Each layer adds to the header." },
  { q: "Why is a layered design useful?", opts: ["It makes the data smaller", "A layer can be changed without changing the others", "It removes the need for hardware", "It makes the connection free"], a: 1, why: "Independence of the layers." },
  { q: "What carries out the interactions between layers?", opts: ["Installed software", "A cable", "A router only", "The user"], a: 0, why: "Installed software." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Stack", "Layers of protocols, each with its own function."],
  ["Adjacent", "A layer interacts only with the layer above and below."],
  ["Interface", "The only interaction between adjacent layers."],
  ["Top layer", "User interaction."],
  ["Bottom layer", "Direct access to the hardware."],
  ["Sending", "Down the stack; data added to the header."],
  ["Receiving", "Up the stack; headers removed."],
  ["Why layers", "Each layer can change on its own."],
] });
