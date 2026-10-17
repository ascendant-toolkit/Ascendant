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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

function pick(id, items, render) {
  const B = $("#" + id + "B"), O = $("#" + id + "O");
  B.innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t.label}</button>`).join("");
  const show = (i) => { $$("button", B).forEach((b, k) => b.classList.toggle("pri", k === i)); O.innerHTML = render(items[i]); };
  $$("button", B).forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
const scoreBar = (m, max) => `<div style="background:var(--soft);border-radius:7px;height:14px;margin:6px 0 2px"><div class="bar ${m === max ? "b3" : m === 0 ? "b2" : "b4"}" style="width:${Math.max(2, (m / max) * 100)}%"></div></div><small>${m} of ${max} marks</small>`;

$("#pic1").innerHTML = (() => {
  const B = [["Work in order", "about 85 min", "Answer every question; short ones first", 20, "f2", 400], ["Return and check", "15 to 20 min", "Skipped questions, number work, diagrams", 440, "f1", 180], ["Buffer", "to 105", "Extra pages labelled", 640, "f3", 100]];
  let o = ""; B.forEach(([n, t, d, x, c, w]) => { o += SV.rect(x, 12, w, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }) + SV.text(x + w / 2, 62, t, "sm", { "text-anchor": "middle" }) + SV.text(x + w / 2, 84, d.length > 34 ? d.slice(0, 34) + "…" : d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Suggested plan for the 105 minutes of Paper 1">${o}</svg>`;
})();
chainStep("#stA", "The decode stage", ["The instruction is held in the MDR after the fetch stage", "It is sent along the data bus to the CIR, which is part of the control unit", "The instruction is split into the opcode and the operand", "The control unit decodes it using the instruction set"], [
  "<b>Start:</b> fetch has finished; the instruction is in the MDR.", "<b>Transfer:</b> MDR to CIR along the data bus.", "<b>Split:</b> the opcode says what to do; the operand says what to do it to.", "<b>Decode:</b> the control unit uses the instruction set. Then execute begins."]);
chainStep("#stB", "Adding 01010100 and 01110100", ["Write the numbers one above the other and add a row for the carries", "Right to left: 0+0=0, 0+0=0, then 1+1=0 carry 1", "0+0+1=1, then 1+1=0 carry 1, then 0+1+1=0 carry 1", "1+1+1=1 carry 1, then 0+0+1=1: the answer is 11001000 (200)"], [
  "<b>Layout:</b> the carries row is where the working mark is earned.", "<b>First columns:</b> the first carry appears in the third column.", "<b>Middle columns:</b> carries keep moving left.", "<b>Check:</b> 84 + 116 = 200 and 11001000 is 200. No overflow, because there is no carry out of the last column."]);
chainStep("#stC", "A sound file: 10 s, 22 016 Hz, 8 bits", ["Bits = sample rate × resolution × seconds", "22 016 × 8 × 10 = 1 761 280 bits", "Bytes = bits ÷ 8 = 220 160 bytes", "KiB = bytes ÷ 1024 = 215 KiB"], [
  "<b>Formula:</b> write it first.", "<b>Substitute:</b> the first working mark.", "<b>Bytes:</b> divide by 8.", "<b>Unit asked:</b> divide by 1024 to get 215 KiB. One mark for the answer."]);

const bin = (n) => n.toString(2).padStart(8, "0");
pick("a", [[84, 116], [155, 100], [15, 15], [170, 85], [200, 100]].map(([x, y]) => ({ label: bin(x) + " + " + bin(y), x, y })), (it) => {
  const A = bin(it.x), B = bin(it.y); let c = 0, s = "", cr = "";
  for (let i = 7; i >= 0; i--) { const t = +A[i] + +B[i] + c; s = (t & 1) + s; cr = (c ? "1" : "·") + cr; c = t >> 1; }
  const sp = (t) => t.split("").join("  "), tot = it.x + it.y;
  return `<div class="formula" style="white-space:pre;overflow-x:auto">carries   ${sp(cr)}\n          ${sp(A)}\n        + ${sp(B)}\n        ──────────────────────\n    =   ${sp(s)}${c ? "  (carry out 1)" : ""}</div><p>${it.x} + ${it.y} = ${tot}. ${c ? "<b>Overflow:</b> the result is greater than 255, so it does not fit in 8 bits. The ninth bit is lost, and the error is called overflow." : "No carry out of the left-hand column, so there is no overflow."} The mark scheme gives a mark for the carries and a mark for each correct nibble.</p>`;
});

