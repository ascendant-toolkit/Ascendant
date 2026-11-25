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

const PROT = [];

PROT.push(...[
  ["HTTP(S)", "Web pages", "Client and server", "A web page", "Pull (the browser asks)", "Stays on the server", "Opening a website"],
  ["FTP", "Files", "Client and server", "Files, in either direction", "Client uploads or downloads", "Stays on the server unless deleted", "Uploading a website's files"],
  ["SMTP", "Sending email", "Client to server, server to server", "An outgoing email", "Push", "Delivered onward to the recipient's server", "Pressing Send"],
  ["POP3", "Receiving email", "Client and server", "Mail downloaded to the device", "Pull", "Normally removed from the server", "A desktop mail program"],
  ["IMAP", "Receiving email", "Client and server", "Mail viewed on any device", "Pull", "Stays on the server", "A phone and laptop in sync"],
  ["BitTorrent", "Peer-to-peer file sharing", "Peers, no central server", "Pieces of a file", "Pieces from many peers", "Each peer keeps and shares its pieces", "Downloading a large file"]]);
const PH = ["Protocol", "Used for", "Model", "Carries", "Push or pull", "Where the data ends up", "Example"];

(function () {
  const A = [["Email client", 20], ["Sender's server", 215], ["Recipient's server", 410], ["Recipient's client", 610]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    A.forEach((a, i) => (o += SV.rect(a[1], 50, 130, 50, i === 0 || i === 3 ? "f1" : "f3", { rx: 8, ...op(0.8) }) + SV.text(a[1] + 65, 80, a[0], "sm bd", { "text-anchor": "middle" })));
    const seg = (i, lbl, cls, a, b, v) => { const x1 = A[a][1] + 130, x2 = A[b][1]; return k >= v ? (x2 > x1 ? arrow(x1, 75, x2, 75, "r", cls, 1) : arrow(A[a][1], 75, A[b][1] + 110, 75, "l", cls, 1)) + SV.text((x1 + x2) / 2, 66, lbl, "sm bd", { "text-anchor": "middle", ...halo }) : ""; };
    o += seg(0, "SMTP", "c1", 0, 1, 1) + seg(1, "SMTP", "c1", 1, 2, 2);
    if (k >= 3) o += SV.rect(410, 110, 130, 34, "cell-ok", { rx: 6 }) + SV.text(475, 133, "mailbox", "sm", { "text-anchor": "middle" });
    if (k >= 4) o += arrow(610, 150, 540, 150, "l", "c3", 1) + SV.text(575, 168, "asks for mail", "sm", { "text-anchor": "middle" });
    if (k >= 5) o += arrow(540, 128, 610, 128, "r", "c3", 1) + SV.text(575, 120, "POP3 / IMAP", "sm bd", { "text-anchor": "middle", ...halo });
    o += SV.text(30, 200, k <= 2 ? "SMTP pushes the message towards its destination" : k >= 4 ? "POP3 and IMAP pull the message from the server" : "The message waits in the recipient's mailbox", "lbl bd", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stM"), { w: 760, h: 215, label: "SMTP sends, POP3 and IMAP receive", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "A user has written an email and presses Send.", s: { i: 0 } },
    { cap: "The email client uses <b>SMTP</b> to push the message to the sender's mail server.", s: { i: 1 } },
    { cap: "That server uses <b>SMTP</b> to push it on to the recipient's mail server.", s: { i: 2 } },
    { cap: "The message sits in the recipient's <b>mailbox</b> on their mail server.", s: { i: 3 } },
    { cap: "Later the recipient's client <b>asks</b> the server for new mail. This is a <b>pull</b>.", s: { i: 4 } },
    { cap: "<b>POP3</b> or <b>IMAP</b> delivers the message to the client.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const dev = (x, y, n, got, gone) => SV.rect(x, y, 76, 40, got ? "cell-ok" : "cell", { rx: 8 }) + SV.text(x + 38, y + 25, n + (got ? " ✓" : ""), "sm bd", { "text-anchor": "middle" });
    const side = (x, title, mode) => {
      let t = SV.text(x + 120, 20, title, "lbl bd", { "text-anchor": "middle" });
      t += SV.rect(x + 45, 40, 150, 46, k >= 1 && !(mode === "pop" && k >= 2) ? "cell-warn" : "cell", { rx: 8 }) + SV.text(x + 120, 68, k >= 1 && !(mode === "pop" && k >= 2) ? "Server: 1 message" : "Server: empty", "sm bd", { "text-anchor": "middle" });
      const have = (i) => mode === "imap" ? k >= 2 : k >= 2 && i === 0;
      ["Phone", "Tablet", "Laptop"].forEach((n, i) => (t += SV.line(x + 120, 86, x + 43 + i * 80, 130, "ax", op(k >= 2 ? 0.9 : 0.25)) + dev(x + 5 + i * 80, 130, n, have(i))));
      return t;
    };
    return side(20, "POP3", "pop") + side(400, "IMAP", "imap");
  };
  Lib.stepper($("#stI"), { w: 760, h: 190, label: "POP3 and IMAP with three devices", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "The user has three devices and no new mail.", s: { i: 0 } },
    { cap: "A message arrives on the mail server.", s: { i: 1 } },
    { cap: "<b>POP3</b>: the first device that checks downloads the message and, by default, it is <b>removed from the server</b>, so only that device has it. <b>IMAP</b>: the message <b>stays on the server</b> and all three devices show it.", s: { i: 2 } }] });
})();

