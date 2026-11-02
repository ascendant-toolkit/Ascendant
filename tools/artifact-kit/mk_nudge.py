"""Builds the Nudge theory page (syllabus 8.1.1). Run: python3 tools/artifact-kit/mk_nudge.py"""
from splitter import page, write, key, newtips
import pathlib
_D = pathlib.Path(__file__).parent
EY = "A Level Economics · 9708 · Syllabus 8.1.1 · Behavioural insights and nudge theory"
KEY = key()

learn = '''
  <div class="card big"><h3>This page in four sentences</h3>
  <p>Nudge theory says people do not always choose rationally: they follow <b>defaults</b>, copy others, put things off and react to how a choice is <b>framed</b>. A <b>nudge</b> changes the way a choice is presented, so that people are steered towards the better option, <b>without banning anything or changing prices</b>. It is cheap and keeps freedom of choice, but its effect can be small, uncertain and short-lived. Governments therefore use nudges beside taxes, subsidies and regulation, not instead of them.</p></div>

  <h2>1 · Where it comes from</h2>
  <p>Traditional economics assumes consumers are rational: they weigh costs and benefits, have full information and maximise utility. <b>Behavioural economics</b> tests that assumption and finds systematic patterns of "irrational" behaviour. Richard Thaler and Cass Sunstein used these findings in their book <i>Nudge</i> (2008), and Thaler won the Nobel Prize in Economics in 2017. They called the idea <b>libertarian paternalism</b>: the state steers people towards choices that improve their own welfare (paternalism) while leaving them free to choose otherwise (libertarian).</p>
  <p>A nudge counts only if it is easy and cheap to avoid. Putting fruit at eye level is a nudge. Banning chocolate is not. The syllabus words are <b>behavioural insights and nudge theory</b>, listed with the other tools for correcting market failure.</p>

  <h2>2 · Why people need nudging: the biases</h2>
  <div class="tw"><table class="t">
    <tr><th>Behaviour</th><th>What it means</th><th>Nudge that uses it</th></tr>
    <tr><td><b>Inertia and status quo bias</b></td><td>People stick with the default, because changing takes effort</td><td>Opt-out organ donation, automatic pension enrolment</td></tr>
    <tr><td><b>Social norms</b></td><td>People copy what they think most others do</td><td>"Most people in your area have already paid their tax"</td></tr>
    <tr><td><b>Present bias</b></td><td>People overvalue now against later, so they under-save and over-indulge</td><td>Saving that starts automatically, or rises when pay rises</td></tr>
    <tr><td><b>Framing and loss aversion</b></td><td>The same facts feel different depending on wording; losses feel bigger than gains</td><td>"You will lose 5p per bag" rather than "reusable bags save 5p"</td></tr>
    <tr><td><b>Salience and choice architecture</b></td><td>People choose what is easy to see and reach</td><td>Fruit at eye level, sweets removed from the till</td></tr>
    <tr><td><b>Limited attention</b></td><td>People forget or are overloaded</td><td>Text message reminders, simpler forms</td></tr>
  </table></div>

  <h2>3 · The main types of nudge</h2>
  <ul>
    <li><b>Defaults</b>: the option you get if you do nothing (opt-out schemes).</li>
    <li><b>Social norms</b>: telling people what others do.</li>
    <li><b>Framing and labels</b>: calorie labels, traffic-light food labels, wording of letters.</li>
    <li><b>Placement</b>: where an option sits on the shelf, the website or the form.</li>
    <li><b>Reminders and commitment devices</b>: messages that tell people when to act, or let them lock in a promise.</li>
  </ul>

  <h2>4 · Nudge, information, tax, ban: how they differ</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Nudge</th><th>Information</th><th>Tax or subsidy</th><th>Ban or regulation</th></tr>
    <tr><td><b>Changes price?</b></td><td>No</td><td>No</td><td>Yes</td><td>No</td></tr>
    <tr><td><b>Limits choice?</b></td><td>No</td><td>No</td><td>No (but changes the budget)</td><td>Yes</td></tr>
    <tr><td><b>Works by</b></td><td>Changing how the choice is presented</td><td>Giving facts and persuasion</td><td>Changing incentives</td><td>Law and enforcement</td></tr>
    <tr><td><b>Typical cost</b></td><td>Low</td><td>Low to medium</td><td>Administration, but can raise revenue</td><td>Enforcement cost</td></tr>
    <tr><td><b>Typical strength</b></td><td>Often modest</td><td>Often modest</td><td>Stronger if demand is elastic</td><td>Strongest, if enforced</td></tr>
  </table></div>
  <div class="tip"><b class="h">The exam trap</b>A tax is not a nudge, even when its purpose is to change behaviour, because it changes the price. A ban is regulation. A health warning or campaign is information, which the syllabus lists separately but which often counts as a nudge when it uses persuasion or example. The Paper 4 mark scheme defined nudge theory as policies that influence behaviour <b>by persuasion or example</b> to achieve one of the government's main economic aims.</div>

  <h2>5 · How nudges correct market failure</h2>
  <ul>
    <li><b>Demerit goods</b> (smoking, sugary food, gambling): consumers under-estimate the harm, so demand is too high. A nudge moves them back.</li>
    <li><b>Merit goods</b> (pensions, vaccination, education, organ donation): consumers under-value the benefit, so demand is too low. A default or reminder raises it.</li>
    <li><b>Information failure</b>: labels and simpler forms close the gap.</li>
    <li><b>Negative externalities</b>: social norm messages can reduce littering, energy use or tax evasion, where a fine would be costly to enforce.</li>
  </ul>

  <h2>6 · Evaluating nudges</h2>
  <div class="tw"><table class="t">
    <tr><th>For</th><th>Against</th></tr>
    <tr><td>Cheap compared with subsidies or enforcement, and quick to run</td><td>Effects may be small, especially where the good is addictive or demand is inelastic</td></tr>
    <tr><td>Preserves freedom of choice, so it may be more acceptable politically</td><td>Effects may fade as people get used to the nudge</td></tr>
    <tr><td>Can be tested first on a small group (randomised trials), so waste is limited</td><td>Hard to measure the long-run result; a trial may not scale up</td></tr>
    <tr><td>Helps where taxes are unpopular or hard to collect</td><td>Ethical concerns: who decides what is "best", and is steering people a form of manipulation?</td></tr>
    <tr><td>Can raise tax revenue or lower public spending (more tax paid on time, more people saving)</td><td>Firms can use the same tricks against consumers (hidden fees, "sludge" that makes cancelling hard)</td></tr>
  </table></div>
  <p><b>Evaluation points to use:</b> the size and <b>time</b> of the effect, how <b>elastic</b> behaviour is, whether it works <b>alone</b> or only with a tax, subsidy or law, the <b>cost</b> against the benefit, the quality of the <b>evidence</b>, and whether it is <b>acceptable</b> to the public.</p>
'''

