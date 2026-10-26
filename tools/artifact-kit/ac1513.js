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
  const layers = [["Physical hardware", "f1", "real processor, RAM, storage"], ["Host operating system", "f2", "controls the real resources; runs the VM software"], ["Hypervisor / VM software", "f3", "creates and runs the VMs; shares host resources"], ["Virtual machine: guest operating system", "f4", "runs inside the VM; emulated hardware"], ["Applications", "f1", "programs in the guest"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    layers.forEach((l, i) => { const y = 200 - i * 44, v = k >= i ? 1 : 0; if (!v) return; o += SV.rect(160, y, 440, 38, k === i ? "cell-warn" : l[1], { rx: 6, ...op(k === i ? 1 : 0.7) }) + SV.text(180, y + 24, l[0], "lbl bd", { style: "font-size:14px" }) + SV.text(620, y + 24, l[2], "sm", { style: "font-size:11px" }); });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 245, label: "The layers of a virtual machine", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "At the bottom is the <b>physical hardware</b>: the real processor, RAM and storage.", s: { i: 0 } },
    { cap: "The <b>host operating system</b> controls all the real resources and runs the virtual machine software.", s: { i: 1 } },
    { cap: "The <b>hypervisor</b> (VM software) runs between the host and guest operating systems, creating the VMs and allocating resources to them.", s: { i: 2 } },
    { cap: "Inside the VM runs the <b>guest operating system</b>, using virtual hardware that the VM software emulates.", s: { i: 3 } },
    { cap: "The guest runs its own applications. Several VMs can run at once, each with its own guest.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.rect(30, 20, 700, 190, "f1", { rx: 10, ...op(0.2) }) + SV.text(50, 44, "Host computer", "lbl bd");
    o += SV.rect(60, 60, 300, 130, k >= 1 ? "cell-no" : "f4", { rx: 8, ...op(0.6) }) + SV.text(80, 86, "Virtual machine A", "lbl bd", { style: "font-size:14px" }) + SV.text(80, 112, k >= 1 ? "guest OS crashes ✗" : "guest OS running", "lbl", { style: "font-size:13px" });
    o += SV.rect(400, 60, 300, 130, "f3", { rx: 8, ...op(0.6) }) + SV.text(420, 86, "Virtual machine B", "lbl bd", { style: "font-size:14px" }) + SV.text(420, 112, "still running normally", "lbl", { style: "font-size:13px" });
    if (k >= 2) o += SV.text(60, 238, "The host and VM B are unaffected. VM A can be restarted or deleted.", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 250, label: "Protection", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "Two virtual machines run on one host.", s: { i: 0 } },
    { cap: "The guest operating system in VM A <b>crashes</b> (or a program in it contains a virus).", s: { i: 1 } },
    { cap: "The problem stays <b>inside</b> VM A. The host and the other VM are not affected: this is the protection a VM gives.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Host RAM: 16 GB", "lbl bd");
    o += SV.rect(30, 34, 700, 30, "cell", { rx: 6 });
    const vms = [4, 4, 4, 4]; let x = 30;
    vms.slice(0, Math.min(k + 1, 4)).forEach((g, i) => { o += SV.rect(x, 34, g / 16 * 700, 30, ["f1", "f2", "f3", "f4"][i], { rx: 6 }) + SV.text(x + 10, 54, "VM" + (i + 1) + " 4 GB", "lbl bd", { style: "font-size:12px" }); x += g / 16 * 700; });
    if (k >= 4) o += SV.rect(30 + 700, 34, 140, 30, "cell-no", { rx: 6 }) + SV.text(34 + 700, 54, "VM5 4 GB", "lbl bd", { style: "font-size:12px" });
    o += SV.text(30, 110, k < 4 ? (k + 1) * 4 + " GB requested of 16 GB: fine" : "20 GB requested of 16 GB: the host runs short; every VM slows", "lbl bd" + (k < 4 ? " t3" : " t2"), { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 130, label: "Sharing the host's RAM", base: { i: 0 }, draw, tween: 250, dwell: 2400, steps: [0, 1, 2, 3, 4].map((i) => ({ cap: i < 4 ? (i + 1) + " VM" + (i ? "s" : "") + " running, each allocated 4 GB." : "A fifth VM is started. The host cannot give all of them what they ask for, so <b>performance drops</b>: the resources are shared.", s: { i } })) });
})();

