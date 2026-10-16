"""Builds the three IGCSE Economics 3.5 Firms and production reviews (3.5.1 to 3.5.3). Run: python3 tools/artifact-kit/mk_ig35.py"""
from igtext import *

# ---------------------------------------------------------------- 3.5.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <b>demand for a factor of production</b> (labour, capital, land) is a <span class="kw">derived demand</span>: firms want factors <b>because of the goods and services they help produce</b>. So the demand for factors depends on the <b>demand for the product</b>, the <b>price of the factor</b> and its substitutes, the <b>availability</b> of the factor and its <b>productivity</b>.</p></div>

  <h2>Influences on the demand for factors</h2>
  <div class="tw"><table class="t">
    <tr><th>Influence</th><th>Effect on demand for the factor</th><th>Example</th></tr>
    <tr><td><b>Demand for the product</b></td><td>Higher product demand raises demand for the factors needed to make it</td><td>More demand for electric cars raises demand for battery workers and lithium</td></tr>
    <tr><td><b>Price of the factor</b></td><td>A higher price cuts the quantity demanded; a fall in price raises it</td><td>Dearer labour makes firms hire fewer workers</td></tr>
    <tr><td><b>Price of other (substitute) factors</b></td><td>If one factor becomes dearer, firms may switch to a cheaper substitute</td><td>Higher wages may lead firms to buy robots</td></tr>
    <tr><td><b>Availability</b></td><td>Scarce factors are dearer and used less; abundant factors are used more</td><td>A shortage of skilled engineers limits hiring</td></tr>
    <tr><td><b>Productivity</b></td><td>More productive factors give more output per $ spent, so demand is higher</td><td>Firms demand more skilled, well-trained workers</td></tr>
  </table></div>
  <ul>
    <li>Factors can be <b>substitutes</b> (labour and machines) or <b>complements</b> (workers and the tools they use).</li>
    <li>A factor's <b>marginal revenue product</b> (the extra revenue an extra unit brings) sets how much a firm will pay.</li>
  </ul>
  <p class="note">The word to remember is <b>derived</b>: demand for factors comes from demand for the final product.</p>
