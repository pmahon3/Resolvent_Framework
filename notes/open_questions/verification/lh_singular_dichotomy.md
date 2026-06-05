# The singular/normal dichotomy for states on L(H) — hand-verified

Supporting entry point #1. This is the analytic companion to
`lh_infinite_extension.py`: the clustering argument (Prop. in the note)
kills every state with `s(e) > 0` on some finite-dim `e`; this note
verifies that the *only* escapees are the singular states, and that
"detected by a finite-rank projection" vs. "purely singular" is a clean
dichotomy with no third class.

**Verification policy (per repo rule "verify LLM proofs independently"):**
the two deep inputs — Mackey–Gleason/Bunce–Wright and Takesaki's
normal/singular decomposition — are textbook-settled and not in Mathlib;
re-proving them in Lean would be a multi-week sink for no gain. So they
are used as **cited black boxes with their hypotheses checked in this
setting**, and the *gluing* (steps 3–4) is hand-verified. This is the
correct scope of the rule: verify the assembly, not the foundations.

## Standing assumptions

- `H` separable, `dim H = ∞`. (Separability is needed for the
  ultrafilter-basis construction of a singular state below; the Calkin
  construction does not need it. State separable as the ambient setting.)
- `dim H ≥ 3` and, equivalently here, `B(H)` has **no type I₂ summand**
  — `B(H)` is type I_∞. This is the same hypothesis that gates Gleason,
  and it is load-bearing for step 1.

A *state* on `L(H)` is `s : P(H) → [0,1]`, `s(I)=1`, finitely
orthoadditive: `s(p ∨ q) = s(p) + s(q)` when `p ⊥ q`. It is bounded
(by 1).

## The chain

**Step 1 — lattice state → bounded positive functional φ on B(H).**
*Mackey–Gleason / Bunce–Wright* (Bunce–Wright, Bull. AMS 26 (1992);
Christensen, Comm. Math. Phys. 86 (1982) for the bounded-vN precursor).
Hypothesis: the vN algebra has **no type I₂ direct summand**. `B(H)`
(dim ∞) is type I_∞, so this holds. A bounded finitely-additive measure
on `P(B(H))` extends *uniquely* to a bounded linear functional `φ` on
`B(H)`; positivity on projections gives a positive `φ`, and `s(I)=1`
gives `φ` a state. **Hypothesis checked. ✓**

(Caveat preserved: "annihilates `K(H)`" is only meaningful *after* this
lift — compacts are not projections, and a bare lattice state is not a
priori linear on operators. All operator-level statements below are
about `φ`, not `s` directly.)

**Step 2 — φ = φ_n + φ_s, both positive, φ_s annihilates K(H).**
*Takesaki normal/singular decomposition* (Theory of Operator Algebras I,
Ch. III). For a positive functional on a vN algebra the decomposition
into normal part `φ_n` and singular part `φ_s` is unique and **both
parts are positive**. For `B(H)` the singular functionals are exactly
those annihilating the compacts `K(H)` (the unique closed two-sided
ideal). Invoke the **positive-functional** version (not merely the
Banach-space splitting) — positivity of both parts is what licenses
step 4. **✓**

**Step 3 — φ_n = tr(ρ·) with ρ ≥ 0 trace-class.** This is **predual
duality**, NOT Gleason: `B(H)_* = ` (trace-class operators), and normal
positive functionals correspond to positive trace-class `ρ`. (Do not
attribute this to Gleason — Gleason is the separate fact that *every*
σ-additive lattice state is normal; here we already have a normal
functional and just name its density.) **✓**

**Step 4 — the dichotomy (hand-verified, elementary).**
Claim: `s(e) = 0` for every finite-dim `e` ⟺ `ρ = 0` ⟺ `φ` is singular.

- (⇐) If `ρ = 0` then `φ = φ_s` annihilates `K(H)`; finite-rank
  projections are compact, so `s(e) = φ(e) = 0` for all finite-dim `e`.
  Trivial.