watch = '''
  <h2>1 · The power of a default</h2>
  <p>An illustrative model of opt-in against opt-out organ donation. These are not real data. Press Play, or click the steps.</p><div id="stD"></div>
  <h2>2 · Where a nudge sits among the policy tools</h2>
  <p>From doing nothing to a total ban, the tools differ in how much they limit your choice and how strong they are.</p><div id="stS"></div>
'''

explore = '''
  <h2>Lab 1 · Defaults and donors</h2>
  <p>Choose how many people just accept the default, and how many would donate if they thought about it. These numbers are illustrative.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Opt-in donors</small><strong id="d1"></strong></div><div><small>Opt-out donors</small><strong id="d2"></strong></div><div><small>Difference</small><strong id="d3"></strong></div></div>
    <div class="verdict" id="dv"></div></div>
    <div><svg id="labD" viewBox="0 0 420 260" role="img" aria-label="Bars comparing the share of donors under opt-in and opt-out"></svg></div></div></div>

  <h2>Lab 2 · Nudge or tax?</h2>
  <p>A town sells 100 sugary drinks a day at $2 each. Choose a nudge (such as moving the drinks off the eye-level shelf) and a tax, then compare. The numbers are illustrative: a tax cuts sales by about 0.6% for every 1% rise in price.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Drinks sold</small><strong id="t1"></strong></div><div><small>Price paid</small><strong id="t2"></strong></div><div><small>Tax revenue per day</small><strong id="t3"></strong></div><div><small>Choice limited?</small><strong id="t4"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labT" viewBox="0 0 420 260" role="img" aria-label="Bars comparing drinks sold with no policy and with the chosen nudge and tax"></svg></div></div></div>
'''

