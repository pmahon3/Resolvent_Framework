# Route (a): scope clarification — NOT redundant. Finding, 2026-07-20

*Session E5 follow-on, branch `e5-banking-audit`. Written before any
hand-work on route (a).*

**⚠ This file previously asserted that route (a) was redundant with
already-proved work. That claim was WRONG and has been retracted; the
error and its diagnosis are recorded in §4 below, because the
conflation it rests on is easy to repeat.*

## 1. Verdict

**Route (a) is open.** It is *not* closed by `thm:ctbly-gen`
(`problem_state.tex` §3.3) nor by Campaign 12
(`oml_omega1_cylinder_hub.md` §1, 2026-07-14). The 2026-07-20
handoff's instruction "attack route (a) first" stands.

What §1 and `thm:ctbly-gen` *do* close is a **strictly weaker**
statement. Keeping the two apart is the content of this note.

## 2. The two configurations, which are different

| | `thm:ctbly-gen` / Campaign 12 §1 | Route (a) |
|---|---|---|
| Carrier piece | **one** Boolean σ-subalgebra `A` | **two** blocks sharing a hub |
| Fragment location | witness confined to / embedded in `A` | fragment `B ⊄ A`, spans both blocks |
| State hypothesis | **a σ-state μ on `A`** | witness is only *finitely* coherent |
| Conclusion | every σ-state on `A` extends to `L` | ? two-cell mechanism forbids the hub |

**Closed (weaker):** a witness confined to a countably-generated
faithful separating piece extends. Indeed for a fragment `B ⊆ A` with
`A` Boolean, `prop:amendment` already hands back a Dirac extension
directly.

**Open (route (a)):** whether `prop:finite-obstruction`'s two-cell
countable-meet mechanism forbids every countably-generated hub *shared
between two blocks*. Here the witness pattern is **not** contained in
the hub — the two-cell mechanism has one decreasing sequence `(U_n)`
sent to *different* points `i ≠ j` by the two faithful embeddings, so
the fragment draws on elements of both blocks.

"σ-states on a countably-generated hub extend" does **not** imply "no
σ-essential witness has a countably-generated shared hub." The first
quantifies over σ-states of the hub; the second is about a
cross-block fragment that need not induce one.

## 3. Why the hypothesis genuinely fails to engage (the discriminating check)

The check that decides it: *on a countably-generated separating hub
shared between two blocks, is the witness's finitely additive `m`,
restricted to the hub, forced to be σ-additive?*

**No — and this is the crux.** A σ-essential state is by definition
only **finitely coherent** (`def:essential`): the global state `m`
witnessing coherence is *finitely* additive. In `thm:main`'s witness
`L₁`, `m` is a non-principal ultrafilter state, and it is provably not
σ-additive — that is exactly what lets `m(A) = m(B) = m(C) = 1` while
`A ∩ B ∩ C = ∅`.

`thm:ctbly-gen` hypothesizes "**μ a σ-state** on `A`." A cross-block
witness need supply no σ-state on the hub whatsoever. So the theorem's
hypothesis is not met, and §1's operative move — "fix the hub σ-state
and extend it into every cell" — never engages: there is no hub
σ-state to fix.

Route (a) is precisely the question of whether *shrinking the shared
hub to countably generated* kills the two-cell disagreement. That is a
genuine open question about the **mechanism**, and it is what
`prop:finite-obstruction` was built for and what route (a) asks to
generalize. `thm:ctbly-gen` does not reach it.

Note also that `prop:finite-obstruction` mentions **no state at all** —
it is a purely structural claim about the ambient countable meet being
computed once. That alone distinguishes it from the state-hypothesised
`thm:ctbly-gen`.

## 4. The error this file originally made (recorded, per the standing lesson)

The retracted claim was: "route (a)'s conclusion was already proved on
2026-07-14, six days before the handoff scoped it as open."

