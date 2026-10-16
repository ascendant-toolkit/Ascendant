const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
const RPS = ["FORWARD 3", "TURN RIGHT", "FORWARD 2", "PICK UP", "TURN LEFT", "FORWARD 1", "PUT DOWN"];
const RPY = ["robot.forward(3)", "robot.turn_right()", "robot.forward(2)", "robot.pick_up()", "robot.turn_left()", "robot.forward(1)", "robot.put_down()"];
/* ---------- 1. robot arm ---------- */
function armChart(s) {
  const bx0 = 380, by0 = 245, L = 105, ex = s.ex, ey = s.ey, dx = ex - bx0, dy = ey - by0, d = Math.min(Math.hypot(dx, dy), 2 * L - 0.01), a = Math.atan2(dy, dx) - Math.acos(d / (2 * L)), elx = bx0 + L * Math.cos(a), ely = by0 + L * Math.sin(a), tx = bx0 + (dx / Math.hypot(dx, dy)) * d, ty = by0 + (dy / Math.hypot(dx, dy)) * d;
  let o = SV.rect(60, 252, 260, 14, "", { rx: 3, style: "fill:#777" }) + sm(190, 285, "conveyor belt") + SV.rect(470, 252, 130, 14, "", { rx: 3, style: "fill:#b08c5a" }) + sm(535, 285, "pallet");
  o += SV.rect(s.bx - 18, s.by - 18, 36, 36, "", { rx: 4, style: "fill:#e0a040;stroke:#8a5a10;stroke-width:2" });
  o += SV.rect(350, 240, 60, 14, "", { rx: 4, style: "fill:#444" }) + SV.line(bx0, by0, elx, ely, "", { style: "stroke:#4a6fa5;stroke-width:14;stroke-linecap:round" }) + SV.line(elx, ely, tx, ty, "", { style: "stroke:#6b8fc5;stroke-width:12;stroke-linecap:round" }) + SV.circle(bx0, by0, 9, "", { style: "fill:#222" }) + SV.circle(elx, ely, 8, "", { style: "fill:#222" });
  const gap = 12 - 8 * s.g; o += SV.line(tx - gap, ty, tx - gap, ty + 20, "", { style: "stroke:#222;stroke-width:5;stroke-linecap:round" }) + SV.line(tx + gap, ty, tx + gap, ty + 20, "", { style: "stroke:#222;stroke-width:5;stroke-linecap:round" }) + SV.line(tx - gap, ty, tx + gap, ty, "", { style: "stroke:#222;stroke-width:5" });
  o += chip(40, 18, 90, "Sensor", s.t === 0 ? ACC : MUT) + chip(150, 18, 130, "Microprocessor", s.t === 1 ? ACC : MUT) + chip(300, 18, 120, "Actuators (motors)", s.t === 2 ? ACC : MUT);
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A factory robot arm moving a box", base: { ex: 380, ey: 110, g: 0, bx: 200, by: 232, t: 0 }, tween: 1100, dwell: 3200, draw: armChart, steps: [
  { cap: "A box arrives on the conveyor belt. A <b>sensor</b> detects it and sends its position to the microprocessor.", s: { ex: 380, ey: 110, g: 0, bx: 200, by: 232, t: 0 } },
  { cap: "The <b>microprocessor</b>, following its program, works out the movements. <b>Actuators</b> (motors in the joints) move the arm over the box.", s: { ex: 200, ey: 205, g: 0, bx: 200, by: 232, t: 2 } },
  { cap: "The gripper actuator <b>closes</b> and grips the box.", s: { ex: 200, ey: 205, g: 1, bx: 200, by: 232, t: 2 } },
  { cap: "The arm lifts the box. Sensors keep checking the arm's position.", s: { ex: 380, ey: 120, g: 1, bx: 380, by: 147, t: 0 } },
  { cap: "The arm moves to the pallet and lowers the box.", s: { ex: 530, ey: 205, g: 1, bx: 530, by: 232, t: 2 } },
  { cap: "The gripper <b>opens</b> and the box is released.", s: { ex: 530, ey: 205, g: 0, bx: 530, by: 232, t: 2 } },
  { cap: "The arm returns to its start position, and the program <b>repeats</b> for the next box. It is the same every time.", s: { ex: 380, ey: 110, g: 0, bx: 530, by: 232, t: 1 } },
] });

