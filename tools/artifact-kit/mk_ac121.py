"""A Level CS syllabus 1.2.1: graphics, bitmap and vector. Run: python3 tools/artifact-kit/mk_ac121.py"""
from ak import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>bitmap</b> image is a grid of <b>pixels</b>, each with one colour stored as a binary code, and the codes are stored in sequence along with a <b>file header</b> that says how to read them. The <b>image resolution</b> (pixels wide × pixels high) and the <b>colour depth</b> (bits per pixel) decide both the quality and the file size, which you estimate as <b>width × height × bit depth</b>. A <b>vector graphic</b> stores a <b>drawing list</b> of <b>drawing objects</b>, each with <b>properties</b> such as fill colour and line weight, so it can be enlarged without pixelation and often has a small file. Bitmaps suit photographs and fine detail, vectors suit logos, diagrams and anything that must be resized. Marks in this topic come from the terms, from file size calculations with the working shown, and from a justified choice between bitmap and vector.</p></div>

  <h2>1 · How a bitmap image is encoded</h2>
  <ol>
    <li>The image is divided into a grid of <b>pixels</b>, the smallest element of an image that can be one colour.</li>
    <li>Each pixel has <b>one colour</b>.</li>
    <li>Each colour has a <b>unique binary code</b>. The number of bits for each code is the colour depth.</li>
    <li>The code for each pixel is stored <b>in sequence</b>, usually row by row from the top left.</li>
    <li>A <b>file header</b> is stored with the data so the computer knows how to read it.</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Pixel</b></td><td>The smallest element of a bitmap image; one square of one colour.</td></tr>
    <tr><td><b>Image resolution</b></td><td>The number of pixels wide × the number of pixels high that make up the image, for example 1024 × 512.</td></tr>
    <tr><td><b>Screen resolution</b></td><td>The number of pixels wide × high that a screen can display (sometimes quoted as dots per inch). The image resolution can be changed; the screen has a physical limit.</td></tr>
    <tr><td><b>Colour depth / bit depth</b></td><td>The number of bits used to represent the colour of each pixel.</td></tr>
    <tr><td><b>File header</b></td><td>Data about the image file stored with the pixel data, such as the file type, image resolution, colour depth, file size, compression type and where the pixel data starts.</td></tr>
  </table></div>

  <h2>2 · Colour depth and the number of colours</h2>
  <p>With <i>n</i> bits per pixel there are 2<sup><i>n</i></sup> different codes, so 2<sup><i>n</i></sup> colours.</p>
  <div class="tw"><table class="t mono">
    <tr><th>Bits per pixel</th><td>1</td><td>2</td><td>4</td><td>8</td><td>16</td><td>24</td></tr>
    <tr><th>Colours</th><td>2</td><td>4</td><td>16</td><td>256</td><td>65 536</td><td>16 777 216</td></tr>
  </table></div>
  <p>To find the <b>smallest bit depth</b> for an image with a given number of colours, find the smallest <i>n</i> where 2<sup><i>n</i></sup> is at least that number. An image that uses 3 colours needs 2 bits; one that uses 256 colours needs 8 bits; one that uses 5 colours needs 3 bits.</p>

  <h2>3 · Estimating the file size</h2>
  <div class="formula">file size (bits) = image width × image height × colour depth</div>
  <ol>
    <li>Multiply the width by the height to get the number of pixels.</li>
    <li>Multiply by the bits per pixel.</li>
    <li>Divide by 8 for bytes, by 1024 for kibibytes, by 1024 again for mebibytes. If the question asks for MB or kB, use 1000.</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>Working</th><th>Answer</th></tr>
    <tr><td>1024 × 512, 8 bits, in mebibytes</td><td>1024 × 512 × 8 ÷ 8 ÷ 1024 ÷ 1024</td><td>0.5 MiB</td></tr>
    <tr><td>2048 × 1024, 10 bits, in mebibytes</td><td>2048 × 1024 × 10 ÷ 8 ÷ 1024 ÷ 1024</td><td>2.5 MiB</td></tr>
    <tr><td>2 million pixels, 16 bits, in megabytes</td><td>2 000 000 × 16 ÷ 8 ÷ 1 000 000</td><td>4 MB</td></tr>
    <tr><td>10 × 5 section, 256 colours</td><td>256 colours = 8 bits; 10 × 5 × 8 ÷ 8</td><td>50 bytes</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>Read the unit of the bit depth: "8 bytes per pixel" means no division by 8 for that part. Read the unit of the answer: mebibytes use 1024, megabytes use 1000. The file header is not included in an "estimate".</div>

  <h2>4 · Changing an image: quality and file size</h2>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Effect on the image</th><th>Effect on the file</th></tr>
    <tr><td><b>Increase image resolution</b></td><td>More pixels, so more detail and a sharper image, especially when enlarged</td><td>More pixels to store, so the file is larger</td></tr>
    <tr><td><b>Decrease image resolution</b></td><td>Fewer pixels, so less detail; the image looks blocky when enlarged</td><td>Smaller file</td></tr>
    <tr><td><b>Increase colour depth</b></td><td>More colours available, so smoother shading and more accurate colours</td><td>More bits per pixel, so a larger file</td></tr>
    <tr><td><b>Decrease colour depth</b></td><td>Fewer colours, so shades merge and detail is lost</td><td>Fewer bits per pixel, so a smaller file</td></tr>
    <tr><td><b>Change the screen resolution</b></td><td>Changes how the image is displayed, not the image itself</td><td>No change to the file</td></tr>
    <tr><td><b>Change one pixel to a different colour</b></td><td>That pixel changes</td><td>No change if the colour depth is the same</td></tr>
  </table></div>

  <h2>5 · Vector graphics</h2>
  <p>A vector graphic is not stored as pixels. It is stored as a set of instructions.</p>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Drawing object</b></td><td>An individual element of the image</td><td>A line, a rectangle, a circle, a letter</td></tr>
    <tr><td><b>Property</b></td><td>An attribute of one drawing object</td><td>Fill colour, line colour, line weight, position, size</td></tr>
    <tr><td><b>Drawing list</b></td><td>All of the drawing objects in the image, stored with the commands or equations needed to draw each one</td><td>Circle: centre (120, 80), radius 40, fill yellow; line: from (0, 0) to (200, 100)</td></tr>
  </table></div>
  <p>When the image is shown, the computer reads the drawing list and calculates the shapes. Because the shapes are recalculated, a vector graphic can be enlarged without pixelation, and one object can be edited without disturbing the rest.</p>

  <h2>6 · Bitmap or vector?</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Bitmap</th><th>Vector</th></tr>
    <tr><td>Stored as</td><td>A colour code for each pixel</td><td>A drawing list of objects and their properties</td></tr>
    <tr><td>Enlarging</td><td>Pixels get bigger and the image looks blocky</td><td>The shapes are recalculated, so quality is kept</td></tr>
    <tr><td>File size</td><td>Usually larger, because every pixel is stored</td><td>Usually smaller for simple shapes</td></tr>
    <tr><td>Best for</td><td>Photographs, scanned images, fine detail and shading</td><td>Logos, diagrams, plans, icons, text-based art</td></tr>
    <tr><td>Editing</td><td>Edit individual pixels</td><td>Edit each object and its properties</td></tr>
    <tr><td>Compression</td><td>Can be compressed a lot (for example run-length encoding)</td><td>Does not compress well, because there is little repeated data</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>When a question says "justify" the choice itself earns nothing; the marks are for reasons that match the choice. Do not mix reasons from both types in one answer.</div>

  <h2>7 · Common ways to lose marks</h2>
  <ul>
    <li>Saying a pixel is "a dot of colour" without "smallest element" or "one colour".</li>
    <li>Describing a bitmap without the sequence: pixel, colour, binary code, stored in order.</li>
    <li>Forgetting to divide by 8 when the colour depth is in bits, or dividing when it is already in bytes.</li>
    <li>Using 1000 for a mebibyte, or 1024 for a megabyte.</li>
    <li>Saying that increasing screen resolution improves the file. Screen resolution does not change the stored image.</li>
  </ul>
