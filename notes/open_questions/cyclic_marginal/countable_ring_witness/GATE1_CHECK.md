# Gate 1 check: independent verification of GATE1.md (2026-10-27)

reviewed: false. Fresh-eyes check, hostile to both sides. Hand steps marked ⟦HAND⟧. Machine answer key:
`/tmp/g1check/states.py` (scratch, not kept; described in §4). No Lean. Nothing else edited.

## Verdicts

1. **Correctness: W★ is CORRECT.** Every claimed property re-derived from scratch; no error found. One
   factual slip in GATE1 §3 (σ-generation is *not* a ring-only feature; see §3 below) and one missing
   check (block disjointness; supplied in §1.5).
2. **Routine: NEW CONSTRUCTION.** Outcome A does **not** stand. Every mechanism the pre-registration lists
   fails on countable Ω (GATE1 §1 itself proves this, and that failure is literally the Outcome-B reason).
   W★ succeeds through a gluing that is not on the list (a carrier cut out by a linear parity code over
   ⊕_ℕ𝔽₂, read through a Bohr-null ultrafilter) and needs a new rigidity argument (singleton-free Dirac
   step). Effective outcome: **C** (Type 1 of "a countable literally irreducible witness exists" UNCLEAR;
   W★ joins the ring as a second candidate for Gate 2). Counterweight stated in §2.
3. **Redundancy: partial.** W★ makes the ring redundant for the bare existence claim only. They differ in
   mechanism (composition vs circle), see §3.

---

## 1. Correctness of W★ ⟦HAND⟧

Notation as GATE1 §2: G = ⊕_{j∈ℕ}𝔽₂ (finite subsets of ℕ under Δ), G* = G∖{0}, F = {1,2,3,4},
Ω = G*×F, p_E(g) = |E^g| mod 2, χ_y(g) = |g∩y| mod 2 for y ⊆ ℕ arbitrary,
D = {E : p_E = χ_y|_{G*} for some y}. Lean's carrier type is Mathlib's `DynkinSystem` (∅, complement,
ℕ-indexed pairwise-disjoint unions); `Irreducible d` = every `Centre d E` is ∅ or univ, with
`Centre d E` = E ∈ d ∧ ∀A ∈ d, E∩A ∈ d (`Admissibility.lean` l.~56, 161).

**1.1 D is a Dynkin system. CORRECT.**
- ∅, Ω: pattern 0 = χ_∅. Complement: |F| = 4, so fibre parity is preserved.
- Countable disjoint union E = ⊔_k E_k with p_{E_k} = χ_{y_k}. At each g the E_k^g are disjoint subsets of
  a 4-set, so at most 4 are nonempty; for the others p_{E_k}(g) = 0, i.e. χ_{y_k}(g) = 0. So
  φ(g) := Σ_k χ_{y_k}(g) is a pointwise-finite sum and equals p_E(g). Set φ(0) = 0.
- φ is a homomorphism G → 𝔽₂: for g, h, the sums at g, h, g+h involve finitely many nonzero terms, and
  termwise χ_{y_k}(g+h) = χ_{y_k}(g) + χ_{y_k}(h); g = h gives φ(0) = 0. ✓
- Every homomorphism ⊕_ℕ𝔽₂ → 𝔽₂ is χ_y with y = {j : φ({j}) = 1}, **y arbitrary** (the dual of ⊕ is ∏).
  This is exactly why y must range over all of P(ℕ): with y finite only, D would not be σ-closed.
  GATE1 has this right.
- Also closed under Δ (patterns add), so D is a σ-complete symmetric logic.

**1.2 Countable Ω, concrete, no singletons, not intersection-closed. CORRECT.**
G* countable. e_g (1 at g only) is not a character: pick h ∉ {0, g}; then χ(g+h) = χ(g)+χ(h) = 1 but
g+h ∉ {0, g}. So no singleton {(g,a)} lies in D. A₁∩A₂ = G*×{1} has the all-ones pattern, not a character.

**1.3 Ultrafilter. CORRECT.** For y ≠ ∅, χ_y ≠ 0 (it is 1 at {j}, j ∈ y). Finitely many kernels meet in a
finite-index subgroup of the infinite G, which is infinite; so the sets Z(y₁…y_k)∖{0} plus the cofinite
sets have the FIP. U exists, is free, and contains {χ_y = 0} for every y. Hence every E ∈ D has
U-almost-all fibres even.

**1.4 m is a `FinAddState`. CORRECT.** On 4even, t (1 on F, 12, 13, 23) is a two-valued state: the only
disjoint pairs with both members nonempty are complementary pairs, and t picks one of each.
m(E) = 1 iff {g : E^g even, t(E^g) = 1} ∈ U. For E, E′ ∈ D disjoint, E⊔E′ ∈ D; on a U-set all three
fibres are even, the sets {t(E^g)=1} and {t(E′^g)=1} are disjoint there and their union is
{t((E⊔E′)^g)=1}; an ultrafilter contains a disjoint union iff it contains exactly one part. Complement
likewise. ✓

