# Convex gluing systems: one framework for existence, uniqueness and location (draft 2026-11-06)

> ⚠ 2026-11-06 prior art: the framework definition is OWNED (Abramsky–Brandenburger; Kharoof–Okay 2025); strong T1 is FALSE (CHSH: no cohomological
> twist, no joint); T3 is OWNED (Fang–Santos; Fang–Seo). Surviving residue: R (ultrafilter holonomy on cyclic covers). **Restated T1 (T1 attempt):** no pointless state has a flat window family (= programme O1);
> proved ⟦HAND⟧ for triangle-free graphs; **open on the triangle with infinite alphabet.** See `CONVEX_GLUING_EQUILIBRIUM_GATES.md`.

reviewed: false. Machine-assisted (the user lifted the by-hand cap, 2026-11-06). Statements are drafts to be attacked. ⟦HAND⟧ marks unverified
arguments. Prior-art check and proof attempts are running (`CONVEX_GLUING_PRIOR_ART.md`, `CONVEX_GLUING_T1_ATTEMPT.md`).

## 1. Objects
- **Cover.** A set of sites I and a family 𝒞 of contexts C ⊆ I, closed under the intersections that occur, as a poset under inclusion.
- **Convex gluing system.** A contravariant functor K: 𝒞 → (convex sets, affine maps). Each K_C is a convex set (compact, or a closed cone) of *local states*;
  for C′ ⊆ C, π_{C→C′} : K_C → K_{C′} is affine ("marginalise"). Extended to the whole of I when the system comes from a global object: K_I with maps
  π_{I→C}.
- **Compatible families.** Comp = {(x_C) ∈ ∏ K_C : π_{C→C′} x_C = x_{C′}}, the limit over 𝒞.
- **Gluing map.** ρ : K_I → Comp, ρ(x) = (π_{I→C} x)_C. Each question is a property of ρ.
- **Ordinary points.** A distinguished subset P ⊆ ext(K_I) of "points": Dirac or principal states, i.e. states realised by an actual configuration.
  Other extreme points are **ideal**.

## 2. The three questions
- **Existence:** is x ∈ Comp in ρ(K_I)?
- **Uniqueness:** is the fibre F_x = ρ⁻¹(x) a singleton?
- **Location:** are the extreme points of F_x in P (ordinary) or ideal? x is **pointless** if F_x ≠ ∅ and F_x ∩ conv‾(P) = ∅.

## 3. Instances (owned)
| instance | K_C | gluing question | owners |
|---|---|---|---|
| marginal problem / contextuality | probability measures on the outcomes of C | existence; ε* = gauge distance | Vorob'ev; Abramsky–Brandenburger; DKC |
| latent-source covariance | cone FW_H pieces (positive decompositions; a *cosheaf* sum, not a restriction) | existence of a decomposition; V_H gauge | Kela et al.; Boman et al. |
| Gibbs measures | local specifications (DLR) | existence (compactness), uniqueness (phase transition), location (boundary conditions, tail-trivial extremes; the Gibbs set is a simplex) | Georgii; Föllmer |
| two-valued states on glued carriers | {0,1}-valued finitely additive states | location: pointless coherence | the programme; Atserias–Kolaitis (forest/loop) |
| consensus / infinite electorates | ultrafilters | location: ideal points (invisible dictator) | Kirman–Sondermann; Ulam |
| holonomy / calibration | group-valued (torsor) data | existence (cocycle closes); uniqueness up to gauge | geodesy; HodgeRank |

## 4. Target theorems
- **T3 (inference; essentially proved).** For any convex gluing system whose image ρ(K_I) is a closed convex cone containing the "local-noise" directions,
  with gauge γ (the support function of the dual), the test T = √n·γ(x̂) against the bootstrap quantile of γ(√n(x̂* − x̂)) has pointwise asymptotic
  size ≤ α, given bootstrap consistency for x̂. Proof: sublinear domination (`REACH_TEST_VALIDITY.md`, independently checked) is purely convex; nothing used
  correlations specifically.
- **T1 (twist–location; conjecture).** Call x **locally ordinary** if each x_C ∈ conv‾(P_C), i.e. each local view is a mixture of genuine local
  configurations. Define the **twist** of x as the obstruction to extending local points coherently around cycles of the cover (for {0,1}-states: the
  holonomy of the local-point choices; for signs: the ℤ₂ class).
  **Conjecture:** if x is locally ordinary and has trivial twist on every cycle of the cover (in particular, if the cover is acyclic), then F_x contains an
  ordinary global point (x is not pointless). Equivalently, pointlessness requires local ordinariness to fail or a non-trivial twist.
  - Consistency checks: consensus (no twist) gives ultrafilters, which are not locally ordinary when free, so T1 is not contradicted. Acyclic covers fall
    under the forest/loop dividing line (Atserias–Kolaitis; owned for the discrete case). The programme's pointless triangle needs a twisted cycle plus infinity.
  - Scope: finite alphabets make every finitely additive state σ-additive (compactness), so T1 has content only for infinite alphabets or infinite covers.
- **T2 (gauge–face; open question, not yet a conjecture).** How do (i) positivity of the existence gauge, (ii) non-uniqueness of the fibre and (iii) ideal
  extreme points relate through the face lattice of ρ(K_I)? Known cases: the gauge is positive only on frustrated supports (Boman); Gibbs non-uniqueness
  coexists with a simplex fibre whose extremes are tail-trivial. A general statement is not yet formulated.

## 5. What would make this a framework rather than a renaming
Theorems that link the three questions (T1, T2) and hold uniformly across instances. T3 alone is an inference result. Definitions alone are owned
(generalised probabilistic theories: state spaces as compact convex sets; Kadison duality; Choquet theory; sheaf contextuality).