**Diagnosis — conflating two configurations.** The reasoning treated
"countably-generated hub" as the only salient feature and matched it to
`thm:ctbly-gen`'s "countably generated `A`", without checking that the
*fragment location* and the *state hypothesis* also matched. They do
not: single-piece-confined vs two-block-spanning, and σ-state-given vs
only-finitely-coherent. The redundancy was not merely a different proof
route to the same conclusion — **the conclusions themselves differ.**

**Why it survived initial scrutiny.** A real sub-result was proved
along the way (standardness-removability, §5) and its correctness lent
unearned confidence to the surrounding claim. A true lemma adjacent to
a false thesis is the dangerous configuration.

Two further errors were caught and killed earlier in the same session,
both from probing an **OML**-hypothesized claim with the **non-OML**
witness `L₁` (`witness_carrier_not_lattice`):

- *"`thm:ctbly-gen` is false, `L₁` refutes it."* Wrong — `L₁` is not an
  OML, so it is out of scope. The "`⋀_n b_n` exists" step is not
  silently assumed; it is the stated OML hypothesis.
- *"`c_μ = 0` for a one-row subalgebra of `L₁`."* Wrong arithmetic —
  each Ulam row is **co-countable**, so its complement is countable and
  nonempty; `c_μ ≠ 0` either way. (`UlamWitnessLatticeGap.lean:39-40`
  records the same co-countability dependence.)

**Standing lesson, thrice-instantiated this session:** *check that every
hypothesis matches before concluding a theorem applies* — the carrier
type (OML vs OMP), the fragment's location (inside the piece vs
spanning blocks), and the state's additivity (σ vs merely finite).
Matching one salient noun is not matching the hypothesis.

## 5. A genuine side-result: standardness is removable

Not the crux, but proved and worth keeping.

Campaign 12 §1's argument opens *"For a standard Borel hub…"* and
invokes Lusin–Souslin, which needs standardness; route (a) grants none.
Non-standard countably-generated separating hubs do exist: such an
`(X,𝒜)` embeds injectively into `2^ω` via `x ↦ (1_{A_n}(x))_n` but is
standard only if the image is Borel — a Bernstein or
analytic-not-Borel image gives a non-standard instance.

The standardness hypothesis is nonetheless removable from
`thm:ctbly-gen` / `prop:ctbly-gen-full`:

1. **Singletons come free from separation alone.** If `(A_n)` separates
   points, then `{x} = ⋂_n B_n` with `B_n := A_n` or `A_n^c` per `x`'s
   membership — a *countable* intersection, hence in the σ-algebra. No
   Lusin–Souslin. Standardness in §1 buys the strictly stronger "the
   generated algebra is the *full* Borel algebra," more than the
   puncture obstruction consumes.
2. **The multi-piece case collapses to the single-piece case.**
   `prop:ctbly-gen-full` combines *countably* many pieces; a countable
   union of countable generator sets is countable, so the join is again
   countably generated, and joint separation makes it separating.
3. **`thm:ctbly-gen`'s own steps are standardness-free:** `c_μ ≠ 0`
   comes from the **OML** hypothesis (σ-complete lattice ⇒ countable
   meets) plus σ-additivity of `μ`; order-separation then supplies the
   charging σ-state. Neither mentions descriptive complexity.

This strengthens the weaker, already-closed statement. It does not
touch route (a).

## 6. Repo defects flagged (not edited — exposition is read-only from this thread)

- `prop:ctbly-gen-full`: the parenthetical justification is stated only
  for a *standard Borel* space while the proposition claims full
  generality — the stated proof is narrower than the stated claim.
  Either restate it standardness-free via §5, or add the hypothesis.
- **"order-separate points" is used five times and never defined**
  (lines 339, 349, 456, 643, 676). It is a hypothesis of
  `thm:ctbly-gen` and the defining feature of route (b); it needs a
  definition in §2 beside `def:state`.

## 7. Next steps (unchanged from the handoff)

Route (a) first, as the handoff directs, with §2–§3 above as the
sharpened target: the open content is whether the **two-cell
countable-meet mechanism** forbids a countably-generated hub *shared
between two blocks*, where the witness supplies no hub σ-state. Then
route (b).
