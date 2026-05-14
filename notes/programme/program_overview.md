# Structure from Observation — Programme Overview

## The Central Question

When an observer makes structured observations of a system — querying it at
increasing levels of refinement, recording outcomes, building a picture of the world
through measurement — what does coherence require of them?

The programme shows that coherence, pursued to its conclusion, requires probability,
dynamics, and reconstruction. Not as additional assumptions, but as what the
structure of observation already contains.

---

## The Three Papers

### Paper I — Probability from Observation

**What it shows:** A coherent family of observations determines a unique probability
measure on the observable σ-algebra.

**The argument has three routes, each illuminating a different facet:**

1. **Carathéodory route:** Bounded discriminability forces the observable distinctions
   to have σ-algebraic structure. Collective exhaustion (CE) — the condition that mass
   does not persist in events the completed observation sees as empty — is the
   irreducible condition that bridges structural coherence and probability. CE cannot
   be derived from any structural condition (proved via Łoś's theorem + finite-cofinite
   counterexample); it is a commitment the observer makes about the infinite, not a
   consequence of finite consistency. Given CE, compatible marginals extend uniquely to
   a global measure via Carathéodory.

2. **Stone duality route:** The same extension theorem approached from the other
   direction. Finite additivity on the cylinder algebra, combined with the compactness
   of the Stone space, yields σ-additivity without assuming it. CE reappears here not
   as an algebraic condition but as a support condition: the measure concentrates on
   the principal ultrafilters — on the image of the sample space inside its Stone
   compactification. The two routes illuminate the same theorem from opposite sides.

3. **The bridge:** The Stone space of the observable algebra is the natural compact
   completion of the sample space. This observation connects Paper I to Paper II: when
   reconstruction holds, the Stone space *is* the state space.

**CE metatheorem (companion note):** The same ultraproduct argument shows the
obstruction is not an artifact of the query-system formalism — in the more primitive
first-order language of Boolean algebras with finitely additive charge, countable
additivity is likewise not first-order axiomatizable. Companion note (3 pages,
APAL target) proves this in full.

**Lean:** `DiscriminabilityFoundations.lean`, `QuerySystem.lean`,
`StoneDualityExtension.lean`, `TopologicalQuerySystem.lean`,
`ProkhorovExtension.lean`, `DelayEmbedding.lean`

**LaTeX:** `papers/paper_i/probability_from_observation.tex` (arXiv-ready, 8 pages;
revised 2026-05-09 — four-way main equivalence theorem added in §6)

---

### Paper II — Dynamics and Reconstruction in the Observable Measure

**What it shows:** Given a probability measure on the observable σ-algebra, the
dynamics and reconstruction structure of the system are uniquely determined —
read off from the measure, not constructed by the observer.

**Register:** Disclosure, not construction. The structures are *in* the measure.

**Part 1 — Conditional regularity and dynamics:**

The Rokhlin disintegration of any two observations Q, F gives a Markov kernel
κ_Q(q,·) = P(F ∈ · | Q = q) — forced by the measure, not chosen. Composing with Q
gives the minimal sufficient factor Q_*, the coarsest reduction carrying full
conditional information. Indexing over time, temporal coherence forces
Chapman–Kolmogorov — derived, not assumed — yielding a Markov semigroup {Π_t} and
Koopman–Perron duality ∫ K_t g dμ = ∫ g d(P_t* μ). When kernels are Dirac measures,
K_t collapses to the classical Koopman operator.

**Notation:** κ_Q = conditional regularity kernel (disintegration layer);
Π_t = time-indexed semigroup kernels; K_t = operator layer. These are kept
notationally distinct throughout.

**Part 2 — Reconstruction:**

For an invertible measure-preserving system (X, ℬ, μ, T) with h ∈ L^∞, define the
observable algebra 𝒪_h = σ({h ∘ T^n : n ∈ ℤ}). The following are equivalent:
1. 𝒪_h = ℬ mod μ
2. alg{h ∘ T^n} is dense in L^2(X, μ)
3. The delay map Φ_h : X → ℝ^ℤ is a measure-theoretic embedding

The density bridge (Lemma 4.3) connects (1) and (2). The Stone space identification
closes the loop with Paper I.

**Lean:** `PredictiveState.lean`, `PredictiveOperators.lean`,
`ReconstructionTheorem.lean` (0 sorrys), `DelayEmbedding.lean`

**LaTeX:** `papers/paper_ii/dynamics_and_reconstruction.tex` (~11 pages, editorially
polished; arXiv pending Paper I upload)

**Added 2026-04-29:**
- `Definition II:def:faithful` — "faithful modulo μ" formally defined at the
  point where prose motivates it; reconstruction question cast as the faithfulness
  question about Φ_h
- `§Discussion` — synthesis section closing the paper: names the three-step
  disclosure arc, states that the Stone space of Paper I collapses onto X when
  Φ_h is faithful, hands the certification question to Paper III

---

### Paper III — WITHDRAWN

**Status:** Canned (2026-05-13). Novelty audit revealed rediscovery throughout:
residual autocorrelation = Billings-Voon (1986), FNN noise sensitivity =
Rhodes-Morari (1997), elbow stopping = Lepski (1991).

