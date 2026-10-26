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

const TOPO = {
  star: { n: { SW: [150, 100, "switch"], A: [50, 40, "PC"], B: [250, 40, "PC"], C: [50, 160, "server"], D: [250, 160, "printer"], E: [150, 28, "PC"] }, e: [["SW", "A"], ["SW", "B"], ["SW", "C"], ["SW", "D"], ["SW", "E"]] },
  bus: { n: { A: [50, 45, "PC"], B: [120, 165, "PC"], C: [190, 45, "server"], D: [260, 165, "PC"], BA: [50, 105, ""], BB: [120, 105, ""], BC: [190, 105, ""], BD: [260, 105, ""], E1: [15, 105, ""], E2: [290, 105, ""] }, e: [["E1", "BA"], ["BA", "BB"], ["BB", "BC"], ["BC", "BD"], ["BD", "E2"], ["A", "BA"], ["B", "BB"], ["C", "BC"], ["D", "BD"]] },
  mesh: { n: { A: [150, 20, "PC"], B: [255, 80, "PC"], C: [215, 165, "PC"], D: [85, 165, "PC"], E: [45, 80, "PC"] }, e: [["A", "B"], ["A", "C"], ["A", "D"], ["A", "E"], ["B", "C"], ["B", "D"], ["B", "E"], ["C", "D"], ["C", "E"], ["D", "E"]] },
  hybrid: { n: { S1: [60, 100, "switch"], S2: [240, 100, "switch"], A: [20, 40, "PC"], B: [20, 160, "PC"], C: [280, 40, "PC"], D: [280, 160, "PC"], BB1: [105, 100, ""], BB2: [195, 100, ""] }, e: [["S1", "A"], ["S1", "B"], ["S2", "C"], ["S2", "D"], ["S1", "BB1"], ["BB1", "BB2"], ["BB2", "S2"]] }
};
function topoSvg(kind, o) { o = o || {}; const T = TOPO[kind]; let s = "";
  T.e.forEach(([a, b]) => { const x1 = T.n[a][0], y1 = T.n[a][1], x2 = T.n[b][0], y2 = T.n[b][1];
    const hot = o.hot && o.hot.some(([p, q]) => (p === a && q === b) || (p === b && q === a)), broken = o.broken && o.broken.some(([p, q]) => (p === a && q === b) || (p === b && q === a));
    s += SV.line(x1, y1, x2, y2, "ax", { style: "stroke:" + (broken ? "var(--bad)" : hot ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (hot ? 4 : broken ? 3 : 2) + (broken ? ";stroke-dasharray:5 5" : "") }); });
  Object.entries(T.n).forEach(([k, [x, y, t]]) => { if (!t) return; const cur = o.cur === k, lost = o.lost && o.lost.includes(k); s += SV.rect(x - 24, y - 15, 48, 30, lost ? "cell-no" : cur ? "cell-warn" : "cell", { rx: 6 }) + SV.text(x, y + 4, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); }); return s; }
document.querySelectorAll("[data-topo]").forEach((el) => (el.innerHTML = '<svg viewBox="0 0 300 190" style="width:300px;max-width:100%;display:block">' + topoSvg(el.dataset.topo) + "</svg>"));
(function () {
  const path = [["A", "SW"], ["SW", "C"]]; const seq = [{ cap: "Computer A wants to send a packet to the server. Every device is connected only to the central switch.", hot: [], cur: "A" }, { cap: "A sends the packet to the <b>switch</b>.", hot: [["A", "SW"]], cur: "SW" }, { cap: "The switch reads the <b>destination address</b> on the packet.", hot: [], cur: "SW" }, { cap: "It forwards the packet <b>only</b> to the server. No other device receives it, so there are few collisions.", hot: [["SW", "C"]], cur: "C" }];
  Lib.stepper($("#stA"), { w: 300, h: 190, label: "Star", base: { i: 0 }, draw: (s) => { const q = seq[Math.round(s.i)]; return topoSvg("star", { hot: q.hot, cur: q.cur }); }, tween: 100, dwell: 2600, steps: seq.map((q, i) => ({ cap: q.cap, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = topoSvg("bus", {}); const pk = (x, c) => SV.circle(x, 105, 8, c);
    if (k === 1) o += pk(50, "dot1") ; if (k === 2) o += pk(120, "dot1") + SV.text(120, 90, "→ to server", "sm", { "text-anchor": "middle" }); if (k === 3) o += pk(190, "dot3"); if (k === 4) o += pk(80, "dot1") + pk(230, "dot2") + SV.text(150, 90, "collision!", "lbl bd t2", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 300, h: 190, label: "Bus", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "All devices share one backbone cable.", s: { i: 0 } }, { cap: "A sends a packet onto the backbone.", s: { i: 1 } }, { cap: "It travels along the cable past every device. Each looks at the address.", s: { i: 2 } }, { cap: "The server sees its own address and accepts the packet.", s: { i: 3 } }, { cap: "If two devices send at the same time, the signals <b>collide</b> and both must try again.", s: { i: 4 } }] });
})();
(function () {
  const seq = [{ cap: "Computer A sends a packet to C. There are several routes.", hot: [["A", "C"]], br: [] }, { cap: "The direct link A to C is cut.", hot: [], br: [["A", "C"]] }, { cap: "The packet goes another way: A to B to C. Devices act as <b>relays</b>.", hot: [["A", "B"], ["B", "C"]], br: [["A", "C"]] }];
  Lib.stepper($("#stC"), { w: 300, h: 190, label: "Mesh", base: { i: 0 }, draw: (s) => { const q = seq[Math.round(s.i)]; return topoSvg("mesh", { hot: q.hot, broken: q.br }); }, tween: 100, dwell: 2800, steps: seq.map((q, i) => ({ cap: q.cap, s: { i } })) });
})();
(function () {
  let n = 8; const paint = () => { $("#nT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Topology</th><th>Cables / links needed</th></tr>' + `<tr><td>Bus</td><td>1 backbone + ${n} connections</td></tr><tr><td>Star</td><td>${n} (one from each device to the switch)</td></tr><tr><td>Full mesh</td><td><b>${(n * (n - 1)) / 2}</b> (n × (n − 1) ÷ 2)</td></tr></table></div><div class="verdict">With ${n} devices a full mesh needs <b>${(n * (n - 1)) / 2}</b> links against ${n} for a star. That is why a full mesh is expensive.</div>`; };
  Lib.slider($("#nS"), { id: "ns", label: "Devices ", min: 2, max: 20, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
(function () {
  let kind = "star", broken = []; const b = $("#fB"), g = $("#fG"); const ALT = { star: TOPO.star, mesh: TOPO.mesh };
  const lostOf = () => { const T = TOPO[kind], names = Object.keys(T.n), hub = kind === "star" ? "SW" : "A"; const adj = {}; names.forEach((x) => (adj[x] = [])); T.e.forEach(([p, q]) => { if (!broken.some(([a, c]) => (a === p && c === q) || (a === q && c === p))) { adj[p].push(q); adj[q].push(p); } }); const seen = new Set([hub]), st = [hub]; while (st.length) { const u = st.pop(); adj[u].forEach((v) => { if (!seen.has(v)) { seen.add(v); st.push(v); } }); } return names.filter((x) => !seen.has(x) && T.n[x][2]); };
  const paint = () => { const T = TOPO[kind], lost = lostOf(); g.innerHTML = '<svg viewBox="0 0 300 190" style="width:300px;max-width:100%;display:block;cursor:pointer" id="fSvg">' + topoSvg(kind, { broken, lost }) + "</svg>";
    $("#fSvg").onclick = (e) => { const r = e.currentTarget.getBoundingClientRect(), x = ((e.clientX - r.left) / r.width) * 300, y = ((e.clientY - r.top) / r.height) * 190; let best = null, bd = 18; T.e.forEach(([p, q], i) => { const [x1, y1] = T.n[p], [x2, y2] = T.n[q]; const dx = x2 - x1, dy = y2 - y1, t = Math.max(0, Math.min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy || 1))), d = Math.hypot(x - (x1 + t * dx), y - (y1 + t * dy)); if (d < bd) { bd = d; best = [p, q]; } }); if (best) { const i = broken.findIndex(([a, c]) => (a === best[0] && c === best[1])); if (i >= 0) broken.splice(i, 1); else broken.push(best); paint(); } };
    $("#fV").innerHTML = broken.length ? (lost.length ? "Devices cut off: <b>" + lost.map((x) => T.n[x][2] + " " + x).join(", ") + "</b>." : "<b>Nobody is cut off:</b> there is another route.") + " Click a broken cable again to repair it." : "Click a cable to break it.";
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === kind ? "on" : "")); };
  ["star", "mesh"].forEach((k) => { const x = document.createElement("button"); x.textContent = k === "star" ? "Star" : "Mesh"; x.dataset.k = k; x.onclick = () => { kind = k; broken = []; paint(); }; b.appendChild(x); }); paint();
})();
btnTable("mB", "mO", [
  ["A company with many users and sensitive data", "Client-server", "Central security, backup and access control"],
  ["Three friends sharing music files", "Peer-to-peer", "Cheap and simple; no server needed"],
  ["A call centre of identical desks", "Thin clients", "Easy to manage; the server does the processing"],
  ["A designer editing large video files", "Thick client", "Processes locally; does not wait for the server"],
  ["A classroom of 20 computers", "Star topology", "Faults stay local; easy to add computers"],
  ["Hospital sites that must stay linked", "Mesh topology", "Several routes if a link fails"]
], ["Situation", "Choice", "Reason"]);
Lib.classify($("#cl1"), { prompt: "Is the description a LAN or a WAN?", buckets: [{"label": "LAN"}, {"label": "WAN"}], items: [{"text": "Covers a small geographical area", "b": 0}, {"text": "Uses leased or public infrastructure", "b": 1}, {"text": "Normally privately owned", "b": 0}, {"text": "The internet is the largest one", "b": 1}, {"text": "Higher data transfer rate", "b": 0}, {"text": "Covers several cities", "b": 1}], done: "LAN: small, private, fast. WAN: large, shared, slower." });
Lib.classify($("#cl2"), { prompt: "Which network model does it describe?", buckets: [{"label": "Client-server"}, {"label": "Peer-to-peer"}], items: [{"text": "A central server manages security and backup", "b": 0}, {"text": "All computers have equal status", "b": 1}, {"text": "Needs a network manager and a server", "b": 0}, {"text": "Each computer is responsible for its own security", "b": 1}, {"text": "Suits a few friends sharing files", "b": 1}, {"text": "Suits a company with sensitive data", "b": 0}], done: "Server in charge, or all peers equal." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["LAN", "A network covering a small area on private equipment"], ["Thin client", "Relies on the server for processing"], ["Thick client", "Does most of its own processing"], ["Star topology", "Every device connects to a central switch"], ["Mesh topology", "Multiple routes between devices"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order for a packet in a star network.", items: ["The sending device sends the packet to the switch", "The switch reads the destination address", "The switch forwards the packet only to the receiver", "The receiving device accepts the packet"], done: "Send, read, forward, receive." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many cables does a star network of 8 devices need (one to each device from the switch)?", "a": 8, "unit": "", "tol": 0.01, "hint": "One per device.", "sol": "<b>8</b>."},
  {"q": "How many links does a full mesh of 5 devices need?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 4 ÷ 2.", "sol": "<b>10</b>."},
  {"q": "How many links does a full mesh of 6 devices need?", "a": 15, "unit": "", "tol": 0.01, "hint": "6 × 5 ÷ 2.", "sol": "<b>15</b>."},
  {"q": "In a star network of 20 computers one computer's cable is cut. How many computers lose their connection?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only that one.", "sol": "<b>1</b>."},
  {"q": "In a bus network the backbone cable is cut in the middle. Is the network still fully connected? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "It splits in two.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a WAN?", opts: ["A network in one room", "A network covering a large geographical area", "A type of cable", "A printer"], a: 1, why: "A wide area network." },
  { q: "Which is a peer-to-peer feature?", opts: ["A central server", "All computers have equal status", "Needs an administrator", "Thin clients"], a: 1, why: "Equal status." },
  { q: "In a star network packets are forwarded by the:", opts: ["Switch", "Printer", "Monitor", "Keyboard"], a: 0, why: "The central switch." },
  { q: "A thin client:", opts: ["Does most processing locally", "Relies on the server", "Has no screen", "Needs no network"], a: 1, why: "It relies on the server." },
  { q: "Which topology has multiple routes between devices?", opts: ["Bus", "Star", "Mesh", "None"], a: 2, why: "Mesh." },
  { q: "A drawback of a bus network is:", opts: ["Collisions on the shared cable", "Too many cables", "Needs a switch for every device", "No data can be sent"], a: 0, why: "Collisions." },
] });
Lib.cards($("#fc1"), { cards: [
  ["LAN", "Small area, private, fast."],
  ["WAN", "Large area, external infrastructure."],
  ["Client-server", "Server manages; clients request."],
  ["Peer-to-peer", "All equal; no central control."],
  ["Thin client", "Server does the processing."],
  ["Thick client", "Does its own processing."],
  ["Star", "All to one switch; fault stays local."],
  ["Mesh", "Many routes; very reliable; costly."],
] });
