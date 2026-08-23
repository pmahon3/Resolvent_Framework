#!/usr/bin/env python3
r"""Blueprint coverage ratchet.

`checkdecls` verifies every \lean{} name in the blueprint resolves in Lean. That
direction is necessary but not sufficient: it says nothing about Lean modules
the blueprint never mentions, so a file can be formalized, graduated, and remain
completely invisible on the paper side. That is what happened to Diagonal.lean
-- ten theorems, including the emptiness fact the escaping-tower argument turns
on, with no blueprint entry and a green CI.

The blueprint is deliberately scoped to the non-classical programme, so most
modules are legitimately uncovered and failing on all of them would be noise.
Instead this ratchets: the currently-uncovered modules are recorded in
coverage_baseline.txt, and CI fails only when a module becomes uncovered that
was not already. Graduating a new file therefore forces a decision -- write the
blueprint entries, or add the file to the baseline deliberately.

Usage:
    coverage.py             check against the baseline (exit 1 on regression)
    coverage.py --update    rewrite the baseline from the current state
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
MODS = os.path.join(PKG, "QuerySystem")
DECLS = os.path.join(HERE, "lean_decls")
BASELINE = os.path.join(HERE, "coverage_baseline.txt")

DECL_RE = re.compile(
    r"(?m)^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(?:theorem|lemma|def|abbrev|structure|inductive|instance)\s+([A-Za-z_][\w']*)")


def uncovered():
    decls = [l.strip() for l in io.open(DECLS, encoding="utf-8") if l.strip()]
    tails = set(d.split(".")[-1] for d in decls)
    out = []
    for m in sorted(os.listdir(MODS)):
        if not m.endswith(".lean"):
            continue
        src = io.open(os.path.join(MODS, m), encoding="utf-8", errors="replace").read()
        if not (set(DECL_RE.findall(src)) & tails):
            out.append(m)
    return out


def main():
    if not os.path.exists(DECLS):
        print("no lean_decls -- run ./blueprint-web.sh first", file=sys.stderr)
        return 1
    now = uncovered()
    if "--update" in sys.argv:
        io.open(BASELINE, "w", encoding="utf-8", newline="\n").write(
            "# Modules with no blueprint entry. Regenerate: blueprint/coverage.py --update\n"
            + "\n".join(now) + "\n")
        print("baseline updated: %d uncovered module(s)" % len(now))
        return 0
    if not os.path.exists(BASELINE):
        print("no coverage_baseline.txt -- create it with coverage.py --update",
              file=sys.stderr)
        return 1
    base = set(l.strip() for l in io.open(BASELINE, encoding="utf-8")
               if l.strip() and not l.startswith("#"))
    new = [m for m in now if m not in base]
    fixed = sorted(base - set(now))
    total = len([m for m in os.listdir(MODS) if m.endswith(".lean")])
    print("blueprint coverage: %d/%d modules mentioned (%d uncovered, baseline %d)"
          % (total - len(now), total, len(now), len(base)))
    for m in fixed:
        print("  now covered: %s -- run coverage.py --update to bank it" % m)
    if new:
        print("\nCOVERAGE REGRESSION -- these modules have no blueprint entry:",
              file=sys.stderr)
        for m in new:
            print("    %s" % m, file=sys.stderr)
        print(r"  Add \lean{} nodes in blueprint/src/content.tex, re-render,",
              file=sys.stderr)
        print("  and commit lean_decls -- or add them to "
              "coverage_baseline.txt on purpose.", file=sys.stderr)
        return 1
    print("COVERAGE OK -- no newly unmentioned modules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
