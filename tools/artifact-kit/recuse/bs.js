/* ===== Recursive binary search ===== */
const ARR = [3, 8, 12, 17, 21, 26, 34, 40, 47, 55, 63];
const PS = ["FUNCTION RecursiveBinarySearch(DataArray, Lower, Upper, DataToFind) RETURNS INTEGER", "   IF Upper >= Lower THEN", "      Middle ← Lower + (Upper - Lower) DIV 2", "      IF DataArray[Middle] = DataToFind THEN", "         RETURN Middle", "      ELSEIF DataArray[Middle] > DataToFind THEN", "         RETURN RecursiveBinarySearch(DataArray, Lower, Middle - 1, DataToFind)", "      ELSE", "         RETURN RecursiveBinarySearch(DataArray, Middle + 1, Upper, DataToFind)", "      ENDIF", "   ELSE", "      RETURN -1", "   ENDIF", "ENDFUNCTION"];
const PY = ["def recursive_binary_search(data_array, lower, upper, data_to_find):", "    if upper >= lower:", "        middle = lower + (upper - lower) // 2", "        if data_array[middle] == data_to_find:", "            return middle", "        elif data_array[middle] > data_to_find:", "            return recursive_binary_search(data_array, lower, middle - 1, data_to_find)", "        else:", "            return recursive_binary_search(data_array, middle + 1, upper, data_to_find)", "    else:", "        return -1"];
const CODE = { ps: PS, py: PY };
Lib.codePanel($("#codeB"), { pseudo: PS, py: PY });

/* the search as a list of calls */
function bsCalls(target, arr = ARR) {
  const calls = []; let lo = 0, up = arr.length - 1;
  for (;;) {
    const c = { lo, up };
    if (up < lo) { c.res = -1; calls.push(c); break; }
    c.mid = lo + Math.floor((up - lo) / 2); c.v = arr[c.mid];
    if (c.v === target) { c.res = c.mid; calls.push(c); break; }
    c.dir = c.v > target ? "low" : "high";
    calls.push(c);
    if (c.dir === "low") up = c.mid - 1; else lo = c.mid + 1;
  }
  return calls;
}

/* array drawing: the live range is bright, the rest faded */
function arrSvg(arr, st, hist) {
  const W = 720, n = arr.length, cw = Math.min(58, (W - 40) / n), x0 = (W - n * cw) / 2, y = 40, ch = 40;
  const cx = (i) => x0 + (Math.max(-0.5, Math.min(n - 0.5, i)) + 0.5) * cw;
  let g = "";
  for (let i = 0; i < n; i++) {
    const live = st.lo !== undefined && i >= st.lo && i <= st.up, isMid = i === st.mid, ok = st.found === i;
    const cls = ok ? "cell cell-ok" : isMid ? "cell cell-cur" : "cell";
    g += SV.rect(x0 + i * cw + 1, y, cw - 2, ch, cls, { rx: 6, style: live || st.lo === undefined ? "" : "opacity:.28" });
    g += SV.text(x0 + (i + 0.5) * cw, y + 26, arr[i], "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:14px" + (live || st.lo === undefined ? "" : ";opacity:.35") });
    g += SV.text(x0 + (i + 0.5) * cw, y - 8, i, "sm", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  }
  if (st.lo !== undefined) {
    const mk = (i, t, row, c) => SV.text(cx(i), y + ch + 18 + row * 15, t, "sm bd " + c, { "text-anchor": "middle" });
    g += mk(st.lo, "▲ Lower", 0, "t1");
    if (st.mid !== undefined) g += mk(st.mid, "▲ Middle", 1, "t2");
    g += mk(st.up, "▲ Upper", 2, "t3");
    if (st.up < st.lo) g += SV.text(W / 2, y + ch + 78, "Upper is below Lower: no items left to search", "lbl bd t2", { "text-anchor": "middle" });
  }
  hist.forEach((h, k) => { g += SV.text(24, 172 + k * 21, h, "sm", { "text-anchor": "start", style: "font-family:var(--mono);font-size:14.5px" }); });
  return g;
}

