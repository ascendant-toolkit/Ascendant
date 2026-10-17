"""AS syllabus 3.1.1 Reasons for government intervention (detailed rebuild). Run: python3 tools/artifact-kit/mk_as30.py"""
from as6k import *
EY = EYAS("3.1.1")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>The <b class="kw">price mechanism</b> allocates resources well when buyers and sellers are well informed and every good can be sold to those who pay for it, but in some markets it produces an <b>inefficient allocation of resources</b>, which is called <b class="kw">market failure</b>, and that is the main reason governments intervene. <b class="kw">Public goods</b> are <b>non-excludable and non-rival</b>, so the <b>free rider problem</b> means private firms cannot earn revenue and the free market does not supply them. <b class="kw">Merit goods</b> are better for people than they realise and so are <b>under-consumed</b>, and <b class="kw">demerit goods</b> are worse for people than they realise and so are <b>over-consumed</b>, both mainly because of <b class="kw">imperfect information</b> (and also income, price and addiction). Governments also fix <b>maximum prices</b> to make essentials affordable and <b>minimum prices</b> to protect producers' incomes, secure food supplies or discourage demerit goods. Intervention has an <b>opportunity cost</b> and can fail, so a good answer explains the reason for intervening and then considers whether the intervention is likely to work.</p></div>

  <h2>1 · The starting point: when the market fails</h2>
  <ul>
    <li>The price mechanism rations scarce resources and signals to producers what consumers want. Resources go where they are most valued, and an <b>efficient allocation of resources</b> results if consumers know what they are buying and producers can charge for what they supply.</li>
    <li><b>Market failure</b> is an inefficient allocation of resources by the free market. The market produces too much of some goods, too little of others, or none at all.</li>
    <li>That gives a government a <b>reason</b> to intervene. This page is about the reasons; the methods (taxes, subsidies, direct provision, regulation) are in Syllabus 3.2.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Reason for intervention</th><th>What the free market does</th><th>Why</th><th>Typical goods</th></tr>
    <tr><td><b>Public goods</b></td><td>Does not supply them</td><td>Non-excludable and non-rival, so free riders</td><td>Street lighting, flood defences, defence</td></tr>
    <tr><td><b>Merit goods</b></td><td>Under-consumes and under-provides</td><td>Imperfect information, low income, high price</td><td>Education, healthcare, vaccinations</td></tr>
    <tr><td><b>Demerit goods</b></td><td>Over-consumes and over-provides</td><td>Imperfect information, addiction, low price</td><td>Tobacco, alcohol, harmful drugs</td></tr>
    <tr><td><b>Information failure</b></td><td>Consumers choose badly</td><td>Imperfect or asymmetric information</td><td>Health, insurance, used goods</td></tr>
    <tr><td><b>Unaffordable essentials</b></td><td>Price too high for some</td><td>Scarcity or market power</td><td>Bread, rent, water</td></tr>
    <tr><td><b>Unstable producer incomes</b></td><td>Price swings</td><td>Supply uncertain, inelastic demand</td><td>Wheat, rice, coffee</td></tr>
  </table></div>

  <h2>2 · Public goods and the free rider problem</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Non-excludable:</b> once the good is provided, nobody can be stopped from using it, even if they have not paid.</li>
    <li><b>Non-rival:</b> one person's use does not reduce the amount available to others.</li>
    <li><b>Free rider problem:</b> because people can use the good without paying, many will not pay, so a private firm cannot earn enough revenue to cover its costs, will make a loss, and will not supply it, even if the benefit to society is greater than the cost.</li>
    <li><b>Government provision:</b> the state provides public goods and pays for them from tax revenue, so that everyone contributes. The good is free at the point of use, but it is not free to society: it has an <b>opportunity cost</b>.</li>
    <li><b>Quantity is hard to judge:</b> because people do not reveal how much they value the good, the government may not know how much to provide, which can lead to over- or under-provision.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Type of good</th><th>Excludable?</th><th>Rival?</th><th>Opportunity cost?</th><th>Example</th></tr>
    <tr><td><b>Private good</b></td><td>Yes</td><td>Yes</td><td>Yes</td><td>A pizza, a phone</td></tr>
    <tr><td><b>Public good</b></td><td>No</td><td>No</td><td>Yes</td><td>Flood barrier, street lights</td></tr>
    <tr><td><b>Free good</b></td><td>No</td><td>No</td><td>No (unlimited supply)</td><td>Sunshine, air</td></tr>
    <tr><td><b>Merit good</b></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Education, healthcare</td></tr>
  </table></div>
  <ul>
    <li><b>Public good or free good?</b> Both are non-excludable and non-rival, but a public good costs resources to produce, while a free good has zero opportunity cost.</li>
    <li><b>Can the market ever supply public goods?</b> Sometimes. Technology or fees can make a good excludable (a toll road, a ticketed beach, encrypted TV), which turns it into a private good, and charities may fund some. Pure public goods such as national defence are rarely supplied this way.</li>
    <li><b>Merit goods are not public goods.</b> Education and healthcare can be charged for and used up by one person, so a market can supply them, but it supplies too little.</li>
  </ul>

  <h2>3 · Merit goods: under-consumption</h2>
  <ul>
    <li><b>Definition:</b> a merit good is a good that is thought to be more beneficial to consumers than they realise, so it is under-consumed and under-provided by the free market.</li>
    <li><b>Why consumers under-consume them:</b> <b>imperfect information</b> (they do not appreciate the full value, for example of education or vaccinations), <b>low income</b> (they cannot afford them) and a <b>high price</b>.</li>
    <li><b>Why firms under-provide them:</b> firms supply only if they can earn a profit, which is less likely where many people cannot pay.</li>
    <li><b>Why the state provides them:</b> they are <b>essential</b>, many people cannot pay, and the whole society gains from a healthier, more educated population, which supports growth and a fairer distribution of income.</li>
    <li><b>Provided by both sectors:</b> because the cost to the state of providing all of it may be too high, many countries rely on private providers as well, especially for healthcare in low and middle-income countries.</li>
    <li><b>Extension (not required at AS):</b> economists also explain merit goods through positive externalities, where others gain from your consumption.</li>
  </ul>
  <div id="pic2" class="card"></div>

  <h2>4 · Demerit goods: over-consumption</h2>
  <ul>
    <li><b>Definition:</b> a demerit good is a good that is thought to be worse for consumers than they realise, so it is over-consumed and over-provided by the free market.</li>
    <li><b>Why consumers over-consume them:</b> <b>imperfect information</b> about the health risks, <b>addiction</b> or habit, <b>low prices</b>, low income and poor education, and peer influence.</li>
    <li><b>Why firms over-provide them:</b> the products are profitable, and sellers have little incentive to warn consumers about the harm.</li>
    <li><b>Why the state intervenes:</b> to protect health, reduce healthcare costs and raise the productivity of the workforce. These benefits can outweigh the loss of tax revenue from lower sales.</li>
    <li><b>Some goods are both:</b> a plastic bottle is a private good (excludable, rival) and a demerit good, as its use can harm the environment.</li>
    <li><b>Extension (not required at AS):</b> negative externalities give another explanation.</li>
  </ul>
  <div id="pic3" class="card"></div>

  <h2>5 · Information failure</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Imperfect (incomplete) information</b></td><td>Consumers do not know the full costs or benefits</td><td>Smokers underestimating health risks</td></tr>
    <tr><td><b>Asymmetric information</b></td><td>One side of the market knows more than the other</td><td>A seller knows a used car's faults; a doctor knows more than a patient</td></tr>
    <tr><td><b>Misleading information</b></td><td>Advertising or labelling creates false beliefs</td><td>Sugary foods marketed as healthy</td></tr>
  </table></div>
  <ul>
    <li>Information failure leads consumers to <b>misjudge the true value</b> of a good, so they buy too much of demerit goods and too little of merit goods.</li>
    <li>Governments respond with <b>information campaigns</b>, labelling, regulation or direct provision (covered in 3.2).</li>
  </ul>

  <h2>6 · Why governments control prices</h2>
  <div id="pic4" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Maximum price (ceiling)</th><th>Minimum price (floor)</th></tr>
    <tr><td><b>Meaning</b></td><td>Legal limit on how high a price can go</td><td>Legal limit on how low a price can go</td></tr>
    <tr><td><b>To be effective</b></td><td>Set below the equilibrium price</td><td>Set above the equilibrium price</td></tr>
    <tr><td><b>Aims</b></td><td>Make essentials affordable for low-income households, protect consumers in emergencies, attract key workers (rent control), control inflation</td><td>Support farmers' incomes, secure food supplies, discourage consumption of demerit goods (minimum alcohol price), protect low-paid workers (minimum wage)</td></tr>
    <tr><td><b>Market effect</b></td><td>Quantity demanded rises and quantity supplied falls: shortage</td><td>Quantity supplied rises and quantity demanded falls: surplus</td></tr>
    <tr><td><b>Who gains</b></td><td>Consumers who can buy at the low price</td><td>Producers who sell at the higher price</td></tr>
    <tr><td><b>Who loses and problems</b></td><td>Those who cannot find the good; queues, rationing, black markets, lower quality, less supply</td><td>Consumers pay more and buy less; surplus must be bought or stored; resources are wasted</td></tr>
  </table></div>

  <h2>7 · Other reasons you may meet</h2>
  <ul>
    <li><b>Equity:</b> governments may intervene so that everyone has access to essentials whatever their income.</li>
    <li><b>Employment and growth:</b> a healthier, better-educated workforce is more productive.</li>
    <li><b>Protecting vulnerable groups and consumers</b> from harm, exploitation and unsafe products.</li>
    <li>Externalities, monopoly power and macroeconomic stability are also reasons in A Level work, but the AS mark schemes focus on the reasons above.</li>
  </ul>

  <h2>8 · Does intervention always work?</h2>
  <ul>
    <li><b>Opportunity cost:</b> money spent on provision cannot be spent elsewhere, especially where the tax base is small.</li>
    <li><b>Information:</b> the government may not know which goods to provide or how much.</li>
    <li><b>Cost and efficiency:</b> state provision may be wasteful without the profit motive, and free provision can cause excess demand and waiting.</li>
    <li><b>Unintended consequences:</b> price controls create shortages or surpluses and may help the wrong people.</li>
    <li><b>Behaviour:</b> if people still do not see the benefits of a merit good, making it free may not raise consumption; time, travel or waiting costs can also deter use.</li>
    <li><b>Political aims and time lags</b> can lead to poorly chosen or late action.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For "explain why" questions, name the <b>market failure</b> first (for example information failure), say <b>who</b> lacks <b>what</b>, give an <b>example</b>, and state the <b>result</b> (under- or over-consumption). Use "may" and "likely". Only then move to the methods, which are covered in 3.2.</div>
