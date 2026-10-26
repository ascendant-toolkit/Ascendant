"""A Level CS syllabus 18.1.4: artificial neural networks, back propagation and regression. Run: python3 tools/artifact-kit/mk_ac1814.py"""
import math
from ak16 import *

# worked values for the Learn tab (a single sigmoid neuron)
def sig(x):
    return 1 / (1 + math.exp(-x))


w1, w2, b0 = 0.8, -0.4, 0.1
x1, x2 = 1, 1
z = x1 * w1 + x2 * w2 + b0
a = sig(z)
assert round(z, 2) == 0.5 and round(a, 3) == 0.622

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>artificial neural network (ANN)</b> is a system of connected <b>nodes (neurons)</b> arranged in an <b>input layer</b>, one or more <b>hidden layers</b> and an <b>output layer</b>, designed to simulate how a biological brain works. Each connection has a <b>weight</b>; a neuron adds up its weighted inputs and passes the result on, and the network <b>learns</b> by adjusting the weights during training, which is why ANNs are a key part of machine learning. <b>Back propagation of errors</b> is how the weights are adjusted: the network's output is compared with the expected output, the error is fed back through the network (using calculus to find the error gradient), and the weight of each node is adjusted to reduce the error; the process repeats until the results are accurate enough. <b>Regression</b> is a supervised learning method that finds the best-fit line or curve showing how one variable depends on others, so it can forecast trends and predict outcomes. Deep learning uses ANNs with many hidden layers.</p></div>

  <h2>1 · The structure of an artificial neural network</h2>
  <ul>
    <li><b>Input layer</b>: receives the data, one node for each input value.</li>
    <li><b>Hidden layers</b>: one or more layers of nodes between input and output, where the data is analysed and characteristics extracted. Each hidden layer feeds the next. <b>Many hidden layers</b> make the network deep, able to learn more complex things and give more accurate results.</li>
    <li><b>Output layer</b>: gives the result, for example a category or a value.</li>
    <li>Every node is connected to nodes in the next layer by a link with a <b>weight</b>, a number saying how strongly the signal counts.</li>
  </ul>
  <p>A single neuron multiplies each input by its weight, adds them (and a bias), and passes the total through an <b>activation function</b> that squashes it into a range such as 0 to 1. Example with inputs 1 and 1, weights 0.8 and −0.4, bias 0.1: total = 1 × 0.8 + 1 × (−0.4) + 0.1 = ''' + f"{z:.1f}" + ''', and a sigmoid activation gives about ''' + f"{a:.2f}" + '''.</p>

  <h2>2 · How ANNs help machine learning</h2>
  <ul>
    <li>They are intended to <b>replicate the way human brains work</b>, and can <b>solve problems</b> that would be impossible or very hard for humans to program by hand.</li>
    <li>Weights are assigned to every connection between nodes. Data goes in at the input layer and passes through the hidden layers, where characteristics are extracted and outputs calculated, to the output layer.</li>
    <li>The training is <b>repeated many times</b>, adjusting the weights, to get the best results. The network is able to make decisions without being specifically programmed, and has <b>self-learning</b> capability: it produces better results as more data becomes available.</li>
    <li><b>Back propagation</b> is used to correct the errors.</li>
  </ul>

  <h2>3 · Back propagation of errors</h2>
  <ol>
    <li>Training data is fed forward through the network, and the <b>initial output is compared with the expected output</b>.</li>
    <li>The <b>error</b> (the difference) is worked out. <b>Calculus</b> is used to find the <b>error gradient</b>: how much each weight contributed to the error.</li>
    <li>The results are <b>fed back</b> into the network, from the output layer backwards through the hidden layers.</li>
    <li>The <b>weightings of each node are adjusted</b> as a result of the feedback, in the direction that <b>minimises</b> the difference between actual and expected outputs.</li>
    <li>The process <b>repeats</b> with more data until the results are accurate enough.</li>
  </ol>
  <p>This is how deep learning refines its parameters and improves accuracy. It is a form of supervised learning, since the expected outputs are known.</p>

  <h2>4 · Regression</h2>
  <p><b>Regression</b> is a <b>supervised learning</b> technique. It finds a <b>mathematical function</b>, plots a <b>best-fit line or curve</b>, that shows how the <b>independent variables</b> (causes, inputs) influence a <b>dependent variable</b> (effect, output). It is trained to understand the relationship between the variables, and is used for <b>forecasting trends</b> and <b>predicting outcomes</b>. The goal is to <b>minimise the difference between the predicted values and the actual values</b>. Calculus is used to find the error gradient.</p>
  <p>Example: the price of a house depends on its floor area. A regression line through past sales lets a new house's price be predicted from its area.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Describing an ANN as "a network of computers". It is a structure of nodes in layers that simulates the brain.</li>
    <li>Leaving out the weights, or not saying that they are adjusted through training.</li>
    <li>Describing back propagation as "going back to the start". The errors are fed back through the network to adjust the weights.</li>
    <li>Missing that the output is compared with the expected output.</li>
    <li>For regression, writing only "predicts a number". Say: a best-fit line or function between independent variables and a dependent variable, minimising the difference from actual values.</li>
  </ul>