(function () {
  const peers = [[400, 40], [560, 90], [560, 190], [400, 240], [240, 190], [240, 90]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    if (k <= 1) { o += SV.rect(30, 110, 110, 60, "f2", { rx: 10, ...op(0.8) }) + SV.text(85, 145, "Server", "lbl bd", { "text-anchor": "middle" }); [[290, 30], [290, 100], [290, 170], [290, 240]].forEach((c, i) => (o += SV.rect(c[0], c[1], 100, 36, "f1", { rx: 8, ...op(0.8) }) + SV.text(c[0] + 50, c[1] + 24, "Client " + (i + 1), "sm bd", { "text-anchor": "middle" }) + (k === 1 ? arrow(140, 140, c[0], c[1] + 18, "r", "c1", 1) : ""))); o += SV.text(430, 150, k === 1 ? "Everyone downloads from one server" : "One server holds the file", "lbl bd", { style: "font-size:14px" }); }
    else { peers.forEach((p, i) => peers.forEach((q, j) => { if (j > i && (k === 3 || (j - i) % 2 === 1)) o += SV.line(p[0] + 20, p[1] + 20, q[0] + 20, q[1] + 20, "c3", { "stroke-width": 1.8, ...op(0.6) }); })); peers.forEach((p, i) => (o += SV.circle(p[0] + 20, p[1] + 20, 24, i === 0 ? "dot4" : "dot1", op(0.9)) + SV.text(p[0] + 20, p[1] + 25, i === 0 ? "Seed" : "Peer", "sm bd", { "text-anchor": "middle", style: "fill:#fff" }))); o += SV.text(30, 130, k === 2 ? "A seed holds the whole file" : "Peers swap pieces", "lbl bd", { style: "font-size:14px" }); if (k === 3) o += SV.text(30, 156, "No central server holds the file", "sm"); }
    return o;
  };
  Lib.stepper($("#stS"), { w: 760, h: 285, label: "Client and server compared with a BitTorrent swarm", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "<b>HTTP and FTP</b> are client and server: a central server holds the file.", s: { i: 0 } },
    { cap: "Every client downloads from the same server, so that server carries the whole load.", s: { i: 1 } },
    { cap: "<b>BitTorrent</b>: the file is split into pieces. A <b>seed</b> has the whole file, and a <b>tracker</b> tells peers who else is in the swarm.", s: { i: 2 } },
    { cap: "Each <b>peer</b> downloads pieces from several others and passes on the pieces it has. There is <b>no central server</b> holding the file.", s: { i: 3 } }] });
})();