'''
steppers = [
  ("Derived demand", "--accent", ["Consumers demand more of a product", "Firms need to produce more", "They demand more labour, capital and land", "The demand for factors is derived from the product", "Factor prices (wages) may rise"]),
  ("Substituting capital for labour", "--warn", ["The wage rate rises", "Labour becomes dearer relative to machines", "Firms demand fewer workers", "They demand more machines", "The mix of factors changes"]),
]
lab1 = dict(title="Derived demand for workers", intro="Each extra worker adds output, but with diminishing returns. Set the product price and wage to see how many workers a firm demands.", rl=["Workers hired", "Revenue", "Profit from labour"],
  sliders=[("Price of the product ($)", 2, 20, 1, 10, "'$' + v"), ("Wage per worker ($)", 10, 100, 5, 40, "'$' + v"), ("Productivity (output of first worker)", 5, 20, 1, 12, "v")],
  fn="let n = 0, rev = 0, prev = 0; for (let w = 1; w <= 12; w++) { const out = v[2] * Math.pow(0.85, w - 1), mrp = out * v[0]; if (mrp >= v[1]) { n = w; prev += out; } else break; } const tr = prev * v[0], cost = n * v[1]; return { r: [n + ' workers', '$' + tr.toFixed(0), (tr - cost >= 0 ? '+' : '−') + '$' + Math.abs(tr - cost).toFixed(0)], t: 'The firm hires workers while the extra revenue each adds (their marginal revenue product) is at least the wage. With product price $' + v[0] + ', wage $' + v[1] + ' and first-worker output ' + v[2] + ', it hires ' + n + ' workers. A higher product price or higher productivity raises the demand for labour; a higher wage lowers it.', bars: [['Workers hired', n, '--accent'], ['Revenue ÷ 20', tr / 20, '--good', '$' + tr.toFixed(0)], ['Labour cost ÷ 20', cost / 20, '--warn', '$' + cost]] };")
lab2 = dict(title="What changes the demand for a factor?", intro="Pick an event to see the effect on the demand for the factor.", h1="Effect on demand for the factor", h2="Why",
  items=[("Demand for the product rises", "Demand for factors rises", "Derived demand."), ("The wage rises", "Quantity of labour demanded falls", "Dearer labour."), ("Machines become cheaper", "Demand for labour falls, for machines rises", "Substitution."), ("Workers become more productive", "Demand for labour rises", "More output per $."), ("A shortage of skilled workers", "Quantity demanded falls", "Higher price; scarce."), ("Product demand falls", "Demand for factors falls", "Derived demand.")])
cl = [("Does each <b>increase</b> or <b>decrease</b> demand for labour?", ["Increase", "Decrease"], [("Product demand rises", 0), ("Workers become more productive", 0), ("Machines become dearer", 0), ("Product demand falls", 1), ("Machines become much cheaper", 1), ("Productivity falls", 1)], "Derived demand."),
      ("Which <b>influence</b> is each?", ["Product demand", "Price of the factor", "Substitute factors", "Availability", "Productivity"], [("A boom in car sales", 0), ("Wages rise", 1), ("Robots replace workers", 2), ("A shortage of engineers", 3), ("Workers trained to work faster", 4)], "Five influences.")]
match = [["Derived demand", "Demand for a factor that comes from demand for the product"], ["Marginal revenue product", "Extra revenue from one more unit of a factor"], ["Substitute factors", "Factors that can replace each other"], ["Complementary factors", "Factors used together"], ["Productivity", "Output per unit of input"], ["Availability", "How easy a factor is to obtain"]]
order = ("Put the chain in order: <b>how a rise in product demand raises demand for workers</b>.", ["Consumer demand for the product rises", "The firm needs to produce more", "It needs more workers", "Demand for labour rises", "Wages and employment may rise"], "Derived demand.")
calcs = [("A worker adds 8 units of output each worth $5. What is the marginal revenue product ($)?", 40, "8 × 5 = <b>$40</b>.", None, None), ("A worker's MRP is $40 and the wage is $35. Should the firm hire? Enter the extra profit ($).", 5, "40 − 35 = <b>$5</b>: yes.", None, None)]
mcq = [("Derived demand means demand for a factor comes from:", ["Demand for the product", "The government", "Tax", "Imports"], 0, "Final product."), ("A rise in wages is likely to:", ["Raise demand for labour", "Lower the quantity of labour demanded", "Have no effect", "Raise productivity"], 1, "Dearer labour."), ("Which raises demand for labour?", ["Falling product demand", "Higher productivity", "Dearer product", "Cheaper machines"], 1, "More output per $."), ("Machines and workers are often:", ["Substitutes", "Complements only", "Unrelated", "Free"], 0, "Can replace each other."), ("A shortage of a factor makes it:", ["Cheaper", "Dearer", "Free", "Unnecessary"], 1, "Scarcity.")]
cards = [("Derived demand", "Demand for a factor of production that comes from demand for the product it makes."), ("Marginal revenue product", "The extra revenue from employing one more unit of a factor."), ("Substitute factors", "Factors that can replace each other."), ("Complementary factors", "Factors used together."), ("Productivity", "Output per unit of input."), ("Availability", "How easily a factor can be obtained."), ("Wage rate", "The price of labour."), ("Capital goods", "Goods used to make other goods."), ("Quantity demanded", "The amount demanded at a price.")]
exam_qs = [
  Q(1, "Define", 2, "Define derived demand.", "Demand for a factor from demand for the product.", "[K|Derived demand is demand for a factor of production] [K|that arises from the demand for the product it helps to make.]"),
  Q(2, "Explain", 4, "Explain two influences on the demand for labour.", "Product demand, wage, productivity, substitutes.", "[K|The demand for the firm's product: if it rises, more workers are needed.] [N|Labour demand shifts right.] [K|The price of labour: a higher wage reduces the quantity of labour demanded] [N|as firms switch to machines or cut output.]"),
  Q(3, "Analyse", 6, "Analyse how an increase in the productivity of workers may affect a firm's demand for labour.", "More output per worker; higher MRP; may hire more or fewer.", "[K|Higher productivity means each worker produces more.] [N|The extra revenue from each worker (MRP) rises, so labour is more valuable to the firm.] [N|The firm may demand more workers and pay higher wages.] [E|If product demand is limited, the firm may need fewer workers to produce the same output.]", key=True),
  Q(4, "Discuss", 8, "Discuss whether a rise in wages will always reduce the demand for labour.", "Substitutes, product demand, productivity, elasticity. Judgement.", "[K|A higher wage raises costs, so firms may hire fewer workers or replace them with machines.] [N|However, if the rise is matched by higher productivity, labour may still be good value.] [N|If product demand is strong, firms may keep hiring.] [E|Overall, a wage rise is likely to reduce the quantity of labour demanded, but not always, because it depends on productivity, product demand and the availability of substitutes.]", key=True),
]
tips_ = [("Derived demand: from the product.", "Say it."), ("Five influences.", "Product demand, factor price, substitutes, availability, productivity."), ("Link to a firm.", "Wages, machines, output."), ("Evaluate: productivity.", "Higher wages can be justified.")]
real_items = [("Electric vehicles", "Rising demand for EVs raises demand for battery engineers and lithium.", "Derived demand."), ("Warehouse robots", "When wages rose, firms bought robots.", "Substitution."), ("Shortage of nurses", "A limited supply of trained nurses raises wages.", "Availability."), ("AI programmers", "High productivity of skilled coders raises demand.", "Productivity.")]
review("ig-factor-demand", "p351", "3.5.1", "Demand for Factors of Production", "What influences firms' demand for labour, capital and land: product demand, factor prices, availability and productivity. Syllabus 3.5.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Analyse", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.5.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Labour-intensive</span> production uses <b>a lot of labour</b> relative to capital. <span class="kw">Capital-intensive</span> production uses <b>a lot of capital</b> (machinery) relative to labour. Firms choose the method that gives the <b>lowest cost</b> for the output, quality and flexibility they need.</p></div>

  <h2>Comparing the two</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Labour-intensive</th><th>Capital-intensive</th></tr>
    <tr><td><b>Examples</b></td><td>Hairdressing, teaching, farming by hand, restaurants</td><td>Car assembly lines, oil refining, automated warehouses</td></tr>
    <tr><td><b>Why adopted</b></td><td>Cheap labour; small scale; personal service; products need skill or creativity; machines are costly or unsuitable</td><td>High wages; large scale; need speed, precision and consistency; cheap capital; technology available</td></tr>
    <tr><td><b>Advantages</b></td><td>Flexible; personal touch; lower start-up cost; easier to adjust to small orders; creates jobs</td><td>High output; lower unit cost at scale; consistent quality; works around the clock; fewer wage costs</td></tr>
    <tr><td><b>Disadvantages</b></td><td>Higher labour costs when wages rise; lower output per worker; variable quality; limited scale</td><td>High start-up and maintenance costs; breakdowns; less flexible; unemployment; skilled workers needed</td></tr>
  </table></div>

  <h2>Choosing between them</h2>
  <ul>
    <li>Compare <b>relative factor prices</b>: dear labour and cheap capital favour capital-intensive methods; cheap labour and dear capital favour labour-intensive methods.</li>
    <li>Think about <b>output level</b>, <b>quality needed</b> and the <b>nature of the product</b>.</li>
    <li>Countries with large populations and low wages (for example India) often use more labour-intensive methods; rich countries use more capital-intensive ones.</li>
  </ul>
'''
steppers = [
  ("Why firms switch to capital", "--warn", ["Wages rise", "Machines become relatively cheaper", "The firm buys robots and cuts workers", "Output per worker rises", "Costs per unit fall (if volume is high enough)"]),
  ("Why some firms stay labour-intensive", "--good", ["The product needs a personal touch (e.g. a hairdresser)", "Machines cannot easily do the job", "Labour is cheap and flexible", "The firm keeps workers", "A labour-intensive method is better"]),
]
lab1 = dict(title="Choose a method", intro="Compare the total cost of labour-intensive and capital-intensive production at different wages and output levels.", rl=["Labour-intensive cost", "Capital-intensive cost", "Cheaper method"],
  sliders=[("Wage per worker per day ($)", 20, 200, 10, 60, "'$' + v"), ("Daily cost of machines ($)", 100, 2000, 100, 800, "'$' + v"), ("Units to produce per day", 50, 500, 50, 200, "v")],
  fn="const lab = Math.ceil(v[2] / 10) * v[0], cap = v[1] + Math.ceil(v[2] / 100) * v[0], ch = lab < cap ? 'Labour-intensive' : lab > cap ? 'Capital-intensive' : 'Equal'; return { r: ['$' + lab, '$' + cap, ch], t: 'To make ' + v[2] + ' units a day, a labour-intensive method needs ' + Math.ceil(v[2] / 10) + ' workers: $' + lab + '. A capital-intensive method costs $' + v[1] + ' for machines plus ' + Math.ceil(v[2] / 100) + ' operators: $' + cap + '. So ' + ch.toLowerCase() + ' production is cheaper. Higher wages or larger output favour capital; cheap labour and small scale favour labour (illustrative model).', bars: [['Labour-intensive', lab, '--accent'], ['Capital-intensive', cap, '--warn']] };")