**1.5 Block, local state, kernel. CORRECT (check added).** A_i = G*×P_i (P₁=12, P₂=13, P₃=23), pattern 0.
B = {A_i, A_iᶜ} is a `Block` (finite, in D, complement-closed). Any two non-complementary members meet
(each pair of P_i, P_jᶜ etc. share a point of F), so the only disjoint pairs in B are complement pairs:
`LocalState` (complement-additivity only) is not dropping a constraint. m extends s₀ (t(P_i) = 1 on every
fibre). Kernel = G*×(P₁∩P₂∩P₃) = ∅. ✓

**1.6 Every σ-additive two-valued state on D is Dirac. CORRECT.** This is the only step with real content.
- (i) The fibres {g}×F (pattern 0) are a countable disjoint cover of Ω; `val_iUnion` makes exactly one true,
  g₀. This is the **only** use of σ-additivity.
- (ii) Any pattern-0 set supported off g₀ is in D and false (subset of the false (G*∖{g₀})×F; monotonicity
  in a Dynkin system uses B∖A = (Bᶜ⊔A)ᶜ ∈ D).
- (iii) Locality. From E ∈ D with pattern χ and fibre X at g₀, reach C(χ,X) = {g₀}×X ∪ ⋃_{g≠g₀, χ(g)=1}{g}×{1}
  by three global moves: remove an even-fibred subset (leaving fibres ∅ or a singleton {a_g}); add a
  disjoint {1,b_g} (b_g ∉ {1,a_g}) where a_g ≠ 1; remove {a_g,b_g}. Each moved set is pattern-0 off g₀,
  hence in D and false by (ii); removal is a proper difference, addition a disjoint union. All
  intermediates have pattern χ. So s(E) = Σ(χ,X) := s(C(χ,X)). ✓
- (iv) Σ(χ+χ′, X⊔X′) = Σ(χ,X) + Σ(χ′,X′) whenever X∩X′ = ∅, |X| ≡ χ(g₀), |X′| ≡ χ′(g₀): off g₀ choose
  disjoint subsets of F with parities χ(g), χ′(g) (sizes ≤ 1 each). Σ(χ,∅) = 0 by (ii). ✓
- (v) Fix y = {j}, j ∈ g₀. μ(X) = Σ(0,X) (X even), Σ(χ_y,X) (X odd). The three parity cases of (iv) give
  additivity on P(F) (odd⊔odd uses χ_y+χ_y = 0); μ(F) = s({g₀}×F) = 1. A two-valued additive state on the
  finite Boolean algebra P(F) is δ_f. ✓
- (vi) For χ(g₀) = 0: Σ(χ,X) = Σ(χ,∅)+Σ(0,X). For χ(g₀) = 1: Σ(χ,X) = Σ(χ+χ_y,∅)+Σ(χ_y,X). Both = δ_f(X).
  So s(E) = δ_f(E^{g₀}) = [(g₀,f) ∈ E]. ✓

**1.7 σ-essential, NonSegregated. CORRECT.** By 1.4–1.6, `FinitelyCoherent s₀` and no σ-state extends
(every σ-state is Dirac; kernel empty; `no_dirac_extends_iff_kernel_empty`). `IsSigmaEssential s₀` holds;
`NonSegregated` by `witness_nonSegregated`; `¬InterClosed` and the conditional Polish clause are forced by
the witness exactly as for D₄.

**1.8 Literal irreducibility. CORRECT.** E central. Meet with {g}×{a,b} (pattern 0): pattern
e_g·|E^g∩{a,b}|, so |E^g∩{a,b}| is even for every pair, forcing E^g ∈ {∅, F}; E = S×F. Meet with
O_j = {(g,1) : j ∈ g} (pattern χ_{{j}}): pattern [j∈g]·1_S(g) must be a homomorphism f_j. For h, h′ ∋ j,
h+h′ ∌ j so f_j(h+h′) = 0 and f_j(h′) = f_j(h). So 1_S is constant on {g ∋ j}; these families pairwise
overlap ({j,k}) and cover G*, so S ∈ {∅, G*}. ✓

**1.9 GATE1 side claims.** §1(a) (D_I σ-class ⟺ I σ-ideal; σ-ideals on countable sets are principal) and
§1(b) first form (common parity ⇒ restricted ultrafilter, nonempty kernel) re-derived: correct. §1(c) not
re-checked in full; it is not load-bearing.

## 2. Routine or new? ⟦HAND judgement⟧