(function () {
  const T = {
    q0: { q: "Is it email?", y: "q1", n: "q2" }, q1: { q: "Is the message being sent?", y: "SMTP", n: "q3" }, q3: { q: "Must the message stay on the server so several devices see it?", y: "IMAP", n: "POP3" },
    q2: { q: "Is it a web page shown in a browser?", y: "HTTP(S)", n: "q4" }, q4: { q: "Is the file shared by many users with no central server holding it?", y: "BitTorrent", n: "FTP" } };
  const WHY = { "SMTP": "SMTP sends email and pushes it towards its destination.", "IMAP": "IMAP leaves mail on the server so every device stays in sync.", "POP3": "POP3 downloads mail to one device and normally removes it from the server.", "HTTP(S)": "HTTP(S) transfers web pages between a web server and a browser.", "BitTorrent": "BitTorrent shares pieces of a file peer to peer, with no central server holding it.", "FTP": "FTP sends and receives files between a client and a server." };
  let path = ["q0"];
  const paint = () => {
    const cur = path[path.length - 1], t = T[cur];
    $("#tree").innerHTML = t ? `<p><b>${t.q}</b></p><div class="btnrow"><button class="b" data-a="y">Yes</button><button class="b" data-a="n">No</button><button class="b" data-a="r">Start again</button></div>` : `<div class="verdict ok"><b>${cur}</b>: ${WHY[cur]}</div><div class="btnrow"><button class="b" data-a="r">Start again</button></div>`;
    $$("#tree button").forEach((b) => (b.onclick = () => { const a = b.dataset.a; if (a === "r") path = ["q0"]; else path.push(T[cur][a]); paint(); }));
  };
  paint();
})();

(function () {
  let a = 0, b = 1;
  const opt = (id, v) => `<select id="${id}">${PROT.map((p, i) => `<option value="${i}"${i === v ? " selected" : ""}>${p[0]}</option>`).join("")}</select>`;
  const paint = () => {
    $("#cmp").innerHTML = `<p>${opt("cA", a)} against ${opt("cB", b)}</p><div class="tw"><table class="t"><tr><th></th><th>${PROT[a][0]}</th><th>${PROT[b][0]}</th><th></th></tr>` + PH.slice(1).map((h, i) => `<tr><td><b>${h}</b></td><td>${PROT[a][i + 1]}</td><td>${PROT[b][i + 1]}</td><td>${PROT[a][i + 1] === PROT[b][i + 1] ? "same" : "differs"}</td></tr>`).join("") + "</table></div>";
    $("#cA").onchange = (e) => { a = +e.target.value; paint(); }; $("#cB").onchange = (e) => { b = +e.target.value; paint(); };
  };
  paint();
})();