/* ---------- 2. robot program ---------- */
const GW = 7, GH = 5, CS = 56, DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]];
function rbView(st, o) {
  let s = ""; for (let r = 0; r < GH; r++) for (let c = 0; c < GW; c++) s += SV.rect(20 + c * CS, 40 + r * CS, CS - 4, CS - 4, "", { rx: 6, style: "fill:var(--soft);stroke:var(--line)" });
  s += SV.rect(20 + 3 * CS, 40 + 0 * CS, CS - 4, CS - 4, "", { rx: 6, style: "fill:var(--good-soft);stroke:var(--good);stroke-width:3" }) + sm(20 + 3 * CS + 26, 40 + 5, "drop zone");
  if (!st.carry && !st.dropped) s += SV.rect(20 + 3 * CS + 12, 40 + 1 * CS + 12, 28, 28, "", { rx: 4, style: "fill:#e0a040;stroke:#8a5a10;stroke-width:2" });
  if (st.dropped) s += SV.rect(20 + 3 * CS + 12, 40 + 12, 28, 28, "", { rx: 4, style: "fill:#e0a040;stroke:#8a5a10;stroke-width:2" });
  const cx = 20 + st.x * CS + 26, cy = 40 + st.y * CS + 26, a = st.d * 90, tri = [[0, -20], [-16, 14], [16, 14]].map(([px, py]) => { const r = (a * Math.PI) / 180; return [cx + px * Math.cos(r) - py * Math.sin(r), cy + px * Math.sin(r) + py * Math.cos(r)]; });
  s += SV.poly(tri, "", { style: "fill:var(--accent);stroke:#fff;stroke-width:2" }); if (st.carry) s += SV.rect(cx - 9, cy - 9, 18, 18, "", { rx: 3, style: "fill:#e0a040;stroke:#8a5a10;stroke-width:2" });
  s += SV.text(20, 26, o.title || "", "lbl bd", { "text-anchor": "start" }); return s;
}
function rbFrames() {
  const F = []; let st = { x: 1, y: 4, d: 0, carry: false, dropped: false };
  const f = (cap, ps, py) => F.push({ cap, ps, py, svg: rbView(st, { title: "Robot program" }) });
  f("The robot starts at the bottom left, facing <b>up</b>. The item is on the grid, and the drop zone is at the top.", [], []);
  const cmds = [["F", 3], ["R"], ["F", 2], ["P"], ["L"], ["F", 1], ["D"]];
  cmds.forEach((c, i) => {
    if (c[0] === "F") for (let k = 1; k <= c[1]; k++) { st = { ...st, x: st.x + DIRS[st.d][0], y: st.y + DIRS[st.d][1] }; f(`<b>${RPS[i]}</b>: step ${k} of ${c[1]}.`, [i], [i]); }
    else if (c[0] === "R") { st = { ...st, d: (st.d + 1) % 4 }; f("<b>TURN RIGHT</b>: the robot rotates 90° clockwise.", [i], [i]); }
    else if (c[0] === "L") { st = { ...st, d: (st.d + 3) % 4 }; f("<b>TURN LEFT</b>: the robot rotates 90° anticlockwise.", [i], [i]); }
    else if (c[0] === "P") { st = { ...st, carry: true }; f("<b>PICK UP</b>: the gripper actuator takes the item.", [i], [i]); }
    else { st = { ...st, carry: false, dropped: true }; f("<b>PUT DOWN</b>: the item is released in the drop zone. The program is finished. The robot does <b>exactly</b> what the instructions say.", [i], [i]); }
  });
  return F;
}
Lib.algo($("#aR"), { w: 440, h: 330, label: "A robot following a program", pseudo: RPS, py: RPY, dwell: 1200, frames: rbFrames() });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdRob"), { pseudo: RPS, py: RPY });

/* ---------- Lab 1 ---------- */
chooser($("#sn"), $("#sv"), ["Robot", "Automated system, not a robot"], [
  ["A robot vacuum cleaner that moves around a room", "Robot"], ["A welding arm on a car production line", "Robot"], ["A drone that sprays crops", "Robot"], ["A surgical arm that holds instruments steady", "Robot"],
  ["A thermostat that switches the boiler on and off", "Automated system, not a robot"], ["Street lights switched by a light sensor", "Automated system, not a robot"], ["A greenhouse controller that opens a window", "Automated system, not a robot"], ["A traffic light controller", "Automated system, not a robot"],
]);