- (⇒) Suppose `s(e) = 0` for every finite-dim `e`. Since `φ_s(e) = 0`
  (finite-rank ⊂ compact), `s(e) = φ(e) = φ_n(e) = tr(ρ e)` for every
  finite-rank projection `e`. Take `e = e_ξ`, the rank-one projection
  onto a unit vector `ξ`: `0 = tr(ρ e_ξ) = ⟨ρ ξ, ξ⟩`. This holds for
  **all** unit `ξ`. A self-adjoint (indeed positive) operator with
  `⟨ρ ξ, ξ⟩ ≡ 0` is `ρ = 0` (the quadratic form is identically zero ⟹
  the operator is zero, by polarization). Hence `φ_n = 0`, i.e. `φ` is
  singular. **✓**

- **No third class.** "Detected by a finite-rank projection"
  (`∃ e finite-dim, s(e) > 0`) ⟺ `φ_n ≠ 0` ⟺ `ρ ≠ 0`. Its negation is
  exactly "purely singular." The decomposition `φ = φ_n + φ_s` is
  *unique* (Takesaki), so every state lands in exactly one of the two
  classes. There is no third option. **✓**

## Consequence for entry point #1

The clustering argument (`lh_infinite_extension.py` / the note's
Proposition) kills exactly the "detected" class — every state with
`s(e) > 0` for some finite-dim `e`, which includes **every normal
(Gleason) state**, since `ρ ≠ 0 ⟹ ⟨ρ ξ, ξ⟩ > 0` for some `ξ ⟹
s(e_ξ) > 0`. The purely singular states sit precisely in the argument's
blind spot (`s(e) = 0` makes the bound `k·s(e) ≤ 1` vacuous). So:

- **No normal state on L(H) extends.** (clustering + this dichotomy)
- **Singular orthoadditive states exist** — two constructions:
  - *Ultrafilter vector state:* fix an orthonormal basis `(e_n)` and a
    free ultrafilter `ω` on `ℕ`; `φ(a) = lim_ω ⟨a e_n, e_n⟩` is a state;
    for compact `k`, `e_n → 0` weakly so `φ(k) = 0`; restrict to `P(H)`.
    (Needs `H` separable.)
  - *Calkin pullback:* the Calkin algebra `Q = B(H)/K(H)` is unital,
    nonzero, hence has states; pull any back along `π : B(H) → Q`; it
    annihilates `K(H)` by construction.
- **Whether a singular orthoadditive state extends: now SETTLED — it
  does not** (resolved 2026-06-05, [[lh_singular_finite_obstruction]]).
  The relevant pairwise-meet-zero families are *infinite-dimensional*
  subspaces with trivial intersection (not lines), as anticipated here.
  A **finite** such family (n=4: MO₂ realised as H₀⊗ℂ² with infinite-dim
  atoms) forces Σ s(aᵢ)=2>1 by orthoadditivity alone, contradicting any
  charge — *no* singular state extends. The discriminator
  (`oml_onboarding.tex` §6) thus resolves **FINITE**: the singular case
  is self-contained and finitary, separable from the σ-wall. The count
  is folklore (Kalmbach MO₂); the application — infinite-dim atoms to
  reach singular states — is what was open.

## What is verified vs. cited

- **Cited black boxes, hypotheses checked in-setting:** Mackey–Gleason/
  Bunce–Wright lift (no-I₂, holds for B(H)); Takesaki normal/singular
  decomposition (positive version); predual duality `B(H)_* =` trace
  class.
- **Hand-verified here:** the gluing (step 4), the `ρ = 0` argument via
  rank-one projections + polarization, uniqueness ⟹ no third class, and
  that normal ⟹ detected.
- **Not attempted (correctly):** Lean formalization of the foundations
  (textbook-settled, not in Mathlib); resolving the singular-extension
  sliver (genuinely open).
