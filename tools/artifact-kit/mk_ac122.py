"""A Level CS syllabus 1.2.2: sound (sampling rate and resolution). Run: python3 tools/artifact-kit/mk_ac122.py"""
from ak import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Sound is an <b>analogue</b> wave, a continuous signal, and a computer can only store <b>digital</b> data, so the wave is <b>sampled</b>: its amplitude is measured at regular intervals and each measurement is stored as a binary number. The <b>sampling rate</b> is how many samples are taken each second (in hertz), and the <b>sampling resolution</b> is how many bits are used for each sample. A higher rate or a higher resolution makes the digital sound closer to the original, with smaller quantisation errors, but the file is larger because more bits are stored. Two things never change the accuracy: the length of the recording only changes the file size. Marks are for the exact meanings, for the effect on <b>both</b> accuracy and file size, and for a calculation with the working shown.</p></div>

  <h2>1 · Analogue and digital</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Analogue data</th><th>Digital data</th></tr>
    <tr><td>Values</td><td>Continuous: any value in a range</td><td>Discrete: a limited set of values, stored in binary</td></tr>
    <tr><td>Example</td><td>The sound wave in the air, the voltage from a microphone</td><td>The numbers stored in a sound file</td></tr>
    <tr><td>Computer use</td><td>Cannot be stored directly</td><td>Can be stored and processed</td></tr>
  </table></div>
  <p>To record sound, the analogue signal is converted into digital data. To play it back, the digital data is converted back into an analogue signal for the speaker.</p>

  <h2>2 · How sound is sampled and encoded</h2>
  <ol>
    <li>The <b>amplitude</b> (height) of the sound wave is measured at regular time intervals. Each measurement is a <b>sample</b>.</li>
    <li>The number of samples taken each second is the <b>sampling rate</b>, measured in hertz (Hz) or kilohertz (kHz). A rate of 44.1 kHz means the amplitude is measured 44 100 times each second.</li>
    <li>Each measured amplitude is rounded to the nearest of the values that can be stored, and given a <b>binary number</b>. The number of bits for each sample is the <b>sampling resolution</b>. With 16 bits there are 2<sup>16</sup> = 65 536 possible amplitudes; 2 bytes is the same as 16 bits.</li>
    <li>The binary number for each sample is stored <b>in sequence</b>.</li>
  </ol>
  <p>The difference between the true amplitude and the nearest stored value is a <b>quantisation error</b>. The Watch tab animates the rounding.</p>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Unit</th></tr>
    <tr><td><b>Sampling</b></td><td>Measuring the amplitude of the analogue wave at regular intervals</td><td></td></tr>
    <tr><td><b>Sampling rate</b></td><td>The number of samples taken per second</td><td>Hz, kHz</td></tr>
    <tr><td><b>Sampling resolution</b></td><td>The number of bits used to store each sample</td><td>bits (or bytes)</td></tr>
  </table></div>

  <h2>3 · Changing the rate and the resolution</h2>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Accuracy of the recording</th><th>File size</th></tr>
    <tr><td><b>Increase the sampling rate</b></td><td>Smaller gaps between samples, so the digital wave is closer to the analogue wave and quantisation errors are smaller</td><td>More samples are stored, so the file is larger</td></tr>
    <tr><td><b>Decrease the sampling rate</b></td><td>Bigger gaps, so the digital wave is less like the original</td><td>Smaller</td></tr>
    <tr><td><b>Increase the sampling resolution</b></td><td>More bits per sample, so more amplitude values are available and each stored value is closer to the true one</td><td>More bits per sample, so a larger file</td></tr>
    <tr><td><b>Decrease the sampling resolution</b></td><td>Fewer amplitude values, so each stored value is further from the true one</td><td>Smaller</td></tr>
    <tr><td><b>Make the recording longer</b></td><td>No change to accuracy</td><td>More samples overall, so larger</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>Name which setting you are describing. "Sampling rate" is about gaps in time; "sampling resolution" is about the number of values for each sample. A mark scheme that says "must be clear which resolution is being described" will not accept an answer that mixes the two.</div>

  <h2>4 · Estimating the file size</h2>
  <div class="formula">file size (bits) = sampling rate × sampling resolution × time (seconds)</div>
  <p>Convert the time to seconds and the rate to samples per second (44.1 kHz = 44 100). Then divide by 8 for bytes and by 1 000 000 (megabytes) or 1024 × 1024 (mebibytes) for larger units. If the question says stereo, there are two channels, so multiply by 2.</p>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>Working</th><th>Answer</th></tr>
    <tr><td>50 kHz, 16 bits, 20 minutes, in megabytes</td><td>50 000 × 16 × 1200 ÷ 8 ÷ 1 000 000</td><td>120 MB</td></tr>
    <tr><td>44.1 kHz, 16 bits, 3 minutes, in bytes</td><td>44 100 × 16 × 180 ÷ 8</td><td>15 876 000 bytes</td></tr>
    <tr><td>8 kHz, 8 bits, 1 minute, in kibibytes</td><td>8000 × 8 × 60 ÷ 8 ÷ 1024</td><td>468.75 KiB</td></tr>
  </table></div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing that a higher sampling rate makes the sound louder or higher pitched. It makes the recording more accurate.</li>
    <li>Saying "more bits" without saying "per sample" for the resolution.</li>
    <li>Forgetting to convert minutes to seconds, or kilohertz to hertz.</li>
    <li>Giving the effect on accuracy but not on file size, when the question asks about both.</li>
    <li>Describing the sampling rate as "how often the sound is recorded" without the unit of time. Say "per second".</li>
  </ul>
