"""Builds the five IGCSE Economics 3.3 Workers reviews (3.3.1 to 3.3.5). Run: python3 tools/artifact-kit/mk_ig33.py"""
from igtext import *
DSJS = open(D / "mk_ig24.py").read().split("DSJS = '''")[1].split("'''")[0]
WAGEJS = DSJS + '''
function axes() { return SV.line(X(0), Y(0), X(0), Y(108)) + SV.line(X(0), Y(0), X(135), Y(0)) + SV.text(X(0) + 8, 14, "Wage rate ($ per hour)", "sm") + SV.text(X(135), Y(0) + 24, "Quantity of labour (workers)", "sm", { "text-anchor": "end" }); }
function lmDraw(d, s, nmw) {
  const [q0, p0] = eq(0, 0), [q, p] = eq(d, s); let o = axes() + dCurve(0, d !== 0 ? "c3" : "c1", "D", d !== 0 ? "t3" : "t1") + sCurve(0, s !== 0 ? "c3" : "c2", "S", s !== 0 ? "t3" : "t2");
  if (d !== 0) o += dCurve(d, d > 0 ? "c1" : "c4", d > 0 ? "D₁" : "D₂", d > 0 ? "t1" : "t4");
  if (s !== 0) o += sCurve(s, s > 0 ? "c2" : "c4", s > 0 ? "S₁" : "S₂", s > 0 ? "t2" : "t4");
  o += dsDrop(q, p) + SV.circle(X(q), Y(p), 7, "dot2") + SV.text(X(0) - 8, Y(p), "W", "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (nmw && nmw > p) { const qd = qD(nmw, d), qs = qS(nmw, s); o += SV.line(X(0), Y(nmw), X(Math.max(qd, qs) + 8), Y(nmw), "c4") + SV.circle(X(qd), Y(nmw), 6, "dot3") + SV.circle(X(qs), Y(nmw), 6, "dot4") + SV.text(X(0) - 8, Y(nmw), "NMW", "sm bd t4", { "text-anchor": "end" }) + SV.text(X((qd + qs) / 2), Y(nmw) - 12, "Unemployment " + Math.round(qs - qd), "lbl bd t4", { "text-anchor": "middle" }); }
  return o;
}
'''

# ---------------------------------------------------------------- 3.3.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>People choose an occupation by weighing <b>wage factors</b> (how much it pays) against <b>non-wage factors</b> (everything else that makes a job attractive). The job that gives the greatest <b>overall benefit</b>, not just the highest pay, is usually chosen.</p></div>

  <h2>Wage and non-wage factors</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Factors</th><th>Example</th></tr>
    <tr><td><b>Wage factors</b></td><td>Basic pay, overtime, bonuses, commission, pension, other financial rewards</td><td>A sales job with high commission</td></tr>
    <tr><td><b>Job satisfaction</b></td><td>Interesting, worthwhile or creative work; sense of purpose</td><td>A teacher or nurse accepting lower pay</td></tr>
    <tr><td><b>Working conditions and hours</b></td><td>Hours, shift patterns, safety, pleasant workplace, holiday</td><td>Avoiding night shifts</td></tr>
    <tr><td><b>Job security</b></td><td>Likelihood of keeping the job</td><td>A permanent public sector post</td></tr>
    <tr><td><b>Promotion and career prospects</b></td><td>Chances to progress and gain skills</td><td>A graduate trainee scheme</td></tr>
    <tr><td><b>Location and travel</b></td><td>Commuting time and cost, living near family</td><td>Working close to home</td></tr>
    <tr><td><b>Qualifications and training</b></td><td>The skills required, and training provided</td><td>A doctor's long training</td></tr>
    <tr><td><b>Fringe benefits</b></td><td>Company car, free meals, health insurance, childcare</td><td>Health cover</td></tr>
  </table></div>
  <p class="note">Different people weigh the factors differently depending on <b>age, family, income and personality</b>. Two jobs with the same pay may attract different numbers of workers.</p>