function bsFrames(target, arr = ARR) {
  const calls = bsCalls(target, arr), fr = [], hist = [];
  const call0 = `RecursiveBinarySearch(DataArray, 0, ${arr.length - 1}, ${target})`;
  fr.push({ cap: `Looking for <b>${target}</b> in a sorted array of ${arr.length} values (indexes 0 to ${arr.length - 1}). The first call is <b>${call0}</b>. Press Next.`, ps: [0], py: [0], svg: arrSvg(arr, {}, []) });
  calls.forEach((c, k) => {
    const no = k + 1, head = `Call ${no}: Lower ${c.lo}, Upper ${c.up}`;
    fr.push({ cap: `<b>Call ${no}.</b> Lower = ${c.lo}, Upper = ${c.up}. Is Upper &gt;= Lower? ${c.up >= c.lo ? "<b>Yes</b>: there is at least one item left to look at." : "<b>No</b>: the range is empty."}`, ps: [1], py: [1], svg: arrSvg(arr, { lo: c.lo, up: c.up }, [...hist]) });
    if (c.up < c.lo) { hist.push(head + " → empty → returns -1"); fr.push({ cap: `Upper &lt; Lower, so the <b>not found</b> base case: RETURN −1. The −1 is passed back up through ${k} waiting call${k === 1 ? "" : "s"}, unchanged.`, ps: [1, 10, 11], py: [1, 9, 10], svg: arrSvg(arr, { lo: c.lo, up: c.up }, [...hist]) }); return; }
    fr.push({ cap: `Middle = ${c.lo} + (${c.up} − ${c.lo}) DIV 2 = <b>${c.mid}</b>. DataArray[${c.mid}] is <b>${c.v}</b>.`, ps: [2], py: [2], svg: arrSvg(arr, { lo: c.lo, up: c.up, mid: c.mid }, [...hist]) });
    if (c.res !== undefined) { hist.push(`${head}, Middle ${c.mid} → ${c.v} = ${target} → returns ${c.mid}`); fr.push({ cap: `${c.v} = ${target}: <b>found</b>. RETURN ${c.mid}. The ${c.mid} is passed back up through ${k} waiting call${k === 1 ? "" : "s"}, unchanged. The answer is index <b>${c.mid}</b>.`, ps: [3, 4], py: [3, 4], svg: arrSvg(arr, { lo: c.lo, up: c.up, mid: c.mid, found: c.mid }, [...hist]) }); return; }
    const low = c.dir === "low";
    hist.push(`${head}, Middle ${c.mid} → ${c.v} ${low ? ">" : "<"} ${target} → search ${low ? `${c.lo}..${c.mid - 1}` : `${c.mid + 1}..${c.up}`}`);
    fr.push({ cap: `${c.v} is ${low ? "greater" : "less"} than ${target}, so the value can only be in the ${low ? "lower" : "upper"} half. The next call searches <b>${low ? `${c.lo} to ${c.mid - 1}` : `${c.mid + 1} to ${c.up}`}</b>. The middle itself is left out, because it has been checked.`, ps: low ? [5, 6] : [7, 8], py: low ? [5, 6] : [7, 8], svg: arrSvg(arr, { lo: c.lo, up: c.up, mid: c.mid }, [...hist]) });
  });
  return fr;
}
const arrAlgo = (sel, target, label) => Lib.algo($(sel), { w: 720, h: 270, label, pseudo: PS, py: PY, dwell: 3000, frames: bsFrames(target) });
arrAlgo("#aFound", 40, "Binary search for 40 in a sorted array");
arrAlgo("#aMiss", 30, "Binary search for 30, which is not in the array");

