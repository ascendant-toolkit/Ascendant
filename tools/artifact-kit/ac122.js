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

const QZ = (v, bits) => { const L = 2 ** bits; return Math.round(((v + 1) / 2) * (L - 1)) / (L - 1) * 2 - 1; };
const QI = (v, bits) => Math.round(((v + 1) / 2) * (2 ** bits - 1));
/* wave drawing: o = {n: samples per cycle, bits, dots, levels, recon, orig}. Two cycles across 680px. */
function waveSvg(o) {
  const X0 = 40, W = 680, Y0 = 130, A = 90, cyc = 2, n = Math.max(2, Math.round(o.n)), bits = Math.max(1, Math.round(o.bits)), L = 2 ** bits;
  const f = (t) => Math.sin(2 * Math.PI * cyc * t), X = (t) => X0 + t * W, Y = (v) => Y0 - v * A;
  let s = SV.line(X0, Y0, X0 + W, Y0, "ax") + SV.line(X0, 24, X0, 236, "ax");
  if (o.levels > 0 && bits <= 5) for (let i = 0; i < L; i++) s += SV.line(X0, Y((i / (L - 1)) * 2 - 1), X0 + W, Y((i / (L - 1)) * 2 - 1), "dash", op(0.5 * o.levels));
  const pts = []; for (let k = 0; k <= 400; k++) pts.push([X(k / 400), Y(f(k / 400))]);
  s += SV.path(ptsPath(pts), "c1", { fill: "none", "stroke-width": 2.5, opacity: o.orig === undefined ? 0.4 : o.orig });
  const N = n * cyc, sp = []; for (let i = 0; i <= N; i++) { const t = i / N; sp.push([X(t), Y(QZ(f(t), bits))]); }
  if (o.recon > 0) s += SV.path(ptsPath(sp), "c3", { fill: "none", "stroke-width": 3, opacity: o.recon });
  if (o.dots > 0) sp.forEach((p) => { s += SV.line(p[0], Y0, p[0], p[1], "dash", op(0.45 * o.dots)) + SV.circle(p[0], p[1], 4.5, "dot2", op(o.dots)); });
  return s;
}
function waveMatch(n, bits) {
  const cyc = 2, N = n * cyc, f = (t) => Math.sin(2 * Math.PI * cyc * t), v = Array.from({ length: N + 1 }, (_, i) => QZ(f(i / N), bits));
  let e = 0; const M = 400;
  for (let k = 0; k <= M; k++) { const t = k / M, p = t * N, i = Math.min(N - 1, Math.floor(p)), fr = p - i, r = v[i] * (1 - fr) + v[i + 1] * fr; e += Math.abs(r - f(t)); }
  return Math.max(0, 100 - (e / (M + 1) / 2) * 100 * 2);
}

(function () {
  const rowsOf = (n, bits) => Array.from({ length: Math.min(8, n * 2 + 1) }, (_, i) => bin(QI(Math.sin(2 * Math.PI * 2 * (i / (n * 2))), bits), bits));
  const draw = (s) => {
    let o = waveSvg({ n: 8, bits: s.q, dots: s.d, levels: s.l, recon: s.r, orig: 0.4 }), codes = rowsOf(8, Math.round(s.q)).join("  ");
    if (s.t > 0) o += SV.text(40, 268, "first samples: " + codes, "lbl bd", { style: "font-family:var(--mono);font-size:14px", ...op(s.t) });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 284, label: "Sampling a sound wave and storing each sample in binary", base: { q: 8, d: 0, l: 0, r: 0, t: 0 }, draw, tween: 700, dwell: 4200, steps: [
    { cap: "The curve is an <b>analogue</b> sound wave: continuous, with a value at every instant. A computer cannot store a continuous curve.", s: {} },
    { cap: "Measure the <b>amplitude</b> at regular intervals. Each dot is a <b>sample</b>. Here there are 8 samples per wave cycle; the number taken each second is the <b>sampling rate</b>.", s: { d: 1 } },
    { cap: "Each sample must be stored with a limited number of bits. With a <b>sampling resolution</b> of 3 bits there are only 8 allowed amplitudes (the dashed lines), so each sample is rounded to the nearest one. The gap is the <b>quantisation error</b>.", s: { d: 1, l: 1, q: 3 } },
    { cap: "Joining the stored samples gives the <b>digital</b> version (green): a stepped copy of the original.", s: { d: 1, l: 1, q: 3, r: 1 } },
    { cap: "Each sample is stored as a <b>binary number</b>, <b>in sequence</b>. With 3 bits each sample uses 3 bits of the file.", s: { d: 1, l: 1, q: 3, r: 1, t: 1 } }] });
})();

