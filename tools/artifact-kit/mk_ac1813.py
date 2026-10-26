"""A Level CS syllabus 18.1.3: machine learning categories and deep learning. Run: python3 tools/artifact-kit/mk_ac1813.py"""
from ak16 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Artificial intelligence (AI)</b> is the ability of a computer system to carry out tasks that normally need human intelligence; <b>machine learning</b> is the part of AI in which a system <b>learns from data</b> instead of being given explicit rules; and <b>deep learning</b> is a part of machine learning that uses <b>artificial neural networks with many hidden layers</b>. The main categories of machine learning are <b>supervised learning</b> (trained on <b>labelled</b> data, to predict outcomes), <b>unsupervised learning</b> (given <b>unlabelled</b> data and left to find hidden patterns or clusters) and <b>reinforcement learning</b> (an agent learns by <b>trial and error</b> from rewards and punishments in an environment). Deep learning copes well with large amounts of unstructured data and can find patterns people would not spot. Each method is chosen for the kind of data available and the kind of answer needed.</p></div>

  <h2>1 · AI, machine learning and deep learning</h2>
  <p>They are nested: deep learning is a type of machine learning, which is a type of AI. A machine learning system is <b>trained</b> on data and improves its results with experience; it is not programmed with every rule.</p>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Artificial intelligence</b></td><td>Computer systems that perform tasks normally needing human intelligence</td></tr>
    <tr><td><b>Machine learning</b></td><td>A branch of AI where a system learns from data to improve at a task</td></tr>
    <tr><td><b>Deep learning</b></td><td>A branch of machine learning using artificial neural networks with many layers</td></tr>
  </table></div>

  <h2>2 · Supervised learning</h2>
  <ul>
    <li>The system is trained with <b>labelled data</b>: sample inputs with the <b>known, correct outputs</b> (for example emails marked spam or not spam).</li>
    <li>It learns a <b>mapping from inputs to outputs</b>, and can then <b>predict outcomes</b> for new data and future events based on past outcomes.</li>
    <li>It needs <b>initial human input</b> to provide and label the training data.</li>
  </ul>

  <h2>3 · Unsupervised learning</h2>
  <ul>
    <li>The system is given <b>unlabelled data</b>, with no known outcomes, and no instructions on what to do with it.</li>
    <li>It searches for <b>hidden patterns, structures, groupings or clusters</b> and for similarities and differences, and uses them to predict outcomes.</li>
    <li>It does <b>not need human intervention</b> or training with the correct outputs. As training progresses it gets closer to the desired outcome.</li>
  </ul>

  <h2>4 · Reinforcement learning</h2>
  <ul>
    <li>An <b>agent</b> learns to behave in an <b>environment</b> by performing actions and seeing the results of those actions: <b>trial and error</b>, using its own experiences.</li>
    <li>It is based on <b>feedback</b>: a good action earns a <b>reward</b> (positive feedback) and a bad action a <b>punishment</b> (negative feedback).</li>
    <li>It learns automatically from the feedback <b>without labelled data</b> or specific instructions, adjusting its weightings to improve at similar tasks.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Supervised</th><th>Unsupervised</th><th>Reinforcement</th></tr>
    <tr><td><b>Data</b></td><td>Labelled, known outputs</td><td>Unlabelled</td><td>No labelled data; feedback from the environment</td></tr>
    <tr><td><b>Goal</b></td><td>Predict outputs for new inputs</td><td>Find hidden patterns or clusters</td><td>Maximise reward by choosing good actions</td></tr>
    <tr><td><b>Human input</b></td><td>Needed to label data</td><td>Not needed</td><td>Not needed to label data</td></tr>
    <tr><td><b>Example</b></td><td>Spam filter</td><td>Grouping customers by buying habits</td><td>A program learning to play chess</td></tr>
  </table></div>

  <h2>5 · Deep learning</h2>
  <p>Deep learning is a <b>specialised form of machine learning</b> that uses <b>artificial neural networks</b>, designed to work like the human brain, with an <b>input layer</b>, a <b>large number of hidden layers</b> and an <b>output layer</b>. Each layer extracts higher-level features from the layer before, so the network gradually breaks the data down and finds hidden patterns. It learns by adjusting the weights of the connections, and uses <b>back propagation of errors</b> to refine them (see 18.1.4).</p>
  <h3>Reasons for using it</h3>
  <ul>
    <li>It makes good use of <b>unstructured data</b>, such as images, sound and text.</li>
    <li>It outperforms other methods when the <b>amount of data is large</b>.</li>
    <li>It can process data with a <b>non-linear</b> approach.</li>
    <li>It is effective at identifying <b>hidden patterns</b> that humans might not see or that are too complex and slow for humans to find.</li>
    <li>More hidden layers can give a <b>more accurate outcome</b>.</li>
  </ul>
  <p>Examples: virtual assistants, chatbots, self-driving cars, image and facial recognition, fraud detection, translation, large language models, playing chess, weather forecasting. It can be made more effective by <b>introducing more hidden layers</b>.</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Writing "labelled" for unsupervised data. Supervised data is labelled; unsupervised is not.</li>
    <li>Describing reinforcement learning without feedback: rewards and punishments for actions.</li>
    <li>Saying deep learning is "the same as" machine learning. It is a branch of it that uses neural networks with many hidden layers.</li>
    <li>Giving "it is better" as a reason for deep learning. Say: unstructured data, large data sets, hidden patterns.</li>
    <li>Mixing up the neural network (the structure) and deep learning (learning with a many-layered one).</li>
  </ul>
