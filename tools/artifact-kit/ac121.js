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

const COL = { W: "#f4f4f0", R: "#c0392b", B: "#2f5fa8", G: "#2e8b57", Y: "#e3b505" }, CODE = { W: "00", R: "01", B: "10" };
(function () {
  const G = ["RRWWWW", "BBRRWW", "WWWRRR", "WWWWRR"], C = 44, X0 = 40, Y0 = 36;
  const draw = (s) => {
    let o = "";
    G.forEach((row, r) => row.split("").forEach((ch, c) => {
      const show = clamp01(s.k - 1 - r);
      o += SV.rect(X0 + c * C, Y0 + r * C, C - 2, C - 2, "f3", { rx: 4, style: `fill:${COL[ch]};opacity:1;stroke:var(--line)` });
      if (show > 0) o += SV.text(X0 + c * C + C / 2 - 1, Y0 + r * C + C / 2 + 5, CODE[ch], "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:14px;fill:${ch === "W" ? "#222" : "#fff"}`, ...op(show) });
    }));
    const L = clamp01(s.k);
    if (L > 0) [["W", "white", "00"], ["R", "red", "01"], ["B", "blue", "10"]].forEach((p, i) => { o += SV.rect(360, 44 + i * 36, 26, 26, "f3", { rx: 4, style: `fill:${COL[p[0]]};opacity:${L};stroke:var(--line)` }) + SV.text(396, 63 + i * 36, p[1] + " = " + p[2], "lbl bd", { style: "font-family:var(--mono);font-size:16px", ...op(L) }); });
    G.forEach((row, r) => { const v = clamp01(s.k - 1 - r); if (v > 0) o += SV.text(360, 170 + r * 26, row.split("").map((ch) => CODE[ch]).join(" "), "lbl bd", { style: "font-family:var(--mono);font-size:15px", ...op(v) }); });
    o += SV.text(360, 152, L > 0 ? "stored in sequence:" : "", "sm", op(L));
    return o;
  };
  const steps = [{ cap: "A bitmap is a grid of <b>pixels</b>. This one is 6 pixels wide and 4 pixels high, a <b>resolution</b> of 6 × 4. Each pixel is one colour.", s: { k: 0 } },
    { cap: "There are 3 colours, and 2 bits give 4 codes, so the <b>colour depth</b> is 2 bits. Each colour is given a <b>unique binary code</b>.", s: { k: 1 } }];
  G.forEach((row, r) => steps.push({ cap: `Row ${r + 1}: the code for each pixel's colour is written, left to right, and added to the stored data.`, s: { k: 2 + r } }));
  steps.push({ cap: "All 24 codes are stored <b>in sequence</b>, row by row, after a <b>file header</b> that holds the resolution and colour depth. Size = 6 × 4 × 2 = <b>48 bits</b> = 6 bytes, not counting the header.", s: { k: 6 } });
  Lib.stepper($("#stA"), { w: 760, h: 276, label: "Encoding a small bitmap image", base: { k: 0 }, draw, tween: 600, dwell: 3800, steps });
})();

(function () {
  const rows = [["Pixels", "1024 × 512 = 524 288"], ["Bits", "524 288 × 8 = 4 194 304"], ["Bytes", "4 194 304 ÷ 8 = 524 288"], ["Kibibytes", "524 288 ÷ 1024 = 512"], ["Mebibytes", "512 ÷ 1024 = 0.5"]];
  const draw = (s) => {
    let o = SV.text(380, 34, "file size = width × height × colour depth", "lbl bd t3", { "text-anchor": "middle" });
    rows.forEach((r, i) => { const v = clamp01(s.k - i); if (v > 0) o += SV.rect(80, 56 + i * 46, 600, 38, ["f1", "f2", "f3", "f1", "f2"][i], { rx: 8, ...op(0.45 * v) }) + SV.text(100, 81 + i * 46, r[0], "lbl bd", op(v)) + SV.text(300, 81 + i * 46, r[1], "lbl", { style: "font-family:var(--mono)", ...op(v) }); });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 296, label: "Calculating the size of a 1024 by 512 bitmap with 8 bits per pixel", base: { k: 0 }, draw, tween: 600, dwell: 3800, steps: [
    { cap: "Start with the formula. The image is 1024 pixels wide, 512 pixels high, with a colour depth of 8 bits.", s: { k: 0 } },
    { cap: "Multiply the width by the height to get the <b>number of pixels</b>: 524 288.", s: { k: 1 } },
    { cap: "Multiply by the <b>bits per pixel</b>: 524 288 × 8 = 4 194 304 bits.", s: { k: 2 } },
    { cap: "Divide by 8 to get <b>bytes</b>: 524 288.", s: { k: 3 } },
    { cap: "Divide by 1024 to get <b>kibibytes</b>: 512.", s: { k: 4 } },
    { cap: "Divide by 1024 again to get <b>mebibytes</b>: <b>0.5 MiB</b>. This is the answer the exam wanted.", s: { k: 5 } }] });
})();