'''

watch = '''
  <h2>1 · From a sound wave to binary</h2>
  <p>Press Play, or click the numbered steps. The faint curve is the original analogue wave.</p>
  <div id="stA"></div>
  <h2>2 · A higher sampling rate</h2>
  <div id="stB"></div>
  <h2>3 · A higher sampling resolution</h2>
  <div id="stC"></div>
  <h2>4 · Working out a sound file size</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Sample the wave yourself</h2>
  <p>Drag the sampling rate (samples per wave cycle) and the sampling resolution (bits). The green line joins the stored samples. The match shows how close the digital version is to the original.</p>
  <div class="card"><div id="wr"></div><div id="wb"></div>
    <div class="readout"><div><small>Samples per cycle</small><strong id="w1"></strong></div><div><small>Different amplitudes</small><strong id="w2"></strong></div><div><small>Stored bits per cycle</small><strong id="w3"></strong></div><div><small>Match to the original</small><strong id="w4"></strong></div></div>
    <svg id="wS" viewBox="0 0 760 270" role="img" aria-label="A sound wave and its samples"></svg>
    <div class="verdict" id="wv"></div></div>

  <h2>Lab 2 · Sound file size</h2>
  <p>Choose the settings and the length. The working follows rate × resolution × time.</p>
  <div class="card"><div id="rB" class="btnrow"></div><div id="bB" class="btnrow"></div><div id="cB" class="btnrow"></div><div id="dS"></div>
    <div class="readout"><div><small>Bits</small><strong id="z1"></strong></div><div><small>Bytes</small><strong id="z2"></strong></div><div><small>Megabytes (1 000 000)</small><strong id="z3"></strong></div><div><small>Mebibytes</small><strong id="z4"></strong></div></div>
    <div class="verdict" id="zv"></div></div>

  <h2>Lab 3 · What does this change do?</h2>
  <p>Choose a change. The table gives the effect on accuracy and on file size, in the words the mark scheme uses.</p>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Sampling rate or sampling resolution?</h2><div id="cl1" class="card"></div>
  <h2>2 · What happens to the accuracy?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for digitising sound in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Why a CD uses 44.1 kHz", "People can hear sounds up to roughly 20 kHz. To capture a wave properly, the sampling rate has to be more than twice the highest frequency, so audio CDs use 44 100 samples each second with 16 bits per sample.", "typical rate and resolution: 44.1 kHz and 16 bits, so 44 100 amplitude measurements per second, each stored in 16 bits.") +
