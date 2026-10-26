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
  const draw = (s) => { const k = Math.round(s.i); const n = [1, 2, 4, 8][k]; let o = ""; for (let i = 0; i < 8; i++) o += SV.rect(30 + i * 60, 40, 52, 40, i < n ? "f2" : "cell", { rx: 6 }) + SV.text(56 + i * 60, 65, i < n ? "infected" : "file", "sm", { "text-anchor": "middle" });
    o += SV.text(30, 120, [`${n} infected file`, `${n} infected files: each copied itself once`, `${n} infected files: it keeps replicating`, `${n} infected files: it fills storage and corrupts data`][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 140, label: "Virus", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["One file is infected by a virus.", "The virus <b>replicates</b> itself into other files.", "It copies itself again.", "It can fill storage and <b>corrupt or delete</b> data."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(10, "User types", true) + B(180, "Spyware (hidden)", k >= 1) + B(350, "Third party", k >= 3) + SV.path("M130,62 H180", "ax") + SV.path("M300,62 H350", "ax", { style: k >= 2 ? "stroke:var(--bad);stroke-width:3" : "" });
    o += SV.text(260, 125, ["", "installed without the user knowing; runs in the background", "it records keystrokes", "and sends the log to a third party"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 500, h: 145, label: "Spyware", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A user types a password.", "<b>Spyware</b> is running in the background.", "It <b>records</b> every keystroke.", "It <b>sends</b> the data to a third party."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Phishing", "lbl bd") + SV.text(300, 20, "Pharming", "lbl bd") + SV.rect(20, 30, 230, 34, "cell", { rx: 6 }) + SV.text(30, 52, k >= 1 ? "email: 'click here'" : "", "lbl", { style: "font-size:12px" }) + SV.rect(300, 30, 230, 34, "cell", { rx: 6 }) + SV.text(310, 52, k >= 2 ? "user types the real address" : "", "lbl", { style: "font-size:12px" });
    if (k >= 3) o += SV.rect(20, 80, 230, 34, "f2", { rx: 6 }) + SV.text(30, 102, "user clicks: fake website", "lbl", { style: "font-size:12px" }) + SV.rect(300, 80, 230, 34, "f2", { rx: 6 }) + SV.text(310, 102, "code redirects: fake website", "lbl", { style: "font-size:12px" });
    o += SV.text(20, 150, k >= 3 ? "Phishing needs the user to act; pharming redirects automatically." : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 170, label: "Phishing and pharming", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Both aim to get personal data through a fake website.", "<b>Phishing</b> starts with an email that tells the user to click.", "<b>Pharming</b> starts with malicious code on the computer.", "Phishing needs <b>user action</b>; pharming is <b>automatic</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let copies = 2, hours = 5; const paint = () => { let a = 1, t = [1]; for (let h = 1; h <= hours; h++) { a *= copies; t.push(t[t.length - 1] + a); } const mx = Math.max(...t); let o = '<svg viewBox="0 0 420 150" style="width:420px;max-width:100%;display:block"><path d="M30,10 V130 H400" class="ax"/>'; t.forEach((v, i) => { const hgt = (Math.log(v + 1) / Math.log(mx + 1)) * 110; o += `<rect x="${40 + i * (350 / t.length)}" y="${130 - hgt}" width="${300 / t.length}" height="${hgt}" fill="var(--bad)" opacity=".7"/>`; }); $("#vG").innerHTML = o + `<text x="400" y="146" class="sm" text-anchor="end" style="font-size:11px">hours</text></svg>`;
    $("#vV").innerHTML = `If every infected file infects <b>${copies}</b> new file(s) each hour, after <b>${hours}</b> hours there are <b>${t[t.length - 1].toLocaleString()}</b> infected files. Replication makes a virus spread fast, which is why anti-malware needs to be running and up to date.`; };
  Lib.slider($("#vS1"), { id: "v1", label: "New infections per infected file per hour ", min: 1, max: 5, value: copies, fmt: (x) => x, onInput: (v) => { copies = v; paint(); } });
  Lib.slider($("#vS2"), { id: "v2", label: "Hours ", min: 1, max: 8, value: hours, fmt: (x) => x, onInput: (v) => { hours = v; paint(); } }); paint();
})();
btnTable("tB", "tO", [
  ["Records every key you press and sends it away", "Spyware", "Secretly records and sends to a third party"],
  ["Copies itself into other files and corrupts them", "Virus", "Replicates"],
  ["Email asking you to confirm your bank details by clicking a link", "Phishing", "Needs the user to act"],
  ["Types bank.com and lands on a copy of the site", "Pharming", "Redirected automatically"],
  ["Guesses a weak password and logs in as a teacher", "Hacker", "Unauthorised access"]
], ["Description", "Threat", "Key idea"]);
btnTable("eB", "eO", [
  ["'Your account is locked, click this link now', from a strange address", "Phishing", "Urgent, unexpected, suspicious sender"],
  ["Message from your school about a timetable, from the school domain, no link", "Genuine", "Expected and no request for details"],
  ["'You have won a prize: send your card number'", "Phishing", "Asks for private information"],
  ["Receipt for something you bought, address matches the shop", "Genuine", "Expected and matches"]
], ["Email", "Verdict", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which threat does it describe?", buckets: [{"label": "Virus"}, {"label": "Spyware"}, {"label": "Phishing"}, {"label": "Pharming"}, {"label": "Hacker"}], items: [{"text": "Replicates itself and corrupts files", "b": 0}, {"text": "Records keystrokes and sends them to a third party", "b": 1}, {"text": "An email pretending to be a bank asking for details", "b": 2}, {"text": "Redirects the user to a fake website automatically", "b": 3}, {"text": "A person with unauthorised access to a system", "b": 4}, {"text": "Installed without the user's knowledge, runs in the background", "b": 1}], done: "Match each description." });
Lib.classify($("#cl2"), { prompt: "Phishing or pharming?", buckets: [{"label": "Phishing"}, {"label": "Pharming"}], items: [{"text": "Uses an email to prompt user action", "b": 0}, {"text": "Malicious code redirects to a fake site", "b": 1}, {"text": "Needs the user to click a link", "b": 0}, {"text": "Happens automatically", "b": 1}, {"text": "Asks you to reply with your bank details", "b": 0}, {"text": "Installed on the computer", "b": 1}], done: "Phishing: user acts. Pharming: automatic." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Virus", "Malicious software that replicates itself"], ["Spyware", "Secretly records user actions and sends them on"], ["Phishing", "An email that pretends to be from an official body"], ["Pharming", "Malicious code that redirects to a fake website"], ["Hacker", "Gains unauthorised access to a computer system"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the phishing attack in order.", items: ["A fake email pretends to be from a bank", "It asks the user to click a link", "The link opens a fake website", "The user enters their bank details", "The details are sent to the criminal"], done: "Email, link, fake site, details, sent." });
Lib.calc($("#c1"), { qs: [
  {"q": "A virus infects 1 file and every infected file infects 2 new files per hour. How many infected files after 4 hours (including the original, cumulative)?", "a": 31, "unit": "", "tol": 0.01, "hint": "1 + 2 + 4 + 8 + 16.", "sol": "<b>31</b>."},
  {"q": "Spyware records 50 keystrokes each minute. How many keystrokes in an hour?", "a": 3000, "unit": "", "tol": 0.01, "hint": "50 × 60.", "sol": "<b>3000</b>."},
  {"q": "An anti-malware database has 2 million known viruses and adds 5000 a day. How many after 10 days?", "a": 2050000, "unit": "", "tol": 0.5, "hint": "2 000 000 + 50 000.", "sol": "<b>2 050 000</b>."},
  {"q": "A school sends 800 emails; 2% are phishing. How many phishing emails?", "a": 16, "unit": "", "tol": 0.01, "hint": "2% of 800.", "sol": "<b>16</b>."},
  {"q": "A password has 8 characters from 26 letters. How many possible passwords, in billions (1 d.p.)?", "a": 208.8, "unit": "billion", "tol": 0.2, "hint": "26^8 = 208 827 064 576.", "sol": "about <b>208.8</b> billion."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A virus:", opts: ["Replicates itself", "Only records keystrokes", "Is a person", "Is an email"], a: 0, why: "Replicates." },
  { q: "Spyware:", opts: ["Sends recorded data to a third party", "Redirects to fake sites", "Blocks ports", "Creates back-ups"], a: 0, why: "Sends data out." },
  { q: "Pharming:", opts: ["Redirects to a fake website automatically", "Needs a user click", "Is a measure", "Is a firewall"], a: 0, why: "Automatic redirect." },
  { q: "A hacker:", opts: ["Gains unauthorised access", "Updates software", "Compresses files", "Formats a disk"], a: 0, why: "Unauthorised access." },
  { q: "Anti-malware:", opts: ["Scans against known malware", "Redirects traffic", "Encrypts emails", "Slows the CPU"], a: 0, why: "Scans." },
  { q: "A back-up helps against malware by:", opts: ["Restoring lost data", "Blocking packets", "Detecting phishing", "Hiding passwords"], a: 0, why: "Restoring data." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Virus", "Replicates; corrupts or deletes data."],
  ["Spyware", "Records and sends to a third party."],
  ["Phishing", "Email; user acts; fake site."],
  ["Pharming", "Code redirects automatically."],
  ["Hacker", "Unauthorised access."],
  ["Anti-malware", "Scan, quarantine, update."],
  ["Firewall", "Blocks unwanted packets."],
  ["Strong password", "Long; mixed characters."],
] });
