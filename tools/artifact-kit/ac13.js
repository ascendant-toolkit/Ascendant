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

const COL = { W: "#f4f4f0", R: "#c0392b", B: "#2f5fa8", G: "#2e8b57", Y: "#e3b505" };
const rle = (s) => { const r = []; for (const ch of s) { if (r.length && r[r.length - 1][0] === ch) r[r.length - 1][1]++; else r.push([ch, 1]); } return r; };

(function () {
  const row = "WWWWRRRBBWWWWWWW", runs = rle(row), C = 42, X0 = 44;
  let starts = [], p = 0; runs.forEach((r) => { starts.push(p); p += r[1]; });
  const draw = (s) => {
    let o = "";
    row.split("").forEach((ch, i) => { o += SV.rect(X0 + i * C, 30, C - 3, 44, "f3", { rx: 5, style: `fill:${COL[ch]};opacity:1;stroke:var(--line)` }); });
    runs.forEach((r, j) => {
      const v = clamp01(s.k - j); if (v <= 0) return;
      const x1 = X0 + starts[j] * C, w = r[1] * C - 3;
      o += SV.line(x1, 88, x1 + w, 88, "c3", { "stroke-width": 3, ...op(v) }) + SV.text(x1 + w / 2, 118, r[1] + r[0], "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:20px", ...op(v) });
    });
    const f = clamp01(s.f);
    if (f > 0) o += SV.text(380, 176, runs.map((r) => r[1] + r[0]).join("  "), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:24px", ...op(f) }) + SV.text(380, 204, "16 pixels become 4 runs: 8 values", "sm", { "text-anchor": "middle", ...op(f) });
    return o;
  };
  const nm = { W: "white", R: "red", B: "blue" };
  const steps = [{ cap: "A row of 16 pixels. W is white, R is red, B is blue. RLE looks for <b>runs</b>: pixels of the same colour next to each other.", s: {} }];
  runs.forEach((r, j) => steps.push({ cap: `Run ${j + 1}: <b>${r[1]}</b> ${nm[r[0]]} pixel${r[1] > 1 ? "s" : ""} in a row, so store the count and the colour: <b>${r[1]}${r[0]}</b>.`, s: { k: j + 1 } }));
  steps.push({ cap: "The compressed row is <b>4W 3R 2B 7W</b>. Nothing was lost: decoding repeats each colour its count, so the original row is rebuilt exactly. That is <b>lossless</b>.", s: { k: 4, f: 1 } });
  Lib.stepper($("#stA"), { w: 760, h: 224, label: "Run-length encoding a row of pixels", base: { k: 0, f: 0 }, draw, tween: 600, dwell: 3800, steps });
})();

