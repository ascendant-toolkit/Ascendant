/* ---------- shared geometry: price p and quantity q both 0..100 ---------- */
const OP = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const X = (q) => 70 + q * 6.4, Y = (p) => 310 - p * 2.4;
const lt = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...OP(v) });
const gs = (v) => ({ style: `stroke-width:1.4;opacity:${0.75 * Math.max(0, Math.min(1, v))}` });
const lineAt = (c, q) => c[0] + c[1] * q;
const seg = (c) => { const [a, b] = c; let lo = 0, hi = 100; if (b > 0) { lo = Math.max(lo, (4 - a) / b); hi = Math.min(hi, (96 - a) / b); } else { lo = Math.max(lo, (96 - a) / b); hi = Math.min(hi, (4 - a) / b); } return [lo, hi]; };
function curve(c, cls, v, name, tcls) {
  const [lo, hi] = seg(c);
  return SV.line(X(lo), Y(lineAt(c, lo)), X(hi), Y(lineAt(c, hi)), cls, OP(v)) + (name ? lt(X(hi) + 6, Y(lineAt(c, hi)) + 4, name, tcls, v) : "");
}
const guide = (q, p, pn, qn, v, qdy = 16) => SV.line(X(q), Y(p), X(q), Y(0), "ax", gs(v)) + SV.line(X(0), Y(p), X(q), Y(p), "ax", gs(v)) + (pn ? SV.text(62, Y(p) + 4, pn, "sm", { "text-anchor": "end", ...OP(v) }) : "") + (qn ? SV.text(X(q), Y(0) + qdy, qn, "sm", { "text-anchor": "middle", ...OP(v) }) : "");
function vArrow(x, p1, p2, cls, v) {
  const y1 = Y(p1), y2 = Y(p2), top = Math.min(y1, y2), bot = Math.max(y1, y2);
  return `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x, top + 8, x, bot - 8, cls)}${SV.arrowHead(x, top, "u", cls === "c4" ? "dot4" : "dot3")}${SV.arrowHead(x, bot, "d", cls === "c4" ? "dot4" : "dot3")}</g>`;
}
const axesSvg = (xl) => SV.line(70, Y(0), 720, Y(0), "ax") + SV.line(70, Y(0), 70, 52, "ax") + SV.text(824, Y(0) + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(76, 46, "Price, cost, benefit ($)", "sm");
function chips(ph) {
  const T = ["1 · Cause", "2 · Problem", "3 · Solution"], C = ["f1", "f2", "f3"];
  return T.map((t, i) => { const a = Math.max(0, 1 - Math.abs(ph - (i + 1))); return SV.rect(70 + i * 168, 6, 156, 28, C[i], { rx: 14, opacity: 0.12 + 0.6 * a }) + SV.text(148 + i * 168, 25, t, "lbl bd", { "text-anchor": "middle", opacity: 0.55 + 0.45 * a }); }).join("");
}

/* ---------- the five scenarios ----------
   D, S are the private curves [intercept, slope]; ex the social curve that is revealed; sgn +1 tax, -1 subsidy; Qs, Ps the social optimum;
   N the new market equilibrium after the fix; tri the welfare loss triangle; tl where the intervention label sits (q, p). */
const D0 = [90, -0.8], S0 = [10, 0.8];
const SC = [
  { key: "A", btn: "Pollution from production", x: "Quantity of electricity", Dn: "D = MPB = MSB", Sn: "S = MPC", exn: "MSC", exl: "MEC", ex: [30, 0.8], side: "S", coin: true, iv: "tax", sgn: 1, ivn: "S + tax",
    Q1: 50, P1: 50, Qs: 37.5, Ps: 60, N: [37.5, 60], tri: [[37.5, 60], [50, 70], [50, 50]], tl: [41.5, 50], ivl: "tax",
    caps: [
      "<b>Cause (1/2):</b> a power station sells electricity. It counts only what it pays itself, its marginal private cost, so <b>S = MPC</b>. Consumers' demand is the marginal private benefit, <b>D = MPB</b>, which here equals the marginal social benefit (MSB).",
      "<b>Cause (2/2):</b> burning fuel pollutes the air and nearby residents bear the cost without being paid. This is a <b>marginal external cost (MEC)</b> of $20 a unit. Adding it to MPC gives the <b>marginal social cost, MSC</b>, which lies $20 above S at every quantity.",
      "<b>Problem (1/3):</b> the free market ignores the MEC. It clears where MPB = MPC, at <b>Q1 = 50</b> and a price of P1 = $50.",
      "<b>Problem (2/3):</b> the socially optimum output is where <b>MSB = MSC</b>, at <b>Q* = 37.5</b> and P* = $60. Q* is below Q1.",
      "<b>Problem (3/3):</b> between Q* and Q1 each unit costs society more (MSC) than it is worth to buyers (MSB). The shaded triangle (WL) is the <b>welfare loss</b>: the market overproduces by 12.5 units.",
      "<b>Solution (1/2):</b> the government puts an <b>indirect tax equal to the MEC</b> ($20 a unit) on the producer. Costs rise by the tax at every quantity, so supply shifts up and to the left, from S to S + tax. The firm now pays for the harm: the externality is <b>internalised</b>.",
      "<b>Solution (2/2):</b> S + tax now lies on MSC and cuts demand at <b>Q* = 37.5</b>. The welfare loss has gone. Buyers pay $60, of which $20 is tax, so the firm keeps $40 a unit. <i>Evaluate:</i> the MEC is hard to measure, and the tax could be passed on to consumers or push production abroad."] },
  { key: "B", btn: "Second-hand smoke (consumption)", x: "Quantity of cigarettes", Dn: "D = MPB", Sn: "S = MPC = MSC", exn: "MSB", exl: "MEC", ex: [70, -0.8], side: "D", coin: false, iv: "tax", sgn: 1, ivn: "S + tax",
    Q1: 50, P1: 50, Qs: 37.5, Ps: 40, N: [37.5, 60], tri: [[37.5, 40], [50, 30], [50, 50]], tl: [41.5, 50], ivl: "tax", p2: "P2",
    caps: [
      "<b>Cause (1/2):</b> smokers buy cigarettes by comparing their own benefit (<b>D = MPB</b>) with the price. Supplying cigarettes costs firms <b>MPC</b>, and here that is also the cost to society (MSC), because the externality arises in <i>consumption</i>.",
      "<b>Cause (2/2):</b> smoking harms bystanders through second-hand smoke: a <b>marginal external cost of $20</b> a unit. Society therefore values each cigarette at less than the smoker does, so <b>MSB = MPB − MEC</b>, below D at every quantity.",
      "<b>Problem (1/3):</b> buyers ignore the harm to others. The market clears where MPB = MPC, at <b>Q1 = 50</b> and P1 = $50.",
      "<b>Problem (2/3):</b> the socially optimum quantity is where <b>MSB = MSC</b>, at <b>Q* = 37.5</b>, with a social price of P* = $40. Q* is below Q1.",
      "<b>Problem (3/3):</b> between Q* and Q1 the cost of each unit (MSC) is above its value to society (MSB). The shaded triangle (WL) is the <b>welfare loss</b>: 12.5 units are over-consumed.",
      "<b>Solution (1/2):</b> the government puts an <b>indirect tax of $20</b> a unit, equal to the MEC at Q*, on cigarettes. Supply shifts up and to the left, from S to S + tax, and the price smokers face rises.",
      "<b>Solution (2/2):</b> S + tax meets demand (MPB) at <b>Q* = 37.5</b>, so the welfare loss has gone. Smokers pay P2 = $60, of which $20 is tax, and sellers keep $40, the social price P*. <i>Evaluate:</i> addiction could make demand inelastic, and the tax is regressive."] },
  { key: "C", btn: "Vaccination (positive consumption)", x: "Quantity of vaccinations", Dn: "D = MPB", Sn: "S = MPC = MSC", exn: "MSB", exl: "MEB", ex: [110, -0.8], side: "D", coin: false, iv: "sub", sgn: -1, ivn: "S − subsidy",
    Q1: 50, P1: 50, Qs: 62.5, Ps: 60, N: [62.5, 40], tri: [[62.5, 60], [50, 70], [50, 50]], tl: [65.5, 55], ivl: "subsidy", p2: "P2",
    caps: [
      "<b>Cause (1/2):</b> people choose whether to be vaccinated by weighing their own benefit (<b>D = MPB</b>) against the price. Supplying vaccinations costs <b>MPC</b>, which is also the cost to society (MSC).",
      "<b>Cause (2/2):</b> each vaccination also lowers the chance that other people catch the disease: a <b>marginal external benefit (MEB)</b> of $20. So <b>MSB = MPB + MEB</b>, above D at every quantity.",
      "<b>Problem (1/3):</b> buyers ignore the benefit to others. The market clears where MPB = MPC, at <b>Q1 = 50</b> and P1 = $50.",
      "<b>Problem (2/3):</b> the socially optimum quantity is where <b>MSB = MSC</b>, at <b>Q* = 62.5</b>, with P* = $60. Q* is above Q1.",
      "<b>Problem (3/3):</b> between Q1 and Q* each vaccination is worth more to society (MSB) than it costs (MSC), but it is not bought. The shaded triangle (WL) is the <b>welfare loss</b>: the good is under-consumed by 12.5 units.",
      "<b>Solution (1/2):</b> the government pays a <b>subsidy of $20</b> a unit, equal to the MEB. Firms' costs fall by the subsidy at every quantity, so supply shifts down and to the right, from S to S − subsidy.",
      "<b>Solution (2/2):</b> S − subsidy meets demand (MPB) at <b>Q* = 62.5</b>, so the welfare loss has gone. Patients pay P2 = $40, and providers receive $60 (P*) once the $20 subsidy is added. <i>Evaluate:</i> the subsidy costs the taxpayer about $1,250 and the MEB is hard to measure."] },
  { key: "D", btn: "R&D spillovers (positive production)", x: "Quantity of research projects", Dn: "D = MPB = MSB", Sn: "S = MPC", exn: "MSC", exl: "MEB", ex: [-10, 0.8], side: "S", coin: true, iv: "sub", sgn: -1, ivn: "S − subsidy",
    Q1: 50, P1: 50, Qs: 62.5, Ps: 40, N: [62.5, 40], tri: [[62.5, 40], [50, 50], [50, 30]], tl: [65.5, 55], ivl: "subsidy",
    caps: [
      "<b>Cause (1/2):</b> a firm decides how much research to do by weighing its own costs (<b>S = MPC</b>) against what it gains (<b>D = MPB</b>, equal here to the marginal social benefit, MSB).",
      "<b>Cause (2/2):</b> research spills over: rivals copy and build on the findings without paying for them. That is a <b>marginal external benefit (MEB)</b> of $20 in production, so the cost to society is lower than the firm's: <b>MSC = MPC − MEB</b>, below S at every quantity.",
      "<b>Problem (1/3):</b> the firm ignores the spillover and clears where MPB = MPC, at <b>Q1 = 50</b> and P1 = $50.",
      "<b>Problem (2/3):</b> the socially optimum quantity is where <b>MSB = MSC</b>, at <b>Q* = 62.5</b>, with P* = $40. Q* is above Q1.",
      "<b>Problem (3/3):</b> between Q1 and Q* the social cost of research (MSC) is below its social benefit (MSB), but the firm does not do it. The shaded triangle (WL) is the <b>welfare loss</b>: research is under-provided by 12.5 units.",
      "<b>Solution (1/2):</b> the government gives a <b>subsidy of $20</b> a unit, equal to the MEB, to the firm. The firm's marginal cost falls by the subsidy, so supply shifts down and to the right, from S to S − subsidy.",
      "<b>Solution (2/2):</b> S − subsidy now lies on MSC and meets demand at <b>Q* = 62.5</b>, so the welfare loss has gone. <i>Evaluate:</i> spillovers are hard to measure, and the firm might have done the research anyway, which would waste the subsidy."] },
  { key: "E", btn: "Pollution: tradable permits", x: "Quantity of electricity", Dn: "D = MPB = MSB", Sn: "S = MPC", exn: "MSC", exl: "MEC", ex: [30, 0.8], side: "S", coin: false, iv: "cap", sgn: 1, ivn: "Permit cap",
    Q1: 50, P1: 50, Qs: 37.5, Ps: 60, N: [37.5, 60], tri: [[37.5, 60], [50, 70], [50, 50]], tl: [41, 50], ivl: "permit",
    caps: [
      "<b>Cause (1/2):</b> the same power station as the first case. It counts only its private cost, <b>S = MPC</b>, against consumers' demand, <b>D = MPB = MSB</b>.",
      "<b>Cause (2/2):</b> its pollution imposes a <b>marginal external cost of $20</b> a unit on others, so <b>MSC = MPC + MEC</b>, above S at every quantity.",
      "<b>Problem (1/3):</b> the market clears where MPB = MPC, at <b>Q1 = 50</b> and P1 = $50.",
      "<b>Problem (2/3):</b> the socially optimum output is where MSB = MSC, at <b>Q* = 37.5</b> and P* = $60.",
      "<b>Problem (3/3):</b> between Q* and Q1 each unit costs more than it is worth, so the shaded triangle (WL) is a <b>welfare loss</b>: 12.5 units of overproduction.",
      "<b>Solution (1/2):</b> instead of a tax, the government sets a <b>cap at Q* = 37.5</b> and issues permits for exactly that much output, which firms may trade. Supply becomes vertical at the cap: nobody may produce more without a permit.",
      "<b>Solution (2/2):</b> demand meets the cap at <b>Q* = 37.5</b> and a price of $60. The welfare loss has gone. The scarce permits sell for about $20 each, the same as the tax, and firms that find cutting pollution cheapest sell permits to those that find it dearer. <i>Evaluate:</i> the cap has to be set accurately and monitored."] },
  { key: "F", btn: "Vaccination: information campaign", x: "Quantity of vaccinations", Dn: "D = MPB", Sn: "S = MPC = MSC", exn: "MSB", exl: "MEB", ex: [110, -0.8], side: "D", coin: true, iv: "info", sgn: 0, ivn: "D2 (= MSB)",
    Q1: 50, P1: 50, Qs: 62.5, Ps: 60, N: [62.5, 60], tri: [[62.5, 60], [50, 70], [50, 50]], tl: [65.5, 55], ivl: "",
    caps: [
      "<b>Cause (1/2):</b> people choose whether to be vaccinated by weighing their own benefit (<b>D = MPB</b>) against the price. Supplying vaccinations costs <b>MPC</b>, which is also the cost to society (MSC).",
      "<b>Cause (2/2):</b> each vaccination also protects other people: a <b>marginal external benefit (MEB)</b> of $20, so <b>MSB = MPB + MEB</b>. Many people also underestimate the private benefit of vaccination (<b>information failure</b>), which is why it is called a <b>merit good</b>.",
      "<b>Problem (1/3):</b> people act on their own, incomplete view of the benefit. The market clears where MPB = MPC, at <b>Q1 = 50</b> and P1 = $50.",
      "<b>Problem (2/3):</b> the socially optimum quantity is where <b>MSB = MSC</b>, at <b>Q* = 62.5</b>, with P* = $60. Q* is above Q1.",
      "<b>Problem (3/3):</b> between Q1 and Q* each vaccination is worth more to society than it costs, but it is not bought. The shaded triangle (WL) is the <b>welfare loss</b>: under-consumption of 12.5 units.",
      "<b>Solution (1/2):</b> the government runs an <b>information campaign</b> (advertising, education, reminders) that shows people the full benefits. People now value vaccination more, so <b>demand (MPB) shifts up and to the right</b>, from D to D2. Nothing is paid to firms: the aim is to change what consumers choose.",
      "<b>Solution (2/2):</b> if the campaign is successful, D2 lies on MSB and meets supply at <b>Q* = 62.5</b>, so the welfare loss has gone. Unlike a subsidy, the price does not fall. <i>Evaluate:</i> it is cheaper per head and respects choice, but it is hard to know how far demand will move, effects could fade, and it could take time."] },
];

function scnDraw(c, s) {
  const [Qs, Ps] = [c.Qs, c.Ps];
  let o = chips(s.ph) + axesSvg(c.x);
  o += curve(D0, "c1", 1, c.Dn, "t1") + curve(S0, "c2", 1, c.Sn, "t2");
  o += curve(c.ex, "c3", s.e, c.exn, "t3").replace(/(<text[^>]*?)opacity="[^"]*"/, (m, a) => (c.coin ? a + `opacity="${Math.max(0, Math.min(1, s.e * (1 - s.m)))}"` : m));
  // external cost or benefit bracket, drawn between the private and social curve
  const base = c.side === "S" ? S0 : D0, qb = 20, ym = lineAt(base, 22.3) + (lineAt(c.ex, 22.3) - lineAt(base, 22.3)) / 2;
  o += vArrow(X(qb), lineAt(base, qb), lineAt(c.ex, qb), "c3", s.br) + lt(X(qb) + 14, Y(ym) + 4, c.exl, "t3", s.br);
  if (s.w > 0) {
    const t = c.tri, cx = (t[0][0] + t[1][0] + t[2][0]) / 3, cy = (t[0][1] + t[1][1] + t[2][1]) / 3;
    o += SV.poly(t.map(([q, p]) => [X(q), Y(p)]), "f2", { style: `opacity:${Math.min(1, s.w) * 0.5}` }) + SV.text(X(cx), Y(cy) + 4, "WL", "lbl bd t2", { "text-anchor": "middle", ...OP(s.w) });
  }
  // private equilibrium
  o += guide(c.Q1, c.P1, "P1", "Q1", s.pg) + SV.circle(X(c.Q1), Y(c.P1), 6, "dot2", OP(s.pg));
  // social optimum
  o += guide(Qs, Ps, "P*", "Q*", s.sg) + SV.circle(X(Qs), Y(Ps), 6, "dot3", OP(s.sg));
  // the fix
  if (s.m > 0) {
    if (c.iv === "cap") {
      const top = lineAt(S0, Qs) + (96 - lineAt(S0, Qs)) * s.m;
      o += SV.line(X(Qs), Y(lineAt(S0, Qs)), X(Qs), Y(top), "c4", OP(Math.min(1, s.m * 3))) + lt(X(Qs) + 8, Y(96) + 4, c.ivn, "t4", s.m);
    } else if (c.iv === "info") {
      o += curve([D0[0] + 20 * s.m, D0[1]], "c4", Math.min(1, s.m * 3), c.ivn, "t4").replace(/(<text[^>]*?)opacity="[^"]*"/, (m, a) => a + `opacity="${s.m > 0.98 ? 1 : 0}"`);
    } else {
      o += curve([S0[0] + c.sgn * 20 * s.m, S0[1]], "c4", Math.min(1, s.m * 3), c.ivn, "t4").replace(/(<text[^>]*?)opacity="[^"]*"/, (m, a) => a + `opacity="${s.m > 0.98 ? 1 : 0}"`);
    }
  }
  if (s.nd > 0) {
    const [nq, np] = c.N;
    if (c.p2) o += SV.line(X(0), Y(np), X(nq), Y(np), "ax", gs(s.nd)) + SV.text(62, Y(np) + 4, c.p2, "sm", { "text-anchor": "end", ...OP(s.nd) });
    o += SV.circle(X(nq), Y(np), 8, "dot4", OP(s.nd * 0.5)) + SV.circle(X(nq), Y(np), 5, "dot3", OP(s.nd));
    const lo = lineAt(S0, Qs), hi = lo + c.sgn * 20, bx = X(Qs) + 6;
    if (c.iv !== "info") o += vArrow(bx, lo, hi, "c4", s.nd) + lt(X(Qs) + 16, Y(c.tl[1]) + 4, c.ivl, "t4", s.nd);
  }
  return o;
}
const BASE0 = { ph: 1, e: 0, br: 0, pg: 0, sg: 0, w: 0, m: 0, nd: 0 };
const STEPS = [
  { ph: 1 }, { ph: 1, e: 1, br: 1 }, { ph: 2, e: 1, br: 1, pg: 1 }, { ph: 2, e: 1, br: 1, pg: 1, sg: 1 }, { ph: 2, e: 1, br: 1, pg: 1, sg: 1, w: 1 },
  { ph: 3, e: 1, br: 0.4, pg: 0.45, sg: 1, w: 0.6, m: 1 }, { ph: 3, e: 1, br: 0.4, pg: 0.45, sg: 1, w: 0, m: 1, nd: 1 },
];
const scnBox = $("#scnBox"), scnB = $("#scnBtns");
SC.forEach((c, i) => {
  const d = document.createElement("div"); d.id = "scn" + c.key; d.hidden = i > 0; scnBox.appendChild(d);
  Lib.stepper(d, { w: 840, h: 345, label: c.btn + ": cause, problem and solution", base: BASE0, draw: (s) => scnDraw(c, s), tween: 800, dwell: 6400, steps: STEPS.map((s, k) => ({ cap: c.caps[k], s })) });
  const b = document.createElement("button"); b.className = "b" + (i ? "" : " pri"); b.textContent = (i + 1) + " · " + c.btn; b.onclick = () => { SC.forEach((z, k) => { $("#scn" + z.key).hidden = k !== i; }); $$("button", scnB).forEach((x, k) => x.classList.toggle("pri", k === i)); }; scnB.appendChild(b);
});

/* ---------- labs: set the tax or subsidy yourself ---------- */
const labA = { svg: "#labA", id: "#a", x: "Quantity of electricity", Qs: 37.5, Ps: 60, soc: [30, 0.8], Qn: (t) => (80 - t) / 1.6, sh: (t) => [10 + t, 0.8], over: true, dir: "above", what: "tax", mx: "cost" };
const labB = { svg: "#labB", id: "#b", x: "Quantity of vaccinations", Qs: 62.5, Ps: 60, soc: [110, -0.8], Qn: (s) => (80 + s) / 1.6, sh: (s) => [10 - s, 0.8], over: false, dir: "below", what: "subsidy", mx: "benefit" };
function labDraw(o, v) {
  const Qn = o.Qn(v), other = o === labA ? [30, 0.8] : [110, -0.8], priv = o === labA ? D0 : S0;
  const wl = 0.8 * (Qn - o.Qs) ** 2, d = Math.abs(Qn - o.Qs), np = lineAt(D0, Qn);
  let s = SV.line(70, Y(0), 720, Y(0), "ax") + SV.line(70, Y(0), 70, 52, "ax") + SV.text(824, Y(0) + 26, o.x, "sm", { "text-anchor": "end" }) + SV.text(76, 46, "Price, cost, benefit ($)", "sm");
  s += curve(D0, "c1", 1) + curve(S0, "c2", 1) + curve(o.soc, "c3", 1);
  if (v > 0) s += curve(o.sh(v), "c4", 1);
  if (wl > 0.5) s += SV.poly([[o.Qs, o.Ps], [Qn, lineAt(other, Qn)], [Qn, lineAt(priv, Qn)]].map(([q, p]) => [X(q), Y(p)]), "f2", { style: "opacity:.5" });
  s += guide(o.Qs, o.Ps, "", d < 0.3 ? "Q* = Q2" : "Q*", 1, 16) + SV.line(X(Qn), Y(np), X(Qn), Y(0), "ax", gs(1)) + SV.line(X(0), Y(np), X(Qn), Y(np), "ax", gs(1));
  s += SV.circle(X(o.Qs), Y(o.Ps), 5, "dot3") + SV.circle(X(Qn), Y(np), 6, "dot4");
  if (d >= 0.3) s += SV.text(X(Qn), Y(0) + (d < 6 ? 31 : 16), "Q2", "sm", { "text-anchor": "middle" });
  s += SV.text(62, Y(np) + 4, "P2", "sm", { "text-anchor": "end" });
  $(o.svg).innerHTML = s;
  const short = o.over ? Qn > o.Qs : Qn < o.Qs;
  $(o.id + "1").textContent = Qn.toFixed(1) + (d < 0.3 ? " (= Q*)" : "");
  $(o.id + "2").textContent = wl < 0.5 ? "None" : "$" + Math.round(wl);
  $(o.id + "3").textContent = d < 0.3 ? "Just right: the " + o.what + " equals the marginal external " + o.mx + " at Q*, so output is socially optimum and there is no welfare loss." : short ? "Not enough: output is still " + o.dir + " Q*, so some welfare loss remains." : "Too much: output has overshot Q*, so a new welfare loss appears on the other side.";
}
const legend = (a) => a.map(([c, t]) => `<span style="display:inline-flex;gap:6px;align-items:center;margin-right:12px"><i style="width:22px;height:4px;border-radius:2px;background:var(--${c})"></i>${t}</span>`).join("");
$("#legA").innerHTML = legend([["accent", "D = MPB = MSB"], ["bad", "S = MPC"], ["good", "MSC"], ["warn", "S + tax"]]);
$("#legB").innerHTML = legend([["accent", "D = MPB"], ["bad", "S = MPC = MSC"], ["good", "MSB"], ["warn", "S − subsidy"]]);
Lib.slider($("#g1"), { id: "tx", label: "Tax per unit ($) ", min: 0, max: 40, step: 1, value: 0, fmt: (v) => "$" + v, onInput: (v) => labDraw(labA, v) });
Lib.slider($("#g2"), { id: "sb", label: "Subsidy per unit ($) ", min: 0, max: 40, step: 1, value: 0, fmt: (v) => "$" + v, onInput: (v) => labDraw(labB, v) });

/* ---------- practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is the externality negative or positive? The right fix follows from the answer.", buckets: [{ label: "Negative: tax, permits or regulation" }, { label: "Positive: subsidy or provision" }], items: [
  { text: "A chemical works releases fumes into a nearby town", b: 0 }, { text: "Each extra driver adds to delay for everyone else on the road", b: 0 },
  { text: "Staff trained by one firm later share their skills with other firms", b: 1 }, { text: "Smokers breathing out smoke around non-smokers", b: 0 },
  { text: "Higher vaccination rates mean fewer infections for everyone", b: 1 }, { text: "A distillery's waste water kills fish downstream", b: 0 },
  { text: "A university's research lets many firms develop new products", b: 1 }, { text: "Homeowners who plant trees cool and clean the air of the whole street", b: 1 }],
  done: "Negative externalities cause too much to be produced or consumed, so the fix cuts the quantity. Positive ones cause too little, so the fix raises it." });
Lib.match($("#m1"), { prompt: "Match the curve gap to the case.", pairs: [
  ["MSC is above MPC", "Negative externality of production"], ["MSB is below MPB", "Negative externality of consumption"], ["MSB is above MPB", "Positive externality of consumption"], ["MSC is below MPC", "Positive externality of production"], ["The vertical gap between MSC and MPC", "Marginal external cost"]],
  done: "Always identify which side (cost or benefit) carries the externality before drawing." });
Lib.order($("#o1"), { prompt: "Put the steps for drawing a negative externality of production in order.", items: [
  "Label the axes and draw D (= MPB = MSB) and S (= MPC)", "Draw MSC above S, parallel, and mark the MEC between them", "Mark Q1 where D meets S", "Mark Q* where D meets MSC", "Shade the welfare loss triangle between Q* and Q1", "Show the tax shifting S up to S + tax, onto MSC", "Mark the new equilibrium at Q* and state that the welfare loss has gone"],
  done: "Cause, problem, solution: the diagram builds in the same order as the argument." });
Lib.calc($("#c1"), { qs: [
  { q: "The MEC is $20 a unit and the socially optimum output is 37.5 units. How much tax revenue does a tax equal to the MEC raise ($)?", a: 750, unit: "$", tol: 1, hint: "Tax × quantity at Q*.", sol: "20 × 37.5 = <b>$750</b>." },
  { q: "Market output is 50 and the socially optimum output is 37.5. The MEC at 50 is $20. What is the welfare loss ($)?", a: 125, unit: "$", tol: 1, hint: "A triangle: ½ × base × height.", sol: "½ × (50 − 37.5) × 20 = <b>$125</b>." },
  { q: "A vaccination has a marginal private cost of $40 and a marginal external benefit of $20. The government subsidises each by the MEB. The socially optimum output is 62.5. What does the subsidy cost ($)?", a: 1250, unit: "$", tol: 1, hint: "Subsidy × quantity at Q*.", sol: "20 × 62.5 = <b>$1,250</b>." },
  { q: "At one output the marginal private cost is $14 and the marginal external cost is $6. What is the marginal social cost ($)?", a: 20, unit: "$", tol: 0.1, hint: "MSC = MPC + MEC.", sol: "14 + 6 = <b>$20</b>." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which curve lies above the supply curve (MPC) when a firm's production creates a negative externality?", opts: ["MSB", "MSC", "MPB", "MEB"], a: 1, why: "MSC = MPC + MEC, so it sits above MPC by the external cost." },
  { q: "A firm's MPC is $30 and the MEC is $8. What is the MSC?", opts: ["$22", "$30", "$38", "$8"], a: 2, why: "30 + 8 = 38." },
  { q: "To reach the socially optimum quantity, a tax on a negative externality should equal:", opts: ["The firm's profit", "The marginal external cost at Q*", "The price at Q1", "The welfare loss"], a: 1, why: "The tax makes the producer pay the marginal external cost at the socially optimum output." },
  { q: "A positive externality of consumption causes:", opts: ["Overproduction because MSC > MSB", "Under-consumption because MSB > MPB", "Overconsumption because MPB > MSB", "No change in output"], a: 1, why: "Consumers ignore the benefit to others, so they buy less than the social optimum." },
  { q: "A government sets a tax higher than the marginal external cost. What is likely?", opts: ["Output stays at Q1", "Output falls below Q*, creating a new welfare loss", "Output rises above Q*", "The welfare loss rises at Q1"], a: 1, why: "An oversized tax over-corrects: units that are worth more than they cost to society are no longer made." },
  { q: "A government advertising campaign persuades more people to be vaccinated. What happens on the diagram?", opts: ["Supply shifts right", "Demand (MPB) shifts right towards MSB", "MSB shifts left", "The price falls to zero"], a: 1, why: "Information changes what consumers value, so it shifts demand, not supply." },
  { q: "Which statement about a subsidy on a positive externality of production is correct?", opts: ["Supply shifts left", "Demand shifts right", "Supply shifts right towards Q*", "The MSC curve shifts"], a: 2, why: "The subsidy lowers costs, so supply shifts down and to the right; MSC is a fixed description of the true cost." }] });
Lib.cards($("#fc1"), { cards: [
  ["Externality", "A cost or benefit to a third party that is not reflected in the market price."],
  ["Marginal external cost (MEC)", "The extra cost imposed on third parties by one more unit produced or consumed."],
  ["Marginal social cost (MSC)", "MPC + MEC: the full cost to society of one more unit."],
  ["Marginal social benefit (MSB)", "MPB + MEB: the full benefit to society of one more unit."],
  ["Socially optimum quantity (Q*)", "The output where MSB = MSC."],
  ["Welfare loss", "The loss of net benefit to society from producing or consuming a quantity other than Q*."],
  ["Internalising an externality", "Making the decision maker face the external cost or benefit, for example through a tax or subsidy."],
  ["Tradable permits", "A cap on total pollution, with permits that firms can buy and sell, fixing the quantity and letting the market set the price."]] });