'''
steppers = [
  ("Weighing up jobs", "--accent", ["A worker compares two job offers", "Job A pays more but has long hours", "Job B pays less but is close to home and more satisfying", "The worker values non-wage factors", "Chooses job B despite the lower pay"]),
  ("Why pay differs for similar jobs", "--warn", ["Some jobs are unpleasant or risky", "Fewer people want them", "Employers must pay more to attract workers", "Pleasant jobs attract many applicants", "They can pay less"]),
]
lab1 = dict(title="Score two jobs", intro="Give each factor a score for Job A. The rest of the points go to Job B. See which job a worker with these priorities picks.", rl=["Job A total", "Job B total", "Better job"],
  sliders=[("Pay: Job A (out of 10; Job B = 10 − A)", 0, 10, 1, 8, "v"), ("Hours and conditions: Job A", 0, 10, 1, 3, "v"), ("Job satisfaction: Job A", 0, 10, 1, 3, "v"), ("Job security: Job A", 0, 10, 1, 4, "v")],
  fn="const a = v.reduce((x, y) => x + y, 0), b = 40 - a; return { r: [a + '/40', b + '/40', a > b ? 'Job A' : a < b ? 'Job B' : 'Equal'], t: 'Job A scores ' + a + ' and Job B ' + b + ' out of 40. ' + (a > b ? 'Job A wins on the factors that matter to this worker, even if some are non-wage.' : a < b ? 'Job B wins: pay is not everything; conditions, satisfaction and security can outweigh a higher wage.' : 'A tie: the worker would need other factors to decide.'), bars: [['Pay A', v[0], '--accent'], ['Pay B', 10 - v[0], '--warn'], ['Conditions A', v[1], '--accent'], ['Conditions B', 10 - v[1], '--warn']] };")
lab2 = dict(title="Wage or non-wage?", intro="Pick a factor to see whether it is a wage or non-wage factor.", h1="Type", h2="Example",
  items=[("Overtime pay", "Wage factor", "Extra pay for extra hours."), ("Job satisfaction", "Non-wage factor", "Enjoying the work."), ("Pension contributions", "Wage factor", "A financial reward."), ("Job security", "Non-wage factor", "Likelihood of keeping the job."), ("Length of commute", "Non-wage factor", "Travel time."), ("Annual bonus", "Wage factor", "Extra financial reward.")])
cl = [("Is each a <b>wage factor</b> or a <b>non-wage factor</b>?", ["Wage factor", "Non-wage factor"], [("Basic pay", 0), ("Overtime", 0), ("Bonus", 0), ("Job satisfaction", 1), ("Working hours", 1), ("Job security", 1)], "Pay vs other aspects."),
      ("Which <b>factor</b> is each?", ["Job security", "Promotion prospects", "Working conditions", "Location"], [("A permanent contract", 0), ("A graduate fast-track scheme", 1), ("A safe, pleasant office", 2), ("A short commute", 3), ("Low risk of redundancy", 0)], "Match the factor.")]
match = [["Wage factor", "Financial reward for work"], ["Non-wage factor", "Non-financial aspect of a job"], ["Fringe benefit", "A perk in addition to pay"], ["Job satisfaction", "Enjoyment of the work"], ["Overtime", "Work beyond normal hours"], ["Occupation", "A type of job or career"]]
order = ("Put the steps in order: <b>how a worker chooses between two jobs</b>.", ["List the factors that matter", "Compare pay in each job", "Compare non-wage factors", "Weigh the overall benefit", "Choose the job with the greater benefit"], "A balanced decision.")
calcs = [("A job pays $30,000 plus a $3,000 bonus. What is the total pay ($)?", 33000, "30,000 + 3,000 = <b>$33,000</b>.", None, None), ("A worker's commute costs $200 a month. How much is that a year ($)?", 2400, "200 × 12 = <b>$2,400</b>.", None, None)]
mcq = [("Which is a non-wage factor?", ["Basic pay", "Job satisfaction", "Overtime pay", "Bonus"], 1, "Not financial."), ("A wage factor is:", ["Job security", "Pension", "Hours", "Commute"], 1, "A financial reward."), ("Why might a worker take a lower-paid job?", ["To avoid work", "Higher job satisfaction or security", "To pay more tax", "No reason"], 1, "Non-wage benefits."), ("Fringe benefits include:", ["Basic pay", "Free health insurance", "Taxes", "Interest"], 1, "Perks."), ("Occupational choice depends on:", ["Pay only", "Pay and non-pay factors", "Weather", "Luck"], 1, "Overall benefit.")]
cards = [("Wage factors", "Financial rewards for work."), ("Non-wage factors", "Non-financial aspects of a job."), ("Job satisfaction", "How much a worker enjoys their job."), ("Job security", "How likely a worker is to keep the job."), ("Fringe benefits", "Extras such as health cover or a company car."), ("Occupation", "A type of job."), ("Career prospects", "Chances of promotion and progress."), ("Working conditions", "Hours, safety and environment."), ("Overtime", "Extra hours of work.")]
exam_qs = [
  Q(1, "Identify", 2, "Identify two wage factors that influence occupational choice.", "Pay, overtime, bonus, pension.", "[K|Basic pay (or overtime).] [K|A bonus (or pension).]"),
  Q(2, "Identify", 2, "Identify two non-wage factors that influence occupational choice.", "Job satisfaction, conditions, security, location.", "[K|Job satisfaction.] [K|Job security (or working conditions).]"),
  Q(3, "Explain", 4, "Explain why a worker might choose a lower-paid job.", "Non-wage benefits: satisfaction, security, hours.", "[K|Non-wage factors can outweigh a higher wage.] [N|A job may offer greater job satisfaction or shorter hours.] [N|The worker values these more than the extra pay.]"),
  Q(4, "Analyse", 6, "Analyse how wage and non-wage factors influence a person's choice of occupation.", "Wage: pay; non-wage: satisfaction, security, prospects; overall benefit.", "[K|Wage factors such as pay and bonuses reward workers financially.] [N|Higher pay attracts more workers to an occupation.] [K|Non-wage factors such as job security, hours and satisfaction also matter.] [N|Some workers accept lower pay for a more enjoyable or secure job.] [E|The weight depends on the worker's age, family and income.]", key=True),
]
tips_ = [("Two groups: wage and non-wage.", "Name at least two of each."), ("Link factors to a worker.", "Age, family, income."), ("Overall benefit.", "Not just pay."), ("Give examples.", "Teacher, banker, nurse.")]
real_items = [("Teachers and nurses", "Many accept pay below some other graduate jobs for job satisfaction and security.", "Non-wage factors."), ("Oil rig workers", "High pay compensates for hard conditions and long periods away.", "Wage factors."), ("Remote working", "Flexibility and no commute attract workers even at slightly lower pay.", "Working conditions."), ("Graduate schemes", "Training and promotion prospects attract applicants.", "Career prospects.")]
review("ig-occupation-choice", "w331", "3.3.1", "Factors Affecting an Individual's Choice of Occupation", "Wage and non-wage factors that influence the job people choose. Syllabus 3.3.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Identify", "Explain", "Analyse"], real_items)

# ---------------------------------------------------------------- 3.3.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <b>wage</b> in a labour market is set by the <b>demand for labour</b> (from firms) and the <b>supply of labour</b> (from workers). The demand curve slopes down (firms hire more at lower wages); supply slopes up (more people want to work at higher wages). The equilibrium wage and employment are where they meet. <b>Trade unions</b>, <b>government policy</b> and a <b>national minimum wage</b> can change the outcome.</p></div>

  <h2>Demand for and supply of labour</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Demand for labour</th><th>Supply of labour</th></tr>
    <tr><td><b>Who</b></td><td>Firms (and government employers)</td><td>Workers</td></tr>
    <tr><td><b>Depends on</b></td><td>Demand for the product, productivity of workers (marginal revenue product), cost of capital and other factors</td><td>Wage rate, skills and qualifications, population and migration, working hours, non-wage factors, benefits</td></tr>
    <tr><td><b>Shifts right (increase)</b></td><td>More demand for the product; higher productivity</td><td>More workers (immigration, more women working, longer retirement age)</td></tr>
    <tr><td><b>Shifts left (decrease)</b></td><td>Falling product demand; machines replace workers</td><td>Fewer workers (emigration, ageing, more training years)</td></tr>
  </table></div>

  <h2>Changes in the labour market</h2>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Wage</th><th>Employment</th></tr>
    <tr><td>Demand for labour rises</td><td>Rises</td><td>Rises</td></tr>
    <tr><td>Demand for labour falls</td><td>Falls</td><td>Falls</td></tr>
    <tr><td>Supply of labour rises</td><td>Falls</td><td>Rises</td></tr>
    <tr><td>Supply of labour falls</td><td>Rises</td><td>Falls</td></tr>
  </table></div>

  <h2>Trade unions</h2>
  <ul>
    <li>Unions <b>bargain collectively</b> for higher wages and better conditions.</li>
    <li>Their <b>bargaining power</b> is greater if many workers are members, the workers have rare skills, demand for the product is inelastic or the firm is profitable; it is weaker if unemployment is high or workers are easily replaced.</li>
    <li>Higher union wages may reduce employment if demand for labour is elastic.</li>
  </ul>
  <h2>Government policy and the national minimum wage (NMW)</h2>
  <ul>
    <li>A <b>national minimum wage</b> is a legal minimum rate of pay. It is a <b>minimum price</b> in the labour market.</li>
    <li>If it is set <b>above</b> the equilibrium wage, a <b>surplus of labour</b> (unemployment) can appear; workers in jobs gain.</li>
    <li>If it is set <b>below</b> equilibrium it has no effect.</li>
    <li>Benefits: reduces poverty and exploitation, raises incentives to work. Costs: firms' costs rise, possible job losses, prices may rise.</li>
    <li>Other policies: taxes, benefits, education and training, and immigration rules affect the supply and demand for labour.</li>
  </ul>
'''
steppers = [
  dict(title="Labour market equilibrium", base="{ d: 0, s: 0, m: 0 }", draw="(s) => lmDraw(s.d, s.s, s.m)", steps="""[
  { cap: "Demand for labour D slopes down; supply S slopes up. They meet at the equilibrium wage W and employment Q.", s: { d: 0, s: 0, m: 0 } },
  { cap: "Demand for the firm's product rises, so demand for labour <b>increases</b>: D shifts right. The wage and employment both <b>rise</b>.", s: { d: 30, s: 0, m: 0 } },
  { cap: "More people enter the labour market (e.g. immigration): supply <b>increases</b>. The wage <b>falls</b> and employment <b>rises</b>.", s: { d: 0, s: 30, m: 0 } },
] """),
  dict(title="A national minimum wage", base="{ d: 0, s: 0, m: 0 }", draw="(s) => lmDraw(s.d, s.s, s.m)", steps="""[
  { cap: "Labour market equilibrium at wage W and employment Q.", s: { d: 0, s: 0, m: 0 } },
  { cap: "A <b>minimum wage above equilibrium</b>: more workers want jobs than firms want to hire. A <b>surplus of labour</b> (unemployment) appears.", s: { d: 0, s: 0, m: 68 } },
  { cap: "Workers who keep jobs earn more, but fewer jobs are available. A minimum wage <b>below</b> equilibrium would have no effect.", s: { d: 0, s: 0, m: 68 } },
] """),
  ("Union bargaining power", "--warn", ["A union has many members and rare skills", "Workers can threaten strike action", "The firm faces high costs if production stops", "The firm agrees higher pay", "Wages rise (employment may fall if demand for labour is elastic)"]),
]
lab1 = dict(title="The labour market", intro="Shift labour demand and supply and add a minimum wage. See the wage, employment and unemployment.", rl=["Wage", "Employment", "Unemployment"],
  sliders=[("Shift in demand for labour", -30, 30, 5, 0, "(v > 0 ? '+' : '') + v"), ("Shift in supply of labour", -30, 30, 5, 0, "(v > 0 ? '+' : '') + v"), ("Minimum wage ($; 0 = none)", 0, 90, 5, 0, "v ? '$' + v : 'none'")],
  fn="const e = eq(v[0], v[1]), q = e[0], p = e[1], nm = v[2]; let u = 0, emp = q, w = p; if (nm > p) { const qd = qD(nm, v[0]), qs = qS(nm, v[1]); emp = qd; u = Math.max(0, qs - qd); w = nm; } return { r: ['$' + w.toFixed(0), emp.toFixed(0), u.toFixed(0)], t: 'Equilibrium wage is $' + p.toFixed(0) + ' with employment ' + q.toFixed(0) + '. ' + (nm > p ? 'The minimum wage of $' + nm + ' is above equilibrium: firms hire ' + emp.toFixed(0) + ' workers but ' + (emp + u).toFixed(0) + ' want jobs, so unemployment is ' + u.toFixed(0) + '.' : nm > 0 ? 'The minimum wage of $' + nm + ' is below equilibrium, so it has no effect.' : 'No minimum wage.'), svg: lmDraw(v[0], v[1], nm) };")