/* ---------- Lab 2 ---------- */
(() => {
  const LV = [{ start: [0, 4], star: [4, 1], walls: [[2, 2], [3, 3]], w: 6, h: 5 }, { start: [0, 4], star: [5, 0], walls: [[0, 2], [1, 2], [3, 3]], w: 6, h: 5 }];
  let prog = [], timer = 0, lvl = LV[0], bot;
  const svg = $("#rg"), pg = $("#rprog"), rv = $("#rv"), sel = $("#lv");
  const draw = (b) => {
    const C = 54; let s = "";
    for (let r = 0; r < lvl.h; r++) for (let c = 0; c < lvl.w; c++) s += SV.rect(10 + c * C, 10 + r * C, C - 4, C - 4, "", { rx: 6, style: "fill:var(--soft);stroke:var(--line)" });
    lvl.walls.forEach(([x, y]) => (s += SV.rect(10 + x * C, 10 + y * C, C - 4, C - 4, "", { rx: 6, style: "fill:#6b7280" })));
    s += SV.text(10 + lvl.star[0] * C + 25, 10 + lvl.star[1] * C + 36, "★", "lbl bd", { "text-anchor": "middle", style: "font-size:34px;fill:#f5b301" });
    const cx = 10 + b.x * C + 25, cy = 10 + b.y * C + 25, a = (b.d * Math.PI) / 2, tri = [[0, -19], [-15, 13], [15, 13]].map(([px, py]) => [cx + px * Math.cos(a) - py * Math.sin(a), cy + px * Math.sin(a) + py * Math.cos(a)]);
    s += SV.poly(tri, "", { style: `fill:${b.crash ? "var(--bad)" : "var(--accent)"};stroke:#fff;stroke-width:2` }); svg.innerHTML = s;
  };
  const reset = () => { bot = { x: lvl.start[0], y: lvl.start[1], d: 0, crash: false }; draw(bot); };
  const show = () => { pg.innerHTML = prog.length ? prog.map((c, i) => `<span style="display:inline-block;padding:3px 9px;margin:2px;border-radius:8px;background:var(--soft);border:1px solid var(--line)">${i + 1}. ${{ F: "FORWARD 1", L: "TURN LEFT", R: "TURN RIGHT" }[c]}</span>`).join("") : "No instructions yet."; };
  $$("[data-c]").forEach((b) => (b.onclick = () => { if (prog.length < 24) prog.push(b.dataset.c); show(); }));
  $("#rundo").onclick = () => { prog.pop(); show(); }; $("#rclr").onclick = () => { prog = []; clearInterval(timer); reset(); show(); rv.textContent = ""; };
  sel.onchange = () => { lvl = LV[+sel.value]; prog = []; clearInterval(timer); reset(); show(); rv.textContent = ""; };
  $("#rrun").onclick = () => {
    clearInterval(timer); reset(); let i = 0; rv.textContent = "Running…";
    timer = setInterval(() => {
      if (i >= prog.length) { clearInterval(timer); const win = bot.x === lvl.star[0] && bot.y === lvl.star[1]; rv.innerHTML = win ? `<span class="okf">Success</span> The robot reached the star in ${prog.length} instructions. Robots do exactly what the program says.` : `<span class="flag">Not there yet</span> The robot finished at column ${bot.x + 1}, row ${bot.y + 1}. Change the program and run it again.`; return; }
      const c = prog[i++];
      if (c === "L") bot.d = (bot.d + 3) % 4; else if (c === "R") bot.d = (bot.d + 1) % 4; else { const nx = bot.x + DIRS[bot.d][0], ny = bot.y + DIRS[bot.d][1]; if (nx < 0 || ny < 0 || nx >= lvl.w || ny >= lvl.h || lvl.walls.some((w) => w[0] === nx && w[1] === ny)) { bot.crash = true; draw(bot); clearInterval(timer); rv.innerHTML = `<span class="flag">Crash</span> at instruction ${i}: the robot hit a wall or the edge. A real robot's sensors would be needed to avoid this.`; return; } bot.x = nx; bot.y = ny; }
      draw(bot);
    }, 450);
  };
  reset(); show();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which characteristic of a robot is each item?", buckets: [{ label: "Mechanical structure" }, { label: "Electrical components" }, { label: "Programmable" }], items: [
  { text: "Robot arm and joints", b: 0 },
  { text: "Wheels or legs", b: 0 },
  { text: "The body or framework", b: 0 },
  { text: "Proximity sensors", b: 1 },
  { text: "A microprocessor", b: 1 },
  { text: "Motors (actuators) in the joints", b: 1 },
  { text: "Its instructions can be changed", b: 2 },
  { text: "Can be taught a new task", b: 2 },
  { text: "Follows a stored program", b: 2 },
], done: "Body, electronics, program." });