rw("Why phone calls sound thin", "Telephone speech has historically been sampled at about 8 kHz with 8 bits. That is enough to make speech understandable, but it removes the higher sounds, so music over a phone line sounds poor.", "a low sampling rate and resolution give a small file and lower accuracy, which is acceptable for speech.") +
rw("High-resolution audio", "Some music is offered at 96 kHz and 24 bits. Each second needs more than three times the data of a CD, and few listeners can hear the difference, so the larger file is a trade-off.", "higher rate and resolution: more accurate, much larger file.") +
rw("Voice notes", "A voice recording app often uses a low sampling rate and one channel so that messages are small enough to send quickly, since a voice does not need the range of music.", "choose settings to suit the use: smaller file against accuracy.") +
rw("A recording that is twice as long", "A podcast recorded for 40 minutes instead of 20 is not twice as accurate. It has the same quality, and the file is twice as big.", "the length of a recording changes the file size only, not the accuracy.")
)

items = [("w22_11", "1(d)", 3), ("w21_11", "7(a)", 4), ("s23_13", "3(c)", 7), ("w22_13", "1(a)-(b)", 4), ("w23_12", "6(b)", 3), ("s24_11", "2(d)", 3), ("s25_13", "1(b)", 3), ("s26_12", "4", 4), ("s26_13", "3(a)", 1)]

