"""A Level CS syllabus 1.3: compression (lossy, lossless, RLE). Run: python3 tools/artifact-kit/mk_ac13.py"""
from ak import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Compression</b> makes a file smaller so that it takes up less storage space and can be transmitted in less time using less bandwidth. <b>Lossless</b> compression keeps all the data, so the original can be rebuilt exactly; <b>lossy</b> compression permanently removes data that is judged unimportant, which gives a much smaller file but cannot be undone. <b>Run-length encoding (RLE)</b> is the lossless method the syllabus names: a run of identical values is replaced by one copy of the value and a count. Text must be compressed losslessly, whereas photographs, music and streamed video can usually be compressed lossily because the loss is hard to notice. A good answer says what is removed or replaced, what the effect on the file is, and why that suits the situation.</p></div>

  <h2>1 · Why compress files?</h2>
  <ul>
    <li><b>Less storage:</b> the file takes up less space on a drive or server, so more files can be kept.</li>
    <li><b>Faster transmission:</b> fewer bits to send, so the file is transmitted or downloaded in less time.</li>
    <li><b>Less bandwidth:</b> it uses less of the connection, which matters for people with a slow or limited connection.</li>
    <li><b>Fits a limit:</b> an email attachment or upload may have a maximum file size.</li>
    <li><b>Less buffering:</b> a streamed video or a real-time call keeps up with the connection.</li>
  </ul>
  <p>Examples: photographs compressed before they are uploaded to a website; a sound file compressed before it is emailed; a text file compressed by an operating system utility; a video compressed before real-time streaming.</p>
  <div class="tip"><b class="h">Exam tip</b>Read the last words of the question. A benefit "for storing" the file is less space; a benefit "for transmitting" it is less time or bandwidth. Both are true of compression, but only one answers the question asked.</div>

  <h2>2 · Lossless and lossy compression</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Lossless</th><th>Lossy</th></tr>
    <tr><td>What happens to the data</td><td>None is lost. The file is stored more efficiently.</td><td>Some data is permanently removed.</td></tr>
    <tr><td>The original</td><td>Can be rebuilt exactly after decompression.</td><td>Cannot be rebuilt; only an approximation remains.</td></tr>
    <tr><td>Size reduction</td><td>Smaller, but not by as much.</td><td>Much smaller.</td></tr>
    <tr><td>Quality</td><td>No loss in quality.</td><td>Some loss, often hard to notice.</td></tr>
    <tr><td>Use when</td><td>Every bit matters: text, program code, spreadsheets, legal or medical records, files that will be edited again.</td><td>The loss will not be noticed or does not matter: photographs on a web page, streamed music and video, a quick preview.</td></tr>
    <tr><td>Examples of methods</td><td>Run-length encoding; replacing repeated patterns with shorter codes</td><td>Reducing the colour depth or resolution of an image; reducing the sampling rate or resolution of sound; removing sounds humans cannot hear</td></tr>
  </table></div>

  <h2>3 · Run-length encoding (RLE)</h2>
  <p>RLE finds <b>runs</b>: consecutive identical values. Each run is replaced with <b>one copy of the value and the number of times it repeats</b>.</p>
  <div class="tw"><table class="t mono">
    <tr><th>Original</th><th>RLE</th><th>Saved?</th></tr>
    <tr><td>AAAABBBCC</td><td>4A3B2C</td><td>9 symbols to 6</td></tr>
    <tr><td>BBBBBBBBBB (ten blue pixels)</td><td>10B</td><td>10 values to 2</td></tr>
    <tr><td>EA F1 F1 F2 F2 F2 EA</td><td>1EA 2F1 3F2 1EA</td><td>7 values to 4 pairs</td></tr>
    <tr><td>RGB (all different)</td><td>1R1G1B</td><td>3 symbols to 6: bigger</td></tr>
  </table></div>
  <ul>
    <li><b>Lossless:</b> decoding repeats each value its count, so the original is rebuilt exactly.</li>
    <li><b>Works best</b> with long runs: a logo, a diagram, a screenshot, a scanned page with large white areas, text with repeated characters.</li>
    <li><b>May not shrink the file</b> when there are few runs, as in a photograph where neighbouring pixels differ slightly. Each value then needs a count of 1 stored beside it, which adds data. The mark scheme example is red, green, blue becoming red 1, green 1, blue 1.</li>
    <li><b>Bitmap:</b> done row by row, or across the whole sequence of pixel codes. The first row of ten blue pixels is stored as blue and 10.</li>
    <li><b>Sound:</b> consecutive samples with the same value can be run-length encoded. Silence is a long run.</li>
  </ul>

  <h2>4 · Compressing each type of file</h2>
  <div class="tw"><table class="t">
    <tr><th>File</th><th>Method</th><th>How it reduces the size</th></tr>
    <tr><td><b>Text</b></td><td>Lossless (RLE, or replacing repeated sequences with shorter codes)</td><td>Repeated characters or words are replaced with one copy and a count, or a shorter code. Lossy is not suitable because any lost character corrupts the text.</td></tr>
    <tr><td><b>Bitmap image</b></td><td>Lossless: RLE. Lossy: reduce the colour depth, the number of colours (palette) or the image resolution</td><td>Runs of the same colour become a colour and a count; or fewer bits per pixel or fewer pixels are stored.</td></tr>
    <tr><td><b>Vector graphic</b></td><td>Lossless</td><td>The drawing list is already compact. There is little repeated data, so vector files compress poorly.</td></tr>
    <tr><td><b>Sound</b></td><td>Lossless: RLE, or recording the change from one amplitude to the next instead of each full value. Lossy: lower the sampling rate or resolution, reduce the range of amplitudes, or remove sounds people cannot hear</td><td>Fewer bits per sample, fewer samples, or smaller values to store.</td></tr>
  </table></div>

  <h2>5 · Choosing a method</h2>
  <div class="tw"><table class="t">
    <tr><th>Situation</th><th>Better choice</th><th>Reason that earns marks</th></tr>
    <tr><td>A company report written in a word processor</td><td>Lossless</td><td>All the data is needed; lossy would remove characters and could change the meaning.</td></tr>
    <tr><td>Photographs downloaded by customers from a website</td><td>Lossy</td><td>Much smaller files, so downloads take less time and use less bandwidth; the loss in detail will not be noticed on a screen.</td></tr>
    <tr><td>A live video concert streamed to subscribers</td><td>Lossy</td><td>Smaller file means less bandwidth and less buffering; viewers on small screens will not notice the lost detail. (Lossless is accepted if justified: viewers who want no loss of quality.)</td></tr>
    <tr><td>A scanned legal contract</td><td>Lossless</td><td>No data can be lost; text must stay readable and the document must be exact.</td></tr>
    <tr><td>A voice message to email</td><td>Lossy or lossless</td><td>Lossy gives the smallest file; lossless keeps the exact recording. Justify the one you pick.</td></tr>
  </table></div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Saying "lossy loses quality" without saying <b>data is permanently removed</b> and cannot be restored.</li>
    <li>Saying "lossless makes the file the same size". It still reduces the size, by encoding the data more efficiently.</li>
    <li>Writing that RLE "compresses repeated images". It compresses runs of identical consecutive values.</li>
    <li>Giving a benefit that is not for the situation, such as faster transmission in a question about storing.</li>
    <li>Suggesting lossy compression for a text file without noting that it would corrupt the text.</li>
  </ul>
