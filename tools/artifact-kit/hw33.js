const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const rg = (x, y, w, h, name, val, hi, col = ACC) => SV.rect(x, y, w, h, "", { rx: 8, style: `fill:${hi ? "var(--soft)" : "var(--surface)"};stroke:${hi ? col : MUT};stroke-width:${hi ? 4 : 2}` }) + sm(x + w / 2, y + 17, name) + SV.text(x + w / 2, y + h - 12, val, "lbl bd", { "text-anchor": "middle", style: `fill:${hi ? col : "var(--ink)"}` });
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:4;${dash ? "stroke-dasharray:7 6" : ""}` }) + SV.arrowHead(x2, y2, x2 >= x1 ? "r" : "l", "").replace('class=""', `style="fill:${col}"`);
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });

/* ---------- 3. virtual memory ---------- */
const VM = [
  { r: ["A", "B", "C", "D"], v: [], h: -1, m: 0 }, { r: ["A", "B", "C", "D"], v: [], h: 1, m: 0 }, { r: ["A", "", "C", "D"], v: ["B"], h: -1, m: 1 },
  { r: ["A", "E", "C", "D"], v: ["B"], h: 1, m: 2 }, { r: ["A", "E", "C", "D"], v: ["B"], h: 2, m: 3 }, { r: ["A", "E", "B", "D"], v: ["C"], h: 2, m: 4 },
];
function vmChart(s) {
  const k = Math.round(s.k), d = VM[k];
  let o = panel(130, 20, 500, 120, "RAM (fast, expensive)", ACC) + panel(130, 190, 500, 90, "Virtual memory: part of the drive (slow)", BAD);
  for (let i = 0; i < 4; i++) {
    const p = d.r[i], hi = d.h === i;
    o += SV.rect(150 + i * 120, 50, 100, 70, "", { rx: 10, style: `fill:${p ? "var(--soft)" : "var(--surface)"};stroke:${hi ? "var(--warn)" : p ? ACC : MUT};stroke-width:${hi ? 5 : 2};${p ? "" : "stroke-dasharray:5 5"}` });
    if (p) o += SV.text(200 + i * 120, 95, "Page " + p, "lbl bd", { "text-anchor": "middle" });
    const q = d.v[i];
    o += SV.rect(150 + i * 120, 215, 100, 50, "", { rx: 10, style: `fill:${q ? "var(--soft)" : "var(--surface)"};stroke:${q ? BAD : MUT};stroke-width:2;${q ? "" : "stroke-dasharray:5 5"}` });
    if (q) o += SV.text(200 + i * 120, 246, "Page " + q, "lbl bd", { "text-anchor": "middle" });
  }
  const msg = ["RAM is full and a new page, E, is needed", "Page B was not used recently, so it is moved out", "Page B is now on the drive and a RAM slot is free", "Page E is loaded into RAM; the program can run", "Page B is needed again, but RAM is full", "Swap: C goes out, B comes back. The drive is slower than RAM"][k];
  o += note(380, 170, msg, k === 5 || k === 0 ? "t2" : "t1");
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Virtual memory swapping pages between RAM and the drive", base: { k: 0 }, tween: 1, dwell: 4200, draw: vmChart, steps: [
  { cap: "RAM is <b>full</b> with pages A to D. The user opens a program that needs another page, E.", s: { k: 0 } },
  { cap: "The operating system picks a page that is not needed right now, <b>page B</b>, to move out of RAM.", s: { k: 1 } },
  { cap: "Page B is copied to <b>virtual memory</b>, space set aside on the hard drive or SSD.", s: { k: 2 } },
  { cap: "Page E is loaded into the free RAM slot. More programs now run than RAM alone could hold.", s: { k: 3 } },
  { cap: "Later, page B is needed again, but RAM is full.", s: { k: 4 } },
  { cap: "Pages are <b>swapped</b>: C goes out, B comes back. This works, but the drive is <b>much slower</b> than RAM, so too much swapping makes the computer slow.", s: { k: 5 } },
] });

/* ---------- Lab 3: virtual memory ---------- */
(() => {
  const RAMS = [2, 4, 8, 16]; let sr, sp;
  function upd() {
    if (!sr || !sp) return;
    const ram = RAMS[sr.get()], n = sp.get(), need = 2 + n * 1.5, inRam = Math.min(ram, need), vm = Math.max(0, need - ram);
    $("#va").textContent = fmtN(need, 1) + " GB"; $("#vb").textContent = fmtN(inRam, 1) + " GB"; $("#vc").textContent = fmtN(vm, 1) + " GB";
    const total = Math.min(30, Math.ceil(need)); let h = "";
    for (let i = 0; i < total; i++) h += `<i class="${i < ram ? "u" : "v"}"></i>`;
    $("#vm").innerHTML = h;
    $("#vv").innerHTML = vm === 0 ? `Everything fits in ${ram} GB of RAM, so the computer runs at full speed. The operating system takes 2 GB, and each program about 1.5 GB.` : vm < ram / 2 ? `${fmtN(vm, 1)} GB has to go into <b>virtual memory</b> (red). Pages swap between RAM and the drive, so it may feel slightly slower.` : `<b>${fmtN(vm, 1)} GB</b> is in virtual memory. With so much swapping between RAM and the much slower drive, the computer is likely to feel very slow. Close programs or add RAM.`;
  }
  sr = Lib.slider($("#v1"), { id: "vr", label: "RAM", min: 0, max: 3, value: 1, fmt: (i) => RAMS[i] + " GB", onInput: upd });
  sp = Lib.slider($("#v2"), { id: "vp", label: "Open programs", min: 1, max: 12, value: 3, onInput: upd });
  upd();
})();


/* ---------- Lab 2: choose the storage ---------- */
(() => {
  const OPT = ["Magnetic (HDD)", "Optical (CD, DVD, Blu-ray)", "Solid-state (SSD, flash)", "RAM", "ROM", "Cloud storage"];
  const ALL = [
    ["Holds the programs a laptop is running right now", "RAM"], ["Holds the start-up instructions of a computer", "ROM"], ["Cheap, very large capacity for a desktop, where speed matters less", "Magnetic (HDD)"],
    ["A fast, light drive in a laptop with no moving parts", "Solid-state (SSD, flash)"], ["Posting a film on a disc that a laser reads", "Optical (CD, DVD, Blu-ray)"], ["Photos you can open on any device while travelling", "Cloud storage"],
  ];
  const el = $("#sn3"), v = $("#sv3");
  el.innerHTML = ALL.map((s) => `<div class="r" data-a="${s[1]}"><span class="q">${s[0]}</span><select class="sel" aria-label="Storage for: ${s[0]}"><option value="">Choose…</option>${OPT.map((x) => `<option>${x}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose the best type of storage for each job.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct.`; }));
})();