'''

watch = '''
  <h2>1 · How a small bitmap is stored</h2>
  <p>Press Play, or click the numbered steps. Each pixel's colour becomes a binary code, and the codes are stored in order.</p>
  <div id="stA"></div>
  <h2>2 · Working out a file size: 1024 × 512 at 8 bits</h2>
  <div id="stB"></div>
  <h2>3 · A vector drawing list, and what happens when you enlarge it</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · File size calculator</h2>
  <p>Drag the width and height, then choose a colour depth. The working follows the formula width × height × bit depth.</p>
  <div class="card"><div id="fw"></div><div id="fh"></div><div id="fb" class="btnrow"></div>
    <div class="readout"><div><small>Colours</small><strong id="f0"></strong></div><div><small>Bits</small><strong id="f1"></strong></div><div><small>Bytes</small><strong id="f2"></strong></div><div><small>Kibibytes</small><strong id="f3"></strong></div><div><small>Mebibytes</small><strong id="f4"></strong></div></div>
    <div class="verdict" id="fv"></div></div>

  <h2>Lab 2 · Paint the pixels</h2>
  <p>Click a pixel to change its colour code. With 1 bit per pixel you only have two colours; with 2 bits you have four. Watch the stored data and the file size.</p>
  <div class="card"><div class="grid2"><div><svg id="pxS" viewBox="0 0 320 320" role="img" aria-label="An eight by eight pixel grid"></svg></div>
    <div><div id="pxB" class="btnrow"></div><div class="readout"><div><small>Colours available</small><strong id="p1"></strong></div><div><small>File size (8 × 8)</small><strong id="p2"></strong></div></div>
    <pre class="mono" id="p3" style="font-size:.78rem;line-height:1.5;background:var(--soft);padding:8px 10px;border-radius:8px;overflow-x:auto;margin:0"></pre></div></div></div>

  <h2>Lab 3 · Resolution and colour depth against quality</h2>
  <p>The same picture is drawn with a chosen resolution and a chosen number of shades. Fewer pixels make it blocky; fewer shades make it banded; both make the file smaller.</p>
  <div class="card"><div class="grid2"><div><div id="qr"></div><div id="qd"></div>
    <div class="readout"><div><small>Pixels</small><strong id="q1"></strong></div><div><small>Shades</small><strong id="q2"></strong></div><div><small>File size</small><strong id="q3"></strong></div></div>
    <div class="verdict" id="qv"></div></div>
    <div><svg id="qS" viewBox="0 0 320 224" role="img" aria-label="A picture drawn at the chosen resolution and colour depth"></svg></div></div></div>

  <h2>Lab 4 · Bitmap or vector?</h2>
  <p>Choose a task. The table gives the better choice and the reasons that would earn the marks.</p>
  <div class="card"><div id="vB" class="btnrow"></div><div id="vO"></div></div>
