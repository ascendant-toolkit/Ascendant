"""AS syllabus 4.4.4-4.4.5 Causes and consequences of economic growth. Run: python3 tools/artifact-kit/mk_as47.py"""
from asx import *
EY = EYAS("4.4.4 to 4.4.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Economic growth has <b>demand-side</b> causes, a rise in <b>aggregate demand</b> (consumption, investment, government spending or net exports) that uses up spare capacity, and <b>supply-side</b> causes, an increase in <b>productive capacity</b> from more or better <b>labour</b>, <b>capital</b>, <b>technology</b>, <b>enterprise</b> and <b>infrastructure</b>, which shifts <b>LRAS</b> right and allows <b>sustained</b> growth. The <b>consequences</b> can be good: <b>higher living standards, lower unemployment, higher tax revenue</b> to fund public services, and more resources for investment and development. They can also be bad: <b>inflation</b> if demand outruns capacity, a <b>current account deficit</b> as imports rise, <b>environmental damage and resource depletion</b>, widening <b>inequality</b>, and congestion. Whether the consequences are positive depends on the <b>source</b> and <b>speed</b> of the growth and on <b>who gains</b>.</p></div>

  <h2>1 · Causes of economic growth (4.4.4)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Causes</th><th>Effect on the diagram</th></tr>
    <tr><td><b>Demand-side (short run)</b></td><td>Lower interest rates, tax cuts, rising confidence, higher government spending, export growth, a weaker currency</td><td>AD shifts right; real output rises, most when there is spare capacity</td></tr>
    <tr><td><b>Supply-side (long run)</b></td><td>More workers (population, immigration, participation); better education and training; <b>net investment</b> in capital; <b>technology</b> and R&amp;D; <b>enterprise</b>; <b>infrastructure</b>; new resources; <b>mobility</b> of factors</td><td>LRAS (and SRAS) shift right; potential output rises; the PPC moves outward</td></tr>
  </table></div>
  <ul>
    <li><b>Sustained growth</b> needs supply-side improvements. Demand-led growth in an economy at full capacity just raises prices.</li>
    <li><b>Measuring the impact</b> of each cause is difficult: the <b>informal economy</b> hides output, causes interact, and time lags are long.</li>
    <li><b>Internal causes</b> (investment, education, technology) and <b>external causes</b> (export demand, commodity prices, foreign investment, world growth) both matter.</li>
  </ul>

  <h2>2 · Consequences of economic growth (4.4.5)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Possible benefits</th><th>Possible costs</th></tr>
    <tr><td><b>Higher living standards</b> (income per head, consumption)</td><td><b>Inflation</b> if AD grows faster than capacity</td></tr>
    <tr><td><b>Lower unemployment</b> as more workers are needed</td><td><b>Current account deficit</b>: rising incomes suck in imports</td></tr>
    <tr><td><b>Higher tax revenue</b>, so more for health, education, welfare and a lower budget deficit</td><td><b>Environmental damage</b>, pollution, resource depletion and climate change</td></tr>
    <tr><td><b>More investment</b> and development; reduced absolute poverty</td><td><b>Inequality</b> may widen; structural unemployment as industries change</td></tr>
    <tr><td>Greater consumer choice; firms' profits rise</td><td>Congestion, longer working hours, loss of leisure; unsustainable boom and bust</td></tr>
  </table></div>
  <ul>
    <li><b>Evaluation:</b> growth is usually beneficial if it is <b>supply-led</b>, <b>sustainable</b> and its gains are <b>widely shared</b>; it is more harmful if it is demand-led near full capacity, based on depleting resources, or raises inequality.</li>
    <li>Compare <b>actual</b> growth (using spare capacity) with <b>potential</b> growth (more capacity), and look at <b>GDP per head</b> and the distribution of income.</li>
  </ul>

  <h2>3 · Worked example: demand-led and supply-led growth</h2>
  <p>Take AD as P = 120 − Y, SRAS as P = 20 + Y and potential output as 70, so equilibrium is Y = 50, P = 70.</p>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Change</th><th>New equilibrium</th><th>Effect on growth and prices</th></tr>
    <tr><td><b>Demand-led</b>: lower interest rates raise AD by 20</td><td>AD: P = 140 − Y</td><td>Y = 60, P = 80</td><td>Output +20%, prices +14%. Uses spare capacity; some inflation</td></tr>
    <tr><td><b>Supply-led</b>: training and technology raise SRAS by 20 (and LRAS)</td><td>SRAS: P = Y</td><td>Y = 60, P = 60</td><td>Output +20%, prices −14%. Potential output rises: sustained growth</td></tr>
    <tr><td><b>Both together</b></td><td>AD and SRAS shift right</td><td>Y = 70, P = 70</td><td>Output +40%, price level unchanged</td></tr>
  </table></div>
  <ul>
    <li>Supply-led growth is better for the economy because it increases output <b>without</b> inflationary pressure and raises potential output.</li>
    <li>Demand-led growth is faster and cheaper to achieve, but only works while there is spare capacity.</li>
  </ul>

  <h2>4 · Causes in more detail</h2>
  <ul>
    <li><b>Labour:</b> a larger workforce (more migration or participation) and better skills raise output. Education and health spending are investments in human capital.</li>
    <li><b>Capital:</b> net investment in machinery, buildings and infrastructure raises productive capacity and productivity.</li>
    <li><b>Technology and innovation:</b> new methods let the same inputs produce more.</li>
    <li><b>Enterprise and competition:</b> encourages new firms and efficiency.</li>
    <li><b>Institutions:</b> stable government, property rights and a good legal system encourage investment.</li>
    <li><b>International trade and investment:</b> access to bigger markets, specialisation and inward foreign investment raise growth; rising commodity prices raise export income in some countries.</li>
    <li><b>Which cause is more important?</b> It depends: in a recession, higher AD matters most; for long-run growth, investment, technology and skills are more important. The impact of each is hard to measure, because causes interact and some output is unrecorded.</li>
  </ul>

  <h2>5 · Consequences: how they arise</h2>
  <div class="tw"><table class="t">
    <tr><th>Consequence</th><th>How it arises</th><th>For whom</th></tr>
    <tr><td><b>Higher living standards</b></td><td>More output per person and higher incomes</td><td>Households</td></tr>
    <tr><td><b>Lower unemployment</b></td><td>Firms need more workers to produce more</td><td>Workers; government (less welfare spending)</td></tr>
    <tr><td><b>Higher tax revenue</b></td><td>Higher incomes and spending raise tax receipts at the same rates</td><td>Government: more for health, education and a smaller deficit</td></tr>
    <tr><td><b>Inflation</b></td><td>AD grows faster than capacity, labour shortages raise wages</td><td>Savers, people on fixed incomes; competitiveness</td></tr>
    <tr><td><b>Current account deficit</b></td><td>Higher incomes raise import spending</td><td>The external sector, the exchange rate</td></tr>
    <tr><td><b>Environmental damage</b></td><td>More production and consumption raise pollution and use up resources</td><td>Future generations; people near polluted areas</td></tr>
    <tr><td><b>Inequality</b></td><td>The gains may go mainly to those with skills or capital</td><td>Poorer households</td></tr>
  </table></div>

  <h2>6 · Is growth always beneficial?</h2>
  <ul>
    <li><b>Sustainable growth</b> meets present needs without reducing future capacity: it considers resource use and pollution.</li>
    <li>Growth is more beneficial when it is <b>supply-led</b>, uses <b>clean</b> technology, creates <b>jobs</b> and is <b>widely shared</b>.</li>
    <li>It is less beneficial when it is <b>demand-led near full capacity</b>, leads to <b>inequality</b>, or damages the <b>environment</b> faster than it raises living standards.</li>
    <li><b>For the government,</b> growth raises revenue and cuts welfare costs, but increases demand for public services and infrastructure. <b>For the people,</b> the effect depends on jobs, prices and the distribution of income.</li>
    <li><b>In developing countries,</b> growth is often essential to reduce poverty; in high-income countries, the costs (pollution, congestion) may weigh more.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For 'always positive' questions, give <b>both</b> sides and then say <b>when</b> growth is more or less beneficial: depending on its source, the economy's spare capacity and who benefits. Do not just list.</div>
'''

watch = '''
  <h2>1 · Demand-led and supply-led growth</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · The virtuous circle of growth</h2>
  <div id="stV"></div>
'''

explore = '''
  <h2>Lab 1 · Sources of growth</h2>
  <p>Growth in potential output depends on more labour, more capital and better productivity or technology. Change each source and see the total.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Contribution: labour</small><strong id="r1"></strong></div><div><small>Contribution: capital</small><strong id="r2"></strong></div><div><small>Growth in potential output</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bars of the contributions of labour, capital and technology to growth"></svg></div></div></div>

  <h2>Lab 2 · Is the growth beneficial?</h2>
  <p>Set the rate of growth, the economy's spare capacity and how much of the growth comes from higher productive capacity.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Inflation pressure</small><strong id="t1"></strong></div><div><small>Current account effect</small><strong id="t2"></strong></div><div><small>Overall</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars showing demand-led growth against spare capacity"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Cause or consequence?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the virtuous circle in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Investing in education and technology", "A country spends heavily on schools and research. Workers become more skilled and firms adopt better methods, so potential output rises. This is supply-side growth, which can last without causing inflation.", "supply-side causes and LRAS shifting right.") +
rw("A consumer boom", "Low interest rates and confidence lead households to borrow and spend. If the economy has spare capacity, output and jobs rise. If it does not, prices rise and the extra spending sucks in imports.", "demand-led growth and its costs.") +
rw("Rapid industrial growth", "A fast-growing economy raises incomes and cuts poverty, but factories and traffic raise air pollution and use up natural resources. The benefits are real, but so are the environmental costs.", "positive and negative consequences.") +
rw("Growth in a few sectors", "If growth is concentrated in mining or finance, a small group may gain most. Average income rises, but inequality widens and workers in declining industries may become unemployed.", "growth and the distribution of income.") +
rw("Investment in education and technology", "A country invests heavily in schools, universities and research. Productivity rises over decades, shifting LRAS right and supporting sustained growth, though the cost is large and the payoff slow.", "supply-side causes of growth.") +
rw("A boom in exports", "Strong foreign demand for a country's exports raises AD, so output and jobs grow. But rising incomes also pull in imports and may raise inflation if capacity is tight.", "an external demand-side cause, and its consequences.")
)

