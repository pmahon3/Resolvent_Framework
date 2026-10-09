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

## Candidate witness on the glued 4-ring (2026-10-08) — now LEAN-CHECKED, prior art PENDING

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