'''

practise = '''
  <h2>1 · Bitmap or vector?</h2><div id="cl1" class="card"></div>
  <h2>2 · Larger, smaller or no change to the file?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for a file size calculation in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Why a small photo looks blocky when enlarged", "A photo is a grid of pixels. Zooming in only makes each square bigger, so the edges become stepped. The computer cannot invent detail that was never stored.", "a bitmap enlarged: pixels get bigger, so the image is pixelated.") +
rw("A logo on a card and on a billboard", "A company usually keeps its logo as a vector graphic. The same drawing list is recalculated for a business card or a huge sign, with sharp edges at either size and a small file.", "justify vector: recalculated when resized, no pixelation, small file size.") +
rw("Megapixels", "A phone camera that records 12 megapixels stores about 12 million pixels in each photo. At 24 bits per pixel the raw image would need 36 million bytes, which is why photos are compressed before they are saved.", "image resolution × colour depth gives the uncompressed size; compression reduces it.") +
rw("What is in the header", "A BMP file begins with a header that holds the file type, the width and height, the colour depth, and where the pixel data starts. Without it the stream of pixel codes could not be put back into the right shape.", "file header items: file type, file size, dimensions, compression type, offset to the pixel data.") +
rw("Fonts and maps", "Many fonts and map symbols are stored as vector outlines, so one description works at any size on a phone or a poster. A satellite photo on the same map is a bitmap.", "mixed use: vector for shapes and text that scale, bitmap for photographic detail.")
)