(function () {
  const draw = (s) => waveSvg({ n: s.n, bits: 8, dots: 1, recon: 1, orig: 0.4 }) + SV.text(40, 262, "samples per cycle: " + Math.round(s.n) + "  (stored per 2 cycles: " + Math.round(s.n) * 2 + ")", "lbl bd", { style: "font-size:15px" });
  Lib.stepper($("#stB"), { w: 760, h: 276, label: "Increasing the sampling rate", base: { n: 4 }, draw, tween: 900, dwell: 4000, steps: [
    { cap: "Only <b>4</b> samples per cycle: big gaps, and the green copy is a rough triangle. The file is small.", s: { n: 4 } },
    { cap: "<b>8</b> samples per cycle: smaller gaps between samples, so the digital wave is closer to the analogue wave.", s: { n: 8 } },
    { cap: "<b>16</b> samples per cycle: the copy is almost on top of the original, so quantisation errors are smaller. But there are four times as many samples as the first picture, so the file is larger.", s: { n: 16 } }] });
})();

(function () {
  const draw = (s) => waveSvg({ n: 16, bits: s.b, dots: 1, levels: 1, recon: 1, orig: 0.4 }) + SV.text(40, 262, Math.round(s.b) + " bits per sample = " + 2 ** Math.round(s.b) + " amplitudes", "lbl bd", { style: "font-size:15px" });
  Lib.stepper($("#stC"), { w: 760, h: 276, label: "Increasing the sampling resolution", base: { b: 2 }, draw, tween: 900, dwell: 4000, steps: [
    { cap: "<b>2 bits</b> per sample: only 4 amplitudes. Every sample is rounded a long way, so the quantisation errors are large.", s: { b: 2 } },
    { cap: "<b>3 bits</b>: 8 amplitudes. Each stored value is closer to the true amplitude.", s: { b: 3 } },
    { cap: "<b>4 bits</b>: 16 amplitudes. The steps are smaller and the copy is closer to the original, but every sample now needs twice the bits of the first picture.", s: { b: 4 } }] });
})();

(function () {
  const rows = [["Rate", "50 kHz = 50 000 samples per second"], ["Time", "20 minutes = 1200 seconds"], ["Samples", "50 000 × 1200 = 60 000 000"], ["Bits", "60 000 000 × 16 = 960 000 000"], ["Bytes", "960 000 000 ÷ 8 = 120 000 000"], ["Megabytes", "120 000 000 ÷ 1 000 000 = 120"]];
  const draw = (s) => {
    let o = SV.text(380, 30, "size (bits) = rate × resolution × time", "lbl bd t3", { "text-anchor": "middle" });
    rows.forEach((r, i) => { const v = clamp01(s.k - i); if (v > 0) o += SV.rect(60, 48 + i * 42, 640, 34, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.42 * v) }) + SV.text(80, 71 + i * 42, r[0], "lbl bd", op(v)) + SV.text(240, 71 + i * 42, r[1], "lbl", { style: "font-family:var(--mono)", ...op(v) }); });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 306, label: "Calculating a sound file size", base: { k: 0 }, draw, tween: 600, dwell: 3800, steps: [
    { cap: "A message is recorded at <b>50 kHz</b> with <b>16 bits</b> per sample for <b>20 minutes</b>.", s: { k: 0 } },
    { cap: "Convert the rate to samples per second: 50 kHz is <b>50 000</b>.", s: { k: 1 } },
    { cap: "Convert the time to seconds: 20 × 60 = <b>1200</b>.", s: { k: 2 } },
    { cap: "Number of samples: 50 000 × 1200 = <b>60 million</b>.", s: { k: 3 } },
    { cap: "Each sample is 16 bits: 60 000 000 × 16 = <b>960 000 000 bits</b>.", s: { k: 4 } },
    { cap: "Divide by 8 for bytes: <b>120 000 000</b>.", s: { k: 5 } },
    { cap: "Divide by 1 000 000 for megabytes: <b>120 MB</b>.", s: { k: 6 } }] });
})();

/* Lab 1 */
(function () {
  let n = 8, b = 3;
  const paint = () => {
    $("#w1").textContent = n; $("#w2").textContent = (2 ** b).toLocaleString("en-GB"); $("#w3").textContent = n * b; const m = waveMatch(n, b); $("#w4").textContent = Lib.fmtN(m, 0) + "%";
    $("#wS").innerHTML = waveSvg({ n, bits: b, dots: 1, levels: 1, recon: 1, orig: 0.4 });
    $("#wv").textContent = m > 96 ? "Very close to the original. The file needs " + n * b + " bits per cycle." : m > 85 ? "A fair copy, with visible steps or gaps. " + n * b + " bits per cycle." : "A poor copy: the digital wave is far from the analogue wave. Only " + n * b + " bits per cycle.";
  };
  Lib.slider($("#wr"), { id: "wrs", label: "Samples per cycle (rate) ", min: 2, max: 48, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } });
  Lib.slider($("#wb"), { id: "wbs", label: "Bits per sample (resolution) ", min: 1, max: 8, value: b, fmt: (x) => x, onInput: (v) => { b = v; paint(); } });
})();