'''

watch = '''
  <h2>1 · Supervised learning: learn from labelled examples</h2>
  <p>Press Play.</p>
  <div id="stA"></div>
  <h2>2 · Unsupervised learning: find the clusters</h2>
  <div id="stB"></div>
  <h2>3 · Reinforcement learning: trial and error</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Supervised or unsupervised?</h2>
  <p>The points are the same. With labels shown (supervised) a new point is classified by its nearest labelled neighbour. Without labels (unsupervised) the computer groups the points itself.</p>
  <div class="card"><div class="btnrow" id="sB"></div><div id="sG"></div><div class="verdict" id="sV"></div></div>

  <h2>Lab 2 · A reinforcement learner</h2>
  <p>An agent can pull one of three levers. Each pays a reward with a hidden probability. Press Train and watch its estimates and choices change.</p>
  <div class="card"><div class="btnrow" id="rB"></div><div id="rT"></div><div class="verdict" id="rV"></div></div>

  <h2>Lab 3 · Which learning method?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

practise = '''
  <h2>1 · Which category of machine learning?</h2><div id="cl1" class="card"></div>
  <h2>2 · Is it a reason for using deep learning?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the category to its description</h2><div id="m1" class="card"></div>
  <h2>4 · Put the reinforcement learning loop in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Spam filters", "The filter is trained on thousands of emails that people have marked as spam or not spam. From these labelled examples it learns to label new messages.", "supervised learning uses labelled data.") +
rw("Shop recommendations", "A shop groups customers with similar buying habits without anyone telling it the groups in advance, then suggests items popular in the same group.", "unsupervised learning finds clusters in unlabelled data.") +
rw("Game-playing programs", "A program plays against itself many times. Wins are rewards and losses are punishments, and it learns which moves work.", "reinforcement learning by trial and error.") +
rw("Voice assistants and photo apps", "Recognising speech or faces needs many layers of a neural network, each picking out a higher-level feature, trained on huge amounts of data.", "deep learning with many hidden layers.") +
rw("Self-driving cars", "They combine deep learning to recognise road scenes with reinforcement learning to improve driving decisions.", "different methods for different parts of the task.")
)

where = [
  ("M/J 2023", "31, 33", "2(a)", "4", "Connect four machine learning categories to descriptions"),
  ("M/J 2023", "32", "10(a)", "1", "State one category of machine learning"),
  ("O/N 2022", "32", "7", "4", "Describe supervised and unsupervised learning"),
  ("O/N 2022", "31, 33", "9", "2 + 2", "Describe deep learning; reasons for using it"),
  ("M/J 2024", "31, 33", "9", "3", "Explain what is meant by Deep Learning"),
  ("M/J 2024", "32", "11", "3", "Explain what is meant by Reinforcement Learning"),
  ("M/J 2025", "32", "6(b)", "4", "How supervised and unsupervised learning differ"),
  ("M/J 2025", "33", "10(c)", "3", "How unsupervised learning takes place"),
  ("O/N 2025", "31", "7(b)", "5", "Describe Deep Learning"),
  ("O/N 2025", "32", "9(a)", "1 + 1", "An example where Deep Learning is used; how it can be made more effective"),
  ("M/J 2026", "31", "9(a)", "4", "Explain how supervised and unsupervised learning are trained"),
  ("M/J 2026", "32", "9(a)", "1", "State the subset of AI that makes use of an artificial neural network")]

past = '''  <p class="note">Machine learning categories are asked in Paper 3 in every series since 2022, often as three or four marks of description. The neural network questions that go with them, back propagation and regression, are on the next page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s23", "31/33", "Q2(a)"), "4 marks", "Match",
  "Draw one line from each machine learning category to its most appropriate description. Categories: supervised learning; reinforcement learning; deep learning; unsupervised learning. Descriptions: (A) simulates the data-processing capabilities of the human brain to make decisions; (B) enables learning by mapping an input to an output based on example input–output pairs; (C) enables information related to errors produced by the neural network to be transmitted; (D) enables learning in an interactive environment by trial and error using its own experiences; (E) enables learning by allowing the process to discover patterns on its own that were previously undetected.",
  "One description is for back propagation.",
  "<p>" + mks(["Supervised learning → B", "Reinforcement learning → D", "Deep learning → A", "Unsupervised learning → E"]) + "</p><p>Description C is not used: it describes back propagation of errors (18.1.4).</p>", None) + peq(SRC("s23", "32", "Q10(a)"), "1 mark", "State",
  "State one category of machine learning.",
  "Any one of the four.",
  "<p>" + mks(["Supervised, unsupervised, reinforcement or deep learning"]) + "</p>", None) + peq(SRC("w22", "32", "Q7"), "4 marks", "Describe",
  "Supervised and unsupervised learning are two categories of machine learning. Describe supervised learning and unsupervised learning.",
  "Up to three marks for each; known outputs or labelled data against patterns in unlabelled data.",
  "<p><b>Supervised</b> (max 3 of 4): " + mks(["Data can be collected, or a data output produced, from previous experience", "Known inputs and associated outputs are given: sample data with known outputs in training, or labelled input data", "Able to predict future outcomes based on past data"]) + "</p><p><b>Unsupervised</b> (max 3 of 4): " + mks(["Helps all kinds of unknown patterns in data to be found", "Only requires input data to be given", "Uses any data; it is not trained on the right output, or it uses unlabelled input data"], "a") + "</p>", "Describing the two as 'with a teacher' and 'without a teacher'. Say what data each uses: labelled, unlabelled.") + peq(SRC("w22", "31/33", "Q9"), "2 + 2 marks", "Describe / Outline",
  "Deep learning is used in Artificial Intelligence (AI). (a) Describe what is meant by deep learning. (b) Outline the reasons for using deep learning.",
  "(a) neural network, many hidden layers, brain; (b) unstructured data, large data, non-linear, patterns.",
  "<p><b>(a)</b> Any two: " + mks(["Uses artificial neural network(s)", "that contain a high number of hidden layers", "modelled on the human brain", "Uses many layers to progressively extract higher level features from the raw input", "A specialised form of machine learning"]) + "</p><p><b>(b)</b> Any two: " + mks(["Makes good use of unstructured data", "Outperforms other methods if the data size is large", "Enables machines to process data with a non-linear approach", "Effective at identifying hidden patterns that humans might not see, or that are too complex or time-consuming for humans", "Can provide a more accurate outcome with higher numbers of hidden layers"], "a") + "</p>", None) + peq(SRC("s24", "31/33", "Q9"), "3 marks", "Explain",
  "Explain what is meant by Deep Learning in relation to Artificial Intelligence (AI).",
  "Hidden patterns; layers; neural network; large amounts of data.",
  "<p>Any three: " + mks(["Deep learning learns by finding hidden patterns that are undetectable to humans", "It structures algorithms in layers: an input layer, hidden layers and an output layer", "to create an artificial neural network to learn and make intelligent decisions on its own", "It is trained using large quantities of unlabelled data", "It requires or uses a large number of hidden layers", "The larger the number of layers, the higher the level of success"]) + "</p>", None) + peq(SRC("s24", "32", "Q11"), "3 marks", "Explain",
  "Explain what is meant by Reinforcement Learning in relation to Artificial Intelligence.",
  "Agent, environment, rewards and punishments, no labelled data.",
  "<p>Any three: " + mks(["Reinforcement learning is a machine learning technique based on feedback, rewards or punishment", "in which an agent learns to behave in an environment by performing actions and seeing the results", "for each good action the agent gets positive feedback or a reward, and each bad action negative feedback or a punishment", "The agent learns automatically using feedback without any labelled data or specific instructions", "Node weightings are adjusted to achieve the correct outcome; it uses feedback to improve its performance at similar tasks"]) + "</p>", None) + peq(SRC("s25", "32", "Q6(b)"), "4 marks", "Explain",
  "Explain how supervised learning and unsupervised learning differ from each other.",
  "Labelled against unlabelled; human input; outcomes known or not.",
  "<p>Any four: " + mks(["Supervised learning uses labelled data; unsupervised learning uses unlabelled data", "Labelled data means that known outcomes are applied to specific inputs to help the AI predict outcomes", "Supervised learning requires initial human input or training; unsupervised learning does not", "With unlabelled data in unsupervised learning, outcomes are not known", "the AI has to search for hidden patterns, structures or clusters", "within the data in order to predict outcomes"]) + "</p>", None) + peq(SRC("s25", "33", "Q10(c)"), "3 marks", "Explain",
  "Explain how unsupervised learning takes place in machine learning.",
  "Unlabelled data; cluster; hidden patterns without human help.",
  "<p>Any three: " + mks(["Unsupervised learning uses algorithms to analyse or cluster", "unlabelled data sets", "They discover hidden patterns or data groupings without the need for human intervention", "It is able to discover similarities and differences in data"]) + "</p>", None) + peq(SRC("w25", "31", "Q7(b)"), "5 marks", "Describe",
  "Describe Deep Learning.",
  "Branch of machine learning; neural networks; layers; patterns; large data; back propagation.",
  "<p>Any five: " + mks(["Deep learning is a branch of machine learning", "It makes use of artificial neural networks", "to work in a similar manner to the human brain, or neural networks that can be trained to process data", "It is a structure of many interconnected layers: input, hidden and output", "gradually breaking down and analysing the data to find hidden patterns", "Its feature extraction involves detecting features or categories from data", "It can involve different types of supervision", "It works well with large data sets", "It uses back propagation of errors to adjust parameters or weightings to refine its results and improve accuracy"]) + "</p>", "Writing only 'it is like the brain'. Say how: many connected layers of nodes, trained by adjusting weights.") + peq(SRC("w25", "32", "Q9(a)"), "1 + 1 marks", "State / Identify",
  "Deep Learning is a form of Machine Learning. (i) State one example where Deep Learning is used. (ii) Identify how Deep Learning can be made more effective.",
  "(ii) more hidden layers.",
  "<p><b>(i)</b> One: " + mks(["Virtual assistants, chatbots, composing music, self-driving cars, natural language processing, fraud detection, image colouring, image or facial recognition, text mining, computer-assisted translation, large language models, playing chess, grading student exams, weather forecasting"]) + "</p><p><b>(ii)</b> " + mks(["Use or introduce more hidden layers"], "a") + "</p>", None) + peq(SRC("s26", "31", "Q9(a)"), "4 marks", "Explain",
  "Explain how supervised learning and unsupervised learning are trained.",
  "Labelled training data to predict future events; unlabelled data to find hidden patterns.",
  "<p>Any four: " + mks(["Supervised learning makes use of labelled training data", "to predict future events based on past outcomes", "Unsupervised learning makes use of unlabelled training data, with no instructions on what to do with it and not using the correct or expected outcomes", "to search for hidden patterns, relationships, structures, similarities or outliers within the data", "and therefore get closer to the desired outcome as the training progresses"]) + "</p>", None) + peq(SRC("s26", "32", "Q9(a)"), "1 mark", "State",
  "State the subset of Artificial Intelligence (AI) which makes use of an artificial neural network.",
  "Deep learning. 'Machine learning' is not enough because not all machine learning uses neural networks.",
  "<p>" + mks(["Deep learning"]) + "</p>", "Writing 'machine learning'. The mark scheme does not accept it: not all machine learning uses neural networks.")

