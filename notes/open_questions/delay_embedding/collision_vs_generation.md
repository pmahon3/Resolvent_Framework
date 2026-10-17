# Open question: when does geometric refinement give σ-algebraic generation?

**Opened 2026-10-08.** Dormant until new input (open-question lifecycle).
This is the "well-conditioned" half of the programme's root question. The
flagship kept the injectivity half and recast it as commensurability.
`notes/programme/genealogy.md` (update 2026-10-08) records the root.

## Statement

Delay factor O_L = σ(Φ_L), fibre weights p_z, conditional laws μ_z.

- Collision mass C_L = Σ_z p_z² (geometric refinement).
- Algebraic defect δ_L(S) = E[Var(1_S | O_L)] = Σ_z p_z μ_z(S)μ_z(Sᶜ).

What condition on Φ_L, not equivalent to the conclusion O_∞ = ℬ mod μ, makes
C_L → 0 imply sup_S δ_L(S) → 0?

> **⚑ CLOSED 2026-10-09 (user decision): the breadcrumb back to geometry is
> ACCOUNTED FOR.** The root's two halves are covered:
> - injectivity: Takens / Sauer–Yorke–Casdagli;
> - σ-algebraic generation: Rokhlin / Kolmogorov–Sinai, killed below for
>   invertible T;
> - metric conditioning: the stable-embedding literature (Eftekhari–Yap–Wakin–
>   Rozell 2018; Yap–Rozell), partially occupied. Its qualitative lower bound
>   (exponential degradation in L) looks elementary.
>
> Residues, not pursued: endomorphisms; a fixed-h explicit-constant bi-Lipschitz
> Takens theorem (technical, off-mission). The countable σ-essential witness
> recorded in this hub is independent and still live.
>
> **⚑ RE-AUDIT 2026-10-09: the σ-algebraic form is KILLED by its own exit criterion
> (classical generator theory), scoped to invertible T. The sup form is
> ill-posed. Endomorphisms are unchecked.** See "Re-audit 2026-10-09" at the end.
> The kill is recorded in place because this hub also carries the live countable
> σ-essential witness. Moving it to `covered_leads/` is the user's call.

## What is already settled (`notes/covered_leads/fibre_mixing.md`)

- δ → 0 ⟹ C → 0. The converse is false.
- Witness: the skew product X = A^ℤ × B^ℤ with h(a,b) = a₀ and independent iid
  coordinates gives C_L = 2^{-(L+1)} → 0 while δ_L = 1/4 for all L.
- Fibre mixing (a lower bound per fibre) is useless. The candidate direction
  is an *upper* rate bound, uniform decay of μ_z(S)μ_z(Sᶜ) as C_L → 0.

## Exit criteria

- **Promote:** a non-circular sufficient condition with a proof sketch.
- **Kill:** the condition turns out to be classical in Rokhlin or
  Kolmogorov–Sinai generator theory. The 2026-05 investigation did not run a
  generator-theory prior-art check.
- **New input that would wake it:** any flagship result quantitative in the
  window length; any metric or conditioning statement on windows.

## Bridge hypothesis (flagged 2026-10-08) and its first falsifier

> **KILLED 2026-10-09** by the falsifier pre-registered at the end of this section
> (winding mismatch). See "Flagship correspondence, 2026-10-09". The carrier results
> and the countable witness below stand on their own.

**Hypothesis ⟦HAND — direction, not result⟧.** The conditioning step is the only
point where the two DAG components could constrain each other. Real-valued
windows remove the finite-alphabet compactness (seed C1′) that keeps them apart.
Contextual window families, glued along shared coordinates, give Polish-built,
non-Boolean carriers, and those fall under the paper's open Q6.6 (`DWPolishCut`).
If Q6.6 is negative, continuous-observation protocols carry no σ-essential
obstruction. If it is positive, delay-window gluings are a place to search for a
witness. Bar: amendment 4(b) of `notes/programme/blueprint_dag_connectivity.md`.
Each lane must constrain the other; an instantiation does not count.

**Falsifier.** Does the gluing collapse to a Boolean carrier, or to a class already
settled (Boolean, horizontal σ-sum, segregated)? **It did not fire.** The non-Boolean
leg alone would not show that: two *disjoint* windows σ(x₀) ∪ σ(x₁) are also
non-Boolean, and that carrier is MO₂-shaped and settled. The block-overlap leg is
the one that separates. Grades are below; everything marked Lean is in
`formalization/staging/WindowGluing.lean`, axioms `[propext, Classical.choice, Quot.sound]`.

