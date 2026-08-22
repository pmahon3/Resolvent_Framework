"""grind.py -- close the `sorry`s in a Lean file using tower compute, unattended.

The division of labour this exists to enforce:

  * expensive (a person, or Claude): statements, and the decomposition of a
    theorem into lemmas small enough to be searchable;
  * free (tower): finding the proof of each individual lemma.

So: write a skeleton whose every proof is `sorry`, run this, read a short
report, and hand-prove only what survives. Nothing here consumes subscription
tokens.

How it works. The Lean REPL, handed a whole file, returns EVERY `sorry` in it
with a `proofState` and the goal at that point -- already in context, with all
prior declarations in scope. Best-first search then runs per goal, reusing
`bfs.search_from` so there is exactly one search implementation in the tree.

Two proposers, cheapest first (the retrodiction eval measured these as
complementary, not redundant -- 43/100 each, 56/100 union):
  1. a fixed Mathlib automation list -- seconds, closes routine goals;
  2. BFS-Prover-V2-7B on the 3060 -- minutes, closes goals automation misses.

Usage:
    python grind.py ../../staging/Foo.lean                 # report only
    python grind.py ../../staging/Foo.lean --apply         # splice in wins
    python grind.py ../../staging/Foo.lean --no-model      # automation only
"""
import argparse, json, os, re, sys, time

# Goals contain ⊢, ℝ, ∀ ... and Windows consoles default to cp1252. Make the
# script robust rather than requiring PYTHONUTF8 at every call site.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bfs import Repl, ReplTimeout, search_from, BASELINE_TACTICS  # noqa: E402


def sorries_of(repl, src):
    """Every `sorry` in the file, with its proofState and goal."""
    out = repl.send({"cmd": src})
    errs = [m for m in (out.get("messages") or [])
            if m.get("severity") == "error"]
    return out.get("sorries") or [], errs


def line_of(src, pos):
    """1-based line for a REPL position dict."""
    if isinstance(pos, dict) and "line" in pos:
        return pos["line"]
    return -1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--model", default="bfs-prover:7b-q4")
    ap.add_argument("--no-model", action="store_true",
                    help="automation only; skip the model arm")
    ap.add_argument("--budget", type=int, default=40)
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--apply", action="store_true",
                    help="splice closed proofs back into the file")
    a = ap.parse_args()

    src = open(a.target, encoding="utf-8").read()
    t0 = time.time()
    repl = Repl(timeout=a.timeout)
    try:
        sors, errs = sorries_of(repl, src)
    except ReplTimeout:
        print("REPL TIMEOUT loading the file -- is it too large, or is a "
              "prior declaration looping?")
        return 2

    if errs:
        print(f"FILE HAS {len(errs)} ERROR(S) -- fix these first; a file that "
              f"does not elaborate has no usable goals:")
        for m in errs[:5]:
            print(f"  L{line_of(src, m.get('pos'))}: {str(m.get('data'))[:160]}")
        return 1

    print(f"GRIND {os.path.basename(a.target)}: {len(sors)} sorries\n")
    results = []
    for idx, s in enumerate(sors, 1):
        ln = line_of(src, s.get("pos"))
        goal = s.get("goal", "")
        head = goal.split("\n")[-1][:90]
        print(f"[{idx}/{len(sors)}] L{ln}  {head}")
        proof, stats = None, {}
        # arm 1: Mathlib automation (cheap)
        proof, stats = search_from(repl, s["proofState"], goal, "__baseline__",
                                   max_expansions=len(BASELINE_TACTICS) + 4,
                                   k=len(BASELINE_TACTICS), verbose=False)
        arm = "automation"
        # arm 2: the model, only on what automation missed
        if proof is None and not a.no_model:
            proof, stats = search_from(repl, s["proofState"], goal, a.model,
                                       max_expansions=a.budget, k=a.k,
                                       verbose=False)
            arm = "model"
        if proof:
            print(f"        CLOSED [{arm}] {' ; '.join(proof)}")
        else:
            print(f"        open ({stats.get('reason')}, {stats.get('secs')}s)")
        results.append({"line": ln, "goal": goal, "closed": bool(proof),
                        "arm": arm if proof else None, "proof": proof,
                        "stats": stats})

    closed = [r for r in results if r["closed"]]
    print(f"\n{'='*70}\nCLOSED {len(closed)}/{len(results)}"
          f"  (automation {sum(1 for r in closed if r['arm']=='automation')},"
          f" model {sum(1 for r in closed if r['arm']=='model')})"
          f"   {round(time.time()-t0)}s")
    if len(closed) < len(results):
        print("\nSTILL OPEN -- hand these back to a person:")
        for r in results:
            if not r["closed"]:
                print(f"  L{r['line']}  {r['goal'].split(chr(10))[-1][:100]}")

    rep = a.target + ".grind.json"
    json.dump(results, open(rep, "w", encoding="utf-8"), indent=1)
    print(f"\nreport: {rep}")

    if a.apply and closed:
        print("NOTE: --apply is not implemented; splicing by REPL position is "
              "unreliable when several sorries share a line. Copy from the "
              "report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
