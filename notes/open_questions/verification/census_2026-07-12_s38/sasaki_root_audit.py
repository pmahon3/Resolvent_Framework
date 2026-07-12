#!/usr/bin/env python3
"""Bounded-depth right-Sasaki root audit for the s38 seven-loop cell."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASES = json.loads((HERE / "s38_p3_k1_checkpoint.json").read_text())["near_misses"]
BOT, TOP = ("0", 0), ("1", 0)
ATOMS = [("a", i) for i in range(14)]
COATOMS = [("c", i) for i in range(14)]
ELEMS = [BOT, TOP] + ATOMS + COATOMS
BLOCKS = [{2*i, 2*i+1, (2*i+2) % 14} for i in range(7)]

def orthogonal(i, j):
    return i != j and any(i in b and j in b for b in BLOCKS)

def leq(x, y):
    if x == BOT or y == TOP or x == y:
        return True
    if x == TOP or y == BOT:
        return False
    return x[0] == "a" and y[0] == "c" and orthogonal(x[1], y[1])

def unique_extreme(xs, lower):
    good = [z for z in ELEMS if all(leq(z, x) for x in xs)] if lower else \
           [z for z in ELEMS if all(leq(x, z) for x in xs)]
    extreme = [z for z in good if all(leq(w, z) for w in good)] if lower else \
              [z for z in good if all(leq(z, w) for w in good)]
    assert len(extreme) == 1, (xs, good, extreme)
    return extreme[0]

def meet(x, y): return unique_extreme((x, y), True)
def join(x, y): return unique_extreme((x, y), False)
def comp(x):
    if x == BOT: return TOP
    if x == TOP: return BOT
    return ("c", x[1]) if x[0] == "a" else ("a", x[1])
def sasaki(x, y): return meet(y, join(x, comp(y)))

# Structural anchors: this really is an orthomodular lattice under the model.
for x in ELEMS:
    assert comp(comp(x)) == x and meet(x, comp(x)) == BOT and join(x, comp(x)) == TOP
for x in ELEMS:
    for y in ELEMS:
        if leq(x, y):
            assert join(x, meet(y, comp(x))) == y

def enc(x):
    if x[0] == "a": return x[1]
    if x[0] == "c": return 14 + x[1]
    return None

def name(x):
    return x[0] if x in (BOT, TOP) else f"a{x[1]}" + ("^perp" if x[0] == "c" else "")

common = None
for c in CASES:
    missing0 = set(map(tuple, c["missing"][0]))
    common = missing0 if common is None else common & missing0

levels = [{("a", 0), ("a", 3), ("a", 11)}]
for _depth in range(1, 5):
    prev = set().union(*levels)
    nxt = {sasaki(x, y) for x in prev for y in prev} - prev
    levels.append(nxt)

generated = set()
hits = []
for depth, level in enumerate(levels):
    generated |= level
    for x in sorted(generated):
        ex = enc(x)
        if ex is None: continue
        for a, b in sorted(common):
            if a == ex and not leq(x, ATOMS[b] if b < 14 else COATOMS[b-14]):
                hits.append({"depth": depth, "root": name(x),
                             "nonorder": f"{name(x)} !<= " +
                             name(ATOMS[b] if b < 14 else COATOMS[b-14])})
    if hits:
        break

out = {
    "schema": 1,
    "cell": "30-element OML pasted from seven 3-atom blocks in a 7-loop",
    "right_sasaki": "x & y = y meet (x join y^perp)",
    "premises": ["a0", "a3", "a11"],
    "depth_new_elements": [[name(x) for x in sorted(level)] for level in levels],
    "first_hit_depth": min(h["depth"] for h in hits),
    "common_root_hits_at_first_depth": [h for h in hits if h["depth"] == min(q["depth"] for q in hits)],
    "anchors": {"elements": len(ELEMS), "orthocomplement_checked": True,
                "orthomodular_law_checked_all_comparable_pairs": True},
}
(HERE / "s38_sasaki_root_audit.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
