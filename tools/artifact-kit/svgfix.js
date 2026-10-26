/* Runs on every published page (build.py injects it). Keeps SVG diagram labels readable whatever the page's own drawing code did:
   1. text wider than the box it sits in shrinks to fit the box (down to 50%)
   2. text that overlaps other text is nudged down until the overlap is gone
   3. text crossed by a visible line gets a background-coloured halo
   4. text outside the canvas grows the viewBox so nothing is cut off
   Works on steppers (re-runs after every repaint), labs and static diagrams. tools/artifact-kit/chk2.js is the matching checker. */
(() => {
  const op = (el) => { let o = 1; for (let e = el; e && e.tagName !== "svg"; e = e.parentNode) { const v = e.getAttribute && (e.style && e.style.opacity !== "" ? e.style.opacity : e.getAttribute("opacity")); if (v !== null && v !== undefined && v !== "") o *= +v; } return o; };
  const num = (e, a) => +e.getAttribute(a);
  function crossed(b, ls, cov) {
    return ls.some((l) => { const [x1, y1, x2, y2] = l.c, n = Math.max(2, Math.ceil(Math.hypot(x2 - x1, y2 - y1) / 2)); for (let i = 0; i <= n; i++) { const x = x1 + ((x2 - x1) * i) / n, y = y1 + ((y2 - y1) * i) / n; if (x > b.x + 1.5 && x < b.x + b.width - 1.5 && y > b.y + 2 && y < b.y + b.height - 2 && !cov(l.l, x, y)) return true; } return false; });
  }
  function fix(sv) {
    const vb = sv.viewBox && sv.viewBox.baseVal;
    if (!vb || !vb.width || !sv.getClientRects().length) return;
    const all = [...sv.querySelectorAll("text")].filter((t) => t.textContent.trim() && op(t) > 0.15 && !t.closest("[transform]") && !t.getAttribute("transform"));
    if (!all.length) return;
    const shapes = [...sv.querySelectorAll("circle,rect")].filter((e) => op(e) > 0.95 && getComputedStyle(e).fill !== "none" && !/^rgba\(.*, 0\)$/.test(getComputedStyle(e).fill));
    const box = (e) => (e.tagName === "circle" ? { x: num(e, "cx") - num(e, "r"), y: num(e, "cy") - num(e, "r"), w: 2 * num(e, "r"), h: 2 * num(e, "r") } : { x: num(e, "x"), y: num(e, "y"), w: num(e, "width"), h: num(e, "height") });
    // 1. fit text inside its box
    all.forEach((t) => {
      if (t.dataset.fx) return;
      let b = t.getBBox(); const cx = b.x + b.width / 2, cy = b.y + b.height / 2;
      const rc = shapes.filter((e) => e.tagName === "rect" && (e.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_FOLLOWING)).map(box).filter((r) => cx > r.x && cx < r.x + r.w && cy > r.y && cy < r.y + r.h).sort((p, q) => p.w - q.w)[0];
      if (rc && rc.w > 20 && (b.x < rc.x + 1 || b.x + b.width > rc.x + rc.w - 1)) {
        const fs = parseFloat(getComputedStyle(t).fontSize) || 12, k = Math.max(0.5, (rc.w - 8) / b.width);
        if (k < 1) { t.style.fontSize = (fs * k).toFixed(2) + "px"; t.dataset.fx = "1"; }
      }
    });
    // 2. separate overlapping text
    for (let pass = 0; pass < 4; pass++) {
      const bb = all.map((t) => t.getBBox()); let moved = false;
      for (let i = 0; i < all.length; i++) for (let j = i + 1; j < all.length; j++) {
        const A = bb[i], B = bb[j];
        if (A.x < B.x + B.width - 1 && B.x < A.x + A.width - 1 && A.y < B.y + B.height - 2 && B.y < A.y + A.height - 2) {
          const dy = Math.min(A.y + A.height - B.y + 1, 18);
          all[j].setAttribute("y", (parseFloat(all[j].getAttribute("y")) || 0) + dy); bb[j] = all[j].getBBox(); moved = true;
        }
      }
      if (!moved) break;
    }
    // 3. halo for text crossed by a visible line
    const ls = [...sv.querySelectorAll("line")].filter((l) => op(l) > 0.5).map((l) => ({ l, c: ["x1", "y1", "x2", "y2"].map((a) => num(l, a)) }));
    const cov = (l, x, y) => shapes.some((e) => (l.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) && (() => { const r = box(e); return e.tagName === "circle" ? Math.hypot(x - num(e, "cx"), y - num(e, "cy")) < num(e, "r") : x > r.x && x < r.x + r.w && y > r.y && y < r.y + r.h; })());
    all.forEach((t) => { if (crossed(t.getBBox(), ls, cov)) { t.style.paintOrder = "stroke"; t.style.stroke = "var(--surface, #fff)"; t.style.strokeWidth = "4px"; t.style.strokeLinejoin = "round"; } });
    // 4. grow the canvas so nothing is cut off
    let x0 = vb.x, y0 = vb.y, x1 = vb.x + vb.width, y1 = vb.y + vb.height;
    all.forEach((t) => { const b = t.getBBox(); x0 = Math.min(x0, b.x - 4); y0 = Math.min(y0, b.y - 4); x1 = Math.max(x1, b.x + b.width + 4); y1 = Math.max(y1, b.y + b.height + 4); });
    if (x0 < vb.x - 0.5 || y0 < vb.y - 0.5 || x1 > vb.x + vb.width + 0.5 || y1 > vb.y + vb.height + 0.5) sv.setAttribute("viewBox", `${x0} ${y0} ${x1 - x0} ${y1 - y0}`);
  }
  let queued = false;
  const run = () => { queued = false; document.querySelectorAll("svg").forEach((sv) => { try { fix(sv); } catch (e) {} }); };
  const queue = () => { if (!queued) { queued = true; requestAnimationFrame(() => setTimeout(run, 30)); } };
  const mo = new MutationObserver((ms) => { if (ms.some((m) => m.target.closest && m.target.closest("svg"))) queue(); });
  const start = () => { mo.observe(document.body, { childList: true, subtree: true }); window.addEventListener("resize", queue); window.addEventListener("load", queue); queue(); };
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", start) : start();
  window.__svgfix = run;
})();