(function () {
  const pix = (cx, cy, r, ox, oy, c) => { let o = ""; const n = 12, S = 24; for (let i = 0; i < n * 2; i++) for (let j = 0; j < n * 2; j++) { const x = (i + 0.5) * S / 2 - r, y = (j + 0.5) * S / 2 - r; if (x * x + y * y <= r * r) o += SV.rect(ox + i * S / 2, oy + j * S / 2, S / 2, S / 2, "f3", { style: `fill:${c};opacity:1` }); } return o; };
  const draw = (s) => {
    const a = clamp01(s.a), b = clamp01(s.b), z = clamp01(s.z);
    let o = SV.rect(24, 24, 330, 200, "f3", { rx: 8, ...op(0.18) });
    if (a > 0) o += SV.rect(50, 150, 140, 54, "f1", { rx: 4, ...op(0.7 * a) });
    if (b > 0) o += SV.circle(250, 100, 44 + 14 * z * 0, "f3", { style: `fill:${COL.Y};opacity:${b}` });
    if (s.l > 0) o += SV.line(60, 70, 190, 130, "c3", { "stroke-width": 4, ...op(clamp01(s.l)) });
    const list = [["Rectangle", "x 50, y 150, 140 × 54, fill blue", a], ["Circle", "centre (250, 100), r 44, fill yellow", b], ["Line", "(60, 70) to (190, 130), weight 4", clamp01(s.l)]];
    o += SV.text(400, 40, "Drawing list", "lbl bd t3");
    list.forEach((it, i) => { if (it[2] > 0) o += SV.text(400, 76 + i * 44, it[0], "lbl bd", op(it[2])) + SV.text(400, 96 + i * 44, it[1], "sm", { style: "font-family:var(--mono)", ...op(it[2]) }); });
    if (z > 0) { o = SV.rect(24, 24, 330, 200, "f3", { rx: 8, ...op(0.18) }) + SV.text(110, 52, "Vector, enlarged", "lbl bd t1", op(z)) + SV.circle(110, 140, 66, "f3", { style: `fill:${COL.Y};opacity:${z}` }) + SV.text(500, 52, "Bitmap, enlarged", "lbl bd t3", op(z)) + pix(0, 0, 66, 434, 74, COL.Y).replace(/opacity:1/g, "opacity:" + z); }
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "A vector drawing list and enlarging it against a bitmap", base: { a: 0, b: 0, l: 0, z: 0 }, draw, tween: 600, dwell: 4000, steps: [
    { cap: "A vector graphic is stored as a <b>drawing list</b>. First <b>drawing object</b>: a rectangle, with the <b>properties</b> position, size and fill colour.", s: { a: 1 } },
    { cap: "Second object: a circle with its centre, radius and fill colour. Each object keeps its own properties.", s: { a: 1, b: 1 } },
    { cap: "Third object: a line with its end points and weight. The file holds only this list, not a colour for every pixel.", s: { a: 1, b: 1, l: 1 } },
    { cap: "Enlarge the picture. The vector circle is <b>recalculated</b> and stays smooth. A bitmap of the same circle only makes each pixel bigger, so the edge becomes stepped (<b>pixelated</b>).", s: { a: 1, b: 1, l: 1, z: 1 } }] });
})();