/* ---------- Practise ---------- */
/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Drag each statement to RAM or ROM.", buckets: [{ label: "RAM" }, { label: "ROM" }], items: [
  { text: "Volatile: contents lost when power is off", b: 0 }, { text: "Holds programs that are currently running", b: 0 }, { text: "Can be read and written", b: 0 }, { text: "Holds the current data being worked on", b: 0 },
  { text: "Non-volatile: contents kept when power is off", b: 1 }, { text: "Stores the start-up (bootstrap) instructions", b: 1 }, { text: "Read only", b: 1 }, { text: "Holds firmware that rarely changes", b: 1 },
], done: "RAM is the working space; ROM is the fixed start-up code." });

Lib.classify($("#cl3"), { prompt: "Drag each statement or device to the type of secondary storage.", buckets: [{ label: "Magnetic" }, { label: "Optical" }, { label: "Solid-state" }], items: [
  { text: "Hard disk drive (HDD)", b: 0 }, { text: "Platters with tracks and sectors", b: 0 }, { text: "Electromagnets read and write the data", b: 0 },
  { text: "DVD", b: 1 }, { text: "Blu-ray", b: 1 }, { text: "A laser reads pits and lands", b: 1 },
  { text: "SSD", b: 2 }, { text: "USB flash drive", b: 2 }, { text: "SD card", b: 2 }, { text: "Floating gates trap charge", b: 2 }, { text: "No moving parts", b: 2 },
], done: "Magnets, lasers, or transistors." });

