// Home page: signed-in students see only their subjects; visitors see everything available plus a sample lesson.
// Also drives the optional /welcome/ landing page (member swap and join list form).
(function () {
  const S = window.Site;
  const $ = (s) => document.querySelector(s);

  async function members() {
    if (!S || !S.configured) return;
    const me = await S.whoami();
    const cards = document.querySelectorAll("[data-home-course]");
    if (!me) {
      $("#homehint") && ($("#homehint").hidden = false);
      $("#sample") && ($("#sample").hidden = false);
      return;
    }
    const bar = $("#memberbar");
    if (bar) {
      bar.hidden = false;
      if (me.is_admin || me.is_teacher || me.is_school_teacher) { $("#memberlink").href = S.profileUrl; $("#memberlink").textContent = "Open your profile →"; }
    }
    if (!me.is_admin) cards.forEach((a) => { a.hidden = !me.subjects.includes(a.dataset.homeCourse); });
    if ($("#pitch")) {
      $("#pitch").hidden = true;
      $("#mine").hidden = false;
      if (me.is_admin) document.querySelectorAll("#mine [data-course]").forEach((a) => { a.hidden = false; });
    }
  }

  const form = $("#joinform");
  if (form) form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const msg = $("#joinmsg"), btn = form.querySelector("button");
    const say = (t, ok) => { msg.hidden = false; msg.textContent = t; msg.className = "msg " + (ok ? "ok" : "err"); };
    const f = new FormData(form);
    const email = String(f.get("email") || "").trim();
    const subjects = f.getAll("subjects");
    if (!form.checkValidity() || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return say("Please add your name and a valid email, and tick the consent box.", false);
    if (!subjects.length) return say("Choose at least one subject.", false);
    if (!S || !S.sb) return say("Sign-up is not available right now. Please try again later.", false);
    btn.disabled = true;
    const { error } = await S.sb.from("waitlist").insert({ email, name: String(f.get("name")).trim(), role: f.get("role"), subjects });
    btn.disabled = false;
    if (error && error.code === "23505") return say("You are already on the list. I will be in touch.", true);
    if (error) return say("That did not go through. Please try again.", false);
    form.reset();
    say("Thanks, you are on the list. You will get an email when your access is ready.", true);
  });

  members();
})();