**LaTeX:** `papers/archive/paper_iii_withdrawn/` and `papers/archive/paper_iii_canned/`

**Updated 2026-04-29:**
- `\ifdraft` conditional: `\draftfalse` in standalone (sketch proofs for arXiv),
  `\drafttrue` in `combined.tex` (full proofs for monograph). Three standard-technique
  proofs gated (McDiarmid/Rademacher concentration, NW bias, Sard-Smale d_eff);
  all conceptually novel proofs remain inline in both builds.
- Abstract compressed to 3 paragraphs (was 4); transitional paragraph merged into
  theorem-list paragraph.
- `Remark III:rem:info-horizon` (§3): information horizon L* = ⌊log₂n⌋ derived
  from first principles; makes fibre-dilution explanation explicit.
- `Remark III:rem:lyapunov` (§9): observable separation exponent λ_h = λ_1 μ-a.e.
  under bi-Lipschitz reconstruction; Paper III closes the deferred Lyapunov claim
  from Paper II Remark II:rem:lyapunov.
- **Re-evaluation resolved (Direction 1):** fibre-dilution picture made explicit
  via the information horizon remark; no structural reframing. Three-theorem spine
  retained.

---

## The Through-Line

Each paper takes the output of the previous as input:

```
Structured observations
    → [Paper I]   → probability measure P on (Ω, σ(CylGen))
                    Stone space St(C) as compact completion of Ω
    → [Paper II]  → conditional regularity kernel κ_Q; semigroup {Π_t}; K_t
                    reconstruction: St(𝒪_h) ≅ X when 𝒪_h = ℬ(X) mod μ
    → [Paper III] → finite-sample: δ̂ stopping rule achieves minimax rate
                    three witnesses certify reconstruction from data alone
```

The unifying object across all three papers is **observational indistinguishability**:
- Paper I: events that never separate across refinements (failure of CE)
- Paper II: identical conditional regularity (κ_Q(q,·) = κ_Q(q',·)); same delay orbit (Φ_h(x) = Φ_h(x'))
- Paper III: same delay vector at lag L — (x,x') ∈ R_L

The programme is complete when δ(L) → 0: the observable σ-algebra generates
the full σ-algebra. Note: this is strictly stronger than collision convergence
(μ⊗μ)(R_L) → 0, which only measures geometric fibre refinement. The bridge
theorem claiming their equivalence under fibre mixing is false (2026-05-14).

---

## The Three Obstructions

| Paper | Obstruction | Status |
|-------|------------|--------|
| I | Lack of CE | Proved irreducible (Łoś + finite-cofinite counterexample) |
| II | Lack of density (𝒪_h ≠ ℬ mod μ) | Characterised by density bridge |
| III | Hidden factor obstruction | Bridge theorem false; geometric ≠ algebraic |

**Updated 2026-05-14:** The bridge theorem (algebraic ↔ geometric reconstruction
under fibre mixing) is false. The core identity has a disintegration error (p_z
vs p_z² weighting). The skew-product counterexample (X = A^Z × B^Z, h(a,b) = a₀)
shows collision → 0 while δ = 1/4. The active direction is now a
negative/clarification note proving geometric and algebraic reconstruction are
inequivalent.

---

## Submission Status (updated 2026-05-14)

| Paper | Status | Target |
|-------|--------|--------|
| Companion note | arXiv-ready, 3 pages | APAL |
| I | Synthesis, not novel. arXiv-ready, 7 pages | Expositiones |
| II | EA/PR/VDR framing novel; math classical. 9 pages | Synthese |
| III | Withdrawn (rediscovery) | — |
| Fibre mixing | Dead (bridge theorem false) | — |

---

## Open Mathematical Frontiers

Ordered by downstream leverage:

**No active standalone leads as of 2026-05-14.**

Previously listed directions closed or parked:
- Geometric ≠ algebraic reconstruction — known/obvious (audited)
- Entropy witness concentration — dead (depended on false bridge theorem)
- Fibre mixing derivability — dead (bridge theorem false)

Remaining signposts (not projects):
1. **CE as sheaf condition** — stalled seed, needs fresh approach.
   See `notes/unsorted/ce_as_sheaf_condition.md`.
2. **Strategy D** — ZFC methods exhausted; likely independent.
   See `notes/unsorted/foundations/ce_nonderivability/index.md`.
3. **OML extension problem** — genuinely open, needs OML expertise.
4. **Foundational topology / zeta** — post-arXiv, speculative.

---

## Repository Layout

- `papers/paper_i/` — Paper I (synthesis, expository)
- `papers/paper_ii/` — Paper II (EA/PR/VDR, strongest contribution)
- `papers/archive/` — all withdrawn/canned/dead papers
- `formalization/QuerySystem/QuerySystem/` — Lean source files
- `notes/knowledge_map/` — research control panel
- `notes/reading_directions/` — guided reading with questions
- `notes/programme/` — programme-level docs
- `.claude/agents/` — 7 custom agents