pick("t", [0b10011100, 0b11110001, 0b10000000, 0b01111111, 0b11111111].map((v) => ({ label: bin(v), v })), (it) => {
  const b = bin(it.v), neg = b[0] === "1", flip = b.split("").map((x) => (x === "1" ? "0" : "1")).join(""), mag = (parseInt(flip, 2) + 1) & 255 || 128;
  return neg
    ? `<div class="formula" style="white-space:pre;overflow-x:auto">pattern   ${b}   left-hand bit = 1: negative\nflip      ${flip}\nadd 1     ${bin((parseInt(flip, 2) + 1) & 255)}   = ${mag}\nanswer    −${mag}</div><p>Trap: read as an ordinary unsigned number, ${b} would be ${it.v}. The mark scheme gives a mark for the flip-and-add working and a mark for the correct negative answer.</p>`
    : `<div class="formula" style="white-space:pre;overflow-x:auto">pattern   ${b}   left-hand bit = 0: positive\nanswer    ${it.v}</div><p>A left-hand bit of 0 means the number is positive and is read as normal binary.</p>`;
});

const KB = (n) => (n % 1 ? n.toFixed(2) : n);
pick("f", [
  { label: "Image 256 × 128, 24-bit", kind: "image", w: 256, h: 128, d: 24 },
  { label: "Image 512 × 512, 16-bit", kind: "image", w: 512, h: 512, d: 16 },
  { label: "Sound 16 s, 8192 Hz, 16-bit", kind: "sound", r: 8192, d: 16, t: 16 },
  { label: "Sound 10 s, 22 016 Hz, 8-bit", kind: "sound", r: 22016, d: 8, t: 10 }
], (it) => {
  const bitsN = it.kind === "image" ? it.w * it.h * it.d : it.r * it.d * it.t, by = bitsN / 8, kib = by / 1024, wrong = by / 1000, f = (n) => n.toLocaleString("en-GB").replace(/,/g, " ");
  const l1 = it.kind === "image" ? `bits = width × height × colour depth = ${it.w} × ${it.h} × ${it.d} = ${f(bitsN)}` : `bits = sample rate × resolution × seconds = ${f(it.r)} × ${it.d} × ${it.t} = ${f(bitsN)}`;
  return `<div class="formula" style="white-space:pre-wrap">${l1}\nbytes = bits ÷ 8 = ${f(by)}\nKiB = bytes ÷ 1024 = ${KB(kib)}</div><p>Common error: dividing by 1000 gives ${KB(wrong)}, which is not ${KB(kib)}. The syllabus says calculations use 1024. Marks: up to two for the stages of working and one for the answer in the unit asked.</p>`;
});