/* stack and tree for the search for 40 */
(() => {
  const T = Trace({ treeName: "Lower..Upper", outTitle: "Values returned", maxDepth: 5 }), target = 40, calls = bsCalls(target);
  let parent = null; const nds = [];
  calls.forEach((c, k) => {
    const nd = T.call(`Search(${c.lo}, ${c.up})`, `${c.lo}-${c.up}`, parent, k ? `line ${calls[k - 1].dir === "low" ? 7 : 9}` : "main", `<b>Call ${k + 1}: Lower = ${c.lo}, Upper = ${c.up}.</b> A new frame is pushed.`, [0], [0]);
    nds.push(nd); parent = nd;
    T.note(nd, `Middle = ${c.mid}: ${c.v}`, `Middle = ${c.mid}, DataArray[${c.mid}] = ${c.v}. ${c.res !== undefined ? "Equal to 40: <b>found</b>." : `${c.v} ${c.dir === "low" ? ">" : "<"} 40, so search the ${c.dir === "low" ? "lower" : "upper"} half.`}`, [2, 3], [2, 3], c.res !== undefined ? "base" : "run");
    if (c.res === undefined) { T.setStatus(nd, "paused: waiting for the smaller search"); }
  });
  for (let k = calls.length - 1; k >= 0; k--) {
    const r = calls[calls.length - 1].res;
    T.ret(nds[k], String(r), k === calls.length - 1 ? `RETURN Middle sends <b>${r}</b> back to the waiting call. The frame is popped and <b>unwinding starts</b>.` : `This call just passes <b>${r}</b> up: nothing is added or changed on the way back.`, k === calls.length - 1 ? [4] : [up(calls[k])], k === calls.length - 1 ? [4] : [up(calls[k])]);
  }
  function up(c) { return c.dir === "low" ? 6 : 8; }
  T.finish(`The stack is empty. The search for 40 returned <b>7</b> after only ${calls.length} calls, from an array of 11 values.`, [], []);
  showAlgo("#aStack", T, CODE, "Animated call stack and call tree for the search for 40", 2600);
})();

/* ===== Explore ===== */
(() => {
  const sel = $("#bsT");
  sel.innerHTML = ARR.map((v) => `<option value="${v}">${v}</option>`).join("") + [1, 30, 50, 70].map((v) => `<option value="${v}">${v} (missing)</option>`).join("");
  sel.value = 40;
  const go = () => {
    const t = +sel.value, calls = bsCalls(t), last = calls[calls.length - 1];
    $("#bsRO").innerHTML = `<div><small>Searching for</small><strong>${t}</strong></div><div><small>Calls made</small><strong>${calls.length}</strong></div><div><small>Returned</small><strong>${last.res}</strong></div><div><small>Linear search would check</small><strong>${last.res < 0 ? ARR.length : last.res + 1}</strong></div>`;
    arrAlgo("#bsAlgo", t, `Binary search for ${t}`);
  };
  sel.addEventListener("change", go); go();

  let S2;
  const draw2 = () => {
    if (!S2) return;
    const k = S2.get(), n = 2 ** k - 1;
    $("#bsRO2").innerHTML = `<div><small>Items in the array</small><strong>${n.toLocaleString()}</strong></div><div><small>Most calls: binary search</small><strong>${k}</strong></div><div><small>Most checks: linear search</small><strong>${n.toLocaleString()}</strong></div><div><small>Binary does it in</small><strong>${((k / n) * 100).toFixed(k > 7 ? 2 : 0)}%</strong></div>`;
    const w1 = Math.max(0.8, (k / n) * 100);
    $("#bsBars").innerHTML = `<div style="display:flex;gap:10px;align-items:center;margin:3px 0"><span style="font:600 .85rem var(--sans);width:70px">Binary</span><div style="flex:1;background:var(--soft);border-radius:4px"><div style="width:${w1}%;height:14px;border-radius:4px;background:var(--accent)"></div></div><b style="font:700 .85rem var(--mono);width:80px;text-align:right">${k}</b></div><div style="display:flex;gap:10px;align-items:center;margin:3px 0"><span style="font:600 .85rem var(--sans);width:70px">Linear</span><div style="flex:1;background:var(--soft);border-radius:4px"><div style="width:100%;height:14px;border-radius:4px;background:var(--warn)"></div></div><b style="font:700 .85rem var(--mono);width:80px;text-align:right">${n.toLocaleString()}</b></div>`;
  };
  S2 = Lib.slider($("#bsK"), { id: "bsk", label: "k (items = 2^k − 1): ", min: 1, max: 20, value: 1, onInput: draw2 });
  draw2();
})();