practise = '''
  <h2>1 · What type of policy?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which behaviour does the nudge use?</h2><div id="m2" class="card"></div>
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the explanation in order</h2><div id="o1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = '''
  <p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>
  <h2>United Kingdom</h2>
  <div class="rw"><h3>The Behavioural Insights Team ("Nudge Unit")</h3><p>The UK government set up a small unit in the Cabinet Office in 2010 to apply behavioural economics to public policy and test ideas with trials before rolling them out. It later became an independent organisation, and similar units now exist in many countries. The Paper 4 extracts on this topic describe exactly these "Nudge Units" in the US, UK and Australia.</p><div class="use"><b>Exam use:</b> evidence that governments take behavioural insights seriously. Evaluate: trials test small changes, and results may not scale to the whole economy.</div></div>
  <div class="rw"><h3>Automatic enrolment into workplace pensions</h3><p>Since 2012 UK employers must enrol eligible workers in a pension scheme automatically, and workers must actively opt out. Participation among eligible employees rose from roughly half to around nine in ten. Tax relief alone had not persuaded many people to save.</p><div class="use"><b>Exam use:</b> a default for a merit good, countering present bias. This is the same mechanism as the "good luck" and saving examples in the Paper 4 extract. Evaluate: contribution rates are often the minimum, so the saving may still be too low for a comfortable retirement.</div></div>
  <div class="rw"><h3>Social norm letters from HMRC</h3><p>Trials by the tax authority added messages such as "most people in your town pay their tax on time" to reminder letters. More people paid on time than with the standard letter, at almost no extra cost.</p><div class="use"><b>Exam use:</b> the standard answer to "how could a nudge raise tax revenue or reduce evasion?", which links to the Paper 3 questions on tax evasion. Evaluate: it helps the people who intend to pay, but does little against deliberate evasion.</div></div>
  <div class="rw"><h3>Organ donation consent</h3><p>Wales changed to an opt-out system in 2015, England followed in 2020 and Scotland in 2021. Families are still consulted, so the system is a soft default. Consent rates are only one factor in donation numbers, which also depend on hospital capacity and family decisions.</p><div class="use"><b>Exam use:</b> default nudge with a merit good. Evaluate: the benefit depends on the whole system, not just the default.</div></div>
  <div class="rw"><h3>Calorie labels on menus, and the 5p bag charge</h3><p>Large restaurants in England must show calories on menus (since 2022), an information and framing tool. The 5p carrier bag charge (2015) cut single-use bag use sharply, but it works through a price, so it is closer to a <b>tax</b> than a nudge.</p><div class="use"><b>Exam use:</b> a good way to show you know the boundary. A small charge is a price change, so say it is not a pure nudge, although its effect on behaviour is larger than the size of the charge would suggest.</div></div>

  <h2>Vietnam</h2>
  <div class="rw"><h3>The hand-washing song and the 5K message</h3><p>In 2020 the Ministry of Health and the National Institute of Occupational and Environmental Health backed a catchy hand-washing song and the "5K" message (face masks, disinfection, distance, no gatherings, health declaration). The campaign used simple memorable wording, a shared social identity and a song that went viral online, with very low cost per person reached.</p><div class="use"><b>Exam use:</b> persuasion and social norms working as an information nudge for a public good, with a positive externality. Evaluate: it was supported by testing, tracing and legal rules, so the nudge was not working alone.</div></div>
  <div class="rw"><h3>QR code payments at the till</h3><p>In Vietnam shops, street stalls and markets display a QR code, and banks and apps compete to make payment as easy as possible. Paying by phone is made the easiest option, and the state encourages cashless payment.</p><div class="use"><b>Exam use:</b> choice architecture and salience: making one option easy raises its use without forbidding cash. Evaluate: the effect depends on phone and bank access, so rural and older people may be left behind.</div></div>
  <div class="rw"><h3>Voluntary social insurance: a possible nudge</h3><p>Many Vietnamese workers in the informal sector are not covered by social insurance because joining is a voluntary, active choice. Economists often suggest simpler sign-up, reminders and matching contributions from the state as ways to use present bias and inertia in reverse.</p><div class="use"><b>Exam use:</b> applies the pension default to a developing economy. Evaluate: a default needs a formal employer, so it is harder to use where many people are self-employed.</div></div>
  <div class="rw"><h3>Where Vietnam used law and tax instead</h3><p>Helmets for motorcycle riders became compulsory in 2007 and drink-driving is banned outright with heavy fines, both <b>regulation</b>. Single-use plastic bags are being phased out under the 2020 environment law, and a special consumption tax on sugary drinks has been legislated to start in 2027 (check the current details). These are not nudges.</p><div class="use"><b>Exam use:</b> shows the contrast. The helmet law worked where a nudge alone might not have, because the harm (death or head injury) is serious and enforcement was strong. A sensible answer says why a government might choose a ban, tax or nudge for a given problem.</div></div>