(function () {
  const A = "WWWWWWBBBBBB", Bq = "RGBRGBRGBRGB", ra = rle(A), rb = rle(Bq), C = 28;
  const strip = (s, y, v) => s.split("").map((ch, i) => SV.rect(40 + i * C, y, C - 2, 30, "f3", { rx: 4, style: `fill:${COL[ch] || COL.G};opacity:${v};stroke:var(--line)` })).join("");
  const draw = (s) => {
    const a = clamp01(s.a), b = clamp01(s.b);
    let o = SV.text(40, 24, "Picture 1: two big blocks", "lbl bd t1", op(a || 1)) + strip(A, 34, 1);
    if (a > 0) o += SV.text(40, 96, "RLE: " + ra.map((r) => r[1] + r[0]).join(" "), "lbl bd", { style: "font-family:var(--mono)", ...op(a) }) + SV.rect(420, 40, (12 / 24) * 300 * a, 20, "f3", { rx: 4, ...op(0.6) }) + SV.text(420, 78, "12 values before", "sm", op(a)) + SV.rect(420, 90, (4 / 24) * 300 * a, 20, "f2", { rx: 4, ...op(0.7) }) + SV.text(420, 126, "4 values after: smaller", "sm", op(a));
    if (b > 0) {
      o += SV.text(40, 150, "Picture 2: every pixel different from its neighbour", "lbl bd t3", op(b)) + strip(Bq, 160, b).replace(/fill:#2e8b57/g, "fill:#2e8b57");
      o += SV.text(40, 222, "RLE: " + rb.slice(0, 6).map((r) => r[1] + r[0]).join(" ") + " ...", "lbl bd", { style: "font-family:var(--mono)", ...op(b) }) + SV.rect(420, 160, (12 / 24) * 300 * b, 20, "f3", { rx: 4, ...op(0.6) }) + SV.text(420, 198, "12 values before", "sm", op(b)) + SV.rect(420, 206, (24 / 24) * 300 * b, 20, "f1", { rx: 4, ...op(0.7) }) + SV.text(420, 244, "24 values after: bigger", "sm", op(b));
    }
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 256, label: "RLE on long runs and on no runs", base: { a: 0, b: 0 }, draw, tween: 700, dwell: 4400, steps: [
    { cap: "Two pictures of 12 pixels. The first has two long runs.", s: {} },
    { cap: "RLE stores <b>6W 6B</b>: 4 values instead of 12. A big saving.", s: { a: 1 } },
    { cap: "The second picture changes colour at every pixel, so every run has length 1.", s: { a: 1, b: 1 } },
    { cap: "RLE has to store a count of 1 beside every colour: <b>24</b> values instead of 12. The file is <b>bigger</b>. This is why RLE may not reduce the size of a photograph.", s: { a: 1, b: 1 } }] });
})();

(function () {
  const orig = [52, 53, 55, 54, 52, 53, 55, 54], lossy = orig.map((v) => Math.round(v / 4) * 4);
  const box = (x, y, w, t, c, v, fs = 18) => SV.rect(x, y, w, 40, c, { rx: 8, ...op(0.5 * v) }) + SV.text(x + w / 2, y + 26, t, "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:${fs}px`, ...op(v) });
  const draw = (s) => {
    const a = clamp01(s.a), b = clamp01(s.b), c = clamp01(s.c), d = clamp01(s.d);
    let o = SV.text(30, 28, "Original sample values", "lbl bd") + box(30, 36, 330, orig.join("  "), "f1", 1);
    if (a > 0) o += SV.text(30, 112, "Lossless: store each run (here the pattern repeats)", "sm", op(a)) + box(30, 120, 330, "2 × (52 53 55 54)", "f2", a, 16);
    if (b > 0) o += SV.text(400, 28, "Decompress", "lbl bd t2", op(b)) + box(400, 36, 330, orig.join("  "), "f2", b) + SV.text(400, 94, "Identical to the original: nothing lost", "sm", op(b));
    if (c > 0) o += SV.text(30, 192, "Lossy: round to the nearest 4, a smaller range to store", "sm", op(c)) + box(30, 200, 330, lossy.join("  "), "f3", c);
    if (d > 0) o += SV.text(400, 192, "Decompress", "lbl bd t3", op(d)) + box(400, 200, 330, lossy.join("  "), "f3", d) + SV.text(400, 258, "Different from the original: the detail is gone for good", "sm", op(d));
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 276, label: "Lossless and lossy compression compared", base: { a: 0, b: 0, c: 0, d: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "Eight sound samples, as an example of data to compress.", s: {} },
    { cap: "<b>Lossless</b>: the repeated pattern is stored once with a count. No value is removed.", s: { a: 1 } },
    { cap: "Decompressing gives back <b>exactly</b> the original values. This is why lossless is used for text and programs.", s: { a: 1, b: 1 } },
    { cap: "<b>Lossy</b>: the values are rounded to the nearest multiple of 4. There are fewer different values, so the file can be much smaller.", s: { a: 1, b: 1, c: 1 } },
    { cap: "Decompressing gives only an approximation: 53 and 55 became 52 and 56 and cannot be recovered. The data was <b>permanently removed</b>.", s: { a: 1, b: 1, c: 1, d: 1 } }] });
})();

