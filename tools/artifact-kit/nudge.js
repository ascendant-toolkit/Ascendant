
/* ---------- helpers ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });

/* ---------- Watch 1: the default effect ---------- */
function defDraw(s) {
  let o = SV.line(60, 250, 740, 250) + SV.text(62, 24, "Share of people who are donors", "sm");
  const H = (v) => 2.2 * v;
  if (s.a > 0) o += SV.rect(180, 250 - H(30) * s.a, 130, H(30) * s.a, "f2", op(s.a)) + SV.text(245, 250 - H(30) * s.a - 8, "30%", "lbl bd", { "text-anchor": "middle", ...op(s.a) });
  if (s.b > 0) o += SV.rect(440, 250 - H(80) * s.b, 130, H(80) * s.b, "f3", op(s.b)) + SV.text(505, 250 - H(80) * s.b - 8, "80%", "lbl bd", { "text-anchor": "middle", ...op(s.b) });
  o += SV.text(245, 274, "Opt-in", "lbl bd", { "text-anchor": "middle", ...op(s.a) }) + SV.text(505, 274, "Opt-out", "lbl bd", { "text-anchor": "middle", ...op(s.b) });
  return o;
}
Lib.stepper($("#stD"), { w: 780, h: 300, label: "Share of donors under opt-in and opt-out systems in an illustrative model", base: { a: 0, b: 0 }, draw: defDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The set-up.</b> Suppose 60% of people would donate if they made an active choice, and half of all people simply accept whatever the default is. (Illustrative numbers.)", s: { a: 0, b: 0 } },
  { cap: "<b>Opt-in.</b> The default is not to donate. Only those who actively choose and want to donate sign up: 50% × 60% = <b>30%</b>.", s: { a: 1, b: 0 } },
  { cap: "<b>Opt-out.</b> The default is to donate. The 50% who accept the default are donors, and 30% (60% of the 50% who choose) also donate: <b>80%</b>.", s: { a: 1, b: 1 } },
  { cap: "<b>Same freedom, different outcome.</b> Everyone can still choose, nothing is banned and no price changes, but the default moves the donor rate by 50 percentage points. That is what a <b>nudge</b> does.", s: { a: 1, b: 1 } },
] });