'''

watch = '''
  <h2>1 · Run-length encoding a row of pixels</h2>
  <p>Press Play, or click the numbered steps. Each run of the same colour becomes a count and a colour.</p>
  <div id="stA"></div>
  <h2>2 · When RLE works and when it does not</h2>
  <div id="stB"></div>
  <h2>3 · Lossless against lossy</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Run-length encode your own text</h2>
  <p>Type up to 30 characters. The lab finds the runs and shows the encoded version. Try AAAABBBCC, then try ABCDEFG.</p>
  <div class="card"><input id="rx" type="text" maxlength="30" value="AAAAAAABBBCCCCCCCCDD" style="width:100%;font:600 1.1rem var(--mono);padding:8px 10px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink)" aria-label="Text to compress">
    <div id="rxT" style="margin-top:12px"></div>
    <div class="readout"><div><small>Original</small><strong id="r1"></strong></div><div><small>RLE code</small><strong id="r2"></strong></div><div><small>Stored items</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>

  <h2>Lab 2 · How much does RLE save on an image?</h2>
  <p>Choose a picture. Each row is run-length encoded. Each run needs two items (a count and a colour), so RLE only saves space when there are long runs.</p>
  <div class="card"><div class="grid2"><div><div id="gB" class="btnrow"></div>
    <div class="readout"><div><small>Pixels</small><strong id="g1"></strong></div><div><small>Runs</small><strong id="g2"></strong></div><div><small>Items after RLE</small><strong id="g3"></strong></div><div><small>Change in size</small><strong id="g4"></strong></div></div>
    <div class="verdict" id="gv"></div></div>
    <div><svg id="gS" viewBox="0 0 352 176" role="img" aria-label="A sixteen by eight pixel image"></svg></div></div></div>

  <h2>Lab 3 · Why compress? Download time</h2>
  <p>Choose a file size and how much it is compressed. The download time shows the benefit for transmission.</p>
  <div class="card"><div id="dz"></div><div id="dc"></div><div id="dB" class="btnrow"></div>
    <div class="readout"><div><small>Compressed size</small><strong id="d1"></strong></div><div><small>Time before</small><strong id="d2"></strong></div><div><small>Time after</small><strong id="d3"></strong></div><div><small>Space saved</small><strong id="d4"></strong></div></div>
    <div class="verdict" id="dv"></div></div>

  <h2>Lab 4 · Lossy or lossless?</h2>
  <p>Choose a situation. The table gives the better choice and the reasons that earn marks.</p>
  <div class="card"><div id="lB" class="btnrow"></div><div id="lO"></div></div>
