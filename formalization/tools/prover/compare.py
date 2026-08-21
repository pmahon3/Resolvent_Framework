import json, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(p):
    rows = json.load(open(os.path.join(HERE, p), encoding="utf-8"))
    return {(r["file"], r["name"]): r for r in rows}


base = load("res_baseline.json")
bfs = load("res_bfsprover.json")

keys = sorted(set(base) & set(bfs))
print("=" * 92)
print(f"MATCHED COMPARISON  n={len(keys)} cases present in both arms")
print("=" * 92)

bs = {k for k in keys if base[k]["ok"]}
ms = {k for k in keys if bfs[k]["ok"]}

both = bs & ms
only_b = bs - ms
only_m = ms - bs
neither = set(keys) - bs - ms

print(f"  Mathlib automation solved : {len(bs):>3}/{len(keys)}  ({100*len(bs)/len(keys):.0f}%)")
print(f"  BFS-Prover-7B solved      : {len(ms):>3}/{len(keys)}  ({100*len(ms)/len(keys):.0f}%)")
print()
print(f"  both                      : {len(both):>3}")
print(f"  baseline only             : {len(only_b):>3}   <- model REGRESSIONS")
print(f"  BFS-Prover only           : {len(only_m):>3}   <- what the model ADDS")
print(f"  neither                   : {len(neither):>3}")

hard = [k for k in keys if not base[k]["ok"]]
won = [k for k in hard if bfs[k]["ok"]]
print(f"\n  >>> on the {len(hard)} cases Mathlib automation could NOT solve,")
print(f"      BFS-Prover solved {len(won)}  ({100*len(won)/max(len(hard),1):.1f}%)")

# --- contamination check: did the model just call Mathlib's search tactics? ---
SEARCH = re.compile(r"(?<![\w'])(exact\?|apply\?|rw\?|simp\?|aesop\?|hint|library_search|polyrith)(?![\w'])")
tainted = [k for k in ms if bfs[k].get("proof") and SEARCH.search(bfs[k]["proof"])]
clean_add = [k for k in only_m if not (bfs[k].get("proof") and SEARCH.search(bfs[k]["proof"]))]
print(f"\n  model wins using a Mathlib SEARCH tactic (exact? etc): {len(tainted)}/{len(ms)}")
print(f"  model-only wins that are search-free                 : {len(clean_add)}/{len(only_m)}")

if only_m:
    print("\n  --- proofs BFS-Prover found that automation missed ---")
    for k in sorted(only_m)[:14]:
        p = (bfs[k].get("proof") or "")[:74]
        tag = "  [SEARCH]" if SEARCH.search(bfs[k].get("proof") or "") else ""
        print(f"    {k[0][:24]:<24} {k[1][:26]:<26} {p}{tag}")

if only_b:
    print("\n  --- regressions (automation solved, model did not) ---")
    for k in sorted(only_b)[:10]:
        print(f"    {k[0][:24]:<24} {k[1][:26]:<26} model={bfs[k]['reason']}")

print("\n  fail reasons, BFS arm:")
for r, n in Counter(bfs[k]["reason"] for k in keys if not bfs[k]["ok"]).most_common():
    print(f"    {r:<20} {n}")

tb = sum(base[k]["secs"] for k in keys)
tm = sum(bfs[k]["secs"] for k in keys)
print(f"\n  wall: automation {tb/60:.1f} min   BFS-Prover {tm/60:.1f} min")