/* ===== Activities ===== */
Lib.order($("#o1"), { prompt: "Binary search for 40. Put the events in the order they happen.", items: ["Call 1 (Lower 0, Upper 10): Middle = 5, DataArray[5] = 26", "26 is less than 40, so Lower becomes Middle + 1 = 6", "Call 2 (Lower 6, Upper 10): Middle = 8, DataArray[8] = 47", "47 is greater than 40, so Upper becomes Middle − 1 = 7", "Call 3 (Lower 6, Upper 7): Middle = 6, DataArray[6] = 34, so Lower becomes 7", "Call 4 (Lower 7, Upper 7): Middle = 7, DataArray[7] = 40: found, returns 7", "The 7 is passed back up through calls 3, 2 and 1"], done: "The range halves each time, until the value is found or the range is empty." });

Lib.classify($("#cl1"), { prompt: "Drag each piece of the function to the part of recursion it plays.", buckets: [{ label: "Base case" }, { label: "General case (calls itself)" }, { label: "Moves towards the base case" }], items: [
  { text: "RETURN Middle when DataArray[Middle] = DataToFind", b: 0 }, { text: "RETURN -1 when Upper < Lower", b: 0 }, { text: "RETURN RecursiveBinarySearch(… Lower, Middle - 1 …)", b: 1 }, { text: "RETURN RecursiveBinarySearch(… Middle + 1, Upper …)", b: 1 }, { text: "Middle - 1 as the new upper bound", b: 2 }, { text: "Middle + 1 as the new lower bound", b: 2 }], done: "Every call makes the range smaller, so one of the base cases must be reached." });

Lib.classify($("#cl2"), { prompt: "Which search is each statement true of?", buckets: [{ label: "Binary search" }, { label: "Linear search" }, { label: "Both" }], items: [
  { text: "Needs the data to be sorted", b: 0 }, { text: "Works on unsorted data", b: 1 }, { text: "Rules out half of the remaining items with each comparison", b: 0 }, { text: "Needs about log₂ n checks for n items, at most", b: 0 }, { text: "May have to check every item", b: 1 }, { text: "Returns the position of the item, or a value meaning not found", b: 2 }], done: "Binary search is far quicker, but only on sorted data." });

Lib.match($("#m1"), { prompt: "Match each term to what it means for binary search.", pairs: [
  ["Lower", "the index of the first item still being searched"], ["Upper", "the index of the last item still being searched"], ["Middle", "Lower + (Upper − Lower) DIV 2: the item checked next"], ["Base case", "found, or no items left (Upper < Lower)"], ["Halving", "each call discards about half of the remaining items"], ["Sorted", "the pre-condition that makes the method work"]], done: "These six ideas are everything the function relies on." });

