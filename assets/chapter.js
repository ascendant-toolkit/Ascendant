// Chapter page: Review / Resources tabs. Cards start where site_data.py puts them; admin overrides
// from the artifact_roles table (and the admin toggle) move them between tabs.
(function () {
  const tabs = [...document.querySelectorAll(".chtabs button")];
  const panels = [...document.querySelectorAll("[data-p]")];
  const cards = [...document.querySelectorAll(".card.art")];
  if (!tabs.length) return;  // the access gate replaced the page
  const el = (t) => document.querySelector(`[data-p="${t}"]`);

  function show(t) {
    tabs.forEach((b) => b.classList.toggle("on", b.dataset.t === t));
    panels.forEach((p) => (p.hidden = p.dataset.p !== t));
    try { history.replaceState(null, "", "#" + t); } catch (e) {}
  }
  tabs.forEach((b) => (b.onclick = () => show(b.dataset.t)));
  const want = location.hash === "#res" ? "res" : location.hash === "#rev" ? "rev" : null;
  if (want) show(want);

  function place(c, role) {
    const t = role === "review" ? "rev" : role === "hidden" ? "del" : "res", grid = el(t).querySelector(".grid");
    c.dataset.role = role;
    const after = [...grid.children].find((x) => +x.dataset.ord > +c.dataset.ord);
    grid.insertBefore(c, after || null);
    const btn = c.querySelector("[data-done-slug]");
    if (btn) btn.hidden = role !== "review" || !btn.dataset.bound;
    if (btn && role === "review" && window.Site) Site.bindButtons();
  }

  function refresh() {
    ["rev", "res", "del"].forEach((t, i) => {
      const n = el(t).querySelectorAll(".card.art").length;
      tabs[i].querySelector("span").textContent = n;
      const m = el(t).querySelector(".emptymsg");
      if (m) m.hidden = n > 0;
      if (t === "del") tabs[i].hidden = !(n > 0 && window.Site && Site.me && Site.me.is_admin);
    });
    // If the open tab emptied out, switch to the other one.
    const open = panels.find((p) => !p.hidden);
    if (open && !open.querySelector(".card.art")) {
      const other = panels.find((p) => p !== open && p.querySelector(".card.art"));
      if (other) show(other.dataset.p);
    }
  }

  document.addEventListener("site:rolechange", (e) => {
    const c = cards.find((x) => x.dataset.slug === e.detail.slug);
    if (c) { place(c, e.detail.role); refresh(); }
  });

  // Apply saved overrides on load.
  (async function () {
    if (!window.Site || !Site.configured) return;
    const cat = await Site.catalog();
    await Site.whoami();
    cards.forEach((c) => {
      const r = cat.roles[c.dataset.slug];
      if (r && r !== c.dataset.role) place(c, r);
    });
    refresh();
  })();
})();

// Topic test block. Students see their best score; teachers get the mark scheme and, on a licence, how their students did.
(async function () {
  const block = document.querySelector(".ttest");
  if (!block || !window.Site || !Site.configured) return;
  try {
    const me = await Site.whoami();
    if (!me) return;
    const box = block.querySelector(".ttscore"), id = block.dataset.test;
    if (me.is_admin || me.is_teacher || me.is_school_teacher) {
      const btn = block.querySelector("a.btn");
      btn.textContent = "View test and mark scheme";
      block.querySelector("p.hint").textContent = "The full paper with the answer key, mark points and model answers. You can print it as a mark scheme or as a student copy.";
      if (me.is_school_teacher) {
        const { data } = await Site.sb.rpc("school_test_attempts");
        const mine = (data || []).filter((r) => r.test === id);
        if (mine.length) {
          const who = new Set(mine.map((r) => r.email)).size, avg = Math.round(mine.reduce((t, r) => t + r.pct, 0) / mine.length);
          box.textContent = `${who} student${who === 1 ? "" : "s"} taken it · ${mine.length} attempt${mine.length === 1 ? "" : "s"} · average ${avg}%`;
        } else box.textContent = "No attempts from your students yet.";
      }
      return;
    }
    const { data } = await Site.sb.rpc("my_test_attempts");
    const mine = (data || []).filter((r) => r.test === id);
    if (mine.length) box.textContent = `Best ${Math.max(...mine.map((r) => r.pct))}% · ${mine.length} attempt${mine.length === 1 ? "" : "s"}`;
  } catch (e) {}
})();