'''

exam = '''
  <h2>Past paper questions on nudge theory</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Nudge theory has appeared in <b>nine Paper 3 multiple choice questions</b> and in <b>two Paper 4 data response questions</b> (2020 and 2021). The data response questions are shown in our own words, with the marks and the points the mark scheme rewards summarised. The multiple choice questions are at the bottom of this tab.</p>
  <div class="tw"><table class="t">
    <tr><th>Paper</th><th>Question</th><th>Marks</th><th>What was asked</th></tr>
    <tr><td>May/June 2020 · 41 (and 43, not sat)</td><td>Q1(a)</td><td>2</td><td>Meaning of nudge theory</td></tr>
    <tr><td>May/June 2020 · 41 (and 43)</td><td>Q1(b)</td><td>6</td><td>Does the information show nudge theory could raise GDP?</td></tr>
    <tr><td>May/June 2021 · 41 (and 43)</td><td>Q1(b)</td><td>4</td><td>Evidence that behavioural economics can help public policy?</td></tr>
    <tr><td>Paper 3 MCQ</td><td>9 questions</td><td>1 each</td><td>Examples, non-examples and the essential feature of a nudge</td></tr>
  </table></div>

  <h2>A · Paper 4 data response parts</h2>
  <details class="eq"><summary>May/June 2020 · 9708/41 · Q1(a) <span class="mark">2 marks</span> The extract describes government "Nudge Units" in the US, UK and Australia. What is meant by nudge theory?</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>A definition with the idea of influencing behaviour by <b>persuasion or example</b> and the link to a government economic aim. Two marks: one for the idea of influencing behaviour without compulsion, one for the purpose.</div>
    <div class="tip"><b class="h">Command word: What is meant by</b>Short definition only. Do not evaluate or give a long example.</div>''' + KEY + '''
    <div class="ans"><p><span class="mk k" data-t="K">Nudge theory is the idea that governments can influence people's behaviour, by persuasion, example or by changing how choices are presented, without forcing them or changing prices,</span> <span class="mk k" data-t="K">so as to help achieve a policy aim such as higher employment, more tax revenue or better health.</span></p></div>
  </div></details>

  <details class="eq"><summary>May/June 2020 · 9708/41 · Q1(b) <span class="mark">6 marks</span> The extract says that nudge policies were used to get people back to work, to pay their taxes on time and to save for pensions or study for better qualifications. Consider whether the information provides any evidence that nudge theory could increase an economy's GDP.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>Use the evidence in the extract. Three routes to higher GDP are rewarded: <b>taxes paid</b> raise government revenue that could fund projects, <b>more people working</b> cuts unemployment and raises incomes, and <b>saving for education</b> could raise skills and productivity. A conclusion (hedged) earns the evaluation mark.</div>
    <div class="tip"><b class="h">Command word: Consider</b>Look at both the evidence for and its limits, then judge. Quote or refer to the extract.</div>''' + KEY + '''
    <div class="ans">
    <p><span class="mk a" data-t="A">The extract says nudge policies encouraged people to pay their taxes on time.</span> <span class="mk n" data-t="N">More tax revenue could allow the government to spend more on infrastructure and projects, and that spending is a component of aggregate demand and could raise GDP.</span></p>
    <p><span class="mk a" data-t="A">It also says nudges helped to get people back to work.</span> <span class="mk n" data-t="N">Falling unemployment means more output and more income, which may raise consumption and GDP through the multiplier.</span> <span class="mk a" data-t="A">Nudging people to study for better qualifications</span> <span class="mk n" data-t="N">could raise skill levels and productivity, which is likely to raise the productive capacity of the economy in the long run.</span></p>
    <p><span class="mk e" data-t="E">However, the extract only says nudges worked "with some success", and that they were not enough to remove the budget deficit, so the effect on GDP is likely to be small and may take years. The evidence is a claim rather than data, so it supports the view that nudge theory could increase GDP, but does not prove it.</span></p></div>
  </div></details>

  <details class="eq"><summary>May/June 2021 · 9708/41 · Q1(b) <span class="mark">4 marks</span> The article describes how a change in the wording of a letter sped up tax payments, how personalised text messages raised job fair attendance, and how automatic enrolment into pensions helped people to save. Is there evidence in the article that a knowledge of behavioural economics can help public policy?</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>Evidence from the text, tied to a policy aim: <b>lower unemployment</b> (job fair attendance), <b>higher tax payments</b> that could help to reduce the budget deficit, and <b>more saving</b> which could reduce demand-pull inflation pressure. Four marks means about two developed points.</div>
    <div class="tip"><b class="h">Command word: Is there evidence</b>Yes or no, then use the article. Spend your time on evidence, not on defining behavioural economics.</div>''' + KEY + '''
    <div class="ans">
    <p><span class="mk a" data-t="A">Yes. The article says jobseekers were nearly twice as likely to turn up to a job fair when the text used their names, and nearly three times as likely if "good luck" was added.</span> <span class="mk n" data-t="N">More people attending job fairs could lead to more people finding work, which would lower unemployment and raise output.</span></p>
    <p><span class="mk a" data-t="A">More behaviourally sensitive wording in a letter sped up tax payments,</span> <span class="mk n" data-t="N">which may improve the government's cash flow and help reduce a budget deficit without raising tax rates.</span> <span class="mk e" data-t="E">The evidence comes from small trials, so it may not apply to the whole economy, but it does suggest behavioural insights can help policy at low cost.</span></p></div>
  </div></details>

  <h2>B · Practice questions with model answers</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> A government wants more workers to save for retirement. Explain how a default could help, and consider one limit of this approach.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define the nudge. Present bias and inertia: why people do not save. Opt-out raises participation. One limit: minimum contributions, opt-outs, or poor effect on the self-employed.</div>''' + KEY + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">A default is the option that applies if a person does nothing, so under automatic enrolment workers are placed in a pension scheme unless they choose to leave.</span></p>
    <p><span class="mk n" data-t="N">Many people suffer from present bias, so they value spending now more than saving for later, and inertia means they rarely fill in forms. Under an opt-in system, many may not join even if they would have wanted to.</span> <span class="mk n" data-t="N">An opt-out system uses the same inertia in the other direction, so most workers are likely to stay in the scheme, and participation could rise sharply without a tax or a ban.</span> <span class="mk a" data-t="A">In the UK, automatic enrolment from 2012 was followed by a large rise in participation among eligible employees.</span></p>
    <p><span class="mk e" data-t="E">However, the default contribution is often low, and many people might stay at it, so total saving may still be too low. Workers in the informal sector or the self-employed are also not reached by an employer default, so the policy is likely to be less effective there.</span></p></div>
  </div></details>

  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">20 marks</span> Evaluate the view that nudge theory is more effective than taxation in reducing the consumption of demerit goods.</summary><div class="body">
    <div class="tip"><b class="h">What a Level 4 answer includes</b>
      <ul>
        <li><b>Analysis (14):</b> why demerit goods are over-consumed (information failure, present bias, external costs); how a nudge works (defaults, placement, labels, social norms) and how a tax works (diagram: unit tax shifts supply left, with price and quantity change, tax revenue); comparison with a diagram of an <b>inelastic demand</b> that makes a tax raise revenue more than it cuts consumption.</li>
        <li><b>Evaluation (6):</b> size of the effect, elasticity, time, cost, regressive effect of the tax on poorer households, ethical concern, evidence, and a judgement on when each tool works best (often together).</li></ul></div>''' + KEY + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">A demerit good, such as sugary drinks, is a good that is over-consumed because consumers under-estimate its harm and because it creates external costs. A nudge changes how the choice is presented without limiting it or changing the price, while a tax raises the price.</span></p>
    <p><span class="mk n" data-t="N">A nudge such as moving sugary drinks to a lower shelf, adding clear labels or making a smaller size the default could reduce demand, shifting the demand curve to the left. Because people remain free to choose, the nudge uses the behaviour that causes the problem, and it may be cheap to introduce.</span> <span class="mk n" data-t="N">A tax shifts supply to the left, raising the price and reducing quantity along the demand curve. The fall in consumption depends on the price elasticity of demand: if demand is inelastic, the percentage fall in quantity is smaller than the percentage rise in price, so the tax may do little to reduce consumption but raise considerable revenue.</span></p>
    <p><span class="mk a" data-t="A">In England, the Soft Drinks Industry Levy led manufacturers to cut the sugar in many drinks, which shows that a tax can change behaviour on the supply side as well as the demand side.</span> <span class="mk n" data-t="N">A nudge on its own has no such effect on producers, and firms may also use their own nudges, such as prominent displays, to push sales the other way.</span></p>
    <p><span class="mk e" data-t="E">Overall, the answer is likely to depend on the good and on the evidence. Where harm is serious or habit-forming, as with cigarettes, nudges are likely to be too weak and a tax or a ban is probably needed. Where people are mainly distracted or undecided, as with food choice in a canteen, a nudge may be more cost-effective and avoid the regressive impact of a tax on lower-income households. A tax raises revenue that can be used to fund health care, whereas a nudge does not.</span> <span class="mk e" data-t="E">The strongest case is most likely to be a combination, since nudges often work better when a small price signal supports them, and the effects of nudges also tend to be measured over short periods, which makes their long-run impact uncertain. Therefore the view is probably only true for goods where consumers are open to persuasion and demand is inelastic to price.</span></p></div>
  </div></details>

  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number. The questions have been asked across 2020 to 2025.</p>
  <div id="qz2"></div>
