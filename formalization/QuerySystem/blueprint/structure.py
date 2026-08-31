#!/usr/bin/env python3
"""Structural integrity of blueprint/src/content.tex.

The other blueprint gates all look OUTWARD from the LaTeX: checkdecls asks
whether each `\\lean{...}` name resolves in the Lean environment, axiomcheck asks
what those names rest on, coverage asks which modules go unmentioned. None of
them reads the LaTeX as a document, so a defect that lives entirely inside
content.tex passes everything.

Three did, in one session:

  * cor:concrete-mo2-not-interclosed carried `\\leanok` on its statement and no
    `\\begin{proof}` at all, so the rendered graph showed it as unproved. Nothing
    noticed until someone looked at the graph.
  * thm:mo2-gap's proof contained `ef{cor:...}` -- a dropped backslash. It
    rendered as literal text.
  * A `\\uses{}` naming a label that does not exist silently drops a DAG edge.
    The dependency graph is the artifact this repository maintains; an edge that
    vanishes is worse than one that was never written, because the picture still
    looks complete.

So this gate reads the document. It is absolute, not ratcheted: all four checks
pass at zero as of 2026-08-31.
"""
import io
import os
import re
import sys

B = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src", "content.tex")

CLAIM = {"lemma", "theorem", "proposition", "corollary"}
ALL_ENVS = "definition|lemma|theorem|proposition|corollary|remark|proof"


def strip_comments(s):
    """Drop LaTeX comments, keeping escaped \\%."""
    return re.sub(r"(?<!" + B + B + r")%.*", "", s)


def main():
    # An explicit path is for the negative tests: point the gate at a copy with
    # a defect injected and check that it fails. A gate nobody has seen fail is
    # not known to work.
    src = sys.argv[1] if len(sys.argv) > 1 else SRC
    raw = io.open(src, encoding="utf-8").read()
    s = strip_comments(raw)

    lab = re.compile(B + B + r"label\{([^}]*)\}")
    env = re.compile(B + B + r"begin\{(" + ALL_ENVS + r")\}(?:\[[^\]]*\])?(.*?)"
                     + B + B + r"end\{\1\}", re.S)

    def line_of(pos):
        return s[:pos].count("\n") + 1

    failures = []

    # --- A. every claim node is followed by a proof -------------------------
    items = []
    for m in env.finditer(s):
        names = lab.findall(m.group(2))
        items.append((m.start(), m.group(1), names[0] if names else None))
    no_proof = []
    for i, (pos, kind, name) in enumerate(items):
        if kind not in CLAIM:
            continue
        nxt = items[i + 1] if i + 1 < len(items) else None
        if not (nxt and nxt[1] == "proof"):
            no_proof.append((line_of(pos), kind, name or "(unlabelled)"))
    if no_proof:
        failures.append(
            ("%d claim node(s) with no proof block -- these render as UNPROVED"
             % len(no_proof),
             ["L%-5d %-11s %s" % r for r in no_proof],
             "Add a \\begin{proof}...\\end{proof}. If the claim is genuinely open,"
             " state it as a definition of a Prop, the way TargetA_sharp is."))

    # --- B/C. every \uses and \ref target is a real label -------------------
    labels = set(lab.findall(s))
    dup = [x for x in set(labels) if len(lab.findall(s)) and
           [y for y in lab.findall(s)].count(x) > 1]

    def targets(macro):
        out = []
        for m in re.finditer(B + B + macro + r"\{([^}]*)\}", s):
            for t in (t.strip() for t in m.group(1).split(",")):
                if t:
                    out.append((line_of(m.start()), t))
        return out

    for macro, what in (("uses", "a DAG edge that silently vanishes"),
                        ("ref", "a reference that renders as ??")):
        bad = [(ln, t) for ln, t in targets(macro) if t not in labels]
        if bad:
            failures.append(
                ("%d %s target(s) naming no label -- %s" % (len(bad), macro, what),
                 ["L%-5d %s" % (ln, t) for ln, t in bad],
                 "Fix the name, or add the missing \\label."))

    # --- E. a macro that lost its backslash ---------------------------------
    # `\ref` written from a non-raw Python string becomes CR + "ef", because
    # \r is a control character; `\begin` likewise loses \b. The result is
    # literal text that renders without complaint. Match the surviving tail
    # when what precedes it is neither a backslash nor a letter.
    maimed = []
    for tail, whole in (("ef", "ref"), ("egin", "begin"), ("nd", "end"),
                        ("abel", "label"), ("eanok", "leanok")):
        for m in re.finditer(r"(?<![" + B + B + r"A-Za-z])" + tail + r"\{", s):
            maimed.append((line_of(m.start()), tail, whole))
    if maimed:
        failures.append(
            ("%d macro(s) missing a backslash -- these render as literal text"
             % len(maimed),
             ["L%-5d found %r, meant %s%s" % (ln, t + "{", B, w)
              for ln, t, w in maimed],
             "Almost always a non-raw Python string: write r'...' or use the"
             " Edit tool."))

    # --- D. no duplicate labels ---------------------------------------------
    if dup:
        failures.append(("%d duplicate label(s)" % len(dup),
                         sorted(dup),
                         "plasTeX keeps one; the other node loses its identity."))

    n_claims = sum(1 for _, k, _ in items if k in CLAIM)
    n_defs = sum(1 for _, k, _ in items if k == "definition")
    print("blueprint structure: %d claims (all with proofs), %d definitions, "
          "%d labels, %d \\uses edges"
          % (n_claims, n_defs, len(labels), len(targets("uses"))))

    if failures:
        print("")
        for head, rows, hint in failures:
            print("%s:" % head)
            for r in rows:
                print("        %s" % r)
            print("    %s" % hint)
        print("", file=sys.stderr)
        print("STRUCTURE FAIL -- the blueprint source is not internally consistent.",
              file=sys.stderr)
        return 1

    print("STRUCTURE OK -- every claim has a proof, every \\uses and \\ref"
          " resolves, no duplicate labels.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