lab2 = dict(title="Which method?", intro="Pick a business to see which method it is likely to use.", h1="Method", h2="Why",
  items=[("A hair salon", "Labour-intensive", "Personal service; skills."), ("A car assembly plant", "Capital-intensive", "High volume; precision."), ("A small family restaurant", "Labour-intensive", "Personal touch; low scale."), ("An oil refinery", "Capital-intensive", "Large equipment; few workers."), ("A rice farm in a low-wage country", "Labour-intensive", "Cheap labour."), ("A bottling plant", "Capital-intensive", "Fast and consistent.")])
cl = [("Is each <b>labour-intensive</b> or <b>capital-intensive</b>?", ["Labour-intensive", "Capital-intensive"], [("A hairdresser", 0), ("A school", 0), ("A restaurant", 0), ("A car factory with robots", 1), ("An oil refinery", 1), ("An automated warehouse", 1)], "Workers vs machines."),
      ("Is each an advantage of <b>labour-intensive</b> or <b>capital-intensive</b> production?", ["Labour-intensive", "Capital-intensive"], [("Flexible", 0), ("Personal service", 0), ("Low start-up cost", 0), ("High output per worker", 1), ("Consistent quality", 1), ("Can work 24 hours a day", 1)], "Pick the method.")]
match = [["Labour-intensive", "Uses mainly labour in production"], ["Capital-intensive", "Uses mainly machinery in production"], ["Automation", "Machines doing tasks once done by workers"], ["Start-up cost", "Money needed to begin production"], ["Relative factor prices", "Cost of labour compared with capital"], ["Output per worker", "Productivity"]]
order = ("Put the chain in order: <b>how rising wages encourage capital-intensive production</b>.", ["Wages rise", "Labour becomes dearer relative to capital", "Firms buy machines to replace workers", "Output per worker rises", "Production becomes more capital-intensive"], "Substitution.")
calcs = [("A firm makes 400 units using 8 workers. What is output per worker?", 50, "400 ÷ 8 = <b>50</b>.", None, None), ("Machines cost $1,200 a day and replace 10 workers paid $100 each. How much does the firm save per day ($)? (Wages saved minus machine cost)", -200, "1,000 − 1,200 = <b>−$200</b>: a loss.", None, None)]
mcq = [("Capital-intensive production uses:", ["Mainly labour", "Mainly machinery", "No inputs", "Only land"], 1, "Machines."), ("Which is likely to be labour-intensive?", ["Car assembly plant", "A hair salon", "An oil refinery", "A bottling plant"], 1, "Personal service."), ("Higher wages encourage:", ["More labour-intensive methods", "More capital-intensive methods", "No change", "Lower output"], 1, "Substitution."), ("A disadvantage of capital-intensive production is:", ["High start-up cost", "Low output", "Poor quality", "Low flexibility needs"], 0, "Costly machines."), ("A country with cheap labour tends to use:", ["Capital-intensive methods", "Labour-intensive methods", "No methods", "Only imports"], 1, "Lower costs.")]
cards = [("Labour-intensive production", "Production using a high proportion of labour."), ("Capital-intensive production", "Production using a high proportion of capital."), ("Automation", "Machines doing work previously done by people."), ("Productivity", "Output per worker."), ("Start-up costs", "The initial costs of beginning production."), ("Flexibility", "Ability to adjust output or products."), ("Relative factor prices", "The cost of one factor compared with another."), ("Mass production", "Large-scale production of identical goods."), ("Unemployment", "People without work who want it.")]
exam_qs = [
  Q(1, "Define", 2, "Define capital-intensive production.", "Uses mainly capital.", "[K|Capital-intensive production is production that uses] [K|a high proportion of capital compared with labour.]"),
  Q(2, "Explain", 4, "Explain two reasons why a firm may choose labour-intensive production.", "Cheap labour, personal service, low start-up costs.", "[K|Labour may be cheap,] [N|so it is the lowest-cost method.] [K|The product may need personal service or skill,] [N|which machines cannot easily provide.]"),
  Q(3, "Explain", 4, "Explain two advantages of capital-intensive production.", "High output, consistent quality, lower unit cost.", "[K|Machines can produce large quantities quickly,] [N|so output per worker is high.] [K|Machines give consistent quality and work all day,] [N|so unit costs are lower.]"),
  Q(4, "Discuss", 8, "Discuss whether a firm should switch from labour-intensive to capital-intensive production.", "Costs, output, jobs, flexibility. Judgement.", "[K|Capital-intensive production can raise output per worker and lower unit costs.] [N|It gives consistent quality and can work around the clock.] [N|However, machines are costly to buy and maintain and may make some workers redundant.] [N|It is less flexible for small or varied orders.] [E|Overall, the switch is worthwhile for large-scale, high-volume production when wages are high, but not for small, personalised services.]", key=True),
]
tips_ = [("Define by proportion.", "More labour or more capital."), ("Link to relative factor prices.", "Dear labour, cheap capital."), ("Examples.", "Hair salon vs car factory."), ("Evaluate with scale.", "High volume favours capital.")]
real_items = [("Hair salons", "Hair cutting remains labour-intensive.", "Labour-intensive."), ("Tesla gigafactories", "Highly automated production lines make batteries and cars.", "Capital-intensive."), ("Garment factories in Bangladesh", "Many workers sew by hand, reflecting cheap labour.", "Labour-intensive."), ("Amazon warehouses", "Robots move shelves, raising output per worker.", "Capital-intensive.")]
review("ig-labour-capital-intensive", "p352", "3.5.2", "Labour-Intensive and Capital-Intensive Production", "Why firms choose labour-intensive or capital-intensive methods, with advantages and disadvantages. Syllabus 3.5.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.5.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Production</span> is the <b>total output</b> of goods and services. <span class="kw">Productivity</span> is <b>output per unit of input</b>, for example output per worker per hour. A firm can raise production by using more inputs, but only <b>raising productivity</b> increases output per unit of input and lowers unit costs.</p></div>

  <h2>Production and productivity</h2>
  <div class="formula">Production = total output<br>Labour productivity = total output ÷ number of workers (or hours)</div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Production</th><th>Productivity</th></tr>
    <tr><td><b>Meaning</b></td><td>How much is produced in total</td><td>How efficiently inputs are used: output per worker or per machine</td></tr>
    <tr><td><b>Example</b></td><td>A factory makes 1,000 shirts a day</td><td>Each worker makes 20 shirts a day</td></tr>
    <tr><td><b>Can rise without the other?</b></td><td>Yes: by hiring more workers</td><td>Only if output rises more than inputs</td></tr>
  </table></div>

  <h2>Influences on production and productivity</h2>
  <ul>
    <li><b>Quantity and quality of labour:</b> more or better-trained workers; health and motivation.</li>
    <li><b>Capital and technology:</b> machinery, equipment and automation.</li>
    <li><b>Management and organisation:</b> division of labour, good planning.</li>
    <li><b>Working conditions and incentives:</b> pay, bonuses, job satisfaction.</li>
    <li><b>Infrastructure and energy supplies.</b></li>
    <li><b>Natural resources and raw materials.</b></li>
  </ul>

  <h2>Effects of investment on productivity</h2>
  <ul>
    <li>Investment in <b>new machinery and technology</b> lets each worker produce more.</li>
    <li>Investment in <b>training and education</b> (human capital) raises workers' skills.</li>
    <li>Higher productivity lowers <b>unit costs</b>, raising profit, lowering prices and increasing <b>competitiveness</b> and <b>economic growth</b>.</li>
    <li>Investment costs money now and may take time to pay off.</li>
  </ul>
'''
steppers = [
  ("Investment raises productivity", "--good", ["A firm invests in new machinery and training", "Each worker has better tools and skills", "Output per worker rises", "Unit costs fall", "The firm becomes more competitive"]),
  ("More production is not always more productivity", "--warn", ["A firm hires twice as many workers", "Output rises, but not by twice as much", "Output per worker falls", "Production is higher but productivity is lower", "Costs per unit may rise"]),
]
lab1 = dict(title="Investment and productivity", intro="Invest in machinery and training and see output per worker and unit cost.", rl=["Output", "Output per worker", "Cost per unit"],
  sliders=[("Number of workers", 10, 100, 10, 50, "v"), ("Investment in machinery ($000)", 0, 500, 50, 100, "'$' + v + 'k'"), ("Investment in training ($000)", 0, 200, 20, 40, "'$' + v + 'k'")],
  fn="const per = 20 + 0.04 * v[1] + 0.08 * v[2], out = per * v[0], cost = (v[0] * 100 + v[1] * 0.2 + v[2] * 0.2) / out; return { r: [Math.round(out) + ' units', per.toFixed(1), '$' + cost.toFixed(2)], t: v[0] + ' workers with $' + v[1] + 'k of machinery and $' + v[2] + 'k of training produce ' + Math.round(out) + ' units, or ' + per.toFixed(1) + ' per worker. Cost per unit is $' + cost.toFixed(2) + ' (wages $100 per worker plus annual investment costs). More investment raises output per worker and lowers unit cost (illustrative model).', bars: [['Output per worker', per, '--good'], ['Output ÷ 20', out / 20, '--accent', Math.round(out)], ['Cost per unit ×10', cost * 10, '--warn', '$' + cost.toFixed(2)]] };")
lab2 = dict(title="Production or productivity?", intro="Pick a statement to see whether it is about production or productivity.", h1="Measure", h2="Why",
  items=[("A factory makes 5,000 cars a year", "Production", "Total output."), ("Each worker makes 40 cars a year", "Productivity", "Output per worker."), ("Output rises 10% after hiring 10% more workers", "Production up, productivity unchanged", "Output per worker stays the same."), ("Output rises 10% with the same workers", "Productivity up", "Output per worker rises."), ("A country's output rises", "Production", "Total output."), ("New machines let each worker make more", "Productivity", "Better tools.")])
cl = [("Is each about <b>production</b> or <b>productivity</b>?", ["Production", "Productivity"], [("Total output of 10,000 units", 0), ("Total GDP", 0), ("Output per worker per hour", 1), ("Output per machine", 1), ("A factory makes 500 shirts a day", 0), ("Each worker makes 25 shirts a day", 1)], "Total vs per input."),
      ("Does each <b>raise</b> or <b>lower</b> productivity?", ["Raises productivity", "Lowers productivity"], [("Better training", 0), ("New technology", 0), ("Better management", 0), ("Poor health of workers", 1), ("Outdated machines", 1), ("Low motivation", 1)], "Influences.")]
match = [["Production", "Total output"], ["Productivity", "Output per unit of input"], ["Investment", "Spending on capital goods or training"], ["Human capital", "Workers' skills and knowledge"], ["Technology", "Methods and machines that raise output"], ["Unit cost", "Cost per item"]]
order = ("Put the chain in order: <b>how investment in training raises growth</b>.", ["Firms invest in training", "Workers become more skilled", "Productivity rises", "Unit costs fall and output rises", "Competitiveness and growth improve"], "Human capital.")
calcs = [("A factory with 50 workers makes 1,000 units. What is output per worker?", 20, "1,000 ÷ 50 = <b>20</b>.", None, None), ("Output rises from 1,000 to 1,200 with the same 50 workers. By what percentage does productivity rise?", 20, "200 ÷ 1,000 × 100 = <b>20%</b>.", None, None), ("Output rises 10% and workers rise 10%. What is the change in productivity (%)?", 0, "Productivity is unchanged: <b>0%</b>.", None, None)]
mcq = [("Productivity is:", ["Total output", "Output per unit of input", "Profit", "Wages"], 1, "Per worker or machine."), ("Which raises productivity?", ["Poor training", "Investment in technology", "Lower pay", "Fewer machines"], 1, "Better tools."), ("If output rises 5% and workers rise 5%, productivity:", ["Rises", "Falls", "Is unchanged", "Doubles"], 2, "Same output per worker."), ("Higher productivity usually:", ["Raises unit cost", "Lowers unit cost", "Cuts output", "Raises prices"], 1, "More output per $."), ("Human capital is:", ["Machines", "Workers' skills", "Money", "Land"], 1, "Skills and knowledge.")]
cards = [("Production", "The total output of goods and services."), ("Productivity", "Output per unit of input, such as output per worker."), ("Investment", "Spending on capital goods, technology or training."), ("Human capital", "Workers' skills, knowledge and health."), ("Technology", "Methods and machines that raise output."), ("Unit cost", "Cost per item produced."), ("Competitiveness", "A firm's ability to compete on price and quality."), ("Economic growth", "A rise in the economy's output."), ("Efficiency", "Using inputs without waste.")]
exam_qs = [
  Q(1, "Define", 2, "Define productivity.", "Output per unit of input.", "[K|Productivity is output per unit of input,] [K|such as output per worker per hour.]"),
  Q(2, "Explain", 4, "Explain the difference between production and productivity.", "Total vs per input.", "[K|Production is the total output of a firm or economy.] [N|For example, a factory makes 1,000 shirts a day.] [K|Productivity is output per unit of input.] [N|For example, each worker makes 20 shirts a day.]"),
  Q(3, "Explain", 4, "Explain two influences on the productivity of workers.", "Training, technology, management, motivation.", "[K|Training raises skills,] [N|so each worker produces more per hour.] [K|Better machinery and technology] [N|help workers produce more with the same effort.]"),
  Q(4, "Analyse", 6, "Analyse how an increase in investment could affect a firm's productivity and costs.", "Machinery and training; output per worker; unit cost; competitiveness.", "[K|Investment in machinery and training raises output per worker.] [N|Higher productivity lowers unit costs.] [N|The firm can cut prices or increase profit and become more competitive.] [E|Investment is costly and takes time to pay off, so benefits depend on demand and how well the new equipment is used.]", key=True),
]
tips_ = [("Production is total; productivity is per input.", "Use a number example."), ("Calculate output ÷ workers.", "Show working."), ("Investment raises productivity and growth.", "Machinery and training."), ("Evaluate: costs and time.", "Investment is not free.")]
real_items = [("Japan's manufacturing", "Heavy investment in robots and training gave high productivity.", "Investment."), ("Remote and online tools", "Software helps office workers do more in the same time.", "Technology."), ("Farm mechanisation", "Tractors and harvesters raise output per farmer.", "Capital."), ("Staff training programmes", "Well-trained staff make fewer errors and work faster.", "Human capital.")]
review("ig-production-productivity", "p353", "3.5.3", "Production and Productivity", "The difference between production and productivity, what influences them and how investment affects productivity. Syllabus 3.5.3.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Analyse"], real_items)