'''

watch = '''
  <h2>1 · A forward pass through a small network</h2>
  <p>Press Play. Thicker lines are heavier weights; green is positive and red negative.</p>
  <div id="stA"></div>
  <h2>2 · Back propagation of the error</h2>
  <div id="stB"></div>
  <h2>3 · Fitting a regression line</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · A single neuron</h2>
  <p>Switch the inputs and move the weights. The neuron adds up the weighted inputs and applies an activation.</p>
  <div class="card"><div class="btnrow" id="nB"></div><div id="nW1"></div><div id="nW2"></div><div id="nBi"></div><div class="verdict" id="nV"></div></div>

  <h2>Lab 2 · Training by adjusting weights</h2>
  <p>A neuron learns the AND function. Each round it compares its output with the expected output and nudges the weights. Press Train.</p>
  <div class="card"><div class="btnrow" id="tB"></div><div id="tT"></div><div class="verdict" id="tV"></div></div>

  <h2>Lab 3 · Regression</h2>
  <p>Drag the sliders to fit a line to the data. The error is the sum of the squared differences. Then press Best fit.</p>
  <div class="card"><div id="gS"></div><div id="gI"></div><div id="gG"></div><div class="verdict" id="gV"></div><div class="btnrow" id="gB"></div></div>
'''

practise = '''
  <h2>1 · Which layer?</h2><div id="cl1" class="card"></div>
  <h2>2 · Back propagation or regression?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of training with back propagation in order</h2><div id="o1" class="card"></div>
  <h2>5 · Working out</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Recognising handwriting", "Each pixel is an input. Hidden layers pick out strokes, then loops and lines, and the output layer says which digit it is. Back propagation adjusted the weights using thousands of labelled examples.", "layers of nodes with trained weights.") +
rw("Predicting house prices", "A regression model fitted to past sales learns how floor area, location and age affect price, then predicts the price of a new house.", "regression: independent variables and a dependent variable.") +
rw("Voice assistants", "A deep network turns the sound into words. Every time it gets a word wrong during training, the error is propagated back and the weights are tuned.", "back propagation refines the weights.") +
rw("Weather and sales forecasting", "Regression finds the trend in past data so that the future can be forecast.", "forecasting trends and predicting outcomes.") +
rw("Learning a skill", "Practising, seeing the error and adjusting is like training a network: each attempt compares the result with the target and corrects a little.", "compare with expected output, adjust, repeat.")
)

where = [
  ("O/N 2021", "31", "9(a)", "1 + 4", "The reason for multiple hidden layers; how ANNs enable machine learning"),
  ("O/N 2023", "31, 33", "12", "4", "Explain what is meant by an artificial neural network"),
  ("M/J 2025", "31", "10(b)", "4", "Explain the use of artificial neural networks in deep learning"),
  ("O/N 2025", "32", "9(b)", "4", "Describe the back propagation of errors method"),
  ("M/J 2026", "33", "9(a)", "3", "Explain what is meant by regression methods in machine learning")]

