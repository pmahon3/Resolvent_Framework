# σ-essential construction log — ARCHIVED DETAIL

*Full prose moved out of the memory topic file `sigma_essential_construction_attempt.md`
to keep it under the 40 KB Read-truncation cap, WITHOUT destroying charted territory.
The navigational one-liners for everything here live in
`notes/open_questions/CHARTED_sigma_essential.md` (grep that first); this file holds the
drill-down detail. Nothing is lost — originating-session jsonl on disk holds the fullest
prose if even this is insufficient. First archived 2026-06-22 (band family + Lean pivot,
Sessions 6–8c).*

---

═══════════════════════════════════════════════════════════════════════════════
## BAND FAMILY — DEAD (Sessions 6–8, compressed spine)
═══════════════════════════════════════════════════════════════════════════════

> Sessions 6–8 (the band-family arc) collapsed to one-liners 2026-06-18 (topic-file cap).
> Every result/kill/reversal preserved below; reasoning-trail prose dropped (full prose in
> originating jsonl on disk). Net: the band family is FULLY DEAD as an Exit-A vehicle — a
> sharp DICHOTOMY (∪-closed ⟹ Boolean / not-∪-closed ⟹ not-a-lattice). Kills ONE route, NOT
> global Exit B. Sessions 8b/8c (the Lean pivot) are kept VERBATIM below.

### THE BAND FAMILY (Session 6) — the substrate that passed the binding check
- SETUP: ℕ≅ℕ×ℕ; {S_α:α<𝔠} an ALMOST-DISJOINT family of infinite row-index subsets. Block
  B_α = {R_i (row i): i∉S_α} ∪ {S_α×{j}: j∈ℕ} (background rows outside S_α + "column-in-band"
  action cells inside). Each B_α≅P(ℕ) infinite atomic. AD ⟹ 𝔠 pairwise-localized blocks (beats
  the "only ℵ₀ disjoint regions" count). BINDING PAIR: a=S_α×{0}, b=S_β×{0}, S_α∩S_β finite
  nonempty ⟹ a∩b=(S_α∩S_β)×{0} ∉B_α,∉B_β ⟹ incompatible-not-orthogonal. First genuine binding
  pair. (Prior families died on the binding check: lines on ℤ² = countably many directions ⟹
  countable-block ⟹ Exit B; tree branch-deviation partitions = LAMINAR ⟹ compatible ⟹ Boolean.)
