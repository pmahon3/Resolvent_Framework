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


DECL_RE = re.compile(
    r"^(?:/--|@\[|private\s|protected\s|noncomputable\s|theorem\s|lemma\s|def\s|"
    r"instance\s|abbrev\s|structure\s|example\s)", re.M)


def decl_spans(src):
    """Byte spans of top-level declarations, in order."""
    starts = [m.start() for m in DECL_RE.finditer(src)]
    if not starts:
        return []
    return [(a, b) for a, b in zip(starts, starts[1:] + [len(src)])]


def sorries_of(repl, src):
    """Every `sorry` in the file, with a proofState that CAN SEE the file's own
    definitions.

    Sending the whole file as one `cmd` does NOT do this: the proof states it
    returns lack that command's own constants, so every tactic mentioning a
    local definition dies with `unknown constant`, the search exhausts in
    seconds, and the run looks like a weak model rather than a broken harness.
    That is exactly the bug `bfs.file_envs` exists to avoid, rediscovered here
    the hard way.

    So: replay the file declaration by declaration, committing each to the
    environment before asking for the next one's goals.
    """
    spans = decl_spans(src)
    if not spans:
        out = repl.send({"cmd": src})
        return (out.get("sorries") or []), _errs(out)

    prologue = src[:spans[0][0]]
    env, sorries, errors = None, [], []
    if prologue.strip():
        out = repl.send({"cmd": prologue})
        env = out.get("env", env)
        errors += _errs(out)

    for a, b in spans:
        chunk = src[a:b]
        msg = {"cmd": chunk} if env is None else {"cmd": chunk, "env": env}
        out = repl.send(msg)
        env = out.get("env", env)
        errors += _errs(out)
        for so in (out.get("sorries") or []):
            # positions are chunk-relative; make them file-relative
            if isinstance(so.get("pos"), dict) and "line" in so["pos"]:
                so["pos"] = dict(so["pos"],
                                 line=so["pos"]["line"] + src.count(chr(10), 0, a))
            sorries.append(so)
    return sorries, errors


def _errs(out):
    return [m for m in (out.get("messages") or []) if m.get("severity") == "error"]


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
    ap.add_argument("--pre", default="",
                    help="extra tactics for the automation arm, ';;'-separated. "
                         "Use for definitional openers, e.g. "
                         "--pre 'simp only [B, A, Set.mem_setOf_eq]'. Without an "
                         "opening move the baseline list cannot touch a goal "
                         "stated over an opaque def.")
    ap.add_argument("--apply", action="store_true",
                    help="splice closed proofs back into the file")
    a = ap.parse_args()

    extra = [t.strip() for t in a.pre.split(";;") if t.strip()]
    base = BASELINE_TACTICS + extra
    if extra:
        print(f"automation arm extended with {len(extra)} opener(s): {extra}")

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
                                   max_expansions=2 * len(base) + 8,
                                   k=len(base), verbose=False, extra=extra)
        arm = "automation"
        # arm 2: the model, only on what automation missed
        if proof is None and not a.no_model:
            proof, stats = search_from(repl, s["proofState"], goal, a.model,
                                       max_expansions=a.budget, k=a.k,
                                       verbose=False, extra=extra)
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
