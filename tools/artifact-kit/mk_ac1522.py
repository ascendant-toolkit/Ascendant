"""A Level CS syllabus 15.2.2: flip-flops (SR and JK). Run: python3 tools/artifact-kit/mk_ac1522.py"""
from ak15 import *

SRNOR = circuit([("R", 40), ("S", 160)], [("Q", "NOR", ["R", "Qb"], 0, 50), ("Qb", "NOR", ["Q", "S"], 0, 150)], outs=["Q", "Qb"], feedback={("Q", 1): 105, ("Qb", 0): 95})
SRNAND = circuit([("S", 40), ("R", 160)], [("Q", "NAND", ["S", "Qb"], 0, 50), ("Qb", "NAND", ["Q", "R"], 0, 150)], outs=["Q", "Qb"], feedback={("Q", 1): 105, ("Qb", 0): 95})
JK = circuit([("J", 32), ("CLK", 110), ("K", 188)],
             [("G1", "NAND", ["J", "CLK", "Qb"], 0, 50), ("G2", "NAND", ["K", "CLK", "Q"], 0, 170), ("Q", "NAND", ["G1", "Qb"], 1, 60), ("Qb", "NAND", ["G2", "Q"], 1, 160)],
             outs=["Q", "Qb"], feedback={("G1", 2): 92, ("G2", 2): 128, ("Q", 1): 108, ("Qb", 0): 112})

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>flip-flop</b> is a circuit that <b>stores one bit</b>: its output stays at 0 or 1 after the inputs have gone back to 0, so it is a basic memory element. An <b>SR flip-flop</b> is two NOR (or two NAND) gates with their outputs fed back to each other's inputs; the <b>S</b> (set) input makes Q = 1, the <b>R</b> (reset) input makes Q = 0, and with both inputs at 0 the stored value is kept. Setting S and R to 1 together is <b>not allowed</b> because the outputs are no longer opposites and the result is unpredictable. A <b>JK flip-flop</b> adds a clock and removes that problem: J = K = 1 makes the output <b>toggle</b> (swap) on each clock pulse. Many flip-flops side by side make a <b>register</b>, one flip-flop per bit.</p></div>

  <h2>1 · The SR flip-flop</h2>
  <p>Two NOR gates are cross-coupled: the output of each gate goes to an input of the other. This feedback is what lets the circuit remember. Q and its inverse Q̄ (written <span class="bx">~Q</span> in the exam, and Qb on the diagram below) are the two outputs.</p>
  ''' + circ_html(SRNOR, cap="SR flip-flop from two NOR gates") + '''
  <div class="tw"><table class="t mono">
    <tr><th>S</th><th>R</th><th>Q next</th><th>Effect</th></tr>
    <tr><td>0</td><td>0</td><td>no change</td><td>the stored bit is <b>kept</b></td></tr>
    <tr><td>1</td><td>0</td><td>1</td><td><b>set</b>: store a 1</td></tr>
    <tr><td>0</td><td>1</td><td>0</td><td><b>reset</b>: store a 0</td></tr>
    <tr><td>1</td><td>1</td><td>not defined</td><td><b>invalid</b>: both outputs become 0, then the final value depends on which gate is faster</td></tr>
  </table></div>
  <p>Walk through the memory: with S = 0 and R = 0 and Q = 1, the top NOR gate has inputs R = 0 and Q̄ = 0, so its output Q = 1 is kept; the bottom gate has inputs S = 0 and Q = 1 so Q̄ = 0, which keeps the top gate steady. Each gate's output holds the other gate's input at the value that keeps it that way.</p>
  <h3>The NAND version</h3>
  <p>The same circuit can be built from two NAND gates. NAND gates are active-low: the inputs are 1 when idle, and a 0 on the S input sets the flip-flop. The mark scheme accepts either NAND or NOR as long as the two gates are the same type, are cross-connected, and the inputs are labelled.</p>
  ''' + circ_html(SRNAND, cap="SR flip-flop from two NAND gates") + '''

  <h2>2 · The JK flip-flop</h2>
  <p>A JK flip-flop has inputs J (like set), K (like reset) and a <b>clock</b>. The inputs are only looked at when the clock pulses, so the circuit changes in step with the rest of the computer. Unlike the SR flip-flop, <b>J = K = 1 is allowed</b>: the output <b>toggles</b>.</p>
  ''' + circ_html(JK, cap="JK flip-flop from NAND gates") + '''
  <div class="tw"><table class="t mono">
    <tr><th>J</th><th>K</th><th>Q after the clock pulse</th><th>Effect</th></tr>
    <tr><td>0</td><td>0</td><td>Q (unchanged)</td><td>keep</td></tr>
    <tr><td>0</td><td>1</td><td>0</td><td>reset</td></tr>
    <tr><td>1</td><td>0</td><td>1</td><td>set</td></tr>
    <tr><td>1</td><td>1</td><td>NOT Q</td><td><b>toggle</b></td></tr>
  </table></div>
  <p>The diagram shows the idea: two NAND gates guarded by the clock feed an SR flip-flop. The extra feedback from Q and Q̄ to the guarding gates is what makes J = K = 1 toggle instead of being invalid. (A real device is built so that it toggles once per clock pulse.)</p>

  <h2>3 · Why flip-flops matter</h2>
  <ul>
    <li><b>One flip-flop stores one bit.</b> The exam's purpose answer: "to store a binary digit".</li>
    <li>A group of flip-flops makes a <b>register</b>: eight flip-flops hold a byte.</li>
    <li>Static RAM (SRAM, used in cache) is built from flip-flop-style cells, so it keeps its contents without refreshing but uses more transistors than DRAM.</li>
    <li>Flip-flops are <b>sequential</b> logic: the output depends on the inputs <b>and the stored state</b>. A gate circuit with no feedback is <b>combinational</b>: the output depends only on the current inputs.</li>
  </ul>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Using two different gate types, or two gates with no cross-feedback. The two outputs must each go back to the other gate.</li>
    <li>Forgetting to label the inputs S and R (or Set and Reset). A labelled-inputs mark is separate.</li>
    <li>Mixing up which input goes to which gate. With NOR gates, R is on the gate that gives Q. With NAND gates, S is on the gate that gives Q.</li>
    <li>Saying the S = R = 1 case "resets" or "sets" it. It is invalid: the result is not defined.</li>
    <li>Describing the purpose as "to remember" or "to be a switch". Say it stores one binary digit (bit).</li>
  </ul>
