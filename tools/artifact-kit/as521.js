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
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 110, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 55, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, "Source code", true) + B(190, "Compiler", k >= 1) + B(360, k >= 3 ? "Executable" : "Errors?", k >= 2) + SV.path("M130,62 H190", "ax") + SV.path("M300,62 H360", "ax");
    o += SV.text(240, 125, ["", "the compiler reads ALL the code", "it reports all errors together (none here)", "an executable file runs without the source code"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 150, label: "Compiler", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [0, 1, 2, 3].map((i) => ({ cap: ["The programmer finishes writing the source code.", "The <b>compiler</b> checks all of it at the same time.", "All errors are reported together; if none, translation continues.", "The result is an <b>executable file</b>."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 5; i++) o += SV.rect(30, 20 + i * 28, 240, 24, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 4 }) + SV.text(40, 37 + i * 28, "line " + (i + 1), "lbl") + (i === 2 ? SV.text(180, 37 + i * 28, "error!", "lbl bd") : "");
    o += SV.text(300, 80, k < 2 ? "line " + (k + 1) + " translated and run" : k === 2 ? "error: the interpreter STOPS" : "fixed: continues from line 3", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 170, label: "Interpreter", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Line 1 is translated and run.", "Line 2 is translated and run.", "Line 3 has an error: the interpreter <b>stops</b> and displays it.", "The programmer corrects it immediately; the interpreter continues from there.", "Lines 4 and 5 run."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(10, "Source code", true) + B(160, "Compiler", k >= 1) + B(310, "Intermediate code", k >= 2) + B(460, "Run by interpreter", k >= 3) + SV.path("M130,62 H160", "ax") + SV.path("M280,62 H310", "ax") + SV.path("M430,62 H460", "ax");
    o += SV.text(300, 125, ["", "the compiler produces intermediate code", "it can be copied to any platform", "interpreted at run time: optimised for that CPU"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 150, label: "Partial compilation", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [0, 1, 2, 3].map((i) => ({ cap: ["The source is compiled first...", "...to an intermediate code, not machine code.", "The same intermediate code works on different platforms.", "It is interpreted when run, and optimised for the CPU in use."][i], s: { i } })) });
})();

(function () {
  const prog = ["x ← 10", "y ← 5 +", "OUTPUT x", "z ← x / 0 ?", "OUTPUT y"], bad = [1, 3]; let fixed = false, msg = "";
  const paint = () => { $("#tlP").innerHTML = '<div class="tw"><table class="t mono">' + prog.map((l, i) => `<tr><td>${i + 1}</td><td>${l}</td><td>${bad.includes(i) && !(fixed && i === 1) ? "← error" : ""}</td></tr>`).join("") + "</table></div>"; $("#tlV").innerHTML = msg || "Choose a translator."; };
  const errs = () => bad.filter((i) => !(fixed && i === 1));
  $("#tl_c").onclick = () => { const e = errs(); msg = e.length ? `<b>Compiler</b> reports <b>all ${e.length} error(s)</b> (line ${e.map((i) => i + 1).join(" and line ")}). No executable file is produced and nothing runs.` : "<b>Compiler</b>: no errors, so an executable file is produced."; paint(); };
  $("#tl_i").onclick = () => { const e = errs(); msg = e.length ? `<b>Interpreter</b> runs line 1${e[0] > 1 ? " to " + e[0] : ""} then <b>stops at line ${e[0] + 1}</b> and reports that one error. Fix it and it continues.` : "<b>Interpreter</b>: all lines run."; paint(); };
  $("#tl_f").onclick = () => { fixed = true; msg = "Line 2 is fixed. Run the translators again: only line 4 is still wrong."; paint(); };
  $("#tl_r").onclick = () => { fixed = false; msg = ""; paint(); }; paint();
})();
btnTable("wB", "wO", [
  ["A finished app to be sold without its source code", "Compiler", "Executable file; source stays private"],
  ["Learning to program: fix each line as you go", "Interpreter", "Stops at the first error"],
  ["Testing half a program", "Interpreter", "Unfinished code can run"],
  ["Mnemonics such as LDD and ADD", "Assembler", "Assembly to machine code"],
  ["The same code on Windows and Mac", "Partially compiled", "Intermediate code interpreted on each platform"]
], ["Situation", "Translator", "Why"]);
(function () {
  let runs = 20; const paint = () => { const ct = 30, ir = 5; $("#rV").innerHTML = `Compile once (<b>${ct} s</b>) then each run takes about 1 s: <b>${ct + runs} s</b> for ${runs} runs. An interpreter translates each time: about 2 s per run, <b>${runs * 2} s</b>. ` + (ct + runs < runs * 2 ? "For many runs the compiled program wins." : "For a few runs the interpreter is quicker overall because there is no compile wait."); };
  Lib.slider($("#rS"), { id: "r1", label: "Number of runs ", min: 1, max: 60, value: runs, fmt: (x) => x, onInput: (v) => { runs = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Compiler or interpreter?", buckets: [{"label": "Compiler"}, {"label": "Interpreter"}], items: [{"text": "Translates all the code at the same time", "b": 0}, {"text": "Translates one line then runs it", "b": 1}, {"text": "Produces an executable file", "b": 0}, {"text": "Stops at the first error", "b": 1}, {"text": "Reports all errors together", "b": 0}, {"text": "Needs the source code every time the program runs", "b": 1}], done: "Compiler: whole program, executable. Interpreter: line by line." });
Lib.classify($("#cl2"), { prompt: "Which translator does the situation need?", buckets: [{"label": "Compiler"}, {"label": "Interpreter"}, {"label": "Assembler"}], items: [{"text": "Translate assembly code into machine code", "b": 2}, {"text": "A finished program to be sold without its source code", "b": 0}, {"text": "Testing a half-finished program one section at a time", "b": 1}, {"text": "Correcting errors in real time while developing", "b": 1}, {"text": "A program that must run quickly on many machines", "b": 0}, {"text": "Converting mnemonics such as LDD and ADD into binary", "b": 2}], done: "Assembler: assembly. Interpreter: development. Compiler: finished." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Compiler", "Translates the whole program and makes an executable"], ["Interpreter", "Translates and runs one line at a time"], ["Assembler", "Translates assembly language into machine code"], ["Executable file", "Machine code that runs without the source code"], ["Source code", "The program as the programmer wrote it"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the compiler stages in order.", items: ["The whole source code is read", "All the code is checked for errors", "Any errors are reported together", "If no errors, an executable file is produced", "The executable runs without the source code"], done: "Read, check, report, produce, run." });
Lib.calc($("#c1"), { qs: [
  {"q": "A program of 600 lines has an error on line 150. An interpreter runs line by line. How many lines does it execute before it stops (lines 1 to 149)?", "a": 149, "unit": "", "tol": 0.01, "hint": "Up to the line before the error.", "sol": "<b>149</b>."},
  {"q": "A compile takes 40 s. You change the code 12 times and recompile each time. Total compile time in minutes?", "a": 8, "unit": "min", "tol": 0.01, "hint": "12 × 40 s = 480 s.", "sol": "<b>8</b> min."},
  {"q": "A program of 600 lines has no errors. How many lines does the compiler translate before it produces the executable?", "a": 600, "unit": "", "tol": 0.01, "hint": "All of them.", "sol": "<b>600</b>."},
  {"q": "A compiler lists 5 errors, but 3 are false errors caused by one real error. How many real errors?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b>."},
  {"q": "A program of 100 lines contains errors at line 20 and line 60. How many errors does an interpreter report on the first run?", "a": 1, "unit": "", "tol": 0.01, "hint": "It stops at the first.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A compiler produces:", opts: ["An executable file", "No output", "Only error messages", "Assembly code"], a: 0, why: "Executable." },
  { q: "An interpreter:", opts: ["Translates line by line", "Translates all at once", "Makes an exe", "Is used only for assembly"], a: 0, why: "Line by line." },
  { q: "An assembler translates:", opts: ["Assembly language", "Python", "A website", "Machine code into text"], a: 0, why: "Assembly." },
  { q: "During development an interpreter is useful because:", opts: ["It stops at the first error and can be fixed immediately", "It makes the exe fast", "It hides the source code", "It needs no source code"], a: 0, why: "Real-time correction." },
  { q: "A drawback of a compiler:", opts: ["Must recompile after every change", "Can run partial code", "Reports one error only", "Is line by line"], a: 0, why: "Recompile." },
  { q: "Partial compilation helps programs:", opts: ["Run on different platforms", "Avoid any translator", "Use no CPU", "Skip testing"], a: 0, why: "Different platforms." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Translator", "Converts a program into machine code."],
  ["Assembler", "Assembly language to machine code."],
  ["Compiler", "Whole program; all errors; executable."],
  ["Interpreter", "Line by line; stops at first error."],
  ["Executable", "Runs without the source code."],
  ["Development", "Interpreter: debug line by line."],
  ["Finished program", "Compiler: runs faster, source hidden."],
  ["Partial compile", "Intermediate code interpreted; platform independent."],
] });