'''

tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Define it in one line.</b> Influencing behaviour by persuasion or example, or by changing how a choice is presented, without forcing it or changing the price. That wins the 2 marks.</li>
    <li><b>A tax is not a nudge.</b> Neither is a ban, a subsidy, a fine or a licence. The Paper 3 questions test this again and again.</li>
    <li><b>Information and persuasion usually count.</b> Telling people what others do, or the harm of tax evasion, is the standard "nudge" answer in tax questions (2025 papers).</li>
    <li><b>Name the behaviour.</b> Inertia, present bias, social norms, framing or salience. This turns a description into analysis.</li>
    <li><b>Link to the failure.</b> Demerit good, merit good, information failure or an externality. Then say which curve moves.</li>
    <li><b>For data response, quote the extract.</b> "Nearly three times as likely..." earns more than general theory.</li>
    <li><b>Evaluate with three points:</b> size and duration of effect, cost, and whether it works alone. Finish with a hedged judgement.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Define a nudge</td><td>"A nudge changes how a choice is presented so that people are steered towards a better option, without banning anything or changing prices."</td></tr>
    <tr><td>Explain a default</td><td>"Because of inertia, most people stay with the default, so changing it could raise participation while leaving people free to choose."</td></tr>
    <tr><td>Compare with a tax</td><td>"A tax changes the price, so it is not a nudge. It may be more effective for a good with inelastic demand, but it can be regressive."</td></tr>
    <tr><td>Judge the effect</td><td>"The effect could be small or may fade, so a nudge is likely to work best alongside other policies."</td></tr>
    <tr><td>Raise the ethical point</td><td>"Nudges raise questions over who decides what is best for consumers, although choice remains."</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''

body = page(EY, "Nudge Theory", "How governments steer choices without forcing them: the behaviour behind it, the types of nudge, examples from the UK and Vietnam, animated diagrams, labs, and every nudge question from the Paper 3 and Paper 4 past papers 2020 to 2025.",
            learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips)

js = r'''
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
'''

write("nudge", body, js, "Nudge Theory", "nudge-theory")