Lib.classify($("#cl4"), { prompt: "Is each point an advantage or a disadvantage of storing data in the cloud, compared with storing it locally?", buckets: [{ label: "Advantage of cloud" }, { label: "Disadvantage of cloud" }], items: [
  { text: "Accessible from any device with internet", b: 0 }, { text: "No hardware to buy or maintain", b: 0 }, { text: "Provider keeps backup copies", b: 0 }, { text: "Easy to share files with others", b: 0 }, { text: "Storage can be increased when needed", b: 0 },
  { text: "Needs an internet connection", b: 1 }, { text: "Ongoing subscription fee", b: 1 }, { text: "Relies on the provider's security", b: 1 }, { text: "Large files are slower to open", b: 1 },
], done: "Convenience and backup against dependence and cost." });

Lib.calc($("#c1"), { qs: [
  { q: "A computer has 8 GB of RAM and its programs need 11 GB. How many GB are in virtual memory?", a: 3, sol: "11 − 8 = 3 GB." },
  { q: "A 1 TB SSD holds 250 GB of video. How many GB are free? (1 TB = 1000 GB)", a: 750, sol: "1000 − 250 = 750 GB." },
  { q: "A DVD holds 4.7 GB. How many DVDs are needed to store 14.1 GB?", a: 3, sol: "14.1 ÷ 4.7 = 3 DVDs." },
  { q: "A cloud plan costs 3 per month. How much does it cost for a year (12 months)?", a: 36, sol: "3 × 12 = 36." },
  { q: "A phone has 6 GB of RAM and 128 GB of flash storage. How many times bigger is the storage than the RAM? (round to the nearest whole number)", a: 21, tol: 0.5, sol: "128 ÷ 6 = 21.3, so about 21 times." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Why does a computer need ROM?", opts: ["To store running programs", "To hold the start-up instructions", "To make virtual memory", "To store photos"], a: 1, why: "ROM is non-volatile, so the bootstrap is there when the computer is switched on." },
  { q: "How does an optical disc store data?", opts: ["Electromagnets set north or south", "Pits and lands read by a laser", "Floating gates trap charge", "Transistors in RAM"], a: 1, why: "Optical storage uses a laser and pits and lands." },
  { q: "What is virtual memory?", opts: ["A second CPU", "Part of secondary storage used as an extension of RAM", "A type of cache", "Memory in the cloud"], a: 1, why: "When RAM is full, pages are swapped to space on the drive." },
  { q: "Which storage has no moving parts?", opts: ["HDD", "DVD", "SSD", "Blu-ray"], a: 2, why: "Solid-state storage is flash memory with no moving parts." },
  { q: "Which is volatile?", opts: ["ROM", "RAM", "SSD", "HDD"], a: 1, why: "RAM loses its contents when the power is off." },
  { q: "Which is a disadvantage of cloud storage?", opts: ["Accessible anywhere", "Needs an internet connection", "Provider keeps backups", "Easy sharing"], a: 1, why: "Without internet, you cannot reach the data." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Primary storage", "Storage directly accessed by the CPU: RAM and ROM."],
  ["RAM", "Volatile primary storage for programs and data currently in use."],
  ["ROM", "Non-volatile, read only primary storage that holds start-up instructions."],
  ["Volatile", "Contents are lost when the power is turned off."],
  ["Secondary storage", "Non-volatile storage not directly accessed by the CPU, for permanent data."],
  ["Magnetic storage", "Platters with tracks and sectors; electromagnets read and write the data, for example an HDD."],
  ["Optical storage", "A laser reads pits and lands, for example CD, DVD, Blu-ray."],
  ["Solid-state storage", "Flash memory (NAND or NOR) using transistors with control gates and floating gates; no moving parts."],
  ["Virtual memory", "Part of secondary storage used as an extension of RAM, swapping pages in and out."],
  ["Page", "A block of data moved between RAM and virtual memory."],
  ["Cloud storage", "Data stored on remote servers and accessed over the internet."]
] });
