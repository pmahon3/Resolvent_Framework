# L₂ state space: the dispersion-free / homomorphism separation (2026-06-10)

> **KILLED 2026-06-10** (`/audit full`, hostile referee, primary-source-
> verified). Clears no contribution-type bar — 5th death on the
> decorative-σ-additivity rock. The math is correct (verified-by-building);
> the *contribution* is not novel: df-state ≠ 2-valued homomorphism on MO₂
> is textbook (Kalmbach 1983, Pták–Pulmannová), σ-additivity is free here
> so L₂ is decorative packaging on a finite MO₂ fact, and the only genuine
> output — the Paper II §5 line-304 fix — is an already-applied internal
> bug-fix, not a contribution. Full audit + disposition in the companion
> kill-note: `l2_dispersion_free_homomorphism_separation.md`. Original seed
> body preserved below verbatim for the record.

**Status: VERIFIED by building (Python, elementary), reconciled against Paper II.**
This is the output of the post-★ reorientation: scouting the finite→limit
degeneration of *states* (Limit 2) after ★ settled the *lattice* limit (Limit 1).

## The pressure test and what it found

After ★ locked (L₂ exercises descent — the meet-zero≠orthogonal **gap** survives
to the infinite limit object), the next question was the programme prize: a
**point-free σ-additive probability theory on L₂** (Q1). Pressure-testing
"PR-survival is the open question" by building the finite state space
(`l2_states.py`, `verify_mo2_state.py`):

> *(Script locations, after the 2026-06-11 archive sweep: `verify_mo2_state.py`
> is in `open_questions/verification/`; `l2_states.py` and `diag_hom.py` moved to
> `archive/oml_descent_inhabitation_dead/` with the dead L_MO₂ lead.)*

**L₂ has a separating family of σ-additive, dispersion-free (2-valued) states** —
the per-block **evaluation states** `s_{m,σ}(f) = σ(f(m))`, σ a 2-valued MO₂
state. Each:
- is a genuine **state** (additive on every orthogonal pair, normalized) ✓
  (verified exhaustively on MO₂, `verify_mo2_state.py`);
- is **dispersion-free** (`s(x) ∈ {0,1}` for all x) ✓;
- is **σ-additive** (the evaluation only sees one block; an ∞ disjoint-support
  join has ≤1 nonzero term per block — and cap-at-2 keeps within-block joins
  finite) ✓;
- assigns the infinite witness `p = ⋁ₙ b|Cₙ` a **definite value** `σ(b) ∈ {0,1}`
  ⟹ **σ-additive states DO concentrate on physical points**.

So L₂ is **concrete and point-FUL** — which is no surprise: MO₂ was chosen
*because* concreteness lifts for free (the ★ design choice). Concrete ⟹
separating 2-valued states = points.

## The separation (the real finding) — corrects a Paper II conflation

