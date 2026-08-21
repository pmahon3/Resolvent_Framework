"""Build a retrodiction eval set from proved theorems in the QuerySystem development.

For each `theorem`/`lemma` with a real proof, record the exact character span of the
proof body so the runner can splice in a candidate and re-elaborate the file.
"""
import re, os, glob, json

SRC = r"C:\Users\pmahon\Research\Mathematics\Resolvent_Framework\formalization\QuerySystem\QuerySystem"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evalset.json")

DECL_RE = re.compile(
    r"^(?:@\[[^\]]*\]\s*)?"
    r"(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+)*"
    r"(theorem|lemma)\s+"
    r"([^\s:({\[]+)",
    re.M)

# a line that starts a new top-level item -> previous declaration ended
STOP_RE = re.compile(
    r"^(?:@\[|/-|--|theorem\b|lemma\b|def\b|abbrev\b|instance\b|structure\b|inductive\b|class\b|"
    r"namespace\b|end\b|section\b|open\b|variable\b|universe\b|import\b|example\b|"
    r"noncomputable\b|private\b|protected\b|nonrec\b|attribute\b|macro\b|notation\b|"
    r"scoped\b|local\b|set_option\b|deriving\b|#\w+)")


def strip_comments(text):
    out = list(text); i, n, depth = 0, len(text), 0
    while i < n:
        if depth == 0 and text.startswith("/-", i):
            depth = 1; out[i] = out[i + 1] = " "; i += 2; continue
        if depth > 0:
            if text.startswith("/-", i):
                depth += 1; out[i] = out[i + 1] = " "; i += 2; continue
            if text.startswith("-/", i):
                depth -= 1; out[i] = out[i + 1] = " "; i += 2; continue
            if text[i] != "\n":
                out[i] = " "
            i += 1; continue
        if text.startswith("--", i):
            j = text.find("\n", i); j = n if j == -1 else j
            for k in range(i, j):
                out[k] = " "
            i = j; continue
        i += 1
    return "".join(out)


def decl_end(code, start):
    """End offset of the declaration beginning at `start`."""
    i = code.find("\n", start)
    if i == -1:
        return len(code)
    while i < len(code):
        j = code.find("\n", i + 1)
        if j == -1:
            return len(code)
        line = code[i + 1:j]
        if line and not line[0].isspace() and STOP_RE.match(line):
            return i + 1
        i = j
    return len(code)


def split_proof(code, start, end):
    """Offset where the proof body begins (after top-level `:=`), else None."""
    depth = 0
    i = start
    while i < end:
        c = code[i]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif depth == 0 and code.startswith(":=", i):
            return i + 2
        i += 1
    return None


cases = []
for path in sorted(glob.glob(os.path.join(SRC, "*.lean"))):
    raw = open(path, encoding="utf-8", errors="replace").read()
    code = strip_comments(raw)
    for m in DECL_RE.finditer(code):
        s = m.start()
        e = decl_end(code, s)
        p = split_proof(code, s, e)
        if p is None:
            continue
        proof = raw[p:e].strip()
        if not proof or re.search(r"(?<![\w'.])sorry(?![\w'])", strip_comments(raw[p:e])):
            continue
        sig = raw[s:p].strip()
        cases.append({
            "file": os.path.basename(path),
            "path": path,
            "kind": m.group(1),
            "name": m.group(2),
            "sig": sig,
            "proof": proof,
            "decl_start": s,
            "proof_start": p,
            "proof_line": raw.count("\n", 0, p) + 1,
            "decl_end": e,
            "proof_chars": len(proof),
            "proof_lines": proof.count("\n") + 1,
            "is_term": not proof.lstrip().startswith("by"),
        })

json.dump(cases, open(OUT, "w", encoding="utf-8"), indent=1)

print("=" * 88)
print(f"EVAL SET: {len(cases)} proved theorems/lemmas across "
      f"{len(set(c['file'] for c in cases))} files")
print("=" * 88)
ls = sorted(c["proof_lines"] for c in cases)
cs = sorted(c["proof_chars"] for c in cases)
if ls:
    print(f"  proof lines  p25={ls[len(ls)//4]}  p50={ls[len(ls)//2]}  "
          f"p90={ls[int(len(ls)*.9)]}  max={ls[-1]}")
    print(f"  proof chars  p50={cs[len(cs)//2]}  p90={cs[int(len(cs)*.9)]}  max={cs[-1]}")
    print(f"  term-mode: {sum(c['is_term'] for c in cases)}   tactic-mode: {sum(not c['is_term'] for c in cases)}")

print("\n  by file (top 15):")
byf = {}
for c in cases:
    byf.setdefault(c["file"], []).append(c)
for f, cc in sorted(byf.items(), key=lambda x: -len(x[1]))[:15]:
    med = sorted(x["proof_lines"] for x in cc)[len(cc) // 2]
    print(f"    {f[:46]:<46} {len(cc):>4}  median {med:>3} lines")

print("\n  --- 5 shortest (best smoke tests) ---")
for c in sorted(cases, key=lambda x: x["proof_chars"])[:5]:
    print(f"    {c['file'][:34]:<34} {c['name'][:34]:<34} := {c['proof'][:34]}")
print(f"\nwrote {OUT}")
