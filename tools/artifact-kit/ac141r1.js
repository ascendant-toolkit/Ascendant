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


const SC = [
  { n: "Loading a web page", d: ["HTTPS request: GET /timetable", "Numbered packets #1, #2, #3…", "192.168.1.20 → 203.0.113.10", "Wi-Fi frame: laptop → router"],
    c: ["Maya opens her school's website on her laptop.", "<b>Application:</b> the browser creates an HTTPS request for the timetable page.", "<b>Transport:</b> the reply will be sent as numbered packets; the request is wrapped with a sequence number and port.", "<b>Internet:</b> adds her laptop's IP address (192.168.1.20) and the school server's (203.0.113.10).", "<b>Link:</b> makes a Wi-Fi frame addressed to the home router, the next hop.", "The frames cross the network. Each router makes a new frame for its next hop; the IP addresses stay the same.", "<b>Link</b> on the school server receives the frame.", "<b>Internet:</b> checks the destination IP address is its own and passes the packet up.", "<b>Transport:</b> puts the packets in order using the sequence numbers and asks for any that are missing.", "<b>Application:</b> the web server receives the request and sends back the page, which travels the same four layers in reverse."] },
  { n: "Sending an email", d: ["SMTP: the message text", "Numbered packets, all must arrive", "10.0.0.8 → 198.51.100.25", "Ethernet frame: PC → router"],
    c: ["A teacher sends an email from an office PC.", "<b>Application:</b> the email client uses SMTP to hand the message to the mail server.", "<b>Transport:</b> splits the message into numbered packets and makes sure they all arrive.", "<b>Internet:</b> adds the IP addresses of the PC and the mail server.", "<b>Link:</b> puts each packet in an Ethernet frame to the office router.", "The frames cross the network to the mail server.", "<b>Link:</b> the mail server's network card receives the frames.", "<b>Internet:</b> confirms the destination IP address and passes the packets up.", "<b>Transport:</b> reorders the packets and requests any that are missing.", "<b>Application:</b> the mail server receives the complete message and stores it for the recipient."] },
  { n: "Video call", d: ["Audio and video data", "Small packets; late ones skipped", "192.168.1.20 → 203.0.113.55", "Wi-Fi frames → router"],
    c: ["Two friends start a video call.", "<b>Application:</b> the call app captures audio and video and prepares it for sending.", "<b>Transport:</b> sends small numbered packets quickly. For a live call a late packet is skipped rather than re-sent.", "<b>Internet:</b> adds the IP addresses of both callers.", "<b>Link:</b> sends Wi-Fi frames to the home router.", "The frames cross the network; each router makes a new frame for its next hop.", "<b>Link:</b> the other caller's device receives the frames.", "<b>Internet:</b> confirms the address and passes the packets up.", "<b>Transport:</b> uses the sequence numbers to play packets in order.", "<b>Application:</b> the call app shows the video and plays the sound."] },
  { n: "Uploading homework (FTP)", d: ["FTP: store homework.zip", "Numbered packets, all must arrive", "10.0.0.8 → 192.0.2.40", "Ethernet frame: PC → router"],
    c: ["A student uploads a file to their school's FTP server.", "<b>Application:</b> the FTP client sends the file using the FTP protocol.", "<b>Transport:</b> splits the file into numbered packets and makes sure every one arrives.", "<b>Internet:</b> adds the IP addresses of the PC and the FTP server.", "<b>Link:</b> puts the packets in Ethernet frames for the router.", "The frames cross the network.", "<b>Link:</b> the FTP server's network card receives the frames.", "<b>Internet:</b> passes the packets up after checking the address.", "<b>Transport:</b> reorders the packets and requests any missing ones.", "<b>Application:</b> the FTP server saves the complete file."] },
  { n: "Streaming a film", d: ["HTTPS: next video chunk", "Ordered packets, lost ones re-sent", "203.0.113.80 → 100.64.0.9", "Mobile data frames → phone"],
    c: ["A phone on mobile data streams a film.", "<b>Application:</b> the streaming app asks for the next piece of video over HTTPS.", "<b>Transport:</b> the server's reply is split into numbered packets and lost ones are re-sent.", "<b>Internet:</b> adds the IP addresses of the streaming server and the phone.", "<b>Link:</b> mobile network frames carry the data to the phone.", "The frames cross the internet and the mobile network.", "<b>Link:</b> the phone's radio receives the frames.", "<b>Internet:</b> checks the address and passes the packets up.", "<b>Transport:</b> puts the packets in order and asks for any missing.", "<b>Application:</b> the app buffers the video and plays it."] },
  { n: "BitTorrent download", d: ["BitTorrent: request piece #17", "Numbered packets", "192.168.1.20 → 203.0.113.99", "Wi-Fi frames → router"],
    c: ["A student downloads a large file from other users with BitTorrent.", "<b>Application:</b> the BitTorrent client asks a peer for piece number 17 of the file.", "<b>Transport:</b> splits the request and reply into numbered packets.", "<b>Internet:</b> adds the IP addresses of the two peers (no central web server is involved).", "<b>Link:</b> Wi-Fi frames to the home router.", "The frames cross the internet to the other peer.", "<b>Link:</b> the peer's network card receives the frames.", "<b>Internet:</b> passes the packets up.", "<b>Transport:</b> reorders the packets of the piece.", "<b>Application:</b> the peer's client sends back the piece, and the download client checks and keeps it."] }];
