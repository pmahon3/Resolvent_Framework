# The finite-versus-countable discriminator: resolved FINITE (n=4)

Settles the open discriminator of `oml_onboarding.tex` §6 (Problem,
"Finite versus countable") and closes the singular-extension
sub-question on the extension axis. Companion to
[[lh_singular_dichotomy]] (which left it OPEN) and
[[singular_defect_tie_check]].

**Verdict.** A **finite** family — four infinite-dimensional,
pairwise-meet-zero subspaces — already forces Σ s(aᵢ) > 1 for *every*
state on L(H), singular included. So the singular case is a
**self-contained, finitary, operator-algebra-free** problem, separable
from the σ-wall. No singular state on L(H) extends to a charge on
S₀(L(H)). Verified in `lh_singular_finite_obstruction.py` (numerics) + primary
source for meet-preservation.

## The witness

H = H₀ ⊗ ℂ², H₀ infinite-dimensional. With ℂ²-basis e, f take four
infinite-dimensional subspaces (each ≅ H₀):

  a₁  = H₀ ⊗ ℂe        a₁^⊥ = H₀ ⊗ ℂf
  a₂  = H₀ ⊗ ℂ(e+f)    a₂^⊥ = H₀ ⊗ ℂ(e−f)

- **All six pairs meet-zero.** The two within-pair pairs are
  *orthogonal*; the four cross-pairs (a₁ vs a₂, a₁ vs a₂^⊥, a₁^⊥ vs a₂,
  a₁^⊥ vs a₂^⊥) are **meet-zero but NOT orthogonal** — this is the
  orthogonal/meet-zero gap doing the work. (Checked numerically.)
- **Pair-sums forced to 1, state-independent.** a_i ⊥ a_i^⊥ and
  a_i ∨ a_i^⊥ = H, so orthoadditivity gives s(a_i)+s(a_i^⊥)=s(H)=1 for
  *any* state — no σ-additivity, no normality. Hence
  Σ = s(a₁)+s(a₁^⊥)+s(a₂)+s(a₂^⊥) = 2.
- **Meet-zero ⟹ disjoint clopens.** MB filters are meet-closed +
  upward-closed ([[mb_primeness_check]] pt 2), so h(a∧b)=h(a)∩h(b) on
  all of F(A); meet-zero a∧b=0 ⟹ h(a)∩h(b)=∅. A charge on S₀ therefore
  forces Σ ≤ 1. Contradiction at Σ = 2.

This contradicts charge-extendibility (`oml_onboarding.tex` Def 2.7(3):
Σ s(aᵢ) ≤ 1 for every pairwise-meet-zero family) with n = 4. The
family is exactly **MO₂** with the atoms realised as infinite-dim
subspaces.

## Why this resolves the SINGULAR case (the load-bearing point)

The Σ=2 count itself is **folklore** — MO₂ admits no meet-zero→disjoint
charge by orthoadditivity + s(1)=1, MO₂ ⊂ L(ℂ²) already, and the Σ=2 is
already *state-independent* there (Kalmbach, *Orthomodular Lattices*
1983). The precise non-folklore content is NOT state-independence (it
holds in ℂ²) but **reaching the states that vanish on finite rank** — what
is load-bearing, and what was genuinely open, is the **realisation of MO₂
with infinite-dimensional atoms**:

- In L(ℂ²) the four atoms are **lines** (rank 1). A singular state
  annihilates all finite rank ([[lh_singular_dichotomy]] step 4), so it
  gives Σ = 0 there: **no obstruction**, and ℂ² carries no singular
  states anyway. The finite-dim count only bites states nonzero on
  finite rank = normal states = Prop 3.4 territory.
- Infinite-dimensional H₀ makes each atom infinite-dim, so
  orthoadditivity forces s(a_i)+s(a_i^⊥)=1 **regardless of behaviour on
  finite rank** — the obstruction now reaches singular states.

So infinite-dimensionality is essential, not cosmetic. (Verified
numerically: d₀=1 ⟹ rank-1 atoms ⟹ Σ=0 for singular; d₀=∞ ⟹ Σ=2 for
all.) This dissolves the apparent tension "why was it open if the count
runs in ℂ²?" — the count runs in ℂ² but does not touch singular states;
the infinite-dim version does. It is the same structure as last turn's
Prop 3.4 (lines in one 2-plane e₀, pair-sum s(e₀), needs k→∞, vacuous
for singular) vs. tensor (orthocomplement in all of H, pair-sum 1,
state-independent) reconciliation.

## Framing (per scout + verify-don't-narrate)

- **The count is folklore.** Cite Kalmbach (MO₂ non-extendability +
  orthoadditivity). Do **not** claim it as a new theorem.
- **The contribution is the application**: realising MO₂ with
  infinite-dim atoms so the obstruction reaches singular states,
  resolving the programme's open discriminator **negatively**. A modest
  **Type 5** (closes the singular-extension sub-question), via
  elementary means — neither "new result" nor "trivial."
- **Do NOT cite Kochen–Specker / Gleason.** The obstruction is to
  *meet-zero → disjoint* (which S₀ enforces via meet-closed MB filters),
  **not** to set-representability. MO₂ — hence L(H) — **is** a concrete
  logic / set-representable (Pták–Pulmannová 1991; witness X={1,2,3,4},
  a₁={1,2}, a₁^⊥={3,4}, a₂={1,3}, a₂^⊥={2,4}). Framing this as "L(H) is
  not concrete" would be a real error.
- **Unverified terminology flag.** The scout's "weakly Boolean" /
  Tkadlec attribution for the meet-zero≠orthogonality gap came from
  search snippets, not a primary read of ws95.pdf. Verify against
  source before naming Tkadlec in any writeup.

## Consequence for the programme

The extension axis is now **fully mapped on L(H)**: **no state extends,
full stop** — and the n=4 family alone proves it. The pair-sum
s(a_i)+s(a_i^⊥)=1 uses only orthoadditivity + s(1)=1; it never inspects
the state, so it kills *normal* states too (for normal s=tr(ρ·),
s(a₁)+s(a₁^⊥)=tr(ρ·I)=1 identically). **Prop 3.4 (the line-in-a-2-plane
argument, via Bunce–Wright/Takesaki) is therefore a now-redundant
special case for the extension question** — it reaches normal states
only (vacuous on singular), whereas n=4 reaches all states. Prop 3.4
survives only as an alternative technique of independent interest, not
as a needed step. The two residues confirmed independent in
[[singular_defect_tie_check]] are now both settled on the *extension*
side; the singular-extension branch is closed. The only remaining open
problem is the **descent axis** (the σ-Stone / Loomis–Sikorski engine,
`oml_onboarding.tex` §5) — and it is *not* reached by this construction
(finitary, no countable joins).

This also closes the hoped-for "extends-but-doesn't-concentrate"
witness ([[singular_defect_tie_check]]): no state extends at all, so
there is no candidate state whose descent behaviour is independent of
extension.