lab2 = dict(title="Shifts in the labour market", intro="Pick an event to see its effect on the wage and employment.", h1="Curve and effect", h2="Wage and employment",
  items=[("Product demand rises", "Demand for labour shifts right", "Wage and employment rise."), ("Robots replace workers", "Demand for labour shifts left", "Wage and employment fall."), ("Immigration rises", "Supply of labour shifts right", "Wage falls, employment rises."), ("Many workers retire", "Supply of labour shifts left", "Wage rises, employment falls."), ("A minimum wage above equilibrium", "Wage floor", "Unemployment appears."), ("A strong union", "Higher bargaining power", "Higher wages.")])
cl = [("Does each shift <b>demand for labour</b> or <b>supply of labour</b>?", ["Demand for labour", "Supply of labour"], [("Product demand rises", 0), ("Productivity of workers rises", 0), ("Robots replace some jobs", 0), ("Immigration increases", 1), ("More women enter the workforce", 1), ("Retirement age rises", 1)], "Firms vs workers."),
      ("Is each <b>advantage</b> or <b>disadvantage</b> of a minimum wage?", ["Advantage", "Disadvantage"], [("Reduces poverty", 0), ("Raises incentive to work", 0), ("Protects workers from exploitation", 0), ("May cause unemployment", 1), ("Raises firms' costs", 1), ("May raise prices", 1)], "Weigh both.")]
