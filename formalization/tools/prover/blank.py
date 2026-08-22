"""blank.py -- make a retrodiction copy of a Lean file.

Replaces every theorem/lemma proof body with `sorry`, leaving definitions,
imports, namespaces and docstrings intact. The result is a file whose goals are
exactly the ones we already know are provable, in their real context -- which is
the only honest way to measure what the prover loop can do on this development,
as opposed to on toy goals.

    python blank.py ../../staging/Foo.lean            # -> Foo_retro.lean
    python blank.py ../../staging/Foo.lean --out X.lean

Then run grind.py on the output and compare against the original.

Definitions are NOT blanked: a `def` is data the later goals need in scope, and
blanking it changes the problem rather than hiding a proof.
"""
import argparse, io, os, re, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

DECL = re.compile(
    r"^(?:/--|@\[|private\s|protected\s|noncomputable\s|theorem\s|lemma\s|def\s|"
    r"instance\s|abbrev\s|structure\s|example\s)", re.M)
IS_PROOF = re.compile(r"(/--(?:.|\n)*?-/\s*)?(theorem|lemma)\s")


def blank(src):
    starts = [m.start() for m in DECL.finditer(src)]
    if not starts:
        return src, 0
    spans = list(zip(starts, starts[1:] + [len(src)]))
    out, prev, n = [], 0, 0
    for a, b in spans:
        out.append(src[prev:a])
        chunk = src[a:b]
        if IS_PROOF.match(chunk.lstrip()) and ":= by" in chunk:
            i = chunk.index(":= by")
            tail = chunk[i + len(":= by"):]
            trailing = "\n" * (len(tail) - len(tail.rstrip("\n")))
            chunk = chunk[:i] + ":= by\n  sorry" + (trailing or "\n")
            n += 1
        out.append(chunk)
        prev = b
    out.append(src[prev:])
    return "".join(out), n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    src = io.open(a.target, encoding="utf-8").read()
    res, n = blank(src)
    out = a.out or (os.path.splitext(a.target)[0] + "_retro.lean")
    io.open(out, "w", encoding="utf-8", newline="\n").write(res)
    print(f"blanked {n} proofs -> {out}")
    print("check it still elaborates (with sorry warnings) before trusting a run:")
    print(f"  lake env lean {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