The pre-registration names a **route** ("Binder–Navara + 4-point-fibre construction, or any routine
variant: other finite non-Boolean fibres, ultrafilter limits, product/sum of logics"), not a difficulty
level. Test: replace W★'s gluing by each listed mechanism and see whether any step survives.

| Ingredient of W★ | Standard? | Source |
|---|---|---|
| 4even fibre + free state t | standard | Pták (free hidden variables, CMUC 1987); Navara–Pták 1983 finite shadow |
| ultrafilter limit of a fibre state | standard | Binder–Navara PAMS 1987 (and `psi_ZFC`) |
| finite-index kernels have FIP; ultrafilter extending them (Bohr-null U) | standard group theory | folklore |
| **carrier = sets whose fibre-parity pattern is a character of ⊕_ℕ𝔽₂** | **not on the list** | no source located (Gate 2) |
| **σ-closure via pointwise-finite sums in the dual ∏𝔽₂** | new use of a standard duality | — |
| **Dirac rigidity without singletons (1.6 iii–vi)** | **new**; GATE1 itself says so (B–N step 5 needs singletons) | — |
| literal-centre argument (1.8) | short, new for this carrier | — |

- Every listed mechanism provably fails on countable Ω: ideal exceptions collapse to principal (§1(a), the
  exact Outcome-B reason pre-registered); products and sums are reducible or not σ-essential (§1(c));
  common-parity gluing has a nonempty kernel (§1(b), first form). The listed ingredients survive only as
  the fibre and the limit; the **gluing** and the **rigidity proof** are new.
- Length: about 1.5 pages of elementary hand proof (1.1–1.8 above), of which the rigidity step is about half.
- "Elementary and short" is not "routine variant of the named route". Calling W★ routine would stretch the
  pre-registered list after the fact, which is the mirror image of rescue by framing.

**Verdict: NEW CONSTRUCTION.** Outcome A does not stand. Read literally, the listed route fails for the
structural reason Outcome B anticipated; but since a new countable witness *does* exist (ours), the honest
reading for Type 1 of the existence theorem is **Outcome C: UNCLEAR → Gate 2**, now with two candidates
(ring, W★).

**Counterweight (hostile to this verdict).** W★ is a σ-complete symmetric logic with a free two-valued
state, a short elementary object squarely inside the De Simone–Navara–Pták / Bikchentaev school's
territory. It may well be printed (or an obvious exercise there). DNP 2015 (SHELF_INDEX l.~3043, read) does
not contain it: Thm 3 is finite, Thms 4–6 are positive extension results (Thm 5: Ω countable, card S = ℵ₁,
σ-states countably carried, hence extend), and Thm 1 needs Δ-subadditivity, which t violates
(t(34 Δ 24) = t(23) = 1, t(34) = t(24) = 0). Gate 2 must search Bikchentaev–Navara 2016, Bikchentaev–Yakushev
2014 (Problem 7.2), Bikchentaev 2009, Sultanbekov, Ovchinnikov 1994a for W★ or a near relative. If found,
both W★ and the ring's existence claim lose Type 1.

## 3. Does W★ make the ring redundant?

Only for the bare statement "a countable, literally irreducible σ-essential witness exists". GATE1 §3 lists
"it σ-generates P(ℕ⁴)" as a ring-only feature; **that is wrong**: W★'s D also σ-generates P(Ω)
({g}×{a,b} ∩ {g}×{a,c} = {(g,a)}). The real difference is where non-Booleanness and the empty kernel come
from. In W★ they are **imported**: a finite non-Boolean fibre (4even, an owned finite shadow) carries the
Specker triple, copied identically into every fibre, and infinity (the code + Bohr-null ultrafilter) serves
only to kill the σ-states. It is a composition. In the ring every window is Boolean (P(ℕ²)), the carrier is
the programme's own coordinate pair-window object on ℕ^L, and the empty kernel arises only from gluing
those Boolean views round a cycle (the order kind of twist, note §9); acyclic window graphs give none. So
the ring is a circle. If the programme's claim is "cycle × infinity is where pointless coherence lives",
W★ shows countability alone does not need the cycle, while the ring remains the instance where neither
the fibres nor the windows are non-Boolean. That difference is a theory statement for the glued-carriers
collection, not a Type 1 claim.

## 4. Machine answer key (scratch, finite slice; says nothing about σ)

`/tmp/g1check/states.py`: G = 𝔽₂²∖0, Ω of 12 points, |D| = 2048, no singletons, centre = {∅, Ω}; full
enumeration (DPLL over 265,722 additivity clauses) of two-valued finitely additive states on D: exactly
**12, all Dirac**. Consistent with 1.6 (on finite G, step (i) is automatic) and with GATE1's `check.py`.

## WHY.md bearing

Circle or composition: W★ is composition, the ring is circle; this check separates them rather than
merging them. Hidden idealisation: W★'s pointlessness lives entirely in an ultrafilter that cannot see any
linear parity question.
