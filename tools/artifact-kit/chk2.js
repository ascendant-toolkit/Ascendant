/* Paste into the browser console (or run via the browser tool) on a page. Shows every tab, steps every stepper to every step, and flags
   SVG text that overlaps other text, crosses a visible line, or runs off the canvas. Faded things (opacity <= 0.5) are ignored.
   Returns JSON {issues:[...], svgs:n} in window.__chk. Set window.__chkScope to a selector to limit the check to one part of the page
   (for a lab that rebuilds its diagram, set the lab to each value and run once per value). */
window.__chk = null; (async () => {
  document.querySelectorAll('[role=tabpanel]').forEach((p) => (p.hidden = false));
  const root = document.querySelector(window.__chkScope || "body");
  const issues = [], seen = new Set();
  const op = (el) => { let o = 1; for (let e = el; e && e.tagName !== "svg"; e = e.parentNode) { const v = e.getAttribute && (e.style && e.style.opacity !== "" ? e.style.opacity : e.getAttribute("opacity")); if (v !== null && v !== undefined && v !== "") o *= +v; } return o; };
  const hit = (cov, b, l, x1, y1, x2, y2) => { const n = Math.max(2, Math.ceil(Math.hypot(x2 - x1, y2 - y1) / 2)); for (let i = 0; i <= n; i++) { const x = x1 + ((x2 - x1) * i) / n, y = y1 + ((y2 - y1) * i) / n; if (x > b.x + 1.5 && x < b.x + b.width - 1.5 && y > b.y + 2 && y < b.y + b.height - 2 && !cov(l, x, y)) return true; } return false; };
  const check = (sv, name) => {
    const vb = sv.viewBox.baseVal, ts = [...sv.querySelectorAll("text")].filter((t) => t.textContent.trim() && op(t) > 0.15).map((t) => ({ t: t.textContent.trim(), b: t.getBBox() }));
    const shapes = [...sv.querySelectorAll("circle,rect")].filter((e) => op(e) > 0.95 && getComputedStyle(e).fill !== "none" && !/^rgba\(.*, 0\)$/.test(getComputedStyle(e).fill));
    const ls = [...sv.querySelectorAll("line")].filter((l) => op(l) > 0.5).map((l) => ({ l, c: ["x1", "y1", "x2", "y2"].map((a) => +l.getAttribute(a)) }));
    const covered = (l, x, y) => shapes.some((e) => (l.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) && (e.tagName === "circle" ? Math.hypot(x - +e.getAttribute("cx"), y - +e.getAttribute("cy")) < +e.getAttribute("r") : x > +e.getAttribute("x") && x < +e.getAttribute("x") + +e.getAttribute("width") && y > +e.getAttribute("y") && y < +e.getAttribute("y") + +e.getAttribute("height")));
    const add = (m) => { if (!seen.has(m)) { seen.add(m); issues.push(m); } };
    ts.forEach((o, i) => {
      const A = o.b;
      for (let j = i + 1; j < ts.length; j++) { const B = ts[j].b; if (A.x < B.x + B.width - 1 && B.x < A.x + A.width - 1 && A.y < B.y + B.height - 2 && B.y < A.y + A.height - 2) add(`${name}: text "${o.t.slice(0, 24)}" overlaps text "${ts[j].t.slice(0, 24)}"`); }
      ls.forEach((o2) => { if (hit(covered, A, o2.l, ...o2.c)) add(`${name}: text "${o.t.slice(0, 24)}" crossed by a line`); });
      const cx = A.x + A.width / 2, cy = A.y + A.height / 2, rc = shapes.filter((e) => e.tagName === "rect" && cx > +e.getAttribute("x") && cx < +e.getAttribute("x") + +e.getAttribute("width") && cy > +e.getAttribute("y") && cy < +e.getAttribute("y") + +e.getAttribute("height")).sort((p, q) => +p.getAttribute("width") - +q.getAttribute("width"))[0];
      if (rc && (A.x < +rc.getAttribute("x") - 1 || A.x + A.width > +rc.getAttribute("x") + +rc.getAttribute("width") + 1)) add(`${name}: text "${o.t.slice(0, 24)}" runs outside its box`);
      if (A.x < -2 || A.x + A.width > vb.width + 2 || A.y < 0 || A.y + A.height > vb.height + 2) add(`${name}: text "${o.t.slice(0, 24)}" off the canvas`);
    });
  };
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  for (const st of root.querySelectorAll(".stp")) {
    const sv = st.querySelector("svg"), dots = [...st.querySelectorAll(".stp-dots button")], name = (st.parentElement.id || st.id || "stepper");
    for (let i = 0; i < dots.length; i++) { dots[i].click(); await wait(120); check(sv, `${name} step ${i + 1}`); }
  }
  const stepSvgs = new Set([...document.querySelectorAll(".stp svg")]);
  [...root.querySelectorAll("svg")].filter((s) => !stepSvgs.has(s) && s.viewBox.baseVal && s.viewBox.baseVal.width).forEach((s, k) => check(s, (s.closest("[id]") || {}).id || "svg" + k));
  window.__chk = JSON.stringify({ issues, svgs: document.querySelectorAll("svg").length });
})();
