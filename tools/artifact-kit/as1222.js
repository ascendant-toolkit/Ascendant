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
  const draw = (s) => { const k = Math.round(s.i); const N = ["S1", "S2", "S3"]; const cur = [0, 1, 1, 2][k]; let o = ""; N.forEach((n, i) => o += SV.circle(50 + i * 110, 50, 24, i === cur ? "f3" : "cell") + SV.text(50 + i * 110, 54, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })); o += SV.text(14, 100, ["Start in S1.", "Input A | output X: move to S2.", "Input A again: a loop on S2, no output.", "Input B | output W: move to S3."][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 330, h: 112, label: "States", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The system starts in S1.", "The first input moves it to S2.", "The same input on S2 is a loop.", "Input B changes the state to S3."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.circle(70, 50, 24, k === 0 ? "f3" : "cell") + SV.text(70, 54, "S2", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); o += SV.circle(220, 50, 24, k === 1 ? "f3" : "cell") + SV.circle(220, 50, 19, "cell") + SV.text(220, 54, "S3", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); o += SV.text(14, 104, ["Loop: the input leaves the system in S2.", "Final state: S3 is a double circle with no way out."][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 320, h: 118, label: "Loop and final state", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["A loop leaves the state unchanged.", "The final or halting state."].map((c, i) => ({ cap: c, s: { i } })) });
})();

