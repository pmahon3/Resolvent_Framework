# Case 1b (PROBE DESIGN): where infinity enters the three-species cycle (2026-10-19)

reviewed: false. This is a probe design with a pre-registered gate (`gate.case1b_depth_types`).
Nothing here is a result. It is a companion to `case_heteroclinic_averages.md`.

## 0. The pushback this starts from (category check, done)

- Case 1's stations record **which species is dominant**, which has finitely many outcomes. Long-run
  averages of that are probability charges on a finite space.
- That is regime (i), finite and probabilistic, where the failure is *visible*: P(no species
  dominant) = −0.2. It is owned contextuality (`definitions_draft.md` §9b).
- Letting time run to infinity changes the *epochs*, not the number of values a query takes. **So
  case 1 as modelled cannot reach regime (ii).** The case pushes back on the proposed probe.

## 1. The infinite-valued variable: depth of rarity

- **What an observer logs.** The order of magnitude of a species' abundance:
  n_i(t) = ⌊−log₁₀ x_i(t)⌋, i.e. "how many decades down is species i?". Survey ecologists do log
  abundances on a log scale.
- **Why it is unbounded.** Near the attracting heteroclinic cycle each dip is deeper than the last,
  so n_i is unbounded along the orbit. **memory/standard; check against Gaunersdorfer**
- **Honest distance, and the point of the case.** Real populations are finite. A species dipping
  many decades goes extinct, and noise near heteroclinic cycles stops the slowing-down
  (Stone–Holmes 1990; Barendregt–Thomas, *J. Math. Biol.* 2023, which says each species gets
  "closer to zero with each cycle" and that discrete populations reach zero; see the ecology
  sweep, 2026-10-20). So **the unbounded depth IS the idealisation**: the
  continuum-abundance, infinite-population model. This is WHY.md's question 3 in a concrete form:
  does that idealisation hide a contradiction among the stations?

## 2. The regime, chosen explicitly

| Regime | Station report | Theory location |
|---|---|---|
| **Two-valued (chosen)** | the ultrafilter limit of (n_i(t), n_j(t)) along the station's own time ultrafilter: a 2-type on ℕ² | regime (ii) proper |
| Probabilistic (NOT this probe) | Banach-limit long-run distribution of (n_i, n_j) | the impossible-point question (`gate.triangle_density_plus1`), not (ii) |

## 3. Hand reduction (partial) ⟦hand, unverified⟧

- **During a passage near vertex k**, log-abundances are nearly linear in time. The species k beats
  sinks at rate a, the species beating k rises at rate b (replicator matrix with entries −a, b).
  In lap L, at time s into the passage:
  n_beaten ≈ E_L + a·s and n_beater ≈ D_L − b·s, with D_L, E_L growing geometrically in L.
- **So a pair value does not fix the time.** A fixed value of one depth recurs in every deep enough
  lap, with a different partner value each time. **The station types are not renamings.** The
  Katětov/renaming shortcut (note §5) does not settle the probe.
- **Three candidate type shapes**, depending on where the station's epoch sits in the passage:
  - (α) the ratio n_j/n_i tends to some c ∈ (0, ∞): approximate scaling, neither renaming nor
    "beyond";
  - (β) c = 0 or ∞: a "beyond" type;
  - (γ) the epoch straddles laps in a way that gives sum-like types (L first, then s).
- **Not yet checked:** whether any of these is *forward* (FinBack), which `triangle_glues_iff`
  needs. Non-forward types are the note's stated open edge.
- **Marginal agreement is a real constraint.** Stations sharing species i must induce the *same*
  ultrafilter on n_i. The depths of i during different phases of the cycle sweep a common
  infinite range, so this looks arrangeable. ⟦hand, unchecked⟧

## 4. Gate (pre-registered 2026-10-19): `gate.case1b_depth_types`

| Outcome | Meaning | Bears on |
|---|---|---|
| **A** | no choice of epochs gives overlap agreement with a twist | the case pushes back: infinity in this idealisation does not create pointlessness |
| **W** | every overlap-agreeing choice glues (a world exists) | as A, more strongly |
| **Tv** | twisted, and some askable question exposes it | the composition law (`conj.composition_law`) applies to dynamical types |
| **Th** | twisted and hidden: pointless | infinity alone (the continuum idealisation) hides what finite stations would see; links regime (ii) to experience |
| **Stuck** | the types are non-forward and the theory can't decide | records a concrete instance of the open edge |

**Order of work:**
1. Classify the pair types (α/β/γ, and FinBack) by hand from the linearised passages.
2. Only then consider any computation, within the compute rules.

**If a dynamical quantity (e.g. the saddle-ratio product (a/b)³, which governs whether the cycle
attracts) turns out to play the role of holonomy: do NOT name or claim it.** Shelf first, then a
hostile web pass over the heteroclinic-cycle literature (Krupa–Melbourne and others). Assume it is
owned until shown otherwise.

## 5. Hand classification, first pass (2026-10-20) ⟦hand, unverified; floors ignored⟧

**Linearised passages.** Visit order 1 → 2 → 3. Let c = a be the decay rate and e = b the invasion
rate, ρ = c/e > 1 (the cycle attracts). Passages are numbered t = 0, 1, 2, … and each has a scale
M_t ≈ M₀ρᵗ. In passage t (at vertex k), s ∈ [0, M_t/e] time in:
- the invader k+1 has depth M_t − e·s;
- the decliner k+2 has depth c·s;
- k itself has depth ≈ 0.

A station sees two unbounded depths only when the *third* species dominates:
- (1,2) during passages at 3;
- (2,3) during passages at 1;
- (3,1) during passages at 2.

**R1. Every station type factors through the passage counter t, with finite fibres.** A pair of
depths fixes t (the segments x + (e/c)y = M_t are geometrically spaced). Each passage holds only
finitely many pairs. So a station's report is a lap ultrafilter p on t, together with "where in the
passage".

**R2. Fixed-fraction types are renamings, and then a world exists (W).**
- Suppose a station sits at a fixed fraction θ of each passage. Its pair is
  ((1−θ)M_t, ρθM_t), and each depth determines t, so the type is a renaming.
- Overlap agreement can be arranged. Equal marginals need matching constants up to powers of ρ
  and shifted lap ultrafilters, and the loop condition
  θφψ / ((1−θ)(1−φ)(1−ψ)) ∈ ρ^(3ℤ) can be met.
- Once the marginals agree, Katětov forces the loop's composite renaming (a lap shift) to be
  trivial. So the triangle glues: **W**. This is note §5 ("renaming never twists for yes-or-no
  answers") appearing in the dynamics.

**R3. Not settled.**
- (i) Section types whose single depth does not fix t: the position in the passage varies
  irregularly with t.
- (ii) Non-section types. These exist only if the lap ultrafilter p is not a Q-point-like
  ultrafilter for the finite-to-one map to t. They are genuinely sum-like within a lap, which is
  the only place a twist could hide.

Gate status: **partial, not fired.** W on the fixed-fraction subclass; the rest is *Stuck* (the
non-forward open edge).

**What the case says (equilibrium, not a claim).** The heteroclinic lap counter t acts as a
**shared clock** for all three stations. Every report factors through it, and on the natural
subclass that forces a world. This is the same shape as case 3, where Newtonian shared time
forced a world. *Shared time forces a world* now has two instances. A twist would have to hide in
how a station places itself *within* a lap, beyond what any regular reading of the clock fixes.