/* Lab 2 */
(function () {
  let r = 44100, bd = 16, ch = 1, t = 180;
  const rates = [[8000, "8 kHz"], [22050, "22.05 kHz"], [44100, "44.1 kHz"], [48000, "48 kHz"], [96000, "96 kHz"]], bs = [8, 16, 24], cs = [[1, "Mono"], [2, "Stereo"]];
  const paint = () => {
    $$("#rB button").forEach((x, i) => x.classList.toggle("pri", rates[i][0] === r)); $$("#bB button").forEach((x, i) => x.classList.toggle("pri", bs[i] === bd)); $$("#cB button").forEach((x, i) => x.classList.toggle("pri", cs[i][0] === ch));
    const bits = r * bd * t * ch, by = bits / 8;
    $("#z1").textContent = bits.toLocaleString("en-GB"); $("#z2").textContent = by.toLocaleString("en-GB"); $("#z3").textContent = Lib.fmtN(by / 1e6, 2); $("#z4").textContent = Lib.fmtN(by / 1048576, 2);
    $("#zv").textContent = `${r.toLocaleString("en-GB")} × ${bd} × ${t} s${ch > 1 ? " × 2 channels" : ""} = ${bits.toLocaleString("en-GB")} bits, which is ${Lib.fmtN(by / 1e6, 2)} MB.`;
  };
  $("#rB").innerHTML = rates.map((x, i) => `<button class="b" data-i="${i}">${x[1]}</button>`).join(""); $("#bB").innerHTML = bs.map((x, i) => `<button class="b" data-i="${i}">${x} bits</button>`).join(""); $("#cB").innerHTML = cs.map((x, i) => `<button class="b" data-i="${i}">${x[1]}</button>`).join("");
  $$("#rB button").forEach((x) => (x.onclick = () => { r = rates[+x.dataset.i][0]; paint(); })); $$("#bB button").forEach((x) => (x.onclick = () => { bd = bs[+x.dataset.i]; paint(); })); $$("#cB button").forEach((x) => (x.onclick = () => { ch = cs[+x.dataset.i][0]; paint(); }));
  Lib.slider($("#dS"), { id: "dsl", label: "Length of recording (seconds) ", min: 1, max: 1200, value: t, fmt: (x) => x + " s", onInput: (v) => { t = v; paint(); } });
})();

