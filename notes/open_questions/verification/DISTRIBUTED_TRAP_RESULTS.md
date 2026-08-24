# Finite distributed-trap audit

## Exact relational result

The implication

\[
C_p\subseteq\bigcup_BD_B(p)\quad\Longrightarrow\quad
\exists B\;C_p\subseteq D_B(p)
\]

is false at the level of relational trace data, even for three blocks and a
three-point face.  Take `C_p={0,1,2}` and
`D_B0={0}`, `D_B1={1}`, `D_B2={2}`.  Their union is the face, no individual
locus covers it, and the cover is irredundant.  The executable receipt is
`distributed_trap_audit.py` / `distributed_trap_audit.json`.

This is deliberately **not** claimed as a concrete σ-class OML.  In
particular, freely assigned local liftability tables need not be realizable
by Boolean block extensions, and finite Boolean interfaces are excluded by
the Lean-certified finite-interface quarantine theorem.  The countermodel
proves only that overlap compatibility plus the cover equation cannot by
itself yield a local trap.

## Finite-atlas full-block localization theorem

There is nevertheless a rigorous finite-atlas reduction in the fine-block
slice.  Let `C_p` be a nonempty Baire face with no global σ-state and let
`B_1,...,B_n` be all the blocks.  Define `N_i` by requiring the given state's
restriction to `B_i` to be non-σ.  For a fine block, the complementary
full-block σ-locus is a union of atom/point cylinders, hence `N_i` is closed.
Blockwise σ-globalization says the finitely many `N_i` cover `C_p`.  Baire
therefore gives some `N_i` with nonempty relative interior.  A basic clopen
cylinder inside that interior gives a finite refinement on which every state
is non-σ on the same full block.

This is weaker than boundary-defect localization.  A non-σ full-block state
may share its boundary trace with a point/σ-state, so it can be boundary-good.
The fine-block boundary-good locus is the point shadow, which need be neither
open nor closed.  Therefore the distributed boundary-trap problem remains
open even for a finite fine atlas.  The original localization argument is
restored by the additional hypothesis that every relevant σ-liftable trace
locus (point shadow in the fine case) is relatively open; its complement is
then closed and the same Baire proof applies.