review = req("3 marks", "Explain", "A bank wants to detect unusual card transactions, but has no examples marked as fraud. Explain which category of machine learning it could use.", "Unlabelled data.", "<p>" + mks(["Unsupervised learning", "It works on unlabelled data, so no examples marked as fraud are needed", "It finds patterns and groups in the transactions, so unusual ones that do not fit can be spotted"]) + "</p>", None) + req("3 marks", "Describe", "A robot is learning to walk. Describe how reinforcement learning could be used.", "Agent, reward, punishment.", "<p>" + mks(["The robot (the agent) tries actions in its environment", "Steps that keep it upright get a reward and falls get a punishment (feedback)", "It adjusts how it chooses actions to earn more reward, by trial and error, without labelled data"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between machine learning and deep learning.", "Which is part of which?", "<p>" + mks(["Machine learning is where a system learns from data to improve at a task", "Deep learning is a branch of it that uses artificial neural networks with many hidden layers"]) + "</p>", None) + req("2 marks", "State", "State two reasons why deep learning would suit an image recognition task.", "Data and patterns.", "<p>" + mks(["Images are unstructured data, which deep learning uses well", "Many layers can extract hidden features and patterns from large amounts of data"]) + "</p>", None) + req("2 marks", "State", "State two things that supervised learning needs that unsupervised learning does not.", "Data and people.", "<p>" + mks(["Labelled training data with known outputs", "Initial human input to provide or label that data"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on the machine learning categories and deep learning (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Supervised: labelled data.", "Known outputs; predicts future outcomes."),
  ("Unsupervised: unlabelled data.", "Finds hidden patterns and clusters; no human labelling."),
  ("Reinforcement: reward and punishment.", "An agent learns by trial and error in an environment."),
  ("Deep learning: many hidden layers.", "A neural network; a branch of machine learning."),
  ("Reasons for deep learning.", "Unstructured data, large data sets, non-linear, hidden patterns."),
  ("Neural network subset: deep learning.", "Not just 'machine learning'."),
], [
  ("supervised learning", "Learning from labelled data to predict outputs."),
  ("unsupervised learning", "Finding patterns in unlabelled data."),
  ("reinforcement learning", "An agent learning from rewards and punishments."),
  ("deep learning", "Machine learning using neural networks with many hidden layers."),
], [("State", "One short answer."), ("Describe", "Several points on how it works."), ("Explain", "Give reasons and the contrast."), ("Outline", "The main points briefly.")]) + FC