mc_exam = [
  mcq("s24_12", 18, "Which change affecting an economy's labour force will cause an increase in economic growth in the short run?", ["an increase in students entering university", "an increase in the birth rate", "an increase in the immigration of skilled labour", "an increase in the school leaving age"], 2, "Skilled immigrants can start work at once, raising output in the short run. The other changes take years."),
  mcq("s23_12", 30, "Economic growth leads to increased levels of income and consumption per capita for the adult population. Which circumstances are needed for this to happen in an economy?", ["a change in technology that maintains the same level of output", "an increase in economic efficiency through higher productivity of factor inputs", "a policy of progressive taxation to reduce inequalities", "a rise in the size of the working population due to immigration"], 1, "Higher productivity raises output per head. A larger population need not raise income per head."),
  mcq("s23_13", 24, "Which government action is least likely to prevent a fall in economic growth?", ["additional controls on commercial banks' lending", "relaxation of rules for immigration of adult population", "removal of trade barriers on import of raw materials", "training and education of workforce"], 0, "Tighter controls on lending reduce credit and spending, so they are least likely to support growth."),
  mcq("s24_12", 20, "What is true about a government's macroeconomic objectives?", ["Economic growth ensures a more even distribution of income", "Increasing output ensures that more workers are employed", "Choosing between macroeconomic objectives requires a normative decision", "A stable rate of inflation means zero inflation is required"], 2, "Choosing between objectives (such as growth against inflation) involves value judgements.")
]

