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
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 130, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 65, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, "Programmer writes", true) + B(190, "Copyright", k >= 1) + B(360, "Licence", k >= 2) + SV.path("M150,62 H190", "ax") + SV.path("M320,62 H360", "ax");
    o += SV.text(260, 125, ["", "the author owns the work", "the licence says what users may do", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 140, label: "Copyright", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A programmer writes a program.", "<b>Copyright</b> gives them legal recognition as the owner.", "A <b>licence</b> sets out what users may do with it."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const rows = [["Commercial", [0, 0, 0, 1]], ["Shareware", [0, 0, 1, 1]], ["Open source", [1, 1, 0, 0]]]; const heads = ["edit source", "redistribute", "free trial", "must pay"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; heads.forEach((h, j) => o += SV.text(160 + j * 95, 18, h, "sm", { "text-anchor": "middle" })); rows.forEach(([n, v], i) => { o += SV.text(10, 50 + i * 34, n, "lbl bd", { style: "font-size:13px" }); v.forEach((x, j) => o += SV.rect(125 + j * 95, 32 + i * 34, 70, 28, i < k ? (x ? "f1" : "cell") : "cell", { rx: 5 }) + (i < k ? SV.text(160 + j * 95, 51 + i * 34, x ? "yes" : "no", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) : "")); }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 140, label: "Licences", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Compare what each licence allows.", "<b>Commercial</b>: no editing or redistributing, no trial, must pay.", "<b>Shareware</b>: a free trial, then pay; source not available.", "<b>Open source</b>: edit and redistribute the source code."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const sc = [["A business that wants to modify the code and pays for updates", "open source (OSI or FSF)"], ["A game sold to the public", "commercial or shareware"], ["A program that reads allergen labels", "commercial: no one can change the output"]][Math.min(k, 2)]; let o = SV.rect(20, 30, 480, 40, "cell", { rx: 6 }) + SV.text(30, 56, sc[0], "lbl", { style: "font-size:13px" }) + SV.rect(20, 90, 480, 40, "f1", { rx: 6 }) + SV.text(30, 116, "licence: " + sc[1], "lbl bd", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 150, label: "Choosing", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The developer's business customer wants to edit the code: choose <b>open source</b>.", "A game sold to the public: <b>commercial</b> (or shareware for a trial).", "A program where wrong output could cause harm: not open source."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const opts = [["wants income per copy", 0], ["wants users to try first", 1], ["wants users to edit the code", 2], ["code must stay private", 3]]; const sel = new Set();
  const paint = () => { let fit = ["Commercial", "Shareware", "Freeware", "Open source (OSI)", "Free software (FSF)"].filter((l) => { if (sel.has(0) && ["Freeware", "Open source (OSI)", "Free software (FSF)"].includes(l)) return false; if (sel.has(1) && l !== "Shareware") return false; if (sel.has(2) && !(l.startsWith("Open") || l.startsWith("Free software"))) return false; if (sel.has(3) && (l.startsWith("Open") || l.startsWith("Free software"))) return false; return true; });
    $("#lV").innerHTML = sel.size ? (fit.length ? "Fits: <b>" + fit.join(", ") + "</b>." : "No licence fits all of those at once.") : "Choose what the developer wants."; };
  const bar = $("#lB"); opts.forEach(([t, i]) => { const b = document.createElement("button"); b.textContent = t; b.onclick = () => { sel.has(i) ? sel.delete(i) : sel.add(i); b.className = sel.has(i) ? "on" : ""; paint(); }; bar.appendChild(b); }); paint();
})();
btnTable("eB", "eO", [
  ["Crediting a colleague's idea in a report", "Ethical", "Treat colleagues fairly and credit their work"],
  ["Hiding a bug so the release date is met", "Unethical", "Not in the best interest of the client"],
  ["Telling users honestly what the app cannot do", "Ethical", "Honest claims maintain public trust"],
  ["Selling users' data without telling them", "Unethical", "Does not protect the public's data"],
  ["Asking for training before using a new tool", "Ethical", "Acting competently"]
], ["Action", "Verdict", "Why"]);
btnTable("fB", "fO", [
  ["A fee is charged; source code cannot be accessed", "Commercial", "No free trial"],
  ["Try before buying; some features may be locked", "Shareware", "Free trial then pay"],
  ["Source code can be altered and redistributed", "Open source / FSF", "Collaboration"],
  ["Only the author may copy or change it", "Copyright", "Legal protection"]
], ["Statement", "Licence", "Key point"]);
Lib.classify($("#cl1"), { prompt: "Which licence does the statement describe?", buckets: [{"label": "Commercial"}, {"label": "Shareware"}, {"label": "Open source / free software"}], items: [{"text": "A fee is charged and the source code cannot be accessed", "b": 0}, {"text": "Users can try the software before buying it", "b": 1}, {"text": "Users can access and alter the source code", "b": 2}, {"text": "Users can redistribute the software", "b": 2}, {"text": "Users always get a trial period", "b": 1}, {"text": "Users must always pay before they can use it", "b": 0}], done: "Commercial: pay. Shareware: trial. Open source: edit." });
Lib.classify($("#cl2"), { prompt: "Ethical or unethical for a programmer?", buckets: [{"label": "Ethical"}, {"label": "Unethical"}], items: [{"text": "Crediting a colleague's contribution", "b": 0}, {"text": "Hiding an error found in tested code to avoid trouble", "b": 1}, {"text": "Making honest claims about what the software can do", "b": 0}, {"text": "Copying a classmate's program as your own", "b": 1}, {"text": "Keeping customers' data secure", "b": 0}, {"text": "Using the school network to hack another computer", "b": 1}], done: "Honest, fair, safe: ethical." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Commercial licence", "A fee, no source code, users cannot copy or change it"], ["Shareware", "Free trial, then the user pays"], ["Freeware", "Free to use, source code not available"], ["Open Source Initiative", "Source code available to edit and redistribute"], ["Copyright", "The legal right of the author to control copying and selling"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the shareware process in order.", items: ["The developer releases a trial version", "The user tries it free of charge", "The user decides whether it meets their needs", "The user pays for the full version", "The developer receives income"], done: "Release, try, decide, pay, income." });
Lib.calc($("#c1"), { qs: [
  {"q": "A shareware trial lasts 30 days. A user starts on 1 March (day 1). On which day of March does the trial end (day 30)?", "a": 30, "unit": "", "tol": 0.01, "hint": "Day 30.", "sol": "<b>30</b> March."},
  {"q": "A program sells for £20 and 5000 users buy it. How much income in pounds?", "a": 100000, "unit": "£", "tol": 0.5, "hint": "20 × 5000.", "sol": "<b>£100 000</b>."},
  {"q": "10% of 8000 trial users buy the £15 full version. How much income in pounds?", "a": 12000, "unit": "£", "tol": 0.5, "hint": "800 × 15.", "sol": "<b>£12 000</b>."},
  {"q": "A team has 4 programmers and an ethical body fee is £60 each per year. Total in pounds?", "a": 240, "unit": "£", "tol": 0.5, "hint": "4 × 60.", "sol": "<b>£240</b>."},
  {"q": "How many licence types are in the Learn tab table?", "a": 5, "unit": "", "tol": 0.01, "hint": "Commercial, shareware, freeware, OSI, FSF.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Shareware gives:", opts: ["A free trial then payment", "No payment ever", "Source code", "No copyright"], a: 0, why: "Trial then pay." },
  { q: "Open source means:", opts: ["The source code is available to edit", "The program is always free", "The program has no author", "No licence"], a: 0, why: "Source code available." },
  { q: "Copyright allows the author to:", opts: ["Take legal action against copying", "Stop all use", "Ignore the law", "Avoid testing"], a: 0, why: "Legal action." },
  { q: "A professional ethical body provides:", opts: ["Guidelines, support and training", "A compiler", "Free software", "A server"], a: 0, why: "Guidelines." },
  { q: "A commercial licence:", opts: ["Does not allow users to change the code", "Gives the source code", "Is always free", "Allows free copying"], a: 0, why: "No changes." },
  { q: "Acting ethically toward the public includes:", opts: ["Keeping data secure", "Hiding errors", "Copying code", "Overstating features"], a: 0, why: "Data security." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Ethics", "Acting fairly and responsibly."],
  ["Ethical body", "Guidelines, recognition, support, training."],
  ["Copyright", "Owner's legal rights; legal action."],
  ["Commercial", "Fee; no source code; no copying."],
  ["Shareware", "Trial then pay."],
  ["Freeware", "Free; no source code."],
  ["Open source", "Source code available; edit and redistribute."],
  ["FSF / OSI", "Two open licence bodies."],
] });