exam = aexam("sound",
  "Nine questions from the 2021 to 2026 Paper 1 papers. Sound questions reward the exact meaning of rate and resolution, the effect on both accuracy and file size, and a calculation with the working shown. The figures here are changed from the originals.",
  items, [
  ceq(AP("w22_11", "1(d)"), "[3]", "Sound samples are recorded and saved in a file. (i) State what is meant by sampling rate. (ii) Explain the effect of increasing the sampling resolution on the sound file.",
      ["The number of samples taken per second.", "More bits are used for each sample, so a wider range of values is available and the file size increases.", "The digital wave is closer to the original analogue wave, with smaller quantisation errors."],
      "<p>One mark for the rate, two for the resolution. Give both the file effect and the accuracy effect.</p>",
      [[("k", "Sampling rate is the number of samples taken per second. "), ("a", "Increasing the sampling resolution means more bits for each sample, so more different values can be stored, the digital sound is more accurate, and the file size is larger.")]]) +
  ceq(AP("w21_11", "7(a)"), "[4]", "A sound is recorded several times, with a different sampling rate each time. (i) Describe the reasons why the sound is closer to the original when a higher sampling rate is used. (ii) Describe the reasons why the file size increases when a higher sampling rate is used.",
      ["(i) Smaller time gaps between the samples; the digital wave is more accurate; smaller quantisation errors (two of three).", "(ii) More samples are recorded; so more bits are stored altogether."],
      "<p>(i) accuracy: gaps, closer wave. (ii) size: more samples, so more bits. Keep each part to its own question.</p>",
      [[("k", "(i) There are smaller gaps between the samples, so the digital sound wave follows the analogue wave more closely. (ii) More samples are taken each second, so more bits are stored altogether.")]]) +
  ceq(AP("s23_13", "3(c)"), "[7]", "(i) Describe how sound is represented in a computer. (ii) A second recording needs to be more precise. Explain the reasons why increasing the sampling rate and the sampling resolution will improve the precision.",
      ["(i) The amplitude is recorded a set number of times a second; each amplitude is given a binary number; the binary numbers are saved in sequence.", "(ii) Rate: smaller gaps in the sound wave, so the digital wave is closer to the analogue wave, and quantisation errors are smaller (two).", "Resolution: more bits per sample, so more amplitude values, so each stored value is closer to the analogue value (two)."],
      "<p>Maximum two for rate and two for resolution in (ii). Use the words quantisation errors and analogue.</p>",
      [[("k", "(i) The amplitude of the sound wave is measured a set number of times each second, each amplitude is converted to a binary number, and the numbers are stored in sequence. "), ("a", "(ii) A higher sampling rate gives smaller gaps between the samples, so the digital wave is closer to the analogue wave. A higher sampling resolution gives more bits per sample, so a wider range of amplitudes can be stored and each stored value is closer to the true amplitude, with smaller quantisation errors.")]]) +
  ceq(AP("w22_13", "1(a)-(b)"), "[4]", "A digital audio message is recorded. (i) State whether each action makes the accuracy increase, decrease or stay the same: change the sampling rate from 40 kHz to 60 kHz; change the duration from 20 to 40 minutes; change the sampling resolution from 24 to 16 bits. (ii) The message is recorded at 40 kHz with 16 bits for 10 minutes. Calculate the file size in megabytes. Show your working.",
      ["Rate up: accuracy increases. Duration longer: no change. Resolution down: accuracy decreases.", "Working 40 000 × 16 × 600 ÷ 8, answer 48 MB."],
      "<p>10 minutes = 600 s. 40 000 × 16 × 600 = 384 000 000 bits ÷ 8 = 48 000 000 bytes = 48 MB.</p>",
      [[("k", "Accuracy increases, stays the same, decreases. "), ("a", "40 000 × 16 × 600 = 384 000 000 bits ÷ 8 = 48 000 000 bytes = 48 megabytes.")]]) +
  ceq(AP("w23_12", "6(b)"), "[3]", "Explain the impact of changing the sampling resolution on the accuracy of a sound recording.",
      ["Increasing: more bits per sample; more amplitudes can be represented; each stored value is closer to the analogue value; quantisation errors reduced; the digital wave is closer to the original.", "Decreasing: the opposite, with fewer values and more quantisation error (the reverse argument is accepted)."],
      "<p>Pick a direction and give three linked points: bits per sample, number of values, closeness to the original.</p>",
      [[("k", "Increasing the sampling resolution gives more bits per sample, so more amplitude values can be represented. Each stored amplitude is therefore closer to the analogue amplitude and the quantisation errors are smaller, so the digital wave is closer to the original.")]]) +
  ceq(AP("s24_11", "2(d)"), "[3]", "A doorbell's microphone is changed from a sampling rate of 44.1 kHz to 88.2 kHz. Describe how this affects the performance of the doorbell.",
      ["More data to transmit, so transmission to the smartphone takes longer.", "The secondary storage fills faster.", "Fewer videos can be stored long term, or videos are overwritten more often."],
      "<p>This question asks about performance, not sound quality. Think about the extra data: transmission time and storage.</p>",
      [[("a", "Doubling the sampling rate doubles the number of samples, so there is more data to transmit and the video takes longer to reach the smartphone. The storage device fills faster, so fewer videos can be kept before the oldest are overwritten.")]]) +
  ceq(AP("s25_13", "1(b)"), "[3]", "Write the sound term for each description: (i) the number of times the amplitude is measured per time interval; (ii) the number of bits used to store each amplitude measurement; (iii) the type of sound wave before it is recorded by a computer.",
      ["Sampling rate.", "Sampling resolution.", "Analogue."],
      "<p>One mark each. Rate is about time; resolution is about bits.</p>",
      [[("k", "(i) sampling rate; (ii) sampling resolution; (iii) analogue.")]]) +
  ceq(AP("s26_12", "4"), "[4]", "A sound file has a sampling rate of 44.1 kHz. (i) Describe what is meant by a sampling rate of 44.1 kHz. (ii) A student makes a recording with a sampling resolution of 2 bytes and a second recording of the same sound with a sampling resolution of 8 bits. Explain how the two recordings and the two files will be affected.",
      ["(i) The sound wave is measured 44 100 times each second.", "(ii) 2 bytes (16 bits) means more bits per sample, so the file is larger, and the sound is more accurate to the original because a greater range of amplitudes can be recorded, with smaller quantisation errors. The 8-bit recording is the reverse: smaller file, less accurate."],
      "<p>Say which resolution you are describing. 2 bytes = 16 bits, so the 8-bit recording has half the bits per sample.</p>",
      [[("k", "(i) The amplitude of the sound wave is measured 44 100 times every second. "), ("a", "(ii) The 2 byte recording uses 16 bits per sample, so its file is larger and it is closer to the original because more amplitudes can be stored. The 8-bit recording has fewer bits per sample, so a smaller file but larger quantisation errors and less accuracy.")]]) +
  ceq(AP("s26_13", "3(a)"), "[1]", "A sound is recorded with a sampling resolution of 2 bytes. State what is meant by this.",
      ["Each sample is stored as a 16-bit binary number, or there are 65 536 different amplitudes that can be recorded."],
      "<p>2 bytes = 16 bits, and 2<sup>16</sup> = 65 536.</p>",
      [[("k", "Each sample is stored using 16 bits, so 65 536 different amplitudes can be recorded.")]])
])