match = [["Demand for labour", "Firms' willingness to hire at each wage"], ["Supply of labour", "Workers' willingness to work at each wage"], ["Trade union", "Workers' group bargaining for pay and conditions"], ["Collective bargaining", "Negotiating as a group"], ["National minimum wage", "A legal floor on pay"], ["Equilibrium wage", "Where labour demand equals labour supply"]]
order = ("Put the chain in order: <b>how a minimum wage above equilibrium causes unemployment</b>.", ["The government sets a minimum wage above equilibrium", "Firms' costs rise", "Firms hire fewer workers", "More people want to work at the higher wage", "A surplus of labour: unemployment"], "A minimum price causes a surplus.")
calcs = [("The equilibrium wage is $50. A minimum wage of $68 leaves firms demanding 32 workers while 68 want jobs. How many are unemployed?", 36, "68 − 32 = <b>36</b>.", None, None), ("A union wins a 4% pay rise for a $25,000 salary. What is the rise ($)?", 1000, "4% × 25,000 = <b>$1,000</b>.", None, None)]
mcq = [("An increase in demand for labour causes the wage to:", ["Fall", "Rise", "Stay the same", "Be zero"], 1, "More hiring."), ("An increase in supply of labour causes the wage to:", ["Rise", "Fall", "Stay the same", "Double"], 1, "More workers."), ("A minimum wage above equilibrium causes:", ["Labour shortage", "Unemployment", "No effect", "Lower prices"], 1, "A surplus of labour."), ("A union's bargaining power is higher when:", ["Few members", "Workers are easy to replace", "Workers have rare skills", "Unemployment is high"], 2, "Hard to replace."), ("The labour demand curve slopes:", ["Down", "Up", "Vertically", "Horizontally"], 0, "Lower wage, more hired.")]
cards = [("Demand for labour", "How many workers firms want to hire at each wage."), ("Supply of labour", "How many workers are willing to work at each wage."), ("Equilibrium wage", "The wage where labour demand equals supply."), ("Trade union", "An organisation of workers bargaining for better pay."), ("Collective bargaining", "Negotiating wages as a group."), ("National minimum wage", "A legal minimum rate of pay."), ("Productivity", "Output per worker."), ("Immigration", "People moving in to work."), ("Wage floor", "A minimum price in the labour market.")]
exam_qs = [
  Q(1, "Define", 2, "Define a national minimum wage.", "Legal minimum pay rate.", "[K|A national minimum wage is a legal minimum rate of pay] [K|that employers must pay workers.]"),
  Q(2, "Explain", 4, "Explain two influences on the demand for labour.", "Product demand, productivity, cost of capital.", "[K|Demand for the firm's product: if it rises, firms need more workers.] [N|Labour demand shifts right.] [K|Productivity: more productive workers are worth more to firms,] [N|so firms hire more at each wage.]"),
  Q(3, "Analyse", 6, "Analyse, using a labour market diagram, how an increase in the supply of labour could affect wages and employment.", "S right; wage down; employment up.", "[K|An increase in supply, for example from immigration, shifts the supply curve to the right.] [N|At the old wage there is now a surplus of labour,] [N|so the equilibrium wage falls and employment rises.] [E|The effect depends on how elastic labour demand is.]", key=True),
  Q(4, "Discuss", 8, "Discuss whether a national minimum wage will benefit workers.", "Higher pay, reduced poverty vs unemployment, higher costs. Judgement.", "[K|A minimum wage sets a legal minimum for pay.] [N|It raises incomes for low-paid workers, reduces poverty and may raise motivation.] [N|However, if it is above equilibrium, firms may hire fewer workers, causing unemployment.] [N|Firms' costs rise and may be passed on as higher prices.] [E|Overall, a modest minimum wage is likely to benefit most workers, but a very high one could cost jobs, particularly for young or unskilled workers.]", key=True),
]
tips_ = [("Draw D, S and label wage and quantity of labour.", "Axes matter."), ("Shifts: wage and employment effects.", "Learn the four cases."), ("Minimum wage above equilibrium.", "Surplus of labour."), ("Union power depends on skills and unemployment.", "Evaluation."), ("Discuss both sides.", "Judgement.")]
real_items = [("UK National Living Wage", "The minimum wage has risen over time with limited job losses in most studies.", "A national minimum wage."), ("Shortage of lorry drivers", "Demand rose while supply fell, pushing wages up.", "Labour market shifts."), ("Strikes in public transport", "Unions use strike threats to bargain.", "Union bargaining."), ("Automation", "Robots reduce demand for some factory workers.", "A fall in demand.")]
review("ig-wage-determination", "w332", "3.3.2", "Wage Determination", "How labour demand and supply, trade unions, government policy and minimum wages determine pay. Syllabus 3.3.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Analyse", "Discuss"], real_items, prelude=WAGEJS)

# ---------------------------------------------------------------- 3.3.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Workers in different jobs are paid very different wages. The main reasons are differences in the <b>demand for and supply of labour</b>, <b>bargaining strength</b>, <b>discrimination</b> and <b>government policy</b>. How strongly these act depends on the <b>skill level</b>, the <b>sector</b> (primary, secondary, tertiary) and whether the worker is in the <b>private or public sector</b>.</p></div>

  <h2>Reasons for differences in wages</h2>
  <div class="tw"><table class="t">
    <tr><th>Reason</th><th>Effect on wages</th></tr>
    <tr><td><b>Demand for labour</b></td><td>High demand for a worker's skills (strong product demand, high productivity) raises their wage</td></tr>
    <tr><td><b>Supply of labour</b></td><td>Few people with the skills (long training, scarce talent) raises the wage; many people able to do the job lowers it</td></tr>
    <tr><td><b>Bargaining strength</b></td><td>Strong unions or valuable individuals negotiate higher pay</td></tr>
    <tr><td><b>Discrimination</b></td><td>Unequal pay for equal work (for example men and women) can lower some groups' wages</td></tr>
    <tr><td><b>Government policy</b></td><td>Minimum wages raise the lowest pay; public sector pay scales; equal pay laws</td></tr>
  </table></div>

  <h2>Applying the reasons</h2>
  <div class="tw"><table class="t">
    <tr><th>Worker type</th><th>Wages tend to be…</th><th>Why</th></tr>
    <tr><td><b>Skilled</b> (surgeon, engineer)</td><td>Higher</td><td>Scarce skills and long training; high productivity; strong demand</td></tr>
    <tr><td><b>Unskilled</b> (cleaner, labourer)</td><td>Lower</td><td>Many workers can do the job; easy to replace; low bargaining power</td></tr>
    <tr><td><b>Primary sector</b> (farming, mining)</td><td>Often lower (low-skill) but mining can pay well</td><td>Depends on skill level, risk and commodity prices</td></tr>
    <tr><td><b>Secondary sector</b> (manufacturing)</td><td>Middle; unions often strong</td><td>Skills vary; union bargaining</td></tr>
    <tr><td><b>Tertiary sector</b> (finance, services)</td><td>Wide range: high for finance, lower for retail</td><td>Skills and demand differ greatly</td></tr>
    <tr><td><b>Private sector</b></td><td>Linked to profit; wider gaps</td><td>Pay reflects firms' profits</td></tr>
    <tr><td><b>Public sector</b></td><td>Set by government; smaller gaps; more security</td><td>Pay scales and budgets</td></tr>
    <tr><td><b>Male / female</b></td><td>Gaps can exist</td><td>Discrimination, occupations, career breaks</td></tr>
  </table></div>
  <p class="note">Wage gaps are often explained by the <b>demand and supply</b> for each type of labour, but discrimination and government policy can add differences that are not about skills.</p>