These dispersion-free states are **NOT 2-valued homomorphisms.** And **L₂ admits
no homomorphism at all** — but note this does NOT follow from "MO₂ has none" by
itself (the W-vs-L subtlety: a block copy `U_C` has top `1_C ≠ ⊤`, so a
homomorphism could sit at `0` on that whole block and dodge the block's gap).
The clean argument is the **DIAGONAL** copy (`diag_hom.py`, verified): the
constant functions `{⊥, c_a, c_a', c_b, c_b', ⊤}` (`c_x(n)=x ∀n`) form a sub-OML
of L₂ with **global** top/bot (`c_⊤=⊤`, `c_⊥=⊥`), closed under coordinatewise
ops, on which the gap survives (`c_a∧c_b=⊥`, `c_a⊀c_b'`). Any homomorphism
`h:L₂→{0,1}` restricts to a homomorphism on this MO₂-copy — and MO₂ has none
(gap pair `a∧b=0`, `s(a)=s(b)=1` ⟹ `s(a∧b)=0≠1`; the `point 1∈a∩b` case of
`concrete_meetzero_vs_orthogonal.py`). `decide`-reducible to the same MO₂ fact,
NO lift needed. So:

| Property | Boolean | L(H) dim≥3 | **L₂ (MO₂-blocks)** |
|---|---|---|---|
| 2-valued **homomorphism** | plentiful | **none** (KS) | **none** (gap) |
| dispersion-free **state** | = homomorphism | **none** (Gleason) | **YES** (eval states) |

On Boolean and on L(H), the two rows **coincide** (both full / both empty). **On
L₂ they bifurcate**: dispersion-free states exist, none is a homomorphism. This
is the [[oml_two_point_spaces]] equivocation resurfacing on a new axis
(state-level, not point-level).

**L(H) gets homomorphism-freeness VIA state-poverty (KS/Gleason kill all
dispersion-free states). L₂ gets homomorphism-freeness VIA the gap, while
KEEPING a rich separating σ-additive state space — no KS needed.** That is the
genuinely new structural fact.

## Reconciliation with Paper II strata (the requested pass)

Three properties were fused under "point-free / VDR / concentrate on points";
they come apart on L₂:
1. **dispersion-free state** (definite values, additive-on-orthogonal-pairs);
2. **2-valued homomorphism** (multiplicative on ALL pairs = consistent global
   truth-valuation);
3. **concentration on principal filters P(A)** (mass on physical points).

Paper II §5 line 304 stated "a dispersion-free state **is** a 2-valued
homomorphism" — **false in general**, L₂ is the counterexample. The paper's own
Remark (after Cor. distributivity) already had the correct sharp characterization
(VDR ⟺ admits a dispersion-free state), and all downstream machinery uses
`S_df(A)`, so the conflation was **expository, not load-bearing**. **FIXED
2026-06-10** (3 edits to `distributivity_and_realism_body.tex`: VDR def line 79,
the line-304 identification, the line-615 horizontal-sums sentence; compiles
clean, 11pp). Operative VDR = dispersion-free state; "homomorphism" is the
strictly-stronger notion that coincides only on Boolean/L(H).

## Two prizes, two objects (user decision 2026-06-10)

"Point-free σ-additive probability" was conflating two readings:

- **Strict point-free** = no dispersion-free points. **L₂ FAILS this** (concrete
  by design ⟹ point-ful). Strict point-freeness lives in the **non-concrete**
  regime — L(H)/Navara, where state-poverty kills the points ("richness starves
  concreteness" — that arc is about THIS prize).
- **Homomorphism-free** = no global 2-valued homomorphism ⟹ probability
  irreducible to a classical truth-valuation. **L₂ DELIVERS this**, without KS,
  with a rich separating σ-additive state space.

**Decision: both are real, distinct objects.** The contribution is the
**SEPARATION** — L₂ splits dispersion-free from homomorphism (which L(H)/Boolean
fuse) — a Paper II §5 refinement, NOT a single prize. L₂ witnesses
homomorphism-free-but-point-ful; L(H) witnesses strict-point-free-via-poverty.

## Open / next

- The separation is a candidate **Type-4 (vocabulary) / §5-refinement**
  contribution — needs the standard audit before any claim. NOT yet audited.
- The strict-point-free prize (if still wanted) requires a NON-concrete
  σ-orthocomplete OML — a different object than L₂. Open whether one exists that
  *also* exercises descent (★) without inheriting L(H)/Navara's state-poverty
  mechanism wholesale.
- Lean: the dispersion-free-state / not-homomorphism separation is `decide`-able
  on MO₂ — could add to the descent-witness suite as a state-level companion to
  the lattice-level ★, if the separation is pursued as a contribution.

Scripts: `l2_states.py`, `verify_mo2_state.py` (both elementary, self-checking).
Primary: Paper II body §5 + Remark; `concrete_meetzero_vs_orthogonal.py`;
Kalmbach 1983 Ch.4 (dispersion-free states on horizontal sums).