/* Lab 1 */
(function () {
  let W = 1024, H = 512, bd = 8;
  const depths = [1, 2, 4, 8, 16, 24, 32];
  const paint = () => {
    $$("#fb button").forEach((b, i) => b.classList.toggle("pri", depths[i] === bd));
    const px = W * H, bits = px * bd, by = bits / 8;
    $("#f0").textContent = (2 ** bd).toLocaleString("en-GB"); $("#f1").textContent = bits.toLocaleString("en-GB"); $("#f2").textContent = by.toLocaleString("en-GB"); $("#f3").textContent = Lib.fmtN(by / 1024, 2); $("#f4").textContent = Lib.fmtN(by / 1048576, 3);
    $("#fv").textContent = `${W.toLocaleString("en-GB")} × ${H.toLocaleString("en-GB")} × ${bd} = ${bits.toLocaleString("en-GB")} bits. ÷ 8 = ${by.toLocaleString("en-GB")} bytes. ÷ 1024 ÷ 1024 = ${Lib.fmtN(by / 1048576, 3)} MiB (${Lib.fmtN(by / 1e6, 3)} MB).`;
  };
  $("#fb").innerHTML = depths.map((d, i) => `<button class="b" data-i="${i}">${d} bit${d > 1 ? "s" : ""}</button>`).join("");
  $$("#fb button").forEach((b) => (b.onclick = () => { bd = depths[+b.dataset.i]; paint(); }));
  Lib.slider($("#fw"), { id: "fws", label: "Width (pixels) ", min: 16, max: 4096, step: 16, value: W, fmt: (x) => x.toLocaleString("en-GB"), onInput: (v) => { W = v; paint(); } });
  Lib.slider($("#fh"), { id: "fhs", label: "Height (pixels) ", min: 16, max: 4096, step: 16, value: H, fmt: (x) => x.toLocaleString("en-GB"), onInput: (v) => { H = v; paint(); } });
})();

/* Lab 2 */
(function () {
  const pal = ["#f4f4f0", "#c0392b", "#2f5fa8", "#2e8b57"], N = 8; let bd = 1;
  const g = Array.from({ length: N * N }, (_, i) => ((i % N) + Math.floor(i / N)) % 2 === 0 && i % 3 === 0 ? 1 : 0);
  const paint = () => {
    $$("#pxB button").forEach((b, i) => b.classList.toggle("pri", i + 1 === bd));
    g.forEach((v, i) => { if (v >= 2 ** bd) g[i] = 0; });
    let o = ""; g.forEach((v, i) => { o += SV.rect(10 + (i % N) * 37, 10 + Math.floor(i / N) * 37, 35, 35, "f3", { rx: 3, "data-i": i, style: `fill:${pal[v]};opacity:1;stroke:var(--line);cursor:pointer` }); });
    $("#pxS").innerHTML = o;
    $("#p1").textContent = 2 ** bd; $("#p2").textContent = N * N * bd + " bits = " + (N * N * bd) / 8 + " bytes";
    $("#p3").textContent = Array.from({ length: N }, (_, r) => g.slice(r * N, r * N + N).map((v) => bin(v, bd)).join(" ")).join("\n");
  };
  $("#pxB").innerHTML = [1, 2].map((d) => `<button class="b" data-d="${d}">${d} bit per pixel</button>`).join("").replace("1 bit per pixel", "1 bit per pixel").replace("2 bit per pixel", "2 bits per pixel");
  $$("#pxB button").forEach((b) => (b.onclick = () => { bd = +b.dataset.d; paint(); }));
  $("#pxS").addEventListener("click", (e) => { const i = e.target.getAttribute && e.target.getAttribute("data-i"); if (i === null || i === undefined) return; g[+i] = (g[+i] + 1) % 2 ** bd; paint(); });
  paint();
})();

