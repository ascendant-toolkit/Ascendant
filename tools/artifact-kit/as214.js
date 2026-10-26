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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.circle(300, 110, 100, "ax", { fill: "none", style: "stroke:var(--accent);stroke-width:3" }) + SV.text(300, 24, "The internet (infrastructure)", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.circle(300, 120, 56, "f1", {}) + SV.text(300, 125, "WWW", "lbl bd", { "text-anchor": "middle" }) + SV.text(300, 143, "web pages, browser", "sm", { "text-anchor": "middle" });
    if (k >= 2) [["email", 180, 105], ["file transfer", 180, 150], ["streaming", 420, 105], ["voice calls", 420, 150]].forEach(([t, x, y]) => (o += SV.rect(x - 52, y - 14, 104, 28, "cell", { rx: 6 }) + SV.text(x, y + 5, t, "lbl", { "text-anchor": "middle", style: "font-size:12px" })));
    if (k >= 3) o += SV.text(300, 238, "webmail uses the WWW (a website) and the internet (the data crosses it)", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 250, label: "Internet and WWW", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The <b>internet</b> is the global network of networks: the infrastructure.", s: { i: 0 } }, { cap: "The <b>World Wide Web</b> is one service that runs on it: web pages and resources.", s: { i: 1 } }, { cap: "Other services also use the internet: email, file transfer, streaming and voice calls.", s: { i: 2 } }, { cap: "Webmail is both: a website (WWW) and data crossing the internet.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 130, 70, "f3", { rx: 10 }) + SV.text(85, 70, "Media server", "lbl bd", { "text-anchor": "middle" }) + SV.text(85, 92, "(compressed video)", "sm", { "text-anchor": "middle" }) + SV.rect(240, 55, 140, 40, "cell", { rx: 6 }) + SV.text(310, 80, "buffer", "lbl bd", { "text-anchor": "middle" }) + SV.rect(470, 40, 110, 70, "cell", { rx: 10 }) + SV.text(525, 80, "Player", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M150,75 H240", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(195, 62, "bits", "sm", { "text-anchor": "middle" }); if (k >= 2) { for (let i = 0; i < 5; i++) o += SV.rect(250 + i * 25, 66, 20, 18, "f1", {}); } if (k >= 3) o += SV.path("M380,75 H470", "ax", { style: "stroke:var(--good);stroke-width:3" }) + SV.text(425, 62, "plays", "sm", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(300, 150, "arrival slower than playback: buffer empties and the video pauses", "lbl bd t2", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 170, label: "Streaming", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "The video is compressed and stored (or uploaded live) on a <b>media server</b>.", s: { i: 0 } }, { cap: "The server sends a <b>continuous stream of bits</b>.", s: { i: 1 } }, { cap: "The bits go into a <b>buffer</b> on the receiving device, which holds them until the device can process them.", s: { i: 2 } }, { cap: "The player takes data from the buffer and plays it while more arrives.", s: { i: 3 } }, { cap: "If the connection is too slow, the buffer empties and playback <b>pauses to buffer</b>.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 50, 120, 60, "cell", { rx: 8 }) + SV.text(80, 85, "Computer", "lbl bd", { "text-anchor": "middle" }) + SV.rect(190, 50, 100, 60, "f3", { rx: 8 }) + SV.text(240, 85, "Modem", "lbl bd", { "text-anchor": "middle" }) + SV.rect(340, 40, 140, 80, "f1", { rx: 10 }) + SV.text(410, 70, "PSTN", "lbl bd", { "text-anchor": "middle" }) + SV.text(410, 92, "switching centres", "sm", { "text-anchor": "middle" }) + SV.rect(520, 50, 70, 60, "cell", { rx: 8 }) + SV.text(555, 85, "ISP", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.text(80, 140, "digital data", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.text(240, 140, "→ analogue signal", "sm", { "text-anchor": "middle" }); if (k >= 3) o += SV.path("M290,80 H340", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.path("M480,80 H520", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(410, 140, "many types of line; both directions at once", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 165, label: "Modem and PSTN", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "A computer wants to send data over a telephone line.", s: { i: 0 } }, { cap: "The data is <b>digital</b>.", s: { i: 1 } }, { cap: "The <b>modem</b> converts it into an <b>analogue</b> signal for the phone line (and back at the other end).", s: { i: 2 } }, { cap: "The signal crosses the <b>PSTN</b>: many types of line, different switching centres, data in both directions at once, to the ISP.", s: { i: 3 } }] });
})();