/* ===== Practise ===== */
Lib.calc($("#c1"), { qs: [
  { q: "RecursiveBinarySearch(DataArray, 0, 10, 40) is called. What is Middle in the first call?", a: 5, tol: 0, hint: "Lower + (Upper − Lower) DIV 2 = 0 + 10 DIV 2.", sol: "0 + (10 − 0) DIV 2 = 5." },
  { q: "DataArray[5] is 26. After the first call, what is the new Lower bound when searching for 40?", a: 6, tol: 0, hint: "26 is less than 40, so the value is in the upper half and the middle is excluded.", sol: "Lower = Middle + 1 = 6." },
  { q: "What is Middle in the second call, with Lower 6 and Upper 10?", a: 8, tol: 0, hint: "6 + (10 − 6) DIV 2.", sol: "6 + 4 DIV 2 = 8." },
  { q: "How many calls are made in total to find 40?", a: 4, tol: 0, hint: "Calls: (0,10), (6,10), (6,7), (7,7).", sol: "Four calls, the last one finds 40 at index 7." },
  { q: "What does the search for 40 return?", a: 7, tol: 0, hint: "Which index holds 40?", sol: "DataArray[7] = 40, so 7 is returned." },
  { q: "What does a search for 30 return? (30 is not in the array.)", a: -1, tol: 0, hint: "Upper falls below Lower.", sol: "The range becomes empty, so −1 is returned." },
  { q: "RecursiveBinarySearch is called with Lower = 10 and Upper = 19. What is Middle?", a: 14, tol: 0, hint: "10 + (19 − 10) DIV 2. Use integer division.", sol: "10 + 9 DIV 2 = 10 + 4 = 14." },
  { q: "Most calls needed to find an item in a sorted array of 1 023 items?", a: 10, tol: 0, hint: "Halving 1 023: 511, 255, 127, 63, 31, 15, 7, 3, 1, 0.", sol: "2¹⁰ − 1 = 1 023, so at most 10 calls." }] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What must be true of the array before a binary search is used?", opts: ["It has no duplicates", "It is sorted", "It has an even number of items", "It is stored in a file"], a: 1, why: "The method relies on knowing that smaller values are on one side of the middle and larger values on the other." },
  { q: "The middle value is greater than the value being searched for. Which call is made?", opts: ["Search Lower to Middle − 1", "Search Middle + 1 to Upper", "Search Lower to Middle", "Return Middle"], a: 0, why: "A greater middle value means the target can only be lower down. The middle is excluded as it has been checked." },
  { q: "What is the base case for ‘not found’?", opts: ["Middle = 0", "Upper < Lower", "Lower = Upper", "DataArray is empty"], a: 1, why: "When the upper bound passes the lower, no items remain." },
  { q: "The condition is mistakenly written as IF Upper > Lower. Which search fails?", opts: ["A search for the first item", "A search where the target is the only item left in the range (Lower = Upper)", "A search for a missing value", "None"], a: 1, why: "When Lower = Upper there is exactly one item left, and it would be skipped, so the function might wrongly return −1." },
  { q: "The recursive calls use Middle instead of Middle − 1 and Middle + 1. What can happen?", opts: ["Nothing: it works the same", "The range may stop shrinking, so the function could call itself forever", "It returns −1 every time", "It finds the item faster"], a: 1, why: "For example with Lower = 7 and Upper = 7 the range never gets smaller, so the calls never end." },
  { q: "RETURN is missing before each recursive call. What is returned when 40 is found by a deeper call?", opts: ["7", "−1", "Nothing is passed back to the first caller", "40"], a: 2, why: "The deepest call returns 7, but the call above it throws the result away, so the original caller gets no value." },
  { q: "A binary search of 100 000 sorted items needs about how many calls at most?", opts: ["10", "17", "100", "1 000"], a: 1, why: "2¹⁷ = 131 072 > 100 000 > 2¹⁶, so at most 17 calls." }] });

Lib.cards($("#fc1"), { cards: [
  ["Binary search", "Searching a sorted array by repeatedly checking the middle item and discarding half of the remaining items."],
  ["Lower / Upper", "The first and last index of the part of the array still being searched."],
  ["Middle", "The index checked next: Lower + (Upper − Lower) DIV 2."],
  ["Base case (found)", "DataArray[Middle] = DataToFind: return Middle."],
  ["Base case (not found)", "Upper < Lower: nothing left to search: return −1."],
  ["General case", "A recursive call on the lower half or the upper half, with the middle excluded."],
  ["Sorted array", "The pre-condition for binary search: values in order, ascending here."],
  ["Linear search", "Checking the items one at a time from the start. Works on unsorted data but may check every item."],
  ["Winding / unwinding", "Calls being made down to the base case, then returning in reverse. Here the returned index is passed up unchanged."],
  ["Stack frame", "The block pushed for each call: parameters (array, Lower, Upper, DataToFind) and the return address."],
  ["Logarithmic", "The number of calls grows by one each time the array size doubles."]] });