(function () {
  let dev = 3;
  const paint = () => {
    $("#pi").innerHTML = `<div id="piS"></div><div class="tw"><table class="t"><tr><th></th><th>POP3 (default)</th><th>IMAP</th></tr><tr><td><b>Devices that can read a new message</b></td><td id="pa"></td><td id="pb"></td></tr><tr><td><b>Copies kept on the server</b></td><td>0</td><td>1</td></tr></table></div>`;
    Lib.slider($("#piS"), { id: "dv", label: "Number of devices: ", min: 1, max: 6, value: dev, onInput: (n) => { dev = n; $("#pa").textContent = "1 (the first to download it)"; $("#pb").textContent = n + " (all of them)"; } });
  };
  paint();
})();
Lib.classify($("#cl1"), { prompt: "Which protocol is described?", buckets: [{"label": "HTTP(S)"}, {"label": "FTP"}, {"label": "SMTP"}, {"label": "POP3"}, {"label": "IMAP"}, {"label": "BitTorrent"}], items: [{"text": "Transfers web pages to a browser", "b": 0}, {"text": "Sends files to a web host", "b": 1}, {"text": "Sends an email", "b": 2}, {"text": "Downloads mail to one device and removes it from the server", "b": 3}, {"text": "Reads the same inbox on a phone and a laptop", "b": 4}, {"text": "Shares a large file in pieces among many users", "b": 5}, {"text": "Delivers mail between mail servers", "b": 2}, {"text": "Uses a tracker and seeds", "b": 5}], done: "Web pages: HTTP(S). Files: FTP. Sending mail: SMTP. Downloading: POP3. In sync: IMAP. Peer to peer: BitTorrent." });
Lib.classify($("#cl2"), { prompt: "Is the protocol used for sending or for receiving email?", buckets: [{"label": "Sending email"}, {"label": "Receiving email"}], items: [{"text": "SMTP", "b": 0}, {"text": "POP3", "b": 1}, {"text": "IMAP", "b": 1}, {"text": "Pushes mail towards its destination", "b": 0}, {"text": "Pulls mail from the mail server", "b": 1}, {"text": "Passes mail from one mail server to another", "b": 0}], done: "SMTP sends. POP3 and IMAP receive." });
Lib.classify($("#cl3"), { prompt: "Client and server, or peer to peer?", buckets: [{"label": "Client and server"}, {"label": "Peer to peer"}], items: [{"text": "HTTP", "b": 0}, {"text": "FTP", "b": 0}, {"text": "BitTorrent", "b": 1}, {"text": "Pieces come from many other users", "b": 1}, {"text": "A central server holds the file", "b": 0}, {"text": "A swarm of peers", "b": 1}], done: "HTTP and FTP use a server. BitTorrent shares pieces between peers." });
Lib.order($("#o1"), { prompt: "Put the journey of an email in order.", items: ["The sender's client pushes the message to its mail server with SMTP", "That mail server passes it to the recipient's mail server with SMTP", "The recipient's mail server stores it in their mailbox", "The recipient's client retrieves it with POP3 or IMAP"], done: "Client, server, server, mailbox, retrieve." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["HTTP", "Transferring hypertext documents"], ["FTP", "Sending and receiving files"], ["SMTP", "Sending email"], ["POP3", "Downloading email from a server"], ["IMAP", "Reading email on any device, in sync"], ["BitTorrent", "Peer-to-peer file sharing"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A file is split into 40 equal pieces and a peer has 25. How many more pieces does it need?", "a": 15, "unit": "", "tol": 0.01, "hint": "40 − 25.", "sol": "<b>15</b>."},
  {"q": "A 900 MB file is shared in pieces of 3 MB. How many pieces?", "a": 300, "unit": "", "tol": 0.01, "hint": "900 ÷ 3.", "sol": "<b>300</b>."},
  {"q": "A user has 4 devices and uses IMAP. On how many devices can they read the same message?", "a": 4, "unit": "", "tol": 0.01, "hint": "All of them.", "sol": "<b>4</b>."},
  {"q": "A user has 4 devices and uses POP3 with default settings. On how many devices will a message be downloaded?", "a": 1, "unit": "", "tol": 0.01, "hint": "The first to download it.", "sol": "<b>1</b>."},
  {"q": "An email passes from a client to its server and then to the recipient's server using SMTP. How many SMTP transfers?", "a": 2, "unit": "", "tol": 0.01, "hint": "Client to server, server to server.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which protocol is used to send email?", opts: ["POP3", "IMAP", "SMTP", "FTP"], a: 2, why: "SMTP." },
  { q: "Which protocol lets you read mail on any device and leaves it on the server?", opts: ["IMAP", "SMTP", "HTTP", "FTP"], a: 0, why: "IMAP." },
  { q: "Which protocol normally removes mail from the server after downloading?", opts: ["IMAP", "POP3", "SMTP", "HTTP"], a: 1, why: "POP3." },
  { q: "What does HTTP transfer?", opts: ["Email", "Web pages", "Peer-to-peer files", "MAC addresses"], a: 1, why: "Hypertext documents." },
  { q: "Which protocol sends and receives files to and from a server?", opts: ["FTP", "SMTP", "POP3", "HTTP"], a: 0, why: "FTP." },
  { q: "In BitTorrent there is...", opts: ["a central server holding the file", "no central server holding the file", "only one source", "no peers"], a: 1, why: "Peer to peer." },
  { q: "To which layer of the TCP/IP suite do all six belong?", opts: ["Application", "Transport", "Internet", "Link"], a: 0, why: "Application." },
  { q: "A peer with the complete file that keeps sharing it is called...", opts: ["a tracker", "a seed", "a router", "a swarm"], a: 1, why: "A seed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["HTTP(S)", "Web pages; S = secure."],
  ["FTP", "Sending and receiving files."],
  ["SMTP", "Sending email (push)."],
  ["POP3", "Receiving email; downloaded, removed from the server."],
  ["IMAP", "Receiving email; stays on the server, any device in sync."],
  ["BitTorrent", "Peer to peer file sharing in pieces."],
  ["Seed", "A peer with the whole file that shares it."],
  ["Tracker", "Holds data about the peers in the swarm."],
] });

(function () {
  const X = (m) => 90 + m * 40;
  const draw = (s) => {
    const k = Math.round(s.i);
    let o = SV.text(12, 49, "Client", "lbl bd") + SV.text(12, 169, "Server", "lbl bd") + SV.line(80, 45, 710, 45, "ax") + SV.line(80, 165, 710, 165, "ax");
    [[0, 1, "9:00", "No new mail"], [5, 2, "9:05", "No new mail"], [10, 4, "9:10", "Yes: 1 new"]].forEach(([m, at, t, reply]) => {
      if (k < at) return;
      o += SV.line(X(m), 52, X(m), 158, "c1") + SV.text(X(m), 28, t + " any mail?", "lbl", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(X(m) + 8, 110, reply, "lbl bd", { style: "font-size:13px" });
    });
    if (k >= 3) o += SV.rect(X(7) - 7, 158, 14, 14, "f3", { rx: 3 }) + SV.text(X(7), 195, "9:07 email arrives and waits", "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    return o;
  };
  Lib.stepper($("#stPoll"), { w: 760, h: 210, label: "A client polling a mail server", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The email client is set to check its mail server every 5 minutes.", s: { i: 0 } },
    { cap: "9:00. The client connects and asks for new mail. There is none.", s: { i: 1 } },
    { cap: "9:05. The client asks again. Still nothing.", s: { i: 2 } },
    { cap: "9:07. An email arrives at the server by SMTP. In a pull protocol the server holds it until the client asks.", s: { i: 3 } },
    { cap: "9:10. The next check finds the email and the client retrieves it with POP3 or IMAP. It waited 3 minutes.", s: { i: 4 } }] });
})();

(function () {
  const stages = [["Compose", "text + photo"], ["MIME", "headers, Base64"], ["SMTP", "send"], ["POP3 / IMAP", "retrieve"], ["MIME", "decode, open"]];
  const detail = [["Message: Here is the photo.", "Attachment: trip.jpg (binary)"], ["Content-Type: image/jpeg", "binary becomes text: /9j/4AAQ..."], ["The all-text message travels to", "the recipient's mail server"],
    ["The recipient's client pulls", "the message from the server"], ["Base64 text becomes bytes again", "and the photo opens"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    stages.forEach((t, i) => { const x = 8 + i * 150; o += SV.rect(x, 20, 136, 62, i === k ? "f3" : "cell", { rx: 8, ...op(i <= k ? 1 : 0.5) }) + SV.text(x + 68, 46, t[0], "lbl bd", { "text-anchor": "middle", style: "font-size:14px" }) + SV.text(x + 68, 68, t[1], "sm", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.rect(150, 112, 460, 72, "cell", { rx: 8 }) + detail[k].map((l, j) => SV.text(380, 142 + j * 24, l, "lbl", { "text-anchor": "middle", style: "font-size:14px" })).join("");
    return o;
  };
  Lib.stepper($("#stMime"), { w: 760, h: 200, label: "An email attachment with MIME", base: { i: 0 }, draw, tween: 250, dwell: 3400, steps: [
    { cap: "You write a message and attach a photo. The photo is binary data.", s: { i: 0 } },
    { cap: "The email client adds MIME headers and encodes the photo as Base64 text.", s: { i: 1 } },
    { cap: "<b>SMTP</b> pushes the message to the recipient's mail server.", s: { i: 2 } },
    { cap: "The recipient's client <b>pulls</b> it with POP3 or IMAP.", s: { i: 3 } },
    { cap: "The client reads the MIME headers, decodes the Base64 and opens the photo.", s: { i: 4 } }] });
})();

(function () {
  let every = 5, arrive = 7;
  const paint = () => {
    const next = Math.ceil(arrive / every) * every, wait = next - arrive;
    $("#poV").textContent = `The email arrives at minute ${arrive}. The next check is at minute ${next}, so it waits ${wait} minute${wait === 1 ? "" : "s"}. Checking every ${every} minute${every === 1 ? "" : "s"} makes ${Math.floor(1440 / every)} checks a day.`;
  };
  Lib.slider($("#poI"), { id: "poi", label: "Check the server every (minutes) ", min: 1, max: 30, value: every, onInput: (v) => { every = v; paint(); } });
  Lib.slider($("#poA"), { id: "poa", label: "Email arrives at minute ", min: 1, max: 60, value: arrive, onInput: (v) => { arrive = v; paint(); } });
})();

Lib.match($("#m2"), {"prompt": "Match the key word to its meaning.", "pairs": [["Push protocol", "The sender starts the transfer"], ["Pull protocol", "The receiving client asks for the data"], ["Polling", "Checking a server at set intervals"], ["MIME", "Lets email carry attachments"], ["Base64", "Writes binary data as safe text characters"], ["Tracker", "Holds data about the peers in a swarm"]], "done": "Use these words in your answers."});
