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
  const draw = (s) => { const k = Math.round(s.i); const N = [["Corrective", "a bug is fixed"], ["Adaptive", "new hardware or law"], ["Perfective", "faster and easier"]]; let o = ""; N.forEach((n, i) => o += SV.rect(10 + i * 110, 14, 100, 30, i === k ? "f3" : "cell", { rx: 5 }) + SV.text(60 + i * 110, 34, n[0], "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })); o += SV.text(10, 70, N[k][0] + ": " + N[k][1], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 350, h: 84, label: "Maintenance", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["A fault is found: corrective.", "The world changes: adaptive.", "The program is improved: perfective."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 8, 310, 62, "cell", { rx: 6 }) + SV.text(20, 26, "Identifier table", "lbl bd", { style: "font-size:12px" }); if (k >= 1) o += SV.text(20, 44, "Total  REAL  sum of the marks", "lbl", { style: "font-size:11px;font-family:monospace" }); if (k >= 2) o += SV.text(20, 60, "Count  INTEGER  number of students", "lbl", { style: "font-size:11px;font-family:monospace" }); o += SV.text(10, 92, ["", "The purpose is recorded", "A new programmer can follow the code"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 102, label: "Documentation", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["An identifier table is made in design.", "Each variable has its type and purpose.", "Years later, the maintenance programmer reads it."].map((c, i) => ({ cap: c, s: { i } })) });
})();
btnTable("mnB", "mnO", [
  ["Users report a bug and it is fixed", "Corrective", "fixing a fault"],
  ["The program is changed for new hardware", "Adaptive", "the environment changed"],
  ["A change in the law means the program stores new data", "Adaptive", "legislation"],
  ["The speed of response is improved", "Perfective", "improvement, same function"],
  ["A library module used by the program changes", "Adaptive", "environment changed"]
], ["Change", "Type", "Why"]);
(function () {
  const Q = [["Passwords were not hidden on screen and this is fixed", 0], ["The program is changed to work with a new operating system", 1], ["The code is rewritten so results appear faster", 2], ["Unexpected bugs are reported in the first week", 0], ["The law changes what data may be stored", 1], ["The menus are redesigned to be easier to use", 2]]; let i = 0, score = 0, tries = 0, done = false;
  const paint = (m) => { $("#qzV").innerHTML = `<p><b>${Q[i][0]}</b></p><div class="verdict">${m || "Choose a type."} Score: ${score} / ${tries}</div>`; };
  const ans = (k) => { if (done) return; tries++; if (k === Q[i][1]) { score++; done = true; paint("Correct."); } else paint("Not that one: try again, or move to the next."); };
  $("#qz_c").onclick = () => ans(0); $("#qz_a").onclick = () => ans(1); $("#qz_p").onclick = () => ans(2); $("#qz_n").onclick = () => { i = (i + 1) % Q.length; done = false; paint(); }; paint();
})();
Lib.classify($("#cl1"), { prompt: "Which type of maintenance?", buckets: [{"label": "Corrective"}, {"label": "Adaptive"}, {"label": "Perfective"}], items: [{"text": "The program crashes when a field is empty and is fixed", "b": 0}, {"text": "The program is changed to run on new hardware", "b": 1}, {"text": "The speed of response is improved", "b": 2}, {"text": "A change in the law means the program must store extra data", "b": 1}, {"text": "Passwords are not hidden when typed, and this is fixed", "b": 0}, {"text": "The interface is made easier to use", "b": 2}], done: "Fix a fault: corrective. Environment changed: adaptive. Improve: perfective." });
Lib.classify($("#cl2"), { prompt: "Is the change a fix, an adaptation or an improvement?", buckets: [{"label": "Fix"}, {"label": "Adapt"}, {"label": "Improve"}], items: [{"text": "A bug is found after installation", "b": 0}, {"text": "A library module the program uses changes", "b": 1}, {"text": "The code is made to run faster", "b": 2}, {"text": "A new HTML version is released", "b": 1}, {"text": "The wrong total is corrected", "b": 0}, {"text": "The screens are redesigned for easier use", "b": 2}], done: "Bug: fix. Environment: adapt. Better: improve." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Corrective", "Fixes errors"], ["Adaptive", "Copes with a change in the environment or requirements"], ["Perfective", "Improves the program without changing what it does"], ["Identifier table", "Documents variables for maintenance"], ["Legislation change", "A reason for adaptive maintenance"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of a maintenance change in order.", items: ["A fault or a need for a change is reported", "The programmer reads the documentation", "The change is made in the code", "The program is tested again", "The updated program is released"], done: "Report, read, change, test, release." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many types of maintenance are named on this page?", "a": 3, "unit": "", "tol": 0.01, "hint": "Corrective, adaptive, perfective.", "sol": "<b>3</b>."},
  {"q": "A bug list has 12 faults. 5 are fixed. How many corrective changes remain?", "a": 7, "unit": "", "tol": 0.01, "hint": "12 − 5.", "sol": "<b>7</b>."},
  {"q": "A response time falls from 800 ms to 200 ms. By what percentage is it reduced?", "a": 75, "unit": "%", "tol": 0.01, "hint": "(800 − 200) ÷ 800.", "sol": "<b>75%</b>. This is perfective maintenance."},
  {"q": "An identifier table has 4 columns: name, type, purpose and example. How many columns record something other than the data type and name?", "a": 2, "unit": "", "tol": 0.01, "hint": "Purpose and example.", "sol": "<b>2</b>."},
  {"q": "A program is on 3 platforms and a new platform is added. How many platforms must now be supported?", "a": 4, "unit": "", "tol": 0.01, "hint": "3 + 1: this is adaptive maintenance.", "sol": "<b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Fixing a bug found after release is:", opts: ["Corrective", "Adaptive", "Perfective", "Analysis"], a: 0, why: "Corrective." },
  { q: "Changing a program for new hardware is:", opts: ["Adaptive", "Corrective", "Perfective", "Design"], a: 0, why: "Adaptive." },
  { q: "Making a program respond faster is:", opts: ["Perfective", "Corrective", "Adaptive", "Testing"], a: 0, why: "Perfective." },
  { q: "A reason for adaptive maintenance:", opts: ["A change in legislation", "A typing error", "A bug", "A faster response"], a: 0, why: "Law changed." },
  { q: "A suitable way of documenting variables:", opts: ["An identifier table", "A beta test", "A stub", "A loop"], a: 0, why: "Identifier table." },
  { q: "Maintenance is in the life cycle:", opts: ["After testing and release", "Before analysis", "Instead of design", "Only for new programs"], a: 0, why: "Last stage." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Corrective", "Fix faults."],
  ["Adaptive", "Adapt to a change in the environment."],
  ["Perfective", "Improve without changing function."],
  ["Legislation", "A reason for adaptive."],
  ["Identifier table", "Documents variables."],
  ["Documentation", "Helps the maintenance programmer."],
  ["Retest", "After every change."],
  ["Maintenance", "The last life cycle stage."],
] });
