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

## Finite-atlas localization theorem

There is nevertheless a rigorous finite-atlas reduction in the fine-block
slice.  Let `C_p` be a nonempty Baire face and let `B_1,...,B_n` be all the
blocks.  For a fine block, its good locus is a union of atom/point cylinders,
hence relatively open; its defect locus `D_i` is relatively closed.  If the
finitely many `D_i` cover `C_p`, the Baire theorem (indeed the elementary
finite closed-cover argument) says some `D_i` has nonempty relative interior.
Because the state space is zero-dimensional, that interior contains a basic
clopen cylinder.  Adding its finitely many coordinates to the pattern gives
a nonempty refined face locally trapped at `B_i`.

Consequently a finite fine-block atlas can be distributed on the original
face, but it cannot remain purely distributed under all coherent finite
pattern refinements.  Any minimal counterexample chosen also minimal under
finite face refinement is locally trapped.  This does not cover coarse
blocks, where σ-liftable trace loci need not be open, nor an uncountable
atlas, where the Baire finite/countable-category reduction needs additional
density hypotheses.