'''

practise = '''
  <h2>1 · Lossy or lossless?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which method suits each situation?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for run-length encoding in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Photos on a website", "A photograph from a phone can be several megabytes. Websites usually store a lossy version a tenth of that size. Pages load faster, and few visitors notice the difference on a screen.", "lossy for web photographs: smaller file, faster download, loss of detail not noticed.") +
rw("Streaming video", "Services send compressed video so that it keeps up with the viewer's connection. If the connection is slow the quality is reduced further. Without lossy compression, most connections could not carry a live video call.", "real-time streaming: lossy reduces bandwidth and buffering.") +
rw("Zip files", "A zip file combines files and compresses them losslessly. The files that come out are identical to the ones that went in, which is why zip is used for documents, spreadsheets and programs.", "lossless for text and program files: nothing may be lost.") +
rw("Screenshots and logos", "An image with big areas of one colour, such as a logo or a screenshot of a web page, has long runs of identical pixels. Run-length encoding shrinks it a lot without changing a pixel.", "RLE works on images with long runs of identical colours.") +
rw("Why a photograph barely shrinks with RLE", "Neighbouring pixels in a photograph are almost never identical, so each run has length 1 or 2. RLE then adds a count for almost every pixel and the file can be bigger. Photographs are compressed with lossy methods instead.", "RLE may not reduce a bitmap's size when there are few runs; the counts add data.")
)

items = [("s21_11", "1(b)", 3), ("w21_11", "7(b)", 4), ("w21_12", "5(b)(ii)", 4), ("s22_13", "1(a)(iii)-(iv)", 4), ("w22_11", "7(c)", 3), ("w22_12", "8(c)", 4), ("s23_11", "1(c)", 6),
         ("w23_12", "6(a)", 3), ("s25_11", "2(b)", 7), ("s26_12", "1(d)(ii)", 3), ("s26_13", "3(c)(i)", 4)]