tips = tips_html([
  ("Name the setting.", "Say sampling rate (samples per second) or sampling resolution (bits per sample). Do not use 'quality' on its own."),
  ("Give both effects.", "Accuracy and file size. If the question asks about one, answer that one."),
  ("Use the words.", "Quantisation error, analogue, digital waveform, amplitude, sample."),
  ("Convert first.", "Minutes to seconds, kHz to Hz, bytes to bits, before multiplying."),
  ("Time changes size only.", "A longer recording is not more accurate."),
  ("Reverse arguments are fine.", "If the question is about decreasing, the mark scheme allows the opposite of the increase points."),
], [
  ("what sampling rate means", "The sound wave is measured a set number of times every second, for example 44 100 times per second at 44.1 kHz."),
  ("what sampling resolution means", "The number of bits used to store each sample, so the number of different amplitudes that can be recorded."),
  ("effect of a higher sampling rate", "There are smaller gaps between samples, so the digital wave is closer to the analogue wave, but more data is stored so the file is larger."),
  ("effect of a lower sampling resolution", "Fewer amplitudes can be stored, so each value is further from the true amplitude, but the file is smaller."),
], [("State", "A short definition or fact."), ("Describe", "Say how the sound is measured and stored, in order."), ("Explain", "Give the cause and the effect, for accuracy and for file size."), ("Calculate", "Show the conversions and the multiplication, then the answer with its unit.")]) + FC

