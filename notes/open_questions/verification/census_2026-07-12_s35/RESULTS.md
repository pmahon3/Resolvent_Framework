# Session 35 — operative 7-loop removable-face relay census

Scope: the 7-loop cell with blocks
`{2i,2i+1,2i+2 mod 14}`, removable face selected by
`C={a0,a3,a11}`, period-one relays, and every oriented injective atom port
of width `k=1,2,3`.  The chain uses the validated one-sided rooted,
any-position σ-liveness convention.

The cell has 29 two-valued states.  The face has exactly three states and
its 26-state complement order-determines all 714 canonical nonorders.
Since every face state charges `a0`, `a0` cannot be the master target.
The common-zero targets are `{a1,a2,a4,a10,a12,a13}`.  The stabilizer of
the cluster has target orbits `{a1,a13}`, `{a2,a12}`, `{a4,a10}`.

## Exhaustive local census

Counts below are per target.  “Valid” means the exact two-cell quotient
linearity/Berge-girth screen.

| width | labeled maps | valid maps | operative survivors |
|---:|---:|---:|---:|
| 1 | 196 | 196 | 0 for every target |
| 2 | 16,562 | 9,408 | 0 for every target |
| 3 | 794,976 | 122,500 | `2,9,0,0,9,2` for targets `1,2,4,10,12,13` |

An operative survivor has all three face states in the free all-zero
basin, no face state σ-live, and σ-live states that order-determine the
cell.  Of the 22 width-three target/map pairs, 16 have live set exactly
the 26-state complement and six have an order-determining 25-state subset.

## Downstream verdict

The four `a1/a13` pairs fail relay girth already in the three-cell window.
The other 18 pairs (nine reflection orbits) pass quotient girth through
six cells, but all fail the target-collecting master geometry at gap one:
their adjacent-target block-chain distance is `d_1=2` or `3`, below the
required `d_1>=4`.  Hence none reaches cross-cell separation.

**Verdict: rigorous bounded no-go for this 7-loop exemplar, period one,
all injective ports of widths 1–3.**  This does not close widths `k>=4`,
period `p>=2`, other removable faces in the 7-loop, or the two-pentagon
shared-atom cell.

Independent machinery:

- `../audit_s35_7loop_census.py` — self-contained exhaustive census and
  explicit liveness-oracle samples;
- `../verify_s35_survivor_girth.py` — quotient girth and master distances;
- `relay7_core.py`, `test_relay7_core.py` — generalized production core
  and independent anchors.
