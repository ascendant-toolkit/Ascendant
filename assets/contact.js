// Contact form: stores the message in contact_messages (admins read it in Supabase). ?topic= preselects the topic.
(function () {
  const S = window.Site, form = document.getElementById("contactform");
  if (!form) return;
  const msg = document.getElementById("contactmsg");
  const say = (t, ok) => { msg.hidden = false; msg.textContent = t; msg.className = "msg " + (ok ? "ok" : "err"); };
  const pre = new URLSearchParams(location.search).get("topic");
  if (pre && form.topic.querySelector(`option[value="${pre}"]`)) form.topic.value = pre;
  const kind = new URLSearchParams(location.search).get("role");
  if (kind && form.role.querySelector(`option[value="${kind}"]`)) form.role.value = kind;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = new FormData(form), email = String(f.get("email") || "").trim();
    if (f.get("website")) return say("Thanks, your message has been sent.", true);  // honeypot
    if (!form.checkValidity() || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return say("Please add your name, a valid email and a message.", false);
    if (!S || !S.sb) return say("Messages are not available right now. Please try again later.", false);
    const btn = form.querySelector("button");
    btn.disabled = true;
    const { error } = await S.sb.from("contact_messages").insert({
      name: String(f.get("name")).trim(), email, role: f.get("role"), org: String(f.get("org") || "").trim() || null,
      topic: f.get("topic"), message: String(f.get("message")).trim(),
    });
    btn.disabled = false;
    if (error) return say("That did not go through. Please try again.", false);
    form.reset();
    say("Thanks, your message has been sent. We will reply by email.", true);
  });
})();
