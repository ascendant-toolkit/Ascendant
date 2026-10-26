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
  const ip = [192, 168, 3, 2];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "192 . 168 . 3 . 2  (IPv4, 32 bits)", "lbl bd", { style: "font-family:var(--mono);font-size:16px" }); ip.forEach((v, i) => { const bits = bin(v, 8); if (k >= i + 1) { o += SV.text(40 + i * 140, 62, "group " + (i + 1) + " = " + v, "sm"); [...bits].forEach((b, j) => (o += SV.rect(30 + i * 140 + j * 15, 70, 14, 28, b === "1" ? "cell-ok" : "cell", { rx: 2 }) + SV.text(37 + i * 140 + j * 15, 90, b, "lbl bd", { "text-anchor": "middle", style: "font-size:12px;font-family:var(--mono)" }))); } });
    if (k >= 5) o += SV.text(20, 140, "4 groups × 8 bits = 32 bits", "lbl bd t3"); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 160, label: "IPv4 in binary", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: [{ cap: "An IPv4 address is four groups, each a number from 0 to 255.", s: { i: 0 } }, { cap: "192 in 8 bits.", s: { i: 1 } }, { cap: "168 in 8 bits.", s: { i: 2 } }, { cap: "3 in 8 bits.", s: { i: 3 } }, { cap: "2 in 8 bits.", s: { i: 4 } }, { cap: "Four groups of 8 bits make <b>32 bits</b>.", s: { i: 5 } }] });
})();
(function () {
  const L = ["User types https://www.example.com/shop", "Browser checks its cache", "Browser splits the URL: https / www.example.com / /shop", "Browser asks a DNS server for the IP address", "DNS server returns 93.184.216.34", "Browser connects to the web server at that address and requests the page", "Server sends the page; the browser renders it"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((t, i) => { if (i <= k) o += SV.rect(20, 10 + i * 36, 560, 30, i === k ? "cell-warn" : "cell-ok", { rx: 6 }) + SV.text(34, 30 + i * 36, t, "lbl", { style: "font-size:13px" }); }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 270, label: "URL to page", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: L.map((t, i) => ({ cap: ["The user types a URL.", "The browser first looks in its <b>cache</b>.", "It <b>parses</b> the URL into protocol, domain name and path.", "It <b>queries a DNS server</b> for the IP address of the domain name.", "The DNS server <b>returns the IP address</b>.", "The browser <b>connects</b> to the web server at that address and <b>requests</b> the page.", "The page is <b>rendered and displayed</b>, and the address is cached for next time."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "LAN (private addresses)", "lbl bd") + SV.rect(20, 30, 230, 160, "cell", { rx: 10 }); [["Laptop", "192.168.1.20", 50], ["Phone", "192.168.1.21", 90], ["Server", "192.168.1.5 (static)", 130]].forEach(([n, a, y]) => (o += SV.text(34, y + 12, n + "  " + a, "lbl", { style: "font-size:12px;font-family:var(--mono)" })));
    o += SV.rect(300, 80, 110, 60, "f3", { rx: 8 }) + SV.text(355, 105, "Router", "lbl bd", { "text-anchor": "middle" }) + SV.text(355, 125, "private 192.168.1.1", "sm", { "text-anchor": "middle", style: "font-size:10px" }); o += SV.path("M250,110 H300", "ax", {}) ;
    if (k >= 1) o += SV.rect(460, 80, 130, 60, "f1", { rx: 8 }) + SV.text(525, 105, "Internet", "lbl bd", { "text-anchor": "middle" }) + SV.text(525, 125, "public 203.0.113.7", "sm", { "text-anchor": "middle", style: "font-size:10px" }) + SV.path("M410,110 H460", "ax", {}); if (k >= 2) o += SV.text(300, 180, "outside, only the router's PUBLIC address is visible", "lbl bd t3", { style: "font-size:12.5px" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 200, label: "Public and private", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "Devices inside the LAN have <b>private</b> addresses, assigned by the router.", s: { i: 0 } }, { cap: "The router also has a <b>public</b> address so it is visible on the internet.", s: { i: 1 } }, { cap: "Outsiders can reach only the public address, not the private ones. The server has a <b>static</b> address, the phone a <b>dynamic</b> one.", s: { i: 2 } }] });
})();

(function () {
  const inp = $("#iI"), out = $("#iO");
  const paint = () => { const s = inp.value.trim(); let h = ""; const v4 = /^\d{1,3}(\.\d{1,3}){3}$/.test(s), g = s.split("."); if (v4 && g.every((x) => +x <= 255)) { const priv = +g[0] === 10 || (+g[0] === 172 && +g[1] >= 16 && +g[1] <= 31) || (+g[0] === 192 && +g[1] === 168); h = `<p><b>Valid IPv4</b> (32 bits). Binary: <span class="bx">${g.map((x) => bin(+x, 8)).join(".")}</span></p><p>This is a <b>${priv ? "private" : "public"}</b> address (${priv ? "only used inside a LAN" : "visible on the internet"}).</p>`; }
    else if (v4) h = "<p><b>Invalid IPv4</b>: a group is above 255. Each group is an 8-bit number, 0 to 255.</p>"; else if (/^([0-9a-fA-F]{1,4}:){2,7}[0-9a-fA-F]{0,4}(::[0-9a-fA-F:]*)?$/.test(s) || /::/.test(s) && /^[0-9a-fA-F:]+$/.test(s)) h = "<p><b>Looks like IPv6</b> (128 bits): eight groups of four hexadecimal digits separated by colons; groups of zeros can be shortened to ::.</p>"; else h = "<p><b>Invalid</b>: not four decimal groups separated by full stops (IPv4) and not hexadecimal groups separated by colons (IPv6).</p>"; out.innerHTML = h; };
  inp.oninput = paint; paint();
})();
(function () {
  let p = 24; const ip = [192, 168, 1, 37];
  const paint = () => { const bits = ip.map((x) => bin(x, 8)).join(""), net = bits.slice(0, p), host = bits.slice(p); const hostBits = 32 - p, hosts = Math.max(0, 2 ** hostBits - 2); const fmt = (b, c) => [...b].map((x, i) => `<span style="color:${c}">${x}</span>` + ((i + 1 + (c === "var(--accent)" ? 0 : p)) % 8 === 0 && (i + 1 + (c === "var(--accent)" ? 0 : p)) < 32 ? "." : "")).join("");
    $("#sO").innerHTML = `<div class="verdict mono"><b style="color:var(--accent)">network ID bits (${p})</b> | <b style="color:var(--bad)">host ID bits (${hostBits})</b></div><p class="bx">${fmt(net, "var(--accent)")}${fmt(host, "var(--bad)")}</p><div class="verdict">Network ID: first <b>${p}</b> bits. Host ID: remaining <b>${hostBits}</b> bits. About <b>${hosts}</b> devices can share this subnet (2<sup>${hostBits}</sup> − 2, as the all-zeros and all-ones host values are reserved). More network bits mean more, smaller subnets.</div>`; };
  Lib.slider($("#sS"), { id: "ss", label: "Network ID bits ", min: 8, max: 30, value: p, fmt: (x) => x, onInput: (v) => { p = v; paint(); } }); paint();
})();
(function () {
  const T = { "www.example.com": "93.184.216.34", "www.school.edu": "198.51.100.12", "mail.example.org": "203.0.113.25", "www.nowhere.invalid": null }; const b = $("#dB");
  const show = (d) => { const ip = T[d]; $("#dO").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Step</th><th>What happens</th></tr><tr><td>1</td><td>Browser cache checked for ${d}: not found</td></tr><tr><td>2</td><td>DNS query: what is the IP address of ${d}?</td></tr><tr><td>3</td><td>${ip ? "DNS reply: <b>" + ip + "</b>" : "<b>No record found</b>: the page cannot be reached"}</td></tr><tr><td>4</td><td>${ip ? "Browser connects to " + ip + " and requests the page" : "Browser shows an error"}</td></tr></table></div>`; b.querySelectorAll("button").forEach((x) => (x.className = x.textContent === d ? "on" : "")); };
  Object.keys(T).forEach((d) => { const x = document.createElement("button"); x.textContent = d; x.onclick = () => show(d); b.appendChild(x); }); show("www.example.com");
})();
Lib.classify($("#cl1"), { prompt: "Is it IPv4 or IPv6?", buckets: [{"label": "IPv4"}, {"label": "IPv6"}], items: [{"text": "32 bits", "b": 0}, {"text": "128 bits", "b": 1}, {"text": "Four groups separated by full stops", "b": 0}, {"text": "Eight groups of four hex digits with colons", "b": 1}, {"text": "Consecutive groups of zeros can be written ::", "b": 1}, {"text": "Each group is a number from 0 to 255", "b": 0}], done: "IPv4: 32 bits, full stops. IPv6: 128 bits, colons." });
Lib.classify($("#cl2"), { prompt: "Which type of IP address is described?", buckets: [{"label": "Public"}, {"label": "Private"}, {"label": "Static"}, {"label": "Dynamic"}], items: [{"text": "Visible on the internet", "b": 0}, {"text": "Used only inside a LAN", "b": 1}, {"text": "Does not change when a device rejoins the network", "b": 2}, {"text": "May change each time the device rejoins", "b": 3}, {"text": "Assigned by the router within the LAN", "b": 1}, {"text": "Lets a device be reached directly from the internet", "b": 0}], done: "Public/private is about visibility; static/dynamic about changing." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["IPv4", "A 32-bit address in four groups"], ["IPv6", "A 128-bit address in eight hex groups"], ["Network ID", "The part of an IP address that identifies the (sub)network"], ["Host ID", "The part that identifies the device within the network"], ["DNS", "Turns a domain name into an IP address"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of loading a web page from a URL in order.", items: ["The browser checks its cache", "It queries a DNS server for the IP address", "The DNS server returns the IP address", "The browser connects to the web server and requests the page", "The browser renders and displays the page"], done: "Cache, query DNS, IP returned, connect, display." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many bits are in an IPv4 address?", "a": 32, "unit": "", "tol": 0.01, "hint": "4 groups of 8.", "sol": "<b>32</b>."},
  {"q": "How many bits are in an IPv6 address?", "a": 128, "unit": "", "tol": 0.01, "hint": "8 groups of 16 bits.", "sol": "<b>128</b>."},
  {"q": "Convert the IPv4 group 192 to binary: how many 1 bits does it contain?", "a": 2, "unit": "", "tol": 0.01, "hint": "192 = 11000000.", "sol": "<b>2</b>."},
  {"q": "A subnet uses 24 bits for the network ID. How many bits are left for the host ID?", "a": 8, "unit": "", "tol": 0.01, "hint": "32 − 24.", "sol": "<b>8</b>."},
  {"q": "With 8 host bits, how many host addresses are there (2 to the power 8, before reserving any)?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "IPv6 groups are separated by:", opts: ["Full stops", "Colons", "Commas", "Spaces"], a: 1, why: "Colons." },
  { q: "DNS converts:", opts: ["A domain name to an IP address", "A file to a picture", "Analogue to digital", "A URL to binary"], a: 0, why: "Domain name to IP address." },
  { q: "A private IP address:", opts: ["Is visible on the internet", "Is only used inside a LAN", "Is always static", "Has 64 bits"], a: 1, why: "Only inside a LAN." },
  { q: "Which is a valid IPv4 address?", opts: ["256.1.1.1", "192.168.0.1", "192.168.0", "A.B.C.D"], a: 1, why: "Each group 0 to 255." },
  { q: "A static IP address:", opts: ["Changes each time", "Does not change", "Is never used", "Is IPv6 only"], a: 1, why: "It does not change." },
  { q: "Subnetting helps by:", opts: ["Reducing congestion", "Deleting devices", "Raising voltage", "Adding bits"], a: 0, why: "Reducing congestion." },
] });
Lib.cards($("#fc1"), { cards: [
  ["IPv4", "32 bits; 4 groups 0-255; full stops."],
  ["IPv6", "128 bits; 8 hex groups; colons; :: for zeros."],
  ["Network ID / host ID", "Network part and device part."],
  ["Subnetting", "Smaller networks: less congestion, more security."],
  ["Public IP", "Visible on the internet."],
  ["Private IP", "Inside the LAN only."],
  ["Static / dynamic", "Fixed / may change."],
  ["DNS", "Domain name to IP address."],
] });