/* Lab 3 */
(function () {
  let res = 16, bd = 8;
  const val = (x, y) => { const dx = x - 0.5, dy = y - 0.5, d = Math.hypot(dx, dy); return Math.max(0, Math.min(1, 1 - d * 1.6 + 0.25 * Math.sin(x * 6) * Math.cos(y * 5))); };
  const paint = () => {
    const w = res, h = Math.round(res * 0.7), lv = 2 ** bd; let o = "";
    for (let j = 0; j < h; j++) for (let i = 0; i < w; i++) { const v = val((i + 0.5) / w, (j + 0.5) / h), q = Math.round(v * (lv - 1)) / (lv - 1), L = Math.round(20 + q * 72); o += `<rect x="${(i * 320) / w}" y="${(j * 224) / h}" width="${320 / w + 0.4}" height="${224 / h + 0.4}" style="fill:hsl(205,60%,${L}%)"/>`; }
    $("#qS").innerHTML = o;
    $("#q1").textContent = `${w} × ${h}`; $("#q2").textContent = lv.toLocaleString("en-GB"); $("#q3").textContent = w * h * bd < 8192 ? w * h * bd + " bits" : Lib.fmtN((w * h * bd) / 8 / 1024, 2) + " KiB";
    $("#qv").textContent = res <= 16 && bd >= 6 ? "Low resolution: the shapes are blocky even though there are many shades." : bd <= 2 && res >= 32 ? "Few shades: the smooth gradient breaks into bands, even with many pixels." : res >= 32 && bd >= 6 ? "High resolution and many shades: smooth and detailed, but the largest file." : "A trade-off between quality and file size.";
  };
  const rs = [8, 16, 32, 64];
  Lib.slider($("#qr"), { id: "qrs", label: "Pixels across (resolution) ", min: 0, max: 3, value: 1, fmt: (x) => rs[x], onInput: (v) => { res = rs[v]; paint(); } });
  Lib.slider($("#qd"), { id: "qds", label: "Colour depth (bits) ", min: 1, max: 8, value: 8, fmt: (x) => x, onInput: (v) => { bd = v; paint(); } });
})();