/* Lab 1 */
(function () {
  let n = 3;
  const paint = () => {
    const req = n * 4; $("#v1").textContent = req + " GB"; $("#v2").textContent = "16 GB"; const perf = req <= 12 ? "good" : req <= 16 ? "ok (host nearly full)" : "poor (not enough RAM)"; $("#v3").textContent = perf;
    $("#vT").innerHTML = '<div class="tw"><table class="t mono"><tr>' + Array.from({ length: n }, (_, i) => `<th>VM${i + 1}</th>`).join("") + "</tr><tr>" + Array.from({ length: n }, () => "<td>4 GB</td>").join("") + "</tr></table></div>";
    $("#vV").textContent = req <= 16 ? "The host can give each VM its RAM. The VMs still run a little slower than real machines because of the extra code and indirect hardware access." : "The VMs ask for " + req + " GB but the host only has 16 GB. The host has to swap data in and out, so every VM slows down: shared resources limit performance.";
  };
  Lib.slider($("#vS"), { id: "vss", label: "Number of virtual machines ", min: 1, max: 6, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();

/* Lab 2 */
(function () {
  const q = [["A developer wants to test a program on three different operating systems using one laptop", "Good choice", "Several guest operating systems run on one host, with no extra hardware to buy."], ["A video game needs the very highest graphics performance", "Poor choice", "A VM accesses the hardware indirectly and shares the host's resources, so performance is lower than on a real machine."], ["An analyst opens a suspicious email attachment", "Good choice", "If it contains a virus it only infects the VM, which can be deleted."], ["A school needs software that only runs on an old operating system", "Good choice", "Run the old OS as a guest: legacy applications can run on a modern host."], ["A hardware engineer needs to test a new graphics card that is not yet supported by the VM software", "Poor choice", "Some hardware cannot be emulated or accessed directly by a VM."]];
  let cur = 0, pick = null;
  const paint = () => {
    $$("#qB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const Q = q[cur]; $("#qO").innerHTML = `<p><b>${Q[0]}</b></p><div class="btnrow"><button class="b${pick === "Good choice" ? " pri" : ""}">Good choice</button><button class="b${pick === "Poor choice" ? " pri" : ""}">Poor choice</button></div><div class="verdict">` + (pick === null ? "Choose an answer." : (pick === Q[1] ? "Correct. " : "Not quite. ") + Q[2]) + "</div>";
    $$("#qO .btnrow button").forEach((b) => (b.onclick = () => { pick = b.textContent; paint(); }));
  };
  $("#qB").innerHTML = q.map((x, i) => `<button class="b" data-i="${i}">Situation ${i + 1}</button>`).join("");
  $$("#qB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Host operating system", "The normal OS of the physical computer", "Controls all the real resources; runs the VM software; provides the user interface to it", "Windows or macOS on the laptop"],
  ["Hypervisor", "VM software between host and guests", "Creates and runs VMs; allocates host resources to them", "VirtualBox, VMware"],
  ["Guest operating system", "The OS inside the virtual machine", "Controls the virtual hardware during emulation; runs under the host's control", "Linux running in a VM on Windows"],
  ["Virtual machine", "A software emulation of a computer system", "A standalone environment with all the components of a computer, simulated", "A test machine"]
], ["Term", "What it is", "Role", "Example"]);
Lib.classify($("#cl1"), { prompt: "Benefit or limitation of a virtual machine?", buckets: [{"label": "Benefit"}, {"label": "Limitation"}], items: [{"text": "Software for another system can run in a compatible guest OS", "b": 0}, {"text": "Performance is poorer than a real machine", "b": 1}, {"text": "A crash or virus stays inside the VM", "b": 0}, {"text": "Some hardware cannot be emulated", "b": 1}, {"text": "No extra hardware has to be bought", "b": 0}, {"text": "Setting up and maintaining it is complex", "b": 1}, {"text": "The host's RAM and processor time are shared", "b": 1}, {"text": "Several operating systems can coexist on one computer", "b": 0}], done: "Benefits: compatibility, protection, cost. Limitations: performance, complexity, hardware." });
Lib.classify($("#cl2"), { prompt: "Is it the host or the guest operating system?", buckets: [{"label": "Host OS"}, {"label": "Guest OS"}], items: [{"text": "Controls all the real resources of the computer", "b": 0}, {"text": "Runs inside the virtual machine", "b": 1}, {"text": "Runs the VM software", "b": 0}, {"text": "Controls the virtual hardware during emulation", "b": 1}, {"text": "Accesses the physical resources directly", "b": 0}, {"text": "Accesses real hardware through the VM and the host OS", "b": 1}], done: "The host runs on the real hardware. The guest runs inside the VM." });
Lib.order($("#o1"), { prompt: "Put the layers in order, from the hardware up.", items: ["Physical hardware", "Host operating system", "Hypervisor / virtual machine software", "Guest operating system in the virtual machine", "Applications"], done: "Hardware, host OS, hypervisor, guest OS, applications." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Virtual machine", "A software emulation of a computer system"], ["Host", "The physical computer and its OS that run the VM"], ["Guest operating system", "The OS that runs inside the virtual machine"], ["Hypervisor", "Software that creates and runs virtual machines"], ["Emulate", "Behave like another system using software"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A host has 32 GB of RAM and each VM is allocated 6 GB. What is the largest number of VMs that fit?", "a": 5, "unit": "", "tol": 0.01, "hint": "32 ÷ 6 = 5.33.", "sol": "<b>5</b>."},
  {"q": "Four VMs are each given 8 GB on a host with 24 GB. How many GB more than the host has are requested?", "a": 8, "unit": "GB", "tol": 0.01, "hint": "32 − 24.", "sol": "<b>8</b> GB."},
  {"q": "How many operating systems are running if a Windows host runs two Linux VMs?", "a": 3, "unit": "", "tol": 0.01, "hint": "One host OS and two guests.", "sol": "<b>3</b>."},
  {"q": "One VM crashes out of three running on a host. How many are still running?", "a": 2, "unit": "", "tol": 0.01, "hint": "The others are unaffected.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a virtual machine?", opts: ["A physical computer", "A software emulation of a computer system", "A type of network", "A kind of memory"], a: 1, why: "It emulates a system in software." },
  { q: "Where does the guest operating system run?", opts: ["On the hardware directly", "Inside the virtual machine", "Only in ROM", "On the keyboard"], a: 1, why: "Inside the VM." },
  { q: "Which is a benefit of a VM?", opts: ["Better performance than a real machine", "A crash does not affect the host", "No software is needed", "It needs no RAM"], a: 1, why: "Protection." },
  { q: "Which is a limitation?", opts: ["It saves money", "It uses extra code and shared resources, so is slower", "It runs legacy software", "It is safe for testing"], a: 1, why: "Performance." },
  { q: "What creates and runs the virtual machines?", opts: ["The hypervisor / VM software", "The keyboard", "The guest OS only", "The printer"], a: 0, why: "VM software." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Virtual machine", "Software emulation of a computer system on a host."],
  ["Host OS", "Normal OS of the host; controls real resources; runs the VM software."],
  ["Guest OS", "Runs inside the VM; controls the virtual hardware."],
  ["Hypervisor", "Creates and runs VMs, allocates host resources."],
  ["Benefits", "Compatibility, protection, cost, several OSs at once."],
  ["Limitations", "Performance, complexity, hardware cannot be emulated."],
  ["Legacy", "Old software runs in a compatible guest."],
  ["Shared", "RAM and processor time are shared with the host."],
] });