Lib.classify($("#cl2"), { prompt: "Is each point an advantage or a disadvantage of using robots?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Can work 24 hours a day", b: 0 },
  { text: "Very accurate and repeatable", b: 0 },
  { text: "Can work in dangerous places", b: 0 },
  { text: "Can lift heavy loads", b: 0 },
  { text: "Expensive to buy and maintain", b: 1 },
  { text: "Can cause job losses", b: 1 },
  { text: "Cannot cope with unexpected problems", b: 1 },
  { text: "A fault stops the work", b: 1 },
], done: "Strength, accuracy and safety against cost, jobs and flexibility." });

Lib.match($("#m1"), { prompt: "Match each area to a robot role.", pairs: [
  ["Industry", "Welding and assembling products"],
  ["Agriculture", "Drones that spray crops"],
  ["Medicine", "Robot-assisted surgery"],
  ["Domestic", "Robot vacuum cleaner"],
  ["Entertainment", "Animatronic characters"],
  ["Transport", "Self-driving delivery vehicle"]
] });

Lib.order($("#o1"), { prompt: "Put the sense, think, act steps of a robot in order.", items: [
  "Sensors detect an obstacle",
  "The data is sent to the microprocessor",
  "The microprocessor decides to turn, using its program",
  "A signal is sent to the motors (actuators)",
  "The robot moves and the sensors check again"
], done: "Sense, send, think, signal, act, repeat." });

Lib.calc($("#c1"), { qs: [
  { q: "A robot arm welds 6 joints a minute. How many joints does it weld in an hour?", a: 360, sol: "6 × 60 = 360." },
  { q: "A robot works 24 hours a day. A person works 8 hours a day. How many times more hours does the robot work?", a: 3, sol: "24 ÷ 8 = 3." },
  { q: "A robot costs 90000 and replaces 3 workers who each cost 20000 a year. How many whole years until the robot pays for itself? (Round up)", a: 2, sol: "3 × 20000 = 60000 a year. After 1 year 60000, after 2 years 120000, so 2 years.", hint: "Total saving each year first." },
  { q: "A robot program has the instructions FORWARD 3, TURN RIGHT, FORWARD 2. How many cells does it move forward in total?", a: 5, sol: "3 + 2 = 5 (turning does not move it)." },
  { q: "A drone checks 4 fields an hour. How many fields in a 6-hour shift?", a: 24, sol: "4 × 6 = 24." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a characteristic of a robot?", opts: ["It is programmable", "It is always humanoid", "It never needs power", "It has no sensors"], a: 0, why: "Robots are programmable." },
  { q: "What is robotics?", opts: ["Design, construction and operation of robots", "Writing web pages", "Storing data", "Making screens"], a: 0, why: "A branch of computer science." },
  { q: "Which is a robot?", opts: ["A robot vacuum cleaner", "A street light sensor", "A thermostat", "A calculator"], a: 0, why: "It has a body that moves, sensors, a microprocessor, actuators and a program." },
  { q: "What does a robot's microprocessor do?", opts: ["Processes sensor data and makes decisions", "Moves the wheels directly", "Stores the batteries", "Measures light"], a: 0, why: "It decides using its program." },
  { q: "Which is a disadvantage of robots?", opts: ["Can work 24 hours a day", "Very accurate", "Cannot cope with unexpected problems", "Work in danger"], a: 2, why: "Robots follow their program." },
  { q: "Why is bomb disposal done by robots?", opts: ["It is cheaper", "To keep people out of danger", "Robots think creatively", "They are faster at walking"], a: 1, why: "Robots can work in dangerous places." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Robotics", "A branch of computer science: the design, construction and operation of robots."],
  ["Robot", "A programmable machine with a mechanical structure and electrical components that can perform tasks."],
  ["Mechanical structure", "The framework of a robot: its body, arms, joints, wheels."],
  ["Electrical components", "Sensors, a microprocessor and actuators."],
  ["Programmable", "Its instructions can be written and changed."],
  ["Drone", "A flying robot, controlled remotely or by a program."],
  ["Sense, think, act", "The cycle a robot follows: sensors detect, the microprocessor decides, actuators act."],
  ["Actuator", "A motor or other part that turns a signal into movement."]
] });