btnTable("vB", "vO", [
  ["Holiday photograph", "Bitmap", "Photographs have millions of small colour changes that a list of simple shapes cannot describe. Each pixel stores its own colour.", "Saying bitmap files are small. They are usually large."],
  ["Company logo on a letterhead and a billboard", "Vector", "Made of simple shapes, recalculated for any size so no pixelation, and a small file.", "Choosing bitmap because it is 'more detailed' without a reason for a logo."],
  ["Floor plan that an architect keeps editing", "Vector", "Each wall or window is a separate drawing object with properties that can be edited without redrawing everything.", "Forgetting to name the drawing object and its properties."],
  ["Scanned old family photograph", "Bitmap", "The scan is a grid of pixels with continuous shading, which a vector graphic cannot store accurately.", "Calling a scan a vector graphic because it is on a computer."],
  ["Icon that is shown on a phone, a tablet and a poster", "Vector", "One drawing list works at every size without pixelation, so one file serves all.", "Describing the three sizes without saying the shapes are recalculated."],
  ["Pixel-art character in a retro game", "Bitmap", "The art is drawn pixel by pixel, so the colour of each pixel matters.", "Using vector because the image is simple."]
], ["Task", "Better choice", "Reasons that earn marks", "Trap"]);
Lib.classify($("#cl1"), { prompt: "Does each description belong to a bitmap or a vector graphic?", buckets: [{"label": "Bitmap"}, {"label": "Vector graphic"}], items: [{"text": "Pixel", "b": 0}, {"text": "Drawing list", "b": 1}, {"text": "Colour depth", "b": 0}, {"text": "Drawing object", "b": 1}, {"text": "File header", "b": 0}, {"text": "Property such as line weight", "b": 1}, {"text": "Looks blocky when enlarged", "b": 0}, {"text": "Recalculated when resized", "b": 1}], done: "Pixels, colour depth and file headers are bitmap terms. Drawing objects, properties and drawing lists are vector terms." });
Lib.classify($("#cl2"), { prompt: "What happens to a bitmap file's size?", buckets: [{"label": "Larger"}, {"label": "Smaller"}, {"label": "No change"}], items: [{"text": "Increase the colour depth from 8 to 24 bits", "b": 0}, {"text": "Reduce the image resolution to half the width and height", "b": 1}, {"text": "Change the screen resolution of the monitor", "b": 2}, {"text": "Change one pixel from blue to green", "b": 2}, {"text": "Increase the image resolution", "b": 0}, {"text": "Reduce the colour depth from 16 to 8 bits", "b": 1}], done: "The size depends on the number of pixels and the bits per pixel. The display and one pixel's colour do not change either." });
Lib.order($("#o1"), { prompt: "Put the steps for estimating a bitmap file size in order.", items: ["Write down the width, height and bits per pixel", "Multiply width × height to get the number of pixels", "Multiply by the bits per pixel", "Divide by 8 to get bytes", "Divide by 1024 (and again) for kibibytes or mebibytes"], done: "Pixels, then bits, then bytes, then the larger units." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Pixel", "The smallest element of a bitmap, one square of one colour"], ["Image resolution", "Pixels wide × pixels high in the image"], ["Colour depth", "Bits used for the colour of each pixel"], ["File header", "Data about the image stored with the pixel data"], ["Drawing list", "All the drawing objects in a vector graphic, with commands to draw each"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many colours can be represented with 8 bits per pixel?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "What is the smallest bit depth for an image with 20 colours?", "a": 5, "unit": "bits", "tol": 0.01, "hint": "2^4 = 16 is too few; 2^5 = 32.", "sol": "<b>5</b> bits."},
  {"q": "A bitmap is 800 × 600 pixels with a colour depth of 8 bits. How many bytes is the file (ignoring the header)?", "a": 480000, "unit": "bytes", "tol": 0.01, "hint": "800 × 600 × 8 ÷ 8.", "sol": "<b>480 000</b> bytes."},
  {"q": "A bitmap is 2048 × 1024 pixels with a colour depth of 24 bits. How many mebibytes?", "a": 6, "unit": "MiB", "tol": 0.01, "hint": "2048 × 1024 × 3 bytes ÷ 1 048 576.", "sol": "<b>6</b> MiB."},
  {"q": "A bitmap has 4 million pixels and a colour depth of 16 bits. How many megabytes (1 MB = 1 000 000 bytes)?", "a": 8, "unit": "MB", "tol": 0.01, "hint": "4 000 000 × 2 bytes.", "sol": "<b>8</b> MB."},
  {"q": "A photograph uses 24 bits per pixel. It is changed to 8 bits per pixel. What fraction of the original size remains (as a decimal)?", "a": 0.333, "unit": "", "tol": 0.01, "hint": "8 ÷ 24.", "sol": "<b>0.333</b>, a third of the size."},
  {"q": "An image is 16 × 16 pixels at 2 bits per pixel. How many bits are stored?", "a": 512, "unit": "bits", "tol": 0.01, "hint": "256 pixels × 2.", "sol": "<b>512</b> bits."},
  {"q": "A bitmap has a bit depth of 3 bytes and a resolution of 100 × 100 pixels. How many bytes?", "a": 30000, "unit": "bytes", "tol": 0.01, "hint": "10 000 pixels × 3. The depth is already in bytes.", "sol": "<b>30 000</b> bytes."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a pixel?", opts: ["A row of identical colours", "The binary code for a colour", "The smallest element of an image that can be one colour", "The number of colours in an image"], a: 2, why: "A pixel is the smallest element of a bitmap and has one colour." },
  { q: "Which change does NOT alter the size of a bitmap file?", opts: ["Doubling the image width", "Changing the colour depth from 8 to 16 bits", "Changing the screen resolution of the monitor", "Halving the image height"], a: 2, why: "Screen resolution changes the display, not the stored image." },
  { q: "Which statement about a vector graphic is correct?", opts: ["It stores a colour for every pixel", "It stores a drawing list of objects and their properties", "It always has a larger file than a bitmap", "It becomes pixelated when enlarged"], a: 1, why: "A vector graphic is a drawing list." },
  { q: "What is a drawing object?", opts: ["The colour of a shape", "An individual element such as a line or circle", "A list of every pixel", "The file type"], a: 1, why: "Drawing objects are the elements; properties describe them." },
  { q: "Why is a vector graphic a good choice for a logo that will be printed at many sizes?", opts: ["It stores more colours", "It is recalculated at each size so it does not pixelate", "It uses a larger file", "It cannot be edited"], a: 1, why: "Recalculation keeps the edges smooth at any size." },
  { q: "A bitmap uses 6 colours. What is the smallest bit depth?", opts: ["2", "3", "4", "6"], a: 1, why: "2^2 = 4 is too few; 2^3 = 8 covers 6 colours." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Pixel", "Smallest element of a bitmap. One square, one colour."],
  ["Image resolution", "Pixels wide × pixels high."],
  ["Screen resolution", "Pixels the screen can display."],
  ["Colour depth", "Bits per pixel. n bits = 2^n colours."],
  ["File header", "Data about the file: type, size, dimensions, colour depth."],
  ["File size", "Width × height × bit depth ÷ 8 for bytes."],
  ["Drawing object", "One element of a vector image: line, circle, rectangle."],
  ["Property", "Attribute of a drawing object: fill colour, line weight."],
  ["Drawing list", "All the drawing objects and the commands to draw them."],
] });