'''

watch = '''
  <h2>1 · The free rider problem</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · A merit good is under-consumed</h2>
  <div id="stB"></div>
  <h2>3 · A demerit good is over-consumed</h2>
  <div id="stC"></div>
  <h2>4 · Information failure to over-consumption</h2>
  <div id="stD"></div>
  <h2>5 · Why governments fix prices</h2>
  <div id="stE"></div>
'''

explore = '''
  <h2>Lab 1 · Merit and demerit goods</h2>
  <p>Choose the type of good, then set how far consumers misjudge the true benefit or harm. The first curve is what consumers think; the second is the true value.</p>
  <div class="card"><div class="grid2"><div><div id="b1" class="btnrow"></div><div id="g1"></div>
    <div class="readout"><div><small>Market quantity</small><strong id="r1"></strong></div><div><small>Desirable quantity</small><strong id="r2"></strong></div><div><small>Gap</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Perceived and true demand for a merit or demerit good with the market and desirable quantities"></svg></div></div></div>

  <h2>Lab 2 · Would a private firm supply it?</h2>
  <p>A good costs $200 000 a year to provide. Choose how many people use it, what it is worth to each, and what share of users can be made to pay.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Total benefit to society</small><strong id="t1"></strong></div><div><small>Revenue a firm can collect</small><strong id="t2"></strong></div><div><small>Tax per person to fund it</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars comparing the cost, the benefit and the revenue a private firm could collect"></svg></div></div></div>

  <h2>Lab 3 · Price controls</h2>
  <p>Demand: P = 90 − 0.8Q, supply: P = 10 + 0.8Q, so equilibrium is price 50, quantity 50. Move the control price.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div>
    <div class="readout"><div><small>Quantity demanded</small><strong id="c1"></strong></div><div><small>Quantity supplied</small><strong id="c2"></strong></div><div><small>Shortage or surplus</small><strong id="c3"></strong></div></div>
    <div class="verdict" id="cv"></div></div>
    <div><svg id="labC" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with a price control and the resulting shortage or surplus"></svg></div></div></div>
''' + chooser_html("h", "Lab 4 · Which reason is it?", "Choose a situation to see which reason for intervention it illustrates.", ["Reason", "What goes wrong in a free market", "Typical government response"])

practise = '''
  <h2>1 · What kind of good is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which reason does each statement give?</h2><div id="cl2" class="card"></div>
  <h2>3 · Build the argument for providing public goods</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Education in Sub-Saharan Africa", "Education is a merit good and would be under-provided if left to the private sector. In many low and lower middle-income countries governments provide education directly or subsidise it, and may make it compulsory. Sub-Saharan Africa has some of the highest rates of children not in education, mainly because of poverty. Kenya has made government education free from primary to high school, with subsidies for boarding fees for low-income families.", "an example of a merit good, information failure and the limits of funding. Evaluate with opportunity cost.") +