js = AKJS + AK20JS + r'''
function lcg(seed) { let s = seed; return () => ((s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff); }
function pts(seed) { const r = lcg(seed), out = []; for (let i = 0; i < 8; i++) out.push([60 + r() * 140, 40 + r() * 120, 0]); for (let i = 0; i < 8; i++) out.push([320 + r() * 140, 110 + r() * 120, 1]); return out; }
const P = pts(5);
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "labelled training data", "sm");
    P.forEach(([x, y, c], i) => { o += SV.circle(x, y, 8, c ? "dot2" : "dot1"); });
    if (k >= 1) o += SV.text(300, 20, "labels: red = spam, blue = ok", "sm");
    if (k >= 2) o += SV.path("M260,20 L260,260", "ax", { style: "stroke-dasharray:6 5;stroke:var(--accent)" }) + SV.text(262, 275, "learned boundary", "sm");
    if (k >= 3) o += SV.circle(420, 70, 9, "dot4") + SV.text(420, 55, "new?", "sm", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(300, 56, "predicted: ok", "lbl bd t3", { style: "font-size:12px", "text-anchor": "start" }) + SV.text(20, 292, "", "sm"); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 290, label: "Supervised", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "A set of examples with data points (blue and red). At first the system knows only the points.", s: { i: 0 } }, { cap: "Each example comes with a <b>label</b> supplied by people: the known output (ok or spam).", s: { i: 1 } }, { cap: "The system <b>learns a mapping</b> from the inputs to the labels, here a boundary between the two groups.", s: { i: 2 } }, { cap: "A <b>new, unlabelled</b> point arrives.", s: { i: 3 } }, { cap: "The system <b>predicts</b> its label from what it learned.", s: { i: 4 } }].map((x) => ({ cap: x.cap, s: x.s })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "unlabelled data: no known outputs", "sm");
    P.forEach(([x, y, c]) => (o += SV.circle(x, y, 8, k >= 2 ? (c ? "dot2" : "dot1") : "dot3")));
    if (k >= 1) o += SV.circle(130, 100, 5, "dot4") + SV.circle(390, 170, 5, "dot4") + SV.text(130, 128, "centre 1", "sm", { "text-anchor": "middle" }) + SV.text(390, 198, "centre 2", "sm", { "text-anchor": "middle" });
    if (k >= 3) o += SV.rect(40, 30, 180, 150, "ax", { rx: 14, fill: "none", style: "stroke:var(--accent);stroke-dasharray:6 5" }) + SV.rect(300, 90, 180, 160, "ax", { rx: 14, fill: "none", style: "stroke:var(--bad);stroke-dasharray:6 5" }); if (k >= 3) o += SV.text(20, 275, "two clusters found, nobody labelled them", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 290, label: "Unsupervised", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "The data has <b>no labels</b>. The system does not know what the points are.", s: { i: 0 } }, { cap: "It looks for structure: it places some trial group centres.", s: { i: 1 } }, { cap: "Each point joins the nearest group, and the centres move to fit the groups.", s: { i: 2 } }, { cap: "Two <b>clusters</b> are found: hidden patterns discovered with no human help.", s: { i: 3 } }] });
})();
(function () {
  const loop = [["Agent", "chooses an action"], ["Environment", "responds to the action"], ["Feedback", "reward (+) or punishment (−)"], ["Agent", "adjusts how it chooses next time"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(30, 40, 160, 60, k === 0 || k === 3 ? "cell-warn" : "cell", { rx: 10 }) + SV.text(110, 76, "Agent", "lbl bd", { "text-anchor": "middle" }) + SV.rect(330, 40, 160, 60, k === 1 ? "cell-warn" : "cell", { rx: 10 }) + SV.text(410, 76, "Environment", "lbl bd", { "text-anchor": "middle" });
    if (k >= 0) o += SV.path("M190,58 H330", "ax") + SV.arrowHead(330, 58, "r", "arr") + SV.text(260, 50, "action", "sm", { "text-anchor": "middle" });
    if (k >= 2) o += SV.path("M330,86 H190", "ax", { style: "stroke:" + (k === 2 ? "var(--good)" : "var(--muted)") + ";stroke-width:3" }) + SV.arrowHead(190, 86, "l", "arr") + SV.text(260, 112, "reward / punishment", "sm", { "text-anchor": "middle" });
    if (k >= 3) o += SV.text(110, 140, "learns: do more of what earned a reward", "lbl bd t3", { "text-anchor": "start", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 170, label: "Reinforcement", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: loop.map((x, i) => ({ cap: `<b>${x[0]}</b> ${x[1]}.`, s: { i } })) });
})();

(function () {
  let labels = true; const b = $("#sB"); let newPt = [260, 120], cl = null;
  const nearest = () => P.reduce((m, p) => (Math.hypot(p[0] - newPt[0], p[1] - newPt[1]) < Math.hypot(m[0] - newPt[0], m[1] - newPt[1]) ? p : m));
  const kmeans = () => { let c = [[100, 100], [400, 180]]; let asg = P.map(() => 0); for (let it = 0; it < 6; it++) { asg = P.map((p) => (Math.hypot(p[0] - c[0][0], p[1] - c[0][1]) <= Math.hypot(p[0] - c[1][0], p[1] - c[1][1]) ? 0 : 1)); c = [0, 1].map((k) => { const m = P.filter((_, i) => asg[i] === k); return m.length ? [m.reduce((a, p) => a + p[0], 0) / m.length, m.reduce((a, p) => a + p[1], 0) / m.length] : c[k]; }); } return { asg, c }; };
  const paint = () => { let o = ""; const km = kmeans();
    P.forEach(([x, y, c], i) => { const col = labels ? (c ? "dot2" : "dot1") : "dot3"; o += SV.circle(x, y, 8, col); if (!labels) o += SV.circle(x, y, 12, "ax", { fill: "none", style: "stroke:" + (km.asg[i] ? "var(--bad)" : "var(--accent)") + ";stroke-width:2" }); });
    const near = nearest(); if (labels) o += SV.circle(newPt[0], newPt[1], 9, "dot4") + SV.path("M" + newPt[0] + "," + newPt[1] + " L" + near[0] + "," + near[1], "ax", { style: "stroke-dasharray:4 4" });
    $("#sG").innerHTML = `<svg viewBox="0 0 520 260" style="width:520px;max-width:100%;display:block;cursor:crosshair" id="svgS">${o}</svg>`;
    $("#svgS").onclick = (e) => { if (!labels) return; const r = e.currentTarget.getBoundingClientRect(); newPt = [((e.clientX - r.left) / r.width) * 520, ((e.clientY - r.top) / r.height) * 260]; paint(); };
    $("#sV").innerHTML = labels ? `<b>Supervised</b>: the points carry labels (colours). The new point (yellow) is classified as <b>${near[2] ? "red" : "blue"}</b>, the label of its nearest labelled neighbour. Click the graph to move it.` : "<b>Unsupervised</b>: no labels. The computer groups the points itself and finds <b>2 clusters</b> (the rings). It does not know what the groups mean.";
    b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "s") === labels ? "on" : "")); };
  [["s", "Supervised (labels)"], ["u", "Unsupervised (no labels)"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { labels = k === "s"; paint(); }; b.appendChild(x); }); paint();
})();
(function () {
  const prob = [0.2, 0.7, 0.4], q = [0, 0, 0], n = [0, 0, 0]; const rnd = lcg(3); let trials = 0, total = 0; const b = $("#rB");
  const step = () => { const eps = 0.15; let a = rnd() < eps || trials < 3 ? Math.floor(rnd() * 3) : q.indexOf(Math.max(...q)); const r = rnd() < prob[a] ? 1 : 0; n[a]++; q[a] += (r - q[a]) / n[a]; trials++; total += r; };
  const paint = () => { $("#rT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Lever</th><th>Times chosen</th><th>Estimated reward (learned)</th></tr>' + [0, 1, 2].map((i) => `<tr><td>${i + 1}</td><td>${n[i]}</td><td>${n[i] ? q[i].toFixed(2) : "?"}</td></tr>`).join("") + "</table></div>";
    $("#rV").innerHTML = trials ? `After <b>${trials}</b> trials the agent has earned <b>${total}</b> rewards. It chooses the lever with the best estimate most of the time and tries others now and then. The hidden payout rates are 20%, 70% and 40%: lever 2 is best.` : "Press Train. At first the agent tries levers at random."; };
  [["Train 10 trials", 10], ["Train 100 trials", 100], ["Reset", 0]].forEach(([t, k]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = () => { if (!k) { q.fill(0); n.fill(0); trials = 0; total = 0; } else for (let i = 0; i < k; i++) step(); paint(); }; b.appendChild(x); }); paint();
})();
btnTable("mB", "mO", [
  ["Sort photos into known categories using thousands of tagged examples", "Supervised learning", "Labelled data with known outputs"],
  ["Group customers by behaviour with no categories decided", "Unsupervised learning", "Unlabelled data; find clusters"],
  ["A program learns to play a game by playing it many times", "Reinforcement learning", "Rewards and punishments for actions"],
  ["Recognise faces using a neural network with many hidden layers", "Deep learning", "Many layers extract features from large data"],
  ["Predict next month's sales from past sales", "Supervised learning", "Past data with known outcomes"],
  ["Find unusual patterns in network traffic with no labels", "Unsupervised learning", "Hidden patterns in unlabelled data"]
], ["Situation", "Method", "Why"]);
''' + CLASSIFY("cl1", "Which category of machine learning?", ["Supervised", "Unsupervised", "Reinforcement"],
  [("Uses labelled training data", 0), ("Finds hidden clusters in unlabelled data", 1), ("An agent learns from rewards and punishments", 2), ("Needs initial human input to label data", 0), ("Learns by trial and error in an environment", 2), ("Needs no human intervention to find groupings", 1)],
  "Labelled: supervised. Unlabelled: unsupervised. Feedback: reinforcement.") + CLASSIFY("cl2", "Is it a reason for using deep learning?", ["Yes", "No"],
  [("It uses unstructured data well", 0), ("It outperforms other methods with large data sets", 0), ("It finds hidden patterns humans might not see", 0), ("It needs no data at all", 1), ("More hidden layers can give more accurate results", 0), ("It always works best with very small data sets", 1)],
  "Deep learning suits large and unstructured data.") + MATCH([
  ["Supervised learning", "Mapping inputs to outputs from example input–output pairs"], ["Unsupervised learning", "Discovering patterns on its own that were previously undetected"], ["Reinforcement learning", "Learning in an interactive environment by trial and error"], ["Deep learning", "A neural network with many hidden layers, like the brain"], ["Back propagation", "Passing information about errors back through the network"]]) + ORDER(
  "Put the reinforcement learning loop in order.",
  ["The agent chooses an action", "The environment responds", "The agent receives a reward or punishment", "The agent adjusts how it chooses actions", "It tries again and gets better at the task"],
  "Action, response, feedback, adjust, repeat.") + CALC([
  {"q": "How many categories of machine learning are named in the syllabus (supervised, unsupervised, reinforcement)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Three.", "sol": "<b>3</b>."},
  {"q": "A deep learning network has an input layer, 4 hidden layers and an output layer. How many layers in total?", "a": 6, "unit": "", "tol": 0.01, "hint": "1 + 4 + 1.", "sol": "<b>6</b>."},
  {"q": "A supervised data set has 1000 examples and 25% are labelled spam. How many are spam?", "a": 250, "unit": "", "tol": 0.5, "hint": "1000 × 0.25.", "sol": "<b>250</b>."},
  {"q": "An agent gets +1 for a good action and −1 for a bad action. After 7 good and 3 bad actions, what is its total reward?", "a": 4, "unit": "", "tol": 0.01, "hint": "7 − 3.", "sol": "<b>4</b>."},
  {"q": "How many of the three categories (supervised, unsupervised, reinforcement) use labelled training data?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only supervised.", "sol": "<b>1</b>."}]) + MCQ([
  ("Supervised learning uses:", ["Labelled data", "No data", "Only rewards", "Only images"], 0, "Labelled data."),
  ("Which finds hidden patterns in unlabelled data?", ["Supervised", "Unsupervised", "Reinforcement", "None"], 1, "Unsupervised."),
  ("In reinforcement learning an agent receives:", ["Labelled data", "Rewards and punishments", "Passwords", "Nothing"], 1, "Feedback."),
  ("Deep learning is:", ["Part of machine learning", "Unrelated to AI", "A type of storage", "A database"], 0, "A branch of machine learning."),
  ("More hidden layers usually make deep learning:", ["Less effective", "More effective", "Unchanged", "Unusable"], 1, "More effective."),
  ("Which subset of AI uses an artificial neural network?", ["Deep learning", "Sorting", "Compression", "Encryption"], 0, "Deep learning.")], "qz1") + CARDS([
  ("Supervised", "Labelled data; known outputs; predicts future outcomes."), ("Unsupervised", "Unlabelled data; hidden patterns and clusters."), ("Reinforcement", "Agent; environment; reward and punishment; trial and error."), ("Deep learning", "Neural network with many hidden layers."),
  ("Why deep learning", "Unstructured and large data; hidden patterns; non-linear."), ("Make it better", "More hidden layers."), ("AI > ML > DL", "Deep learning is part of machine learning, part of AI."), ("Back propagation", "Errors fed back to adjust weights (18.1.4).")])

build("ac1813", "ac-18-1-3-machine-learning-categories", "Machine Learning and Deep Learning", EYA("18.1.3"),
  "Supervised, unsupervised and reinforcement learning and deep learning, with reasons for using each; animations, a labelled-versus-unlabelled lab, a reinforcement learner and the real Paper 3 questions from 2022 to 2026.",
  dict(sub=CBK("Chapter 18 · Artificial Intelligence, section 18.1 Artificial Intelligence"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
