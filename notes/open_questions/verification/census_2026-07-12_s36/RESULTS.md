# Session 36 — exhaustive period-one width-four census

Scope is the session-35 seven-loop cell and face `C={a0,a3,a11}`, every
oriented injective width-four atom port, and the validated one-sided rooted
σ-liveness convention.

The exhaustive labeled count is
`C(14,4)^2 4! = 24,048,024`.  Of these, 477,848 pass the necessary
all-six-width-two-subports prefilter, 477,652 pass the exact two-cell
linearity/Berge-girth test, and 334,054 also pass the three-cell girth test.

The full operative screen on cluster-stabilizer target representatives has
counts:

| target | operative | reflected target |
|---:|---:|---:|
| `a1` | 8 | `a13` |
| `a2` | 40 | `a12` |
| `a4` | 1 | `a10` |

Thus there are 49 representative or 98 fully labeled target/map survivors.
All have the whole three-state face free and nonlive and an
order-determining live subset of the 26-state complement.  Live-set sizes
range from 18 to 26; two survivors have the exact complement.

Downstream, 44/49 representatives pass three-cell girth and 43/49 pass
through six cells.  Exactly two representatives also meet the adjacent
master-target distance bound `d1>=4`:

1. target `a1`, port
   `((0,11),(3,5),(6,9),(13,3))`, with target-gap distances
   `4,5,6,8,9,10,12,13,14,16,17,18,20,21,22` for gaps 1–15;
2. target `a1`, port
   `((1,7),(5,9),(11,11),(12,3))`, with distances `4,5,6,...,6`.

Both pass the finite relay quotient girth test through 120 cells (exact
girth five) and all target gaps through 60 meet the master bound.  Target
atoms remain distinct in the tested quotient, so adjoining them to one
complete master block has the intended distinct-atom interpretation.

The exact rooted cross-cell path screen then kills both at adjacent cells.
For each candidate, every state word through cells 0 and 1 that has an
infinite exactly-one-target continuation was enumerated.  Candidate 1 has
31 realizable adjacent state pairs and candidate 2 has 26.  In both, the
actual cross-cell nonorder

`a1(cell 0) not<= a1(cell 1)^perp`

has no σ-state witness: every admissible path charging the left `a1` also
charges the right `a1`.  This is already conclusive; the broader audit also
records all cross-cell false orders for every pair of cells `0<=i<j<=12`.
Reflections give the target-`a13` cases.

Hence this is a rigorous **bounded no-go for period one, all injective
ports of widths k<=4**, on the named seven-loop face.  The next classes
remain period two at small width or a higher-slack shared-pentagon face.

Authoritative machine output is in `s36_k4_results.json` and
`s36_downstream_results.json` and `s36_cross_cell_results.json`.
