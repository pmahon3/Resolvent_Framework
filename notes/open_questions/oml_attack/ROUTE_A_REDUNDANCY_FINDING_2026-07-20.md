# Route (a) is redundant with already-proved work — finding, 2026-07-20

*Session E5 follow-on, branch `e5-banking-audit`. Written before any
hand-work on route (a), which is what this finding makes unnecessary in
its stated form.*

## Verdict

**Route (a)'s target conclusion was already proved on 2026-07-14**
(Campaign 12, `oml_omega1_cylinder_hub.md` §1), six days before the
2026-07-20 handoff scoped it as open. The handoff's instruction
"attack route (a) first" rests on a staleness error, not on new
mathematics.

Important scope distinction, kept deliberately: §1 closes route (a)'s
**conclusion** by a *different argument* than the one route (a) names.
Route (a) literally asks whether `prop:finite-obstruction`'s two-cell
countable-meet mechanism generalizes. §1 does not generalize that
mechanism; it reaches the same conclusion via
`thm:ctbly-gen` (the extension theorem) + a Lusin–Souslin closure. So:

- **Proved:** no witness lives on a countably-generated, faithful,
  order-separating hub.
- **NOT proved, and still genuinely open:** that the specific two-cell
  meet-disagreement mechanism is what does the killing.

If route (a) is wanted for the *mechanism* rather than the conclusion,
it survives as a question about proof technique, not about existence.
That is a Type-2 (new proof) question at best, not a Type-1 gap.

## The standardness seam, and why it closes

The one real gap between §1 and route (a)'s full generality:

§1's argument opens *"For a standard Borel hub…"* and invokes
Lusin–Souslin, which requires standardness. Route (a) grants no
standardness — it quantifies over any faithful, order-separating,
countably-generated hub in any concrete σ-complete OML. And
**non-standard countably-generated separating hubs genuinely exist**: a
countably generated separating (X,𝒜) embeds injectively into 2^ω via
x ↦ (1_{A_n}(x))_n, but is standard only when that image is Borel; a
Bernstein or analytic-not-Borel image gives a non-standard instance.

So §1's *stated* argument does not reach all of route (a). **But the
conclusion still does**, because standardness is not load-bearing for
what is actually needed downstream:

1. **Singletons come free from separation alone.** If (A_n) separates
   points of X, then for each x, {x} = ⋂_n B_n with B_n := A_n or
   A_n^c according to x's membership — a *countable* intersection,
   hence in the σ-algebra. No Lusin–Souslin, no standardness.
   Standardness in §1 is used for the strictly stronger conclusion
   "the generated algebra is the *full* Borel algebra," which is more
   than the puncture obstruction consumes.

2. **The multi-piece case collapses to the single-piece case.**
   `prop:ctbly-gen-full` quantifies over "however many
   countably-generated pieces are combined," but the combination is
   over *countably* many pieces. A countable union of countable
   generator sets is countable, so the join is again countably
   generated; joint separation makes the join separating. Hence the
   join is a single countably-generated separating algebra and
   `thm:ctbly-gen` applies to it directly.

3. **`thm:ctbly-gen` itself is standardness-free.** Its two
   load-bearing steps are (i) c_μ = ⋀_n b_n ≠ 0, supplied by the
   **OML** hypothesis (a σ-complete lattice has countable meets)
   together with σ-additivity of μ; and (ii) order-separation supplies
   a σ-state charging c_μ. Neither step mentions the hub's descriptive
   complexity.

**Upshot:** the standardness hypothesis in §1 and in
`prop:ctbly-gen-full` is removable. Route (a)'s conclusion holds in the
full generality route (a) asks for.

## Recommended repo fixes (not yet applied)

- `notes/exposition/problem_state.tex` `prop:ctbly-gen-full`: the
  parenthetical justification is stated only for a *standard Borel*
  space, while the proposition claims full generality. Either restate
  the justification standardness-free via (1)+(2) above, or add the
  standardness hypothesis to the proposition. Currently the stated
  proof is narrower than the stated claim. (Exposition is marked
  read-only from the routes thread — flagging, not editing.)
- `problem_state.tex`: **"order-separate points" is used five times and
  never defined** (lines 339, 349, 431/456 variants, 643, 676). It is a
  hypothesis of `thm:ctbly-gen` and the defining feature of route (b),
  so it should carry a definition in §2 alongside `def:state`.

## Errors made and corrected this session (recorded per the standing lesson)

Two wrong claims were formed and killed before anything was written
into the repo; both are instances of the same standing lesson
(`feedback_verify_by_building`, and the handoff's own "read the proof,
not the statement").

1. **"`thm:ctbly-gen` is false, L₁ is the counterexample."** Wrong.
   `thm:ctbly-gen` hypothesizes an **OML**; L₁ is provably not one
   (`witness_carrier_not_lattice`). The "⋀_n b_n exists" step is not
   silently assumed — it is exactly the stated OML hypothesis. Lesson:
   **when probing an OML-hypothesized claim, the test object must be an
   OML.** L₁ is the OMP witness and is the wrong instrument.

2. **"c_μ = 0 for a one-row subalgebra of L₁."** Wrong arithmetic.
   Each Ulam row is **co-countable**, so its complement is countable
   and *nonempty*. Either one cell has μ-value 1 and c_μ is that cell,
   or all cells are 0 and σ-additivity forces the complement to value
   1. Either way c_μ ≠ 0, and `thm:ctbly-gen`'s conclusion holds for L₁
   as well. (The Lean file records the same co-countability point at
   `UlamWitnessLatticeGap.lean:39-40`: at M := ℕ the slab is countable
   and lands *in* the carrier, so uncountability of M is load-bearing.)

Neither error reached a repo file or a claim; both are logged because
the near-miss pattern (probing a lattice hypothesis with the poset
witness) is likely to recur.

## What this means for next steps

- **Route (a) as stated: do not hand-work it.** Its conclusion is
  proved. Reframe or drop.
- **Route (b) is now the only live direction** of the two, and the
  handoff's own assessment of it stands unchanged: the algebraic
  scaffolding exists (Navara–Rogalewicz 1991 Thm 4.11 + Prop 4.2(iii);
  Example 4.8 as a no-join hub template), and the entire open content
  is on the **state** side — arranging that no global σ-additive state
  assembles.
- The (a)/(b) partition was meant to be exhaustive. With (a)'s
  conclusion already proved, the honest statement of the frontier is:
  *countably-generated boundaries are closed; everything open is
  uncountably generated and turns on state non-assembly.*
