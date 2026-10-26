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
  const stops = ["Sender's email client", "Sender's mail server", "Recipient's mail server", "Recipient's email client"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    stops.forEach((t, i) => (o += SV.rect(20 + i * 185, 60, 160, 60, k >= i ? "f3" : "cell", { rx: 8, ...op(k >= i ? 1 : 0.5) }) + SV.text(100 + i * 185, 96, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" })));
    const labs = ["SMTP", "SMTP", "POP3 or IMAP"]; labs.forEach((t, i) => { const on = k > i; o += arrow(180 + i * 185, 90, 205 + i * 185, 90, i === 2 ? "l" : "r", on ? "c2" : "c1", on ? 1 : 0.2) + SV.text(192 + i * 185, 50, t, "lbl bd" + (on ? " t3" : ""), { "text-anchor": "middle", style: "font-size:12px", ...op(on ? 1 : 0.35) }); });
    if (k >= 1) o += SV.text(30, 160, k === 1 ? "push: the client sends the message to its mail server" : k === 2 ? "push: servers pass the message towards its destination" : "pull: the recipient's client retrieves the message", "lbl bd", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 190, label: "An email's journey", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "An email travels from the sender's email client to the recipient's email client through two mail servers.", s: { i: 0 } },
    { cap: "<b>SMTP</b> pushes the message from the sender's client to the sender's mail server.", s: { i: 1 } },
    { cap: "<b>SMTP</b> again carries it from server to server, towards its destination.", s: { i: 2 } },
    { cap: "The recipient's client <b>pulls</b> the message from the server with <b>POP3</b> or <b>IMAP</b>.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "POP3", "lbl bd") + SV.text(400, 22, "IMAP", "lbl bd");
    const box = (x, t, on, cls) => SV.rect(x, 34, 150, 44, on ? cls : "cell", { rx: 6 }) + SV.text(x + 75, 61, t, "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    o += box(30, "Mail server: 1 email", true, "f3") + box(400, "Mail server: 1 email", true, "f3");
    o += box(30, k >= 1 ? "Laptop: downloaded" : "Laptop", k >= 1, "cell-ok") + box(400, k >= 1 ? "Laptop: shows a copy" : "Laptop", k >= 1, "cell-ok");
    o += SV.rect(30, 130, 150, 44, k >= 2 ? "cell-no" : "cell", { rx: 6 }) + SV.text(105, 157, k >= 2 ? "Phone: nothing" : "Phone", "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    o += SV.rect(400, 130, 150, 44, k >= 2 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(475, 157, k >= 2 ? "Phone: shows a copy" : "Phone", "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    if (k >= 1) { o += SV.rect(30 + 160, 34, 190, 44, k >= 1 ? "cell-no" : "cell", { rx: 6 }) + SV.text(285, 61, "removed from the server", "lbl", { "text-anchor": "middle", style: "font-size:12px" }); o += SV.text(560, 61, "stays on the server", "lbl bd t3", { style: "font-size:13px" }); }
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 200, label: "POP3 and IMAP", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "One email waits on the mail server. The user has a laptop and a phone.", s: { i: 0 } },
    { cap: "The laptop retrieves it. With <b>POP3</b> the message is downloaded and normally removed from the server; with <b>IMAP</b> the server keeps it and the laptop shows a copy.", s: { i: 1 } },
    { cap: "Later the user checks the phone. With POP3 the email is not there (it was downloaded to the laptop). With IMAP the phone shows the same email, <b>in sync</b>.", s: { i: 2 } }] });
})();

(function () {
  const peers = [[0, 1, 2, 3, 4, 5], [0, 1, 2], [3, 4, 5], [0, 3], []];
  const names = ["Seed A", "Peer B", "Peer C", "Peer D", "Peer E"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    names.forEach((n, i) => { const y = 20 + i * 38; let have = peers[i].slice(); if (k >= 2 && i === 4) have = [0, 3, 4]; if (k >= 3 && i === 4) have = [0, 1, 2, 3, 4, 5]; o += SV.text(30, y + 22, n, "lbl bd", { style: "font-size:13px" }); for (let p = 0; p < 6; p++) o += SV.rect(130 + p * 52, y, 46, 30, have.includes(p) ? "f3" : "cell", { rx: 4, ...op(have.includes(p) ? 1 : 0.45) }) + SV.text(153 + p * 52, y + 20, "P" + (p + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" }); });
    if (k >= 1) o += SV.text(480, 40, "tracker: lists the swarm", "lbl bd", { style: "font-size:13px" }) + SV.text(480, 62, "A, B, C, D, E", "sm");
    if (k >= 2) o += SV.text(480, 110, "E asks several peers at once:", "lbl bd", { style: "font-size:13px" }) + SV.text(480, 132, "P1 from A, P4 from C, P5 from C...", "sm");
    if (k >= 3) o += SV.text(480, 170, "E now has the whole file: a new seed", "lbl bd t3", { style: "font-size:13px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "A BitTorrent swarm", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The file is split into six equal <b>pieces</b>. Seed A has them all; B, C and D have some. New peer E has none.", s: { i: 0 } },
    { cap: "E gets the <b>torrent file</b> and contacts the <b>tracker</b>, which tells it who is in the <b>swarm</b>.", s: { i: 1 } },
    { cap: "E downloads <b>different pieces from different peers at the same time</b>. Each piece it receives, it can share.", s: { i: 2 } },
    { cap: "E now has every piece. If it stays connected and shares, it is a <b>seed</b>. No central server held the file.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const P = ["HTTP/HTTPS", "FTP", "SMTP", "POP3", "IMAP", "BitTorrent"];
  const q = [["Your browser fetches a web page", 0], ["Sending an email from your client to a mail server", 2], ["Downloading emails to one device and removing them from the server", 3], ["Reading the same inbox, in sync, on a phone and a laptop", 4], ["Uploading a folder of files to a web server", 1], ["Downloading a large file in pieces from thousands of other users", 5]];
  let cur = 0, pick = null;
  const paint = () => {
    $$("#wB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const Q = q[cur]; $("#wO").innerHTML = `<p><b>${Q[0]}</b></p><div class="btnrow">` + P.map((p, i) => `<button class="b${pick === i ? " pri" : ""}" data-i="${i}">${p}</button>`).join("") + '</div><div class="verdict">' + (pick === null ? "Choose a protocol." : pick === Q[1] ? "Correct: " + P[Q[1]] + "." : "Not " + P[pick] + ". The best answer is " + P[Q[1]] + ".") + "</div>";
    $$("#wO button").forEach((b) => (b.onclick = () => { pick = +b.dataset.i; paint(); }));
  };
  $("#wB").innerHTML = q.map((x, i) => `<button class="b" data-i="${i}">Situation ${i + 1}</button>`).join("");
  $$("#wB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

/* Lab 2: swarm */
(function () {
  const N = 8, names = ["A (seed)", "B", "C", "D", "E", "F"]; let have, round, seed = 7;
  const rnd = () => { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; };
  const reset = () => { seed = 7; round = 0; have = names.map((_, i) => (i === 0 ? new Set([...Array(N).keys()]) : new Set())); paint("Press Next round."); };
  const paint = (msg) => {
    $("#tS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Peer</th>' + Array.from({ length: N }, (_, i) => `<th>P${i + 1}</th>`).join("") + "<th>Done?</th></tr>" + names.map((n, i) => "<tr><td>" + n + "</td>" + Array.from({ length: N }, (_, p) => `<td style="${have[i].has(p) ? "background:var(--good-soft)" : ""}">${have[i].has(p) ? "✓" : ""}</td>`).join("") + "<td>" + (have[i].size === N ? "seed" : have[i].size + "/" + N) + "</td></tr>").join("") + "</table></div>";
    $("#tV").textContent = msg;
  };
  $("#tN").onclick = () => {
    round++; const snap = have.map((h) => new Set(h)); let moved = 0;
    names.forEach((_, i) => { if (snap[i].size === N) return; const need = [...Array(N).keys()].filter((p) => !snap[i].has(p)); const options = []; need.forEach((p) => names.forEach((_, j) => { if (j !== i && snap[j].has(p)) options.push(p); })); if (options.length) { have[i].add(options[Math.floor(rnd() * options.length)]); moved++; } });
    const done = have.every((h) => h.size === N);
    paint(done ? "Round " + round + ": every peer has the whole file and can seed it. No server held the file." : "Round " + round + ": " + moved + " pieces were downloaded from other peers. Every piece a peer receives it can pass on.");
  };
  $("#tR").onclick = reset; reset();
})();

btnTable("eB", "eO", [
  ["HTTP / HTTPS", "Web pages / hypertext documents", "Browser requests, server responds; HTTPS is secure", "Sending and receiving web pages"],
  ["FTP", "Files between devices", "Upload and download to a server", "Sending and receiving files"],
  ["SMTP", "Sending email", "Push: client to server, server to server", "Sending / uploading emails"],
  ["POP3", "Receiving email", "Pull: download from the server, normally removed", "Receiving / downloading emails"],
  ["IMAP", "Receiving email", "Pull: any device, server copy kept, in sync", "Access email from any device"],
  ["BitTorrent", "Peer-to-peer file sharing", "Torrent file, tracker, swarm, pieces, seeds", "Sharing files peer to peer"]
], ["Protocol", "Purpose", "Key points", "Exam wording"]);
Lib.classify($("#cl1"), { prompt: "Which protocol is described?", buckets: [{"label": "HTTP(S)"}, {"label": "FTP"}, {"label": "SMTP"}, {"label": "POP3 / IMAP"}, {"label": "BitTorrent"}], items: [{"text": "Transfers web pages between a server and a browser", "b": 0}, {"text": "Sends and receives files over a network", "b": 1}, {"text": "Sends email towards its destination", "b": 2}, {"text": "Retrieves email from a mail server", "b": 3}, {"text": "Peer-to-peer file sharing", "b": 4}, {"text": "Hypertext documents", "b": 0}, {"text": "Reads email from any device without removing it from the server", "b": 3}, {"text": "Uses a tracker, a swarm and pieces of a file", "b": 4}], done: "Web pages: HTTP. Files: FTP. Sending mail: SMTP. Receiving mail: POP3/IMAP. Peer to peer: BitTorrent." });
Lib.classify($("#cl2"), { prompt: "Is it a push or a pull protocol?", buckets: [{"label": "Push"}, {"label": "Pull"}], items: [{"text": "SMTP", "b": 0}, {"text": "POP3", "b": 1}, {"text": "IMAP", "b": 1}, {"text": "Sending an email to the mail server", "b": 0}, {"text": "Retrieving emails from the mail server", "b": 1}, {"text": "Delivering mail between mail servers", "b": 0}], done: "SMTP pushes mail out. POP3 and IMAP pull mail in." });
Lib.order($("#o1"), { prompt: "Put the journey of an email in order.", items: ["The sender's email client pushes the message to its mail server with SMTP", "That mail server passes it to the recipient's mail server with SMTP", "The recipient's mail server stores it in their mailbox", "The recipient's client retrieves it with POP3 or IMAP"], done: "Client, server, server, mailbox, retrieve." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["HTTP", "Transferring hypertext documents"], ["SMTP", "Sending email towards its destination"], ["IMAP", "Reading email on any device, in sync with the server"], ["BitTorrent", "Peer-to-peer file sharing"], ["FTP", "Sending and receiving files over a network"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A file is split into 20 equal pieces. A peer has 12. How many more does it need?", "a": 8, "unit": "", "tol": 0.01, "hint": "20 − 12.", "sol": "<b>8</b>."},
  {"q": "A 600 MB file is split into pieces of 2 MB. How many pieces?", "a": 300, "unit": "", "tol": 0.01, "hint": "600 ÷ 2.", "sol": "<b>300</b>."},
  {"q": "How many protocols are used when an email is sent from one client and read on another using IMAP (count each protocol name once: SMTP, IMAP)?", "a": 2, "unit": "", "tol": 0.01, "hint": "SMTP and IMAP.", "sol": "<b>2</b>."},
  {"q": "A user has 3 devices and uses IMAP. On how many devices can they read the same message?", "a": 3, "unit": "", "tol": 0.01, "hint": "All devices see the server's copy.", "sol": "<b>3</b>."},
  {"q": "A user has 3 devices and uses POP3 with default settings. On how many devices will the message be downloaded?", "a": 1, "unit": "", "tol": 0.01, "hint": "The first to download it; it is then removed.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which protocol sends email?", opts: ["POP3", "IMAP", "SMTP", "FTP"], a: 2, why: "SMTP." },
  { q: "Which protocol lets you read email on any device without removing it from the server?", opts: ["IMAP", "SMTP", "HTTP", "FTP"], a: 0, why: "IMAP." },
  { q: "What does HTTP transfer?", opts: ["Email", "Hypertext documents (web pages)", "Peer-to-peer files", "MAC addresses"], a: 1, why: "Web pages." },
  { q: "In BitTorrent there is...", opts: ["a central server holding the file", "no central server holding the file: users share pieces", "only one source", "no tracker or swarm"], a: 1, why: "Peer to peer." },
  { q: "FTP is used for...", opts: ["sending and receiving files", "reading email", "web browsing only", "routing"], a: 0, why: "File transfer." },
  { q: "A peer with the complete file that keeps sharing it is called...", opts: ["a tracker", "a seed", "a router", "a swarm"], a: 1, why: "A seed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["HTTP(S)", "Web pages / hypertext documents."],
  ["FTP", "Sending and receiving files."],
  ["SMTP", "Sending email (push)."],
  ["POP3", "Receiving email (pull); downloaded."],
  ["IMAP", "Receiving email (pull); any device, in sync."],
  ["BitTorrent", "Peer-to-peer file sharing."],
  ["Tracker", "Holds data about the peers in the swarm."],
  ["Seed", "A peer with the whole file that shares it."],
] });
