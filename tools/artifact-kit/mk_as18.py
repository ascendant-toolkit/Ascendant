"""AS syllabus 1.6.1-1.6.2 Free goods, private (economic) goods and public goods. Run: python3 tools/artifact-kit/mk_as18.py"""
from asx import *
EY = EYAS("1.6.1 to 1.6.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">private good</b> (an <b>economic good</b>) is <b>rivalrous</b> (one person's use stops another using it) and <b>excludable</b> (non-payers can be kept out), so it is scarce, has a price and an opportunity cost. A <b class="kw">free good</b> is <b>not scarce</b>: it has <b>zero opportunity cost</b> and uses no factors of production, such as fresh air. A <b class="kw">public good</b> is <b>non-rivalrous and non-excludable</b>, so people can <b>free ride</b> and enjoy it without paying; private firms cannot make a profit supplying it, so a free market will not provide it and the <b>government</b> usually does, funded by taxation. Do not confuse a good that is <b>free of charge</b> (paid for by taxes) with a <b>free good</b>.</p></div>

  <h2>1 · Private goods, economic goods and free goods (1.6.1)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Private (economic) good</th><th>Free good</th></tr>
    <tr><td><b>Scarcity</b></td><td>Scarce: uses factors of production</td><td>Not scarce: unlimited at zero price</td></tr>
    <tr><td><b>Opportunity cost</b></td><td>Yes</td><td>None</td></tr>
    <tr><td><b>Price</b></td><td>Has a price (unless the state pays)</td><td>No price: supply equals demand at zero</td></tr>
    <tr><td><b>Rivalry and excludability</b></td><td><b>Rival</b> and <b>excludable</b>: when one person consumes it, others cannot; non-payers can be excluded</td><td>Usually no one is excluded and enjoyment does not use resources</td></tr>
    <tr><td><b>Examples</b></td><td>Bread, a haircut, a bus ride, a phone</td><td>Sunlight, fresh air, in some places sea breezes</td></tr>
  </table></div>
  <ul>
    <li>A good that costs <b>nothing at the point of use</b> is not necessarily a free good. A government vaccination programme or school lunches are free of charge to the user but use scarce resources and are paid for by taxpayers, so they have an <b>opportunity cost</b>.</li>
    <li>A good <b>provided by the government</b> is not automatically a public good: free school meals, health care and education are <b>private goods</b> (rival and excludable) that are provided free or subsidised by the state.</li>
    <li><b>Private goods are not only supplied by the private sector.</b> The state can supply private goods too.</li>
    <li>A product may be both a private good and a demerit good (for example a plastic bottle): rival and excludable, but over-consumed because of information failure (see syllabus 1.6.3 and 1.6.4).</li>
  </ul>

  <h2>2 · Public goods (1.6.2)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Characteristic</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Non-rivalrous</b></td><td>One person's use <b>does not reduce</b> the amount available to others</td><td>Many ships can use the light from a lighthouse</td></tr>
    <tr><td><b>Non-excludable</b></td><td>It is <b>impossible or impractical to stop</b> people who have not paid from using it</td><td>Everyone in a country is protected by national defence</td></tr>
  </table></div>
  <ul>
    <li><b>The free rider problem:</b> because no one can be excluded, each person has an incentive to <b>let others pay</b> and enjoy the good free. If everyone does so, <b>no one pays</b>, so revenue is zero and no firm will supply it.</li>
    <li>Therefore <b>a free market will not provide public goods</b> (<b>market failure</b>): there is no price mechanism. The <b>government</b> provides them and pays for them from <b>tax revenue</b>, which compels everyone to contribute.</li>
    <li><b>Examples:</b> national defence, street lighting, flood-control barriers, lighthouses, clean air regulations, public parks (to a degree).</li>
    <li><b>Pure public goods are rare.</b> Many goods are <b>quasi-public</b> (partly non-rival or non-excludable), such as a beach, which may be crowded (rival) or have a fee or gate (excludable). Roads, education and health care are <b>not</b> public goods in the strict sense, because they are rival and excludable.</li>
    <li><b>A public good can become a private good</b> if technology makes it excludable (for example, a toll gate or electronic charging on a motorway, or scrambled satellite signals).</li>
    <li><b>Opportunity cost:</b> provision of public goods uses scarce resources, so there is an opportunity cost even though users pay nothing directly.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Give <b>both</b> characteristics of a public good and explain the <b>free rider problem</b> to say why the market will not supply it. Use pure examples such as national defence and street lighting, not roads or schools.</div>
'''

watch = '''
  <h2>1 · Sorting goods by rivalry and excludability</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · The free rider problem</h2>
  <div id="stF"></div>
'''

explore = '''
  <h2>Lab 1 · What type of good is it?</h2>
  <p>Set how rivalrous a good is (does one person's use reduce what is left?) and how excludable it is (can non-payers be kept out?). The type of good follows.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Rivalry</small><strong id="r1"></strong></div><div><small>Excludability</small><strong id="r2"></strong></div><div><small>Type of good</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="A grid of rivalry and excludability with a marker for the chosen good"></svg></div></div></div>

  <h2>Lab 2 · Will the market provide it?</h2>
  <p>A street lamp costs $1,000 to install. Each resident values it at some amount. A private firm can only charge those it can exclude. Change the number of residents, the value each places on it and the share who can be made to pay.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Total benefit</small><strong id="t1"></strong></div><div><small>Revenue a firm can collect</small><strong id="t2"></strong></div><div><small>Outcome</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of the cost of the lamp, the total benefit to residents and the revenue a firm can collect"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Private, free or public good?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the free rider problem in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A lighthouse", "A lighthouse beam helps every ship, and one ship's use does not reduce the light for another. The owner cannot stop passing ships from using it, so cannot charge them. Lighthouses are the classic example of a public good, which is why governments and harbour authorities build them.", "non-rivalry, non-excludability and the free rider problem.") +
rw("Free school lunches", "A government pays for lunches for all children in school. The lunches are free of charge to the child, but each meal can be eaten by only one child (rival) and a child who is not registered can be kept out (excludable). They are private goods provided by the state, and cost taxpayers resources.", "the difference between a good that is free of charge and a free good, and between a private good and a public good.") +
rw("A beach", "A public beach has no entry fee and few people use it in winter, so it behaves like a public good. In summer it becomes crowded, so one person's use reduces another's enjoyment (rival), and some beaches charge for entry or parking (excludable). It is a quasi-public good.", "why real goods fall between the pure types.") +
rw("Motorway tolls", "A free motorway is close to a public good because it is hard to charge individual drivers. Electronic tolling makes it possible to exclude those who do not pay, so the road becomes a private good that can be run for profit.", "how technology that makes a good excludable can turn it from a public good into a private good.")
)

mc_exam = [
  mcq("s20_11", 18, "What is a necessary characteristic of a public good?", ["It has a fixed maximum price", "It has an opportunity cost of production of zero", "It is non-excludable", "It is an essential good"], 2, "Non-excludability, together with non-rivalry, defines a public good. Public goods have an opportunity cost, because they use resources."),
  mcq("w20_12", 2, "Which statement is correct?", ["Private goods are both non-rival and non-excludable", "Private goods are only provided by the private sector", "Public goods are both non-rival and non-excludable", "Public goods do not incur opportunity costs"], 2, "Public goods are non-rival and non-excludable. Private goods can be provided by the state, and public goods use resources."),
  mcq("w20_13", 2, "What is characterised as a free good?", ["One that has zero opportunity cost", "One that is non-excludable and non-rivalrous", "One that is supplied by the government with no charge", "One that receives a 100% government subsidy"], 0, "A free good is not scarce and has no opportunity cost. Option B describes a public good, and C and D describe goods free of charge."),
  mcq("w22_11", 2, "A local council provides a tap for drinking water in a town. Would this make drinking water a free good?", ["No, because it is possible to exclude some people from using the tap", "No, because it requires the use of scarce resources", "Yes, because it is available to all passers-by", "Yes, because it is impossible to charge for it"], 1, "The water is provided free of charge, but it uses scarce resources (pipes, pumping, labour), so it has an opportunity cost and is not a free good."),
  mcq("w23_13", 4, "What is an example of a free good?", ["A government sponsoring a free vaccination programme", "A hospital providing free treatment to the poor", "A school providing free education to outstanding students", "Anything that provides free utility but is not scarce"], 3, "A free good is not scarce. The first three are free of charge to the user but use scarce resources."),
  mcq("w24_13", 2, "Which type of good does not consume scarce resources?", ["Economic good", "Free good", "Merit good", "Public good"], 1, "Only a free good uses no scarce resources and has zero opportunity cost."),
  mcq("w24_11", 3, "Which statement is not correct?", ["Addictive drugs are regarded as demerit goods because users are unaware of the full damage they do", "Air is regarded as a free good because its use has no opportunity cost", "National defence is regarded as a public good because one citizen consuming it reduces the amount available to others", "Visits to a doctor are regarded as private goods partly because they are rival"], 2, "National defence is a public good because it is non-rival: one citizen's consumption does not reduce what is available to others."),
  mcq("s21_13", 1, "A government department provides milk at no charge to very low-income families. Which term best describes the milk?", ["Free good", "Inferior good", "Private good", "Public good"], 2, "Milk is rival and excludable, so it is a private good even though the state provides it free of charge."),
  mcq("s25_11", 5, "How can a public good become a private good?", ["Consumers are dissatisfied with the performance of state-run services", "New technological developments make the good excludable", "The government privatises the industry producing the good", "The price of the good increases so it becomes more profitable"], 1, "If technology makes it possible to exclude non-payers, the good is no longer a public good."),
  mcq("w20_11", 17, "A good is provided by the government. Consumption by one person does not affect the amount of the good available for others. Which type of good must this be?", ["Complementary good", "Merit good", "Private good", "Public good"], 3, "Consumption by one person leaving the amount available unaffected is non-rivalry, a feature of a public good."),
  mcq("s25_13", 1, "A tourist visits a government-owned tropical beach. She pays $10 to enter but finds it overcrowded. Which type of good is the beach?", ["A free good", "An inferior good", "A public good", "A private good"], 3, "The entry fee shows it is excludable and overcrowding shows it is rival, so in this case it is a private good."),
  mcq("w23_11", 3, "A country's health care is funded by taxation but can be used free of charge by patients. Which type of good is health care in this country?", ["Demerit good", "Free good", "Private good", "Public good"], 2, "A doctor's time and hospital beds are rival and excludable, so health care is a private good provided by the state.")
]

exam = exam_page("free goods, private goods and public goods",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The difference between private, free and public goods is the most frequent 8 mark Paper 2 topic after the PPC, with one in nearly every series, and it appears as 2 and 4 mark parts and in Paper 1 every year. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "6", "May/June 2020 (22) Q4(a); May/June 2021 (21) Q2(a); Feb/March 2025 (22) Q3(a); May/June 2025 (22) Q2(a); Oct/Nov 2023 (22) Q3(a); Oct/Nov 2024 (23) Q2(a)"), ("Data response, 2 and 4 marks", "2", "May/June 2022 (22) Q1(b); May/June 2021 (23) Q1(c)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("s20_22", "4(a)"), "8 marks", "Explain, using examples, the difference between private goods and public goods and why public goods will not be supplied by private enterprise.",
     ["Knowledge (up to 2): the distinction based on excludability (1) and rivalry in consumption (1).",
      "Application (up to 6): why public goods are not supplied in a free market economy, because of non-excludability and non-rivalry (4 marks), with reference to the free rider issue (2 marks)."],
     "Private: rival and excludable. Public: non-rival and non-excludable. Free riders: no revenue, so no private supply.",
     [[("k", "A private good, such as a loaf of bread, is rival, because when one person eats it another cannot, and excludable, because the seller can refuse to sell to someone who does not pay. A public good, such as street lighting, is non-rival, because one person's use does not reduce the amount available, and non-excludable, because it is impractical to stop people from using it.")], [("n", "Private enterprise will not supply public goods because, if people cannot be excluded, they can enjoy the good without paying. This is the free rider problem: each person waits for others to pay. As a result the firm cannot collect revenue or make a profit, so the market fails to provide the good and the government must provide it and pay for it through taxes.")]]),
  eq(P("s21_21", "2(a)"), "8 marks", "Explain whether private goods, free goods and public goods will all be sold in a free market economy.",
     ["Knowledge (up to 2): of private goods, free goods and public goods (just two types earns 1).",
      "Application (up to 6, 2 for each type): private goods are sold, as they are rival and excludable; free goods are not sold as they are not scarce, have no price attached, supply equals demand at zero price and need no factors of production; public goods are not sold because of non-rivalry and non-excludability."],
     "Private: yes. Free: no, as they have no price. Public: no, because of the free rider problem.",
     [[("k", "Private goods are economic goods consumed by an individual for their own benefit, are rival and excludable, so they are sold in a free market. Free goods, such as fresh air, are not scarce and have a zero opportunity cost. Public goods are non-rival and non-excludable.")], [("n", "In a free market private goods will be sold because firms can charge a price and earn a profit. Free goods will not be sold because they have no price, supply equals demand at zero price and no factors of production are used. Public goods will not be sold, because people cannot be excluded and so will not pay, so firms cannot make a profit.")]]),
  eq(P("m25_22", "3(a)"), "8 marks", "Explain what is meant by a public good and a private good (economic good) and consider the extent to which a beach could be described as a public good.",
     ["Knowledge (3): explanation of rivalrous and non-rivalrous (1); excludable and non-excludable (1); correctly applied to a public good and a private good to explain the difference (1).",
      "Analysis (3): the extent to which a beach might be rivalrous (1); the extent to which it might be excludable (1); alternatives are also considered (1).",
      "Evaluation (2): a valid explanation that the extent a beach is public may vary (a quasi-public good) and a justified conclusion."],
     "Define both goods using rivalry and excludability. Test the beach on each. Quasi-public: depends on crowding and charges.",
     [[("k", "A public good is non-rival, so one person's use does not reduce its availability for others, and non-excludable, so non-payers cannot be kept out. A private good is rival and excludable: when one person uses it, others cannot, and it can be denied to those who do not pay.")], [("n", "A beach may be non-rival when it is uncrowded, since more visitors do not reduce anyone else's use, and it may be non-excludable if it is open to anyone with no charge. But in summer a beach can become overcrowded, which makes it rival, and some beaches charge for entry or parking, which makes them excludable.")], [("e", "Therefore a beach is probably a quasi-public good: it is close to a public good when open and uncrowded, but not when it is crowded or has an entry charge. Whether it is public depends on the beach and the time of year.")]]),
  eq(P("s25_22", "2(a)"), "8 marks", "With the help of examples, explain the difference between public goods and free goods and consider whether a market economy can ever produce public goods.",
     ["Knowledge (3): free goods are not scarce, have zero opportunity cost and need no factors of production (1); public goods are non-excludable and non-rival, each explained (1); appropriate examples of both, such as fresh air as a free good and national defence as a public good (1). Roads, education or health are not accepted as examples, nor is 'provided by the government'.",
      "Analysis (3): the characteristics of public goods make it easy not to pay, so firms cannot charge a price (the free rider problem) (1), so people enjoy benefits without paying and firms cannot make a profit (1), so a market economy is unlikely to provide them (1).",
      "Evaluation (2): unless some method of making them excludable exists, or the government subsidises production, or firms act in the public interest, it is unlikely that a market economy could produce them."],
     "Free good: not scarce. Public good: non-rival and non-excludable. Free rider problem. Evaluate: excludability by technology, subsidies.",
     [[("k", "A free good, such as fresh air, is not scarce and has no opportunity cost, since no factors of production are used. A public good, such as national defence, is non-rival and non-excludable, but it is scarce, because it uses resources.")], [("n", "The two characteristics of public goods let people enjoy the good without paying, which is the free rider problem. Firms cannot charge a price or earn a profit, so a market economy is unlikely to produce them.")], [("e", "However, a market might produce some public goods if technology makes them excludable, such as scrambled signals, or if the government pays a subsidy to private firms. So a pure market probably cannot produce true public goods, but a mixed arrangement can.")]]),
  eq(P("w24_23", "2(a)"), "8 marks", "With the aid of examples, explain the characteristics of public goods and free goods and consider whether free-of-charge vaccinations offered by a government should be classified as a free good.",
     ["Knowledge (3): free goods are not scarce, have zero opportunity cost and need no factors of production (1); public goods are non-excludable and non-rival, each briefly explained (1); accurate examples such as fresh air and street lighting (1).",
      "Analysis (3): a vaccine is free at the point of use (1), but there is a cost to taxpayers (1), so there is an opportunity cost to the government because providing it uses scarce resources (1).",
      "Evaluation (2): a judgement on whether free-of-charge vaccinations should be classed as a free good."],
     "Characteristics of both. Vaccine: free of charge but uses resources, so not a free good. Judge.",
     [[("k", "A free good, such as fresh air, is not scarce and has zero opportunity cost. A public good, such as street lighting, is non-rival and non-excludable.")], [("n", "A vaccination offered free of charge costs the user nothing, but it uses scarce resources such as doctors, nurses and medicines, which are paid for by taxpayers. The government therefore has an opportunity cost, because the money could have been used for other things.")], [("e", "So free-of-charge vaccinations should not be classified as a free good. Free of charge is not the same as free: the good is scarce and has a cost to society, although not to the individual.")]]),
  eq(P("s22_22", "1(b)"), "4 marks", "Explain whether school lunches provided free of charge by a government would be classified as private goods or public goods.",
     ["Clear and accurate understanding of what is meant by excludable and non-excludable (1).", "Clear and accurate understanding of rivalry and non-rivalry in consumption (1).", "A correct application of both terms to free school meals (1).", "A conclusion that free school meals must be private and not public goods (1)."],
     "Define excludable and rival. Apply both to a lunch. Conclude: private.",
     [[("k", "A good is excludable if people who do not pay can be kept out, and rival if one person's consumption reduces the amount for others."), ("n", "A school lunch is rival, because a meal eaten by one child cannot be eaten by another, and excludable, because the school can decide who receives meals. Providing them free of charge does not change this, so they are private goods provided by the government, not public goods.")]]),
  eq(P("s21_23", "1(c)"), "2 marks", "Explain whether public transport in a city has become a free good as a result of all prices being removed.",
     ["Explain what is meant by a free good (1).", "Explain why it is not a free good, because factors of production are still needed to provide the transport service, so there is a cost (1)."],
     "Free good: not scarce. Transport still uses buses, drivers and fuel, so it is not free.",
     [[("k", "A free good is one that is not scarce and has no opportunity cost."), ("n", "Public transport still needs buses, drivers and fuel, which are scarce factors of production, so it has a cost, even though users pay nothing. It is free of charge, not a free good.")]])
  ],
  )