'''
steppers = [
  ("Why skilled workers earn more", "--good", ["The job needs long training and rare talent", "Few people can do it: supply is low", "Firms value the high productivity: demand is high", "The wage is bid up", "Skilled workers earn more"]),
  ("Why unskilled workers earn less", "--bad", ["Many people can do the job", "Supply of labour is high", "Workers are easily replaced: weak bargaining power", "The wage is low", "Unskilled workers earn less"]),
]
lab1 = dict(title="What determines a wage?", intro="Rate a job on four features and see the likely wage.", rl=["Wage score", "Likely wage level", "Biggest driver"],
  sliders=[("Skill level required (1 low, 10 high)", 1, 10, 1, 5, "v"), ("Demand for the worker (1 low, 10 high)", 1, 10, 1, 5, "v"), ("Number of people able to do the job (1 few, 10 many)", 1, 10, 1, 5, "v"), ("Bargaining strength (1 weak, 10 strong)", 1, 10, 1, 5, "v")],
  fn="const sc = v[0] * 1.2 + v[1] * 1.5 + (11 - v[2]) * 1.5 + v[3] * 0.8, lvl = sc > 28 ? 'High' : sc > 18 ? 'Medium' : 'Low', nm = ['Skills', 'Demand', 'Scarcity of workers', 'Bargaining strength'], contrib = [v[0] * 1.2, v[1] * 1.5, (11 - v[2]) * 1.5, v[3] * 0.8], top = nm[contrib.indexOf(Math.max(...contrib))]; return { r: [sc.toFixed(0), lvl, top], t: 'Skill ' + v[0] + ', demand ' + v[1] + ', supply of workers ' + v[2] + ' and bargaining strength ' + v[3] + ' give a wage score of ' + sc.toFixed(0) + ': likely a ' + lvl.toLowerCase() + ' wage. High demand and scarce skills push wages up; plentiful workers and weak bargaining hold wages down (illustrative model).', bars: nm.map((n, i) => [n, contrib[i], ['--accent', '--good', '--warn', '--bad'][i], contrib[i].toFixed(0)]) };")
lab2 = dict(title="Why do these jobs pay differently?", intro="Pick a worker to see the main reason for their pay.", h1="Pay level", h2="Main reason",
  items=[("A heart surgeon", "High", "Rare skills, long training, high demand."), ("A supermarket cashier", "Low", "Many people can do the job."), ("A footballer", "Very high", "Scarce talent; huge revenue."), ("A public sector teacher", "Medium", "Set by government pay scales."), ("A female employee paid less than a male colleague", "Lower", "Discrimination."), ("An oil worker", "High", "Risk, skills, high demand.")])
cl = [("Which <b>reason</b> explains each wage difference?", ["Demand and supply", "Bargaining strength", "Discrimination", "Government policy"], [("Surgeons are scarce and in high demand", 0), ("A strong union wins higher pay", 1), ("Women paid less for the same job", 2), ("Public sector pay is set by the state", 3), ("Cleaners are easily replaced", 0), ("A minimum wage lifts the lowest pay", 3)], "Reasons for wage differences."),
      ("Is the wage likely to be <b>high</b> or <b>low</b>?", ["Higher wage", "Lower wage"], [("Rare skills and high demand", 0), ("Strong union", 0), ("Many workers available", 1), ("Easily replaced", 1), ("Discrimination", 1), ("Long training required", 0)], "Think demand and supply.")]
match = [["Skilled worker", "A worker with specialist training"], ["Unskilled worker", "A worker needing little training"], ["Discrimination", "Unfair treatment based on a characteristic"], ["Public sector", "Government-run employment"], ["Private sector", "Employment in privately owned firms"], ["Tertiary sector", "Service industries"]]
order = ("Put the chain in order: <b>why a footballer earns more than a cashier</b>.", ["Few people have elite football skills", "Supply of such players is very low", "Clubs and fans value them highly: demand is high", "Clubs bid up wages", "Footballers earn far more than cashiers"], "Scarce talent and high demand.")
calcs = [("A surgeon earns $240,000 and a nurse $48,000. How many times larger is the surgeon's pay?", 5, "240,000 ÷ 48,000 = <b>5</b>.", None, None), ("A woman earns $40,000 and a man in the same job $44,000. By what percentage is her pay lower than his (nearest whole number)?", 9, "4,000 ÷ 44,000 × 100 ≈ <b>9%</b>.", None, None)]
mcq = [("Skilled workers usually earn more because:", ["Supply is lower and demand higher", "They work fewer hours", "They have no unions", "Their jobs are unpleasant"], 0, "Scarce skills."), ("Which is a reason for wage differences?", ["Weather", "Discrimination", "Gravity", "Tides"], 1, "Unequal treatment."), ("Public sector pay is set mainly by:", ["Profit", "The government", "Customers", "Share prices"], 1, "State pay scales."), ("A strong union is likely to:", ["Lower wages", "Raise wages", "Remove jobs", "Ban work"], 1, "Higher bargaining power."), ("Unskilled wages are low because:", ["Few people can do the work", "Many people can do the work", "Training is long", "Demand is high"], 1, "Easily replaced.")]
cards = [("Skilled worker", "A worker with specialist training."), ("Unskilled worker", "A worker needing little training."), ("Discrimination", "Unfair treatment based on a personal characteristic."), ("Bargaining strength", "The power to negotiate better pay."), ("Public sector", "Government-run employment."), ("Private sector", "Employment in privately owned firms."), ("Primary sector", "Extracting raw materials."), ("Secondary sector", "Manufacturing."), ("Tertiary sector", "Services.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain two reasons why wages differ between occupations.", "Demand and supply of labour, bargaining strength, discrimination, government policy.", "[K|Differences in demand and supply of labour affect wages.] [N|Doctors are scarce and in high demand, so their wages are high.] [K|Bargaining strength differs.] [N|Workers in strong unions can win higher pay than non-union workers.]"),
  Q(2, "Explain", 4, "Explain how discrimination may affect wages.", "Unequal pay for equal work.", "[K|Discrimination means some workers are treated unfairly, for example by gender.] [N|Women may be paid less than men for the same work,] [N|so their wages are lower than their skills justify.]"),
  Q(3, "Analyse", 6, "Analyse why wages in the private sector may differ from those in the public sector.", "Profit vs pay scales; job security; budgets.", "[K|Private sector pay depends on firms' profit and demand for labour, so wages can vary widely.] [N|Public sector pay is set by government scales and budgets, so differences are smaller.] [N|Public sector jobs often offer more security and pensions, which may make up for lower pay.] [E|The size of the gap depends on skills and the budget.]", key=True),
  Q(4, "Discuss", 8, "Discuss whether skill level is the most important reason for differences in wages.", "Skills vs demand, bargaining, discrimination, policy. Judgement.", "[K|Skilled workers earn more because skills are scarce and highly productive.] [N|Training is costly, so supply is low.] [N|However, wages also depend on demand: a rare skill nobody wants is not well paid.] [N|Bargaining strength, discrimination and government policy also matter.] [E|Overall, skill is a key reason but demand and bargaining can outweigh it, so it is not always the most important.]", key=True),
]
tips_ = [("Reasons: demand/supply, bargaining, discrimination, policy.", "Learn them."), ("Link to skills, sector, public/private.", "Use the syllabus list."), ("Explain through supply and demand.", "Scarcity and value."), ("Use examples.", "Surgeon, cleaner, footballer.")]
real_items = [("Gender pay gap", "Women in many countries earn less on average, partly due to discrimination and career breaks.", "Discrimination."), ("Footballers' wages", "Scarce talent and huge revenue drive very high pay.", "Demand and supply."), ("Public sector pay scales", "Teachers' and nurses' pay is set nationally.", "Government policy."), ("Banking bonuses", "High demand for financial skills raises pay.", "Skills and demand.")]
review("ig-wage-differences", "w333", "3.3.3", "Reasons for Differences in Wages", "Why wages differ between workers: demand and supply, bargaining, discrimination and government policy. Syllabus 3.3.3.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Analyse", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.3.4
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Mobility of labour</span> is how easily workers can move to a different <b>job or occupation</b> (<b>occupational mobility</b>) or to a different <b>place</b> (<b>geographical mobility</b>). High mobility helps the economy match workers to jobs and reduces unemployment; low mobility leaves people unemployed while vacancies go unfilled.</p></div>

  <h2>Types of mobility</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Occupational mobility</th><th>Geographical mobility</th></tr>
    <tr><td><b>Meaning</b></td><td>Ability to switch between occupations or industries</td><td>Ability to move between regions or countries to work</td></tr>
    <tr><td><b>Increased by</b></td><td>Education and retraining, transferable skills, apprenticeships, careers advice, fewer licensing barriers</td><td>Cheaper housing and transport, better information about jobs, help with moving costs, ability to work remotely, fewer immigration restrictions</td></tr>
    <tr><td><b>Reduced by</b></td><td>Specialised skills, lack of qualifications, age, fear of change, costly retraining</td><td>High housing costs, family and social ties, language and culture, visa rules, poor transport</td></tr>
  </table></div>

  <h2>Consequences of changes in mobility</h2>
  <div class="grid2">
    <div class="card"><h3>Higher mobility</h3><ul><li>Lower structural unemployment</li><li>Workers fill vacancies faster</li><li>Higher output and productivity</li><li>Wage differences narrow</li><li>Better use of resources</li><li>But: some regions or industries may lose workers (brain drain)</li></ul></div>
    <div class="card"><h3>Lower mobility</h3><ul><li>Higher structural and regional unemployment</li><li>Labour shortages in some areas or sectors</li><li>Lower output and growth</li><li>Wage gaps widen</li><li>Greater need for government help (retraining, relocation grants)</li></ul></div>
  </div>
'''
steppers = [
  ("A factory closes", "--bad", ["Factory workers lose their jobs", "Their skills are specialised: low occupational mobility", "Jobs elsewhere need a move: low geographical mobility", "They remain unemployed", "Structural unemployment rises"]),
  ("Retraining raises mobility", "--good", ["The government funds retraining", "Workers gain new skills", "Occupational mobility rises", "They move into growing industries", "Unemployment falls and output rises"]),
]
lab1 = dict(title="Matching workers to jobs", intro="Set how many workers lose jobs, how many vacancies exist elsewhere and how mobile workers are. See how many find work.", rl=["Workers moving", "Still unemployed", "Vacancies unfilled"],
  sliders=[("Unemployed workers in a declining region", 100, 1000, 50, 500, "v"), ("Vacancies in other regions or industries", 100, 1000, 50, 400, "v"), ("Mobility of workers (%)", 10, 100, 10, 40, "v + '%'")],
  fn="const mv = Math.min(v[1], Math.round(v[0] * v[2] / 100)), un = v[0] - mv, vac = v[1] - mv; return { r: [mv, un, vac], t: v[2] + '% of the ' + v[0] + ' unemployed workers can move into the ' + v[1] + ' vacancies, so ' + mv + ' find work, ' + un + ' stay unemployed and ' + vac + ' vacancies stay unfilled. Higher mobility, through retraining or help with moving, would cut both unemployment and shortages.', bars: [['Unemployed', v[0], '--bad'], ['Vacancies', v[1], '--accent'], ['Find work', mv, '--good']] };")
