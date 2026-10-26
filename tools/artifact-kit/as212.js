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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 120, 60, "cell", { rx: 8 }) + SV.text(80, 66, "Your device", "lbl bd", { "text-anchor": "middle" }) + SV.text(80, 86, k >= 3 ? "(no files kept)" : "", "sm", { "text-anchor": "middle" });
    o += SV.rect(420, 20, 140, 120, k >= 1 ? "f1" : "cell", { rx: 12 }) + SV.text(490, 48, "Cloud server", "lbl bd", { "text-anchor": "middle" }) + SV.text(490, 68, "(remote)", "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M140,60 H420", "ax", { style: "stroke-dasharray:6 5" }) + SV.text(280, 52, "internet", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.rect(445, 82, 90, 28, "cell-ok", { rx: 4 }) + SV.text(490, 101, "file.docx", "lbl", { "text-anchor": "middle", style: "font-size:12px" });
    if (k >= 3) o += SV.rect(20, 140, 120, 36, "cell", { rx: 8 }) + SV.text(80, 163, "Another device", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) + SV.path("M140,158 L420,120", "ax", { style: "stroke-dasharray:6 5" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 190, label: "Cloud storage", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A device and a remote <b>cloud server</b> run by a provider.", s: { i: 0 } }, { cap: "The device connects to the server over the <b>internet</b>.", s: { i: 1 } }, { cap: "The file is stored on the <b>remote server</b>.", s: { i: 2 } }, { cap: "Any other device with an internet connection can reach the same file. Without the internet, nobody can.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "copper: electrical signal", "lbl bd") + SV.path("M20,50 H560", "ax", { style: "stroke:#b87333;stroke-width:6" }); const x1 = 20 + k * 110; o += SV.circle(Math.min(560, x1), 50, 8 - Math.min(6, k), "dot4");
    o += SV.text(20, 22 + 80, "fibre: pulses of light", "lbl bd") + SV.path("M20,130 H560", "ax", { style: "stroke:var(--accent);stroke-width:6;opacity:.5" }); o += SV.circle(Math.min(560, 20 + k * 110), 130, 8, "dot1");
    if (k >= 4) o += SV.text(20, 76, "signal weakens and picks up noise: repeaters needed over distance", "sm") + SV.text(20, 156, "light arrives strong: far less interference, much longer distance", "sm"); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 175, label: "Copper and fibre", base: { i: 0 }, draw, tween: 100, dwell: 1600, steps: [{ cap: "The same data is sent down copper (electrical signals) and fibre (light).", s: { i: 0 } }, { cap: "The copper signal is already weakening; the light pulse is not.", s: { i: 1 } }, { cap: "Further on, the copper signal is weaker and can pick up interference.", s: { i: 2 } }, { cap: "Over distance the electrical signal needs a repeater.", s: { i: 3 } }, { cap: "<b>Fibre</b>: higher bandwidth, longer distance, less interference, harder to tap. <b>Copper</b>: cheaper and easier to install.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; [[110, 40], [300, 40], [490, 40], [205, 110], [395, 110]].forEach(([x, y], i) => (o += SV.rect(x - 38, y - 18, 76, 36, "cell", { rx: 8, ...op(0.8) }) + SV.text(x, y + 4, "cell " + (i + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" })));
    o += SV.rect(262, 80, 76, 40, "f3", { rx: 8 }) + SV.text(300, 104, "tower", "lbl bd", { "text-anchor": "middle" }); if (k >= 1) o += SV.rect(520, 140, 70, 30, "cell-warn", { rx: 6 }) + SV.text(555, 160, "phone", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); if (k >= 2) o += SV.path("M520,150 L338,106", "ax", { style: "stroke-dasharray:5 4;stroke:var(--accent);stroke-width:3" }) + SV.text(440, 118, "radio", "sm", { "text-anchor": "middle" }); if (k >= 3) o += SV.rect(30, 140, 70, 30, "cell-warn", { rx: 6 }) + SV.text(65, 160, "phone 2", "lbl", { "text-anchor": "middle", style: "font-size:11px" }) + SV.path("M100,150 L262,108", "ax", { style: "stroke-dasharray:5 4;stroke:var(--accent);stroke-width:3" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 190, label: "Cell phone network", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The land is split into <b>cells</b>. Each has a tower with an antenna.", s: { i: 0 } }, { cap: "A phone is in range of one cell's tower.", s: { i: 1 } }, { cap: "It transmits data to the tower using <b>low-power radio signals</b>.", s: { i: 2 } }, { cap: "<b>Many devices</b> can communicate with the same tower at the same time.", s: { i: 3 } }] });
})();