/* ---------- Watch 2: the spectrum of tools ---------- */
const TOOLS = [["Do nothing", 70], ["Information", 230], ["Nudge", 390], ["Tax or subsidy", 550], ["Ban", 710]];
function specDraw(s) {
  let o = SV.line(50, 120, 730, 120, "ax") + SV.text(50, 38, "Weaker, cheaper, more freedom", "sm") + SV.text(730, 38, "Stronger, costlier, less freedom", "sm", { "text-anchor": "end" });
  TOOLS.forEach(([t, x], i) => {
    const v = s.n > i ? 1 : 0, hi = s.h === i;
    o += SV.circle(x, 120, hi ? 13 : 9, hi ? "dot3" : "dot1", op(v)) + SV.text(x, i % 2 ? 168 : 82, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
  });
  if (s.h === 2) o += SV.rect(300, 96, 180, 48, "f3", op(1));
  return o;
}
Lib.stepper($("#stS"), { w: 780, h: 210, label: "Policy tools from doing nothing to a ban, with the nudge highlighted", base: { n: 0, h: -1 }, draw: specDraw, tween: 700, dwell: 5200, steps: [
  { cap: "<b>The range.</b> A government facing over-consumption of a demerit good has more options than a tax or a ban.", s: { n: 0, h: -1 } },
  { cap: "<b>Do nothing and information.</b> Leave the market alone, or tell people the facts with labels and campaigns. Cheap, but people may ignore it.", s: { n: 2, h: -1 } },
  { cap: "<b>The nudge.</b> Changes how the choice is presented (defaults, placement, social norms). No price change and no ban, so choice is kept. Often cheap, with an effect that is uncertain.", s: { n: 3, h: 2 } },
  { cap: "<b>Tax or subsidy.</b> Changes the price. Still free choice, but the budget changes. Stronger where demand is elastic.", s: { n: 4, h: 3 } },
  { cap: "<b>Ban.</b> Regulation: choice is removed. Strongest, but costliest to enforce and the least free. Many problems need a mix of these tools.", s: { n: 5, h: 4 } },
] });

/* ---------- Lab 1: defaults ---------- */
function labDef() {
  if (!$("#inr") || !$("#sup")) return;
  const f = +$("#inr").value / 100, t = +$("#sup").value / 100, a = (1 - f) * t * 100, b = (f + (1 - f) * t) * 100;
  $("#d1").textContent = Math.round(a) + "%"; $("#d2").textContent = Math.round(b) + "%"; $("#d3").textContent = "+" + Math.round(b - a) + " points";
  $("#dv").textContent = f === 0 ? "If nobody follows the default, the system makes no difference: both give the same donor rate."
    : `With ${Math.round(f * 100)}% accepting the default and ${Math.round(t * 100)}% in favour, opt-in gives ${Math.round(a)}% donors and opt-out ${Math.round(b)}%. The more people go along with defaults, the bigger the effect of the nudge.`;
  const H = (v) => 1.8 * v;
  let o = SV.line(30, 220, 400, 220);
  [[70, a, "f2", "Opt-in"], [240, b, "f3", "Opt-out"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 220 - H(v), 100, H(v), c) + SV.text(x + 50, 220 - H(v) - 8, Math.round(v) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g1"), { id: "inr", label: "People who just accept the default: ", min: 0, max: 80, step: 10, value: 50, fmt: (v) => v + "%", onInput: labDef });
Lib.slider($("#g2"), { id: "sup", label: "People who would donate if they chose: ", min: 40, max: 80, step: 10, value: 60, fmt: (v) => v + "%", onInput: labDef });

/* ---------- Lab 2: nudge or tax ---------- */
function labTax() {
  if (!$("#nud") || !$("#tax")) return;
  const n = +$("#nud").value, tx = +$("#tax").value, price = 2 + tx / 100;
  const cut = 0.6 * (tx / 2);
  const qq = Math.max(0, Math.round(100 * (1 - n / 100) * (1 - cut / 100)));
  $("#t1").textContent = qq; $("#t2").textContent = "$" + price.toFixed(2); $("#t3").textContent = "$" + (qq * tx / 100).toFixed(2); $("#t4").textContent = tx > 0 ? "Budget only" : "No";
  $("#tv").textContent = n === 0 && tx === 0 ? "No policy: 100 drinks a day."
    : n > 0 && tx === 0 ? `The nudge alone cuts sales to ${qq} drinks, with no tax revenue and no price rise. If the nudge fades, sales may drift back towards 100.`
    : n === 0 ? `A ${tx}c tax lifts the price to $${price.toFixed(2)} and cuts sales to ${qq}, and raises $${(qq * tx / 100).toFixed(2)} a day. Demand is inelastic, so the fall is small against the price rise.`
    : `Together they cut sales to ${qq}. The nudge cuts demand without a price rise and the tax adds revenue, which is why governments often combine the two tools.`;
  const H = (v) => 1.8 * v;
  let o = SV.line(30, 220, 400, 220);
  [[70, 100, "f1", "No policy"], [240, qq, "f3", "With policy"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 220 - H(v), 100, H(v), c) + SV.text(x + 50, 220 - H(v) - 8, Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labT").innerHTML = o;
}
Lib.slider($("#g3"), { id: "nud", label: "Nudge: fall in demand it causes: ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labTax });
Lib.slider($("#g4"), { id: "tax", label: "Tax per drink (cents): ", min: 0, max: 60, step: 10, value: 0, fmt: (v) => v + "c", onInput: labTax });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "What type of policy is each one?",
  buckets: [{ label: "A nudge" }, { label: "A tax or subsidy" }, { label: "Regulation or ban" }],
  items: [
    { text: "Opt-out organ donation", b: 0 }, { text: "Fruit placed at eye level in a canteen", b: 0 }, { text: "A letter saying most people have already paid their tax", b: 0 }, { text: "Automatic enrolment in a pension", b: 0 }, { text: "A catchy public song on hand-washing", b: 0 },
    { text: "A tax on sugary drinks", b: 1 }, { text: "A subsidy on fresh fruit", b: 1 }, { text: "A 5p charge for plastic bags", b: 1 },
    { text: "A ban on new petrol cars", b: 2 }, { text: "Compulsory motorcycle helmets", b: 2 }, { text: "Heavy fines for tax evasion", b: 2 }, { text: "Zero tolerance for drink-driving", b: 2 },
  ], done: "A nudge keeps free choice and does not change the price; a charge is a price, and a ban or fine is regulation.",
});
Lib.match($("#m2"), { prompt: "Match each nudge to the behaviour it uses.", pairs: [
  ["Opt-out pension scheme", "Inertia and present bias"],
  ["\"Most of your neighbours pay on time\"", "Social norms"],
  ["Sweets removed from the supermarket till", "Salience and choice architecture"],
  ["\"You will lose $50 if you do not act\"", "Loss aversion and framing"],
  ["Text reminder before an appointment", "Limited attention"],
], done: "Naming the behaviour is what turns a description into analysis." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Nudge", "A change in how choices are presented that influences behaviour without forcing it"],
  ["Default", "The option that applies if a person does nothing"],
  ["Libertarian paternalism", "Steering people towards better choices while leaving them free to choose"],
  ["Choice architecture", "The way options are laid out and presented"],
  ["Present bias", "Valuing now over later, so under-saving"],
  ["Social norm", "What people think most others do"],
  ["Inertia", "Sticking with the current option because changing takes effort"],
  ["Sludge", "Friction that makes a good choice harder, such as complex forms"],
], done: "Eight words for behavioural insights." });
Lib.order($("#o1"), { prompt: "Put the explanation of an opt-out pension default in order.", items: [
  "Many people under-save because of present bias and inertia",
  "Under opt-in, most people never fill in the form, so participation is low",
  "The government makes enrolment the default and allows opting out",
  "Most people stay in the scheme because changing takes effort",
  "Participation and saving rise without a tax, subsidy or ban",
  "Evaluate: the default rate may be low, and some groups are not reached",
], done: "A reliable structure for explaining any default." });
Lib.calc($("#c1"), { qs: [
  { q: "Under opt-in, 40% of workers join a pension scheme. After opt-out is introduced, 85% remain in. By how many percentage points does participation rise?", a: 45, sol: "85 − 40 = <b>45 percentage points</b>." },
  { q: "A town has 20 000 eligible workers. How many more workers are in the scheme under opt-out?", a: 9000, hint: "45% of 20 000.", sol: "0.45 × 20 000 = <b>9 000</b>." },
  { q: "A tax letter trial finds 70% pay on time with the standard letter and 77% with a social-norm letter. What is the percentage increase in on-time payment (%)?", a: 10, sol: "(77 − 70) ÷ 70 × 100 = <b>10%</b>." },
  { q: "The government sends 400 000 letters and each extra on-time payer saves it $15 in chasing costs. How many extra people pay on time at 7 percentage points higher?", a: 28000, sol: "7% × 400 000 = <b>28 000</b>." },
  { q: "What is the total saving ($)?", a: 420000, sol: "28 000 × $15 = <b>$420 000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an example of a nudge?", opts: ["A tax on sugary drinks", "A ban on smoking indoors", "An opt-out organ donation system", "A subsidy for fruit"], a: 2, why: "Changing the default influences choice without forcing it or changing the price." },
  { q: "Why is a nudge described as 'libertarian paternalism'?", opts: ["It bans harmful goods for people's own good", "It steers people to better choices but leaves them free to choose", "It lets the market decide with no government role", "It uses taxes to raise revenue"], a: 1, why: "Paternalism because the state steers; libertarian because choice is not removed." },
  { q: "Which is the best reason why a nudge may be less effective than a ban?", opts: ["It raises the price of the good", "People can ignore it", "It needs a law", "It always costs more"], a: 1, why: "People remain free to choose otherwise, so the effect could be small." },
  { q: "A 5p charge on plastic bags is best described as:", opts: ["A pure nudge", "A price change, closer to a tax", "A ban", "A subsidy"], a: 1, why: "A charge changes the price, so it is not a pure nudge, even though it changes behaviour." },
  { q: "Which is a likely limit of using a nudge to reduce smoking?", opts: ["Nicotine is addictive, so demand may be inelastic to a nudge", "Nudges cost more than a ban", "Nudges cut tax revenue to zero", "Smokers are always rational"], a: 0, why: "Addiction weakens the effect of changing how choices are presented." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Nudge theory", "Influencing behaviour by persuasion, example or changing how choices are presented, without forcing it or changing prices."],
  ["Behavioural economics", "Studies how real people decide, including biases, habits and social influence."],
  ["Default", "The option applied if no choice is made; opt-out schemes use it."],
  ["Libertarian paternalism", "Steering people towards better choices while leaving them free to choose."],
  ["Present bias", "Overvaluing the present, so under-saving and over-consuming."],
  ["Loss aversion", "Losses feel bigger than equal gains."],
  ["Choice architecture", "How options are laid out; salience and placement matter."],
  ["Sludge", "Friction that makes good choices harder."],
] });

/* ---------- Past paper multiple choice (Paper 3) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2020 · 32 · Q13] Charities leave plastic bags at homes for unwanted clothes; one charity adds a note thanking the householder for the donation. What best describes this charity's approach?", opts: ["game theory", "monopoly behaviour", "non-price competition", "nudge theory"], a: 3, why: "A thank-you note uses persuasion and social reward to influence behaviour, with no price change or compulsion." },
  { q: "[Oct/Nov 2020 · 32 · Q13] What is the essential feature of nudge theory?", opts: ["the aim of satisficing", "the establishing of a legal requirement", "the existence of a contestable market", "the idea of persuasion"], a: 3, why: "Nudges work by persuasion and example, not by legal requirement." },
  { q: "[Feb/March 2021 · 32 · Q14] A sign beside a busy road says the road was recently cleared of 17 bags of litter and that clearing litter puts lives at risk. What is this an example of?", opts: ["free good", "government regulation", "merit good", "nudge theory"], a: 3, why: "The sign uses information and persuasion to change behaviour, with no ban or fine." },
  { q: "[May/June 2022 · 31 and 33 · Q15] What is an example of 'nudge' theory when applied to encouraging healthy eating?", opts: ["advertising the benefits of healthy eating", "increasing tax on sugary foods", "introducing a subsidy for fruit growers", "supermarkets putting fruit near cash registers"], a: 3, why: "Placement changes the choice environment, but leaves people free. Advertising informs but is not a change to the presentation of choices." },
  { q: "[Feb/March 2022 · 32 · Q14] What would be an example of 'nudge' theory?", opts: ["a subsidy on fresh fruit to increase demand", "a unit tax on unhealthy food to reduce demand", "banning all unhealthy food to reduce demand", "putting fresh fruit at eye level in shops to increase demand"], a: 3, why: "Eye-level placement is a nudge. A subsidy and a tax change prices, and a ban removes choice." },
  { q: "[May/June 2022 · 32 · Q14] What is not an example of the application of 'nudge' theory?", opts: ["A coffee chain offers a larger coffee if customers bring a reusable cup", "A government imposes an indirect tax on sugary snacks", "A government introduces an opt-out system for organ donation", "A restaurant chain introduces smaller main courses to reduce food waste"], a: 1, why: "A tax changes the price, so it is not a nudge." },
  { q: "[May/June 2023 · 31 and 33 · Q13] In 2020 the governor of California ordered a ban on the sale of new petrol and diesel vehicles from 2035. Which type of government policy is this?", opts: ["a nudge", "a permit to pollute", "nationalisation", "regulation"], a: 3, why: "A legal ban is regulation. It removes choice." },
  { q: "[May/June 2025 · 31 and 33 · Q13] What is an example of 'nudge' theory as applied to the prevention of tax evasion?", opts: ["employing an extensive administration to ensure detection of evasion", "imposing heavy penalties on those who do evade tax", "providing information to taxpayers about the undesirable effects of tax evasion", "requiring employers to inform the tax authorities of workers' pay"], a: 2, why: "Information and persuasion are the nudge. Detection, penalties and compulsion are enforcement." },
  { q: "[May/June 2025 · 34 · Q8] A government wishes to discourage tax avoidance. Which policy would be an example of the behavioural approach of nudge theory?", opts: ["compelling direct tax deduction by employers", "making random inspections of individual tax records", "providing information on how the tax is spent by the government", "using penalties such as fines and imprisonment for tax avoidance"], a: 2, why: "Telling people how their tax is spent persuades; the other options compel or punish." },
] });

labDef(); labTax();