const MACH = {
  1: { start: "S1", T: { S1: { "Low level detected": ["S2", "Activate pump"], "Normal level detected": ["S3", ""] }, S2: { "Low level detected": ["S2", ""], "Normal level detected": ["S3", "Deactivate pump"] }, S3: {} } },
  2: { start: "S1", T: { S1: { "Button-Y": ["S3", ""], "Button-X": ["S2", ""] }, S2: { "Button-Z": ["S1", ""], "Button-Y": ["S4", "Output-A"] }, S3: { "Button-Z": ["S3", "Output-C"], "Button-Y": ["S4", ""] }, S4: { "Button-Z": ["S2", "Output-B"] } } },
  3: { start: "Heaters Off", T: { "Heaters Off": { "Temp < 10": ["Heaters On", "switch on"], "Temp >= 10": ["Heaters Off", ""] }, "Heaters On": { "Temp > 20": ["Heaters Off", "switch off"], "Temp <= 20": ["Heaters On", ""] } } }
};
function mkSim(i, host, svg) {
  const M = MACH[i]; const box = $("#sim" + i); const out = $("#simo" + i); const bar = $("#simb" + i); let cur = M.start, log = [];
  const paint = (msg) => { box.querySelectorAll("circle[data-n]").forEach((c) => c.style.fill = c.getAttribute("data-n") === cur ? "var(--accent, #fcd34d)" : "var(--surface)"); const outs = log.filter((x) => x).length; out.innerHTML = `<div class="verdict">Current state: <b>${cur}</b>. ${msg || ""}</div><p>Inputs so far: ${log.length}. Outputs so far: <b>${outs}</b>.</p>`; };
  const inputs = [...new Set(Object.values(M.T).flatMap((o) => Object.keys(o)))];
  inputs.forEach((inp) => { const b = document.createElement("button"); b.textContent = inp; b.onclick = () => { const t = (M.T[cur] || {})[inp]; if (!t) return paint(`No transition for ${inp} from ${cur}: nothing happens.`); const was = cur; cur = t[0]; log.push(t[1]); paint(`${was} → ${cur}${t[1] ? ", output: " + t[1] : ", no output"}${was === cur ? " (a loop)" : ""}.`); }; bar.appendChild(b); });
  const r = document.createElement("button"); r.textContent = "Reset"; r.onclick = () => { cur = M.start; log = []; paint("Back to the start."); }; bar.appendChild(r); paint("Choose an input.");
}
[1, 2, 3].forEach((i) => mkSim(i));
btnTable("trB", "trO", [
  ["S1, A1, X1, S2", "Arrow S1 to S2 labelled A1 | X1", "a change of state with an output"],
  ["S2, A3, none, S1", "Arrow S2 to S1 labelled A3", "no output: only the input is written"],
  ["S5, A1, X1, S5", "A loop on S5 labelled A1 | X1", "current state equals next state"],
  ["S3, A9, X9, S4", "Arrow S3 to S4 labelled A9 | X9", "S3 is the current state, S4 the next"]
], ["Table row", "On the diagram", "Why"]);
Lib.classify($("#cl1"), { prompt: "In the pump diagram, which is it?", buckets: [{"label": "Start"}, {"label": "Final state"}, {"label": "Output"}, {"label": "Loop"}], items: [{"text": "The dot with an arrow into S1", "b": 0}, {"text": "S3, drawn as a double circle", "b": 1}, {"text": "Activate pump", "b": 2}, {"text": "Low level detected on S2 returning to S2", "b": 3}, {"text": "Deactivate pump", "b": 2}, {"text": "The state with no transitions out", "b": 1}], done: "Dot start; double circle final; after the bar an output." });
Lib.classify($("#cl2"), { prompt: "Which belongs in a state-transition table?", buckets: [{"label": "Table column"}, {"label": "Not a column"}], items: [{"text": "Current state", "b": 0}, {"text": "Input", "b": 0}, {"text": "Output", "b": 0}, {"text": "Next state", "b": 0}, {"text": "The author's name", "b": 1}, {"text": "The number of marks", "b": 1}], done: "Current state, input, output, next state." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["State", "A circle"], ["Transition", "An arrow between states"], ["Start", "A filled dot and an arrow"], ["Final state", "A double circle"], ["Output", "After the bar on the label"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of tracing Input-A, Input-A, Input-B from S1 in order (using the four-state diagram).", items: ["Start in S1", "Input-A: output X, move to S2", "Input-A: no output, loop on S2", "Input-B: output W, move to S3", "End in S3"], done: "Follow each arrow." });
Lib.calc($("#c1"), { qs: [
  {"q": "In the pump diagram, how many transitions result in a different state?", "a": 3, "unit": "", "tol": 0.01, "hint": "S1 to S2, S1 to S3, S2 to S3.", "sol": "<b>3</b>."},
  {"q": "In the pump diagram, how many transitions have an associated output?", "a": 2, "unit": "", "tol": 0.01, "hint": "Activate pump and Deactivate pump.", "sol": "<b>2</b>."},
  {"q": "In the pump diagram from S1, four Low level detected inputs occur. How many outputs?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the first leaves S1.", "sol": "<b>1</b> (and the state is S2)."},
  {"q": "The button diagram uses Button-X, Button-Y and Button-Z. How many different inputs?", "a": 3, "unit": "", "tol": 0.01, "hint": "Count the distinct labels.", "sol": "<b>3</b>."},
  {"q": "A table has 9 rows. How many arrows does the diagram have?", "a": 9, "unit": "", "tol": 0.01, "hint": "One per row, including loops.", "sol": "<b>9</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A loop on a state means:", opts: ["The input does not change the state", "The system stops", "An error", "The start"], a: 0, why: "Same state." },
  { q: "A final state is drawn as:", opts: ["A double circle", "A diamond", "A dot", "A rectangle"], a: 0, why: "Double circle." },
  { q: "The label after the bar is the:", opts: ["Output", "Input", "State", "Start"], a: 0, why: "Output." },
  { q: "The X on the start arrow should be labelled:", opts: ["Start", "S0", "Input", "Halt"], a: 0, why: "Start." },
  { q: "In a trace table the current state of a row is:", opts: ["The next state of the previous row", "Always S1", "The input", "The output"], a: 0, why: "Chain." },
  { q: "A state-transition diagram is produced in:", opts: ["The design stage", "Coding", "Testing", "Maintenance"], a: 0, why: "Design." },
] });
Lib.cards($("#fc1"), { cards: [
  ["State", "A circle in the diagram."],
  ["Transition", "An arrow between states."],
  ["Input | Output", "The label on an arrow."],
  ["Loop", "An arrow from a state to itself."],
  ["Start", "A dot and an arrow."],
  ["Final state", "A double circle."],
  ["Table row", "Current state, input, output, next state."],
  ["none", "Write it when there is no output."],
] });