exam = exam_page("the causes and consequences of economic growth",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Growth is one of the most common Paper 2 topics: an 8 mark part on causes and a 12 mark assessment of whether growth is always beneficial in most series, plus short data-response parts. Reworded past questions are below, with four Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "May/June 2025 (23) Q4(a); Oct/Nov 2024 (21) Q4(a)"), ("Essay parts, 12 marks", "4", "Feb/March 2023 (22) Q4(b); Feb/March 2024 (22) Q5(b); May/June 2025 (23) Q4(b); May/June 2023 (22) Q3(b)"), ("Data response, 6 marks", "1", "Oct/Nov 2023 (21) Q1(e)"), ("Multiple choice (Paper 1)", "4 shown below", "2023 to 2024")],
  [
  eq(P("s25_23", "4(a)"), "8 marks", "Explain two causes of economic growth and consider the extent to which their impact can be measured.",
     ["Knowledge (up to 3): economic growth is the increase in the real value of goods and services produced in an economy over time (1); an explanation of two causes, such as an increase in AD (higher real wages, direct tax cuts, lower interest rates) or increases in LRAS (increased investment, increased productivity) (1 + 1).",
      "Analysis (up to 3): an explanation of how each cause increases economic growth (1 + 1), for example reductions in income tax raise disposable income, AD and growth, though if job insecurity is high the increase may be less; or alternatively that the ability to measure the impact is affected by the size of the hidden or informal economy (1).",
      "Evaluation (up to 2): the extent to which the causes can be measured, such as the size of the informal economy, with a justified conclusion (1)."],
     "Define growth. Two causes, each explained: one demand-side (lower interest rates), one supply-side (investment). Measurement: informal economy, lags.",
     [[("k", "Economic growth is an increase in the real value of goods and services produced in an economy over time. Lower interest rates are one cause, because they make borrowing cheaper and so raise consumption and investment, shifting AD to the right. Increased investment in machinery and technology is another, because it raises productivity and shifts LRAS to the right.")], [("n", "Lower interest rates raise AD, so real GDP rises if there is spare capacity. Investment raises productive capacity, so potential output grows. Each increases real GDP, but the extent can be hard to measure: causes work together, there are time lags, and output in the informal economy is not recorded.")], [("e", "The impact of each cause can be estimated, for example from changes in investment and in GDP, but it cannot be measured exactly because of the hidden economy and because of other influences. So the measurement is approximate.")]]),
  eq(P("w24_21", "4(a)"), "8 marks", "Explain two possible causes of economic growth and consider whether the consequences of economic growth for an economy will always be positive.",
     ["Knowledge (up to 3): what is meant by economic growth (1) and two causes, such as an increase in the number of workers, better education and training, research and development, technology, investment in capital stock, mobility of factors or new export markets (up to 2).",
      "Analysis (up to 3): the possible positive and negative consequences of growth, such as a higher standard of living and lower unemployment, but also inflation, a worse current account, environmental damage and inequality.",
      "Evaluation (up to 2): a judgement on whether the consequences will always be positive, with a conclusion."],
     "Growth defined. Two causes. Consequences: higher living standards, jobs, but inflation, imports, environment, inequality. Judge: not always.",
     [[('k', 'Economic growth is an increase in real GDP over time. One cause is investment in capital stock, such as machines, factories and infrastructure, which raises productive capacity, so output can rise. A second is better education and training, which raises the quality and productivity of labour, so each worker produces more. Other causes include technology, an increase in the number of workers and new export markets.')], [('n', 'The consequences of growth are often positive. Living standards rise, because real incomes are higher and people can buy more, unemployment may fall as firms need more workers, and higher tax revenue lets the government spend more on health, education and welfare.'), ('n', 'However, the consequences are not always positive. If AD grows faster than capacity, there may be demand-pull inflation. Higher incomes raise spending on imports, which can widen the current account deficit. The gains may go mainly to richer households, so inequality can increase, and more production may cause pollution, congestion and the depletion of resources, which reduces quality of life and sustainability.')], [('e', 'So the consequences are not always positive. They depend on the type of growth: growth from higher productivity and investment is more likely to be sustainable and non-inflationary than growth from rising AD at full capacity. They also depend on how the gains are shared and whether the government manages the environmental costs. Overall, growth is likely to bring more benefits than costs in most economies, but not always, and the positive effects are not guaranteed.')]]),
  eq(P("m23_22", "4(b)"), "12 marks", "Assess whether the consequences of economic growth for an economy are always positive.",
     ["Analysis (up to 8): the positive consequences, such as higher living standards, lower unemployment, higher tax revenue and more resources for public services (up to 4); the negative consequences, such as inflation, a current account deficit, environmental damage and inequality (up to 4).",
      "Evaluation (up to 4): a judgement on whether the consequences are always positive, depending on the type of growth, the economy's spare capacity and who benefits, with a conclusion."],
     "Positives: living standards, jobs, tax revenue. Negatives: inflation, imports, environment, inequality. Judge: depends on source, capacity and distribution.",
     [[('k', 'Economic growth is an increase in real GDP over time, measured as the percentage change in real national output. It can be shown by an outward shift of the LRAS curve or PPC.')], [('n', 'The positive consequences are that real incomes and living standards rise, since people can buy more goods and services. Firms need more workers to produce the extra output, so employment rises and unemployment falls. Higher incomes and profits raise tax revenue without raising tax rates, and spending on unemployment benefits falls, so the government can spend more on health, education and infrastructure, or reduce the deficit. Growth may also raise business confidence and encourage investment.'), ('n', 'However, the consequences may be negative. Growth that comes from rising AD in an economy with little spare capacity pushes up prices, which causes demand-pull inflation. Higher incomes raise spending on imports and may widen a current account deficit. More output can cause pollution, congestion and the depletion of resources, so quality of life may fall and future generations may be harmed. The benefits may go mainly to the wealthy, so inequality may widen, and some workers may lose their jobs as industries change.')], [('e', 'Whether the consequences are always positive depends on the type of growth and how it is managed. Growth that is based on productivity, technology and investment, and that raises LRAS, can be sustained without inflation. Growth that is shared widely and that is combined with environmental policies has more positive consequences than growth that is unequal and polluting. Also, the time period matters, since some costs only appear in the long run.'), ('e', 'Overall, the consequences are mostly positive, because growth raises living standards and jobs, but they are not always positive, since inflation, inequality and environmental costs can offset the gains.')]]),
  eq(P("m24_22", "5(b)"), "12 marks", "Assess whether economic growth is always desirable for an economy.",
     ["Analysis (up to 8): the meaning of economic growth; the potential benefits for an economy: higher incomes, a reduction in unemployment, improved government finances, increased international competitiveness, increases in consumer and business confidence, increased life expectancy; the costs of economic growth: inflation, current account deficits, inequality, pollution.",
      "Evaluation (up to 4): consideration that fully assesses the relative perspectives of economic growth for an economy and arrives at a reasoned conclusion on which viewpoint is most likely."],
     "Benefits: incomes, jobs, tax revenue, competitiveness. Costs: inflation, current account deficit, inequality, pollution. Judge: depends on source and how it is shared.",
     [[('k', 'Economic growth is an increase in real GDP over time, that is, an increase in the output of goods and services after allowing for inflation. It can be shown by an outward shift of the PPC or LRAS curve.'), ('n', "The potential benefits are that incomes and living standards rise, so people can buy more goods and services. Firms need more workers, so unemployment falls, and rising incomes lift tax revenue, so governments can spend more on health and education, or reduce borrowing. Growth may raise consumer and business confidence, encourage investment, improve a country's international competitiveness, and increase life expectancy through better health care.")], [('n', "However, growth has costs. If AD grows faster than the economy's capacity, demand-pull inflation can result. Higher incomes raise spending on imports, which can worsen a current account deficit. The benefits may go mainly to the wealthy, so inequality may widen. More output can mean more pollution, congestion and depletion of non-renewable resources, which reduce quality of life and impose costs on future generations.")], [('e', 'Whether growth is desirable depends on the type of growth, who gains and the time period. Growth that results from investment and productivity, and that is shared widely, is more likely to be sustainable and desirable, while growth that is based on using up resources or that mainly benefits a few may not be. For a poor country, where many people lack basic needs, growth is very desirable, but in a rich country, the extra costs may be greater than the benefits.'), ('e', 'Overall, economic growth is usually desirable, but not always, since its value depends on whether it is sustainable, how it is distributed and whether the costs are managed.')]]),
  eq(P("s25_23", "4(b)"), "12 marks", "Assess the extent to which economic growth is always beneficial for the people and government in an economy.",
     ["Analysis (up to 8): potential benefits, for example higher real GDP per capita and a better quality of life, more jobs as firms need more workers, more tax revenue without raising tax rates so the government can invest in public services such as healthcare and education, and more investment and consumption as expectations about future income and profits rise; potential costs, for example growth that disproportionately benefits the wealthy and widens the gap between rich and poor, and higher pollution and depletion of natural resources.",
      "Evaluation (up to 4): a judgement on the extent to which growth is beneficial to the people and the government, with a conclusion."],
     "People: income, jobs, quality of life; inequality, pollution. Government: revenue, spending; costs of services, deficit. Judge: depends on distribution and sustainability.",
     [[('n', 'For the people, economic growth raises average real incomes, so households can buy more goods and services and quality of life can improve. Firms need more workers to produce extra output, so jobs are created and unemployment may fall. Rising incomes widen consumer choice and may allow people to afford better health care and education. For the government, higher incomes and profits raise tax revenue without raising tax rates, so it can spend more on public services such as hospitals and schools, or reduce borrowing. Expectations of higher future incomes and profits also encourage further consumption and investment, which supports further growth.')], [('n', 'However, growth is not always beneficial. The gains may go mainly to the wealthy, for example owners of firms or skilled workers, which widens the gap between rich and poor, so many people may see little improvement. Extra production can cause pollution, congestion and the depletion of resources, which lowers quality of life and imposes costs on future generations. Rapid growth could also raise demand-pull inflation, pull in more imports and worsen the current account, and require large government spending on infrastructure.')], [('e', 'The extent to which growth is beneficial depends on how it is shared, whether it is sustainable and what causes it. Growth that comes from investment and productivity is more likely to be sustainable and to help both groups than growth that comes from drawing down natural resources. The effect on the government also depends on whether the extra revenue is used well.'), ('e', 'Overall, growth is usually beneficial for most people and for the government, but not always: its benefits are greatest when it is shared widely and is environmentally sustainable, and are weaker when inequality and pollution rise sharply.')]]),
  eq(P("s23_22", "3(b)"), "12 marks", "Entrepreneurs are vital in a modern economy to achieve long run economic growth. Assess whether encouraging entrepreneurship or increasing another of the factors of production will be a more effective way to achieve long run economic growth.",
     ["Analysis (up to 8): the advantages of encouraging entrepreneurship: entrepreneurs organise the other three factors of production; they take risks and receive profit, which motivates success and stimulates growth; they must be creative and innovative, raising productive potential and so long-run growth, shown by a shift of the PPC to the right; modern economies are dynamic and need to respond quickly to change, which successful entrepreneurs can do; there may be a cost in training and educating future entrepreneurs; and the advantages and disadvantages of increasing another factor of production.",
      "Evaluation (up to 4): a judgement on which approach is more effective, with a conclusion."],
     "Enterprise: organises, takes risk, innovates; training cost. Another factor, such as labour or capital: skills, investment. Judge: factors complement each other.",
     [[('n', 'Entrepreneurs organise land, labour and capital, take risks in the hope of profit and are creative and innovative. By introducing new products and cheaper methods of production, they raise the productive potential of the economy, shifting the PPC to the right and raising long-run growth. Profit motivates success, so a successful entrepreneur may expand and employ more workers, and the competition they create pushes other firms to improve. Modern economies are dynamic and need to respond quickly to change, which entrepreneurs can do. Encouraging enterprise through tax breaks, grants and training may therefore raise growth. However, it is costly to train entrepreneurs, many new businesses fail, and the results are uncertain and may take years.')], [('n', 'Increasing another factor can also raise growth. More capital, through investment in machinery and technology, raises labour productivity; more or better-educated labour increases the labour force and its skills; discovering natural resources raises potential output. These factors are often easier to plan and measure than enterprise: for example, a government can fund investment or education directly. However, without entrepreneurs to organise and use them effectively, extra capital and labour may be underused, or produce goods that do not meet demand, and there are diminishing returns when one factor is increased and the others are fixed.')], [('e', 'The judgement depends on the economy. In a modern, developed economy that already has high capital and skills, extra enterprise is likely to be the better route because innovation drives further growth, whereas in a developing economy short of capital and skills, investment in capital and education may be more effective first. The factors are also complementary, so the best approach may be to combine them.'), ('e', 'Overall, encouraging entrepreneurship is probably the most effective way to achieve long-run growth in a modern economy, because it drives innovation and makes the best use of the other factors, but it works best where capital, labour and a stable economic environment are also in place.')]]),
  eq(P("w23_21", "1(e)"), "6 marks", "Assess the possible consequences of a higher rate of economic growth for an economy such as Taiwan.",
     ["Analysis (up to 4): positive consequences (up to 2): increased expenditure such as on education and health care, a higher standard of living, more jobs, higher incomes and less poverty; negative consequences (up to 2): more pressure on available resources with possible environmental effects such as congestion and pollution.",
      "Evaluation (up to 2): weighing up the consequences on both sides (1) to reach a conclusion on the likely overall effect (1)."],
     "Positive: spending on services, living standards, jobs, incomes. Negative: pressure on resources, congestion, pollution. Judge overall.",
     [[('n', 'A higher rate of growth in an economy such as Taiwan raises real incomes, so living standards improve and poverty is likely to fall. Firms produce more and need more workers, so jobs are created. Higher incomes and profits raise tax revenue, which allows the government to spend more on education and health care, and may raise productivity further. Exports are likely to rise, bringing in foreign currency.')], [('n', 'However, faster growth puts more pressure on resources. Greater output means more use of land, energy and raw materials, with possible pollution, congestion in cities and loss of green space, which reduces quality of life and has costs for future generations. Growth may also widen inequality if the gains go mainly to skilled workers or owners of firms, and may raise inflation if AD grows faster than capacity.'), ('e', 'On balance, the consequences are likely to be positive, particularly for incomes and employment, and a developed economy such as Taiwan can afford to invest in cleaner technology. But the environmental costs could become more serious if growth is rapid, so the overall effect depends on how well the government manages the costs.')]])
  ],
  )