const LN = ["Application", "Transport", "Internet", "Link"], LC = ["f1", "f2", "f3", "f4"];

(function () {
  let cur = 0;
  const make = () => {
    const sc = SC[cur];
    const draw = (s) => {
      const k = Math.round(s.i); let o = SV.text(120, 20, "Sender", "lbl bd", { "text-anchor": "middle" }) + SV.text(640, 20, "Receiver", "lbl bd", { "text-anchor": "middle" });
      const stack = (x, side) => LN.map((n, i) => {
        const active = side === "s" ? k === i + 1 : k === 9 - i, shown = side === "s" ? k >= i + 1 : k >= 9 - i;
        return SV.rect(x, 32 + i * 62, 240, 54, active ? "cell-warn" : LC[i], { rx: 8, ...op(active ? 1 : shown ? 0.85 : 0.4) }) + SV.text(x + 12, 52 + i * 62, n, "lbl bd") + (shown ? SV.text(x + 12, 72 + i * 62, sc.d[i].length > 38 ? sc.d[i].slice(0, 36) + "…" : sc.d[i], "sm", {}) : "");
      }).join("");
      o += stack(0, "s") + stack(520, "r");
      o += SV.line(250, 160, 510, 160, "dash", op(k === 5 ? 1 : 0.3)) + SV.text(380, 152, k === 5 ? "frames cross the network" : "network and routers", "sm", { "text-anchor": "middle" });
      return o;
    };
    Lib.stepper($("#scS"), { w: 760, h: 292, label: sc.n + " through the four layers", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: sc.c.map((cap, i) => ({ cap, s: { i } })) });
  };
  $("#scB").innerHTML = SC.map((s, i) => `<button class="b" data-i="${i}">${s.n}</button>`).join("");
  const sel = () => $$("#scB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
  $$("#scB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; sel(); make(); }));
  sel(); make();
})();

(function () {
  const steps = [
    ["Application", "Write the letter", "You write a letter the reader can understand. This is the message and the language (protocol) it uses."],
    ["Transport", "Split into numbered parcels", "The letter is cut into parcels numbered 1 of 4, 2 of 4 and so on, so the reader can reassemble them and spot a missing one."],
    ["Internet", "Label with the full address", "Every parcel gets the full sender and receiver address. Sorting offices read it and choose the route."],
    ["Link", "Van to the next depot", "A van carries the parcels one stretch of the journey. At the next depot another van takes over."],
    ["Link", "New van, same address", "The van and depot change at every stage but the sender and receiver address on the parcel never does."],
    ["Link", "Arrives at the reader", "The last van delivers the parcels."],
    ["Transport", "Reassemble", "The reader puts the parcels in order using the numbers. If parcel 3 is missing, they ask for it again."],
    ["Application", "Read the letter", "The reader gets the complete letter, exactly as written."]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    LN.forEach((n, i) => (o += SV.rect(20, 20 + i * 52, 150, 42, steps[k][0] === n ? "cell-warn" : LC[i], { rx: 8, ...op(steps[k][0] === n ? 1 : 0.5) }) + SV.text(95, 47 + i * 52, n, "lbl bd", { "text-anchor": "middle" })));
    o += SV.rect(200, 20, 540, 194, "cell", { rx: 10 }) + SV.text(220, 56, steps[k][1], "lbl bd", { style: "font-size:19px" });
    const words = steps[k][2].split(" "); let line = "", y = 90;
    words.forEach((w) => { if ((line + w).length > 62) { o += SV.text(220, y, line, "lbl", {}); y += 26; line = ""; } line += w + " "; });
    o += SV.text(220, y, line, "lbl", {});
    return o;
  };
  Lib.stepper($("#stP"), { w: 760, h: 234, label: "A letter through the post as the four layers", base: { i: 0 }, draw, tween: 1, dwell: 3200, steps: steps.map((s, i) => ({ cap: "<b>" + s[0] + " layer:</b> " + s[1] + ".", s: { i } })) });
})();

(function () {
  let cur = 0;
  const hdr = [["Message", "Application", "The data the program wants to send"], ["Transport header", "Transport", "Sequence number and port, so the packets can be put in order"], ["Internet header", "Internet", "Source and destination IP address, so the packet can be routed"], ["Link header", "Link", "MAC addresses of this hop, to make a frame"]];
  const paint = () => {
    $$("#hB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const sc = SC[cur];
    $("#hO").innerHTML = '<div class="tw"><table class="t"><tr><th>Layer</th><th>What it contributes</th><th>In this situation</th></tr>' + hdr.map((h, i) => `<tr><td><b>${LN[i]}</b></td><td>${h[2]}</td><td>${sc.d[i]}</td></tr>`).join("") + "</table></div>";
  };
  $("#hB").innerHTML = SC.map((s, i) => `<button class="b" data-i="${i}">${s.n}</button>`).join("");
  $$("#hB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); paint();
})();

btnTable("fB", "fO", [
  ["Wi-Fi signal lost", "Link", "The device cannot send or receive frames on the physical medium", "No page loads at all"],
  ["404 Not Found", "Application", "The HTTP reply came back, so the network worked; the page does not exist", "A message from the website"],
  ["Two devices with the same IP address", "Internet", "Packets cannot be delivered reliably to a duplicated address", "One device keeps losing its connection"],
  ["Download arrives with chunks missing, then repeats them", "Transport", "Lost packets are noticed by sequence number and re-sent", "A slow download"],
  ["A router has no route to a network", "Internet", "Routing is the Internet layer's job", "Packets never reach that network"],
  ["Mail server rejects a message", "Application", "SMTP, the Application layer protocol, refused the message", "A bounce-back email"],
  ["Ethernet cable unplugged", "Link", "The physical connection has gone", "No connection"]
], ["Symptom", "Layer most likely involved", "Why", "What the user sees"]);

btnTable("dB", "dO", [
  ["Web browser", "Application", "Creates the HTTP request and shows the page"],
  ["Operating system", "Transport and Internet", "Its network software splits data into packets and adds IP addresses"],
  ["Home router", "Internet (and Link)", "Reads the IP address, routes the packet, builds a new frame for the next hop"],
  ["Network switch", "Link", "Passes frames within a local network using MAC addresses"],
  ["Wi-Fi chip or network card", "Link", "Sends and receives the frames over the physical medium"],
  ["Cable or radio link", "Physical medium used by the Link layer", "Carries the signal; it does not look at the data"]
], ["Device", "Layer(s) it works at", "What it does with the data"]);
Lib.classify($("#cl1"), { prompt: "Which layer is involved?", buckets: [{"label": "Application"}, {"label": "Transport"}, {"label": "Internet"}, {"label": "Link"}], items: [{"text": "Chrome sends an HTTP request", "b": 0}, {"text": "A packet's sequence number is checked", "b": 1}, {"text": "A router reads the destination IP address", "b": 2}, {"text": "The Wi-Fi chip sends a frame", "b": 3}, {"text": "An email client uses SMTP", "b": 0}, {"text": "A lost packet is requested again", "b": 1}, {"text": "A new frame is made for the next hop", "b": 3}, {"text": "Choosing the best route", "b": 2}], done: "Programs and protocols: Application. Numbers and re-sending: Transport. IP and routing: Internet. Frames, MAC and the medium: Link." });
Lib.classify($("#cl2"), { prompt: "Which layer is the likely cause?", buckets: [{"label": "Application"}, {"label": "Transport"}, {"label": "Internet"}, {"label": "Link"}], items: [{"text": "The Wi-Fi is switched off", "b": 3}, {"text": "The website returns 404 Not Found", "b": 0}, {"text": "Two devices share one IP address", "b": 2}, {"text": "Packets are missing and are re-sent, slowing a download", "b": 1}, {"text": "The Ethernet cable is unplugged", "b": 3}, {"text": "A router has no route to the destination", "b": 2}, {"text": "The mail server refuses an email", "b": 0}, {"text": "A file arrives with pieces out of order", "b": 1}], done: "The symptom points to one layer: Link, Application, Internet or Transport." });
Lib.order($("#o1"), { prompt: "Put a web page request in order as it is sent.", items: ["The browser creates an HTTP request", "The message is split into numbered packets", "IP addresses are added to each packet", "Each packet is put into a frame and sent over Wi-Fi"], done: "Application, Transport, Internet, Link." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Chrome", "Application layer"], ["Sequence number", "Transport layer"], ["203.0.113.10 (an IP address)", "Internet layer"], ["Wi-Fi chip", "Link layer"], ["Router (routing)", "Internet layer"], ["Frame", "Link layer"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 3 MB photo (3 000 000 bytes) is split into packets of 1500 bytes. How many packets?", "a": 2000, "unit": "", "tol": 0.01, "hint": "3 000 000 ÷ 1500.", "sol": "<b>2000</b>."},
  {"q": "A video call sends 50 packets every second. How many packets in a 2-minute call?", "a": 6000, "unit": "", "tol": 0.01, "hint": "50 × 120.", "sol": "<b>6000</b>."},
  {"q": "A packet crosses 4 routers between a laptop and a server. How many separate frames are made for the journey?", "a": 5, "unit": "", "tol": 0.01, "hint": "Laptop to router 1, then 1 to 2, 2 to 3, 3 to 4, 4 to server.", "sol": "<b>5</b>."},
  {"q": "A message is split into 12 packets and 3 are lost and re-sent. How many packet transmissions in total?", "a": 15, "unit": "", "tol": 0.01, "hint": "12 + 3.", "sol": "<b>15</b>."},
  {"q": "In the 4-router journey above, how many times does the destination IP address change?", "a": 0, "unit": "", "tol": 0.01, "hint": "It stays the same from end to end.", "sol": "<b>0</b>. It never changes."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A router mainly works at which layer?", opts: ["Application", "Transport", "Internet", "Link"], a: 2, why: "It reads IP addresses and routes packets." },
  { q: "Your laptop has no Wi-Fi signal. Which layer is most likely involved?", opts: ["Application", "Transport", "Internet", "Link"], a: 3, why: "The Link layer gives access to the medium." },
  { q: "What changes at every hop?", opts: ["The destination IP address", "The MAC addresses of the frame", "The sequence numbers", "The web page"], a: 1, why: "MAC addresses are for the next hop." },
  { q: "In the postal analogy, numbering the parcels is like...", opts: ["the Application layer", "the Transport layer", "the Internet layer", "the Link layer"], a: 1, why: "Sequence numbers are the Transport layer." },
  { q: "A video call app is part of which layer?", opts: ["Application", "Transport", "Internet", "Link"], a: 0, why: "The program is the Application layer." },
  { q: "Which statement is true?", opts: ["Only computers use the stack", "Phones, routers and doorbells all use the same layers", "Only the Link layer is needed for the internet", "Each layer talks to every other layer"], a: 1, why: "Every networked device uses the stack." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Application", "The program and the protocol it speaks."],
  ["Transport", "Numbered packets, re-sending, reordering."],
  ["Internet", "IP addresses and routing."],
  ["Link", "Frames and the physical medium, hop by hop."],
  ["IP address", "Stays the same for the whole journey."],
  ["MAC address", "Changes at every hop."],
  ["Router", "Reads the IP address and routes; makes new frames."],
  ["Fault finding", "A symptom usually points to one layer."],
] });