(function () {
  let on = true; const b = $("#iB");
  const paint = () => { const rows = [["Open a file stored in the public cloud", on], ["Share a document with a colleague online", on], ["Open a file on the LAN server", true], ["Print on the office printer", true]]; $("#iO").innerHTML = '<div class="tw"><table class="t"><tr><th>Task</th><th>Possible?</th></tr>' + rows.map(([t, ok]) => `<tr><td>${t}</td><td style="font-weight:700;color:${ok ? "var(--good)" : "var(--bad)"}">${ok ? "yes" : "no: no internet"}</td></tr>`).join("") + `</table></div><div class="verdict">${on ? "The internet is on: cloud and LAN both work." : "The internet is off: cloud files cannot be reached. The LAN server still works because it does not use the internet."}</div>`; b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "on") === on ? "on" : "")); };
  [["on", "Internet on"], ["off", "Internet off"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { on = k === "on"; paint(); }; b.appendChild(x); }); paint();
})();
(function () {
  let dist = 50, need = "speed"; const b = $("#dB");
  const paint = () => { const L = [["Copper cable", dist <= 100 && need !== "remote", "cheap and easy to install; fine over short distances"], ["Fibre-optic cable", need !== "mobile" && need !== "remote", "high bandwidth, long distance, little interference"], ["Radio waves (Wi-Fi)", dist <= 100 && need !== "speed", "no cables; devices can move"], ["Microwaves", dist > 100 && need !== "mobile", "line of sight between towers; long distances"], ["Satellite", need === "remote" || dist > 1000, "reaches remote areas; long delay"]];
    $("#dO").innerHTML = '<div class="tw"><table class="t"><tr><th>Medium</th><th>Suitable?</th><th>Why</th></tr>' + L.map(([m, ok, w]) => `<tr><td>${m}</td><td style="font-weight:700;color:${ok ? "var(--good)" : "var(--muted)"}">${ok ? "suitable" : "less suitable"}</td><td>${w}</td></tr>`).join("") + `</table></div><div class="verdict">Distance ${dist} m, need: <b>${need}</b>.</div>`; b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === need ? "on" : "")); };
  [["speed", "Fast and reliable"], ["mobile", "Devices must move"], ["remote", "Remote area"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { need = k; paint(); }; b.appendChild(x); });
  Lib.slider($("#dS"), { id: "ds", label: "Distance (m) ", min: 10, max: 5000, value: 50, fmt: (x) => x, onInput: (v) => { dist = v; paint(); } }); paint();
})();
btnTable("wB", "wO", [
  ["Downloading large files and playing online games", "Wired", "Faster, lower latency, more stable"],
  ["Moving between rooms with a tablet", "Wireless", "Freedom of movement, no cable"],
  ["Transferring confidential data", "Wired", "More secure: a physical connection is needed"],
  ["A temporary stall at an event", "Wireless", "Quick, cheap setup with no cabling"],
  ["A server room", "Wired", "Reliable and fast connections between servers"],
  ["Adding many guest devices", "Wireless", "Easy to add devices without more cables"]
], ["Situation", "Choice", "Reason"]);
Lib.classify($("#cl1"), { prompt: "Is it a public cloud or a private cloud?", buckets: [{"label": "Public cloud"}, {"label": "Private cloud"}], items: [{"text": "Run by a third-party provider and open to anyone with credentials", "b": 0}, {"text": "Only available to one organisation's staff", "b": 1}, {"text": "Gives the company greater control over backup", "b": 1}, {"text": "Infrastructure is shared with other customers", "b": 0}, {"text": "A dedicated, bespoke system", "b": 1}, {"text": "Online storage anyone can sign up to", "b": 0}], done: "Public is open and shared; private is dedicated." });
Lib.classify($("#cl2"), { prompt: "Is it a benefit or a drawback of cloud computing?", buckets: [{"label": "Benefit"}, {"label": "Drawback"}], items: [{"text": "Access from any computer with internet", "b": 0}, {"text": "Cannot be used without an internet connection", "b": 1}, {"text": "No need to buy extra hardware", "b": 0}, {"text": "Reliance on a third party for backup", "b": 1}, {"text": "Easy to share documents", "b": 0}, {"text": "Uploading a large file can take a long time", "b": 1}], done: "Benefits: access, no hardware, sharing. Drawbacks: internet, third party." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Copper cable", "Carries data as electrical signals"], ["Fibre-optic cable", "Carries data as pulses of light"], ["Microwaves", "Line-of-sight signals between towers or dishes"], ["Satellite", "Covers remote areas but has a long delay"], ["Radio waves", "Used for Wi-Fi: no cables, devices can move"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of cell phone data transfer in order.", items: ["The phone sends low-power radio signals to the nearest tower", "The tower's antenna receives the data", "The data passes on through the network to its destination", "The reply comes back to the tower", "The tower transmits it to the phone"], done: "Phone, tower, network, tower, phone." });
Lib.calc($("#c1"), { qs: [
  {"q": "A file is 400 MB and the upload speed is 20 MB per minute. How many minutes does it take?", "a": 20, "unit": "min", "tol": 0.1, "hint": "400 ÷ 20.", "sol": "<b>20</b> minutes."},
  {"q": "How many types of cloud (public, private) must you be able to define?", "a": 2, "unit": "", "tol": 0.01, "hint": "Public and private.", "sol": "<b>2</b>."},
  {"q": "A company pays $5 per user per month for cloud storage for 40 users. What is the cost per year ($)?", "a": 2400, "unit": "$", "tol": 0.5, "hint": "5 × 40 × 12.", "sol": "<b>$2400</b>."},
  {"q": "A fibre cable carries data at 10 times the rate of a copper cable at 100 Mbps. What is the fibre rate in Mbps?", "a": 1000, "unit": "Mbps", "tol": 0.5, "hint": "100 × 10.", "sol": "<b>1000</b> Mbps."},
  {"q": "How many transmission media does the syllabus list (copper, fibre-optic, radio waves, microwaves, satellite)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Fibre-optic cable carries data as:", opts: ["Electrical signals", "Pulses of light", "Sound", "Heat"], a: 1, why: "Light pulses." },
  { q: "A drawback of cloud storage is:", opts: ["Needs an internet connection", "Access from anywhere", "Easy sharing", "No hardware to buy"], a: 0, why: "Needs the internet." },
  { q: "A private cloud is:", opts: ["Open to everyone", "Dedicated to one organisation", "Free for all", "A wireless network"], a: 1, why: "Dedicated." },
  { q: "Which is most affected by interference?", opts: ["Fibre-optic", "Copper cable", "Neither", "Both equally"], a: 1, why: "Copper." },
  { q: "A satellite link has a long:", opts: ["Cable", "Delay (latency)", "Battery", "Keyboard"], a: 1, why: "Delay." },
  { q: "Compared with wired, wireless is usually:", opts: ["More mobile", "Always faster", "Always more secure", "Cheaper per bit always"], a: 0, why: "More mobile." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Cloud computing", "Accessing services or files on a remote server."],
  ["Public cloud", "Third party; open to anyone with credentials."],
  ["Private cloud", "Dedicated to one organisation."],
  ["Copper", "Electrical signals; interference; repeaters."],
  ["Fibre", "Light; fast; long distance; secure; costly."],
  ["Radio", "Wi-Fi; mobile; interference."],
  ["Microwave", "Line of sight; towers."],
  ["Satellite", "Remote areas; delay; expensive."],
] });