/* Lab 1 */
(function () {
  const inp = $("#rx");
  const paint = () => {
    const s = inp.value.toUpperCase().slice(0, 30), r = rle(s), enc = r.map((x) => x[1] + x[0]).join(""), items = r.length * 2;
    $("#rxT").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Run</th>${r.map((x, i) => `<td>${i + 1}</td>`).join("")}</tr><tr><th>Value</th>${r.map((x) => `<td>${esc(x[0])}</td>`).join("")}</tr><tr><th>Count</th>${r.map((x) => `<td>${x[1]}</td>`).join("")}</tr></table></div>`;
    $("#r1").textContent = s.length + " characters"; $("#r2").textContent = enc || "-"; $("#r3").textContent = items + " (" + r.length + " runs × 2)";
    $("#rv").textContent = !s.length ? "Type something." : items < s.length ? `${items} stored items instead of ${s.length}: RLE has saved space (lossless, so decoding gives back exactly ${s}).` : items === s.length ? "No change: the runs are short." : `${items} stored items for ${s.length} characters: the encoded version is bigger. RLE needs long runs.`;
  };
  inp.addEventListener("input", paint); paint();
})();

/* Lab 2 */
(function () {
  const W = 16, H = 8, mk = (f) => Array.from({ length: H }, (_, r) => Array.from({ length: W }, (_, c) => f(r, c)).join(""));
  const seed = (r, c) => { const x = Math.sin(r * 12.9898 + c * 78.233) * 43758.5453; return x - Math.floor(x); };
  const pics = [
    ["Flat logo", mk((r, c) => (r >= 2 && r <= 5 && c >= 4 && c <= 11 ? (r >= 3 && r <= 4 && c >= 6 && c <= 9 ? "Y" : "R") : "W"))],
    ["Stripes", mk((r, c) => "WRBG"[Math.floor(c / 4)])],
    ["Gradient", mk((r, c) => "WRBGY"[Math.floor((c + r) / 4) % 5])],
    ["Photo-like noise", mk((r, c) => "WRBGY"[Math.floor(seed(r, c) * 5)])]
  ];
  const show = (i) => {
    $$("#gB button").forEach((b, k) => b.classList.toggle("pri", k === i));
    const rows = pics[i][1], runs = rows.reduce((a, row) => a + rle(row).length, 0), items = runs * 2, px = W * H, ch = ((items - px) / px) * 100;
    let o = ""; rows.forEach((row, r) => row.split("").forEach((c, k) => { o += SV.rect(k * 22, r * 22, 21, 21, "f3", { style: `fill:${COL[c]};opacity:1;stroke:var(--line)` }); }));
    $("#gS").innerHTML = o;
    $("#g1").textContent = px; $("#g2").textContent = runs; $("#g3").textContent = items; $("#g4").textContent = (ch > 0 ? "+" : "") + Lib.fmtN(ch, 0) + "%";
    $("#gv").textContent = ch < -30 ? "Long runs: RLE saves a lot." : ch < 0 ? "Some saving, but the runs are short." : "Almost no runs: RLE makes the file bigger, as it stores a count for nearly every pixel.";
  };
  $("#gB").innerHTML = pics.map((p, i) => `<button class="b" data-i="${i}">${p[0]}</button>`).join("");
  $$("#gB button").forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
})();

/* Lab 3 */
(function () {
  let mb = 40, pct = 30, mbps = 8;
  const speeds = [2, 8, 50];
  const fmtT = (s) => (s < 90 ? Lib.fmtN(s, 1) + " s" : Lib.fmtN(s / 60, 1) + " min");
  const paint = () => {
    $$("#dB button").forEach((b, i) => b.classList.toggle("pri", speeds[i] === mbps));
    const c = (mb * pct) / 100, t0 = (mb * 8) / mbps, t1 = (c * 8) / mbps;
    $("#d1").textContent = Lib.fmtN(c, 1) + " MB"; $("#d2").textContent = fmtT(t0); $("#d3").textContent = fmtT(t1); $("#d4").textContent = Lib.fmtN(mb - c, 1) + " MB";
    $("#dv").textContent = `${mb} MB at ${mbps} Mbit/s takes ${fmtT(t0)}. Compressed to ${pct}% (${Lib.fmtN(c, 1)} MB) it takes ${fmtT(t1)}, so it is transmitted in less time and uses less bandwidth and storage.`;
  };
  Lib.slider($("#dz"), { id: "dzs", label: "Original file size (MB) ", min: 1, max: 200, value: mb, fmt: (x) => x, onInput: (v) => { mb = v; paint(); } });
  Lib.slider($("#dc"), { id: "dcs", label: "Compressed size (% of original) ", min: 5, max: 100, value: pct, fmt: (x) => x + "%", onInput: (v) => { pct = v; paint(); } });
  $("#dB").innerHTML = speeds.map((x) => `<button class="b">${x} Mbit/s</button>`).join("");
  $$("#dB button").forEach((b, i) => (b.onclick = () => { mbps = speeds[i]; paint(); }));
})();

btnTable("lB", "lO", [
  ["Company report to be edited later", "Lossless", "Every character is needed and the file will be edited, so no data can be lost.", "Choosing lossy because the file is smaller"],
  ["Holiday photographs downloaded from a website", "Lossy", "Much smaller files, so a shorter download and less bandwidth; the loss of detail will not be noticed on a screen.", "Giving a benefit for storage when the question is about customers downloading"],
  ["A live video call", "Lossy", "Smaller file, so less bandwidth and less buffering; people stay in step in the conversation.", "Saying lossless because it keeps the quality"],
  ["A source code file", "Lossless", "One lost character stops the program working, so the exact file must be rebuilt.", "Not saying what the lost data would cause"],
  ["Music downloaded to a phone with little storage", "Lossy", "A much smaller file lets more songs be stored; most listeners will not notice the removed detail.", "Not linking to the storage limit"],
  ["A scan of a legal document", "Lossless", "Every detail must be exact and readable; nothing can be permanently removed.", "Saying lossless 'keeps quality' without saying why it matters here"]
], ["Situation", "Better choice", "Reasons that earn marks", "Trap"]);
Lib.classify($("#cl1"), { prompt: "Is each method lossless or lossy?", buckets: [{"label": "Lossless"}, {"label": "Lossy"}], items: [{"text": "Run-length encoding", "b": 0}, {"text": "Reduce the colour depth of an image", "b": 1}, {"text": "Reduce the sampling rate of a sound", "b": 1}, {"text": "Store the change between samples instead of each sample", "b": 0}, {"text": "Reduce the image resolution", "b": 1}, {"text": "Remove sounds humans cannot hear", "b": 1}, {"text": "Replace repeated characters with a character and a count", "b": 0}, {"text": "Reduce the number of colours in the palette", "b": 1}], done: "Lossless methods keep every value. Lossy methods reduce the detail that is stored." });
Lib.classify($("#cl2"), { prompt: "Which type of compression suits each file?", buckets: [{"label": "Lossless"}, {"label": "Lossy"}], items: [{"text": "A text report", "b": 0}, {"text": "A streamed live concert", "b": 1}, {"text": "A program file", "b": 0}, {"text": "A photograph on a news website", "b": 1}, {"text": "A spreadsheet of accounts", "b": 0}, {"text": "Music on a phone with little storage", "b": 1}], done: "Lossless where every bit matters; lossy where the loss will not be noticed." });
Lib.order($("#o1"), { prompt: "Put the steps for run-length encoding AAAABBC in order.", items: ["Start at the first character", "Count how many identical characters follow in a row", "Write the count then one copy of the character", "Move to the next different character and repeat", "Finish with the code 4A2B1C"], done: "Count each run, write count and character, repeat." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Lossy", "Data is permanently removed to make the file smaller"], ["Lossless", "No data is lost; the original can be rebuilt exactly"], ["Run-length encoding", "A run of identical values becomes one copy and a count"], ["Run", "Identical values next to each other"], ["Compression", "Reducing the size of a file"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Run-length encode AAAAABBBCCCC. Type the code with no spaces.", "t": ["5A3B4C"], "unit": "", "hint": "Count each run.", "sol": "<b>5A3B4C</b>."},
  {"q": "Decode 3X2Y4Z. How many characters are in the original?", "a": 9, "unit": "", "tol": 0.01, "hint": "3 + 2 + 4.", "sol": "<b>9</b>: XXXYYZZZZ."},
  {"q": "A row of 40 white pixels is stored as 40W. How many values were stored instead of the 40?", "a": 2, "unit": "", "tol": 0.01, "hint": "One count and one colour.", "sol": "<b>2</b>."},
  {"q": "A file is 24 MB and is compressed to 6 MB. What fraction of the original is it (as a decimal)?", "a": 0.25, "unit": "", "tol": 0.01, "hint": "6 ÷ 24.", "sol": "<b>0.25</b>."},
  {"q": "A 50 MB file is compressed by 80%. What is the compressed size in MB?", "a": 10, "unit": "MB", "tol": 0.01, "hint": "20% remains: 50 × 0.2.", "sol": "<b>10</b> MB."},
  {"q": "A 40 MB file is downloaded at 8 Mbit/s. How many seconds does it take?", "a": 40, "unit": "s", "tol": 0.01, "hint": "40 × 8 = 320 megabits ÷ 8.", "sol": "<b>40</b> seconds."},
  {"q": "The same file is compressed to 10 MB. How many seconds does it take at 8 Mbit/s?", "a": 10, "unit": "s", "tol": 0.01, "hint": "10 × 8 ÷ 8.", "sol": "<b>10</b> seconds."},
  {"q": "RGB (three different pixels) is run-length encoded as a count and a colour for each. How many values are stored?", "a": 6, "unit": "", "tol": 0.01, "hint": "Three runs × 2.", "sol": "<b>6</b>, which is more than the 3 original values."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is lossless compression?", opts: ["Data is permanently removed", "No data is lost and the original can be rebuilt exactly", "The file always stays the same size", "Only sound can be compressed this way"], a: 1, why: "Lossless means the original can be rebuilt exactly." },
  { q: "Why is lossy compression not suitable for a text file?", opts: ["It makes the file bigger", "Removed data cannot be recovered, so the text would be corrupted", "It only works on images", "It is slower than lossless"], a: 1, why: "Every character is needed, and lossy removes data permanently." },
  { q: "What does run-length encoding store?", opts: ["The number of colours in the file", "One copy of a repeated value and the number of times it repeats", "The difference between two files", "The first pixel only"], a: 1, why: "RLE replaces a run with a value and a count." },
  { q: "Why might RLE not reduce the size of a photograph?", opts: ["Photographs have few runs of identical pixels, so counts add data", "Photographs are vector graphics", "RLE is lossy", "RLE needs a longer header"], a: 0, why: "With short runs, each pixel is stored with a count." },
  { q: "Which is a benefit of compressing a file for transmission?", opts: ["It uses more bandwidth", "It is transmitted in less time", "It becomes a vector graphic", "It needs a higher sampling rate"], a: 1, why: "A smaller file is transmitted in less time." },
  { q: "Which method is lossy?", opts: ["Run-length encoding", "Reducing the colour depth of an image", "Storing the change between sound samples", "Replacing repeated characters with a count"], a: 1, why: "Reducing the colour depth discards colour detail." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Compression", "Reducing the size of a file."],
  ["Lossless", "No data lost. Original rebuilt exactly. Text, code."],
  ["Lossy", "Data permanently removed. Much smaller. Photos, video, music."],
  ["Run-length encoding", "Replace a run with one copy and a count."],
  ["RLE weakness", "Few runs: counts add data, file can grow."],
  ["Lossy image methods", "Reduce colour depth, colours or resolution."],
  ["Lossy sound methods", "Reduce sampling rate or resolution."],
  ["Benefit of compression", "Less storage, less transmission time, less bandwidth."],
] });