rw("Healthcare reform in Pakistan", "Pakistan's government has promised to reform healthcare so that quality care is available to all, not only those who can pay private providers. The main issues are funding with a limited tax base, building hospitals in rural areas, preventative care such as immunisation, and regulating private and state providers.", "healthcare as a merit good, provided by both sectors, with real funding constraints.") +
rw("Vaccination programmes", "Governments often offer vaccinations free because individuals may not appreciate the benefit, cost may deter some, and wide coverage protects the whole population. A vaccine is a private good, but protection against the spread of disease works much like a public good.", "merit goods, information failure and why intervention can raise overall welfare.") +
rw("Smoking bans and graphic warnings", "Many countries ban smoking in public places and require health warnings and graphic photographs on packaging. Governments justify this to protect health, make the workforce more productive and cut healthcare spending. These arguments have usually outweighed the loss of tax revenue from falling tobacco sales.", "cigarettes as the standard demerit good, with information failure as the reason.") +
rw("Lighthouses, street lighting and flood defences", "These are classic public goods. Everyone nearby benefits and nobody can be stopped from benefiting, so private firms cannot charge and the government pays from taxation.", "a lighthouse or flood barrier as a clear example of both characteristics of a public good.") +
rw("A beach or park", "A beach that is open to everyone looks like a public good. But if an entry fee is charged, or visitor numbers can be limited, it becomes excludable, and if it becomes overcrowded it is rival. It may then be better described as a private good.", "the difference between a public good and a good that merely looks free.") +
rw("Bread price ceilings", "In some former socialist economies, basic foods such as bread were given a maximum price to protect low-income households. The price was held below the market level, and shortages and queues were common.", "a maximum price example. State the aim (affordability) and explain the consequences.") +
rw("Rent controls for key workers", "Rent controls aim to provide affordable housing for low-income families and to attract key workers such as nurses and teachers to areas with high housing costs. Where rent is held below the equilibrium, the supply of rented housing may fall and demand exceed supply.", "an aim for a maximum price other than low income, linked to shortages in Syllabus 3.2.") +
rw("Wheat and rice price floors", "Many governments support farmers' incomes with a minimum price for key crops such as wheat and rice. Farm incomes are unpredictable because supply is uncertain, and governments also want to keep food supplies secure.", "a minimum price example. Evaluate: farmers gain, consumers pay more and it can be an inefficient use of resources.") +
rw("Minimum unit pricing for alcohol", "Scotland introduced a minimum price per unit of alcohol in 2018 to reduce harmful drinking. It targets cheap, strong drinks, but its effect depends on how many drinkers respond to the higher price and on whether they switch to other products.", "a minimum price used for a demerit good, and the question of whether it is the best policy.")
)

mc_exam = [
  mcq("s20_13", 3, "Which type of good is healthcare?", ["demerit", "free", "merit", "public"], 2, "Healthcare is more beneficial than consumers realise, so it is a merit good."),
  mcq("s20_11", 3, "Consumers do not use enough of a product to maximise their private benefit because they have imperfect information about the product. How would an economist classify this product?", ["demerit good", "free good", "merit good", "public good"], 2, "Under-consumption caused by imperfect information is the mark of a merit good."),
  mcq("s21_11", 3, "Which type of good would be over-consumed because of information failure?", ["demerit", "inferior", "merit", "public"], 0, "Consumers underestimate the harm of demerit goods and so buy too much."),
  mcq("m24_12", 13, "What explains the underconsumption of merit goods?", ["Their value is not fully understood by consumers.", "They are unproductive goods and services.", "They can only be provided by the government.", "They are only provided by private sector businesses."], 0, "Imperfect information means consumers do not see their full value."),
  mcq("m24_12", 4, "What is the main reason an economy is unlikely to rely completely on market forces to allocate resources?", ["Demerit goods will be over supplied.", "Merit goods will be under supplied.", "Private goods will not be supplied.", "Public goods will not be supplied."], 3, "Public goods cannot be sold, so the market does not provide them at all."),
  mcq("m21_12", 18, "Why is national defence provided by the government?", ["In a free market it is excludable and rival in consumption.", "In a free market it is non-excludable and non-rival in consumption.", "The government has perfect information, so it can set the correct quantity required.", "The private sector firm would charge a high price for its use as it is a necessity."], 1, "Non-excludability and non-rivalry mean a private firm could not charge for it."),
  mcq("s25_12", 3, "What is a statement of the non-rivalrous nature of public goods?", ["It is not possible to stop a non-payer from using the product.", "One person consuming the product does not reduce the amount of it available to others.", "People consume too little of the product because they are unaware of its true benefits.", "There is an unlimited supply of the product."], 1, "Non-rival means one person's use does not reduce what is available to others."),
  mcq("s21_13", 14, "In many countries there are goods that must be provided directly by the government. What would be the most convincing argument for such provision?", ["The consumption of these products may be beneficial.", "The production of these products may be harmful.", "The production of these products have high opportunity costs.", "These products are non-rival in consumption and non-excludable."], 3, "A good that is non-rival and non-excludable will not be supplied by the market."),
  mcq("s25_12", 13, "Why might governments provide free education for children aged 4 to 16 years old?", ["Consumers are not fully aware of the benefits of education.", "Education in a free market system would be over consumed.", "Education is a public good and there would be many free riders.", "The private costs of education exceed the private benefits in a free market."], 0, "Education is a merit good, under-consumed because people do not see its full benefits."),
  mcq("s21_12", 18, "Education from 4 to 16 years of age in most developed economies is provided at zero price, financed from taxation. Why should the government do this?", ["In a free market, consumers have imperfect information so do not realise the full personal benefit of education.", "In a free market, education is not considered to be a private good.", "In a free market, consumers will be unwilling to pay for education.", "In a free market, education is non-rival and non-excludable in consumption so zero output would be produced."], 0, "Imperfect information leads to under-consumption of a merit good."),
  mcq("s25_13", 13, "A flood-control dam is an example of a good provided directly by a government. Which statement relating to the direct provision of a flood-control dam is not correct?", ["It allows the government to tackle the failure to provide public goods.", "It forces the government to incur an opportunity cost.", "It involves the supply of a merit good.", "It is an example of government allocation of resources."], 2, "A flood-control dam is a public good, not a merit good."),
  mcq("s24_13", 12, "A government introduces an effective minimum price for a product but makes no other intervention in the market. This policy suggests that the government's objective is", ["to discourage consumption of a demerit good.", "to increase the consumption of a merit good.", "to reduce the price of a private good.", "to support the incomes of producers."], 0, "A minimum price raises price and reduces consumption, which fits a demerit good. Supporting producers' incomes is also possible, but the answer key gives the demerit good aim."),
  mcq("m22_12", 16, "The National Library Board of Singapore is a public sector organisation that finances and manages the state libraries. What is the most likely reason for this?", ["Libraries are public goods.", "Libraries are merit goods.", "The cost of providing library services would be greater in the private sector.", "The opportunity cost to the public sector of providing library services is zero."], 1, "Libraries are excludable and rival, so they are merit goods, not public goods."),
  mcq("m23_12", 1, "A good is most suitable to be provided by the market if it is", ["excludable and non-rival.", "excludable and rival.", "non-excludable and non-rival.", "non-excludable and rival."], 1, "A private good can be charged for and used up, so the market can supply it."),
  mcq("s25_11", 5, "How can a public good become a private good?", ["Consumers are dissatisfied with the performance of state-run services.", "New technological developments make the good excludable.", "The government privatises the industry producing the good.", "The price of the good increases so it becomes more profitable."], 1, "If a way is found to exclude non-payers, the good can be sold."),
  mcq("w20_12", 2, "Which statement is correct?", ["Private goods are both non-rival and non-excludable.", "Private goods are only provided by the private sector.", "Public goods are both non-rival and non-excludable.", "Public goods do not incur opportunity costs."], 2, "That is the definition of a public good.")
]