past = '''  <p class="note">Neural networks, back propagation and regression appear in Paper 3 from 2021 to 2026, always as a description or explanation. No calculation with weights has been asked. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "31", "Q9(a)"), "1 + 4 marks", "State / Explain",
  "The diagram shown represents an artificial neural network (an input layer, three hidden layers and an output layer). (i) State the reason for having multiple hidden layers in an artificial neural network. (ii) Explain how artificial neural networks enable machine learning.",
  "(i) enables deep learning; more complex problems need more layers.",
  "<p><b>(i)</b> One: " + mks(["Enables deep learning to take place", "A problem of higher complexity needs more layers to solve", "To enable the network to learn and make decisions on its own", "To improve the accuracy of the result"]) + "</p><p><b>(ii)</b> Any four: " + mks(["Artificial neural networks are intended to replicate the way human brains work", "Weights or values are assigned to each connection between nodes", "The data are input at the input layer and passed into the system", "They are analysed at each subsequent (hidden) layer, where characteristics are extracted or outputs calculated", "This process of training is repeated many times to achieve optimum outputs (reinforcement learning takes place)", "Decisions can be made without being specifically programmed", "The deep learning net will have created complex feature detectors", "The output layer provides the results", "Back propagation of errors is used to correct any errors that have been made"], "a") + "</p>", None) + peq(SRC("w23", "31/33", "Q12"), "4 marks", "Explain",
  "Artificial neural networks have played a significant role in the development of machine learning. Explain what is meant by the term artificial neural network.",
  "Simulates the brain; layers; weights adjusted through training.",
  "<p>Any four: " + mks(["An artificial neural network is the component of AI meant to simulate the functioning of a biological brain", "ANNs are a key component of machine learning", "They can solve problems that would prove impossible or difficult for humans, or have self-learning capabilities that produce better results as more data becomes available", "They can be layered (input, hidden and output layers), with many interconnected layers, some or many of which are hidden", "Weights are assigned between nodes", "Weights are adjusted through training to give a more accurate result", "More complex learning capabilities or more accurate results are available with larger numbers of hidden layers"]) + "</p>", None) + peq(SRC("s25", "31", "Q10(b)"), "4 marks", "Explain",
  "Explain the use of artificial neural networks in Deep Learning.",
  "Work like the brain; layers of connected nodes; weights adjusted; many hidden layers.",
  "<p>Any four: " + mks(["Artificial neural networks are designed to work in the same way as the human brain", "ANNs provide the architecture and algorithms for learning from the data", "They have a large number of connected processing units, or nodes", "that are arranged in layers, interconnected and working together to process data", "Deep learning models learn from data by adjusting the weights or biases of the connections between neurons", "They use multiple hidden layers to extract complex features and to make predictions"]) + "</p>", None) + peq(SRC("w25", "32", "Q9(b)"), "4 marks", "Describe",
  "Describe the back propagation of errors method in Machine Learning.",
  "Compare with expected output; adjust weights to minimise the difference; feed the results back; repeat.",
  "<p>Any four: " + mks(["Initial outputs are compared to the expected outputs", "Weightings are adjusted to minimise the difference between actual and expected outputs", "Calculus is used to find the error gradient in the obtained outputs", "The results are fed back into the neural network", "The weightings of each neuron or node are adjusted as a result of the feedback", "The process repeats until the results are more accurate"]) + "</p>", "Describing training in general terms. The marks are for comparing with expected outputs, feeding the error back and adjusting the weights.") + peq(SRC("s26", "33", "Q9(a)"), "3 marks", "Explain",
  "Explain what is meant by regression methods in relation to machine learning.",
  "Supervised; best-fit line or function; independent and dependent variables; minimise the difference.",
  "<p>Any three: " + mks(["A supervised learning technique of machine learning", "It finds a mathematical function, plots a best-fit line or curve, or uses calculus to find the error gradient", "that maps how independent variables (causes) influence a dependent variable (effect) between the data", "It is used for forecasting trends and predicting outcomes", "It is trained to understand the relationship between different causes and effects", "The goal is to minimise the difference between the predicted values and the actual values"]) + "</p>", None)

review = req("3 marks", "Describe", "Describe the roles of the input layer, the hidden layers and the output layer of an artificial neural network.", "In, process, out.", "<p>" + mks(["The input layer receives the data", "The hidden layers analyse it and extract characteristics, each feeding the next", "The output layer gives the result"]) + "</p>", None) + req("3 marks", "Explain", "Explain what a weight is and why the weights change during training.", "Strength of a connection.", "<p>" + mks(["A weight is a number on a connection between nodes saying how much that signal counts", "During training the output is compared with the expected output", "The weights are adjusted to reduce the error, so the results become more accurate"]) + "</p>", None) + req("2 marks", "State", "State two things back propagation uses to improve a neural network.", "Expected output; the error.", "<p>" + mks(["The difference between the actual and the expected output (the error)", "Feedback of that error through the network to adjust the weights"]) + "</p>", None) + req("3 marks", "Explain", "A shop has ten years of data on temperature and ice-cream sales. Explain how regression could be used.", "Independent and dependent variable.", "<p>" + mks(["Temperature is the independent variable and sales is the dependent variable", "A best-fit line or function is found that minimises the difference from the actual sales", "It can then predict sales for a forecast temperature"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a network with more hidden layers can solve harder problems.", "Features.", "<p>" + mks(["Each hidden layer extracts higher-level features from the layer before", "So more layers can learn more complex patterns and give more accurate results"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on artificial neural networks, back propagation and regression (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Layers: input, hidden, output.", "Many hidden layers make it deep."),
  ("Weights on connections.", "Adjusted through training."),
  ("Back propagation: compare, feed back, adjust.", "Repeat until accurate."),
  ("Calculus finds the error gradient.", "Quote it if asked how."),
  ("Regression: best-fit line.", "Independent variables to a dependent variable; minimise the difference."),
  ("Both are supervised.", "The expected outputs are known."),
], [
  ("an ANN", "Layers of connected nodes that simulate how a brain works."),
  ("a weight", "A value on a connection that is adjusted in training."),
  ("back propagation", "Feeding errors back through the network to adjust weights."),
  ("regression", "Finding the best-fit function between variables."),
], [("State", "One short answer."), ("Describe", "Several points."), ("Explain", "Give the reasons."), ("Outline", "Main points.")]) + FC

js = AKJS + AK20JS + r'''
const sig = (x) => 1 / (1 + Math.exp(-x));
const fmt = (x) => (Math.round(x * 100) / 100).toString();
/* 2-2-1 network with fixed starting weights */
const NET0 = { w1: [[0.5, -0.3], [0.2, 0.8]], b1: [0.1, -0.1], w2: [0.7, -0.6], b2: 0.2 }; const IN = [1, 0], TARGET = 1;
function fwd(n, x) { const h = [0, 1].map((j) => sig(x[0] * n.w1[0][j] + x[1] * n.w1[1][j] + n.b1[j])); const o = sig(h[0] * n.w2[0] + h[1] * n.w2[1] + n.b2); return { h, o }; }
function backprop(n, x, t, lr) { const { h, o } = fwd(n, x), dO = (o - t) * o * (1 - o), dH = [0, 1].map((j) => dO * n.w2[j] * h[j] * (1 - h[j]));
  const m = JSON.parse(JSON.stringify(n)); [0, 1].forEach((j) => { m.w2[j] -= lr * dO * h[j]; m.b1[j] -= lr * dH[j]; [0, 1].forEach((i) => (m.w1[i][j] -= lr * dH[j] * x[i])); }); m.b2 -= lr * dO; return { m, dO, dH }; }
