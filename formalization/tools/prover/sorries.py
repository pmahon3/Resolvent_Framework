import re, os, glob, json, sys, argparse

# Repo-relative so this runs in CI as well as on tower/the Mac.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
SRC = os.environ.get(
    "QS_SRC", os.path.join(_ROOT, "formalization", "QuerySystem", "QuerySystem"))

ap = argparse.ArgumentParser(description="separate real open goals from `sorry` in prose")
ap.add_argument("--max", type=int, default=None,
                help="ratchet: exit 1 if the real open-goal count exceeds this")
ARGS = ap.parse_args()

def strip_comments(text):
    """Blank out -- line comments and /- -/ block comments, preserving offsets."""
    out = list(text)
    i, n = 0, len(text)
    depth = 0
    while i < n:
        if depth == 0 and text.startswith("/-", i):
            depth = 1; out[i] = out[i+1] = " "; i += 2; continue
        if depth > 0:
            if text.startswith("/-", i):
                depth += 1; out[i] = out[i+1] = " "; i += 2; continue
            if text.startswith("-/", i):
                depth -= 1; out[i] = out[i+1] = " "; i += 2; continue
            if text[i] != "\n":
                out[i] = " "
            i += 1; continue
        if text.startswith("--", i):
            j = text.find("\n", i)
            j = n if j == -1 else j
            for k in range(i, j):
                out[k] = " "
            i = j; continue
        i += 1
    return "".join(out)

TOK = re.compile(r"(?<![A-Za-z0-9_'.])sorry(?![A-Za-z0-9_'])")
DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+)*"
                  r"(theorem|lemma|def|instance|example|abbrev)\s+([A-Za-z0-9_'.\u00c0-\u024f\u0370-\u03ff]*)",
                  re.M)

# The library root module (QuerySystem.lean, one level up from SRC) is part of
# the build too -- scan it as well, or the ratchet has a blind spot exactly
# where one already cost us: see the header of QuerySystem.lean.
_ROOT_MODULE = os.path.join(os.path.dirname(SRC), "QuerySystem.lean")

_paths = sorted(glob.glob(os.path.join(SRC, "*.lean")))
if os.path.isfile(_ROOT_MODULE):
    _paths.append(_ROOT_MODULE)

real, commented = [], []
for path in _paths:
    raw = open(path, encoding="utf-8", errors="replace").read()
    code = strip_comments(raw)
    lines_raw = raw.splitlines()
    # index of declarations by offset
    decls = [(m.start(), m.group(1), m.group(2)) for m in DECL.finditer(code)]
    for m in TOK.finditer(raw):
        off = m.start()
        ln = raw.count("\n", 0, off) + 1
        is_code = TOK.match(code, off) is not None
        owner = ("?", "?")
        for s, kind, nm in decls:
            if s <= off:
                owner = (kind, nm)
            else:
                break
        rec = {"file": os.path.basename(path), "line": ln, "kind": owner[0],
               "name": owner[1], "text": (lines_raw[ln-1].strip() if ln-1 < len(lines_raw) else "")}
        (real if is_code else commented).append(rec)

print("=" * 92)
print(f"REAL open goals (sorry in code): {len(real)}     prose/comment mentions: {len(commented)}")
print("=" * 92)
byfile = {}
for r in real:
    byfile.setdefault(r["file"], []).append(r)
for f, rs in sorted(byfile.items(), key=lambda x: -len(x[1])):
    print(f"\n  {f}  ({len(rs)})")
    for r in rs:
        print(f"    L{r['line']:<5} {r['kind']:<8} {r['name'][:44]:<44} | {r['text'][:40]}")

print("\n" + "=" * 92)
print("SigmaEssential* files:")
sig = [f for f in os.listdir(SRC) if f.startswith("SigmaEssential")]
for f in sorted(sig):
    n = len(byfile.get(f, []))
    print(f"  {f:<44} real sorries: {n}")

json.dump(real, open(os.path.join(_HERE, "open_goals.json"), "w"), indent=1)
print(f"\nwrote open_goals.json ({len(real)} goals)")

if ARGS.max is not None:
    print("")
    if len(real) > ARGS.max:
        print(f"RATCHET FAIL: {len(real)} real open goals, budget is {ARGS.max}.")
        print("A new `sorry` was introduced. Close it, or raise the budget deliberately.")
        sys.exit(1)
    if len(real) < ARGS.max:
        print(f"RATCHET: {len(real)} real open goals, budget {ARGS.max} -- tighten"
              f" the budget in .github/workflows/lean.yml to {len(real)}.")
    print(f"RATCHET OK: {len(real)} <= {ARGS.max}")