exam = aexam("compression",
  "Eleven questions from the 2021 to 2026 Paper 1 papers: why files are compressed, lossy against lossless with a justified choice, and how RLE and other methods work for text, bitmaps and sound. The scenarios and values are changed from the originals.",
  items, [
  ceq(AP("s21_11", "1(b)"), "[3]", "A scanned bitmap image is compressed using lossless compression. Identify one method of lossless compression that can be used on the image and describe how the method will reduce the file size.",
      ["Run-length encoding (RLE).", "Sequences of pixels of the same colour are replaced.", "Each is replaced with the colour code and the number of identical pixels."],
      "<p>Name the method, then say what is replaced and by what.</p>",
      [[("k", "Run-length encoding. Each sequence of consecutive pixels of the same colour is replaced by one copy of the colour code and the number of identical pixels, so fewer values are stored.")]]) +
  ceq(AP("w21_11", "7(b)"), "[4]", "A sound file is compressed before it is emailed. (i) Explain the reasons why the sound file is compressed. (ii) The compression is lossless. Describe how lossless compression can compress the sound file.",
      ["(i) Reduces the file size; faster to transmit or download; the original may be too large for the email attachment limit (two).", "(ii) Run-length encoding: where consecutive samples are the same, store the value and the number of repeats; or store the changes between samples instead of the actual values; or reduce amplitudes to the range actually used (two)."],
      "<p>(i) benefits for sending. (ii) one method with its working described.</p>",
      [[("k", "(i) Compressing reduces the file size, so it is faster to send and may fit under the attachment size limit. "), ("a", "(ii) Run-length encoding can be used: where several consecutive samples have the same value, the value is stored once with the number of times it repeats. Alternatively the change from each sample to the next is stored instead of the full value, which needs fewer bits.")]]) +
  ceq(AP("w21_12", "5(b)(ii)"), "[4]", "A photograph is compressed before it is emailed. Describe two lossy methods that can be used to compress the image.",
      ["Each method is one mark for the method and one for how it reduces the size.", "Reduce the colour depth, so each pixel needs fewer bits.", "Reduce the number of colours (the palette), so fewer bits are needed for each colour.", "Reduce the image resolution, so fewer pixels are stored."],
      "<p>Two methods with two marks each: name it, then say why the file is smaller.</p>",
      [[("k", "Method 1: reduce the colour depth. Each pixel is stored with fewer bits, so the file is smaller. Method 2: reduce the image resolution. There are fewer pixels per unit of the picture, so less binary has to be stored.")]]) +
  ceq(AP("s22_13", "1(a)(iii)-(iv)"), "[4]", "(i) Describe how lossless compression can be used to reduce the file size of a text file. (ii) Explain why lossy compression should not be used on a text file.",
      ["(i) Run-length encoding; groups of repeated characters are identified; each is replaced with one copy of the character and the number of times it occurs (two).", "(ii) None of the original data can be lost; the text file would be corrupted or could not be opened (two)."],
      "<p>(i) name the method and what it replaces. (ii) say what is lost, then the consequence.</p>",
      [[("k", "(i) Run-length encoding finds groups of repeated characters and replaces each with one copy of the character and the number of times it occurs. "), ("a", "(ii) Lossy compression permanently removes data, but all the characters in a text file are needed, so the file would be corrupted and the meaning could be lost.")]]) +
  ceq(AP("w22_11", "7(c)"), "[3]", "An operating system includes a utility program to compress text files. Describe one appropriate method of compressing a text file.",
      ["Lossless compression.", "Run-length encoding.", "Repeated sequences of characters are replaced by a single copy of the character and a counter of how many times it repeats."],
      "<p>Three marks: type, method, how it works.</p>",
      [[("k", "Lossless compression using run-length encoding. Each sequence of repeated characters is replaced by one copy of the character and a counter showing how many times it occurs.")]]) +
  ceq(AP("w22_12", "8(c)"), "[4]", "(i) A bitmap image uses 8 bits per pixel and is compressed with RLE. Each colour is a hexadecimal value. Complete the table. AB AB AB 4C 4C 1F 1F 1F 1F is compressed to ...; the compressed code 2D5 1E0 3C2 is uncompressed to .... (ii) Explain why lossless compression is more appropriate than lossy compression for a text file.",
      ["3AB 24C 41F (each run as a count and a value).", "D5 D5 E0 C2 C2 C2.", "(ii) All the data is required, none can be lost; otherwise the text file would be corrupted or not make sense."],
      "<p>Read each compressed item as count then value: 3 × AB, 2 × 4C, 4 × 1F. Decompress by repeating each value.</p>",
      [[("k", "(i) 3AB 24C 41F, and D5 D5 E0 C2 C2 C2. (ii) Every character in a text file is needed, so no data can be lost; lossy compression would corrupt the file and it may not make sense.")]]) +
  ceq(AP("s23_11", "1(c)"), "[6]", "Photographs are compressed before they are uploaded to a web server, and customers download them. (i) Explain the reasons why compressing the photographs will benefit the customers. (ii) An image can be compressed using run-length encoding. Explain the reasons why RLE may not reduce the file size of a bitmap image. Give one example.",
      ["(i) The photographs download in less time; they use less of the customer's bandwidth; they take up less space on the customer's device, so more can be stored (three).", "(ii) RLE stores a colour and the number of times it occurs in a row; an image may not have many sequences of the same colour; it would store each colour with a count of 1, adding data; example: red, green, blue becomes red 1, green 1, blue 1."],
      "<p>(i) three separate benefits for the customer. (ii) the reason, the consequence, and the example.</p>",
      [[("k", "(i) The customer can download the photographs in less time and uses less bandwidth. The files also take less space on the customer's device, so more can be stored. "), ("a", "(ii) RLE stores each colour with the number of times it occurs consecutively. If there are few runs of the same colour, each colour is stored with a count of 1, which adds data. For example red, green, blue becomes red 1, green 1, blue 1, which is larger.")]]) +
  ceq(AP("w23_12", "6(a)"), "[3]", "A real-time video of a music concert is streamed to subscribers. Tick lossy or lossless as the most appropriate type of compression and justify your answer.",
      ["No mark for the tick. Three marks for matching justification.", "Lossy: loss of quality will not be noticed; less bandwidth because the file is smaller; less buffering so the video plays smoothly; viewers on different devices may not need high resolution.", "Lossless: original may not have been recorded in high quality; viewers want no loss of quality; the reduction is enough for the receiving device."],
      "<p>Choose one and give three reasons that all support it.</p>",
      [[("k", "Lossy. "), ("a", "The video must be viewed in real time, and a lossy file is smaller so it needs less bandwidth. A smaller file also reduces buffering, so the concert plays smoothly, and the viewers will not notice the loss of fine detail.")]]) +
  ceq(AP("s25_11", "2(b)"), "[7]", "A video conference is compressed before it is transmitted as a real-time bit stream. (i) Explain the reasons why the video is compressed. (ii) Identify whether lossy or lossless compression is more appropriate, and justify your answer.",
      ["(i) Video is data-intensive; the file size needs reducing to reduce bandwidth use and buffering; so people are not behind in the conversation and people with lower bandwidth can still take part (four).", "(ii) Lossy (no mark for the choice). Reduces the file size more than lossless; significantly less bandwidth; less buffering; data that cannot be seen can be removed, for example reducing the resolution or the sample rate (three)."],
      "<p>(i) four marks: size, bandwidth, buffering, effect on the conversation. (ii) lossy, and the reason it goes further than lossless.</p>",
      [[("k", "(i) A video is a large amount of data, so compression reduces the file size and the bandwidth needed. This reduces buffering, so people are not behind in the conversation, and people with slower connections can still take part. "), ("a", "(ii) Lossy. It reduces the file size more than lossless, so even less bandwidth is needed and buffering is reduced further. Detail that viewers will not notice, such as some of the resolution, can be removed.")]]) +
  ceq(AP("s26_12", "1(d)(ii)"), "[3]", "A bitmap image has rows such as R R W W W W (R is red and W is white). Explain how the image can be compressed using lossless compression.",
      ["Run-length encoding can be used.", "A sequence of consecutive pixels of the same colour is stored as one copy of the colour and the number of consecutive occurrences.", "A reference to the image: for example the row R R W W W W is stored as R2 W4."],
      "<p>Name the method, say what is stored, then use the example from the picture. Do not call pixels bits or characters.</p>",
      [[("k", "Run-length encoding can be used. A run of consecutive pixels of the same colour is stored as a single copy of the colour and the number of times it occurs. "), ("a", "For example, the first row R R W W W W is stored as R2 W4.")]]) +
  ceq(AP("s26_13", "3(c)(i)"), "[4]", "An animation's images and sound are compressed independently using lossless compression. Explain the different ways that lossless compression can be used for the images and for the sound file.",
      ["Images (max two): run-length encoding; store each colour and the number of times it appears consecutively.", "Sound (max two): reduce the amplitude range to the values actually used, which reduces the sampling resolution without affecting the sound; or record the changes in amplitude instead of each amplitude, since each change needs fewer bits; RLE is accepted for sound but not for both parts."],
      "<p>Two different methods, one for each file type. Do not use RLE for both.</p>",
      [[("k", "Images: run-length encoding stores each colour with the number of times it appears in a row. "), ("a", "Sound: instead of storing every full amplitude, the change from one amplitude to the next is stored, and each change needs fewer bits than a whole new amplitude.")]])
])