js = AKJS + r'''
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
''' + CLASSIFY("cl1", "Does the description fit the sampling rate or the sampling resolution?", ["Sampling rate", "Sampling resolution"],
  [("Samples taken per second", 0), ("Bits used for each sample", 1), ("Measured in hertz or kilohertz", 0), ("Measured in bits or bytes", 1), ("44.1 kHz", 0), ("16 bits", 1), ("Decides how many amplitude values can be stored", 1), ("Decides how often the wave is measured", 0)],
  "Rate is about time (per second). Resolution is about the number of bits for each sample.") + CLASSIFY("cl2", "What is the effect on the accuracy of the recording?", ["Accuracy increases", "Accuracy decreases", "No change to accuracy"],
  [("Sampling rate 40 kHz to 60 kHz", 0), ("Sampling resolution 24 bits to 16 bits", 1), ("Recording length 20 minutes to 40 minutes", 2), ("Sampling resolution 8 bits to 16 bits", 0), ("Sampling rate 44.1 kHz to 22.05 kHz", 1), ("Saving the same recording to a different folder", 2)],
  "Rate and resolution change accuracy. The length of the recording only changes the size.") + ORDER(
  "Put the steps for storing sound in order.",
  ["Measure the amplitude of the analogue wave at regular intervals", "Round each measurement to the nearest value that can be stored", "Convert each value to a binary number", "Store the binary numbers in sequence", "Repeat at the sampling rate, for the length of the recording"],
  "Measure, round, convert, store in sequence, repeat.") + MATCH([
  ["Analogue", "Continuous data, such as a sound wave"], ["Sampling rate", "The number of samples taken per second"], ["Sampling resolution", "The number of bits used to store each sample"], ["Quantisation error", "The difference between the true amplitude and the stored value"], ["Sample", "One measurement of the amplitude of the wave"]]) + CALC([
  {"q": "A recording has a sampling rate of 8 kHz. How many samples are taken in 3 seconds?", "a": 24000, "unit": "samples", "tol": 0.01, "hint": "8000 × 3.", "sol": "<b>24 000</b> samples."},
  {"q": "How many different amplitudes can a sampling resolution of 8 bits store?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "A sound is recorded at 20 kHz, 16 bits, for 10 seconds. How many bytes?", "a": 400000, "unit": "bytes", "tol": 0.01, "hint": "20 000 × 16 × 10 ÷ 8.", "sol": "<b>400 000</b> bytes."},
  {"q": "A sound is recorded at 44.1 kHz, 16 bits, for 1 minute. How many megabytes (1 MB = 1 000 000 bytes), to 2 decimal places?", "a": 5.29, "unit": "MB", "tol": 0.02, "hint": "44 100 × 16 × 60 ÷ 8 ÷ 1 000 000.", "sol": "<b>5.29</b> MB."},
  {"q": "A voice message is recorded at 10 kHz, 8 bits, for 2 minutes. How many kilobytes (1 kB = 1000 bytes)?", "a": 1200, "unit": "kB", "tol": 0.01, "hint": "10 000 × 8 × 120 ÷ 8 ÷ 1000.", "sol": "<b>1200</b> kB."},
  {"q": "The sampling resolution is changed from 8 bits to 16 bits. By what factor does the file size change?", "a": 2, "unit": "×", "tol": 0.01, "hint": "16 ÷ 8.", "sol": "<b>2</b> times larger."},
  {"q": "The sampling rate is halved and the sampling resolution is doubled. By what factor does the file size change?", "a": 1, "unit": "×", "tol": 0.01, "hint": "0.5 × 2.", "sol": "<b>1</b>: no change in size."},
  {"q": "A sampling resolution of 3 bytes is how many bits?", "a": 24, "unit": "bits", "tol": 0.01, "hint": "3 × 8.", "sol": "<b>24</b> bits."}]) + MCQ([
  ("What does the sampling rate measure?", ["The number of bits for each sample", "The number of samples taken per second", "The loudness of the sound", "The length of the recording"], 1, "Sampling rate is samples per second."),
  ("What does the sampling resolution measure?", ["Samples per second", "Bits used to store each sample", "The pitch of the sound", "The size of the speaker"], 1, "Sampling resolution is bits per sample."),
  ("Increasing the sampling rate has which effect?", ["Digital wave is closer to the analogue wave and the file is larger", "The file is smaller and less accurate", "The sound is louder", "No effect on the file size"], 0, "More samples per second means a closer copy and more data."),
  ("Which change does NOT affect how accurate the recording is?", ["Raising the sampling rate", "Raising the sampling resolution", "Making the recording longer", "Lowering the sampling resolution"], 2, "The length only affects the file size."),
  ("What is a quantisation error?", ["A mistake in the file header", "The difference between the true amplitude and the stored value", "A gap in the recording", "A loss of the network connection"], 1, "It comes from rounding each sample to a stored value."),
  ("What type of data is the sound wave before it is recorded?", ["Digital", "Binary", "Analogue", "Discrete"], 2, "The wave is continuous, which is analogue.")], "qz1") + CARDS([
  ("Analogue", "Continuous data. The sound wave."), ("Digital", "Discrete data stored in binary."), ("Sampling", "Measuring the amplitude at regular intervals."), ("Sampling rate", "Samples per second. Hz or kHz."),
  ("Sampling resolution", "Bits per sample. n bits = 2^n amplitudes."), ("Quantisation error", "Gap between true amplitude and stored value."), ("Higher rate or resolution", "More accurate, larger file."), ("File size", "Rate × resolution × seconds, ÷ 8 for bytes.")])

build("ac122", "ac-1-2-2-sound-sampling", "Sound: Sampling Rate and Sampling Resolution", EYA("1.2.2"),
  "How an analogue sound wave is sampled and stored in binary, what changing the sampling rate and resolution does to accuracy and file size, sound file calculations, and nine questions from the 2021 to 2026 papers.",
  dict(sub=CBK("Chapter 1 · Information representation, section 1.2 Multimedia (sound)"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