- THREE "FORCED SQUEEZES" EACH FAILED AT THEIR FLAGGED LINK (the pattern was the Session-6 signal;
  each = a would-be reversal #16 advisor caught): region-count (ℵ₀ disjoint regions, beaten by AD),
  AD-count, and ∪-closure. The ∪-closure one: adding union block B_{α∪β} for the LUB is a CONTAINER
  not a MERGER — a∩b still ∉B_α,B_β ⟹ binding SURVIVES finite-∪-closing the index. So "binding wants
  non-∪-closed, lattice wants ∪-closed, they pull oppositely" is FALSE (∪-closed ⇏ nested ⇏ compatible).

### THE COLLAPSED DICHOTOMY (Session 8, ⟦HAND — verified⟧, supersedes the Session-6 trichotomy)
- Session 6 had a TRICHOTOMY: (a) not-∪-closed ⟹ NOT-A-LATTICE [AD case, cl(a∪b) escapes =
  Strategy-D limit-branch on the OML side]; (b) ∪-closed w/ comparable-finite-diff pair ⟹ BOOLEAN;
  (c) ∪-closed, no such pair ⟹ claimed "NOT σ-COMPLETE" via mixed-column escaping join
  X=⊔ⱼ(S_{αⱼ}×{j}). Session 8 OVERTURNS the (b)/(c) cut: it is SPURIOUS — regime (c) is BOOLEAN too.
- THE FORCING CHAIN (⟦HAND — verified⟧, advisor ×3, now Lean-certified — see 8b/8c). Column j, sets
  ⊆ℕ. For ANY binding pair with S_α∪S_β∈ℐ (= finite-∪-closure, the DEFINING property of (b),(c)):
  • STEP 1: S_α ⊆ S_α∪S_β comparable ⟹ relCompl (S_β∖S_α)×{j} ∈ L̄.
  • STEP 2: (S_β∖S_α) ⊆ S_β comparable ⟹ relCompl (S_α∩S_β)×{j} ∈ L̄.
  ⟹ the FORBIDDEN finite cell (S_α∩S_β)×{j} is FORCED IN at the FINITE pre-σ level, any difference
  size. AIRTIGHT via the legality check: A⊆B ⟹ A,Bᶜ disjoint ⟹ Bᶜ⊔A legal ⟹ (Bᶜ⊔A)ᶜ=B∖A∈L̄. No
  orthomodular subtlety; difference size IRRELEVANT (the whole point). Step 1 does NOT need ℕ — only
  S_α∪S_β∈ℐ — so the (b)/(c) finite-diff distinction never gated it (the ℕ-caveat was a conflation:
  in the minimal evens∪{0}/odds∪{0} example S∪S′=ℕ exactly; on a genuine AD pair S_α∪S_β≠ℕ but ∈ℐ).
- DICHOTOMY (sharp, whole band-family verdict): (a) not-∪-closed ⟹ NOT-A-LATTICE; (b)+(c) ∪-closed ⟹
  BOOLEAN. ⟹ NO band index yields a concrete σ-complete non-Boolean lattice. The regime-(c)
  X-escape/"not-σ-complete" death is SUPERSEDED not contradicted: the relCompl closure manufactures
  (S_α∩S_β)×{j} FIRST, so X-escape was computed on the wrong (pre-closure) object; (c)'s real death
  is "Boolean." (= DEATH 2 generalized from finite-diff/one-step/ℕ-union to any-diff/two-step/any-∪-in-ℐ.)

### THE SESSION-7 EQUIVALENCE (the non-Booleanness criterion the chain feeds)
- Ω=ℕ×ℕ COUNTABLE + generators SEPARATE POINTS ⟹ a point-separating family generates the FULL
  σ-algebra P(Ω). THEREFORE **L̄ NON-BOOLEAN ⟺ L̄⊊P(Ω) ⟺ disjoint-∪-closure PROPER ⟺ the finite sets
  (S∩S′)×{0} STAY OUT of L̄** = HW Problem 2 in fully concrete countable form. WHY single-axis
  invariants fail: row-trace T_i and column-slice σ_j are each σ-HOMOMORPHISMS ONTO P(ℕ) ⟹ both axes
  are already all of P(ℕ) ⟹ non-Booleanness is irreducibly a JOINT 2D fact about WHICH INTERSECTIONS
  CLOSE. NON-CIRCULAR TARGET (the bite-3 frontier): an INTRINSIC class 𝒦⊆P(Ω) with (a) generators∈𝒦,
  (b) 𝒦 closed under ^c + countable DISJOINT ∪, (c) (S∩S′)×{0}∉𝒦 ⟹ L̄⊆𝒦 non-Boolean. THE CATCH: rows
  thin-across-columns, cells thin-across-rows (TRANSPOSES); 𝒦 must tolerate BOTH — obvious one-axis
  candidates die on the other generator type. 𝒦 exists ⟺ witness substrate; refute ⟺ (c) Boolean too.
- "EXISTENCE IS FREE" trap (Session 7, advisor): P(Ω) is a σ-complete concrete OML ⊇ L∪{X}; smallest
  σ-complete sub-OML exists (=⋂). The crux is NOT "does the limit exist" but (σ-complete ∧ LATTICE ∧
  NON-BOOLEAN ∧ REGULAR-over-L) SIMULTANEOUSLY; L↪P(Ω) is NON-regular (a∧b=∅ in L, a∩b≠∅ in P(Ω)) =
  HW Problem 2 itself.

### FENCED REVERSALS FROM THE BAND ARC (Sessions 6–8, DO NOT REVIVE)
- "X∉L is index-independent" (Session 6) — OVERSTATED; X-escape needs the paste premise, fails in (b)/(c).
- "regime (c) = HW Problem 2, open both ways" (Sessions 6–7) — OVERTURNED *for the band family* by S8;
  (c) is Boolean. HW-Problem-2 connection survives ONLY for a hypothetical NON-BAND concrete σ-complete
  non-Boolean OML.
- "the collapse is finite-specific, needs ℕ∈ℐ" (Session 8, caught immediately) — FALSE; relCompl
  ignores difference size.
- REVERSAL #21 (Session 7, the circularity, RETRACTED): "S∩S′ finite ⟹ incompatible-in-L̄ ⟹ gap ∅ ⟹
  no singleton" is CIRCULAR — round-0 incompatibility holds in L, NOT necessarily in L̄; σ-closure is
  PRECISELY what might ADD the intersection. Round-1 generator meets ≠ the σ-closure.
- "band family dead ⟹ Exit B" (Session 8, REFUSED) — FALSE; kills ONE route. HW Problem 2 in general +
  non-band pasting + the state w are UNTOUCHED. (On a countable band index the countable-block theorem
  gives μ(fakes)=0 ⟹ Exit B on the state anyway, so the band ceiling was always "substrate fact.")
- SUBSTRATE ≠ WITNESS (standing): even a non-Boolean σ-complete irreducible L̄ is only the lattice; the
  prize is the σ-essential contextual STATE w (extends? σ-additive? contextual?) — UNTOUCHED.

═══════════════════════════════════════════════════════════════════════════════
## SESSIONS 8b & 8c — Lean pivot, collapsed to spine 2026-06-22
═══════════════════════════════════════════════════════════════════════════════
> *Was verbatim "live frontier" — NO LONGER (band family DEAD, existence route PARKED
> S11). Lean work durable in repo + [[formalization_status]]; full verbatim in git
> history. The "Lean-as-search-container" pivot certified the band engine, then was
> mooted by the park.*

**SETTLED, 0 sorry/0 axiom** (`formalization/QuerySystem/QuerySystem/BandClosure.lean`):
Lean-as-search-container — concrete logic = complement-and-disjoint-∪-closed `Set (ℕ×ℕ)`
collection (NO OML typeclass — that re-enters the Mathlib wall; concreteness is the gift).
`relCompl` (`A⊆B→B∖A` via `(Bᶜ∪A)ᶜ`; Lean forces the non-skippable disjointness check =
the hand legality check), `csUnion`, `forces_boolean` (singletons⟹P(Ω) by disjoint ∪ NOT
∩), `band_forces_boolean` (the forcing/assembly engine, CONDITIONAL on the `index⟹singletons`
step which is HAND-ONLY). Certified the band engine; the state `w` always out of scope.
Bite 3 (candidate `𝒦` as a Lean predicate) never reached — **mooted by the S11 park**
(finite-assembly carriers ruled out; needed lever is global/non-compositional).