tips = tips_html(
  [("Split causes into demand and supply.", "AD shifts versus LRAS shifts."),
   ("Name two causes and explain each.", "Do not just list factors."),
   ("Actual versus potential growth.", "Using spare capacity versus raising capacity."),
   ("Give both sides of consequences.", "Benefits and costs."),
   ("Say when growth is beneficial.", "Supply-led, sustainable, shared."),
   ("Mention measurement.", "The informal economy, lags, interacting causes."),
   ("Use GDP per head and distribution.", "Who gains?")],
  [("Growth", "Economic growth is an increase in real GDP over time."),
   ("Demand-led", "Growth driven by AD may raise inflation if capacity is limited."),
   ("Supply-led", "Higher productive capacity shifts LRAS to the right."),
   ("Consequences", "Growth may raise living standards but harm the environment."),
   ("Assess", "The consequences are not always positive: it depends on the source of growth.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
function gcDraw(s) { return adasPlot({ a: s.a, s: s.s, l: s.l, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifting right and LRAS and SRAS shifting right">${gcDraw({ a: 20, s: 15, l: 15, n: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 300, label: "Demand-led and supply-led growth", base: { a: 0, s: 0, l: 0, n: 0 }, draw: gcDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is at output 50, below potential output of 75: there is spare capacity.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Demand-led growth.</b> Lower interest rates shift AD to the right. Real output rises to about 60 and prices rise a little. Growth uses up spare capacity.", s: { a: 20, s: 0, l: 0, n: 1 } },
  { cap: "<b>Supply-led growth.</b> Investment and better education shift SRAS and LRAS to the right. Potential output rises to 90, so the economy can keep growing without inflation.", s: { a: 20, s: 15, l: 15, n: 1 } },
] });

function vcDraw(s) {
  const bx = (x, y, t, k, v) => SV.rect(x, y, 170, 52, k, { rx: 8, ...op(0.55 * v) }) + SV.text(x + 85, y + 31, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
  const ar = (x1, y1, x2, y2, d, v) => SV.line(x1, y1, x2, y2, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y2, d, "dot4");
  let o = bx(60, 40, "Economic growth", "f3", s.a) + ar(232, 66, 330, 66, "r", s.b) + bx(335, 40, "Higher incomes and tax revenue", "f1", s.b) + ar(505, 66, 560, 66, "r", s.c) + bx(565, 40, "Spending on education, health, roads", "f2", s.c);
  o += ar(650, 94, 650, 150, "d", s.d) + bx(565, 155, "Higher productive capacity", "f1", s.d) + ar(560, 181, 235, 181, "l", s.e) + bx(60, 155, "LRAS shifts right: more growth", "f3", s.e);
  if (s.f > 0) o += SV.text(380, 255, "Costs to weigh: inflation, imports, pollution, inequality", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)", ...op(s.f) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 280" role="img" aria-label="A virtuous circle from growth to higher incomes and tax revenue, public spending, capacity and more growth">${vcDraw({ a: 1, b: 1, c: 1, d: 1, e: 1, f: 1 })}</svg>`;
Lib.stepper($("#stV"), { w: 760, h: 280, label: "The virtuous circle of economic growth", base: { a: 0, b: 0, c: 0, d: 0, e: 0, f: 0 }, draw: vcDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>Economic growth</b> raises real output.", s: { a: 1 } },
  { cap: "<b>Higher incomes and tax revenue.</b> People earn more, and the government collects more tax without raising rates.", s: { a: 1, b: 1 } },
  { cap: "<b>More public spending</b> on education, health care and infrastructure becomes affordable.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Productive capacity rises:</b> a healthier, more skilled workforce and better infrastructure.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>LRAS shifts right,</b> making further growth possible: a virtuous circle.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
  { cap: "<b>But there are costs to weigh:</b> inflation if demand outruns capacity, a worse current account, pollution and inequality. Growth is not always positive.", s: { a: 1, b: 1, c: 1, d: 1, e: 1, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labG() {
  if (!["lb", "cp", "tf"].every((i) => $("#" + i))) return;
  const l = +$("#lb").value, c = +$("#cp").value, t = +$("#tf").value, a = 0.6 * l, b = 0.4 * c, tot = a + b + t;
  $("#r1").textContent = Lib.fmtN(a, 1) + " pts"; $("#r2").textContent = Lib.fmtN(b, 1) + " pts"; $("#r3").textContent = Lib.fmtN(tot, 1) + "%";
  $("#rv").textContent = `Labour growth of ${l}% (weight 0.6) adds ${Lib.fmtN(a, 1)} points, capital growth of ${c}% (weight 0.4) adds ${Lib.fmtN(b, 1)}, and productivity or technology adds ${t}. Potential output grows ${Lib.fmtN(tot, 1)}% a year. ${t >= a + b ? "Most growth comes from productivity, which is the most sustainable source." : "Most growth comes from adding more labour and capital, which can be limited."}`;
  const Y = (v) => 250 - v * 28; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30) + SV.text(46, 26, "Growth (% points)", "sm"), y = 250;
  [["Labour", a, "f1"], ["Capital", b, "f2"], ["Technology", t, "f3"]].forEach(([n, v, k]) => { const h = v * 28; o += SV.rect(130, y - h, 140, h, k, op(0.65)) + (h > 14 ? SV.text(200, y - h / 2 + 5, n + " " + Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" }) : ""); y -= h; });
  o += SV.text(200, 270, "Total " + Lib.fmtN(tot, 1) + "%", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "lb", label: "Growth in the labour force, % ", min: 0, max: 4, step: 0.5, value: 1.5, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "cp", label: "Growth in the capital stock, % ", min: 0, max: 8, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g3"), { id: "tf", label: "Productivity and technology, % points ", min: 0, max: 4, step: 0.5, value: 1, fmt: (v) => v + "%", onInput: labG });
labG();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!["gg", "sp", "sh"].every((i) => $("#" + i))) return;
  const g = +$("#gg").value, sp = +$("#sp").value, sh = +$("#sh").value / 100, dem = g * (1 - sh), infl = Math.max(0, dem - sp / 2), ca = -0.45 * g;
  $("#t1").textContent = infl < 0.3 ? "Low" : infl < 2 ? "Moderate" : "High"; $("#t2").textContent = Lib.fmtN(ca, 1) + "% of GDP"; $("#t3").textContent = infl < 0.3 && sh > 0.4 ? "Mostly positive" : infl < 2 ? "Mixed" : "Risky";
  $("#tv").textContent = `${g}% growth, ${Lib.fmtN(sh * 100, 0)}% of it from higher capacity, so ${Lib.fmtN(dem, 1)} points are demand-led. With spare capacity of ${sp}% the economy can absorb about ${Lib.fmtN(sp / 2, 1)} points without much inflation, leaving inflation pressure of ${Lib.fmtN(infl, 1)}. Higher incomes also raise imports, which could worsen the current account by about ${Lib.fmtN(-ca, 1)}% of GDP. ${infl > 2 ? "The growth is likely to be inflationary and may not be sustainable." : "The growth looks reasonably sustainable."}`;
  let o = SV.line(40, 180, 400, 180); [["Total growth", g, "f1"], ["Demand-led", dem, "f3"], ["Absorbable", sp / 2, "f2"]].forEach(([n, v, k], i) => (o += SV.rect(70 + i * 110, 180 - v * 18, 80, v * 18, k, op(0.65)) + SV.text(110 + i * 110, 200, n, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, 174 - v * 18, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Real GDP growth, % ", min: 1, max: 9, step: 1, value: 5, fmt: (v) => v + "%", onInput: labB });
Lib.slider($("#g5"), { id: "sp", label: "Spare capacity in the economy, % of GDP ", min: 0, max: 12, step: 1, value: 4, fmt: (v) => v + "%", onInput: labB });
Lib.slider($("#g6"), { id: "sh", label: "Share of growth from higher productive capacity, % ", min: 0, max: 100, step: 10, value: 30, fmt: (v) => v + "%", onInput: labB });
labB();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Benefit or cost of growth?", ["Possible benefit", "Possible cost"],
  [("Higher living standards", 0), ("Inflation when near full capacity", 1), ("Lower unemployment", 0), ("Pollution and resource depletion", 1), ("Higher tax revenue", 0), ("A bigger current account deficit", 1), ("More resources for health and education", 0), ("Widening inequality", 1)],
  "Growth can raise incomes and jobs but may bring inflation, imports, environmental damage and inequality.") + MATCH([
  ["Demand-led growth", "A rise in AD that uses up spare capacity"],
  ["Supply-led growth", "A rise in productive capacity: LRAS shifts right"],
  ["Net investment", "Spending on capital that adds to the capital stock"],
  ["Productivity", "Output per worker or per unit of input"],
  ["Informal economy", "Unrecorded output, which makes growth hard to measure"],
  ["Sustainable growth", "Growth that can continue without harming future output"]]) + ORDER(
  "Put the virtuous circle of growth in order.",
  ["Economic growth raises output", "Incomes and tax revenue rise", "The government spends more on education and infrastructure", "Productive capacity rises", "LRAS shifts right and growth continues"],
  "Growth, revenue, investment in capacity, more growth.") + CALC([
  {"q": "Labour grows 2% (weight 0.6), capital grows 5% (weight 0.4) and technology adds 1 point. What is growth in potential output (%)?", "a": 4.2, "unit": "%", "tol": 0.1, "hint": "1.2 + 2.0 + 1.", "sol": "<b>4.2%</b>."},
  {"q": "What share of that growth comes from technology (%)?", "a": 23.8, "unit": "%", "tol": 0.3, "hint": "1 ÷ 4.2.", "sol": "<b>23.8%</b>."},
  {"q": "Real GDP grows 5% and imports have an income elasticity of 1.5 with imports at 30% of GDP. By roughly what % of GDP do imports rise?", "a": 2.25, "unit": "%", "tol": 0.1, "hint": "7.5% × 0.3.", "sol": "Imports rise 7.5%, which is <b>2.25%</b> of GDP."},
  {"q": "Real GDP is $400bn. After growth of 3.5% it is: ($bn)", "a": 414, "unit": "$bn", "tol": 0.5, "hint": "400 × 1.035.", "sol": "<b>$414bn</b>."}]) + MCQ([
  ("Which is a supply-side cause of growth?", ["Investment in capital goods", "A cut in interest rates", "A rise in government spending", "A depreciation"], 0, "It raises capacity."),
  ("Demand-led growth is most likely to cause inflation when:", ["The economy is near full capacity", "There is much spare capacity", "AD is falling", "Unemployment is high"], 0, "Output cannot rise."),
  ("A possible consequence of growth is:", ["A rise in imports", "A fall in tax revenue", "A fall in living standards for all", "No change in demand"], 0, "Higher incomes raise import spending."),
  ("Growth is more sustainable when it comes from:", ["Higher productivity", "Borrowing to spend", "Running down natural resources", "Rising prices"], 0, "Higher capacity."),
  ("Growth is measured by the change in:", ["Real GDP", "Nominal GDP", "Prices", "Exports"], 0, "Real, not nominal.")
], "qz1") + CARDS([
  ("Demand-side", "AD shifts right."),
  ("Supply-side", "LRAS shifts right."),
  ("Benefits", "Living standards, jobs, tax revenue."),
  ("Costs", "Inflation, imports, environment, inequality."),
  ("Sustainable", "Productivity-led."),
  ("Measure", "Informal economy limits it."),
  ("Actual growth", "Uses spare capacity."),
  ("Judge", "Source, capacity, distribution.")]) + MCQ(mc_exam)

build("as47", "as-causes-consequences-of-growth", "Causes and Consequences of Economic Growth", EY,
  "4.4.4 to 4.4.5: demand-side and supply-side causes of economic growth, and its possible benefits and costs. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
