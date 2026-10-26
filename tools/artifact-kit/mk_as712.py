"""AS CS 7.1.2: artificial intelligence and its impact. Run: python3 tools/artifact-kit/mk_as712.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Artificial intelligence (AI)</b> is the ability of a computer system to perform tasks that normally need human intelligence, such as recognising faces, understanding speech and playing games, by using <b>data</b>, <b>patterns</b> and <b>training</b>. AI systems are trained on large amounts of data and learn to make a prediction, such as the probability that an image matches a face. Typical applications are <b>image and facial recognition</b>, <b>speech recognition and natural language processing</b>, <b>optical character recognition</b>, <b>self-driving cars</b> and <b>game playing</b>. AI has <b>social</b>, <b>economic</b> and <b>ethical</b> impacts, both positive and negative; exam answers describe one clearly and link it to the situation. The explaining questions ask how a given system uses AI, with a chain such as camera, pixels, features, comparison with a database and a probability of a match.</p></div>

  <h2>1 · How AI is used in common systems</h2>
  <div class="tw"><table class="t">
    <tr><th>System</th><th>How it uses AI</th></tr>
    <tr><td><b>Facial recognition</b> (phone unlock, shop entry, CCTV)</td><td>The camera captures an image; image recognition identifies that it is a face by analysing the pixels for patterns; the distances between facial features are measured and compared with those stored in a database; the system uses the probability of a match. It is trained using a large number of images</td></tr>
    <tr><td><b>CCTV tracking</b></td><td>Image recognition monitors every image for shapes or features that match a person; recording starts when a person is identified; the direction of movement is used to decide where to move the camera or which camera to start</td></tr>
    <tr><td><b>Reading registration plates</b> (optical character recognition)</td><td>The camera image is stored as pixels; the area of the plate is found; the pixels are matched to expected characters, letters and numbers</td></tr>
    <tr><td><b>Voice assistants and robots</b> (speech and natural language)</td><td>Speech recognition identifies the words or key phrases spoken and matches them to a database; natural language processing combines them into the most likely sentence or command and the programmed action is performed</td></tr>
    <tr><td><b>Reading and translating text</b></td><td>Optical character recognition finds characters in the photograph; natural language processing combines them into words and compares them with a database in the chosen language; text-to-speech generates audio</td></tr>
    <tr><td><b>Game playing</b></td><td>The rules and past moves are stored; the AI is trained by playing many times; it looks ahead at possible moves and chooses the move most likely to succeed; it learns from past mistakes by storing the result of each choice and changing future choices</td></tr>
    <tr><td><b>Self-driving cars</b></td><td>Sensors and cameras detect the car's position on the road and in traffic; it follows a route, avoids collisions and parks itself</td></tr>
  </table></div>

  <h2>2 · Impacts of AI</h2>
  <div class="tw"><table class="t">
    <tr><th>Impact</th><th>Positive</th><th>Negative</th></tr>
    <tr><td><b>Social</b></td><td>Helps visually impaired people choose products; helps people who cannot understand a language; helps with learning or reading difficulties; individuals may feel safer and crime may be reduced; early help for students who struggle</td><td>Privacy concerns about constant surveillance and data passed to third parties; mistakes such as incorrect recognition of faces (people denied access); misinformation if an AI answer is wrong; students may miss out on developing reasoning skills; digital divide; stress and loneliness</td></tr>
    <tr><td><b>Economic</b></td><td>Lower costs (for example faster fault diagnosis in a garage so technicians complete more jobs); higher profits; lower prices passed to customers</td><td>The AI program may be expensive to buy, maintain and update, which reduces profit margins; jobs may be lost</td></tr>
    <tr><td><b>Ethical</b></td><td>More personalised learning; improved safety</td><td>Surveillance and consent; protection of intellectual property; bias and incorrect results</td></tr>
  </table></div>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing that AI "thinks like a human". Describe the actual steps: image recognition, comparison with a database, probability of a match.</li>
    <li>Describing only what the system does (recognises a face) and not how AI does it.</li>
    <li>Giving an impact with no explanation. "Privacy concerns" needs "because people are under constant surveillance".</li>
    <li>Giving a positive impact when the question asks for an ethical impact only if it concerns ethics (privacy, consent, surveillance, bias).</li>
    <li>Confusing AI with simple programming. AI is trained on data and works with probabilities.</li>
  </ul>
'''

watch = '''
  <h2>1 · Facial recognition</h2>
  <div id="stA"></div>
  <h2>2 · Training an AI</h2>
  <div id="stB"></div>
  <h2>3 · Looking ahead in a game</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Match threshold</h2>
  <p>The system compares a face to the stored one and gives a probability of a match. Change the threshold at which access is allowed.</p>
  <div class="card"><div id="tS"></div><div id="tG"></div><div id="tV" class="verdict"></div></div>
  <h2>Lab 2 · Which AI technique?</h2>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aO"></div></div>
  <h2>Lab 3 · Social, economic or ethical?</h2>
  <div class="card"><div id="iB" class="btnrow"></div><div id="iO"></div></div>
'''

_pr, _prjs = PR(["Which AI technique?", "Positive or negative impact?", "Match the AI use to its description", "Put facial recognition in order", "Working out", "Multiple choice"],
  ("Which AI technique does the description use?", ["Image recognition", "Speech recognition", "Game-playing AI"], [("Compares the pixels of a camera image with stored features", 0), ("Matches spoken words to a database of words", 1), ("Looks ahead at possible moves and picks the most likely to win", 2), ("Identifies a face from the distance between features", 0), ("Turns key phrases heard into a command", 1), ("Learns from previous mistakes by changing future choices", 2)], "Match the technique."),
  ("Is it a positive or a negative impact of AI?", ["Positive", "Negative"], [("Helps visually impaired people choose products", 0), ("Constant surveillance causes privacy concerns", 1), ("Faster fault diagnosis lowers costs for a garage", 0), ("Incorrect recognition denies someone access", 1), ("Personalised support for struggling students", 0), ("A wrong AI answer gives misinformation", 1)], "Helps: positive. Harms: negative."),
  [["Image recognition", "Compares pixels with stored features"], ["Speech recognition", "Matches spoken words to a database"], ["Natural language processing", "Works out the meaning of a sentence"], ["Training", "Learning from a large amount of data"], ["Probability of a match", "How likely it is that the image is the person"]],
  ("Put facial recognition in order.", ["The camera captures an image", "Image recognition identifies that there is a face", "The distances between facial features are measured", "The values are compared with those in the database", "Access is allowed if the probability of a match is high enough"], "Capture, find face, measure, compare, decide."),
  [{"q": "A system compares a face with 1000 stored faces. How many comparisons for one face?", "a": 1000, "unit": "", "tol": 0.01, "hint": "One per stored face.", "sol": "<b>1000</b>."}, {"q": "A face scanner is right 98% of the time. How many errors in 500 scans?", "a": 10, "unit": "", "tol": 0.01, "hint": "2% of 500.", "sol": "<b>10</b>."}, {"q": "A garage saves 20 minutes on each of 6 diagnoses a day. How many hours saved per day?", "a": 2, "unit": "h", "tol": 0.01, "hint": "120 minutes.", "sol": "<b>2</b> hours."}, {"q": "A chess AI looks 3 moves ahead with 10 choices each move. How many move sequences?", "a": 1000, "unit": "", "tol": 0.01, "hint": "10^3.", "sol": "<b>1000</b>."}, {"q": "An AI trained on 40 000 images uses 80% for training. How many images for training?", "a": 32000, "unit": "", "tol": 0.5, "hint": "0.8 × 40 000.", "sol": "<b>32 000</b>."}],
  [("Facial recognition compares:", ["Facial features with a database", "The phone battery", "Only passwords", "Colours of the room"], 0, "Features and database."), ("Speech recognition:", ["Matches words to a database", "Compresses audio", "Prints text only", "Needs no data"], 0, "Matches words."), ("A game AI improves by:", ["Learning from past mistakes", "Using a new screen", "Ignoring the rules", "Copying files"], 0, "Learns."), ("A negative social impact of AI:", ["Privacy concerns from surveillance", "Faster diagnosis", "Lower costs", "Better translation"], 0, "Privacy."), ("An economic impact of AI:", ["Lower costs for a business", "More colourful screens", "Quieter fans", "Bigger buttons"], 0, "Costs."), ("OCR is used to:", ["Convert pixels into characters", "Encrypt data", "Record video", "Count users"], 0, "Pixels to characters.")],
  [("AI", "Computer performing tasks needing human intelligence."), ("Image recognition", "Pixels to features; compare with database."), ("Speech recognition", "Words matched to a database."), ("OCR", "Pixels to characters."), ("Training", "Learning from large amounts of data."), ("Social impact", "Privacy, safety, accessibility."), ("Economic impact", "Costs, profits, jobs."), ("Ethical impact", "Surveillance, bias, consent.")])

real = RWNOTE + (
rw("Unlocking your phone with your face", "The phone measures the distances between your facial features and compares them with the stored values: image recognition and a probability of a match.", "facial recognition.") +
rw("Voice assistants", "You speak a request; the assistant identifies the words, matches them to commands and replies: speech recognition and natural language processing.", "speech recognition.") +
rw("Number plate cameras in car parks", "The camera finds the plate and optical character recognition turns the pixels into the registration number.", "OCR.") +
rw("A chess program", "It looks ahead at possible moves and picks the one most likely to win, improving from experience.", "game-playing AI.") +
rw("A translation app that reads signs", "The camera reads the text, the app translates it and says it aloud: it helps people who cannot read the language.", "OCR, language processing, text-to-speech.")
)

where = [
  ("M/J 2021", "12", "2(b)", "3", "How the computer would use AI to play a board game"),
  ("M/J 2022", "12", "8", "3", "Describe one application of AI"),
  ("O/N 2022", "12", "9", "2", "The social impact of facial recognition in an airport"),
  ("O/N 2022", "13", "8(b)", "2", "One economic impact of an AI module in a garage"),
  ("M/J 2023", "11", "4(c)", "3", "How AI is used in a CCTV system"),
  ("M/J 2023", "12", "7(d)", "3", "How AI converts speech into commands"),
  ("M/J 2023", "13", "3(b)", "3", "How AI focuses a camera on faces"),
  ("M/J 2024", "11", "5(c)(ii)", "4", "How AI is used in facial recognition"),
  ("M/J 2024", "13", "7(b)", "3", "How AI is used for a robot to communicate with customers"),
  ("O/N 2024", "11", "6", "4", "How AI identifies a car's registration number"),
  ("M/J 2025", "11", "4(a)", "4", "How a shop system uses AI to identify customers"),
  ("M/J 2025", "12", "3(a), (b)", "4 + 2", "How AI reads and translates words; two social benefits"),
  ("O/N 2025", "11", "8(c)", "4", "Two social impacts of students using AI for homework"),
  ("O/N 2025", "13", "7(a)", "2", "One ethical impact of AI analysing classroom video")]

past = '''  <p class="note">AI questions appear in Paper 1 every year with a different scenario. The marking is always a short chain of steps (capture, analyse, compare, decide). Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "12", "Q2(b)"), "3 marks", "Describe",
  "The team are developing a computer game where the user plays a board game (such as chess) against the computer. Describe how the computer would use Artificial Intelligence (AI) to play the board game.", "Rules and moves stored, trained, look ahead, choose, learn.",
  "<p>Any three: " + mks(["The rules, past moves or decision-making algorithms of the game are stored", "The AI program is trained by playing many times", "The AI looks ahead at possible moves", "and/or analyses the pattern of past choices", "and chooses the move most likely to be successful", "The computer could learn from previous mistakes by storing the result of choices and changing its future choices"]) + "</p>", None) + peq(SRC("s22", "12", "Q8"), "3 marks", "Describe",
  "Describe one application of Artificial Intelligence (AI).", "Name an application and describe it.",
  "<p>One mark for the application and up to two for the description, for example: " + mks(["Police identifying wanted people: uses image recognition to identify features or characteristics in an image", "Natural language interface: uses speech recognition to identify spoken words and adapts to learn regional accents", "Self-driving cars: detects its position on the road and in traffic, follows a route, avoids collisions", "Game playing: models characters so they react according to the player's movements"]) + "</p>", None) + peq(SRC("w22", "12", "Q9"), "2 marks", "Describe",
  "One use of AI is facial recognition software. Describe the social impact of using facial recognition software to identify individuals in an airport.", "Mistakes, privacy, safer, less crime, faster boarding.",
  "<p>Any two: " + mks(["Incorrect recognition of faces leads to mistakes, such as access to facilities being denied", "Privacy issues: people do not like data being stored", "Individuals will feel safer and there might be a reduction in crime", "Faster boarding", "Catching criminals"]) + "</p>", None) + peq(SRC("w22", "13", "Q8(b)"), "2 marks", "Describe",
  "A commercial program for a vehicle repair garage includes an AI module that can diagnose faults and suggest repairs. Describe one economic impact the AI module may have on the garage.", "Costs and profits, with a reason.",
  "<p>One impact and one expansion: " + mks(["Reduces costs to the garage because less time is taken for diagnosis", "Increases profits because technicians spend more time repairing, completing more jobs in a day", "Decreases costs passed to customers, so the garage may gain customers", "Profit margins can be reduced because the program may be expensive to buy, maintain or update"]) + "</p>", None) + peq(SRC("s23", "11", "Q4(c)"), "3 marks", "Describe",
  "A CCTV system uses Artificial Intelligence to identify the presence of a person in the house and to track their movements. Describe how AI is used in this system.", "Image recognition, person, recording, direction of movement.",
  "<p>Any three: " + mks(["Uses image recognition", "Monitors every image taken to identify matching images, shapes or features of a person", "Starts recording to secondary storage when a person is identified", "Identifies the direction of movement of the person and uses it to decide where or how to move the camera or record", "Identifies other cameras to start recording based on the direction of movement"]) + "</p>", None) + peq(SRC("s23", "12", "Q7(d)"), "3 marks", "Explain",
  "One section of the program converts the user's speech into commands. Explain how AI can be used in this program.", "Speech recognition, key phrases, database, most likely command.",
  "<p>Any three: " + mks(["Uses speech recognition", "which identifies key phrases or words spoken", "and matches these to a database", "and generates the most likely sentence, command or word"]) + "</p>", None) + peq(SRC("s23", "13", "Q3(b)"), "3 marks", "Explain",
  "The digital camera automatically focuses on the faces of people. Explain how AI is used by the camera.", "Scans the scene, identifies a face pattern, focuses on it.",
  "<p>Any three: " + mks(["Scans the scene in real time", "Identifies if there are faces in the image using facial or image recognition", "Takes each frame individually and analyses the pixels", "Stores the pattern for a face and looks for patterns that match or come close", "The camera focuses on the pattern identified"]) + "</p>", None) + peq(SRC("s24", "11", "Q5(c)(ii)"), "4 marks", "Describe",
  "One biometric authentication method is facial recognition. Facial recognition uses Artificial Intelligence. Describe how AI is used in facial recognition.", "Capture, image recognition, trained, features, probability.",
  "<p>Any four: " + mks(["Captures an image of the face", "Uses image recognition", "Is trained to identify the features of a face in an image using a large number of images", "Analyses the images for facial features", "Uses the probability of a match"]) + "</p>", None) + peq(SRC("s24", "13", "Q7(b)"), "3 marks", "Explain",
  "A robot uses Artificial Intelligence to communicate with customers who speak to it to order food and drink. Explain how AI will be used in this part of the robot.", "Speech recognition, sound compared with a database, natural language.",
  "<p>Any three: " + mks(["Voice or speech recognition is used", "to identify if someone is speaking", "The sound is recorded and analysed", "The audio is compared to a database of words or sound waves to identify the word with the highest probability of being said", "Natural language recognition combines words and compares them with known sentences", "The programmed actions for matching sentences are performed"]) + "</p>", None) + peq(SRC("w24", "11", "Q6"), "4 marks", "Explain",
  "A car park system uses a camera to record the registration number of each car. Explain how artificial intelligence is used to identify the car's registration number.", "Image recognition and OCR on pixels.",
  "<p>Any four: " + mks(["It uses image recognition", "The pixels of each image from the camera are stored", "and matched to the expected shape, size or colour of a registration number", "It uses optical character recognition", "The pixels within the identified registration area are analysed", "and compared to expected characters, letters and numbers"]) + "</p>", None) + peq(SRC("s25", "11", "Q4(a)"), "4 marks", "Explain",
  "A shop system uses digital cameras and Artificial Intelligence to identify the customers. Explain how the new system uses AI to identify each customer.", "Image captured, face found, distances measured, compared with the database.",
  "<p>Any four: " + mks(["Uses image recognition or facial recognition", "Measures the distance between facial features of the customer", "and stores the values in a database of user information", "An image is captured using the digital camera", "The AI identifies that the image is a face by analysing the pixels for patterns", "The distances between features are calculated and compared to those in the database"]) + "</p>", None) + peq(SRC("s25", "12", "Q3(a)(b)"), "4 + 2 marks", "Explain / State",
  "A computer program uses a digital camera to read the words on an item, translates them to a chosen language and outputs the words as audio. It uses AI. (a) Explain how AI is used. (b) State two social benefits of the use of AI in the program.", "OCR, natural language, text-to-speech. Visual impairment, language, reading difficulty.",
  "<p><b>(a)</b> Any four: " + mks(["Uses image recognition or optical character recognition to analyse the pixels and identify the location of characters", "to convert the pattern of pixels into individual characters", "Uses natural language processing to combine the characters into words and compare them to a database in the chosen language to translate", "Uses text-to-speech to generate the audio waveforms for the words"]) + "</p><p><b>(b)</b> Any two: " + mks(["It can help people with visual impairment identify which products to buy", "It can help people who cannot understand the language", "It can help to overcome learning or reading difficulties"], "a") + "</p>", None) + peq(SRC("w25", "11", "Q8(c)"), "4 marks", "Describe",
  "Describe two social impacts of students using Artificial Intelligence to complete their homework.", "Reasoning skills, communication, digital divide, wrong answers; support, self-esteem.",
  "<p>Any four (an impact and its expansion for each): " + mks(["If students use AI to shortcut learning they may miss out on developing reasoning and problem-solving skills", "Heavy reliance on AI may limit opportunities for collaboration and communication", "It emphasises the digital divide: some students may not have access to the technology", "The AI answer might not be correct, leading to misinformation", "Increased screen time and isolation could contribute to anxiety or loneliness", "Students given additional support may do better", "Pupils who struggle may gain self-esteem through AI-assisted learning at their own pace"]) + "</p>", None) + peq(SRC("w25", "13", "Q7(a)"), "2 marks", "Describe",
  "A digital video camera records students in a classroom. AI is used to analyse the video on the server to identify when students are interacting with the lesson and the teacher. Describe one ethical impact of this use of AI in the classroom.", "Privacy, surveillance, mental health, or improved learning.",
  "<p>One impact and its expansion: " + mks(["The learning experience could be improved by identifying students who are struggling, with more personalised learning or early intervention", "There could be privacy concerns because students or teachers may be uncomfortable with constant surveillance, or may not want their data passed to third parties", "There could be mental health concerns due to constant monitoring and pressure, contributing to student stress and anxiety"]) + "</p>", None)

review = req("3 marks", "Describe", "Describe how AI could be used by a supermarket checkout camera to identify the fruit a customer places on the scale.", "Image recognition, compare, probability.", "<p>" + mks(["The camera captures an image of the item", "Image recognition analyses the colour, shape and size of the pixels", "These are compared with stored data to find the most probable match"]) + "</p>", None) + req("2 marks", "Describe", "Describe one negative social impact of using facial recognition in a shop.", "Privacy, errors.", "<p>" + mks(["Customers' faces are recorded and stored, causing privacy concerns", "Incorrect recognition could mean a customer is wrongly refused entry"]) + "</p>", None) + req("2 marks", "Explain", "Explain why an AI system needs to be trained on a large amount of data.", "Patterns.", "<p>" + mks(["It learns the patterns that identify what it is looking for", "more data makes the probability of a correct match higher"]) + "</p>", None) + req("2 marks", "Describe", "Describe one economic impact of AI on a delivery company.", "Costs, jobs.", "<p>" + mks(["Self-driving vehicles could reduce the cost of drivers", "but the cost of buying and maintaining the AI is high and jobs could be lost"]) + "</p>", None) + req("3 marks", "Explain", "Explain how speech recognition could be used by a voice assistant to set an alarm.", "Words, database, command.", "<p>" + mks(["The microphone records the speech", "Speech recognition identifies the key words and matches them to a database", "The most likely command is generated and the alarm is set"]) + "</p>", None)

tips = tips_html([
  ("Give the chain.", "Capture, analyse, compare, decide."),
  ("Name the technique.", "Image recognition, speech recognition, OCR, NLP."),
  ("Probability of a match.", "AI works with likelihood, not certainty."),
  ("Impact plus reason.", "Social: privacy because of surveillance."),
  ("Trained on large data.", "Say it for any AI question."),
  ("Use the scenario's words.", "The shop, the robot, the airport."),
], [("AI", "A computer system doing tasks that need human intelligence."), ("image recognition", "Analysing pixels to identify shapes or features."), ("OCR", "Optical character recognition: pixels to characters."), ("natural language processing", "Working out the meaning of words and sentences.")],
  [("Describe", "Several points in order."), ("Explain", "Reasons as well."), ("State", "Short answer."), ("Give", "Impact or example.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 100, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 50, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(10, "camera image", k >= 0) + B(130, "face found?", k >= 1) + B(250, "measure", k >= 2) + B(370, "compare", k >= 3) + B(490, "match: 96%", k >= 4); for (let i = 0; i < 4; i++) o += SV.path(`M${110 + i * 120},62 H${130 + i * 120}`, "ax"); return o; };
  Lib.stepper($("#stA"), { w: 610, h: 110, label: "Facial recognition", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The camera captures an image.", "Image recognition finds that there is a face.", "The distances between facial features are measured.", "They are compared with the values in the database.", "The system gives a probability of a match."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const n = [0, 6, 24, 60][k]; let o = SV.text(20, 20, "training images: " + n, "lbl bd"); for (let i = 0; i < 60; i++) o += SV.rect(20 + (i % 20) * 24, 30 + Math.floor(i / 20) * 24, 20, 20, i < n ? "f1" : "cell", { rx: 3 }); o += SV.text(20, 125, ["", "few examples: rarely right", "more examples: right more often", "a large amount of data: the AI learns the patterns well"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 140, label: "Training", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["An AI starts with no examples.", "Trained on a few images: it often gets it wrong.", "With more images: it improves.", "Trained on a large number of images it learns the patterns."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const mv = [["now", "start"], ["move A", "score 3"], ["move B", "score 7"], ["move C", "score 5"], ["choose", "move B"]][k]; let o = SV.rect(20, 40, 100, 40, "f3", { rx: 8 }) + SV.text(70, 65, "position", "lbl bd", { "text-anchor": "middle" });
    [["A", 3], ["B", 7], ["C", 5]].forEach(([n, v], i) => { if (i < k) o += SV.path(`M120,60 L220,${35 + i * 40}`, "ax") + SV.rect(220, 20 + i * 40, 120, 30, v === 7 && k === 4 ? "f1" : "cell", { rx: 6 }) + SV.text(280, 40 + i * 40, "move " + n + ": " + v, "lbl", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.text(380, 70, k === 4 ? "picks the best" : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 150, label: "Game AI", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The AI looks at the current position.", "It looks ahead at move A: a low score.", "Move B scores higher.", "Move C is middle.", "It chooses the move most likely to be successful."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let th = 80; const same = [96, 91, 88, 74, 99, 85], other = [32, 55, 61, 78, 45, 69]; const paint = () => { const fn = same.filter((v) => v < th).length, fp = other.filter((v) => v >= th).length;
    let o = '<svg viewBox="0 0 420 100" style="width:420px;max-width:100%;display:block"><path d="M20,70 H400" class="ax"/>'; same.forEach((v, i) => o += `<circle cx="${20 + v * 3.7}" cy="${50 - (i % 2) * 14}" r="6" fill="var(--good)"/>`); other.forEach((v, i) => o += `<circle cx="${20 + v * 3.7}" cy="${52 - (i % 2) * 14}" r="6" fill="var(--bad)"/>`); o += `<line x1="${20 + th * 3.7}" y1="10" x2="${20 + th * 3.7}" y2="80" stroke="var(--accent)" stroke-width="2"/><text x="20" y="95" class="sm" style="font-size:11px">probability of match (%)</text></svg>`; $("#tG").innerHTML = o;
    $("#tV").innerHTML = `Access is allowed when the match probability is at least <b>${th}%</b>. Green = the real owner, red = other people. With this threshold <b>${fn}</b> owner scan(s) are wrongly refused and <b>${fp}</b> other person scan(s) are wrongly accepted. A high threshold is safer but refuses the owner more often: AI works with probabilities, so mistakes happen.`; };
  Lib.slider($("#tS"), { id: "t1", label: "Threshold (%) ", min: 30, max: 100, value: th, fmt: (x) => x, onInput: (v) => { th = v; paint(); } }); paint();
})();
btnTable("aB", "aO", [
  ["Unlocking a phone with your face", "Image (facial) recognition", "Compares facial features with stored values"],
  ["Asking a speaker to play music", "Speech recognition + language processing", "Words matched to a command"],
  ["Reading a car's number plate", "Optical character recognition", "Pixels to characters"],
  ["A computer opponent in chess", "Game-playing AI", "Looks ahead, learns from mistakes"],
  ["A car that stays in its lane", "Self-driving AI", "Detects position and avoids collisions"]
], ["Situation", "AI technique", "Key idea"]);
btnTable("iB", "iO", [
  ["Helps visually impaired people choose products", "Social (positive)", "Accessibility"],
  ["Faster fault diagnosis saves a garage money", "Economic (positive)", "Lower costs, higher profit"],
  ["Constant classroom monitoring raises stress", "Ethical (negative)", "Surveillance and wellbeing"],
  ["An AI program is expensive to buy and update", "Economic (negative)", "Reduces profit margins"],
  ["Wrong recognition denies someone access", "Social (negative)", "Mistakes affect people"]
], ["Impact", "Type", "Why"]);
''' + _prjs

finish("as-7-1-2-artificial-intelligence", "as712", "Artificial Intelligence and its Impact",
  "How facial recognition, speech recognition, optical character recognition and game-playing AI work, and the social, economic and ethical impacts of AI, with animations, a match-threshold lab and the real Paper 1 questions from 2021 to 2026.",
  "7.1.2", "7 · Ethics and ownership", "section 7.1 Ethics and ownership", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on artificial intelligence (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
