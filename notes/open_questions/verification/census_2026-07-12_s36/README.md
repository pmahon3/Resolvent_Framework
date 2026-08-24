# Session 36 width-four census

This directory contains the production exhaustive period-one width-four
screen for the session-35 seven-loop removable face.  It is deliberately
separate from the session-35 artifacts.

`s36_k4_census.py` enumerates all
`C(14,4)^2 4! = 24,048,024` labeled oriented injective ports.  Before the
exact two-cell quotient test it applies the rigorous necessary condition
that all six width-two subports pass that same test: adding identifications
cannot remove a short Berge cycle or restore a collapsed block.  Ports
passing the exact test are then screened at the three cluster-stabilizer
target representatives `a1,a2,a4`; reflection transfers the answers to
`a13,a12,a10`.

The JSON checkpoint is rewritten after each old-atom 4-set.  Thus an
interrupted run resumes without recounting completed chunks.