lab2 = dict(title="Raising or lowering mobility", intro="Pick a factor to see whether it raises or lowers mobility.", h1="Effect", h2="Type",
  items=[("Retraining programme", "Raises mobility", "Occupational."), ("High housing costs in cities", "Lowers mobility", "Geographical."), ("Strong family ties", "Lowers mobility", "Geographical."), ("Better transport links", "Raises mobility", "Geographical."), ("Specialised skills", "Lowers mobility", "Occupational."), ("Online job listings", "Raises mobility", "Both.")])
cl = [("Is each <b>occupational</b> or <b>geographical</b> mobility?", ["Occupational mobility", "Geographical mobility"], [("A miner retrains as a nurse", 0), ("A driver learns to code", 0), ("A worker moves city for a job", 1), ("A graduate emigrates for work", 1), ("Switching from farming to teaching", 0), ("Moving to another region", 1)], "Job vs place."),
      ("Does each <b>increase</b> or <b>decrease</b> labour mobility?", ["Increases mobility", "Decreases mobility"], [("Retraining schemes", 0), ("Cheaper housing", 0), ("Relocation grants", 0), ("Language barriers", 1), ("Specialised skills", 1), ("Strong family ties", 1)], "Factors.")]
match = [["Occupational mobility", "Moving between types of job"], ["Geographical mobility", "Moving between places for work"], ["Structural unemployment", "Unemployment from a mismatch of skills or location"], ["Retraining", "Learning new skills"], ["Transferable skills", "Skills useful in many jobs"], ["Brain drain", "Skilled workers leaving a country"]]
order = ("Put the chain in order: <b>how low mobility causes unemployment</b>.", ["Jobs disappear in one industry or region", "Workers lack skills for new jobs", "Workers cannot or will not move", "Vacancies elsewhere stay unfilled", "Structural unemployment persists"], "A mismatch of skills and jobs.")
calcs = [("500 workers lose jobs and 40% can move to new vacancies. How many find work?", 200, "40% × 500 = <b>200</b>.", None, None), ("A retraining scheme costs $2,000 per worker for 150 workers. What is the total cost ($)?", 300000, "2,000 × 150 = <b>$300,000</b>.", None, None)]
mcq = [("Occupational mobility is:", ["Moving between places", "Moving between jobs or industries", "Retiring", "Working overtime"], 1, "Job switching."), ("Which raises geographical mobility?", ["High housing costs", "Cheaper housing", "Family ties", "Language barriers"], 1, "Easier to move."), ("Low mobility causes:", ["Lower structural unemployment", "Higher structural unemployment", "Higher wages for all", "More vacancies filled"], 1, "Mismatch."), ("Retraining increases:", ["Occupational mobility", "Inflation", "Taxes", "Interest rates"], 0, "New skills."), ("A consequence of higher mobility is:", ["Higher unemployment", "Fewer unfilled vacancies", "Lower output", "Wider wage gaps"], 1, "Better matching.")]
cards = [("Mobility of labour", "How easily workers can change jobs or location."), ("Occupational mobility", "Ability to move between jobs."), ("Geographical mobility", "Ability to move between places."), ("Structural unemployment", "Unemployment from a mismatch of skills or location."), ("Retraining", "Learning new skills."), ("Transferable skills", "Skills usable in many jobs."), ("Relocation grant", "Help with the cost of moving."), ("Brain drain", "Skilled people leaving a country."), ("Labour shortage", "Too few workers for the jobs available.")]
exam_qs = [
  Q(1, "Define", 2, "Define geographical mobility of labour.", "Ability to move between places to work.", "[K|Geographical mobility of labour is the ability of workers] [K|to move between areas or countries to find work.]"),
  Q(2, "Explain", 4, "Explain two causes of a fall in the occupational mobility of labour.", "Specialised skills, age, lack of training.", "[K|Workers with very specialised skills find it hard to switch jobs.] [N|Their skills are not useful in other industries.] [K|Lack of retraining or qualifications also reduces mobility.] [N|Workers cannot afford or access training for new jobs.]"),
  Q(3, "Analyse", 6, "Analyse the consequences of an increase in the geographical mobility of labour.", "Fewer vacancies; lower unemployment; more output; brain drain.", "[K|Workers can move to areas with vacancies.] [N|Unemployment falls in the region they leave and labour shortages fall elsewhere.] [N|Output and productivity rise because labour is used better.] [E|However, regions losing workers may face a brain drain and falling demand.]", key=True),
  Q(4, "Discuss", 8, "Discuss whether governments should spend money to increase the mobility of labour.", "Benefits: employment, growth; costs: expense, uncertain results. Judgement.", "[K|Retraining and relocation grants can raise occupational and geographical mobility.] [N|They reduce structural unemployment and fill vacancies, raising output.] [N|They also reduce welfare spending.] [E|However, programmes cost money and many workers may still not move because of family ties.] [E|Overall, the benefits are likely to outweigh the costs if schemes are well targeted.]", key=True),
]
tips_ = [("Two types.", "Occupational and geographical."), ("Say what raises or lowers mobility.", "Retraining, housing, ties."), ("Link to structural unemployment.", "Mismatch."), ("Evaluate costs of policy.", "Retraining is expensive.")]
real_items = [("Coal mining closures", "Many miners struggled to find new work because of low occupational and geographical mobility.", "Low mobility."), ("EU freedom of movement", "Workers could move easily between member states, raising geographical mobility.", "High mobility."), ("Remote working", "Working from home lets people take jobs far from their home.", "Mobility."), ("Coding bootcamps", "Short courses retrain people for tech jobs.", "Occupational mobility.")]
review("ig-labour-mobility", "w334", "3.3.4", "Mobility of Labour", "Causes and consequences of changes in the occupational and geographical mobility of labour. Syllabus 3.3.4.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Analyse", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.3.5
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Division of labour</span> (worker specialisation) is when the production of a good is <b>split into separate tasks</b>, each done by a different worker (or group), so each worker specialises in one task. Adam Smith's pin factory is the classic example. It raises output but can make work <b>boring</b> and leaves production <b>dependent</b> on every stage.</p></div>

  <h2>Advantages and disadvantages</h2>
  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul>
      <li><b>Higher productivity:</b> workers become skilled and quick at one task (practice makes perfect)</li>
      <li><b>Time saved</b> switching between tasks</li>
      <li><b>Lower costs and prices</b> through economies of scale</li>
      <li>Workers can be matched to the task they do best</li>
      <li>Easier to train new workers for a single task</li>
      <li>Suits mass production and machines</li>
      <li>Higher output raises wages and profit</li>
    </ul></div>
    <div class="card"><h3>Disadvantages</h3><ul>
      <li><b>Boredom and low motivation</b> from repetitive work</li>
      <li><b>Dependence:</b> one stage stopping halts all production</li>
      <li><b>Loss of wider skills</b> and difficulty finding other jobs (low occupational mobility)</li>
      <li><b>Lower quality</b> if workers lose pride in the finished product</li>
      <li>Higher labour turnover and absence</li>
      <li>Workers can be replaced by machines more easily</li>
    </ul></div>
  </div>

  <h2>Example: making pins</h2>
  <p>One worker doing every step might make 20 pins a day. If ten workers each do one or two steps, they may make thousands between them.</p>
  <p class="note">Division of labour is <b>specialisation by workers</b> within a firm. Specialisation by countries or firms is a different idea.</p>
'''
steppers = [
  ("Division of labour raises output", "--good", ["Production is split into separate tasks", "Each worker repeats one task", "Workers become faster and more skilled", "No time is lost switching tasks", "Output per worker rises and cost per unit falls"]),
  ("The downside of division of labour", "--bad", ["Workers repeat the same task all day", "Work becomes boring", "Motivation and quality fall; absence rises", "If one stage stops, all stop", "Productivity gains can be lost"]),
]
lab1 = dict(title="A pin factory", intro="Split the work between more workers. Each specialises and becomes faster, but add too many and the gains fade.", rl=["Total output", "Output per worker", "Cost per pin"],
  sliders=[("Number of workers", 1, 10, 1, 4, "v"), ("Wage per worker per day ($)", 50, 200, 10, 100, "'$' + v"), ("Fixed daily cost ($)", 0, 500, 50, 100, "'$' + v")],
  fn="const per = v[0] === 1 ? 20 : 20 * Math.pow(v[0], 1.35) / v[0] * (v[0] > 8 ? 0.85 : 1), tot = per * v[0], cost = (v[1] * v[0] + v[2]) / tot; return { r: [Math.round(tot) + ' pins', Math.round(per) + ' pins', '$' + cost.toFixed(2)], t: v[0] + ' worker' + (v[0] > 1 ? 's' : '') + ' make about ' + Math.round(tot) + ' pins a day (' + Math.round(per) + ' each). Total cost is $' + (v[1] * v[0] + v[2]) + ', so each pin costs $' + cost.toFixed(2) + '. More specialisation raises output per worker and cuts the cost per pin (illustrative model: the very high numbers of workers show some loss of gains).', bars: [['Output per worker', per, '--good'], ['Total output ÷ 10', tot / 10, '--accent', Math.round(tot)], ['Cost per pin ×100', cost * 100, '--warn', '$' + cost.toFixed(2)]] };")
lab2 = dict(title="Advantages and disadvantages", intro="Pick an effect to see whether it is an advantage or a disadvantage.", h1="Advantage or disadvantage", h2="Why",
  items=[("Workers become very fast", "Advantage", "Practice makes perfect."), ("Work is repetitive", "Disadvantage", "Boredom."), ("Lower cost per unit", "Advantage", "Economies of scale."), ("One stage halts production", "Disadvantage", "Dependence."), ("Easy training", "Advantage", "Single tasks."), ("Loss of broad skills", "Disadvantage", "Harder to change jobs.")])
cl = [("Is each an <b>advantage</b> or a <b>disadvantage</b> of division of labour?", ["Advantage", "Disadvantage"], [("Higher productivity", 0), ("Lower unit costs", 0), ("Time saved switching tasks", 0), ("Boredom", 1), ("Dependence on every stage", 1), ("Loss of skills", 1)], "Weigh both."),
      ("Which <b>group</b> benefits from each?", ["Firm", "Workers", "Consumers"], [("Lower production costs", 0), ("Faster training", 0), ("Cheaper goods", 2), ("Higher wages from higher output", 1), ("More choice and lower prices", 2)], "Who gains.")]
match = [["Division of labour", "Splitting production into tasks done by specialist workers"], ["Specialisation", "Concentrating on one task or product"], ["Productivity", "Output per worker"], ["Economies of scale", "Falling unit costs as output rises"], ["Mass production", "Large-scale making of identical goods"], ["Labour turnover", "Rate at which workers leave and are replaced"]]
order = ("Put the chain in order: <b>how division of labour lowers costs</b>.", ["Production is divided into tasks", "Workers specialise and become more skilled", "Output per worker rises", "Total output rises while fixed costs are spread", "Cost per unit falls"], "Productivity cuts unit cost.")
calcs = [("A worker alone makes 20 pins a day. Ten specialised workers make 4,800 in total. How many does each make?", 480, "4,800 ÷ 10 = <b>480</b>.", None, None), ("A firm's costs are $1,000 and output is 500 units. What is the cost per unit ($)?", 2, "1,000 ÷ 500 = <b>$2</b>.", None, None)]
mcq = [("Division of labour means:", ["One worker does everything", "Splitting production into separate tasks", "Closing the factory", "Paying workers less"], 1, "Specialisation."), ("An advantage is:", ["Boredom", "Higher productivity", "Dependence", "Lower quality"], 1, "More output."), ("A disadvantage is:", ["Lower costs", "Repetitive, boring work", "Faster training", "More output"], 1, "Motivation."), ("Who is most harmed if one stage breaks down?", ["Only that worker", "The whole production line", "No one", "Customers only"], 1, "Dependence."), ("Division of labour is also called:", ["Worker specialisation", "Barter", "Nationalisation", "Taxation"], 0, "Same idea.")]
cards = [("Division of labour", "Splitting production into separate tasks done by specialist workers."), ("Worker specialisation", "Another name for division of labour."), ("Productivity", "Output per worker."), ("Economies of scale", "Lower unit costs as output rises."), ("Mass production", "Making large quantities of identical goods."), ("Labour turnover", "How often workers leave."), ("Motivation", "The drive to work well."), ("Dependence", "Reliance on every stage working."), ("Unit cost", "Cost per item.")]
exam_qs = [
  Q(1, "Define", 2, "Define division of labour.", "Specialisation by tasks.", "[K|Division of labour is when production is split into separate tasks] [K|with each worker specialising in one task.]"),
  Q(2, "Explain", 4, "Explain two advantages of division of labour for a firm.", "Productivity, lower costs, training.", "[K|Workers become more skilled and faster at their task,] [N|so productivity rises.] [K|Higher output lowers cost per unit,] [N|so the firm can cut prices or increase profit.]"),
  Q(3, "Explain", 4, "Explain two disadvantages of division of labour.", "Boredom, dependence, loss of skills.", "[K|Repetitive work may be boring,] [N|which lowers motivation and quality and raises absence.] [K|Production depends on every stage,] [N|so a problem at one stage stops the whole line.]"),
  Q(4, "Discuss", 8, "Discuss whether division of labour benefits firms and workers.", "Productivity and wages vs boredom and dependence. Judgement.", "[K|Division of labour lets workers specialise, raising productivity and lowering unit costs.] [N|Firms gain lower prices and more profit; workers may earn higher wages.] [N|However, repetitive work may reduce motivation and skills, and workers can be replaced by machines.] [E|Overall, firms usually gain, but workers' gains depend on training and job variety, so firms may use job rotation to reduce the downsides.]", key=True),
]
tips_ = [("Define: tasks split between workers.", "Specialisation."), ("Advantages: productivity, cost, training.", "Disadvantages: boredom, dependence, skills."), ("Use the pin factory example.", "Easy to remember."), ("Evaluate with job rotation.", "A way to reduce the downsides.")]
real_items = [("Car assembly lines", "Each worker repeats a task on the line, producing a car every minute or so.", "Division of labour."), ("Fast-food kitchens", "One person cooks, another assembles, another serves.", "Specialised tasks."), ("Call centres", "Different teams handle sales, support and complaints.", "Specialisation."), ("Amazon warehouses", "Pickers, packers and loaders each do a defined task.", "Division of labour.")]
review("ig-division-of-labour", "w335", "3.3.5", "Division of Labour", "What division of labour is, and its advantages and disadvantages. Syllabus 3.3.5.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Discuss"], real_items)