tips = tips_html([
  ("Say what is removed.", "Lossy permanently removes data and the original cannot be rebuilt. Lossless keeps all the data."),
  ("Match the benefit to the question.", "Storage means less space. Transmission means less time and bandwidth."),
  ("Describe RLE fully.", "A run of identical values becomes one copy of the value and a count."),
  ("Use the example you are given.", "If the question shows a row of pixels, write its RLE code."),
  ("Justify one side.", "Pick lossy or lossless and keep every reason on that side."),
  ("RLE can make a file bigger.", "When there are few runs, each value is stored with a count of 1."),
], [
  ("how RLE works", "A sequence of identical values is replaced by one copy of the value and the number of times it repeats."),
  ("why lossless for text", "All the data is needed, so lossy compression would corrupt the text and it might not make sense."),
  ("why lossy for streaming", "The file is smaller, so less bandwidth is needed and there is less buffering, and the loss of detail will not be noticed."),
  ("why RLE may not work", "There may be few runs of the same value, so each value is stored with a count of 1, which adds data."),
], [("State / Give", "Short facts or an example."), ("Identify", "Name the method or type."), ("Describe", "Say what is replaced or removed and by what."), ("Explain", "Reasons and effects: why it helps or why it fails."), ("Justify", "A reason that matches the choice you made.")]) + FC