const QS = [
  ["Q1", "Data representation: units and compression", 6, "A tick, two types of compression, three benefits"],
  ["Q2", "Hardware: smart phone devices and storage", 10, "Input, output, purpose of secondary storage, justify a choice"],
  ["Q3", "Data representation: conversions, shift, addition", 11, "Number work with working"],
  ["Q4", "Data transmission: packets and methods", 11, "Describe the packet; explain why a method is chosen"],
  ["Q5", "Hardware: fetch-decode-execute", 11, "Registers, decode stage, buses, clock speed"],
  ["Q6", "Software: embedded system, assembly, IDE", 10, "Six marks for how an IDE helps"],
  ["Q7", "Software: operating system and firmware", 4, "Function and description"],
  ["Q8", "Internet: blockchain", 4, "A labelled diagram"],
  ["Q9", "Emerging technology: AI", 8, "Complete a paragraph; name machine learning"]
].map(([label, topic, m, what]) => ({ label, topic, m, what }));
pick("q", QS, (it) => `<p><b>${it.topic}</b></p>${scoreBar(it.m, 11)}<p>${it.what}. At 1.4 minutes a mark this question deserves about <b>${Lib.fmtN(it.m * 1.4, 1)} minutes</b>. It is ${Lib.fmtN((it.m / 75) * 100, 0)}% of the paper.</p>`);
Lib.classify($("#cl1"), { prompt: "Does the device fit a smart phone or smartwatch?", buckets: [{"label": "Fits"}, {"label": "Does not fit"}], items: [{"text": "Touchscreen", "b": 0}, {"text": "Microphone", "b": 0}, {"text": "Digital camera", "b": 0}, {"text": "Screen", "b": 0}, {"text": "Speaker", "b": 0}, {"text": "Mouse", "b": 1}, {"text": "Printer", "b": 1}, {"text": "Full-size keyboard", "b": 1}, {"text": "Plotter", "b": 1}], done: "A device must be one that could feasibly be built into the product." });
Lib.classify($("#cl2"), { prompt: "Is the statement correct or a misconception?", buckets: [{"label": "Correct"}, {"label": "Misconception"}], items: [{"text": "Encryption makes stolen data meaningless to the thief", "b": 0}, {"text": "Encryption stops data being stolen", "b": 1}, {"text": "The accumulator stores the interim result of a calculation", "b": 0}, {"text": "The accumulator carries out calculations", "b": 1}, {"text": "Lossy and lossless are the two types of compression", "b": 0}, {"text": "JPEG is a type of compression", "b": 1}, {"text": "The browser sends the page request to the web server after the DNS returns the IP address", "b": 0}, {"text": "The DNS sends the page request to the web server", "b": 1}, {"text": "Secondary storage keeps data when the device is switched off", "b": 0}, {"text": "Secondary storage is only used when primary storage is full", "b": 1}], done: "Each wrong idea is one the examiners have recorded." });
Lib.order($("#o1"), { prompt: "Put the retrieval of a web page in order.", items: ["The user enters the URL in the web browser", "The browser sends the URL to the DNS", "The DNS finds the matching IP address", "The IP address is returned to the browser", "The browser sends a request to the web server", "The web server sends the web page back", "The browser renders the HTML"], done: "URL, DNS, IP address, request, page, render." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Program counter", "Stores the address of the next instruction to be fetched"], ["Accumulator", "Stores the interim result of a calculation"], ["Memory data register", "Holds the data or instruction just fetched from memory"], ["Control unit", "Decodes instructions and sends signals to manage the flow of data"], ["Instruction set", "A list of all the commands the processor can carry out"], ["Opcode", "The part of an instruction that says what to do"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Add 01010100 and 01110100. Give the answer in denary.", "a": 200, "unit": "", "tol": 0.01, "hint": "84 + 116.", "sol": "<b>200</b> (11001000)."},
  {"q": "A logical left shift of 2 places is performed on 00001111. Give the answer in denary.", "a": 60, "unit": "", "tol": 0.01, "hint": "00111100.", "sol": "<b>60</b>: 15 multiplied by 4."},
  {"q": "A 16-bit colour image is 512 pixels wide and 512 pixels high. What is its file size in KiB?", "a": 512, "unit": "KiB", "tol": 0.01, "hint": "512 × 512 × 16 ÷ 8 ÷ 1024.", "sol": "<b>512 KiB</b>."},
  {"q": "A sound file is 10 seconds at 22 016 Hz with 8-bit samples. What is its size in KiB?", "a": 215, "unit": "KiB", "tol": 0.5, "hint": "22 016 × 8 × 10 ÷ 8 ÷ 1024.", "sol": "<b>215 KiB</b>."},
  {"q": "The 8-bit two's complement pattern 11110001 is stored. What is its denary value?", "a": -15, "unit": "", "tol": 0.01, "hint": "Flip to 00001110, add 1.", "sol": "<b>−15</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which of these is a mistake candidates make about the accumulator?", opts: ["It stores the interim result of a calculation", "It carries out calculations", "It is a register", "It is in the CPU"], a: 1, why: "The ALU calculates; the accumulator stores the result." },
  { q: "A question asks you to add two binary numbers. What gets the working mark?", opts: ["Converting to denary", "Showing the carries in a binary addition", "Writing only the answer", "Drawing a circuit"], a: 1, why: "The working mark is for binary addition." },
  { q: "Which is the best storage device for a smart phone?", opts: ["Hard disk drive", "Solid state", "Magnetic tape", "Optical disc"], a: 1, why: "Small, light, no moving parts, low power." },
  { q: "In the web page retrieval, what does the DNS return to the browser?", opts: ["The web page", "The IP address", "The URL", "The HTML"], a: 1, why: "The DNS returns the IP address. The browser then sends the request." },
  { q: "What does the syllabus say to use when calculating file sizes?", opts: ["1000", "1024", "1048", "Either"], a: 1, why: "Calculations must use 1024, not 1000." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Paper 1", "75 marks, 105 minutes, no calculator."],
  ["1.4 minutes", "Per mark."],
  ["Binary addition", "Carries row; overflow above 255."],
  ["Two's complement", "Left bit 1: flip, add 1, negative."],
  ["File size", "Bits ÷ 8 ÷ 1024."],
  ["Decode", "MDR → CIR, opcode and operand, instruction set."],
  ["DNS", "URL → IP address → browser → request → page."],
  ["Phone storage", "Solid state: small, light, no moving parts."],
] });