btnTable("eB", "eO", [
  ["Increase the sampling rate", "Increases: smaller gaps, closer to the analogue wave, smaller quantisation errors", "Increases: more samples, so more bits stored", "Saying the sound is louder"],
  ["Decrease the sampling rate", "Decreases: bigger gaps, less like the original", "Decreases: fewer samples", "Forgetting that fewer samples also lose detail"],
  ["Increase the sampling resolution", "Increases: more bits per sample, so more amplitude values and a closer match", "Increases: more bits for every sample", "Writing 'more bits' without 'per sample'"],
  ["Decrease the sampling resolution", "Decreases: fewer amplitudes, larger quantisation errors", "Decreases: fewer bits per sample", "Mixing it up with a lower sampling rate"],
  ["Make the recording twice as long", "No change: each moment is recorded as accurately as before", "Doubles", "Claiming a longer recording is more accurate"],
  ["Record in stereo instead of mono", "Not about accuracy of one channel: two channels are recorded", "Doubles (two channels)", "Treating stereo as a higher sampling rate"]
], ["Change", "Accuracy", "File size", "Trap"]);
Lib.classify($("#cl1"), { prompt: "Does the description fit the sampling rate or the sampling resolution?", buckets: [{"label": "Sampling rate"}, {"label": "Sampling resolution"}], items: [{"text": "Samples taken per second", "b": 0}, {"text": "Bits used for each sample", "b": 1}, {"text": "Measured in hertz or kilohertz", "b": 0}, {"text": "Measured in bits or bytes", "b": 1}, {"text": "44.1 kHz", "b": 0}, {"text": "16 bits", "b": 1}, {"text": "Decides how many amplitude values can be stored", "b": 1}, {"text": "Decides how often the wave is measured", "b": 0}], done: "Rate is about time (per second). Resolution is about the number of bits for each sample." });
Lib.classify($("#cl2"), { prompt: "What is the effect on the accuracy of the recording?", buckets: [{"label": "Accuracy increases"}, {"label": "Accuracy decreases"}, {"label": "No change to accuracy"}], items: [{"text": "Sampling rate 40 kHz to 60 kHz", "b": 0}, {"text": "Sampling resolution 24 bits to 16 bits", "b": 1}, {"text": "Recording length 20 minutes to 40 minutes", "b": 2}, {"text": "Sampling resolution 8 bits to 16 bits", "b": 0}, {"text": "Sampling rate 44.1 kHz to 22.05 kHz", "b": 1}, {"text": "Saving the same recording to a different folder", "b": 2}], done: "Rate and resolution change accuracy. The length of the recording only changes the size." });
Lib.order($("#o1"), { prompt: "Put the steps for storing sound in order.", items: ["Measure the amplitude of the analogue wave at regular intervals", "Round each measurement to the nearest value that can be stored", "Convert each value to a binary number", "Store the binary numbers in sequence", "Repeat at the sampling rate, for the length of the recording"], done: "Measure, round, convert, store in sequence, repeat." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Analogue", "Continuous data, such as a sound wave"], ["Sampling rate", "The number of samples taken per second"], ["Sampling resolution", "The number of bits used to store each sample"], ["Quantisation error", "The difference between the true amplitude and the stored value"], ["Sample", "One measurement of the amplitude of the wave"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A recording has a sampling rate of 8 kHz. How many samples are taken in 3 seconds?", "a": 24000, "unit": "samples", "tol": 0.01, "hint": "8000 × 3.", "sol": "<b>24 000</b> samples."},
  {"q": "How many different amplitudes can a sampling resolution of 8 bits store?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "A sound is recorded at 20 kHz, 16 bits, for 10 seconds. How many bytes?", "a": 400000, "unit": "bytes", "tol": 0.01, "hint": "20 000 × 16 × 10 ÷ 8.", "sol": "<b>400 000</b> bytes."},
  {"q": "A sound is recorded at 44.1 kHz, 16 bits, for 1 minute. How many megabytes (1 MB = 1 000 000 bytes), to 2 decimal places?", "a": 5.29, "unit": "MB", "tol": 0.02, "hint": "44 100 × 16 × 60 ÷ 8 ÷ 1 000 000.", "sol": "<b>5.29</b> MB."},
  {"q": "A voice message is recorded at 10 kHz, 8 bits, for 2 minutes. How many kilobytes (1 kB = 1000 bytes)?", "a": 1200, "unit": "kB", "tol": 0.01, "hint": "10 000 × 8 × 120 ÷ 8 ÷ 1000.", "sol": "<b>1200</b> kB."},
  {"q": "The sampling resolution is changed from 8 bits to 16 bits. By what factor does the file size change?", "a": 2, "unit": "×", "tol": 0.01, "hint": "16 ÷ 8.", "sol": "<b>2</b> times larger."},
  {"q": "The sampling rate is halved and the sampling resolution is doubled. By what factor does the file size change?", "a": 1, "unit": "×", "tol": 0.01, "hint": "0.5 × 2.", "sol": "<b>1</b>: no change in size."},
  {"q": "A sampling resolution of 3 bytes is how many bits?", "a": 24, "unit": "bits", "tol": 0.01, "hint": "3 × 8.", "sol": "<b>24</b> bits."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does the sampling rate measure?", opts: ["The number of bits for each sample", "The number of samples taken per second", "The loudness of the sound", "The length of the recording"], a: 1, why: "Sampling rate is samples per second." },
  { q: "What does the sampling resolution measure?", opts: ["Samples per second", "Bits used to store each sample", "The pitch of the sound", "The size of the speaker"], a: 1, why: "Sampling resolution is bits per sample." },
  { q: "Increasing the sampling rate has which effect?", opts: ["Digital wave is closer to the analogue wave and the file is larger", "The file is smaller and less accurate", "The sound is louder", "No effect on the file size"], a: 0, why: "More samples per second means a closer copy and more data." },
  { q: "Which change does NOT affect how accurate the recording is?", opts: ["Raising the sampling rate", "Raising the sampling resolution", "Making the recording longer", "Lowering the sampling resolution"], a: 2, why: "The length only affects the file size." },
  { q: "What is a quantisation error?", opts: ["A mistake in the file header", "The difference between the true amplitude and the stored value", "A gap in the recording", "A loss of the network connection"], a: 1, why: "It comes from rounding each sample to a stored value." },
  { q: "What type of data is the sound wave before it is recorded?", opts: ["Digital", "Binary", "Analogue", "Discrete"], a: 2, why: "The wave is continuous, which is analogue." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Analogue", "Continuous data. The sound wave."],
  ["Digital", "Discrete data stored in binary."],
  ["Sampling", "Measuring the amplitude at regular intervals."],
  ["Sampling rate", "Samples per second. Hz or kHz."],
  ["Sampling resolution", "Bits per sample. n bits = 2^n amplitudes."],
  ["Quantisation error", "Gap between true amplitude and stored value."],
  ["Higher rate or resolution", "More accurate, larger file."],
  ["File size", "Rate × resolution × seconds, ÷ 8 for bytes."],
] });