items = [("s21_11", "1(a)", 5), ("s22_12", "1(a)", 3), ("s22_12", "1(b)-(c)", 5), ("s23_11", "1(b)(i)", 2), ("s26_12", "1(b)-(d)(i)", 4), ("w22_12", "8(a)", 2), ("s26_13", "3(b)", 5),
         ("s25_13", "1(a)", 6), ("w21_12", "5(a)", 4), ("s24_12", "2(d)(ii)", 2), ("w21_12", "5(b)(i)", 4), ("w22_12", "8(b)", 2), ("s26_11", "5(c)", 3)]

exam = aexam("bitmap and vector graphics",
  "Thirteen questions from the 2021 to 2026 Paper 1 papers: terms, encoding, file size calculations, the effect of changing resolution and colour depth, and bitmap against vector. The scenarios and figures are changed from the originals, so the answers are our own.",
  items, [
  ceq(AP("s21_11", "1(a)"), "[5]", "A scanned image is a bitmap. (i) Describe the terms pixel and file header. (ii) The image has a resolution of 2048 × 1536 pixels and a colour depth of 16 bits per pixel. Calculate an estimate of the file size in mebibytes. Show your working.",
      ["Pixel: the smallest element of an image, one square of one colour.", "File header: data about the image file, such as the dimensions or colour depth.", "Working: 2048 × 1536 × 16 ÷ 8 ÷ 1024 ÷ 1024.", "Answer: 6 mebibytes."],
      "<p>Two marks for the terms, one for the working, one for the answer. 2048 × 1536 = 3 145 728 pixels; × 2 bytes = 6 291 456 bytes; ÷ 1 048 576 = 6.</p>",
      [[("k", "A pixel is the smallest element of an image and is one square of one colour. A file header stores data about the bitmap, such as its resolution and colour depth. "), ("a", "2048 × 1536 × 16 = 50 331 648 bits ÷ 8 = 6 291 456 bytes ÷ 1024 ÷ 1024 = 6 mebibytes.")]]) +
  ceq(AP("s22_12", "1(a)"), "[3]", "Define each term for a bitmap image: image resolution, bit depth and file header.",
      ["Image resolution: the number of pixels wide by the number of pixels high.", "Bit depth: the number of bits used to represent the colour of each pixel.", "File header: stores data about the image file, such as the file type, the image resolution and the bits per pixel."],
      "<p>One mark each. Use the precise phrases: pixels wide by pixels high; bits per colour or pixel; data about the file.</p>",
      [[("k", "Image resolution is the number of pixels wide by the number of pixels high. Bit depth is the number of bits used to represent the colour of each pixel. A file header stores data about the image file, such as the file type and size.")]]) +
  ceq(AP("s22_12", "1(b)-(c)"), "[5]", "A section of a bitmap image is 12 pixels wide and 6 pixels high. The complete image can have up to 64 colours. (i) Identify the smallest number of bits that can represent each colour. (ii) Calculate an estimate of the file size of the section in bytes. Show your working. (iii) Describe how reducing the colour depth affects the file size.",
      ["6 bits.", "Working 12 × 6 × 6 ÷ 8, answer 54 bytes.", "Reducing the colour depth means fewer bits per pixel, so less data is stored and the file is smaller."],
      "<p>64 = 2<sup>6</sup>. 72 pixels × 6 bits = 432 bits = 54 bytes. The effect needs the cause and the result: fewer bits per pixel, so a smaller file.</p>",
      [[("k", "(i) 6 bits, because 2^6 = 64. (ii) 12 × 6 × 6 = 432 bits ÷ 8 = 54 bytes. (iii) A lower colour depth uses fewer bits per pixel, so less data is stored and the file size decreases.")]]) +
  ceq(AP("s23_11", "1(b)(i)"), "[2]", "Colour depth and image resolution are both included in the file header of a bitmap image. Identify two other items that could be included in the header.",
      ["Any two: the file type or format, the file size, the type of compression used, the location or offset of the pixel data."],
      "<p>Do not give colour depth or resolution, as the question has already given them. Two different items, one mark each.</p>",
      [[("k", "The file type (that it is a bitmap) and the location of the pixel data within the file.")]]) +
  ceq(AP("s26_12", "1(b)-(d)(i)"), "[4]", "(i) Describe the difference between image resolution and screen resolution. (ii) A bitmap image uses the colours red, white, blue, green and yellow. State the smallest bit depth that can be used.",
      ["Image resolution is the number of pixels wide by high that form the image; screen resolution is the number of pixels wide by high that a screen can display.", "If the screen resolution is lower than the image resolution, the displayed quality is worse; the image resolution can be changed but the screen has a physical limit.", "3 bits."],
      "<p>Both terms in one answer. Five colours need more than 2 bits (4 colours), so 3 bits (8 colours).</p>",
      [[("k", "Image resolution is the number of pixels wide by pixels high in the image whereas screen resolution is the number of pixels wide by high that the screen can display. If the screen has fewer pixels than the image, the displayed quality is lower. Five colours need 3 bits.")]]) +
  ceq(AP("w22_12", "8(a)"), "[2]", "A bitmap image has a resolution of 4096 × 4096 pixels and 24 bits per pixel. State whether each action increases the file size, decreases it or leaves it unchanged. (i) Change the resolution to 2048 × 2048 pixels. (ii) Change the monitor's screen resolution. (iii) Change the colour of one pixel from white to yellow.",
      ["(i) decreases the file size.", "(ii) no change.", "(iii) no change."],
      "<p>The file stores pixels × bits per pixel. Only (i) changes the number of pixels. The monitor and one pixel's colour do not change the stored amount.</p>",
      [[("k", "(i) Decreases, because there are fewer pixels to store. (ii) No change, because screen resolution is about the display. (iii) No change, because the same number of bits stores a pixel of any colour.")]]) +
  ceq(AP("s26_13", "3(b)"), "[5]", "An animation is a sequence of bitmap images. (i) Explain how the data for a bitmap image is encoded. (ii) The bitmap images have a bit depth of 3 bytes, a resolution of 1024 × 768 pixels, and there are 12 images in one second of video. Calculate an estimate of the file size of one second of the video in mebibytes. Show your working.",
      ["The image is a series of pixels; each pixel has one colour; each colour has a unique binary code; the code for each pixel is stored in sequence.", "Working 1024 × 768 × 3 × 12 ÷ 1024 ÷ 1024, answer 27 MiB."],
      "<p>Three points from four for the encoding. In (ii) the depth is already in bytes, so do not divide by 8. 786 432 pixels × 3 = 2 359 296 bytes per image × 12 = 28 311 552 bytes = 27 MiB.</p>",
      [[("k", "The image is made of pixels and each pixel has one colour. Each colour has a unique binary code, and the code for the colour of each pixel is stored in sequence. "), ("a", "1024 × 768 × 3 bytes × 12 images = 28 311 552 bytes ÷ 1024 ÷ 1024 = 27 MiB.")]]) +
  ceq(AP("s25_13", "1(a)"), "[6]", "A camera creates an image with a resolution of 3 million pixels and a bit depth of 24 bits. (i) Calculate the file size in megabytes. Show your working. (ii) A second photograph uses a lower bit depth. Explain the effect of decreasing the bit depth on the image and on the image file.",
      ["Working 3 000 000 × 24 ÷ 8 ÷ 1 000 000, answer 9 MB.", "Image: fewer shades of colour are available, so detail is lost and it does not match the original as well.", "File: fewer bits are used for each pixel, so less data is stored and the file is smaller."],
      "<p>Megabytes means divide by 1 000 000. The explanation has two halves: the image, then the file.</p>",
      [[("k", "3 000 000 × 24 = 72 000 000 bits ÷ 8 = 9 000 000 bytes = 9 MB. "), ("a", "Image: fewer shades of colour are available, so the image loses detail. File: fewer bits are stored for each pixel, so the file size is reduced.")]]) +
  ceq(AP("w21_12", "5(a)"), "[4]", "A logo is a vector graphic made of a red circle and a black line. Complete the table by describing each term and giving an example from the logo: property, drawing list.",
      ["Property: data about one aspect of the appearance of a drawing object; example fill colour red or line colour black.", "Drawing list: the list of shapes in the image, with the commands needed to draw each; example circle and line."],
      "<p>Each row has a description mark and an example mark. The example must come from the logo in the question.</p>",
      [[("k", "Property: an attribute of one drawing object, for example the fill colour of the circle is red. "), ("a", "Drawing list: the list of drawing objects and the commands to draw each, for example the circle and the black line.")]]) +
  ceq(AP("s24_12", "2(d)(ii)"), "[2]", "Describe the contents of a vector graphic drawing list.",
      ["A list of the objects in the drawing.", "The commands or description of how to draw each object.", "The properties of each object, such as fill colour and line weight (max 2)."],
      "<p>Objects, then how each is drawn, then properties. Two of the three.</p>",
      [[("k", "The drawing list stores each drawing object in the image and the command or equation needed to draw it, together with its properties, such as the fill colour and line weight.")]]) +
  ceq(AP("w21_12", "5(b)(i)"), "[4]", "Describe two differences between a vector graphic and a bitmap image.",
      ["Each difference is worth two marks (a point on each side): a bitmap is made of pixels whereas a vector graphic stores instructions to draw shapes; a bitmap pixelates when enlarged whereas a vector is recalculated; bitmap files are usually larger because each pixel is stored whereas vector files are smaller."],
      "<p>Two differences, each with a bitmap half and a vector half.</p>",
      [[("k", "A bitmap is made up of pixels with a colour stored for each whereas a vector graphic stores a set of instructions for drawing shapes. When a bitmap is enlarged the pixels get bigger and it looks pixelated whereas a vector graphic is recalculated so it does not pixelate.")]]) +
  ceq(AP("w22_12", "8(b)"), "[2]", "State two benefits of creating a vector graphic instead of a bitmap image.",
      ["Any two: it can be enlarged without pixelation or loss of quality; individual components can be edited; the file size is generally smaller."],
      "<p>Benefits, not features. Say what the user gains.</p>",
      [[("k", "It can be enlarged without losing quality, and individual objects in it can be edited separately.")]]) +
  ceq(AP("s26_11", "5(c)"), "[3]", "A school needs a new logo, which can be a bitmap image or a vector graphic. Identify which is most appropriate and justify your choice.",
      ["No mark for the choice. Three marks for reasons that match it.", "Vector: made of simple shapes calculated mathematically; can be resized without pixelation so it works on many documents; smaller file so it does not use much storage.", "Bitmap: could include photographic detail; more precise or detailed; edited at pixel level."],
      "<p>Pick one and keep every reason on that side. Vector is the easier case to justify for a logo.</p>",
      [[("k", "Vector graphic. "), ("a", "A logo is made of simple shapes that are calculated, so it can be resized for a letterhead or a banner without pixelation. The file is also small, so it does not use much storage when it is used on many documents.")]])
])