exam = exam_page("reasons for government intervention",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). This topic is among the most common in Paper 2: 8 mark parts on public goods, merit and demerit goods and information failure, and 12 mark parts on provision and price controls. The mark schemes note that externalities are not on the AS syllabus. Reworded past questions are below, with sixteen Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "7", "Oct/Nov 2022 (23) Q2(a); May/June 2023 (23) Q3(a); May/June 2022 (23) Q2(a); Oct/Nov 2020 (21) Q2(a); May/June 2025 (23) Q3(a); May/June 2020 (22) Q4(a); Oct/Nov 2023 (21) Q3(a)"), ("Essay parts, 12 marks", "3", "Oct/Nov 2022 (23) Q2(b); May/June 2023 (21) Q2(b); May/June 2020 (22) Q4(b)"), ("Multiple choice (Paper 1)", "16 shown below", "2020 to 2025")],
  [
  eq(P("w22_23", "2(a)"), "8 marks", "Explain why demerit goods are over-consumed and merit goods are under-consumed.",
     ["Knowledge (up to 2): demerit goods are thought to be undesirable or worse for consumers than they realise (1) and merit goods are thought to be desirable or better for them than they realise (1).",
      "Application (up to 6): demerit goods are often over-consumed because of imperfect information (1), with an example (1) and further development, such as low income, poor education, low prices and addiction (1); merit goods are often under-consumed because of imperfect information (1), with an example (1) and further development, such as low income or high prices (1). Externalities are not on the AS syllabus but may be rewarded."],
     "Define merit and demerit goods. Demerit: imperfect information about health risks, addiction, low price. Merit: benefits not appreciated, low income, high price. Examples for each.",
     [[("k", "A demerit good is one that is worse for consumers than they realise, and a merit good is one that is better for them than they realise.")], [("n", "Demerit goods such as cigarettes may be over-consumed because consumers lack full information about the health risks, and addiction, low prices or low income and poor education could make this worse, so people buy more than is best for them. Merit goods such as education may be under-consumed because many people do not appreciate the full benefits, for example higher future earnings, and low income or high prices could prevent some from paying for them, so too little is consumed.")]]),
  eq(P("s23_23", "3(a)"), "8 marks", "Explain why government intervention may be required to provide merit goods and consider why such intervention may not always be successful.",
     ["Knowledge (up to 3): government intervention takes place when markets fail (1); the nature of information failure (1); examples of merit goods (1).",
      "Analysis (up to 3): reasons for government provision, including the essential nature of merit goods (1), the private sector being unwilling to provide them fully (1), the problem of payment (1) and the benefits to society and the economy (1); 1 mark for each example that is explained.",
      "Evaluation (up to 2): governments may lack the resources to provide enough merit goods, or enough information on which to provide; one mark reserved for a justified conclusion."],
     "Market failure: information failure, under-provision. Reasons: essential, private sector unwilling, cost to individuals, social benefits. Limits: resources, information.",
     [[("k", "A merit good, such as healthcare or education, is better for consumers than they realise. Governments may intervene because markets fail when consumers lack information about the full benefits, so merit goods are under-consumed.")], [("n", "Merit goods are essential, but the private sector may be unwilling to provide them fully because many people cannot afford to pay, so provision may be too low. If the government provides them, financed by taxes, access rises, the population is healthier and better educated, and the economy may benefit through a more productive workforce.")], [("e", "Intervention may not always succeed. The government may lack the resources to provide enough, particularly where the tax base is small, or the information to know which merit goods to provide and in what quantity. Overall, intervention is likely to improve access, but its success depends on funding and how well it is targeted.")]]),
  eq(P("s22_23", "2(a)"), "8 marks", "A government has decided to spend money building a new barrier to prevent flooding across a city. Explain why this flood defence barrier is likely to meet the characteristics of a public good.",
     ["Knowledge (up to 2): the difference between a private good and a public good by reference to excludability (1) and rivalry (1).",
      "Application (up to 6): that a flood defence system is a public good (1), why it is non-excludable (1) and why it is non-rival (1); that it cannot be a private good (1), with accurate reference to both excludability and rivalry (1) and the free rider problem (1)."],
     "Private good: excludable and rival. Public good: neither. Flood barrier: nobody can be excluded, one person's protection does not reduce another's. Free riders, so no private provision.",
     [[("k", "A private good is excludable, so non-payers can be stopped from using it, and rival, so one person's use reduces what is left for others. A public good is non-excludable and non-rival.")], [("n", "A flood barrier protects everyone in the city. It is non-excludable because it is impossible to protect only those who paid, and non-rival because one household's protection does not reduce the protection of others. It cannot be a private good, since it could neither be sold to some people only nor used up. Because people can benefit without paying, there is a free rider problem, so a private firm could not raise enough revenue, and the government is likely to fund it from taxation.")]]),
  eq(P("w20_21", "2(a)"), "8 marks", "Explain, with the help of examples, how imperfect information among consumers affects their consumption of merit goods and demerit goods.",
     ["Knowledge (up to 2): knowledge and understanding of imperfect information in relation to a merit good and a demerit good, with suitable examples. Merit goods are private goods, rival and excludable, with benefits to the individual, such as education or healthcare; demerit goods are rival and excludable and potentially damaging, such as alcohol or tobacco.",
      "Application (up to 6): the application of imperfect information to the under-consumption of a merit good (up to 3) and to the over-consumption of a demerit good (up to 3)."],
     "Merit: consumers do not fully appreciate the value, so under-consumed and under-produced. Demerit: consumers do not understand the dangers, so over-consumed and over-produced. Examples.",
     [[("k", "Imperfect information means consumers lack full knowledge of the costs or benefits of a product. Merit goods such as education and healthcare are rival and excludable and good for the individual; demerit goods such as tobacco are rival and excludable and potentially damaging.")], [("n", "With merit goods, consumers may not fully appreciate the value of education or preventive healthcare, so they buy too little and the market under-produces them. With demerit goods, consumers may not fully understand the dangers of tobacco or alcohol, or may underestimate them, so they buy too much and the market over-produces them.")]]),
  eq(P("s25_23", "3(a)"), "8 marks", "Explain what is meant by a merit good, why governments provide merit goods such as healthcare free of charge and consider why such provision may not always be successful.",
     ["Knowledge (up to 3): a merit good is thought to be desirable but is under-provided or under-consumed (1) because of information failure or a lack of awareness (1); by providing healthcare free of charge the government encourages greater consumption and improves overall welfare (1).",
      "Analysis (up to 3): some healthcare services, such as vaccinations, act as public goods because they are non-excludable and non-rival, so the private sector will not provide them (1); governments provide them to prevent under-provision and protect public health (1); government provision removes financial barriers, ensuring fair access and reducing inequality (1).",
      "Evaluation (up to 2): provision may not always succeed if individuals still do not see the benefits (1), or if time, travel or waiting costs discourage people from using free services (1)."],
     "Merit good: under-consumed due to information failure. Free healthcare: more consumption, public health, fair access. Limits: people may still not see the benefit; time, travel and waiting costs.",
     [[("k", "A merit good, such as healthcare, is better for consumers than they realise, so a free market under-provides it because of information failure. By providing healthcare free of charge, the government encourages consumption and raises overall welfare.")], [("n", "Services such as vaccinations may act like public goods, as protection spreads to others, so the private sector may not provide enough of them. Government provision protects public health, removes financial barriers so that poorer people can use services, and so reduces inequality.")], [("e", "It may not always succeed. If people still do not appreciate the benefits of healthcare, making it free may not raise consumption by much, and time, travel and waiting costs may deter some people even when there is no charge. Funding limits can also reduce quality.")]]),
  eq(P("s20_22", "4(a)"), "8 marks", "Explain, using examples, the difference between private goods and public goods and why public goods will not be supplied by private enterprise.",
     ["Knowledge (up to 2): the distinction between the two types of good based on excludability (1) and rivalry in consumption (1).",
      "Application (up to 6): why public goods will not be supplied in a free market because of non-excludability and the lack of rivalry in consumption (4 marks), with due reference to the free rider issue (2 marks)."],
     "Private: excludable and rival (food). Public: non-excludable and non-rival (street lights). Private firms cannot charge, free riders, so no revenue and no supply.",
     [[("k", "A private good, such as a loaf of bread, is excludable, because only those who pay get it, and rival, because once eaten it is not available to others. A public good, such as street lighting, is non-excludable and non-rival.")], [("n", "A private firm needs to charge for what it supplies. With street lighting, everyone who lives nearby benefits whether they pay or not, so the firm cannot exclude non-payers, and one person's use does not reduce what is available to others. This creates the free rider problem, as people have no reason to pay voluntarily, so the firm would not earn revenue to cover its costs and would not supply the good. The government therefore provides it and funds it from taxation.")]]),
  eq(P("w23_21", "3(a)"), "8 marks", "Explain why a government might decide to increase its direct provision of essential goods and services and consider whether such a policy is always likely to be successful.",
     ["Knowledge (up to 3): the role of the state in providing essential goods and services, such as merit goods (1); these could include education and healthcare (1); and they could be financed from taxation (1).",
      "Analysis (up to 3): up to 2 marks for explaining each essential good or service the government might provide directly (a maximum of 3 marks), with 1 mark for a good or service with limited explanation.",
      "Evaluation (up to 2): a valid judgement on whether an increase in direct provision will always be successful in achieving its objectives, with a conclusion."],
     "Essential goods: education, healthcare, food, shelter. Why: market under-provides, people cannot pay, social benefits. Limits: cost, waste, excess demand.",
     [[("k", "Essential goods and services such as education and healthcare are merit goods. The government can provide them directly and finance them from taxation.")], [("n", "A government may provide education directly because many households could not afford it and might not appreciate its value, so the free market would under-provide it. It may provide healthcare directly because access would otherwise depend on ability to pay, and a healthier population is more productive. It might also provide food or housing for low-income households to ensure a basic standard of living.")], [("e", "Direct provision is not always successful. It has an opportunity cost, may lead to waste or excess demand and long waiting times, and may be underfunded if the tax base is small. Its success depends on how efficiently the money is spent.")]]),
  eq(P("w22_23", "2(b)"), "12 marks", "Education and healthcare are considered to be merit goods. Discuss why merit goods are provided by both the private sector and the public sector.",
     ["Analysis (up to 8): why merit goods are provided by the public sector (up to 4), because of information failure leading to under-consumption and under-production, and positive effects on society; and why they are also provided by the private sector (up to 4), often because the cost to the public sector is too great or cannot be met in full, as in healthcare in many low and middle-income countries. No marks for merely explaining what a merit good is.",
      "Evaluation (up to 4): considers why merit goods are likely to be provided by both sectors, with a reasoned conclusion."],
     "Public: information failure, essential, cannot pay, social benefits. Private: state cannot afford it all, choice and quality, those who can pay. Judge: a mixed supply is likely.",
     [[("n", "The public sector provides education and healthcare because consumers may not appreciate their full benefits, so a free market under-supplies them, and because many people cannot afford them. Free or subsidised provision widens access and raises the productivity of the workforce. The private sector also provides them because the government may not have enough funds to supply all of the demand, particularly in low and middle-income countries, and some people are willing to pay for higher quality, shorter waiting times or more choice, which allows firms to earn a profit.")], [("e", "A mixture of both sectors is likely, because the state can ensure basic access while private providers add capacity and choice. The balance may depend on the country's income, tax base and the efficiency of public provision.")]]),
  eq(P("s23_21", "2(b)"), "12 marks", "Assess whether education should be classified as a public good rather than classified as a merit good.",
     ["Analysis (up to 8): education is a merit good because it is a private good with the characteristics of being rival and excludable, so it can be provided through a market because it is possible to charge a price, although it can also be provided by the state; a public good is non-rival and non-excludable, so it is difficult or impossible to charge a price because of the free rider problem, and it therefore has to be provided by the state.",
      "Evaluation (up to 4): public goods can only be provided by the state; merit goods are under-provided by the free market and governments should intervene; if demand for education is extremely low, a government could provide it entirely through the state; a conclusion that education should be classified as a merit good rather than a public good."],
     "Merit good: rival and excludable, can be charged for, under-consumed. Public good: neither, free riders. Education is rival (class size) and excludable (fees), so merit.",
     [[("n", "Education is a private good because it is rival, as a place in a class is used by one student and limited by teachers and space, and excludable, as schools can charge fees and exclude those who do not pay. Because a price can be charged, a market can provide it, although many people undervalue it, so it is a merit good and tends to be under-consumed. A public good is both non-excludable and non-rival, so nobody could be charged because of free riders, and only the government could provide it. Education does not meet these characteristics.")], [("e", "Education should therefore be classified as a merit good, not a public good. The government may still provide it mainly or entirely itself, particularly if demand is very low in a country, but that is because of under-consumption and ability to pay, not because it is a public good.")]]),
  eq(P("s20_22", "4(b)"), "12 marks", "Consider the problem of the provision of merit goods in a market economy and assess whether direct provision of such goods is the most effective way to deal with this problem.",
     ["Analysis (up to 8): the under-production and under-consumption of merit goods because of information failure in a market economy (up to 4); a comparison of direct provision with at least one alternative, such as subsidising these goods or public education campaigns (up to 4).",
      "Evaluation (up to 4): a judgement on whether direct provision is the most effective way to deal with the problem, with a conclusion."],
     "Problem: information failure, under-consumption. Direct provision: free access, but cost, waste, excess demand. Alternatives: subsidy, information campaigns. Judge by cost and effect.",
     [[("n", "In a market economy merit goods such as healthcare are under-produced and under-consumed because consumers lack information about their full benefits and many cannot afford them. Direct provision, financed by taxes, can ensure everyone has access, but it has a high opportunity cost, may be wasteful and may lead to excess demand and waiting. A subsidy lowers the price and encourages private provision, but it may not reach those who most need it and may still leave consumers unaware of the benefits. Information campaigns tackle the cause, imperfect information, and are cheap, but they may take time and may not change behaviour much.")], [("e", "Direct provision may be the most effective for essential goods where many cannot pay, but it is costly, so a combination of provision, subsidies and information may be more effective and affordable. The best approach is likely to depend on the good and the country's resources.")]])
  ],
  )