function netDraw(n, x, o) { /* nodes: in 0,1 ; hidden 0,1 ; out */ const P = { i0: [70, 70], i1: [70, 170], h0: [250, 50], h1: [250, 190], o: [430, 120] }; let s = "";
  const edge = (a, b, w) => (s += SV.line(P[a][0], P[a][1], P[b][0], P[b][1], "ax", { style: "stroke:" + (w >= 0 ? "var(--good)" : "var(--bad)") + ";stroke-width:" + (1 + Math.abs(w) * 5) + ";opacity:.8" }));
  [0, 1].forEach((j) => [0, 1].forEach((i) => edge("i" + i, "h" + j, n.w1[i][j]))); [0, 1].forEach((j) => edge("h" + j, "o", n.w2[j]));
  const node = (k, v, lab) => (s += SV.circle(P[k][0], P[k][1], 26, "nd", {}) + SV.text(P[k][0], P[k][1] + 5, v === null ? "" : fmt(v), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(P[k][0], P[k][1] + 44, lab, "sm", { "text-anchor": "middle" }));
  node("i0", x[0], "input 1"); node("i1", x[1], "input 2"); if (o) { node("h0", o.h[0], "hidden 1"); node("h1", o.h[1], "hidden 2"); node("o", o.o, "output"); } else { node("h0", null, "hidden 1"); node("h1", null, "hidden 2"); node("o", null, "output"); } return s; }
(function () {
  const r = fwd(NET0, IN);
  const draw = (s) => { const k = Math.round(s.i); let o = netDraw(NET0, IN, k >= 1 ? { h: k >= 2 ? r.h : [0, 0], o: k >= 3 ? r.o : 0 } : null); if (k < 2 && k >= 1) o = netDraw(NET0, IN, null); return o + SV.text(20, 20, "weights: green positive, red negative", "sm"); };
  Lib.stepper($("#stA"), { w: 500, h: 250, label: "Forward pass", base: { i: 0 }, draw: (s) => { const k = Math.round(s.i); return netDraw(NET0, IN, k >= 2 ? { h: k >= 3 ? r.h : [0, 0], o: k >= 4 ? r.o : 0 } : null) + SV.text(20, 18, "weights: green positive, red negative", "sm"); }, tween: 120, dwell: 2800, steps: [{ cap: "A small network: 2 inputs, 2 hidden nodes and 1 output. Each line is a connection with a <b>weight</b>.", s: { i: 0 } }, { cap: "The input layer receives the data: the inputs are 1 and 0.", s: { i: 1 } }, { cap: "Each hidden node adds up its weighted inputs plus a bias and applies the activation function.", s: { i: 2 } }, { cap: `The hidden outputs are ${fmt(r.h[0])} and ${fmt(r.h[1])}, which feed the output node.`, s: { i: 3 } }, { cap: `The network outputs <b>${fmt(r.o)}</b>. The expected output is <b>${TARGET}</b>, so there is an error of ${fmt(TARGET - r.o)}.`, s: { i: 4 } }] });
})();
(function () {
  const r0 = fwd(NET0, IN), bp = backprop(NET0, IN, TARGET, 2), r1 = fwd(bp.m, IN);
  const draw = (s) => { const k = Math.round(s.i); const n = k >= 3 ? bp.m : NET0, r = k >= 4 ? r1 : r0; let o = netDraw(n, IN, r);
    if (k >= 1 && k < 4) o += SV.text(430, 190, "error " + fmt(TARGET - r0.o), "lbl bd t2", { "text-anchor": "middle", style: "font-size:13px" }); if (k >= 2 && k < 3) o += SV.path("M400,120 H280", "ax", { style: "stroke:var(--bad);stroke-width:3" }) + SV.arrowHead(274, 120, "l", "dot2");
    if (k >= 4) o += SV.text(430, 190, "error " + fmt(TARGET - r1.o), "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 500, h: 250, label: "Back propagation", base: { i: 0 }, draw, tween: 120, dwell: 3000, steps: [{ cap: `The network's output is ${fmt(r0.o)}.`, s: { i: 0 } }, { cap: `The expected output is ${TARGET}: the <b>error</b> is ${fmt(TARGET - r0.o)}. The output is compared with the expected output.`, s: { i: 1 } }, { cap: "The error is <b>fed back</b> through the network, from the output layer towards the input layer. Calculus gives each weight's share of the error (the error gradient).", s: { i: 2 } }, { cap: "The <b>weights are adjusted</b> to reduce the error: some connections grow stronger and some weaker.", s: { i: 3 } }, { cap: `After one round the output is ${fmt(r1.o)} and the error has fallen to ${fmt(TARGET - r1.o)}. The process <b>repeats</b> until the results are accurate.`, s: { i: 4 } }] });
})();
(function () {
  const D = [[1, 2.2], [2, 3.1], [3, 4.4], [4, 4.8], [5, 6.2], [6, 6.9], [7, 8.3]]; const n = D.length, sx = D.reduce((a, d) => a + d[0], 0), sy = D.reduce((a, d) => a + d[1], 0), sxy = D.reduce((a, d) => a + d[0] * d[1], 0), sxx = D.reduce((a, d) => a + d[0] * d[0], 0);
  const m = (n * sxy - sx * sy) / (n * sxx - sx * sx), c = (sy - m * sx) / n; const X = (x) => 40 + x * 55, Y = (y) => 230 - y * 24;
  const draw = (s) => { const k = Math.round(s.i); const lm = k === 0 ? 0.2 : k === 1 ? 2 : m, lc = k === 0 ? 4 : k === 1 ? -1 : c; let o = SV.path("M40,20 V230 H440", "ax") + SV.text(240, 252, "independent variable (x)", "sm", { "text-anchor": "middle" });
    if (k >= 1) D.forEach(([x, y]) => (o += SV.line(X(x), Y(y), X(x), Y(lm * x + lc), "ax", { style: "stroke:var(--bad);stroke-width:1.5;opacity:.7" }))); D.forEach(([x, y]) => (o += SV.circle(X(x), Y(y), 5, "dot1")));
    if (k >= 0) o += SV.line(X(0.4), Y(lm * 0.4 + lc), X(7.6), Y(lm * 7.6 + lc), "ax", { style: "stroke:var(--good);stroke-width:3" }); const err = D.reduce((a, [x, y]) => a + (y - (lm * x + lc)) ** 2, 0); if (k >= 1) o += SV.text(50, 14, "squared error = " + fmt(err), "lbl bd", { "text-anchor": "start", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 262, label: "Regression", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "Past data: each dot is an example (an x value and the actual y). A first, poor line is tried.", s: { i: 0 } }, { cap: "The <b>differences</b> between the predicted values (on the line) and the actual values are the red lines. The goal is to <b>minimise</b> them.", s: { i: 1 } }, { cap: "The best-fit line is found. Its total error is the smallest possible, and it can now be used to <b>predict</b> y for a new x.", s: { i: 2 } }] });
})();

(function () {
  const x = [1, 1], b = $("#nB"); let w1 = 0.8, w2 = -0.4, bi = 0.1;
  const paint = () => { const z = x[0] * w1 + x[1] * w2 + bi, a = sig(z); $("#nV").innerHTML = `Total = ${x[0]} × ${w1} + ${x[1]} × ${w2} + ${bi} = <b>${fmt(z)}</b>. Activation (sigmoid) = <b>${a.toFixed(3)}</b>. ${a >= 0.5 ? "The neuron fires (output near 1)." : "The neuron stays quiet (output near 0)."}`; b.querySelectorAll("button").forEach((y, i) => { y.textContent = "Input " + (i + 1) + " = " + x[i]; y.className = x[i] ? "on" : ""; }); };
  [0, 1].forEach((i) => { const y = document.createElement("button"); y.onclick = () => { x[i] ^= 1; paint(); }; b.appendChild(y); });
  Lib.slider($("#nW1"), { id: "w1", label: "Weight 1 ", min: -20, max: 20, value: 8, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { w1 = v / 10; paint(); } });
  Lib.slider($("#nW2"), { id: "w2", label: "Weight 2 ", min: -20, max: 20, value: -4, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { w2 = v / 10; paint(); } });
  Lib.slider($("#nBi"), { id: "bi", label: "Bias ", min: -20, max: 20, value: 1, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { bi = v / 10; paint(); } }); paint();
})();
(function () {
  const DATA = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]; let w = [0.1, -0.2], bi = 0.0, ep = 0; const hist = []; const b = $("#tB");
  const err = () => DATA.reduce((a, [x1, x2, t]) => a + Math.abs(t - sig(x1 * w[0] + x2 * w[1] + bi)), 0);
  const round = () => { DATA.forEach(([x1, x2, t]) => { const o = sig(x1 * w[0] + x2 * w[1] + bi), d = (o - t) * o * (1 - o); w[0] -= 2 * d * x1; w[1] -= 2 * d * x2; bi -= 2 * d; }); ep++; hist.push(err()); if (hist.length > 8) hist.shift(); };
  const paint = () => { $("#tT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>x1</th><th>x2</th><th>expected</th><th>output</th></tr>' + DATA.map(([x1, x2, t]) => { const o = sig(x1 * w[0] + x2 * w[1] + bi); return `<tr><td>${x1}</td><td>${x2}</td><td>${t}</td><td style="color:${Math.abs(o - t) < 0.3 ? "var(--good)" : "var(--bad)"};font-weight:700">${o.toFixed(2)}</td></tr>`; }).join("") + "</table></div>";
    $("#tV").innerHTML = `Rounds of training: <b>${ep}</b>. Weights: ${w.map(fmt).join(", ")}, bias ${fmt(bi)}. Total error <b>${err().toFixed(2)}</b>` + (hist.length > 1 ? " (recent: " + hist.map((h) => h.toFixed(2)).join(" → ") + ")" : "") + ". The error falls as the weights are adjusted."; };
  [["Train 1 round", 1], ["Train 100 rounds", 100], ["Reset", 0]].forEach(([t, k]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = () => { if (!k) { w = [0.1, -0.2]; bi = 0; ep = 0; hist.length = 0; } else for (let i = 0; i < k; i++) round(); paint(); }; b.appendChild(x); }); paint();
})();
(function () {
  const D = [[1, 2.2], [2, 3.1], [3, 4.4], [4, 4.8], [5, 6.2], [6, 6.9], [7, 8.3]]; let m = 0.5, c = 3; const X = (x) => 40 + x * 55, Y = (y) => 230 - y * 24;
  const n = D.length, sx = D.reduce((a, d) => a + d[0], 0), sy = D.reduce((a, d) => a + d[1], 0), sxy = D.reduce((a, d) => a + d[0] * d[1], 0), sxx = D.reduce((a, d) => a + d[0] * d[0], 0), bm = (n * sxy - sx * sy) / (n * sxx - sx * sx), bc = (sy - bm * sx) / n;
  const paint = () => { let o = '<path d="M40,20 V230 H440" class="ax"/>'; D.forEach(([x, y]) => (o += `<line x1="${X(x)}" y1="${Y(y)}" x2="${X(x)}" y2="${Y(m * x + c)}" stroke="var(--bad)" stroke-width="1.5" opacity=".7"/>`)); D.forEach(([x, y]) => (o += `<circle cx="${X(x)}" cy="${Y(y)}" r="5" class="dot1"/>`)); o += `<line x1="${X(0.4)}" y1="${Y(m * 0.4 + c)}" x2="${X(7.6)}" y2="${Y(m * 7.6 + c)}" stroke="var(--good)" stroke-width="3"/>`;
    $("#gG").innerHTML = `<svg viewBox="0 0 480 250" style="width:480px;max-width:100%;display:block">${o}</svg>`; const e = D.reduce((a, [x, y]) => a + (y - (m * x + c)) ** 2, 0), eb = D.reduce((a, [x, y]) => a + (y - (bm * x + bc)) ** 2, 0);
    $("#gV").innerHTML = `y = ${m.toFixed(2)}x + ${c.toFixed(2)}. Sum of squared differences: <b>${e.toFixed(2)}</b> (the best possible is ${eb.toFixed(2)}). Prediction for x = 8: <b>${(m * 8 + c).toFixed(1)}</b>.`; };
  Lib.slider($("#gS"), { id: "gs", label: "Slope ", min: 0, max: 30, value: 5, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { m = v / 10; paint(); } });
  Lib.slider($("#gI"), { id: "gi", label: "Intercept ", min: -20, max: 60, value: 30, fmt: (v) => (v / 10).toFixed(1), onInput: (v) => { c = v / 10; paint(); } });
  const b = $("#gB"), x = document.createElement("button"); x.textContent = "Best fit"; x.onclick = () => { m = bm; c = bc; paint(); }; b.appendChild(x); paint();
})();
''' + CLASSIFY("cl1", "Which layer of an artificial neural network?", ["Input layer", "Hidden layer", "Output layer"],
  [("Receives the data", 0), ("Extracts characteristics from the data", 1), ("Gives the result", 2), ("A deep network has many of these", 1), ("One node for each input value", 0), ("Feeds the next layer after analysing", 1)],
  "Input receives, hidden extracts, output gives the answer.") + CLASSIFY("cl2", "Back propagation or regression?", ["Back propagation", "Regression"],
  [("Feeds the error back through the network", 0), ("Finds a best-fit line between variables", 1), ("Adjusts the weights of the nodes", 0), ("Forecasts trends from past data", 1), ("Compares the output with the expected output", 0), ("Maps independent variables to a dependent variable", 1)],
  "Back propagation trains network weights; regression fits a function.") + MATCH([
  ["Weight", "A value on a connection that training adjusts"], ["Hidden layer", "A layer between input and output where characteristics are extracted"], ["Back propagation", "Errors are fed back to adjust the weights"], ["Regression", "A supervised method that fits a best-fit line or curve"], ["Error gradient", "Found using calculus to see how to change each weight"]]) + ORDER(
  "Put the steps of training with back propagation in order.",
  ["Feed data forward through the network", "Compare the output with the expected output", "Work out the error and feed it back through the network", "Adjust the weights to reduce the error", "Repeat until the results are accurate"],
  "Forward, compare, feed back, adjust, repeat.") + CALC([
  {"q": "A neuron has inputs 1 and 1, weights 0.5 and 0.5, and bias 0. What is the total?", "a": 1, "unit": "", "tol": 0.01, "hint": "0.5 + 0.5.", "sol": "<b>1</b>."},
  {"q": "A network has an input layer of 3 nodes, a hidden layer of 4 and an output of 2. How many connections between the input and hidden layers (every node to every node)?", "a": 12, "unit": "", "tol": 0.01, "hint": "3 × 4.", "sol": "<b>12</b>."},
  {"q": "And between the hidden and output layers?", "a": 8, "unit": "", "tol": 0.01, "hint": "4 × 2.", "sol": "<b>8</b>."},
  {"q": "The expected output is 1 and the network outputs 0.6. What is the error?", "a": 0.4, "unit": "", "tol": 0.01, "hint": "1 − 0.6.", "sol": "<b>0.4</b>."},
  {"q": "A regression line is y = 2x + 1. What does it predict for x = 5?", "a": 11, "unit": "", "tol": 0.01, "hint": "2 × 5 + 1.", "sol": "<b>11</b>."}]) + MCQ([
  ("What does an artificial neural network simulate?", ["A biological brain", "A hard disk", "A monitor", "A keyboard"], 0, "The brain."),
  ("What is adjusted during training?", ["The weights", "The screen", "The power", "The font"], 0, "The weights."),
  ("Back propagation feeds back:", ["The error", "The input only", "The password", "The file name"], 0, "The error."),
  ("Regression is a type of:", ["Supervised learning", "Reinforcement only", "Encryption", "Sorting"], 0, "Supervised."),
  ("The goal of regression is to:", ["Maximise the error", "Minimise the difference between predicted and actual values", "Delete data", "Add layers"], 1, "Minimise the difference."),
  ("More hidden layers lead to:", ["Deeper learning of complex features", "Fewer weights", "No learning", "Smaller data"], 0, "More complex learning.")], "qz1") + CARDS([
  ("ANN", "Layers of connected nodes simulating the brain."), ("Layers", "Input, hidden (one or many), output."), ("Weight", "Value on a connection, adjusted in training."), ("Back propagation", "Compare, feed back the error, adjust weights, repeat."),
  ("Error gradient", "Found with calculus."), ("Regression", "Best-fit function between variables; supervised."), ("Forecasting", "A use of regression."), ("Deep learning", "ANN with many hidden layers.")])

build("ac1814", "ac-18-1-4-neural-networks-backpropagation-regression", "Neural Networks, Back Propagation and Regression", EYA("18.1.4"),
  "Artificial neural networks and how they help machine learning, back propagation of errors, and regression; animations, a neuron lab, a training lab and a regression lab, and the real Paper 3 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 18 · Artificial Intelligence, section 18.1 Artificial Intelligence"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