tips = tips_html([
  ("Define with the exact words.", "Pixel: smallest element, one colour. Image resolution: pixels wide by pixels high. Bit depth: bits per pixel."),
  ("Describe encoding in order.", "Pixels, one colour each, a unique binary code for each colour, codes stored in sequence."),
  ("Check the unit.", "Bits or bytes per pixel? Mebibytes (1024) or megabytes (1000)?"),
  ("Show the multiplication.", "Width × height × bit depth, then the divisions. The working earns its own mark."),
  ("Say the cause.", "Decreasing the colour depth means fewer bits per pixel, so the file is smaller."),
  ("Justify one side only.", "For bitmap or vector, no mark for the choice, and mixed reasons contradict each other."),
], [
  ("how a bitmap is encoded", "The image is made of pixels, each pixel has one colour, each colour has a unique binary code, and the code for each pixel is stored in sequence."),
  ("the effect of higher resolution", "More pixels are stored, so the image has more detail, but the file is larger."),
  ("why vector suits a logo", "It is recalculated when resized, so it does not pixelate, and its file size is small."),
  ("a file header", "Data about the image file, such as the file type, the dimensions and the colour depth."),
], [("Define / State", "The precise meaning, or one fact."), ("Describe", "Say what it is made of or how it is stored, in order."), ("Calculate", "Show the multiplication and divisions, then the answer with its unit."), ("Explain", "Give the cause and the effect."), ("Justify", "A reason that matches the choice you made.")]) + FC

