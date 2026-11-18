// Launch-updates sign-up: adds an email to the waitlist table. Duplicates are treated as success.
(function () {
  const S = window.Site;
  document.querySelectorAll(".notifyform").forEach((form) => {
    const msg = form.querySelector(".msg");
    const say = (t, ok) => { msg.hidden = false; msg.textContent = t; msg.className = "msg " + (ok ? "ok" : "err"); };
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = new FormData(form);
      const email = String(f.get("email") || "").trim();
      if (f.get("website")) return say("Thanks, you are on the list.", true); // honeypot: quietly ignore bots
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || !f.get("consent")) return say("Please add a valid email and tick the box.", false);
      if (!S || !S.sb) return say("Sign-up is not available right now. Please try again later.", false);
      const btn = form.querySelector("button"); btn.disabled = true;
      const { error } = await S.sb.from("waitlist").insert({ email, role: f.get("role") || null });
      btn.disabled = false;
      if (error && error.code !== "23505") return say("That did not go through. Please try again.", false);
      form.reset();
      say("Thanks, you are on the list. We will email you when paid plans open.", true);
    });
  });
})();