'''

watch = '''
  <h2>1 · An SR flip-flop remembers</h2>
  <p>Press Play. Watch what happens to Q when S goes back to 0: it stays at 1.</p>
  <div id="stA"></div>
  <h2>2 · A JK flip-flop on each clock pulse</h2>
  <div id="stB"></div>
  <h2>3 · Eight flip-flops make a register</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · SR flip-flop</h2>
  <p>Switch S and R on and off. See how Q changes and what happens when you let go.</p>
  <div class="card"><div class="btnrow" id="srB"></div><div id="srS"></div><div class="verdict" id="srV"></div></div>
  <h2>Lab 2 · JK flip-flop</h2>
  <p>Choose J and K, then pulse the clock a few times.</p>
  <div class="card"><div class="btnrow" id="jkB"></div><div id="jkS"></div><div class="verdict" id="jkV"></div></div>
  <h2>Lab 3 · A register</h2>
  <p>Each box is one flip-flop. Click a box to set or reset it and see the byte stored.</p>
  <div class="card"><div class="btnrow" id="rgB"></div><div class="verdict" id="rgV"></div></div>
'''

practise = '''
  <h2>1 · What does the SR input combination do?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which statement is true of?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the SR flip-flop set sequence in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Registers in the processor", "The accumulator and other registers are rows of flip-flops, one for each bit, holding the value in use between clock cycles.", "a register is a group of flip-flops.") +
rw("Cache memory", "Static RAM uses flip-flop-style cells. It is fast because it needs no refresh, which is why it is used for the cache.", "a flip-flop stores a bit without refreshing, but uses more transistors than DRAM.") +
rw("A switch that does not bounce", "A mechanical switch can flicker on and off when pressed. An SR latch after the switch settles the signal into one clean change.", "the SR flip-flop remembers the last input.") +
rw("A light that toggles each time you press a button", "A JK flip-flop with J = K = 1 swaps its output on every clock pulse: on, off, on, off. Chains of them make counters.", "J = K = 1 toggles the output.") +
rw("A burglar alarm that stays on", "Once a sensor trips the alarm it stays on even if the door is closed again, until a reset button is pressed. That is a set and a reset on a flip-flop.", "S sets and keeps Q = 1 until R resets it.")
)