js = AKJS + r'''
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
''' + CLASSIFY("cl1", "Does each description belong to a bitmap or a vector graphic?", ["Bitmap", "Vector graphic"],
  [("Pixel", 0), ("Drawing list", 1), ("Colour depth", 0), ("Drawing object", 1), ("File header", 0), ("Property such as line weight", 1), ("Looks blocky when enlarged", 0), ("Recalculated when resized", 1)],
  "Pixels, colour depth and file headers are bitmap terms. Drawing objects, properties and drawing lists are vector terms.") + CLASSIFY("cl2", "What happens to a bitmap file's size?", ["Larger", "Smaller", "No change"],
  [("Increase the colour depth from 8 to 24 bits", 0), ("Reduce the image resolution to half the width and height", 1), ("Change the screen resolution of the monitor", 2), ("Change one pixel from blue to green", 2), ("Increase the image resolution", 0), ("Reduce the colour depth from 16 to 8 bits", 1)],
  "The size depends on the number of pixels and the bits per pixel. The display and one pixel's colour do not change either.") + ORDER(
  "Put the steps for estimating a bitmap file size in order.",
  ["Write down the width, height and bits per pixel", "Multiply width × height to get the number of pixels", "Multiply by the bits per pixel", "Divide by 8 to get bytes", "Divide by 1024 (and again) for kibibytes or mebibytes"],
  "Pixels, then bits, then bytes, then the larger units.") + MATCH([
  ["Pixel", "The smallest element of a bitmap, one square of one colour"], ["Image resolution", "Pixels wide × pixels high in the image"], ["Colour depth", "Bits used for the colour of each pixel"], ["File header", "Data about the image stored with the pixel data"], ["Drawing list", "All the drawing objects in a vector graphic, with commands to draw each"]]) + CALC([
  {"q": "How many colours can be represented with 8 bits per pixel?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "What is the smallest bit depth for an image with 20 colours?", "a": 5, "unit": "bits", "tol": 0.01, "hint": "2^4 = 16 is too few; 2^5 = 32.", "sol": "<b>5</b> bits."},
  {"q": "A bitmap is 800 × 600 pixels with a colour depth of 8 bits. How many bytes is the file (ignoring the header)?", "a": 480000, "unit": "bytes", "tol": 0.01, "hint": "800 × 600 × 8 ÷ 8.", "sol": "<b>480 000</b> bytes."},
  {"q": "A bitmap is 2048 × 1024 pixels with a colour depth of 24 bits. How many mebibytes?", "a": 6, "unit": "MiB", "tol": 0.01, "hint": "2048 × 1024 × 3 bytes ÷ 1 048 576.", "sol": "<b>6</b> MiB."},
  {"q": "A bitmap has 4 million pixels and a colour depth of 16 bits. How many megabytes (1 MB = 1 000 000 bytes)?", "a": 8, "unit": "MB", "tol": 0.01, "hint": "4 000 000 × 2 bytes.", "sol": "<b>8</b> MB."},
  {"q": "A photograph uses 24 bits per pixel. It is changed to 8 bits per pixel. What fraction of the original size remains (as a decimal)?", "a": 0.333, "unit": "", "tol": 0.01, "hint": "8 ÷ 24.", "sol": "<b>0.333</b>, a third of the size."},
  {"q": "An image is 16 × 16 pixels at 2 bits per pixel. How many bits are stored?", "a": 512, "unit": "bits", "tol": 0.01, "hint": "256 pixels × 2.", "sol": "<b>512</b> bits."},
  {"q": "A bitmap has a bit depth of 3 bytes and a resolution of 100 × 100 pixels. How many bytes?", "a": 30000, "unit": "bytes", "tol": 0.01, "hint": "10 000 pixels × 3. The depth is already in bytes.", "sol": "<b>30 000</b> bytes."}]) + MCQ([
  ("What is a pixel?", ["A row of identical colours", "The binary code for a colour", "The smallest element of an image that can be one colour", "The number of colours in an image"], 2, "A pixel is the smallest element of a bitmap and has one colour."),
  ("Which change does NOT alter the size of a bitmap file?", ["Doubling the image width", "Changing the colour depth from 8 to 16 bits", "Changing the screen resolution of the monitor", "Halving the image height"], 2, "Screen resolution changes the display, not the stored image."),
  ("Which statement about a vector graphic is correct?", ["It stores a colour for every pixel", "It stores a drawing list of objects and their properties", "It always has a larger file than a bitmap", "It becomes pixelated when enlarged"], 1, "A vector graphic is a drawing list."),
  ("What is a drawing object?", ["The colour of a shape", "An individual element such as a line or circle", "A list of every pixel", "The file type"], 1, "Drawing objects are the elements; properties describe them."),
  ("Why is a vector graphic a good choice for a logo that will be printed at many sizes?", ["It stores more colours", "It is recalculated at each size so it does not pixelate", "It uses a larger file", "It cannot be edited"], 1, "Recalculation keeps the edges smooth at any size."),
  ("A bitmap uses 6 colours. What is the smallest bit depth?", ["2", "3", "4", "6"], 1, "2^2 = 4 is too few; 2^3 = 8 covers 6 colours.")], "qz1") + CARDS([
  ("Pixel", "Smallest element of a bitmap. One square, one colour."), ("Image resolution", "Pixels wide × pixels high."), ("Screen resolution", "Pixels the screen can display."), ("Colour depth", "Bits per pixel. n bits = 2^n colours."),
  ("File header", "Data about the file: type, size, dimensions, colour depth."), ("File size", "Width × height × bit depth ÷ 8 for bytes."), ("Drawing object", "One element of a vector image: line, circle, rectangle."), ("Property", "Attribute of a drawing object: fill colour, line weight."), ("Drawing list", "All the drawing objects and the commands to draw them.")])

build("ac121", "ac-1-2-1-bitmap-and-vector-graphics", "Graphics: Bitmap Images and Vector Graphics", EYA("1.2.1"),
  "How a bitmap is encoded, resolution and colour depth, estimating file sizes, how changes affect quality and size, vector drawing lists, choosing between bitmap and vector, and thirteen questions from the 2021 to 2026 papers.",
  dict(sub=CBK("Chapter 1 · Information representation, section 1.2 Multimedia (graphics)"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