tips = tips_html(
  [("Define market failure properly.", "An inefficient allocation because the price mechanism fails."),
   ("Use both characteristics of a public good.", "Non-excludable and non-rival, then the free rider problem."),
   ("Information failure is the key AS reason.", "Say who lacks what: consumers lack the full benefit or harm."),
   ("Merit under, demerit over.", "Do not swap them."),
   ("A price control only bites on the right side of equilibrium.", "Maximum below, minimum above."),
   ("Reasons before methods.", "This topic is why; 3.2 is how."),
   ("Evaluate with opportunity cost and information.", "Funding is limited and governments can fail.")],
  [("Market failure", "Market failure is an inefficient allocation of resources by the market."),
   ("Public good", "A public good is non-excludable and non-rival."),
   ("Free rider", "A free rider uses a good without paying for it."),
   ("Merit good", "A merit good is better for consumers than they realise, so it is under-consumed."),
   ("Demerit good", "A demerit good is worse for consumers than they realise, so it is over-consumed."),
   ("Imperfect information", "Imperfect information means consumers lack full knowledge of costs or benefits."),
   ("Maximum price", "A maximum price is a legal limit on how high a price can go."),
   ("Minimum price", "A minimum price is a legal limit on how low a price can go.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["discuss"], CW["assess"]]) + FC

js = SDJS + CHAINJS + '''
/* ---------- static pictures ---------- */
$("#pic1").innerHTML = (() => {
  const B = [["Private good", "Excludable and rival", 30, "f1"], ["Public good", "Non-excludable and non-rival", 270, "f3"], ["Free good", "No opportunity cost", 510, "f2"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 120, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 60, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 90, d, "sm", { "text-anchor": "middle" }); });
  o += SV.text(380, 175, "Free riders: non-payers cannot be excluded, so a firm earns no revenue and does not supply a public good", "sm", { "text-anchor": "middle" });
  return `<svg viewBox="0 0 760 200" role="img" aria-label="Private good, public good and free good compared">${o}</svg>`;
})();
const meLab = { x: "Quantity", y: "Price", D1: "Perceived demand", D2: "True value", S1: "Supply", S2: "Supply", P1: "P1", Q1: "Qm", P2: "P2", Q2: "Qd" };
function meDraw(d, n) { return sdPlot({ d, s: 0, g: 1, n }, meLab); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="True value above perceived demand for a merit good: the market quantity is below the desirable quantity">${meDraw(20, 1)}</svg>`;
$("#pic3").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="True value below perceived demand for a demerit good: the market quantity is above the desirable quantity">${meDraw(-20, 1)}</svg>`;
const ctlP = (p) => ({ qd: (90 - p) / 0.8, qs: (p - 10) / 0.8 });
function ctlDraw(p, k = 1) {
  const c = ctlP(p); let o = sdPlot({ d: 0, s: 0, g: 1, n: 0 }, { x: "Quantity", y: "Price", D1: "D", S1: "S", P1: "P*", Q1: "Q*" });
  o += SV.line(70, SDY(p), 720, SDY(p), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, SDY(p) - 6, (p < 50 ? "Maximum price " : "Minimum price ") + p, "c3", k, "end");
  if (Math.abs(p - 50) > 0.5) o += SV.line(SDX(Math.min(c.qd, c.qs)), SDY(p) + (p < 50 ? 16 : -16), SDX(Math.max(c.qd, c.qs)), SDY(p) + (p < 50 ? 16 : -16), "c4", { "stroke-width": 3, ...op(k) }) + SV.text(SDX((c.qd + c.qs) / 2), SDY(p) + (p < 50 ? 34 : -22), (p < 50 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(c.qd - c.qs), 1), "sm", { "text-anchor": "middle", ...op(k) });
  return o;
}
$("#pic4").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A maximum price below equilibrium creates a shortage">${ctlDraw(35)}</svg>`;

/* ---------- steppers ---------- */
chainStep("#stA", "The free rider problem", ["A good is provided that nobody can be excluded from using", "Everyone can benefit without paying (free riders)", "Few people pay voluntarily, so a firm earns little revenue", "A private firm makes a loss and does not supply it", "The government provides it and funds it from taxation"], [
  "<b>Non-excludable and non-rival:</b> a street light or flood barrier.", "<b>Free riders:</b> if others pay, you benefit anyway, so why pay?", "<b>Revenue collapses</b> because the firm cannot charge.", "<b>Market failure:</b> the good is not supplied, though its benefit to society exceeds its cost.", "<b>Government provision</b>, with an opportunity cost: the money could be spent elsewhere."]);
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A merit good is under-consumed because consumers undervalue it", base: { d: 0, n: 0 }, draw: (s) => meDraw(s.d, s.n), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Perceived demand and supply</b> give the market quantity Qm: what consumers choose to buy.", s: { d: 0, n: 0 } },
  { cap: "<b>The true value is higher</b> than consumers realise (imperfect information), so the true-value curve lies to the right.", s: { d: 20, n: 1 } },
  { cap: "<b>The desirable quantity Qd is greater than Qm.</b> The gap is the <b>under-consumption</b> that gives the government a reason to intervene.", s: { d: 20, n: 1 } },
] });
Lib.stepper($("#stC"), { w: 760, h: 300, label: "A demerit good is over-consumed because consumers undervalue the harm", base: { d: 0, n: 0 }, draw: (s) => meDraw(s.d, s.n), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Perceived demand and supply</b> give the market quantity Qm.", s: { d: 0, n: 0 } },
  { cap: "<b>The true value is lower</b> than consumers think (they underestimate the harm), so the true-value curve lies to the left.", s: { d: -20, n: 1 } },
  { cap: "<b>The desirable quantity Qd is less than Qm.</b> The gap is the <b>over-consumption</b> that gives the government a reason to intervene.", s: { d: -20, n: 1 } },
] });
chainStep("#stD", "Information failure leads to over-consumption", ["Consumers lack full information about the harm", "They underestimate the risks and the costs to themselves", "They buy more than they would if fully informed", "The market over-provides the demerit good", "The government may provide information, tax or regulate"], [
  "<b>Imperfect information</b> is the root cause.", "<b>Addiction, habit and low prices</b> can make it worse.", "<b>Over-consumption:</b> quantity above the best level.", "<b>Firms</b> supply it because it is profitable.", "<b>Methods</b> are covered in Syllabus 3.2."]);
Lib.stepper($("#stE"), { w: 760, h: 300, label: "A maximum price and a minimum price", base: { p: 50, k: 0 }, draw: (s) => ctlDraw(s.p, s.k), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Free market:</b> equilibrium price 50 and quantity 40.", s: { p: 50, k: 0 } },
  { cap: "<b>A maximum price of 35</b> makes the good affordable (to protect low-income households). It is below equilibrium, so it is effective.", s: { p: 35, k: 1 } },
  { cap: "<b>Result:</b> quantity demanded exceeds quantity supplied, a <b>shortage</b> of 37.5 units: rationing, queues and possible black markets.", s: { p: 35, k: 1 } },
  { cap: "<b>A minimum price of 65</b> supports producers' incomes. It is above equilibrium, so it is effective.", s: { p: 65, k: 1 } },
  { cap: "<b>Result:</b> quantity supplied exceeds quantity demanded, a <b>surplus</b> of 37.5 units, which must be bought, stored or wasted.", s: { p: 65, k: 1 } },
] });

/* ---------- Lab 1 ---------- */
let meMode = 0;
function labA() {
  if (!$("#g1v")) return;
  const m = +$("#g1v").value, d = meMode === 0 ? m : -m, q1 = 50, q2 = 50 + 0.5 * d, gap = Math.abs(q2 - q1);
  $("#r1").textContent = Lib.fmtN(q1, 1); $("#r2").textContent = Lib.fmtN(q2, 1); $("#r3").textContent = Lib.fmtN(gap, 1) + (gap < 0.5 ? "" : meMode === 0 ? " under-consumed" : " over-consumed");
  $("#rv").textContent = gap < 0.5 ? "Consumers judge the good correctly, so the market quantity is about right." : meMode === 0 ? `Consumers underestimate the benefit of a merit good, so the market quantity is ${Lib.fmtN(q1, 1)} but ${Lib.fmtN(q2, 1)} is desirable: under-consumption of ${Lib.fmtN(gap, 1)}.` : `Consumers underestimate the harm of a demerit good, so the market quantity is ${Lib.fmtN(q1, 1)} but ${Lib.fmtN(q2, 1)} is desirable: over-consumption of ${Lib.fmtN(gap, 1)}.`;
  $("#labA").innerHTML = meDraw(d, 1);
}
$("#b1").innerHTML = `<button class="b pri" data-i="0">Merit good (healthcare)</button><button class="b" data-i="1">Demerit good (cigarettes)</button>`;
Lib.slider($("#g1"), { id: "g1v", label: "How far consumers misjudge the value ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labA });
$$("#b1 button").forEach((b) => (b.onclick = () => { meMode = +b.dataset.i; $$("#b1 button").forEach((x, k) => x.classList.toggle("pri", k === meMode)); labA(); }));
labA();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!["g2v", "g3v", "g4v"].every((i) => $("#" + i))) return;
  const n = +$("#g2v").value, w = +$("#g3v").value, ex = +$("#g4v").value / 100, cost = 200000, ben = n * w, rev = n * ex * w, tax = cost / n;
  $("#t1").textContent = "$" + Lib.fmtN(ben, 0); $("#t2").textContent = "$" + Lib.fmtN(rev, 0); $("#t3").textContent = "$" + Lib.fmtN(tax, 2);
  const mx = Math.max(ben, cost, rev, 1), W = (v) => (v / mx) * 280, bar = (y, lab, v, c) => SV.text(10, y + 15, lab, "sm") + SV.rect(130, y, Math.max(2, W(v)), 22, c, op(0.7));
  $("#labB").innerHTML = bar(20, "Cost", cost, "f3") + bar(70, "Benefit", ben, "f1") + bar(120, "Firm revenue", rev, "f2");
  $("#tv").textContent = ben < cost ? "The benefit to society is below the cost, so providing the good is not worthwhile." : rev >= cost ? `A private firm can charge ${Lib.fmtN(ex * 100, 0)}% of users and collect $${Lib.fmtN(rev, 0)}, enough to cover the cost, so a market could supply it.` : `The benefit ($${Lib.fmtN(ben, 0)}) exceeds the cost ($200 000), but a firm could collect only $${Lib.fmtN(rev, 0)} because most users cannot be made to pay: the free rider problem. A tax of about $${Lib.fmtN(tax, 2)} per person would fund it.`;
}
Lib.slider($("#g2"), { id: "g2v", label: "Number of users ", min: 1000, max: 20000, step: 1000, value: 10000, fmt: (v) => Lib.fmtN(v, 0), onInput: labB });
Lib.slider($("#g3"), { id: "g3v", label: "Value to each user, $ ", min: 5, max: 60, step: 5, value: 40, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g4"), { id: "g4v", label: "Share of users who can be made to pay, % ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labB });
labB();

/* ---------- Lab 3 ---------- */
function labC() {
  if (!$("#g5v")) return;
  const p = +$("#g5v").value, c = ctlP(p), gap = c.qd - c.qs;
  $("#c1").textContent = Lib.fmtN(c.qd, 1); $("#c2").textContent = Lib.fmtN(c.qs, 1); $("#c3").textContent = Math.abs(gap) < 0.5 ? "None" : (gap > 0 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(gap), 1);
  $("#cv").textContent = p === 50 ? "At the equilibrium price the market clears: no shortage or surplus." : p < 50 ? `A maximum price of ${p} is below equilibrium, so it is effective. It makes the good cheaper, but quantity demanded (${Lib.fmtN(c.qd, 1)}) exceeds quantity supplied (${Lib.fmtN(c.qs, 1)}): a shortage of ${Lib.fmtN(gap, 1)}, with rationing, queues and possible black markets.` : `A minimum price of ${p} is above equilibrium, so it is effective. It raises producers' price, but quantity supplied (${Lib.fmtN(c.qs, 1)}) exceeds quantity demanded (${Lib.fmtN(c.qd, 1)}): a surplus of ${Lib.fmtN(-gap, 1)} that must be bought, stored or wasted.`;
  $("#labC").innerHTML = ctlDraw(p, 1);
}
Lib.slider($("#g5"), { id: "g5v", label: "Control price ", min: 20, max: 80, step: 5, value: 35, fmt: (v) => v, onInput: labC });
labC();

/* ---------- Lab 4 ---------- */
chooser("h", [
  ["A private firm will not light the street", "Public good", "Non-excludable and non-rival: free riders, so no revenue and no supply", "Government provision paid for by taxes", 5],
  ["Many people skip vaccinations", "Merit good", "Imperfect information and cost lead to under-consumption", "Free provision, subsidy, information campaigns", 5],
  ["Teenagers take up smoking", "Demerit good", "Underestimated harm and addiction lead to over-consumption", "Warnings, taxes, bans, minimum prices", 5],
  ["A seller knows a used car's faults, the buyer does not", "Information failure", "Asymmetric information leads to poor choices", "Regulation, labelling, compulsory information", 4],
  ["Bread becomes unaffordable for poor households", "Maximum price case", "Price too high for low-income households", "A maximum price (with a risk of shortages)", 3],
  ["Wheat prices swing and farm incomes are unstable", "Minimum price case", "Supply is uncertain and incomes unpredictable", "A minimum price (with a risk of surpluses)", 3]
], (it) => `${it[0]}: this is ${it[1].toLowerCase()}. The market problem is that ${it[2].toLowerCase()}. A typical response is ${it[3].toLowerCase()}.`, "How clear-cut the case is");
''' + CLASSIFY("cl1", "What kind of good is it?", ["Public good", "Private good"],
  [("Street lighting", 0), ("A pizza", 1), ("A flood defence barrier", 0), ("A school textbook bought by a student", 1), ("National defence", 0), ("A ticketed concert", 1), ("A lighthouse", 0), ("A mobile phone", 1)],
  "Public goods are non-excludable and non-rival; private goods can be charged for and used up.") + CLASSIFY("cl2", "Which reason for intervention does each statement give?", ["Merit good", "Demerit good", "Price control"],
  [("Consumers do not realise the full value, so too little is consumed", 0), ("Consumers underestimate the harm, so too much is consumed", 1), ("The price must be kept low so poor households can afford it", 2), ("Farmers' incomes are unstable and need support", 2), ("Many families cannot afford it and under-use it", 0), ("It is addictive and cheap, so consumption is high", 1)],
  "Merit goods are under-consumed, demerit goods over-consumed, and price controls respond to affordability or unstable incomes.") + ORDER(
  "Put the argument for government provision of a public good in order.",
  ["The good is non-excludable and non-rival", "Non-payers cannot be stopped from using it (free riders)", "A private firm cannot earn enough revenue", "The free market does not supply it", "The government provides it, financed by taxation"],
  "Characteristics, free riders, no revenue, no supply, government provision.") + MATCH([
  ["Market failure", "An inefficient allocation of resources by the market"],
  ["Public good", "A good that is non-excludable and non-rival"],
  ["Free rider", "Someone who uses a good without paying for it"],
  ["Merit good", "A good better for people than they realise, so under-consumed"],
  ["Demerit good", "A good worse for people than they realise, so over-consumed"],
  ["Imperfect information", "Consumers lack full knowledge of costs or benefits"],
  ["Maximum price", "A legal limit on how high a price can go"],
  ["Minimum price", "A legal limit on how low a price can go"]]) + CALC([
  {"q": "A street light system costs $2 000 000 a year to provide and has 40 000 users. What tax per user would fund it ($)?", "a": 50, "unit": "$", "tol": 0.5, "hint": "2 000 000 ÷ 40 000.", "sol": "<b>$50</b> per user."},
  {"q": "Demand is P = 90 - Q and supply P = 10 + Q (a simpler model than the lab). A maximum price of 30 is set. What is the quantity demanded?", "a": 60, "unit": "", "tol": 0.5, "hint": "Q = 90 - 30.", "sol": "<b>60</b>."},
  {"q": "Using the same maximum price of 30, what is the quantity supplied?", "a": 20, "unit": "", "tol": 0.5, "hint": "Q = 30 - 10.", "sol": "<b>20</b>."},
  {"q": "What is the shortage?", "a": 40, "unit": "", "tol": 0.5, "hint": "60 - 20.", "sol": "<b>40 units</b>."},
  {"q": "A minimum price of 70 is set instead. What is the surplus?", "a": 40, "unit": "", "tol": 0.5, "hint": "Qs = 60, Qd = 20.", "sol": "<b>40 units</b>."},
  {"q": "The government buys the surplus of 40 units at the minimum price of 70. What does it cost ($)?", "a": 2800, "unit": "$", "tol": 0.5, "hint": "40 × 70.", "sol": "<b>$2800</b>."}]) + MCQ([
  ("A public good is:", ["Non-excludable and non-rival", "Excludable and rival", "Excludable and non-rival", "Non-excludable and rival"], 0, "Neither characteristic of a private good."),
  ("The free rider problem arises because:", ["Non-payers cannot be excluded", "Prices are too low", "Goods are rival", "Demand is inelastic"], 0, "Non-payers benefit anyway."),
  ("Merit goods are under-consumed mainly because of:", ["Imperfect information", "Perfect information", "Free provision", "Low production costs"], 0, "Consumers do not see the full benefit."),
  ("A demerit good is likely to be:", ["Over-consumed", "Under-consumed", "A public good", "A free good"], 0, "Harm is underestimated."),
  ("To be effective a maximum price must be:", ["Below equilibrium", "Above equilibrium", "At equilibrium", "Zero"], 0, "Otherwise it has no effect."),
  ("A minimum price above equilibrium creates:", ["A surplus", "A shortage", "Equilibrium", "No change"], 0, "Supply exceeds demand."),
  ("A free good differs from a public good because it has:", ["No opportunity cost", "A high price", "Excludability", "Rivalry"], 0, "Its supply is unlimited."),
  ("Government provision of public goods is financed by:", ["Taxation", "User fees only", "Free riders", "Advertising only"], 0, "Everyone contributes through taxes.")
], "qz1") + CARDS([
  ("Market failure", "Inefficient allocation of resources."),
  ("Public good", "Non-excludable and non-rival."),
  ("Free rider", "Uses without paying."),
  ("Merit good", "Better than people realise; under-consumed."),
  ("Demerit good", "Worse than people realise; over-consumed."),
  ("Imperfect information", "Consumers lack full knowledge."),
  ("Maximum price", "Below equilibrium; causes shortage."),
  ("Minimum price", "Above equilibrium; causes surplus."),
  ("Government failure", "Costs, poor information, unintended effects.")]) + MCQ(mc_exam)

build("as30", "as-reasons-for-intervention", "Reasons for Government Intervention in Markets", EY,
  "3.1.1: market failure, public goods and the free rider problem, merit and demerit goods, information failure and why governments control prices, with animated diagrams, labs and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
