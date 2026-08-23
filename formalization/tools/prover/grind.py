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



NAME_RE = re.compile(
    r"^\s*(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+)*"
    r"(?:theorem|lemma|def|instance|abbrev|structure|example)\s+"
    r"([A-Za-z_][A-Za-z0-9_'.]*)", re.M)

DECL_RE = re.compile(
    r"^(?:/--|@\[|private\s|protected\s|noncomputable\s|theorem\s|lemma\s|def\s|"
    r"instance\s|abbrev\s|structure\s|example\s)", re.M)


def _is_only_attachment(chunk):
    """True if `chunk` is a docstring, section comment or bare attribute -- i.e.
    something that must stay attached to the declaration that FOLLOWS it.
    Splitting there sends Lean an incomplete command ("unexpected end of input;
    expected 'lemma'")."""
    t = chunk.strip()
    if t.startswith("/-"):
        j = t.find("-/")
        return j == -1 or t[j + 2:].strip() == ""
    if t.startswith("@["):
        j = t.find("]")
        return j == -1 or t[j + 1:].strip() == ""
    return False


def decl_spans(src):
    """Byte spans of top-level declarations, docstrings kept with their bodies."""
    starts = [m.start() for m in DECL_RE.finditer(src)]
    if not starts:
        return []
    raw = list(zip(starts, starts[1:] + [len(src)]))
    spans, i = [], 0
    while i < len(raw):
        a, b = raw[i]
        while _is_only_attachment(src[a:b]) and i + 1 < len(raw):
            i += 1
            b = raw[i][1]
        spans.append((a, b))
        i += 1
    return spans


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
        env_before = env
        msg = {"cmd": chunk} if env is None else {"cmd": chunk, "env": env}
        out = repl.send(msg)
        env = out.get("env", env)
        errors += _errs(out)
        nm = NAME_RE.search(chunk)
        for so in (out.get("sorries") or []):
            so["decl"] = nm.group(1) if nm else "?"
            # Keep what `confirm` needs: the declaration's own text and the
            # environment it was elaborated in.
            so["_chunk"], so["_env"] = chunk, env_before
            # positions are chunk-relative; make them file-relative
            if isinstance(so.get("pos"), dict) and "line" in so["pos"]:
                so["pos"] = dict(so["pos"],
                                 line=so["pos"]["line"] + src.count(chr(10), 0, a))
            sorries.append(so)
    return sorries, errors


NL = chr(10)
SORRY_RE = re.compile(r"(?m)^([ 	]*)sorry[ 	]*$")


def confirm(repl, so, proof):
    """Re-elaborate a found proof as real file text.

    The search accepts a tactic when the REPL reports no remaining goals, but
    that is not the same as the declaration compiling. A `?_` in *term*
    position (e.g. `rcases h (fun x hx => ?_) hy`) defers its metavariable:
    the REPL reports no goals while the hole is still unsynthesized, and the
    file then fails with "don't know how to synthesize placeholder". So splice
    the proof in and elaborate the whole declaration, which is what the file
    will do. Returns (ok, detail).
    """
    chunk, env = so.get("_chunk"), so.get("_env")
    if chunk is None:
        return True, "not confirmed (no chunk)"
    holes = SORRY_RE.findall(chunk)
    if len(holes) != 1:
        return True, f"not confirmed ({len(holes)} sorries in decl)"
    body = NL.join(holes[0] + t.strip() for t in proof)
    msg = {"cmd": SORRY_RE.sub(lambda _: body, chunk, count=1)}
    if env is not None:
        msg["env"] = env
    try:
        out = repl.send(msg)
    except Exception as e:
        return False, f"confirm raised {type(e).__name__}"
    errs = _errs(out)
    if errs:
        return False, (errs[0].get("data") or "error")[:120].replace(NL, " ")
    if out.get("sorries"):
        return False, "still contains sorry"
    return True, "confirmed"


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
        ln = s.get("decl") or line_of(src, s.get("pos"))
        goal = s.get("goal", "")
        head = goal.split("\n")[-1][:90]
        print(f"[{idx}/{len(sors)}] {ln}  {head}")
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
            ok, why = confirm(repl, s, proof)
            if not ok:
                # The search saw no goals but the declaration does not compile.
                print(f"        REJECTED [{arm}] {why}")
                print(f"          was: {' ; '.join(proof)}")
                proof = None
                stats = dict(stats, reason="rejected", rejected=why)
            else:
                print(f"        CLOSED [{arm}] {' ; '.join(proof)}")
        if not proof:
            print(f"        open ({stats.get('reason')}, {stats.get('secs')}s)")
        results.append({"decl": s.get("decl"), "index": idx - 1,
                        "line": line_of(src, s.get("pos")),
                        "goal": goal, "closed": bool(proof),
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
                print(f"  {r.get('decl') or r['line']}  {r['goal'].split(chr(10))[-1][:100]}")

    # NB `index` is the reliable identifier: sorries are reported in file
    # order, so results[i] is the i-th `sorry` in the file. `line` comes from
    # the REPL's chunk-relative position and has been observed off by a
    # declaration -- splice by index or by `decl`, never by `line`.
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