js = AKJS + r'''
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
''' + CLASSIFY("cl1", "Is each method lossless or lossy?", ["Lossless", "Lossy"],
  [("Run-length encoding", 0), ("Reduce the colour depth of an image", 1), ("Reduce the sampling rate of a sound", 1), ("Store the change between samples instead of each sample", 0), ("Reduce the image resolution", 1), ("Remove sounds humans cannot hear", 1), ("Replace repeated characters with a character and a count", 0), ("Reduce the number of colours in the palette", 1)],
  "Lossless methods keep every value. Lossy methods reduce the detail that is stored.") + CLASSIFY("cl2", "Which type of compression suits each file?", ["Lossless", "Lossy"],
  [("A text report", 0), ("A streamed live concert", 1), ("A program file", 0), ("A photograph on a news website", 1), ("A spreadsheet of accounts", 0), ("Music on a phone with little storage", 1)],
  "Lossless where every bit matters; lossy where the loss will not be noticed.") + ORDER(
  "Put the steps for run-length encoding AAAABBC in order.",
  ["Start at the first character", "Count how many identical characters follow in a row", "Write the count then one copy of the character", "Move to the next different character and repeat", "Finish with the code 4A2B1C"],
  "Count each run, write count and character, repeat.") + MATCH([
  ["Lossy", "Data is permanently removed to make the file smaller"], ["Lossless", "No data is lost; the original can be rebuilt exactly"], ["Run-length encoding", "A run of identical values becomes one copy and a count"], ["Run", "Identical values next to each other"], ["Compression", "Reducing the size of a file"]]) + CALC([
  {"q": "Run-length encode AAAAABBBCCCC. Type the code with no spaces.", "t": ["5A3B4C"], "unit": "", "hint": "Count each run.", "sol": "<b>5A3B4C</b>."},
  {"q": "Decode 3X2Y4Z. How many characters are in the original?", "a": 9, "unit": "", "tol": 0.01, "hint": "3 + 2 + 4.", "sol": "<b>9</b>: XXXYYZZZZ."},
  {"q": "A row of 40 white pixels is stored as 40W. How many values were stored instead of the 40?", "a": 2, "unit": "", "tol": 0.01, "hint": "One count and one colour.", "sol": "<b>2</b>."},
  {"q": "A file is 24 MB and is compressed to 6 MB. What fraction of the original is it (as a decimal)?", "a": 0.25, "unit": "", "tol": 0.01, "hint": "6 ÷ 24.", "sol": "<b>0.25</b>."},
  {"q": "A 50 MB file is compressed by 80%. What is the compressed size in MB?", "a": 10, "unit": "MB", "tol": 0.01, "hint": "20% remains: 50 × 0.2.", "sol": "<b>10</b> MB."},
  {"q": "A 40 MB file is downloaded at 8 Mbit/s. How many seconds does it take?", "a": 40, "unit": "s", "tol": 0.01, "hint": "40 × 8 = 320 megabits ÷ 8.", "sol": "<b>40</b> seconds."},
  {"q": "The same file is compressed to 10 MB. How many seconds does it take at 8 Mbit/s?", "a": 10, "unit": "s", "tol": 0.01, "hint": "10 × 8 ÷ 8.", "sol": "<b>10</b> seconds."},
  {"q": "RGB (three different pixels) is run-length encoded as a count and a colour for each. How many values are stored?", "a": 6, "unit": "", "tol": 0.01, "hint": "Three runs × 2.", "sol": "<b>6</b>, which is more than the 3 original values."}]) + MCQ([
  ("What is lossless compression?", ["Data is permanently removed", "No data is lost and the original can be rebuilt exactly", "The file always stays the same size", "Only sound can be compressed this way"], 1, "Lossless means the original can be rebuilt exactly."),
  ("Why is lossy compression not suitable for a text file?", ["It makes the file bigger", "Removed data cannot be recovered, so the text would be corrupted", "It only works on images", "It is slower than lossless"], 1, "Every character is needed, and lossy removes data permanently."),
  ("What does run-length encoding store?", ["The number of colours in the file", "One copy of a repeated value and the number of times it repeats", "The difference between two files", "The first pixel only"], 1, "RLE replaces a run with a value and a count."),
  ("Why might RLE not reduce the size of a photograph?", ["Photographs have few runs of identical pixels, so counts add data", "Photographs are vector graphics", "RLE is lossy", "RLE needs a longer header"], 0, "With short runs, each pixel is stored with a count."),
  ("Which is a benefit of compressing a file for transmission?", ["It uses more bandwidth", "It is transmitted in less time", "It becomes a vector graphic", "It needs a higher sampling rate"], 1, "A smaller file is transmitted in less time."),
  ("Which method is lossy?", ["Run-length encoding", "Reducing the colour depth of an image", "Storing the change between sound samples", "Replacing repeated characters with a count"], 1, "Reducing the colour depth discards colour detail.")], "qz1") + CARDS([
  ("Compression", "Reducing the size of a file."), ("Lossless", "No data lost. Original rebuilt exactly. Text, code."), ("Lossy", "Data permanently removed. Much smaller. Photos, video, music."), ("Run-length encoding", "Replace a run with one copy and a count."),
  ("RLE weakness", "Few runs: counts add data, file can grow."), ("Lossy image methods", "Reduce colour depth, colours or resolution."), ("Lossy sound methods", "Reduce sampling rate or resolution."), ("Benefit of compression", "Less storage, less transmission time, less bandwidth.")])

build("ac13", "ac-1-3-compression", "Compression: Lossy, Lossless and Run-Length Encoding", EYA("1.3"),
  "Why files are compressed, lossy against lossless with a justified choice, run-length encoding step by step, how text, images and sound are compressed, and eleven questions from the 2021 to 2026 papers.",
  dict(sub=CBK("Chapter 1 · Information representation, section 1.3 Compression"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