tips = tips_html(
  [("Define with rivalry and excludability.", "Private: rival and excludable. Public: non-rival and non-excludable."),
   ("Free is not 'free of charge'.", "A free good is not scarce. A government service paid for by taxes still has an opportunity cost."),
   ("Explain the free rider problem.", "No one can be excluded, so people will not pay, and the market does not supply."),
   ("Use pure examples.", "National defence, street lighting, lighthouses, flood barriers. Not roads, schools or health."),
   ("Government provision does not make a good public.", "School meals are private goods."),
   ("Mention quasi-public goods.", "A beach is partly rival and partly excludable."),
   ("Say technology can change the type.", "Tolls make a motorway excludable.")],
  [("Public good", "A public good is non-rival and non-excludable, so people may be able to use it without paying."),
   ("Free rider", "Because of the free rider problem, a private firm might not be able to earn revenue from a public good."),
   ("Government", "The government may provide public goods and pay for them from taxation."),
   ("Free good", "A free good is not scarce, so it has no opportunity cost."),
   ("Judge", "A beach could be a quasi-public good, depending on how crowded it is and whether it charges.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- grid ---------- */
function gridDraw(s) {
  let o = SV.rect(90, 40, 310, 130, "f1", op(0.15)) + SV.rect(400, 40, 310, 130, "f1", op(0.15)) + SV.rect(90, 170, 310, 130, "f1", op(0.15)) + SV.rect(400, 170, 310, 130, "f1", op(0.15));
  o += SV.text(245, 28, "Excludable", "lbl bd", { "text-anchor": "middle" }) + SV.text(555, 28, "Non-excludable", "lbl bd", { "text-anchor": "middle" }) + SV.text(82, 110, "Rival", "lbl bd", { "text-anchor": "end" }) + SV.text(82, 240, "Non-rival", "lbl bd", { "text-anchor": "end" });
  const q = (x, y, t, sub, c, k) => (k > 0 ? SV.rect(x, y, 310, 130, c, op(0.45 * k)) + SV.text(x + 155, y + 56, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 155, y + 82, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += q(90, 40, "PRIVATE GOOD", "bread, a haircut, school meals", "f3", s.a) + q(400, 170, "PUBLIC GOOD", "national defence, street lighting", "f2", s.b) + q(400, 40, "Common resource (in between)", "fish in the open sea", "f1", s.c) + q(90, 170, "Club good (in between)", "a cinema seat when the film is half empty", "f1", s.c);
  if (s.d > 0) o += SV.text(400, 322, "FREE GOOD: not scarce (e.g. fresh air), no opportunity cost: outside this grid", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)", ...op(s.d) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 335" role="img" aria-label="A grid of rival and excludable goods: private goods, public goods and in-between cases">${gridDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 335, label: "A grid of rival and excludable goods showing private goods, public goods and free goods", base: { a: 0, b: 0, c: 0, d: 0 }, draw: gridDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Private (economic) goods</b> are rival and excludable. A loaf of bread eaten by one person is gone, and the shop can refuse a customer who does not pay. They are scarce and have a price.", s: { a: 1 } },
  { cap: "<b>Public goods</b> are non-rival and non-excludable. Street lighting helps everyone and cannot be withheld from those who did not pay.", s: { a: 1, b: 1 } },
  { cap: "<b>In between</b> are goods that are only partly rival or excludable, such as a half-empty cinema or fish in the open sea. A beach is a good example of a quasi-public good.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Free goods</b> are a separate idea: they are not scarce, so there is no opportunity cost. Do not confuse them with goods that are only free of charge.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- free rider ---------- */
function frDraw(s) {
  let o = SV.text(40, 26, "Four neighbours each value a street lamp at $30. The lamp costs $100.", "lbl bd");
  for (let i = 0; i < 4; i++) { const x = 70 + i * 160; o += SV.circle(x + 40, 80, 20, "dot1", op(0.8)) + SV.text(x + 40, 130, "Neighbour " + (i + 1), "sm", { "text-anchor": "middle" }); if (s.v > 0) o += SV.text(x + 40, 150, "values it at $30", "sm", { "text-anchor": "middle", ...op(s.v) }); if (s.w > 0) o += SV.rect(x + 5, 170, 70, 36, "f2", op(0.5 * s.w)) + SV.text(x + 40, 193, "pays $0", "lbl bd", { "text-anchor": "middle", ...op(s.w) }); if (s.t > 0) o += SV.rect(x + 5, 215, 70, 36, "f3", op(0.6 * s.t)) + SV.text(x + 40, 238, "tax $25", "lbl bd", { "text-anchor": "middle", ...op(s.t) }); }
  if (s.w > 0) o += SV.text(380, 285, "Voluntary: total paid $0. The lamp is not built.", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)", ...op(s.w) });
  if (s.t > 0) o += SV.text(380, 310, "Tax: 4 × $25 = $100. The lamp is built and every neighbour gains $30.", "lbl bd", { "text-anchor": "middle", style: "fill:var(--good)", ...op(s.t) });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 325, label: "Four neighbours, a street lamp, free riding and a tax", base: { v: 0, w: 0, t: 0 }, draw: frDraw, tween: 800, dwell: 5800, steps: [
  { cap: "<b>The benefit.</b> Each of four neighbours gets $30 of value from a street lamp, so the total benefit is $120, which is more than its $100 cost. It would be worth building.", s: { v: 1 } },
  { cap: "<b>Free riding.</b> Once the lamp is built, no neighbour can be excluded. Each hopes the others will pay, so each pays nothing. A firm collects no revenue, so it will not build the lamp. The market fails.", s: { v: 1, w: 1 } },
  { cap: "<b>The government solution.</b> A tax of $25 on each neighbour pays for the lamp. Everyone is better off: they pay $25 and get $30 of benefit.", s: { v: 1, w: 1, t: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 325" role="img" aria-label="Four neighbours who each value a street lamp at 30 dollars, voluntary payment fails and a tax of 25 dollars each succeeds">${frDraw({ v: 1, w: 1, t: 1 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labK() {
  if (!$("#rv1") || !$("#ex")) return;
  const r = +$("#rv1").value, e = +$("#ex").value, rt = r >= 50, et = e >= 50, type = rt && et ? "Private good" : !rt && !et ? "Public good" : rt && !et ? "Common resource" : "Club good", ex = rt && et ? "bread, a haircut, school lunches" : !rt && !et ? "national defence, street lighting, a lighthouse" : rt && !et ? "fish in the open sea, a crowded free beach" : "a half-empty cinema, a toll motorway at quiet times";
  $("#r1").textContent = rt ? "Rival" : "Non-rival"; $("#r2").textContent = et ? "Excludable" : "Non-excludable"; $("#r3").textContent = type;
  $("#rv").textContent = `${rt ? "Rival" : "Non-rival"} and ${et ? "excludable" : "non-excludable"}: a ${type.toLowerCase()}, for example ${ex}. ${type === "Public good" ? "A free market will not supply it because people can free ride, so the government provides it." : type === "Private good" ? "A free market can supply it because non-payers are excluded and each unit is used by one person." : "This good is in between the two main types, so the market may supply it only partly."}`;
  const X = (v) => 40 + v * 3.4, Y = (v) => 270 - v * 2.4; let o = SV.rect(40, 30, 170, 120, "f1", op(0.15)) + SV.rect(210, 30, 170, 120, "f1", op(0.15)) + SV.rect(40, 150, 170, 120, "f1", op(0.15)) + SV.rect(210, 150, 170, 120, "f1", op(0.15));
  o += SV.text(125, 22, "Non-excludable", "sm", { "text-anchor": "middle" }) + SV.text(295, 22, "Excludable", "sm", { "text-anchor": "middle" }) + SV.text(125, 288, "PUBLIC", "sm", { "text-anchor": "middle" }) + SV.text(295, 288, "CLUB", "sm", { "text-anchor": "middle" }) + SV.text(125, 50, "COMMON RESOURCE", "sm", { "text-anchor": "middle" }) + SV.text(295, 50, "PRIVATE", "sm", { "text-anchor": "middle" });
  o += SV.circle(X(e), Y(r), 9, "dot4"); $("#labA").innerHTML = o + SV.text(400, 300, "Excludability →", "sm", { "text-anchor": "end" }) + SV.text(4, 16, "Rivalry ↑", "sm");
}
Lib.slider($("#g1"), { id: "rv1", label: "Rivalry (0 = non-rival, 100 = very rival) ", min: 0, max: 100, step: 5, value: 20, fmt: (v) => v, onInput: labK });
Lib.slider($("#g2"), { id: "ex", label: "Excludability (0 = cannot exclude, 100 = easy) ", min: 0, max: 100, step: 5, value: 10, fmt: (v) => v, onInput: labK });
labK();

/* ---------- Lab 2 ---------- */
function labF() {
  if (!$("#nn") || !$("#bb") || !$("#ee")) return;
  const n = +$("#nn").value, b = +$("#bb").value, e = +$("#ee").value / 100, ben = n * b, rev = ben * e, cost = 1000, ok = rev >= cost, soc = ben >= cost;
  $("#t1").textContent = "$" + ben.toLocaleString("en-US"); $("#t2").textContent = "$" + Math.round(rev).toLocaleString("en-US"); $("#t3").textContent = ok ? "Market provides it" : soc ? "Worth building, market will not" : "Not worth building";
  $("#tv").textContent = ok ? `A private firm can collect $${Math.round(rev).toLocaleString("en-US")} from those it can exclude, which covers the $1,000 cost, so it will build the lamp. Because most users can be made to pay, the good behaves like a private good.` : soc ? `The residents together gain $${ben.toLocaleString("en-US")}, more than the $1,000 cost, so the lamp is worth building. But the firm can only charge ${Lib.fmtN(e * 100, 0)}% of users, so it collects $${Math.round(rev).toLocaleString("en-US")} and makes a loss. The market will not supply it: the free rider problem. The government could tax residents and build it.` : "The total benefit is less than the cost, so it would not be worth building even if everyone paid.";
  const Y = (v) => 270 - v / Math.max(2000, ben) * 220; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "$", "sm");
  [["Cost", cost, "f2"], ["Total benefit", ben, "f3"], ["Revenue firm can collect", rev, "f1"]].forEach(([l, v, c], i) => { const x = 55 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c, op(0.75)) + SV.text(x + 40, 290, l.split(" ").slice(0, 2).join(" "), "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, "$" + Math.round(v).toLocaleString("en-US"), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "nn", label: "Number of residents ", min: 5, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labF });
Lib.slider($("#g4"), { id: "bb", label: "Value each places on the lamp, $ ", min: 5, max: 60, step: 5, value: 30, fmt: (v) => v, onInput: labF });
Lib.slider($("#g5"), { id: "ee", label: "Share of users the firm can exclude, % ", min: 0, max: 100, step: 5, value: 0, fmt: (v) => v + "%", onInput: labF });
labF();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which type of good is it?", ["Private good", "Free good", "Public good"],
  [("A loaf of bread", 0), ("Fresh air", 1), ("National defence", 2), ("School lunches provided free by the government", 0), ("Sunshine on a clear day", 1), ("Street lighting", 2), ("A haircut", 0), ("A lighthouse beam", 2)],
  "Private: rival and excludable. Free: not scarce. Public: non-rival and non-excludable.") + MATCH([
  ["Rivalry", "One person's use reduces what is left for others"],
  ["Excludability", "Non-payers can be kept from using the good"],
  ["Free rider", "Someone who benefits without paying"],
  ["Public good", "Non-rival and non-excludable"],
  ["Free good", "Not scarce and has zero opportunity cost"],
  ["Quasi-public good", "A good that is partly rival or excludable"]]) + ORDER(
  "Put the free rider problem in order.",
  ["A good is non-excludable, so non-payers cannot be kept out", "Each person has an incentive to let others pay", "Few or no people pay voluntarily", "A private firm earns no revenue and will not supply the good", "The government supplies it and pays for it through taxation"],
  "Non-excludability leads to free riding, which leads to market failure.") + CALC([
  {"q": "A street lamp costs $1,000. 40 residents each value it at $30. What is the total benefit ($)?", "a": 1200, "unit": "$", "tol": 1, "hint": "40 × 30.", "sol": "<b>$1,200</b>, more than the cost."},
  {"q": "A tax raises the $1,000 equally from the 40 residents. How much does each pay ($)?", "a": 25, "unit": "$", "tol": 0.5, "hint": "1,000 ÷ 40.", "sol": "<b>$25</b>. Each gets $30 of benefit, so everyone gains $5."},
  {"q": "A firm can charge only 10% of the residents (because the rest cannot be excluded). Each pays $30. What revenue does it collect ($)?", "a": 120, "unit": "$", "tol": 1, "hint": "4 residents × 30.", "sol": "4 × 30 = <b>$120</b>, far below the $1,000 cost."},
  {"q": "Using the figures above, what is the firm's profit or loss ($, use a minus sign for a loss)?", "a": -880, "unit": "$", "tol": 1, "hint": "120 − 1,000.", "sol": "<b>−$880</b>: the market will not provide it."}]) + MCQ([
  ("A public good is:", ["Non-rival and non-excludable", "Rival and excludable", "Any good supplied by the government", "A good that has no price"], 0, "Both characteristics define a public good."),
  ("Why will a free market not supply a pure public good?", ["Free riders mean no revenue", "It is too cheap", "Consumers do not want it", "It has no opportunity cost"], 0, "Firms cannot make a profit if non-payers cannot be excluded."),
  ("A free good is one that:", ["Is not scarce and has zero opportunity cost", "Is free of charge to users", "Is provided by the government", "Is non-rival and non-excludable"], 0, "Free of charge is not the same as free."),
  ("School lunches provided free by a government are:", ["Private goods", "Public goods", "Free goods", "Demerit goods"], 0, "They are rival and excludable."),
  ("Which could make a public good into a private good?", ["Technology that makes it excludable", "A rise in taxes", "More free riders", "A fall in demand"], 0, "If non-payers can be excluded, a charge is possible.")
], "qz1") + CARDS([
  ("Private good", "Rival and excludable."),
  ("Public good", "Non-rival and non-excludable."),
  ("Free good", "Not scarce; zero opportunity cost."),
  ("Free rider", "Benefits without paying."),
  ("Free of charge", "Not the same as a free good."),
  ("Quasi-public", "Partly rival or excludable."),
  ("Provision", "Public goods: government, tax-funded."),
  ("Technology", "Can make a good excludable.")]) + MCQ(mc_exam)

build("as18", "as-free-private-public-goods", "Free, Private and Public Goods", EY,
  "1.6.1 to 1.6.2: free goods, private (economic) goods and public goods, rivalry and excludability, and why the free rider problem means a market will not supply public goods. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
