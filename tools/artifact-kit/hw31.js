const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const rg = (x, y, w, h, name, val, hi, col = ACC) => SV.rect(x, y, w, h, "", { rx: 8, style: `fill:${hi ? "var(--soft)" : "var(--surface)"};stroke:${hi ? col : MUT};stroke-width:${hi ? 4 : 2}` }) + sm(x + w / 2, y + 17, name) + SV.text(x + w / 2, y + h - 12, val, "lbl bd", { "text-anchor": "middle", style: `fill:${hi ? col : "var(--ink)"}` });
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:4;${dash ? "stroke-dasharray:7 6" : ""}` }) + SV.arrowHead(x2, y2, x2 >= x1 ? "r" : "l", "").replace('class=""', `style="fill:${col}"`);
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });

/* ---------- 1. FDE cycle ---------- */
function fdeChart(s) {
  const k = Math.round(s.k);
  const pc = k >= 3 ? "101" : "100", mar = k >= 1 ? "100" : "–", mdr = k >= 3 ? "ADD 7" : "–", cir = k >= 4 ? "ADD 7" : "–", accv = k >= 6 ? "12" : "5";
  let o = panel(10, 10, 490, 320, "", MUT) + note(255, 32, "CPU", "t1");
  o += rg(25, 45, 100, 56, "PC", pc, k === 0 || k === 1 || k === 3 || k === 7) + rg(135, 45, 100, 56, "MAR", mar, k === 1 || k === 2) + rg(245, 45, 100, 56, "MDR", mdr, k === 3 || k === 4) + rg(355, 45, 120, 56, "CIR", cir, k === 4 || k === 5);
  o += panel(25, 135, 140, 80, "Control unit", k === 5 ? ACC : MUT) + sm(95, 178, k === 5 ? "decodes ADD 7" : "decodes, controls") + (k === 5 ? sm(95, 196, "add 7 to the ACC") : "");
  o += panel(180, 135, 140, 80, "ALU", k === 6 ? ACC : MUT) + sm(250, 180, k === 6 ? "5 + 7 = 12" : "arithmetic + logic");
  o += rg(335, 145, 140, 56, "ACC (accumulator)", accv, k === 6, GOOD);
  o += sm(255, 250, k === 7 ? "The PC now holds 101, so the next cycle fetches the next instruction." : "Registers are tiny, very fast stores inside the CPU.");
  o += chip(150, 275, 210, k <= 4 ? "FETCH" : k === 5 ? "DECODE" : k === 6 ? "EXECUTE" : "REPEAT", k <= 4 ? ACC : k === 5 ? "var(--warn)" : GOOD);
  const ab = k === 2 || k === 1 && false, db = k === 3, cb = k === 2;
  o += panel(570, 10, 180, 320, "RAM", MUT);
  [["100", "ADD 7"], ["101", "SUB 2"], ["102", "STORE"], ["103", "HALT"]].forEach((r, i) => { const hi = (k === 2 || k === 3) && i === 0; o += SV.rect(582, 45 + i * 62, 156, 50, "", { rx: 8, style: `fill:${hi ? "var(--soft)" : "var(--surface)"};stroke:${hi ? ACC : MUT};stroke-width:${hi ? 4 : 1.5}` }) + sm(612, 75 + i * 62, r[0]) + SV.text(690, 76 + i * 62, r[1], "lbl bd", { "text-anchor": "middle" }); });
  o += (ab ? arr(500, 80, 570, 80, ACC) : SV.line(500, 80, 570, 80, "", { style: `stroke:${MUT};stroke-width:2` })) + sm(535, 70, "address");
  o += (db ? arr(570, 170, 500, 170, ACC) : SV.line(500, 170, 570, 170, "", { style: `stroke:${MUT};stroke-width:2` })) + sm(535, 160, "data");
  o += (cb ? arr(500, 260, 570, 260, "var(--warn)") : SV.line(500, 260, 570, 260, "", { style: `stroke:${MUT};stroke-width:2` })) + sm(535, 250, cb ? "READ" : "control");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 340, label: "The fetch decode execute cycle", base: { k: 0 }, tween: 1, dwell: 4400, draw: fdeChart, steps: [
  { cap: "RAM holds the instructions. The <b>PC</b> holds <b>100</b>, the address of the next instruction. The <b>ACC</b> holds 5.", s: { k: 0 } },
  { cap: "<b>Fetch:</b> the address in the PC is copied to the <b>MAR</b>.", s: { k: 1 } },
  { cap: "The address goes along the <b>address bus</b>, and the <b>control bus</b> sends a read signal to RAM.", s: { k: 2 } },
  { cap: "The instruction <b>ADD 7</b> comes back along the <b>data bus</b> into the <b>MDR</b>. The <b>PC is incremented</b> to 101.", s: { k: 3 } },
  { cap: "The instruction is copied from the MDR into the <b>CIR</b>. Fetch is finished.", s: { k: 4 } },
  { cap: "<b>Decode:</b> the <b>control unit</b> works out what ADD 7 means, using the instruction set.", s: { k: 5 } },
  { cap: "<b>Execute:</b> the <b>ALU</b> adds 7 to the 5 in the <b>ACC</b>. The result, 12, is stored in the ACC.", s: { k: 6 } },
  { cap: "The cycle <b>repeats</b>. The PC holds 101, so the next instruction is fetched.", s: { k: 7 } },
] });

/* ---------- Lab 1: CPU performance ---------- */
(() => {
  const CORES = [1, 2, 4, 8, 16], CACHE = [1, 2, 4, 8, 16];
  let sc, sk, sa, sp;
  function upd() {
    if (!sc || !sk || !sa || !sp) return;
    const c = CORES[sc.get()], g = sk.get() / 10, ca = CACHE[sa.get()], p = sp.get() / 100;
    const speedup = 1 / ((1 - p) + p / c), cf = 1 + 0.08 * Math.log2(ca), perf = g * cf * speedup;
    $("#pa").textContent = fmtN(perf, 1); $("#pb").textContent = fmtN(g, 1) + " billion each";
    const bits = [];
    if (c > 1 && p < 0.3) bits.push(`Only ${Math.round(p * 100)}% of this program can be shared between cores, so the extra cores help very little.`);
    else if (c > 1) bits.push(`${c} cores let ${Math.round(p * 100)}% of the work run at the same time.`);
    else bits.push("With one core, instructions are processed one after another.");
    bits.push(`The clock runs ${fmtN(g, 1)} billion cycles per second on each core.`);
    bits.push(ca >= 8 ? "A large cache means fewer slow trips to RAM." : ca <= 2 ? "A small cache means more slow trips to RAM." : "A medium cache.");
    $("#pv").innerHTML = bits.join(" ");
  }
  sc = Lib.slider($("#p1"), { id: "pc1", label: "Cores", min: 0, max: 4, value: 1, fmt: (i) => CORES[i], onInput: upd });
  sk = Lib.slider($("#p2"), { id: "pc2", label: "Clock speed", min: 10, max: 50, value: 30, fmt: (v) => fmtN(v / 10, 1) + " GHz", onInput: upd });
  sa = Lib.slider($("#p3"), { id: "pc3", label: "Cache size", min: 0, max: 4, value: 1, fmt: (i) => CACHE[i] + " MB", onInput: upd });
  sp = Lib.slider($("#p4"), { id: "pc4", label: "Program that can use several cores", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: upd });
  upd();
})();


/* ---------- Lab 2: FDE trace ---------- */
(() => {
  const PROG = [["100", "ADD 7"], ["101", "SUB 2"], ["102", "ADD 10"], ["103", "HALT"]];
  const MICRO = ["Copy the address in the PC to the MAR", "Fetch: the instruction goes along the data bus into the MDR, and the PC is incremented", "Copy the instruction from the MDR to the CIR", "Decode: the control unit works out what the instruction means", "Execute: the ALU does the calculation and the result goes in the ACC"];
  let pc, mar, mdr, cir, acc, m, hi, halted;
  const el = $("#tr"), out = $("#trv");
  function reset() { pc = 100; mar = mdr = cir = "–"; acc = 5; m = 0; hi = ""; halted = false; draw(); out.textContent = "Press Step to run the first micro-step."; }
  function draw() {
    el.innerHTML = `<div class="grid2"><div class="readout">${[["PC", pc], ["MAR", mar], ["MDR", mdr], ["CIR", cir], ["ACC", acc]].map(([n, v]) => `<div style="${hi === n ? "outline:3px solid var(--accent);border-radius:8px" : ""}"><small>${n}</small><strong>${v}</strong></div>`).join("")}</div>
    <div><p class="lab">RAM</p><div class="tw"><table class="t">${PROG.map((r) => `<tr style="${+r[0] === +mar ? "background:var(--soft)" : ""}"><td>${r[0]}</td><td><b>${r[1]}</b></td></tr>`).join("")}</table></div></div></div>`;
  }
  function step() {
    if (halted) return;
    if (m === 0) { mar = pc; hi = "MAR"; }
    else if (m === 1) { mdr = PROG[pc - 100][1]; pc++; hi = "MDR"; }
    else if (m === 2) { cir = mdr; hi = "CIR"; }
    else if (m === 3) { hi = "CIR"; }
    else { const [op, n] = cir.split(" "); if (op === "ADD") acc += +n; else if (op === "SUB") acc -= +n; else halted = true; hi = "ACC"; }
    out.innerHTML = `<b>${MICRO[m]}.</b>` + (m === 4 ? (halted ? " HALT stops the program." : " Next cycle starts.") : "");
    m = (m + 1) % 5; draw();
  }
  $("#trs").onclick = step; $("#trr").onclick = reset; reset();
})();

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each CPU part to its job.", pairs: [
  ["ALU", "Carries out arithmetic and logic operations"], ["Control unit", "Decodes instructions and sends control signals"], ["PC", "Holds the address of the next instruction"], ["MAR", "Holds the address being read from or written to"],
  ["MDR", "Holds data or an instruction just fetched from memory"], ["CIR", "Holds the instruction being decoded and executed"], ["ACC", "Holds the result of a calculation"], ["Address bus", "Carries addresses from the CPU to memory"],
] });

Lib.order($("#o1"), { prompt: "Put these steps of one fetch–decode–execute cycle in order.", items: [
  "The address in the PC is copied to the MAR", "The PC is incremented", "The instruction is fetched from RAM into the MDR", "The instruction is copied from the MDR to the CIR", "The control unit decodes the instruction in the CIR", "The instruction is executed, for example the ALU result is stored in the ACC",
], done: "Fetch (PC, MAR, increment, MDR, CIR), decode, execute." });

Lib.classify($("#cl1"), { prompt: "Which part of the CPU does each effect describe?", buckets: [{ label: "Cores" }, { label: "Cache" }, { label: "Clock speed" }], items: [
  { text: "Several instructions processed at the same time", b: 0 }, { text: "Only helps if the software can share its work", b: 0 }, { text: "Each one runs its own fetch–decode–execute cycle", b: 0 },
  { text: "Keeps frequently used data close to the CPU", b: 1 }, { text: "Fewer slow trips to RAM", b: 1 }, { text: "Small, very fast memory", b: 1 },
  { text: "Measured in GHz", b: 2 }, { text: "Number of cycles each second", b: 2 }, { text: "Higher means more instructions per second", b: 2 },
], done: "Cores: at once. Cache: close by. Clock: how fast." });

Lib.classify($("#cl2"), { prompt: "Drag each item to embedded system or general-purpose computer.", buckets: [{ label: "Embedded system" }, { label: "General-purpose computer" }], items: [
  { text: "Washing machine controller", b: 0 }, { text: "Car engine management", b: 0 }, { text: "Vending machine", b: 0 }, { text: "Central heating thermostat", b: 0 }, { text: "Security alarm system", b: 0 },
  { text: "Laptop", b: 1 }, { text: "Desktop PC", b: 1 }, { text: "Many different programs can be installed", b: 1 }, { text: "Performs one dedicated function", b: 0 },
], done: "One job, built in, against many jobs." });

Lib.calc($("#c1"), { qs: [
  { q: "A CPU has a clock speed of 3 GHz. How many clock cycles does it run each second?", a: 3000000000, tol: 0.5, sol: "3 GHz = 3 × 10⁹ = 3,000,000,000 cycles per second.", hint: "1 GHz is a billion cycles per second." },
  { q: "Name the register that holds the address of the next instruction to be fetched (the abbreviation).", t: ["PC"], ph: "abbreviation", sol: "The program counter (PC)." },
  { q: "Name the register that holds the result of a calculation (the abbreviation).", t: ["ACC"], ph: "abbreviation", sol: "The accumulator (ACC)." },
  { q: "The PC holds 250. After one fetch, what does it hold?", a: 251, sol: "The PC is incremented after the fetch: 250 + 1 = 251." },
  { q: "The ACC holds 9. The instruction ADD 6 is executed. What does the ACC hold?", a: 15, sol: "9 + 6 = 15, stored back in the ACC." },
  { q: "A quad-core CPU runs at 2.5 GHz. How many cycles per second does each core run? (give the number)", a: 2500000000, tol: 0.5, sol: "2.5 GHz = 2,500,000,000 cycles per second per core." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which register holds the instruction that is being decoded?", opts: ["PC", "MAR", "MDR", "CIR"], a: 3, why: "The current instruction register (CIR)." },
  { q: "Which bus carries addresses from the CPU to memory?", opts: ["Data bus", "Address bus", "Control bus", "Power bus"], a: 1, why: "The address bus carries addresses." },
  { q: "What is stored in the ACC?", opts: ["The next address", "The instruction", "The result of a calculation", "A memory address"], a: 2, why: "The accumulator holds results from the ALU." },
  { q: "Which of these is an embedded system?", opts: ["A laptop", "A washing machine controller", "A desktop PC", "A games console that installs apps"], a: 1, why: "A washing machine controller has one dedicated function." },
  { q: "What does a larger cache do?", opts: ["Raises the clock speed", "Stores more frequently used data near the CPU", "Adds another core", "Makes ROM writable"], a: 1, why: "Fewer slower trips to RAM are needed." },
  { q: "Which unit decodes an instruction?", opts: ["ALU", "Control unit", "ACC", "RAM"], a: 1, why: "The control unit decodes; the ALU calculates." }
] });

Lib.cards($("#fc1"), { cards: [
  ["CPU", "The central processing unit: processes instructions and data that are input so the result can be output."],
  ["Microprocessor", "An integrated circuit on a single chip; a CPU on one chip."],
  ["ALU", "Arithmetic logic unit: carries out arithmetic and logic operations."],
  ["Control unit", "Decodes instructions and sends control signals to coordinate the CPU."],
  ["PC", "Program counter: holds the address of the next instruction to be fetched."],
  ["MAR", "Memory address register: holds the address being read from or written to."],
  ["MDR", "Memory data register: holds data or an instruction fetched from, or to be written to, memory."],
  ["CIR", "Current instruction register: holds the instruction being decoded and executed."],
  ["ACC", "Accumulator: holds the results of ALU calculations."],
  ["Bus", "A set of wires that carries data, addresses or signals (address, data and control buses)."],
  ["Von Neumann architecture", "Instructions and data are stored together in the same memory."],
  ["Core", "A processing unit in a CPU that can run its own fetch–decode–execute cycle."],
  ["Cache", "Small, very fast memory close to the CPU that holds frequently used instructions and data."],
  ["Clock speed", "The number of cycles the CPU runs each second, in hertz."],
  ["Instruction set", "The list of all the machine code commands a CPU can process."],
  ["Embedded system", "A computer system in a device with one dedicated function."]
] });