where = [("O/N 2022", "32", "8(a), 8(b), 8(c)", "4 + 1 + 3", "Draw an SR flip-flop and label the inputs; state the purpose of a flip-flop; simplify a Boolean expression using De Morgan's laws (the Boolean part is on the 15.2.3 page)")]

past = '''  <p class="note">Flip-flops have been examined once in Papers 3 and 4 between May/June 2021 and Oct/Nov 2025: Oct/Nov 2022, Paper 32. The JK flip-flop has never been asked. Expect a drawing question of the same kind, so practise drawing both versions of the SR flip-flop. The question is reworded; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w22", "32", "Q8(a)(b)"), "4 + 1 marks", "Draw / State",
  "(a) Draw a logic circuit for an SR flip-flop and label the inputs. (The paper gives a blank box with two inputs on the left, each with a dotted line to label, and outputs Q and Q-bar on the right.) (b) State the purpose of a flip-flop.",
  "Two NOR or two NAND gates, outputs crossed over to the other gate's input, S and R labelled.",
  "<p><b>(a)</b> " + mks(["One correct NAND or NOR gate with two separate inputs and one output", "A second gate of the same type with two separate inputs and one output", "Correct connections between the gates (each output goes to an input of the other gate)", "Inputs correctly labelled (S/Set and R/Reset)"]) + "</p><p>Either version scores full marks. With NOR gates, R is on the gate that gives Q:</p>" + circ_html(SRNOR, cap="NOR version") + "<p>With NAND gates, S is on the gate that gives Q:</p>" + circ_html(SRNAND, cap="NAND version") + "<p><b>(b)</b> " + mks(["To store a binary digit / a single bit"], "a") + "</p>", "Using one NOR and one NAND gate, or drawing the two gates without the cross-over feedback. Both gates must be the same type and each output must feed the other gate.")

review = req("2 marks", "State", "State the output Q of an SR flip-flop made from NOR gates when S = 1 and R = 0, and then when S and R both return to 0.", "Set, then hold.", "<p>" + mks(["When S = 1 and R = 0, Q = 1 (set)", "When S and R return to 0, Q stays at 1 (the bit is stored)"]) + "</p>", None) + req("2 marks", "Explain", "Explain why S = 1 and R = 1 must be avoided in an SR flip-flop.", "Think about the two outputs.", "<p>" + mks(["Both outputs go to 0, so Q and its inverse are no longer opposites", "When the inputs return to 0 the final state is unpredictable (depends on which gate responds first)"]) + "</p>", None) + req("3 marks", "Complete", "A JK flip-flop has Q = 0. J = 1 and K = 1 and the clock pulses three times. State Q after each pulse and name the behaviour.", "Toggle.", "<p>" + mks(["After pulse 1: Q = 1", "After pulse 2: Q = 0 and after pulse 3: Q = 1", "J = K = 1 makes the output toggle on each clock pulse"]) + "</p>", None) + req("2 marks", "Describe", "Describe how a group of flip-flops can be used to store the byte 10110001.", "One bit per flip-flop.", "<p>" + mks(["Eight flip-flops are used, one for each bit of the byte", "Each is set (Q = 1) or reset (Q = 0) to match its bit, and keeps that value until changed"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between combinational and sequential logic circuits.", "Does the stored state matter?", "<p>" + mks(["In a combinational circuit the output depends only on the current inputs", "In a sequential circuit (such as a flip-flop) the output depends on the inputs and on the stored previous state"]) + "</p>", None)

exam = exam20("Part 1 is the one real 9618 flip-flop question (Paper 3, Oct/Nov 2022). Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Two gates, same type.", "Two NORs or two NANDs, never one of each."),
  ("Cross the outputs.", "Each gate's output goes to an input of the other gate."),
  ("Label S and R.", "Inputs labelled Set/S and Reset/R, outputs Q and Q-bar."),
  ("Purpose: store one bit.", "It stores a single binary digit."),
  ("S = R = 1 is invalid.", "Never say it sets or resets."),
  ("JK: J = K = 1 toggles.", "Output swaps on each clock pulse."),
], [
  ("a flip-flop", "A circuit that stores one bit."),
  ("an SR flip-flop", "Two cross-coupled NOR or NAND gates with a set input and a reset input."),
  ("a JK flip-flop", "A clocked flip-flop where J = K = 1 toggles the output."),
  ("a register", "A group of flip-flops holding the bits of one value."),
], [("State", "Give the answer only."), ("Draw", "A clear labelled diagram; use a ruler for the wires."), ("Explain", "Give the reason as well."), ("Distinguish", "Say how the two things differ.")]) + FC

js = AKJS + AK20JS + AK15JS + "const GSR = " + gjson(SRNOR) + ";\n" + r'''
function srStep(st, S, R) { let Q = st.Q, Qb = st.Qb; for (let i = 0; i < 6; i++) { const nq = (R | Qb) ? 0 : 1, nqb = (S | nq) ? 0 : 1; Q = nq; Qb = nqb; } return { Q, Qb }; }
function srVals(st, S, R) { return { R, S, Q: st.Q, Qb: st.Qb }; }
(function () {
  const seq = [[0, 0], [1, 0], [0, 0], [0, 1], [0, 0]]; let st = { Q: 0, Qb: 1 }; const hist = [{ st, S: 0, R: 0 }];
  seq.forEach(([S, R], i) => { st = srStep(st, S, R); hist.push({ st, S, R }); });
  const draw = (s) => { const h = hist[Math.round(s.i) + 1]; return circFit(GSR, srVals(h.st, h.S, h.R), 560, { vals: false }); };
  const caps = ["Start: Q = 0, S = 0 and R = 0. Nothing is stored yet (Q = 0).", "S goes to 1: the flip-flop is <b>set</b>. Q becomes 1.", "S returns to 0. Q is <b>still 1</b>: the flip-flop has remembered.", "R goes to 1: the flip-flop is <b>reset</b>. Q becomes 0.", "R returns to 0. Q stays 0. The bit is stored again, this time as 0."];
  Lib.stepper($("#stA"), { w: 560, h: Math.round(SRNOR.h * 2.2) + 12, label: "SR flip-flop remembering", base: { i: 0 }, draw, tween: 150, dwell: 2800, steps: caps.map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const ev = [{ j: 1, k: 0, q: 1, c: "J = 1, K = 0, clock pulse: Q is <b>set</b> to 1." }, { j: 0, k: 0, q: 1, c: "J = 0, K = 0, clock pulse: Q <b>keeps</b> its value, 1." }, { j: 1, k: 1, q: 0, c: "J = 1, K = 1, clock pulse: Q <b>toggles</b> from 1 to 0." }, { j: 1, k: 1, q: 1, c: "J = 1, K = 1, another pulse: Q toggles from 0 to 1." }, { j: 0, k: 1, q: 0, c: "J = 0, K = 1, clock pulse: Q is <b>reset</b> to 0." }];
  const draw = (s) => { const i = Math.round(s.i), e = ev[i]; let o = SV.rect(210, 20, 180, 150, "cell", { rx: 10 }) + SV.text(300, 46, "JK flip-flop", "lbl bd", { "text-anchor": "middle" });
    o += SV.text(60, 70, "J = " + e.j, "lbl bd") + SV.text(60, 110, "K = " + e.k, "lbl bd") + SV.text(60, 150, "clock pulse " + (i + 1), "lbl bd t1") + SV.path("M150,66 H210 M150,106 H210 M150,146 H210", "ax");
    o += SV.rect(430, 70, 100, 50, e.q ? "cell-ok" : "cell", { rx: 8 }) + SV.text(480, 103, "Q = " + e.q, "lbl bd", { "text-anchor": "middle" }) + SV.path("M390,95 H430", "ax");
    o += SV.text(60, 200, "Q before the pulse: " + (i === 0 ? 0 : ev[i - 1].q), "sm"); return o; };
  Lib.stepper($("#stB"), { w: 640, h: 215, label: "JK flip-flop", base: { i: 0 }, draw, tween: 150, dwell: 2800, steps: ev.map((e, i) => ({ cap: e.c, s: { i } })) });
})();
(function () {
  const target = [1, 0, 1, 1, 0, 0, 0, 1];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; target.forEach((b, i) => { const on = i < k; o += SV.rect(30 + i * 80, 30, 66, 60, on ? (b ? "cell-ok" : "cell-warn") : "cell", { rx: 8 }) + SV.text(63 + i * 80, 68, on ? String(b) : "?", "lbl bd", { "text-anchor": "middle", style: "font-size:22px;font-family:var(--mono)" }) + SV.text(63 + i * 80, 110, "bit " + (7 - i), "sm", { "text-anchor": "middle" }); });
    o += SV.text(30, 150, k === 8 ? "stored: 10110001 = " + parseInt(target.join(""), 2) + " (hex " + hx(parseInt(target.join(""), 2)) + ")" : "each flip-flop stores one bit", "lbl bd t3"); return o; };
  Lib.stepper($("#stC"), { w: 680, h: 170, label: "A register of eight flip-flops", base: { i: 0 }, draw, tween: 150, dwell: 1200, steps: [0, 1, 2, 3, 4, 5, 6, 7, 8].map((i) => ({ cap: i === 0 ? "A register is a row of flip-flops. Each will store one bit of the byte." : i === 8 ? "All eight bits are stored: 10110001. They stay until new values are loaded." : "Bit " + (8 - i) + " is stored in its own flip-flop (set for 1, reset for 0).", s: { i } })) });
})();

(function () {
  let S = 0, R = 0, st = { Q: 0, Qb: 1 }, note = "";
  const b = $("#srB");
  const paint = () => { $("#srS").innerHTML = circSvg(SRG, srVals(st, S, R), { vals: false }); b.querySelectorAll("button").forEach((x, i) => { const v = i ? R : S; x.textContent = (i ? "R" : "S") + " = " + v; x.className = v ? "on" : ""; });
    $("#srV").innerHTML = S && R ? "S = R = 1 is <b>invalid</b>: both outputs are 0. When you release them the result is unpredictable." : S ? "Set: Q = 1." : R ? "Reset: Q = 0." : "S = 0 and R = 0: the flip-flop <b>keeps</b> its value, Q = " + st.Q + "." + note; };
  const SRG = GSR;
  [0, 1].forEach((i) => { const x = document.createElement("button"); x.onclick = () => { const was = S && R; if (i) R ^= 1; else S ^= 1; st = srStep(st, S, R); note = was && !S && !R ? " (it was set to 0 by R = S = 1 being released, so the result here is arbitrary)" : ""; paint(); }; b.appendChild(x); });
  paint();
})();
(function () {
  let J = 0, K = 0, Q = 0, n = 0; const hist = [];
  const b = $("#jkB");
  const paint = () => { let o = SV.rect(150, 15, 170, 110, "cell", { rx: 10 }) + SV.text(235, 40, "JK flip-flop", "lbl bd", { "text-anchor": "middle" }) + SV.text(30, 56, "J = " + J, "lbl bd") + SV.text(30, 96, "K = " + K, "lbl bd") + SV.path("M100,52 H150 M100,92 H150", "ax") + SV.rect(350, 55, 100, 46, Q ? "cell-ok" : "cell", { rx: 8 }) + SV.text(400, 85, "Q = " + Q, "lbl bd", { "text-anchor": "middle" }) + SV.path("M320,78 H350", "ax");
    $("#jkS").innerHTML = `<svg viewBox="0 0 480 140" style="width:480px;max-width:100%;display:block">` + o + "</svg>";
    b.querySelectorAll("button").forEach((x, i) => { if (i === 0) x.textContent = "J = " + J, x.className = J ? "on" : ""; if (i === 1) x.textContent = "K = " + K, x.className = K ? "on" : ""; if (i === 2) x.textContent = "Clock pulse"; });
    $("#jkV").innerHTML = n ? "After " + n + " pulse" + (n > 1 ? "s" : "") + " the outputs have been: " + hist.join(", ") + "." + (J && K ? " J = K = 1 toggles on every pulse." : "") : "Click Clock pulse. J and K are only looked at when the clock pulses."; };
  [0, 1, 2].forEach((i) => { const x = document.createElement("button"); x.onclick = () => { if (i === 0) J ^= 1; else if (i === 1) K ^= 1; else { Q = J && K ? 1 - Q : J ? 1 : K ? 0 : Q; n++; hist.push(Q); if (hist.length > 12) hist.shift(); } paint(); }; b.appendChild(x); });
  paint();
})();
(function () {
  const bits = [0, 0, 0, 0, 0, 0, 0, 0]; const b = $("#rgB");
  const paint = () => { b.querySelectorAll("button").forEach((x, i) => { x.textContent = "bit " + (7 - i) + " = " + bits[i]; x.className = bits[i] ? "on" : ""; }); const v = parseInt(bits.join(""), 2); $("#rgV").innerHTML = "Stored: <b>" + bits.join("") + "</b> = " + v + " (hex " + hx(v) + ")"; };
  bits.forEach((_, i) => { const x = document.createElement("button"); x.onclick = () => { bits[i] ^= 1; paint(); }; b.appendChild(x); }); paint();
})();
''' + CLASSIFY("cl1", "Which effect does the SR input combination have?", ["Keeps Q", "Sets Q to 1", "Resets Q to 0", "Invalid"],
  [("S = 0, R = 0", 0), ("S = 1, R = 0", 1), ("S = 0, R = 1", 2), ("S = 1, R = 1", 3)],
  "00 keep, 10 set, 01 reset, 11 invalid (NOR version).") + CLASSIFY("cl2", "Is the statement about an SR or a JK flip-flop?", ["SR flip-flop", "JK flip-flop"],
  [("Has set and reset inputs but no clock in its basic form", 0), ("Has a clock input", 1), ("An input of 1 and 1 is not allowed", 0), ("An input of 1 and 1 makes the output toggle", 1), ("Is made of two cross-coupled NOR or NAND gates", 0)],
  "SR: set and reset, 11 invalid. JK: clocked, 11 toggles.") + MATCH([
  ["Flip-flop", "A circuit that stores one bit"], ["Set", "Makes Q = 1"], ["Reset", "Makes Q = 0"], ["Toggle", "Output swaps on each clock pulse"], ["Register", "A group of flip-flops holding one value"]]) + ORDER(
  "Put the steps in order for storing a 1 in an SR flip-flop (NOR version).",
  ["S goes to 1 (R stays 0)", "Q becomes 1", "S returns to 0", "Q stays at 1: the bit is stored"],
  "Set, output changes, set released, value kept.") + CALC([
  {"q": "How many flip-flops are needed to store one byte?", "a": 8, "unit": "", "tol": 0.01, "hint": "One bit per flip-flop.", "sol": "<b>8</b>."},
  {"q": "A JK flip-flop has Q = 0 and J = K = 1. What is Q after three clock pulses?", "a": 1, "unit": "", "tol": 0.01, "hint": "1, 0, 1.", "sol": "<b>1</b>."},
  {"q": "How many flip-flops would store a 16-bit word?", "a": 16, "unit": "", "tol": 0.01, "hint": "One per bit.", "sol": "<b>16</b>."},
  {"q": "An SR flip-flop with Q = 1 gets S = 0 and R = 0. What is Q?", "a": 1, "unit": "", "tol": 0.01, "hint": "It remembers.", "sol": "<b>1</b>."},
  {"q": "How many gates are in an SR flip-flop?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two NOR or two NAND.", "sol": "<b>2</b>."}]) + MCQ([
  ("What does a flip-flop store?", ["One bit", "One byte", "A program", "A character set"], 0, "One binary digit."),
  ("Which gates can make an SR flip-flop?", ["One AND, one OR", "Two NOR or two NAND", "Two XOR", "Three NOT"], 1, "Same type, cross-connected."),
  ("In a NOR SR flip-flop, S = 1 and R = 0 gives:", ["Q = 0", "Q = 1", "Invalid", "No change"], 1, "Set."),
  ("The JK flip-flop with J = K = 1 on a clock pulse:", ["Resets", "Sets", "Toggles", "Is invalid"], 2, "Toggle."),
  ("A circuit whose output depends on stored state is:", ["Combinational", "Sequential", "Parallel", "Serial"], 1, "Sequential."),
  ("A register is made of:", ["Flip-flops", "Resistors only", "Hard disk sectors", "Capacitors only"], 0, "One flip-flop per bit.")], "qz1") + CARDS([
  ("Flip-flop", "Stores one bit. Sequential, uses feedback."), ("SR", "Two cross-coupled NOR or NAND gates. S sets, R resets, 11 invalid."), ("JK", "Clocked. J set, K reset, 11 toggle."), ("Register", "Flip-flops side by side, one per bit."),
  ("Combinational", "Output depends only on the current inputs."), ("Sequential", "Output depends on the inputs and stored state."), ("SRAM", "Flip-flop-style cells; no refresh needed."), ("Drawing", "Same gate type, crossed outputs, labelled S and R.")])

build("ac1522", "ac-15-2-2-flip-flops", "Flip-flops", EYA("15.2.2"),
  "SR and JK flip-flops, how they store a bit and how a register is built; animations, labs and the one real Paper 3 flip-flop question (Oct/Nov 2022).",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.2 Boolean algebra and logic circuits"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