(function () {
  let rate = 5, speed = 4;
  const paint = () => { const T = 30, pts = []; let buf = 3; for (let t = 0; t <= T; t++) { pts.push(buf); buf = Math.max(0, Math.min(10, buf + (speed - rate) / Math.max(rate, 1))); } let o = '<path d="M40,20 V150 H400" class="ax"/>'; let d = ""; pts.forEach((p, i) => (d += (i ? "L" : "M") + (40 + i * 12) + "," + (150 - p * 12) + " ")); o += `<path d="${d}" fill="none" stroke="${speed >= rate ? "var(--good)" : "var(--bad)"}" stroke-width="3"/>`;
    o += '<text x="46" y="16" class="sm" style="font-size:11px">buffer level (seconds of video)</text><text x="400" y="166" class="sm" text-anchor="end" style="font-size:11px">time (30 s)</text>';
    $("#vG").innerHTML = `<svg viewBox="0 0 420 175" style="width:420px;max-width:100%;display:block">${o}</svg>`; const stalls = pts.filter((p) => p <= 0.01).length;
    $("#vV").innerHTML = speed >= rate ? `The connection (<b>${speed} Mbps</b>) is at least the video's bit rate (<b>${rate} Mbps</b>): the buffer stays full and the video plays smoothly.` : `The connection (<b>${speed} Mbps</b>) is slower than the video's bit rate (<b>${rate} Mbps</b>): the buffer drains${stalls ? " and the video <b>pauses to buffer</b>" : ""}. Use a faster connection, or compress the video more.`; };
  Lib.slider($("#vR"), { id: "vr", label: "Video bit rate (Mbps) ", min: 1, max: 20, value: rate, fmt: (x) => x, onInput: (v) => { rate = v; paint(); } });
  Lib.slider($("#vS"), { id: "vs", label: "Connection speed (Mbps) ", min: 1, max: 20, value: speed, fmt: (x) => x, onInput: (v) => { speed = v; paint(); } }); paint();
})();
btnTable("iB", "iO", [
  ["Browsing a company's web pages", "Both", "A website (WWW) delivered across the internet"],
  ["Sending email from a mail program", "Internet", "Data crosses the internet; no web page needed"],
  ["Using webmail in a browser", "Both", "A website (WWW) and data across the internet"],
  ["Transferring a file with FTP", "Internet", "A service on the internet, not a web page"],
  ["Reading a wiki article", "Both", "A web page found by URL, carried by the internet"],
  ["A video call", "Internet", "Streams over the internet, not web pages"]
], ["Activity", "Uses", "Why"]);
btnTable("rB", "rO", [
  ["A live football match", "Real-time", "Sent as it happens; cannot be paused"],
  ["Watching last week's lesson recording", "On-demand", "Stored on a media server; pause and rewind"],
  ["A team video meeting", "Real-time", "Heavy compression so nobody is behind"],
  ["A film on a streaming service", "On-demand", "Buffer fills ahead of the viewing point"],
  ["A live concert broadcast", "Real-time", "Lossy compression to use less bandwidth"],
  ["Catch-up TV", "On-demand", "A stored file chosen by the viewer"]
], ["Situation", "Type", "Reason"]);
Lib.classify($("#cl1"), { prompt: "Does it describe the internet or the World Wide Web?", buckets: [{"label": "Internet"}, {"label": "World Wide Web"}], items: [{"text": "A global network of networks", "b": 0}, {"text": "Web pages found with URLs in a browser", "b": 1}, {"text": "The physical infrastructure of cables and routers", "b": 0}, {"text": "A service that runs on the internet", "b": 1}, {"text": "Also carries email and file transfer", "b": 0}, {"text": "Uses HTTP or HTTPS", "b": 1}], done: "Internet: infrastructure. Web: a service on it." });
Lib.classify($("#cl2"), { prompt: "Is it real-time or on-demand streaming?", buckets: [{"label": "Real-time"}, {"label": "On-demand"}], items: [{"text": "A live video conference", "b": 0}, {"text": "A film you choose to watch tonight", "b": 1}, {"text": "Can be paused and rewound", "b": 1}, {"text": "Sent as it happens, not stored", "b": 0}, {"text": "Played from a file on a media server", "b": 1}, {"text": "Viewers must see it at the same moment", "b": 0}], done: "Real-time is live; on-demand is stored." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Bit streaming", "A continuous flow of bits played as it arrives"], ["Buffer", "Stores data until the device can process it"], ["Modem", "Converts digital to analogue and back"], ["PSTN", "The public telephone network with many line types and switching centres"], ["Dedicated line", "A direct private connection"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of bit streaming in order.", items: ["The video is compressed", "It is uploaded to a media server", "The server sends it to the user as a stream of bits", "It is stored in a buffer on the user's device", "The player plays it from the buffer"], done: "Compress, upload, stream, buffer, play." });
Lib.calc($("#c1"), { qs: [
  {"q": "A video needs 5 Mbps. The connection gives 8 Mbps. Does it need to pause to buffer? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "8 is more than 5.", "sol": "<b>0</b>."},
  {"q": "The same video on a 3 Mbps connection. How many Mbps short is it?", "a": 2, "unit": "Mbps", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b> Mbps."},
  {"q": "A film file is 600 MB. At 8 MB per second how many seconds does it take to download completely?", "a": 75, "unit": "s", "tol": 0.5, "hint": "600 ÷ 8.", "sol": "<b>75</b> s."},
  {"q": "A video of 24 Mbps is compressed to a third of its size. What is the new bit rate in Mbps?", "a": 8, "unit": "Mbps", "tol": 0.01, "hint": "24 ÷ 3.", "sol": "<b>8</b> Mbps."},
  {"q": "How many services are named as using the internet in the table (web, email, file transfer, streaming, voice calls)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The WWW is:", opts: ["The whole internet", "A service that uses the internet", "A cable", "A router"], a: 1, why: "A service." },
  { q: "What does a buffer do in streaming?", opts: ["Stores data until the device can process it", "Compresses data", "Encrypts data", "Prints data"], a: 0, why: "Stores data." },
  { q: "Which compression suits real-time streaming?", opts: ["Lossy", "Lossless only", "None", "Encryption"], a: 0, why: "Lossy, for the bandwidth." },
  { q: "A modem converts:", opts: ["Digital to analogue and back", "Text to images", "Light to sound", "Files to paper"], a: 0, why: "Digital and analogue." },
  { q: "Webmail uses:", opts: ["Only the internet", "Only the web", "Both the internet and the WWW", "Neither"], a: 2, why: "Both." },
  { q: "A dedicated line is:", opts: ["A direct private connection", "A shared public link", "A radio wave", "A browser"], a: 0, why: "A direct private connection." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Internet", "Global network of networks."],
  ["WWW", "Web pages on the internet; browser, URL."],
  ["Bit streaming", "Continuous bits, played as they arrive."],
  ["Buffer", "Holds data until it can be played."],
  ["Real-time", "Live; played immediately."],
  ["On-demand", "Stored; played when chosen."],
  ["Modem", "Digital to analogue and back."],
  ["PSTN", "Telephone network; switching centres; duplex."],
] });
