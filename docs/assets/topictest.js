// Topic test page: ?t=<chapter path>, e.g. a-econ/as/s2-2. MCQs are marked on the server. Written questions are
// self-marked: after submitting, the student ticks the mark points their answer earned and the server adds them up.
// Unlimited attempts; every finished attempt is kept for the tracker.
(function () {
  const S = window.Site;
  const root = document.getElementById("tt-root");
  const id = new URLSearchParams(location.search).get("t") || "";
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const $ = (sel, el = root) => el.querySelector(sel);
  const draftKey = "site.ttdraft." + id;
  let quiz, me;

  const chapterUrl = () => S.base + id + "/";
  const trackerUrl = () => S.base + "progress/";
  const loadDraft = () => { try { return JSON.parse(localStorage.getItem(draftKey) || "{}"); } catch (e) { return {}; } };
  const saveDraft = (d) => { try { localStorage.setItem(draftKey, JSON.stringify(d)); } catch (e) {} };
  const clearDraft = () => { try { localStorage.removeItem(draftKey); } catch (e) {} };
  const marksWord = (n) => `${n} mark${n === 1 ? "" : "s"}`;
  const para = (t) => esc(t).split(/\n+/).map((x) => `<p>${x}</p>`).join("");
  const code = (q) => (q.code ? `<pre class="code">${esc(q.code)}</pre>` : "");
  const ctx = (q) => (q.context ? `<div class="qctx">${para(q.context)}</div>` : "");
  const ICONS = {
    ok: '<path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    no: '<path d="M7 7l10 10M17 7L7 17" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
    part: '<path d="M6 12h12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
  };
  const icon = (k) => `<svg class="ico ${k}" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><circle cx="12" cy="12" r="12"/>${ICONS[k]}</svg>`;

  const keepNote = `<p class="note"><b>Every attempt is saved.</b> You can retake this test as often as you like. All of your scores go on your progress chart, so your first score and your improvement both show. Teachers can see them too.</p>`;

  function field(q, val) {
    if (q.type === "mcq") {
      return `<div class="opts">${q.opts.map((o, i) => `<label class="opt"><input type="radio" name="${q.id}" value="${i}" ${String(val) === String(i) ? "checked" : ""}> <span>${esc(o)}</span></label>`).join("")}</div>`;
    }
    return `<textarea class="ans" name="${q.id}" rows="${Math.min(14, 3 + q.marks)}" placeholder="Write your answer here.">${esc(val || "")}</textarea>`;
  }

  function viewIntro() {
    const preview = !!(me.is_admin || me.is_teacher || me.is_school_teacher);
    const total = quiz.questions.reduce((t, q) => t + q.marks, 0);
    const mcq = quiz.questions.filter((q) => q.type === "mcq").length;
    const wr = quiz.questions.filter((q) => q.type === "written").length;
    root.innerHTML = `<section class="card block"><h3>${esc(quiz.title)}</h3>
      <p class="hint">${total} marks: ${mcq} multiple choice question${mcq === 1 ? "" : "s"} and ${wr} written question${wr === 1 ? "" : "s"}. The multiple choice is marked for you. For the written questions you see the model answer and mark points, then tick the marks your answer earned. Be honest: the tracker only helps if the marks are accurate.</p>
      ${keepNote}
      ${quiz.tries ? `<p class="hint">You have taken this ${quiz.tries} time${quiz.tries === 1 ? "" : "s"}. Best score so far: <b>${quiz.best}%</b>.</p>` : ""}
      ${preview ? '<p class="msg err">You are signed in as a teacher, so you can read the questions but not submit.</p>' : ""}
      ${quiz.pending ? `<p class="msg err">You submitted an attempt but did not finish self-marking it.</p><p><button class="btn" id="resume">Finish marking that attempt</button></p>` : ""}
      <p><button class="btn" id="start">${quiz.pending ? "Start a new attempt instead" : "Start the test"}</button> <a class="btn ghost" href="${chapterUrl()}">Back to the chapter</a></p></section>`;
    $("#start").onclick = () => viewForm(preview);
    $("#resume")?.addEventListener("click", async () => {
      const { data, error } = await S.sb.rpc("resume_topic_test", { _attempt: quiz.pending });
      if (error) return alert(error.message);
      viewMark(data);
      window.scrollTo(0, 0);
    });
  }

  function viewForm(preview) {
    const draft = loadDraft();
    root.innerHTML = `<section class="card block"><h3>${esc(quiz.title)}</h3>
      <p class="hint">Answer from memory first. Your answers are kept on this device until you submit.</p>${keepNote}</section>
      <form id="qf">${quiz.questions.map((q, i) => `<section class="card block q"><div class="row"><b>Question ${i + 1}</b><span class="hint">${marksWord(q.marks)}</span></div>
        ${ctx(q)}<p class="qtext">${esc(q.q)}</p>${code(q)}${field(q, draft[q.id])}</section>`).join("")}
        <section class="card block"><p class="hint" id="left"></p><p class="msg err" hidden></p><button class="btn" type="submit" ${preview ? "disabled" : ""}>Submit answers</button></section></form>`;
    const f = $("#qf"), left = $("#left");
    const read = () => Object.fromEntries(quiz.questions.map((q) => {
      const el = f.elements[q.id];
      return [q.id, q.type === "mcq" ? (f.querySelector(`[name=${q.id}]:checked`)?.value ?? "") : (el.value || "").trim()];
    }));
    const upd = () => {
      const a = read(), n = Object.values(a).filter((v) => v !== "").length;
      left.textContent = `${n} of ${quiz.questions.length} answered.`;
      saveDraft(a);
    };
    f.addEventListener("input", upd); upd();
    f.addEventListener("submit", async (e) => {
      e.preventDefault();
      const a = read(), blank = Object.values(a).filter((v) => v === "").length;
      if (!confirm(`${blank ? blank + " question(s) are blank. " : ""}Submit now? You cannot change your answers afterwards, but you can retake the test.`)) return;
      const btn = f.querySelector("button[type=submit]"), m = $(".msg", f);
      btn.disabled = true;
      const { data, error } = await S.sb.rpc("submit_topic_test", { _id: id, _answers: a });
      if (error) { btn.disabled = false; m.textContent = error.message; m.hidden = false; return; }
      clearDraft();
      viewMark(data);
      window.scrollTo(0, 0);
    });
  }

  function mcqCards(items) {
    return items.map((it, i) => {
      const full = it.got >= it.max;
      return `<section class="card block q ${full ? "good" : "bad"}"><div class="row"><b>Multiple choice ${i + 1}</b><span class="score">${icon(full ? "ok" : "no")}<small>${it.got} / ${it.max}</small></span></div>
        <p class="qtext">${esc(it.q)}</p>${code(it)}
        <p><span class="hint">Your answer</span><br>${it.typed ? esc(it.typed) : "<i>No answer</i>"}</p>
        ${full ? "" : `<p><span class="hint">Correct answer</span><br>${esc(it.model)}</p>`}
        ${it.feedback ? `<p class="fb">${esc(it.feedback)}</p>` : ""}</section>`;
    }).join("");
  }

  // Step 2: MCQ marked; student self-marks the written questions.
  function viewMark(r) {
    const ticks = {};
    r.written.forEach((w) => { ticks[w.id] = new Set(); });
    const sum = (w) => Math.min(w.marks, [...ticks[w.id]].reduce((t, i) => t + (w.points[i]?.m || 1), 0));
    root.innerHTML = `<section class="card block"><div class="row"><h3>${esc(r.title || quiz?.title || "Topic test")}</h3><span class="big">${r.mcq_score} / ${r.mcq_max}</span></div>
      <p><b>Multiple choice marked.</b> Now mark your written answers. For each question, read the model answer, then tick every mark point your own answer clearly made. A point only counts if you said it, not if you meant it.</p>
      <p class="hint">Your attempt is not saved to your tracker until you press Save my marks.</p></section>
      ${r.written.map((w, i) => `<section class="card block q" data-w="${w.id}"><div class="row"><b>Written question ${i + 1}</b><span class="score"><small class="wtot">0 / ${w.marks}</small></span></div>
        ${ctx(w)}<p class="qtext">${esc(w.q)}</p>
        <p><span class="hint">Your answer</span></p><div class="yours">${w.typed ? para(w.typed) : "<p><i>No answer</i></p>"}</div>
        <p class="hint" style="margin-top:12px">Mark points (tick those you made, up to ${marksWord(w.marks)})</p>
        <div class="pts">${w.points.map((p, k) => `<label class="opt"><input type="checkbox" data-k="${k}"> <span>${esc(p.t)} <span class="hint">(${p.m} mark${p.m === 1 ? "" : "s"})</span></span></label>`).join("")}</div>
        <details class="model"><summary>Model answer</summary>${para(w.model || "")}</details>
        ${w.tips ? `<p class="fb">${esc(w.tips)}</p>` : ""}</section>`).join("")}
      <details class="card block"><summary><b>Review your multiple choice answers</b></summary>${mcqCards(r.mcq)}</details>
      <section class="card block"><p class="msg err" hidden></p><button class="btn" id="save">Save my marks</button></section>`;
    root.querySelectorAll("[data-w]").forEach((sec) => {
      const w = r.written.find((x) => x.id === sec.dataset.w);
      sec.addEventListener("change", (e) => {
        const k = +e.target.dataset.k;
        e.target.checked ? ticks[w.id].add(k) : ticks[w.id].delete(k);
        $(".wtot", sec).textContent = `${sum(w)} / ${w.marks}`;
      });
    });
    $("#save").onclick = async (e) => {
      const m = $(".msg", e.target.parentElement), payload = Object.fromEntries(Object.entries(ticks).map(([k, v]) => [k, [...v]]));
      e.target.disabled = true;
      const { data, error } = await S.sb.rpc("finalize_topic_test", { _attempt: r.attempt, _ticks: payload });
      if (error) { e.target.disabled = false; m.textContent = error.message; m.hidden = false; return; }
      viewResult(r, data, payload);
      window.scrollTo(0, 0);
    };
  }

  function advice(r, res, ticks) {
    const weak = new Set();
    r.mcq.filter((i) => i.got < i.max && i.topic).forEach((i) => weak.add(i.topic));
    r.written.forEach((w) => {
      const got = Math.min(w.marks, (ticks[w.id] || []).reduce((t, k) => t + (w.points[k]?.m || 1), 0));
      if (w.topic && got < w.marks * 0.6) weak.add(w.topic);
    });
    const band = res.pct >= 80 ? "A strong result. Keep it fresh by revisiting this topic before it comes up again."
      : res.pct >= 50 ? "A solid base with gaps. Revise the points below, then retake the test to see the difference."
      : "This topic needs more work. Go back through the chapter, then try the test again.";
    return `<p>${band}</p>${weak.size ? `<p><b>Focus on:</b> ${[...weak].map((t) => `<span class="pill soft">${esc(t)}</span>`).join(" ")}</p>` : ""}`;
  }

  function viewResult(r, res, ticks) {
    root.innerHTML = `<section class="card block result ${res.pct >= 50 ? "pass" : "fail"}">
      <div class="row"><h3>${esc(r.title || "Topic test")}</h3><span class="big">${res.pct}%</span></div>
      <p><b>${res.score} / ${res.max} marks.</b> Multiple choice ${res.mcq} / ${res.mcq_max}, written ${res.written} / ${res.written_max}.</p>
      ${advice(r, res, ticks)}
      <p class="hint">Saved to your tracker. Your earlier attempts are still there, so retaking shows how far you have come.</p>
      <p><a class="btn" href="${S.base}tests/?t=${encodeURIComponent(id)}">Retake the test</a> <a class="btn ghost" href="${trackerUrl()}">My test tracker</a> <a class="btn ghost" href="${chapterUrl()}">Back to the chapter</a></p></section>
      ${mcqCards(r.mcq)}`;
  }

  async function boot() {
    if (!id) { root.innerHTML = `<p class="msg err">No test chosen.</p>`; return; }
    me = await S.whoami();
    if (!me) {
      try { sessionStorage.setItem("site.next", location.href); } catch (e) {}
      root.innerHTML = `<section class="card block"><h3>Sign in to take the test</h3><p><a class="btn" href="${S.profileUrl}">Sign in</a></p></section>`;
      return;
    }
    const { data, error } = await S.sb.rpc("get_topic_test", { _id: id });
    if (error || !data) { root.innerHTML = `<p class="msg err">${error ? esc(error.message) : "There is no topic test for this chapter yet."}</p>`; return; }
    if (data.locked) {
      root.innerHTML = `<section class="card block"><h3>Topic tests are part of the Full plan</h3>
        <p class="hint">Your access to this subject does not include the server-marked tests and the progress tracker. Upgrade to Full to take them.</p>
        <p><a class="btn" href="${S.base}pricing/">See plans</a> <a class="btn ghost" href="${chapterUrl()}">Back to the chapter</a></p></section>`;
      return;
    }
    quiz = data;
    viewIntro();
  }
  if (S && S.configured) boot();
})();