| leg | result | grade |
|---|---|---|
| non-Boolean | `glued_not_interClosed`: coordinates `i, j` that each lie in a window but share none make the carrier fail intersection-closure. Covers chains of length ≥ 2 and rings of length ≥ 4. `ring4_real_not_interClosed` is the real 4-ring | **Lean** |
| not a horizontal σ-sum | `glued_blocks_overlap`: two **distinct** maximal blocks (the repo's `IsMaxBlock`) share the nontrivial element `{x_m ∈ U}`, when `m` shares a window with `i` and another with `j`. Uses `exists_isMaxBlock_superset`, so there is no Zorn gap | **Lean** |
| concrete, σ-complete | automatic for any `DynkinSystem` | Lean (existing) |
| Borel, generating | `glued_le_borel` and `generateFrom_glued`: when the windows cover all coordinates, σ(D) is the product σ-algebra. This is the Derr–Williamson D.6 setting exactly | **Lean** |
| `NonSegregated` (`Admissible` conjunct 2) | `glued_nonSegregated` for ℝ-valued windows: an ultrafilter escaping to +∞ in one coordinate has an empty block kernel. **Cheap, so it does not discriminate**: every Borel σ-algebra of ℝ is non-segregated too | **Lean** |
| `EssentiallyIrreducible` (`Admissible` conjunct 1) | `ring4_real_essentiallyIrreducible`: the centre is `{∅, univ}`. A central E meets `{x_i = a}` inside D, and the rectangle identity at a separated pair then makes E independent of x_j. In a ring every coordinate has a separated partner. **`ring4_real_admissible`: the glued real 4-ring is an `Admissible` carrier** | **Lean** |
| `PolishRepresentable` | opaque `axiom` in `SigmaEssentialOpenCore`, so it can't be certified. The D.6-shaped facts above are what can be | not decidable in current formalization |
| triangle (all pairs share a window) | non-Boolean in the finite binary oracle only. The Lean invariant does not reach it | machine, finite |

**Contextual statistics live on the carrier, but that does not make a witness.**
In the finite binary oracle (`notes/open_questions/verification/window_gluing_states.py`, exact rational arithmetic):
- The odd-parity 4-ring statistics (PR-box-like, not realisable) define a genuine
  state on the glued carrier, with range [0,1].
- The contextual triangle statistics do **not**: the carrier contains
  `{000,111}`, which gets −1/2.
- Restriction to `{0,1}^4 ⊂ ℝ^4` is a Dynkin homomorphism ⟦HAND⟧. So the
  4-ring state pulls back to a **σ-additive** state on the real carrier that no
  Borel measure extends.

That is contextuality, but not σ-essentiality: Φ concerns *two-valued* states.
On the finite glued ring every two-valued state is a Dirac (window restrictions
are Diracs; shared coordinates force a global point) ⟦HAND⟧. This agrees with
standing check 3.

**What is left: the real question, sharpened.** The glued real 4-ring passes every certifiable admissibility test, so it is a concrete Q6.6 instance. What remains is Φ on it. A σ-essential witness on a
window gluing needs finitely additive two-valued window states (Borel
ultrafilters, not points) that agree on shared coordinates but do not glue
around a cycle. Chains (trees) plausibly always amalgamate; rings are the
candidate ⟦HAND — speculative⟧. Next check: can Borel-ultrafilter patterns on
ring windows fail to amalgamate, and does that cycle condition match the
flagship's winding/parity obstruction? A match would be the two-way constraint
the bar asks for. A mismatch, or always-amalgamating rings, would kill the bridge.

## Candidate witness on the glued 4-ring (2026-10-08) — LEAN-CHECKED; prior-art gate PASSED 2026-10-15 (not found)

**Update (same day): proved.** In `formalization/staging/WindowGluing.lean` §`WindowGluing.Cyclic`
(standard axioms `[propext, Classical.choice, Quot.sound]`), on the glued 4-ring of
**ℕ-valued** windows (Ω = ℕ⁴, countable; window events are arbitrary sets, so every
event is Borel):
- `mu_cases`: μ = v₀ − Σ s_k + Σ P_w (iterated limits along a non-principal
  ultrafilter) is {0,1}-valued on the carrier. The proof combines eight rectangle
  identities (reset 0) found as a minimal SAT core: Φ = v(3412)+v(0231)−v(0321) =
  v(2341)+v(0123)−v(0231).
- `s₀_sigmaEssential`: the pattern C_k = {x_k < x_{k+1}}, all true, is σ-essential
  in the repo's own `IsSigmaEssential`.
- `admissible`, `targetA_sharp_countable`, `targetA_sharp'`, `dwPolishCut_excludes`:
  admissible carrier, countable Ω, generating σ-algebra 𝒫(ℕ⁴); given `DWPolishCut`,
  the carrier is not `PolishRepresentable`.

⚠ This bears on paper Q6.6 (Polish case) and on the paper's countable-Ω question.
**Nothing propagates to the paper until a hostile prior-art check has been run.**
The text below is the pre-proof record, kept for the trail.

### Structural simplification of `mu_cases`, 2026-10-15 ⟦HAND; finite-alphabet machine check⟧ — qualifies the novelty rebuttal

**Lemma.** Suppose the window structure has pair windows, and no three windows
pairwise share a coordinate. This holds for paths and for rings with L ≥ 4. Then
the Dynkin closure D equals the set of E_{k-1} ⊔ E_k with adjacent window events.

**Why.** Non-adjacent non-empty window events always intersect. On two adjacent
windows, slicing at the shared coordinate shows complements stay in that form.

**Consequences:**
- On the ring, any finitely additive state on D is *forced*:
  s(E) = u_{k-1}(E_{k-1}) + u_k(E_k), from the window ultrafilters.
- So `mu_cases` reduces to checking that this explicit formula is well defined
  across two-window decompositions and is {0,1}-valued. A referee holding the
  lemma could call that bookkeeping.
- **The rebuttal recorded below ("all novelty sits in `mu_cases`") is therefore
  weaker than stated.** This is a simplification, not a kill. No source was
  found for the lemma or the witness.
- **On paths** the same lemma plus window amalgamation proves that every
  two-valued state is an ideal point: no pointless coherence without a cycle.
- **The triangle (L = 3)** breaks the lemma: D ≠ G (70 vs 66 sets, binary). This
  has the same shape as Greechie's Loop Lemma, where order-3 loops are special
  (Kalmbach 1983 §4 L9, shelf). Prior art for the lemma itself is unchecked.

Details: `notes/open_questions/cyclic_marginal/pointless_coherence.tex` (§§4.4, 4.7; the problem-set kit was retired 2026-10-16). Script: `notes/open_questions/verification/pointless_path_dynkin.py`.

### Third-pass prior-art gate, 2026-10-15: NOT FOUND after three passes (residual risk named)

One sonnet scout read full texts:
- shelf: Navara–Pták 1983, Navara 1984, Navara 1992, Dvurečenskij–Neubrunn–Pulmannová 1992,
  Müller–Pták–Tkadlec 1992, Pták–Pulmannová 1994, Abramsky–Barbosa 2025 talk;
- web: Cardona–Mejía–Uribe-Zapata 2503.08910, Burešová–Pták 2401.13651,
  Burešová–Pták–Ševčík 2609.10770, Barbosa et al. 1905.08267 (continuous-variable
  contextuality).

**No source states the result or implies it in a few lines. None makes `mu_cases` routine.**

What the sources do contain:
- **Finite shadow.** Navara–Pták 1983 has a 6-point σ-class with cyclically
  overlapping M₁…M₄ and the non-point two-valued state m ≡ 0. A referee can call
  the countable version "the same phenomenon with ultrafilters". Rebuttal: on a
  finite carrier, finite additivity and σ-additivity coincide, so there is no
  split to exhibit.
- **Navara 1984 claims "measures on σ-classes extend uniquely from the
  generators".** That is σ-additive only, and μ shows it fails for finite
  additivity. Say so in any write-up.
- **Boolean tools cannot reach μ.** Any {0,1} charge on the *algebra* generated
  by the windows would give μ(∩C_k) = 1 with ∩C_k = ∅. So μ is not the
  restriction of an ultrafilter, and Cardona et al. and Horn–Tarski do not apply.
- **Barbosa et al. presuppose σ-additivity.** Their framework (§5.3, compact
  Hausdorff outcomes) leaves the finitely additive gap outside its scope.

**Unread:**
- Bhaskara Rao, *Theory of Charges*;
- Goldberg / Hindman–Strauss bodies (cyclic ℕⁿ amalgamation);
- Okay-school bodies on infinite outcomes;
- MathOverflow, searched only shallowly.

**Costume found and fixed in the same pass.** `Admissible` includes
`EssentiallyIrreducible`, i.e. every central E is countable or co-countable. On a
countable Ω that conjunct is **vacuous**. The proof of
`ring4_essentiallyIrreducible` actually showed the centre is literally {∅, univ},
but the exported statement threw that away.
- Now exported as `ring4_centre_trivial`.
- New receipt `targetA_sharp_countable_literal`: countable Ω₄, `Irreducible D₄`
  (centre literally {∅, univ}; the existing `Admissibility.Irreducible`),
  `NonSegregated`, `IsSigmaEssential`. Standard axioms, 0 sorry.
- New receipt `D₄_six_conjuncts`: the six original conjuncts on D₄, with
  `Irreducible` in place of the vacuous conjunct. Its axiom profile is identical
  to `L₁_six_conjuncts`, i.e. the Polish clause is conditional on `DWPolishCut`.
- D₄ cannot contain every singleton. If it did, countable disjoint unions would
  give D₄ = 𝒫(Ω₄), which is Boolean, and a Boolean carrier has no witness
  (`boolean_no_witness`). So the paper's "necessarily without all singletons"
  holds automatically.
- Literal irreducibility is proved for L = 4 only, not yet for D_L at L > 4.

**What this answers.** σ-essential paper Q `q:cardinality` asks: "can a countable
Ω carry one … Is there a ZFC lower bound beyond 'uncountable'?"
- **Candidate answer, yes**, in the sharp form scoped exactly like `psi_ZFC`:
  Ω = ℕ⁴, a literally irreducible carrier, all six conjuncts.
- It stays a candidate until the Phase-2 audit (promote-to-seed).
- The lower-bound half is then moot.
- **Not propagated to the paper. That is the user's call.** Memory: paper claims
  have run ahead of Lean four times before. The `FIDELITY_CHECKLIST` standing
  re-read finds no drift, because the paper cites no `WindowGluing` name.
- **Q6.6 / `DWPolishCut`: not assessed.** D₄ lives on discrete ℕ⁴, where
  𝒫(ℕ⁴) is Polish-Borel. Whether `dwPolishCut_excludes` says anything about
  the cut depends on the paper's definition of Polish-representable and on the
  s13 coarse-riding escape: the window restrictions are non-principal (p⊗p).
  Do not read it as refuting the cut.
- **Scope:** σ-essential on every ring L ≥ 4. Literal irreducibility has a
  receipt for L = 4 only. For L > 4 the irreducibility conjunct is still the
  vacuous one.

### Prior-art scout, 2026-10-08: FOLKLORE-ADJACENT, coverage partial

Shelf first, then two web queries. **Not found as a stated result. No contradiction
found.**
- **Closest:** Navara–Pták 1983 (shelf PDF). It has a non-point *σ-additive*
  two-valued measure on a small countable σ-class, which is the opposite polarity.
- **Derr–Williamson Thm 4.5 / D.6:** the extension framework; neither states this.
- **Navara 1992 / Dvurečenskij–Neubrunn–Pulmannová 1992:** FA-not-σ examples on
  non-σ-complete logics.
- **Vorob'ev / Kellerer:** the cycle obstruction is classical. No finitely
  additive two-valued ultrafilter form was found.
- **Referee risk:** "a routine Vorob'ev-cycle plus ultrafilter-amalgamation
  variant". Rebuttal on the record: the non-routine step is two-valuedness on the
  *Dynkin closure* (`mu_cases`). Window-level gluing is easy; additivity across
  D's cross-window disjoint unions is what the eight identities settle.
- **Horn–Tarski note:** μ does not extend to 2^Ω (its kernel is empty). That is
  intended: `FinitelyCoherent` asks for an FA state on the carrier D, not on 2^Ω.
- **Not yet searched:**
  - ultrafilter model theory (p⊗p, 3-amalgamation)
  - Pták–Pulmannová, *Orthomodular Structures*
  - Dvurečenskij, *Gleason's Theorem*
  - Navara–Rüttimann 1991; de Simone–Navara–Pták
  - work citing Derr–Williamson

  These need a second pass before any paper change.

### Second-pass scout, 2026-10-08: FOLKLORE-ADJACENT (not found)

**No source states the combination. No contradiction found.** Each ingredient is
folklore:
- the cyclic marginal obstruction (the three-coin cycle);
- the non-commutativity of p⊗p (Goldberg JSL 2022, arXiv 2102.04677;
  Hindman–Strauss);
- "σ-additive 0-1 on a countable set is a Dirac".

The last makes the no-σ-extension half trivial. **All novelty sits in the finitely
additive existence step, `mu_cases`** (two-valuedness across D's cross-window
disjoint unions). No source was found for it.

**Closest new neighbour:** Cardona–Mejía–Uribe-Zapata, arXiv 2503.08910. It
generalises Horn–Tarski to three FA measures, one an ultrafilter. Only the
abstract was read: it concerns extension to Boolean algebras, with no cycles and
no σ-additivity mentioned. Burešová–Pták(–Ševčík), arXiv 2401.13651 and
2609.10770, cover Z₂-state extension and are finite or extension-theoretic.

**Weak point: search depth, not contrary evidence.** Still unread:
- the bodies of 2503.08910 and 2609.10770;
- Bhaskara Rao, *Theory of Charges* (λ-system / 0-1 charge sections);
- Pták–Pulmannová 1991 and Dvurečenskij 1993;
- Navara–Pták 1983 full text;
- Mushtari, Ovchinnikov, Müller, Godowski, Navara–Rüttimann;
- 3-amalgamation for types (model theory);
- MathOverflow.

**Gate:** read the 2503.08910 body and the Pták–Pulmannová / Dvurečenskij
state chapters by hand before any paper change.

### Pre-proof record

⚠ If this candidate holds, it would show `DWPolishCut` fails on an admissible,
Borel-generating carrier. The σ-essential verdict has already oscillated four
times (memory: "do NOT swing again"). **Nothing here is a claim.** Run a hostile
cross-field prior-art check before any further investment.

**Reduction ⟦HAND⟧.** A σ-additive two-valued state on the glued real ring
restricts, on each window, to a σ-additive 0–1 state on Borel(ℝ²), which is a
Dirac at a point. Shared coordinates make those points agree, and the
Dynkin-uniqueness argument extends agreement from the generators to all of D, so
the state is a global Dirac. Clause (ii) of `localization` is then automatic, and:
a witness exists ⟺ some finitely additive two-valued state on D has a true family
without the finite intersection property.

**The pattern.** Let `C_k = {x_k < x_{k+1}}` (indices mod 4), each a window
event, and `B = {C_k, C_kᶜ}` with all `C_k` true. The kernel `⋂ C_k` is empty
(cyclic order), so no Dirac extends. On each window the pattern comes from the
ordered ultrafilter p⊗p (p non-principal on ℕ ⊂ ℝ). All four single-coordinate
marginals are p, so the window ultrafilters agree on shared coordinates, yet they
do not glue: a σ-additive analogue (P(x₀<x₁)=1 with equal marginals) is impossible.
It is the ultrafilter form of a cyclic (Vorob'ev-type) marginal obstruction:
contextuality that only finite additivity permits.

**The crux, open.** Is the pattern *finitely coherent*, i.e. does some finitely
additive two-valued state on all of D extend it? Graph-type window ultrafilters
can't do this (Katětov: f(p)=p forces f = id on a p-set, so the monodromy is
trivial); ordered product ultrafilters escape that argument.
- Natural candidate: μ(E) := Σ_w lim_{u_w} f_w, where 1_E = Σ_w f_w is the
  anchored window decomposition. It is linear, well-defined (kernel = gauge
  terms, which telescope), and finitely additive. What is needed is that it is
  **{0,1}-valued on D**.
- Hand progress: a {0,1}-valued f ∈ V has, at each (x₁,x₃), an (x₀,x₂)-section
  depending on one coordinate only. A nonstandard tower h₁≪…≪h₅ gives μ ∈ {0,1}
  whenever the relevant section type is x₀-independent. The remaining case
  needs all four break positions to fail simultaneously, and that is unresolved.
- **Evidence:** `notes/open_questions/verification/window_gluing_cyclic_order.py`
  propagates the pattern through the Dynkin closure of order+threshold window
  atoms (a faithful finite model of that sub-carrier). It is **consistent and
  two-valued** at T=1 (|D'|=466) and T=2 (|D'|=40,418). No contradiction was
  found. This covers sub-carriers only, not all Borel window events or countable
  operations.

**Next, in order:**
1. Hostile prior-art check: the finitely additive cyclic marginal problem,
   ultrafilter amalgamation over cycles (model-theoretic 3-amalgamation), and
   two-valued states on Polish concrete logics.
2. Prove or refute μ ∈ {0,1} on D. A refutation would be a set E ∈ D with
   μ(E) ∉ {0,1}, which would kill the candidate.
3. Only then, Lean.

## Ring sweep, 2026-10-08 — where the cyclic witness lives ⟦machine, tower relaxation; not Lean except L=4⟧

Oracle: `notes/open_questions/verification/window_gluing_ring_sweep.py`. It ranges
over ring lengths L=3,4,5 and every orientation ε ∈ {±}^L (ascent/descent per
window, ε₀=+ by symmetry).

| L | σ-essential (this μ) | non-witnesses |
|---|---|---|
| 3 | **none**. +++ is unrealisable, but μ is NOT two-valued: in the triangle every pair shares a window, so only the triple-difference identity holds | all mixed: two-valued but σ-realisable |

> **Note 2026-10-16:** the L=3 "not two-valued" failure is on a non-buildable 0/1 function, off the carrier. It does **not** obstruct the triangle. On finitely built triangle questions Λ is two-valued (six-orders argument, below).
| 4 | **exactly ++++** | all 7 mixed: σ-realisable |
| 5 | **exactly +++++** | all 15 mixed: σ-realisable |

**Emerging rule ⟦conjecture⟧.** A witness of this type appears iff
(i) **winding**: the orientation cocycle has nonzero net winding (no height
function integrates it, so it is σ-unrealisable), and
(ii) **room**: L ≥ 4 (a non-adjacent pair supplies the separating rectangle
identities that make μ two-valued).
This is the same two-part shape as the flagship's winding criterion: winding ≥ 2,
plus layer-injectivity. A correspondence is not yet shown.

**Caveat.** L=3 failing is a fact about *this* μ, not a no-witness theorem for the
triangle.

**Update 2026-10-09: the witness half is proved for every L ≥ 4 (Lean).**
`WindowGluing.Ring.sL_sigmaEssential` (std axioms) transports the 4-ring witness
along the degree-one cycle map k ↦ ⌊4k/L⌋ : ℤ_L → ℤ₄. With ψ(y)_k =
(L+1)·y_{⌊4k/L⌋} + k:
- ψ⁻¹ sends L-window events to 4-window events, so the L-ring carrier pulls back
  into D₄ (`pullback`);
- μ∘ψ⁻¹ is a two-valued finitely additive state (`muL`);
- ascents inside a block pull back to Ω, and block-crossing ascents contain C_k
  (`muL_CL`).

The σ side is a max-element argument. **The mechanism is winding:** the witness
is functorial along winding-one maps of cycles.

Still open from the rule:
- the converse ("mixed orientations are σ-realisable", trivial);
- the triangle.

**Triangle probe, 2026-10-15** ⟦machine; sub-carrier only⟧. Ran the order+threshold
propagation oracle on the triangle (`window_gluing_cyclic_order_triangle.py`).
- The +++ staircase (p⊗p on every window) extends **consistently and
  two-valued**: 430 sets at T=1 and 74,738 at T=2.
- So nothing rules out a triangle witness. The failure recorded above is a fact
  about the specific inclusion–exclusion μ, not about the triangle.
- On the triangle the carrier is not determined by adjacent window pairs: D ≠ G,
  see `notes/open_questions/cyclic_marginal/pointless_coherence.tex` §5. So any
  triangle witness must use a different formula.
- Evidence now leans toward "any cycle permits pointless coherence" rather than
  "length ≥ 4". Not proved.
- **Downgraded 2026-10-16 (Helly-lens test).** The order+threshold sub-carrier is
  *not point-Helly*. Its chosen generic cells per window pairwise meet but are
  jointly empty (checked: pairwise True, joint False). So the finite consistent
  state found is a **point-level (die-type) Helly failure**, which is possible
  for finite reasons alone. It does not test the ideal-level question.
- The same caveat applies to the 4-ring sub-carrier runs; there the Lean
  witness settles the matter independently.
- **Triangle: inconclusive.** "Leans any cycle" is withdrawn.
- **Correction to the downgrade (2026-10-16, later the same day).** The
  sub-carrier oracle did not test an arbitrary finite state; it propagated the
  **forced** values.
  - Any state extending the staircase must equal
    Λ(f) = Σ_k lim_{u_k} f_k on every *finitely built* question. Λ is well
    defined: zero-sum triples f₀+f₁+f₂ = 0 are coboundaries plus constants, and
    the marginals agree.
  - So "consistent" there is a genuine **necessary-condition** check. It can
    refute, and cannot confirm.
  - **Results** (`verification/triangle_forced_functional.py`): Λ is
    two-valued on all definable finitely built triangle questions.
    - T=0: 26 atoms, 430 sets, 0 bad.
    - T=1: 51 atoms, 74,738 sets, 0 bad.
  - **The old ring-sweep failure** ("μ not two-valued at L=3") lives on the same
    26 atoms, so its failing 0/1 function is **not buildable**. It does not
    obstruct the triangle.
  - **Untested:** countably built questions, where finite additivity does not
    force the value.
  - **Refutation hunt, 20 min per level** (`verification/triangle_lambda_hunt.py`):
    no refutation at T=2 (513,802 buildable questions explored, 256,624 true),
    T=3 (496,150 / 246,608) or T=4 (493,038 / 244,116). It searches for two
    disjoint true questions, which is exactly a failure of Λ.
  - Status: open, with the necessary condition holding at every level tested.
- **Cut-the-loop decomposition (2026-10-16) ⟦HAND⟧.** For window k, let
  W⁽ᵏ⁾ be the ultrafilter gluing the other windows along the path left after
  cutting k (iterated p⊗p). On window k it equals u_kᵀ. Then for every finitely
  built E with indicator f₀+f₁+f₂:
  - **Λ(E) = W⁽ᵏ⁾(E) + δ_k(E)**, where
    δ_k(E) = lim_a lim_b f_k − lim_b lim_a f_k, the commutator of iterated
    p-limits on window k;
  - δ_k is gauge-invariant (single-coordinate terms have order-independent
    limits) and linear.
- **Consequences:**
  - Λ(E) ∈ {0,1} whenever E is twist-free (δ_k = 0) on some window.
  - A failure needs E twisted with the same sign on all three windows at once.
  - Example: C₀ = {x₀<x₁} has δ₀ = 1 and δ₁ = δ₂ = 0.
- **Remaining lemma:** no finitely built triangle question is twisted
  same-sign on all three windows.
- **PROVED ⟦HAND⟧, same day (six-orders argument).**
  - Let W_π be the iterated-p⊗p ultrafilter for each of the 6 drawing orders π.
    A window question's profile π ↦ W_π(E) depends only on the order of its
    pair. Complement and disjoint union preserve "constant or half" profiles.
  - Λ(E) = W⁽ᵏ⁾ + W⁽ʲ⁾ − W⁽ʲᵏ⁾, an identity that holds termwise on each window.
    It gives Λ ∈ {0,1} on constants and halves, and Λ = 2 only on the profile
    "exactly the 3 rotations of 012", which is not a half.
  - **Hence Λ ∈ {0,1} on every finitely built triangle question**, definable or
    not.
  - The ring sweep searched every 0/1 function in the span of window functions
    on a finite tower. Its L=3 failure is on such a function with the cyclic
    profile, and that function is not buildable.
  - **Verified 2026-10-16** (`verification/triangle_profile_check.py`): on
    every set at T=0 (430) and T=1 (74,738), the profile is constant or a half,
    and Λ = W⁽ᵏ⁾+W⁽ʲ⁾−W⁽ʲᵏ⁾ holds, with 0 failures in both checks.
  - **Dichotomy.** s\* = W⁽ᵏ⁾+W⁽ʲ⁾−W⁽ʲᵏ⁾ is finitely additive on all of
    𝒫(ℕ³) and extends the staircase. It is a pointless triangle state iff every
    full-carrier set has a constant-or-half profile.
  - **Slice probe:** are slices {x₀=n}×S in the carrier? At A=3, only 14/512
    are, so the "carrier is everything" route to (b) is closed there.
  - s\* failing would not alone fire (b).
- **Box transfer (2026-10-16).**
  - **Proved ⟦HAND⟧:** the whole carrier D_ℕ lies in the span V, since zero
    triple interaction survives complements and countable disjoint unions. So
    Λ = s\* is defined on all of D_ℕ and is finitely additive; the only question
    is whether it stays in {0,1}.
  - **Bad profiles:** a set with the cyclic profile would restrict, on a box
    {v₁<v₂<v₃}³ chosen through p-large sets, to a carrier set containing the 3
    rotations and none of the reversals.
  - **3-box check (pre-registered, fired (b)):** 612/15,914 ternary carrier sets
    have that footprint, including E\* = {[x₀≤x₁]+[x₁<x₂]+[x₂<x₀]=2}.
  - **Why boxes can never decide:** the A=3 carrier is exactly *all* 0/1
    functions in the span (15,914 = 15,914; `verification/triangle_span_count.py`).
    The buildable-versus-span gap exists only at infinity.
- **Sharpest open form:** is E\* (or any cyclic-profile set) in the Dynkin
  closure over ℕ? E\* is in V, and not finitely built (six orders).
  - If no: the triangle is pointless (s\* works).
  - If yes: s\* fails, and other extensions must be examined.
  - Prior-art target: λ-systems generated by unions of σ-algebras ("sums of
    σ-algebras").
- **Navara connection (2026-10-16, read from primary source: Navara, Math.
  Slovaca 34 (1984); shelf).**
  - Navara's K(a,b) = "at least two of {f<a, g<b, f+g>a+b}", a triple that
    can never hold together.
  - With f = x₁−x₀ and g = x₂−x₁ (flight functions), f+g = x₂−x₀ is a
    flight-2 function. So the triangle carrier contains C_{f,g}, and **E\*ᶜ is
    a Navara two-of-three set**, up to integer threshold conventions.
  - **His Lemma 1:** K(a,b) ∈ C ⟺ a shifted K ∈ C, via disjoint-union
    identities with level sets. Chains propagate membership from a **base
    case**, which needs one generator bounded on one side.
  - Our generators are two-sided unbounded integer differences, so there is no
    finite base case. This is consistent with E\* not finitely built.
  - **Open, concrete:** does a countable chain or monotone limit reach a base
    case? The degenerate "one condition always true" case is buildable (a
    disjoint union of two window events). If yes, E\* ∈ D and s\* fails; if no,
    the triangle is pointless.
  - Dravecký–Šipoš: additivity fails for ℤ-valued observables, which is
    consistent with this.
  - Navara–Pták 1983, Q×Q example: a σ-additive pointless state via the lines
    x=1/3, y=1/3, x+y=1/2. That is die-type (not point-Helly); it confirms this
    school owns the die side of the seam, not the σ-forbidden side.
  - **Navara identity on the triangle ⟦HAND⟧.**
    - Setup: d₀=x₁−x₀, d₁=x₂−x₁, d₂=x₀−x₂ (summing to 0), and
      T(α,β,γ) = "at least two of d₀≥α, d₁≥β, d₂≥γ"; E\* = T(0,1,1).
    - **Identity:** if α+β+γ=2, then T(α−1,β,γ) = T(α,β,γ) ⊔ {d₀=α−1}. On
      that layer exactly one of the other two conditions holds. The same holds
      with the roles rotated.
    - So all T with threshold sum ∈ {1,2} are linked by single window-event
      layers, and E\* ∈ D ⟺ any of them ∈ D.
    - Along T(−n,n+1,1), the sets converge pointwise (each point changes ≤2
      times) to the window event {d₂≥1}.
    - **The obstacle:** each step adds one layer and removes another, so the
      sequence is not monotone. D is closed under monotone limits and disjoint
      unions, not under arbitrary pointwise limits. This is Navara's missing
      base case.
    - **Remaining combinatorial question:** can the process be rearranged into a
      monotone or disjoint-union construction? If yes, E\* ∈ D and s\* fails.
    - **Answered 2026-10-17: no**, E\* ∉ D (see the theorem below). This does
      **not** decide the triangle: other cyclic-profile sets remain.
  - **E\* cannot be split (2026-10-17) ⟦finite checks + HAND sketch⟧.**
    - Any zero-interaction subset of E\* is ∅ or E\*: kernel dimension 1 on
      every integer box up to 8³, and on definable carriers T=0,1. At T=0,1 the
      only finitely built subset of E\* is ∅.
    - Consequence: E\* can enter the carrier only as a complement.
    - The complement *can* be split: it contains the tie window events
      {x₁=x₂=c} and {x₀=x₂=c}. Switching the tie convention swaps which side is
      atomic.
    - **Plan.**
      - Off-tie lemma: strict-cyclic and strict-anticyclic are each atomic off
        the tie set, with ties free.
      - Then a least-rank argument over the family "cyclic or anticyclic mod
        ties" shows that no member is in D, so E\* ∉ D.
    - **The off-tie lemma failed** (finite boxes, ties free). It freed too much.
    - **Thin-set gate (pre-registered).** Here L = the window cells inside Y,
      checked by hand: {x₁=x₂}, {x₀=x₂}, {x₀=x₁+1} (nothing lies between b and
      b+1). E\* contains no window cell.
      - Check A (Y∖L atomic) passes at M=3.
      - Check B fails, and its failure is exactly the window cells that lie
        inside E\*∪L (rank 9 = 9). This is Navara's chain at the level of
        interactions: each layer exposes the next.
      - Gate fired (b), and the family was enlarged to finite bands.
  - **Theorem (E\* is not in the carrier) ⟦HAND; corner conditions machine-checked⟧.**
    - Notation: gap(x) = min |xᵢ−xⱼ|; B_n = {gap ≤ n}; C and A are the strict
      cyclic and strict anticyclic sets.
    - Family 𝔉 = {Z : Z Δ E\* ⊆ B_n or Z Δ E\*ᶜ ⊆ B_n, for some n}.
      - It is closed under complement.
      - It contains no window event: a window-(0,1) cell (a,b) with b−a large
        meets both generic C and generic A.
    - **Lift lemma.** Suppose Z Δ E\* ⊆ B_n, f has zero box interaction, and
      f = 0 off Z. Then f is constant on C ∖ B_{2n+1}.
      - Proof: f = 0 on A∖B_n. At a 012-point (a,b,c) with gaps ≥ 2n+2, use the
        box with x₀∈{a,a'}, x₁∈{b,c+n+1} and x₂∈{c,a+n+1}, where a' ≥ c+2n+2.
        Its other six corners are generic anticyclic points, so
        f(a,b,c) = f(a',b,c). That is, the minimum is lifted far above the
        maximum.
      - Rotations give the same lift for the other orders. Each lift moves the
        point to the next rotation class, and enough lifts reach any far point
        of any class, so all generic C-points share one value.
      - **Clean form, without Z:** if f has zero box interaction and vanishes
        on A∖B_n, then f is constant on C∖B_{2n+1}.
      - **Free strengthening:** every corner of a lift box has all
        coordinates ≥ the point's minimum. So B_n can be enlarged to
        B_n ∪ {min coordinate ≤ n}.
      - The E\*ᶜ side follows by the reflection (x₀,x₂,x₁), which preserves the
        windows and swaps C and A.
    - **Main argument.** The class {G : 1_G has zero interaction, G ∉ 𝔉} is a
      Dynkin system containing the generators. The lift lemma is exactly the
      countable-disjoint-union step. Equivalently, take the least stage of the
      λ-hierarchy at which a member Z of 𝔉 appears.
      - Not as a complement: the complement is in 𝔉 and would already be there.
      - Not as a countable disjoint union ⊔Gᵢ: each 1_{Gᵢ} has zero interaction
        (pointwise sums), so by the lift lemma it is constant on Z∖B_{2n+1}.
        Exactly one piece takes all of it, and that piece is in 𝔉 at an earlier
        stage.
      - So **no member of 𝔉 is in D. In particular E\* ∉ D**, and countable
        unions cannot build the cyclic set.
    - **Finite checks.**
      - `triangle_offtie_atomicity.py` (checks A and B).
      - `triangle_lift_lemma_check.py`: 18,000 lift boxes, 0 failures.
      - Band rank checks pass at n=0 (gap>1) and at n=1 (gap>3, both sides),
        At n=1 with gap>2 the check fails at margins 2 and 4 (rank 19 both
        times). That is finite-box evidence that 2n+1 is needed, not a proof.
      - At n=2 the check fails at a 16³ box. That is a top-of-box artifact: the
        lifts need room above the point.
    - **Scope.** This excludes E\* and every finite-band perturbation of it or
      of its complement. **It is not gate (a).** A set can have the cyclic
      ultrafilter profile while differing from E\* on a non-band region that
      is p-small, for example on slices {x₀ odd}. E\* itself shows that no
      statement at the interaction level alone can exclude cyclic behaviour.
      Next: `gate.triangle_lambda2_agreement`.
    - **Lean-checked (2026-10-17):** `formalization/staging/TriangleCyclic.lean`.
      - `estar_not_mem` and `not_inF_of_mem`: 0 sorry; axioms propext,
        Classical.choice, Quot.sound.
      - The carrier is `DynkinSystem.generate` of the three pair windows,
        the same construction as `WindowGluing.glued`.
    - **Prior art (scout, 2026-10-17): NOT FOUND; coverage partial.**
      - Closest work:
        - Navara–Pták 1983 / Navara 1984: the finite cyclic shadow and the
          two-of-three sets, with no infinite exclusion.
        - Fishburn–Lagarias–Reeds–Shepp 1990 and Kemperman 1990–91: additive
          sets, with no λ-closure question.
        - Keleti–Preiss 2000: the same invariant-plus-induction template on a
          different object, so only the method is folklore-adjacent.
      - Not covered:
        - Pták 1987 is a scan and was unreadable.
        - Kellerer 1964 was a stub.
        - The full texts of FLRS and Kemperman were not opened.
        - Ridge functions, Kolmogorov superposition, Sternfeld,
          Marshall–O'Farrell, Hindman–Strauss and MathOverflow were not
          searched.
  - **`gate.triangle_lambda2_agreement` FIRED (b), 2026-10-17 ⟦HAND + check⟧.**
    - Witness: F_S = E\* + [x₀∈S]([x₁<x₀] − [x₂<x₀]).
      - It is a sum of window functions, and 0/1-valued: 40³ points checked,
        0 failures.
      - On slices with x₀ ∈ S it is {x₁<x₂}; elsewhere it is E\*.
      - For S p-small, Λ(F_S) = 2, yet it differs from E\* on the unbounded
        non-band region {x₀ ∈ S}. Script: `triangle_lambda2_counterexample_check.py`.
    - The slice computation behind it: on slice x₀=a, E\* is [s<t] on the
      blocks L×L and H×H (L=[0,a), H=[a,∞)), 0 on L×H and 1 on H×L. The
      additive change [s<a] − [t<a] swaps the off-diagonal blocks.
  - **Stronger route: Λ is two-valued on the triangle carrier ⟦HAND, unverified⟧.**
    - (i) **Representation.** Λ = W₀₁₂ + W₁₂₀ − W₁₀₂ on all of V. Each
      W_π(f_k) is u_k or its reverse, according to whether π puts i before j.
      Rotating the representation gives two more.
      - So Λ = 2 forces the full cyclic profile, and Λ = −1 the full
        anticyclic profile.
    - (ii) **Finding a homogeneous set.** Suppose a 0/1 set F has a bad
      profile. The six order-cell conditions intersect to a set
      Y ∈ p^{⊗3}. The ultrafilter proof of Ramsey's theorem works for every
      non-principal p and gives an infinite P with [P]³ ⊆ Y. On that P, F
      agrees with C (or with A) at every distinct-coordinate point of P³.
    - (iii) **The exclusion family.** Let
      𝔉_∞ = {Z : ∃ infinite P, Z agrees with C, or with A, on the
      distinct points of P³}.
      - Thin P to the even-indexed elements P′, so that a P-element lies
        between any two P′-elements.
      - The lift lemma then runs inside P′ (corner values chosen in P).
      - The least-stage induction goes through as before.
      - No window event, and not ∅, is in 𝔉_∞.
    - **Consequence: no 0/1 set in D has Λ ∉ {0,1}, for any non-principal p.**
      So s\* = Λ is a pointless state on the triangle carrier, which would
      fire gate (a): pointless ⟺ not a forest.
    - **LEAN-CHECKED 2026-10-17:** `TriangleCyclic.triangle_pointless_state`,
      `triangle_state_no_ultrafilter` and `triangle_has_pointless_state`.
      - 0 sorry; standard axioms only.
      - The proof includes an ultrafilter-Ramsey recursion for triples
        (`ramsey3`), since Mathlib has none.
      - Two box identities pin down the pattern (`pat_arith`); a brute force
        found that two suffice.
      - The packaging is simplified: s\* = W₀₁₂ + W₁₂₀ − W₁₀₂ is defined on all
        sets, so no V-decomposition is needed.
    - **gate.triangle fired (a).** With `thm:travel` (its transport ψ covers a
      triangle inside any graph) and the forests theorem: a window graph has a
      pointless state ⟺ it is not a forest. The assembly is by hand; the
      triangle piece is Lean.
    - **Scope:** pair windows over ℕ. Over a finite alphabet every state is a
      point, and a window covering the whole triangle makes the carrier Boolean.
    - **Fidelity (Lean):** `sstar_window01/12/20` show that on every window
      event s\* equals the staircase p⊗p limit in that window's orientation.
      For window 01 the W₁₂₀ and W₁₀₂ terms cancel; for window 20 the W₀₁₂ and
      W₁₀₂ terms cancel. That s\* is the forced functional Λ on finitely built
      questions is hand (`prop:forced`).
    - **Gate leg (ii) was not run:** at definable levels Λ is fixed by the far
      strict atoms, so agreement there is automatic.
    - **Prior art: two budgeted sonnet scouts (2026-10-17), NOT FOUND.**
      - Both were shallow: snippets only.
      - Unread: Navara–Pták-era papers, Gudder, Bhaskara Rao, the
        Hindman–Strauss text, Blass.
      - Residual risk:
        - a folklore non-extendability argument from ultrafilter products
          (non-commutativity of p⊗p);
        - a Navara-style set-representable logic with a non-point two-valued
          state.
      - This was scouting, not the claim gate (workflow step 6).
  - **`/audit pure` (opus, hostile, 2026-10-17): NOT FOUND, UNCLEAR at the
    margin. The ingredients are owned.**
    - **Direct precedent: Dravecký–Šipoš 1980, Ex. 6** (full text read).
      - The flight σ-algebras A_{d₀} ∪ A_{d₁} ∪ A_{d₂} form a σ-class inside
        D₃. It carries σ-additive pointless two-valued states, and the
        staircase steps lie in it.
      - Those states do not extend to D₃. A σ-additive two-valued state on D₃
        is Dirac on each window, and these glue to a point.
      - So the content is the extension to the full λ-closure, which must be
        finitely additive.
    - Navara 1984 (full text read): its chains need a one-sided-bounded
      generator. The triangle is exactly the regime with no base case.
    - **Standard names to use:**
      - point = Dirac/concentrated state;
      - ideal point = coherent (extendable) state, Bhaskara Rao Thm 3.2.10;
      - pointless = non-coherent two-valued finitely additive state;
      - glued carrier = σ-class generated by coordinate sub-σ-algebras;
      - window graph = marginal scheme / measurement cover.
    - **Types:**
      - Type 3: FAIL for now. The method template is Keleti–Preiss. It would
        flip by deciding Navara's two-sided-unbounded regime elsewhere.
      - Type 4: FAIL as vocabulary; the statements are PASS-pending.
    - **Scoped claim:** a non-coherent two-valued finitely additive state on
      the full λ-closure of the three pair windows over ℕ, plus non-membership
      of the cyclic family. Do not upgrade to NOVEL until these coverage gaps
      close: Bhaskara Rao (book body), Gudder SIAM Rev 1984 Ex 3.1,
      Hindman–Strauss, Blass, the Pták–Pulmannová book, Ovchinnikov PAMS 1999.
  - **Finite alphabets: every state is a point ⟦HAND; A=2 enumerated⟧.**
    - Window states on a finite alphabet are principal, and consistent
      marginals glue them to a point ω.
    - The sets where s and δ_ω agree form a Dynkin system, since every disjoint
      union in a finite Ω is finite. So s = δ_ω on D.
    - This holds for any window graph.
    - Check: `triangle_finite_states_check.py 2`: 70 sets, 8 states, 8 points.
    - The claim "D = all 0/1 span elements" over finite alphabets is
      machine-checked at A=3 only.

  - Keleti–Preiss (shelf): their method is a σ-ideal normal form. On discrete ℕ
    any σ-ideal containing the bounded slabs is trivial, so it does not
    transfer directly; it would need a continuum model.
  - **Still open: countably built questions.**
- **Conceptual ring proof (L ≥ 4) ⟦HAND⟧.** Locality gives E = E_{k−1}⊔E_k.
  Cut at a window m that E does not touch, so Λ(E) = W⁽ᵐ⁾(E) ∈ {0,1}; Λ is
  linear, hence a state. This *explains* the `mu_cases` case analysis; Lean
  remains the certificate. It inherits the locality theorem (hand + finite
  checks). Note Theorem `ringconcept`.
- **Cocycle reading:** W⁽ʲ⁾ − W⁽ᵏ⁾ = δ_k − δ_j. This is the first concrete
  form of the "cohomological classification" target.
- **On rings with L ≥ 4:** every question lives on two adjacent windows, so
  cutting at an untouched window gives δ = 0 and Λ = W⁽ᵏ⁾ ∈ {0,1} question by
  question. This is a candidate conceptual proof of the Lean `mu_cases`
  two-valuedness, still unchecked against the Lean proof.
- A finite-alphabet test of the full carrier would be uninformative: there,
  every two-valued state is a point.

## Flagship correspondence, 2026-10-09: winding mismatch; carrier blind at L = 3 — BRIDGE KILLED

Compared against `thm:winding` of `papers/reconstruction/reconstruction_skeleton.tex`
("L unsafe iff the layered ring carries a layer-injective simple cycle of winding
≥ 2"). Oracle: `notes/open_questions/verification/window_gluing_flagship_bridge.py`
(binary rings, pair windows; exact rationals on vertices, float LP on the whole
polytope).

**Verdict: the bridge hypothesis (DAG connector) is KILLED by its own
pre-registered falsifier.** The bridge-hypothesis section above says: "A
mismatch, or always-amalgamating rings, would kill the bridge." The windings do
not match (below). No candidate two-way statement is kept alive here.

**What survives, independent of the bridge:**
- the countable σ-essential witness (`WindowGluing.Ring`, Lean, every L ≥ 4),
  which bears on Q6.6 and the countable-Ω question, with prior art pending;
- the collision→δ open question at the top of this note, which this result does
  not touch.

**Dictionary.**

| flagship | σ-essential lane (Lean defs) | relation |
|---|---|---|
| window table (probability, finite A) | `LocalState` on a `Block` (two-valued) | different value types |
| EA = pairwise marginal agreement | `FinitelyCoherent` = extends to a `FinAddState` on all of the glued D | glued coherence is stronger than EA (L=3 below) |
| PR = global measure on configurations | extends to a σ-additive `TwoValuedState` | on finite Ω both collapse to Diracs / R |
| contextual = C∖R | σ-essential = finitely coherent, no σ-extension | live in disjoint regimes (winding below) |

**Winding: mismatch ⟦HAND, elementary⟧.** The two windings are different
quantities.
- Flagship winding is the net site-advance of a closed walk in the layered graph
  of a *finite* language ρ. Its contextual certificates are winding-≥2 cycles.
- Orientation winding is the sign pattern of the order relation around the site
  ring. For the all-ascent pattern the layered graph (alphabet ℕ, arcs a→b for
  a<b) has **no closed walk of any winding**: the state value is a strict potential.
  Truncated to {0..m} the same potential shows the circulation polytope, which is C
  by the flagship's gate identification, is **empty**. So there is no flagship
  certificate object at all.
- The σ-essential witness lives in exactly that gap. C is empty at every finite
  truncation and impossible σ-additively (equal marginals with P(x₀<x₁)=1), but
  finitely additive ultrafilter tables exist. Mass escapes to infinity.
- Conversely, on a finite alphabet every two-valued finitely additive window state
  is a Dirac, so σ-essentiality is empty there. That is exactly where the
  flagship's winding-≥2 contextuality lives.

**Carrier side: the glued D is EA-faithful iff L ≥ 4 ⟦machine; binary alphabet,
pair windows, L = 3..6 only⟧.** This is a fact about the σ-lane carrier, tested on
flagship data. It is **not** a comparison with the flagship's layer-injectivity,
which was never matched.
- **L = 3:** every odd-parity (PR-box-type) vertex of C fails to be a state on D
  (it gets −1/2 on a set like {000,111}). Over C ∩ {states on D}, every odd-cycle
  functional has maximum 2, its value on R, not 3. So glued coherence on the
  triangle restores the cycle (Boole) inequalities: C ∩ states-on-D = R
  ⟦modulo the classical fact that these inequalities cut out R for the binary
  3-cycle; not re-derived here⟧.
- **L = 4, 5, 6:** all 2^{L−1} contextual parity vertices are states on D, and the
  LP confirms all of C lies inside states-on-D (min over C of every extension
  value on D is 0).

**A second mismatch.** At L = 3 the glued carrier cannot carry the flagship's
smallest unsafe instance, the golden-mean odd-triangle gap from the parity theorem.
The flagship sees contextuality there; the carrier is blind to it.

**Not a shared threshold yet.** The σ-side L = 3 failure is a fact about *this* μ
(see the ring-sweep caveat). The thresholds coincide only if the triangle has no
σ-essential witness at all. The finite L = 3 collapse is evidence in that
direction, and an impossibility proof would plausibly go through the
triple-difference sets of D. ⟦conjecture⟧

**Open, now internal to the σ lane (none of it serves the bridge):**
- the triangle: is there any σ-essential witness at L = 3?
- the converse (mixed orientations are σ-realisable), trivial, for Lean
  completeness;
- the prior-art gate on the countable witness.

## Re-audit 2026-10-09: the collision → δ question against generator theory ⟦HAND; textbook citations, not shelf-verified⟧

New input: the programme hierarchy put this question at the top layer (F,
identification), and its exit criterion names a generator-theory check that had
never been run. Setting: finite-valued h, partition P = h⁻¹, O_L = ∨_{n=0}^{L} T⁻ⁿP.

**(a) The sup form is ill-posed.** O_L is a finite partition. If μ is non-atomic,
each fibre law μ_z is non-atomic, so a set S can split every fibre in half. Then
sup_S δ_L(S) = Σ p_z · ¼ = ¼ at every L. This is a defect in how the question was
stated, not a result.

**(b) The per-S form is classical, for invertible T.**
- *Equivalence.* By martingale convergence, δ_L(S) → 0 for every S ⟺ O_∞ = ℬ mod μ.
  Also C_L = Σ p_z² → 0 ⟺ max_z p_z → 0, i.e. the partitions' atoms shrink.
- *Positive entropy.*
  - A one-sided generator of an invertible system forces h(T) = 0, by the
    Rokhlin/Kolmogorov–Sinai formula h(T,P) = H(P | ∨_{n≥1} T⁻ⁿP) (Walters,
    *An Introduction to Ergodic Theory*, Ch. 4).
  - So for h(T,P) > 0 the forward delays never generate.
  - Meanwhile C_L → 0 by Shannon–McMillan–Breiman, since the atoms decay like
    e^{−hL}.
  - Hence C → 0 ⇏ δ → 0, generically. The hub's hidden-factor skew product is one
    instance.
- *Zero entropy.*
  - If h(T,P) = 0 then P ⊆ ∨_{n≥1} T⁻ⁿP, so O_∞ = T⁻¹O_∞ is a genuine factor.
  - Then "C → 0 ⇒ δ → 0 for every finite-valued observable" holds iff the system
    has no proper non-atomic factor. That is a property of the **system** (prime
    systems; minimal self-joinings: Rudolph 1979; Chacón: del Junco–Rahe–Swanson
    1980), not a condition on Φ_L.
  - For a single observable the condition is generation itself, which is the
    circularity the Statement already forbids.
  - Zero-entropy witness: two independent irrational rotations on 𝕋², observed
    through an arc of the first coordinate. O_∞ is the first-coordinate factor, so
    C_L → 0, while δ_L(S) = μ(S)μ(Sᶜ) for an arc S in the second coordinate.
- *Verdict:* **KILLED** for invertible T, by the exit criterion's own named route.

**(c) Unchecked: endomorphisms.** For non-invertible T the Rokhlin obstruction
fails. The one-sided Bernoulli shift's time-zero partition generates at positive
entropy. The classical home is Rokhlin's endomorphism theory (exactness,
H(P | T⁻¹ℬ)). Not audited here.

**(d) What this does to the breadcrumb.**
- In the real-valued Takens setting a generic delay map is injective for large L,
  so σ-algebraic generation is trivial there.
- What remains of "well-conditioned" is **metric** distortion of the delay map
  (bi-Lipschitz constants). That is a *different* question, not a sharpening of
  this one: no check flipped and no witness exists.
- It plausibly has an occupied literature on stable or geometry-preserving
  delay-coordinate maps (Eftekhari–Yap–Wakin–Rozell is a candidate, **unverified**).
- It is offered to the user as a possible new seed, prior art first. It is not
  carried forward here.

## Metric conditioning: prior-art scout 2026-10-09 — PARTIALLY OCCUPIED

This is a candidate new question, not a sharpening of collision → δ. Scout: one
sonnet agent, about 15 searches. It read theorem statements via ar5iv/WebFetch
summaries and some abstracts only; nothing below is shelf-verified.

**Occupied:**
- **Random observables, general systems.** Eftekhari–Yap–Wakin–Rozell, "Stabilizing
  Embedology", *Phys. Rev. E* 97, 022222 (2018), arXiv:1609.06347.
  - Thm 3.1 gives two-sided distortion bounds for delay maps, with high
    probability over a *random* linear-combination observable.
  - The L-dependence enters through geometric sums in σ_min, σ_max of DT.
  - The paper itself states that large Lyapunov exponents worsen the bounds
    ("stably embedding chaotic systems is often difficult"), and that the stable
    rank plateaus with irrelevance/redundance.
- **Linear systems.** Yap–Rozell, arXiv:1010.5938: the conditioning provably
  **saturates** at a floor δ₀ as L → ∞.
- **Hölder or pointwise inverse regularity:**
  - Hunt–Kaloshin 1999 (linear maps);
  - Robinson 2011 (delay injectivity with thickness);
  - Śpiewak 2025 (pointwise Lipschitz inverse a.e.).
- **Noise amplification.** Casdagli–Eubank–Farmer–Gibson 1991, asymptotic: an
  "explosion" at large dimension and large Lyapunov exponents. Uzal et al. 2011
  is heuristic.

**Not found:**
- a deterministic bi-Lipschitz bound for a *fixed* generic h;
- explicit-constant Hölder-inverse delay theorems;
- lower bounds or obstructions in terms of Lyapunov exponents.

**The "lower bound" gap is probably elementary ⟦HAND sketch, unverified⟧.**
- For a forward delay map on a hyperbolic set, a separation along the unstable
  direction is stretched by ~λ_u^k at lag k, so the upper Lipschitz constant of
  Φ_L grows like e^{λ₁L}.
- Along the stable direction the lag terms decay, so the lower constant stays
  O(1) (generic ∇h).
- Hence cond(Φ_L) ≳ e^{λ₁L}: conditioning *must* degrade exponentially in L for
  chaotic T, while injectivity needs L > 2d. That is a trade-off with an optimal
  window, the rigorous face of "irrelevance".
- It is consistent with Thm 3.1's formula and with the Casdagli et al. explosion.
  It is likely folklore, so it is **not** a candidate contribution without a
  primary-source read.

**What looks open** is the fixed-h, deterministic, explicit-constant
(prevalence-quantitative) bi-Lipschitz Takens theorem. It is heavy technical
analysis, and it does not touch "what coherence forces".

## Extension and classification (2026-10-17)

### (i) Extension is automatic on triangle-free graphs ⟦HAND; a corollary of `thm:star`⟧

Take a finite-degree triangle-free window graph and window ultrafilters u_w with consistent slot
marginals. Then s(E) := Σ u_{w_i}(E_i), summed over a star decomposition of E, is a state. It is
unique and fits the u_w.
- **Same centre.** A full slice can be assigned to either leaf, and the marginals agree. Empty
  slices contribute 0.
- **Different centres.** A set that is a star set at two centres depends only on single
  coordinates or on a shared window, and consistent marginals settle it.
- **Two-valued.** The pieces lie over disjoint x_c-sets, so the sum is at most m_c(union) ≤ 1.
- **Complement.** s(E) + s(Eᶜ) = m_c(S) + m_c(Sᶜ) = 1.
- **Additive.** Disjoint pieces pairwise meet, so with no triangle they lie on one star; regroup
  window by window.

**Consequence.** Every twisted family extends on rings with L ≥ 4. The Lean `mu_cases` is the
staircase instance. On triangle-free graphs the carrier drops out: states are consistent window
families, and pointless means non-amalgamable. Ultrafilters on ℕⁿ are complete n-types over the
full structure on ℕ, so this is type amalgamation. Model-theory prior art is unchecked, and
banking (ii) is blocked on it.

### (ii) Candidate invariant for tensor types (NOT banked)

"A directed cycle of product orders after contracting the bijection windows." Hand sketch:
- *Flat:* the projection of an iterated product to i<j is p_i⊗p_j, and bijection monodromy
  F₊p = p forces Fix F ∈ p (Katětov).
- *Twisted:* a directed cycle gives an empty intersection of {y_i < y_{i+1}}; a single product
  window closed by bijections gives the graph measure 0.
- Blocked on the model-theory pass.

### Probe `gate.triangle_graph_windows` (pre-registered)

The triangle with diagonal, diagonal and p⊗p windows (WLOG via coordinatewise bijections). Does
it extend to D₃?

### `gate.triangle_graph_windows` FIRED (a) ⟦HAND + finite check⟧

- **The family.** Diagonal, diagonal, and p⊗p with x₀ first. Its forced functional is
  Λ = W[01|2] + W[0|12] − W[0|1|2], over ideal buildings indexed by ordered partitions with ties.
  The identity was checked window by window.
- **The patterns.**
  - Box identities allow 32 of the 2¹³ tie-patterns.
  - Exactly 2 of them have Λ ∉ {0,1}: on strict orders, one is anticyclic (Λ=2) and the other
    cyclic (Λ=−1).
  - Lean's `not_inP_of_mem` does not depend on the window family. Together with ultrafilter
    Ramsey over the 13 cells it excludes both. So the family extends, and the state is pointless.
  - Script: `triangle_tie_patterns.py`.
- **Generalised to all 27 tensor-type families** (each window diagonal or a product in either
  order, one slot ultrafilter p). Every pattern with Λ ∉ {0,1} is cyclic or anticyclic on strict
  orders, so every such family extends (`triangle_tensor_families.py`).
  - Twisted families have bad patterns: 2, 6 or 12 of them. Flat ones have none.
  - This is checked mechanically: twisted means the order constraints are inconsistent, so 14
    families are twisted and 13 are flat. My first count, 15/12, included the script's
    summary line. The 14 fall into 3 orbits under S₃.
- **Reading.** Even with a triangle, extension is not the obstruction for tensor types. The
  carrier's one exclusion, the cyclic family, absorbs every twist.
- **New conjecture.** `conj.triangle_extends_all`: every consistent family extends on the triangle.
  - Open for products of distinct ultrafilters and for non-tensor 2-types.
- **Model-theory pass (sonnet, abstracts only).**
  - Forests: folklore.
  - Oriented-cycle failure, the directed-cycle classification, graph-monodromy flatness: NOT FOUND.
  - Model theory owns n-amalgamation over models in stable or simple theories.
  - Gaps: the theorems of Goldberg 2102.04677, Blass's thesis, Puritz, Hindman–Strauss.
- **Lean (layer 3, 2026-10-17).** There is one representative of each of the three S₃-orbits of
  twisted families:
  - the staircase;
  - `triangle_ddp_pointless` (diagonal, diagonal, product);
  - `triangle_dpp_pointless` (diagonal, product, product).

  Each theorem covers: {0,1} on D₃, additive, normalised, equal to its window family on every
  window event, and no ultrafilter fits. 0 sorry; standard axioms.
  - Minimal boxes: 3 for `ddp`, 2 for `dpp`. They were found by brute force and generated by
    `formalization/tools/gen_triangle_family.py`.
  - Transport to the remaining 11 twisted families by coordinate permutations is hand.
