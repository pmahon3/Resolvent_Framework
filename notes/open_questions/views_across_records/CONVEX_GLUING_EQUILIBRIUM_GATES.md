# Equilibrium gates: definitions vs intended meaning (convex gluing framework)

reviewed: false. 2026-11-06. Set by the user's request: definitions and the semantic content of the theorems must be brought into reflective
equilibrium (cf. memory feedback-reflective-equilibrium: generalisations must survive concrete applied cases before they are recorded as theory).
**Rule:** a definition passes a gate only if it classifies every test case as intended. On a failure, revise the definition *or* the intuition, and record
which and why. No theorem in `CONVEX_GLUING_FRAMEWORK.md` is stated as settled until its definitions pass.

*Terminology (added 2026-11-06, terminology pass).* "Flat" below = **globally glued / amalgamable**: the window family has a global section (Abramsky–Brandenburger 2011), here one ultrafilter on Ω. New text uses that term; "flat" was dropped because a flat connection can still have holonomy round a loop. Records below are kept as written. See `../../programme/TERMINOLOGY_CROSSWALK.md`. "Frustrated" (correlation sense) = **not antibalanced**: signs not multiplying to (−1)^{length}, i.e. frustration of −R, the reverse of the signed-graph usage on triangles (Toulouse 1977; Zaslavsky; Harary 1953 says "unbalanced").

## G1. "Ordinary point" (P)
- **Intended meaning:** a global state realised by an actual configuration of the world. "There is a world behind the answers."
- **Test cases:** (a) a Dirac state on a configuration → ordinary; (b) a free ultrafilter on ℕ (the invisible dictator) → **not** ordinary; (c) an extreme
  Gibbs measure of the Ising model (a pure phase) → ?; (d) a σ-additive mixture of configurations → in conv‾(P), not itself a point.
- **Status: FAILS as a single notion.** Case (c) separates two meanings. An extreme Gibbs state is σ-additive (a genuine probability law on
  configurations) but not a Dirac point. **Revision:** split into P_Dirac (configuration) and P_normal (σ-additive extreme state). "Pointless" must say
  which. For yes/no (two-valued) states the two coincide (two-valued σ-additive ⇒ Dirac on the relevant algebra), so the programme's existing results are
  unaffected. For probabilistic instances, P_normal is the intended notion ("a σ-additive world"), and P_Dirac would make every non-degenerate Gibbs
  phase "pointless", which is not the intended meaning.

## G2. "Locally ordinary"
- **Intended meaning:** each local view, taken on its own, could have come from an actual world. Any strangeness is not inside a single view.
- **Test cases:** (a) the pointless triangle (programme, Lean) → locally ordinary (each window's answers are realised); (b) consensus via a free ultrafilter
  → **not** locally ordinary (the idealisation sits inside each view's tail); (c) a finite-window marginal problem with finite alphabets → always locally ordinary.
- **Status: PASSES (a)–(c) with the draft definition** (x_C ∈ conv‾(P_C), P_C = ordinary points of K_C), provided P_C uses the G1 split. To recheck against
  the T1 attempt's formal version.

## G3. "Twist" (the obstruction on cycles)
- **Intended meaning:** local views that are each fine but cannot be continued consistently around a loop. "The twist lives in the loop."
- **Test cases:**
  - (a) the parity twist on a finite binary ring (three pairs agree, one disagrees) → twisted, and existence fails;
  - (b) the pointless triangle → twisted, existence holds (a state exists), location fails;
  - (c) consensus on a ring → **untwisted**;
  - (d) a calibration loop whose factors multiply to ≠ 1 → twisted (group-valued);
  - (e) correlation patterns on a frustrated triangle → twisted in the ℤ₂ sense (Boman), and antibalanced supports → untwisted;
  - (f) any acyclic cover → untwisted by definition.
- **Status: PENDING.** One definition must cover the group-valued holonomy (d), the ℤ₂ sign class (e) and the two-valued case (a, b), and distinguish
  existence failure (a) from location failure (b). Candidate: the Čech obstruction class of the local-point choices (Abramsky–Mansfield–Barbosa style),
  with its known false positives and negatives. Awaiting `CONVEX_GLUING_T1_ATTEMPT.md` and `CONVEX_GLUING_PRIOR_ART.md`.

## G4. "Pointless"
- **Intended meaning:** the answers cohere (a global state exists), yet no world stands behind them, not even "at infinity" in the ideal-point sense.
- **Test cases:** (a) the pointless triangle → pointless; (b) consensus via a free ultrafilter → **not pointless**, it is an *ideal* point (the seam B
  verdict); (c) any σ-additive glued state → not pointless.
- **Status: TENSION.** The draft defines pointless as F_x ∩ conv‾(P) = ∅. Under that definition (b) *is* pointless (a free ultrafilter is not in conv‾(P)),
  which contradicts the intended meaning, where an ideal point counts as a point "at infinity". **Two ways out:**
  - (i) *revise the definition*: pointless = the fibre contains no ordinary point **and no ideal point**, i.e. no extreme state of the Stone/βℕ kind. That
    needs a general notion of "ideal point" in a convex gluing system;
  - (ii) *revise the intuition*: accept that ideal points count as pointless and split T1 into "ideal" vs "twisted" sources.

  Recommendation: (i). It matches the WHY reading ("consensus has a centre at infinity, pointlessness needs twist") and makes T1 sharper:
  *no-twist ⇒ ordinary or ideal point*. **DECIDED 2026-11-07 (user): (i).** Ideal points count as a centre at infinity, so a
  state reached through an ideal point is *not* pointless. The user notes this leaves room for philosophical quibbling
  (is a point at infinity a centre?) but is the same in practice either way: T1 reads *pointless ⇒ twisted (non-flat)*.

## G5. "Gauge" (existence budget) and T3
- **Intended meaning:** how far the data are from what the hypothesised structure can produce, in units where 0 means "explainable".
- **Test cases:** ε* on the parity ring = 1/4 (known); V_G on Poland ≫ 0 (common cause needed); V_G on an antibalanced support ≤ 0 always (Boman).
- **Status: PASSES** (all verified in earlier work).

## G6. "Uniqueness" (T2 territory)
- **Intended meaning:** the local views determine the world.
- **Test cases:** Ising below the critical temperature → non-unique (two phases); K₄ minimal centres → non-unique explanation; Manchak spacetimes → non-unique;
  a Gaussian triangle at the boundary of FW₂ → unique decomposition (?).
- **Status: PENDING.** It needs a choice: uniqueness of the global *state* (fibre) vs uniqueness of the *structure* (which hypergraph). These are different
  questions. Gibbs and Manchak are about the state; K₄ is about the structure. **Revision proposed:** keep T2 about the fibre only, and treat structure
  non-identifiability as a separate (owned) phenomenon.

## Summary
| gate | status |
|---|---|
| G1 ordinary point | revised: split P_Dirac / P_normal |
| G2 locally ordinary | passes (to recheck) |
| G3 twist | pending (needs a unified definition) |
| G4 pointless | **decided 2026-11-07: (i)**, ideal points are not pointless |
| G5 gauge | passes |
| G6 uniqueness | revised: fibre only |

## Update after the prior-art check (2026-11-06, `CONVEX_GLUING_PRIOR_ART.md`)
- **Framework definition: OWNED.** Abramsky–Brandenburger distribution presheaf; Kharoof–Okay (TAC 2025) convex-categorical version; the existence /
  uniqueness / extremes agenda belongs to marginal-problem theory (Kellerer; Douglas–Lindenstrauss–Winkler) and Gibbs theory (Georgii; Dynkin).
  "Location" is handled per instance; no uniform definition was found.
- **G2 REVISED (my verdict was wrong):** with the weak* closure, conv‾(P_C) = *all* finitely additive states, so every state, free ultrafilters
  included, is "locally ordinary". The definition is vacuous there. With the σ-additive closure, gluing also needs compactness (standard Borel),
  independent of twist. **G2 now FAILS; it needs a non-vacuous notion** (e.g. countably additive *and* tight, or "realised by a finite configuration
  on each window").
- **G3 informed:** cohomological (Čech) twist has false negatives. A full-support CHSH-violating model has trivial cohomological twist and no joint.
  So "twist" cannot be the cohomology class if T1 is to hold. Either twist = the full convex obstruction (then T1 is near-circular), or T1 must
  assume F_x ≠ ∅. **Strong T1 is FALSE.**
- **T3: OWNED** (Fang–Santos 2019 §4; Fang & Seo, Econometrica 2021).
- **Surviving residue R:** on a cyclic cover with infinite local algebras, does trivial *ultrafilter holonomy* force coherence (a σ-additive / ordinary
  global point)? First check the shelf witnesses (Dravecký–Šipoš Ex. 6; Navara–Pták 1983) for trivial holonomy; Kellerer 1964 §§3–4 is unread.

## Update after the T1 attempt (2026-11-06, `CONVEX_GLUING_T1_ATTEMPT.md`; machine-assisted, ⟦HAND⟧, not independently checked)
- **T1 as drafted is a tautology.** With "locally ordinary" = principal on each window, compatible principal views give a point a, and δ_a is in the
  fibre. With the weak* reading it is false (consensus ultrafilters).
- **G3 resolved by a definition:** twist := **non-flatness**. A window family is *flat* if it glues to one ultrafilter. This separates the pointless
  triangle (twisted) from consensus (flat). Principal families are always flat.
- **Restated T1:** *no pointless state has a flat window family.* This is the programme's own open question O1 (`conj.window_restriction_r`: does the
  window family determine the state?) in other words.
- **Proved (⟦HAND⟧):**
  - (i) a linearly extending state is determined by its window family (via the triangle Box identity `box_of_mem`, Lean);
  - (ii) restated T1 holds on triangle-free finite graphs, incl. every ring L ≥ 4 (via `thm.shape_lemma`);
  - (iii) finitely many sites + countable alphabet: a finitely additive gluing of σ-additive marginals is σ-additive.
- **Open:** the triangle with an infinite alphabet. A counterexample must be a non-linear state. Such states exist on concrete logics (De Simone–Navara–Pták
  Ex. 2.2, identity checked by script), and a triangle counterexample would transport to every graph containing a triangle.
- **G4 (pointless) decision now concrete:** with twist := non-flat, recommendation (i) reads "pointless ⇒ twisted (non-flat)", and the flat (ideal-point)
  case is exactly "not pointless".

## Independent check of the T1 attempt (2026-11-06, `CONVEX_GLUING_T1_CHECK.md`): no item wrong
- (i) Lemma A + Prop B: **CORRECT WITH FIXES.**
  - `box_of_mem` = the 8-corner identity for X = ℕ on the triangle only (it matches the 7-term formula). The other alphabets, general graphs and Prop B are
    routine hand steps.
  - s = Λ holds for *finitely built* sets for any state (on all of D if X is finite), so "finitely built" must be stated.
  - Cite `triangle_pointless_state`, not the ring staircase.
- (ii) Prop C (triangle-free graphs): **CORRECT** given the shape lemma (hand-proved; prior art UNCLEAR). "V finite" is used only for finite degree.
- (iii) Lemma E: **CORRECT and KNOWN** (folklore: *Theory of Charges* + tightness).
  - My suspected diagonal-coupling counterexample fails: any coupling of σ-additive marginals on ℕ×ℕ is tight.
  - Scope fix: Lemma E needs a charge on all subsets of Ω, while states live on D. So "gluing is automatically σ-additive" holds only for *coherent* states.
- Script cross-check (binary triangle): |D₃| = 70; 7-term formula everywhere; no singleton in D₃; states determined by window values.

## Prior art on the restated T1 (2026-11-06, `CONVEX_GLUING_T1_PRIOR_ART.md`)
- **No shelf witness falsifies it.** Every printed pointless state has a **non-flat** (twisted) window family, checked fibre by fibre at full-text read level:
  Navara–Pták ℚ², Dravecký–Šipoš Ex. 6, De Simone–Navara–Pták Ex. 2.2, Navara 1984 ℤ×ℕ₀.
- **Q1, determination by generating blocks: PARTLY OWNED.**
  - σ-additive form (Navara–Pták 1983 Thm 1 proof; Navara 1984 Prop.): any counterexample must be *purely finitely additive*.
  - Finite carriers: trivial. Finitely built sets: `obs.forced_functional`.
  - The general form is false (free ultrafilters on the finite–cofinite algebra), so on D₃ the link "determined ⇔ not pointless" rests on the
    ⟦HAND⟧ Lemma A / Prop B.
- **Q3:** printed non-linear states are finite or σ-additive, and there non-linear forces non-flat (⟦HAND⟧). Nothing found on the infinite triangle.
- **Remaining open case = a purely finitely additive two-valued state on D₃ over an infinite alphabet** (the attempt note's gate).
- **Book pointers (not yet blocking):** *Theory of Charges* §3.2 (Horn–Tarski; a signed version?), Thm 3.5.1(v), any uniqueness-of-extension result.
  Pták–Pulmannová 1991: no table of contents online; sections listed by topic.

## Infinite-triangle attack (2026-11-06, `TRIANGLE_GATE_ATTEMPT.md`): neither proof nor counterexample; one rung proved ⟦HAND⟧
- **Level-1 rigidity (⟦HAND⟧, finite scripts):** two two-valued states with the same window family agree on D¹ (countable disjoint unions of
  window-event unions, and complements). Any alphabets; flatness not used. Gives s = Λ_u where Λ_u is a state (flat, principal, staircase).
- Also:
  - principal case: s = δ_a ⟺ s is σ-additive on D₃;
  - over ℕ, D₃ ⊊ box sets (E* is a 0/1 pair-sum not in D₃);
  - the De Simone–Navara–Pták Ex. 2.2 transport collapses into the same blocker.
- **Counterexample shape:** at the first level k+1 ≥ 2 where two same-family states differ, F = H ⊔ ⊔ₙ(Ω∖Hₙ), with H, Hₙ ∈ Dᵏ and the Hₙ pairwise co-covering.
- **Blockers:**
  - **L1:** an alignment / normal-form lemma for complements at the next level (needed at every level).
  - **L2:** rigidity when one vertex is finite with m ≥ 3 values (proved for m = 2).
  - **L1′ shortcut:** "a two-valued state σ-additive on each of three σ-algebras is σ-additive on their Dynkin join" (settles the principal case only).
  - Likely owners: the pinned hardcopies (Pták–Pulmannová 1991 concrete-logic chapters; *Theory of Charges* Ch. 3 §3.2). Exact locations unverified.

## 2026-11-10: triangle gate closed YES (supersedes the blocker list L1/L2 above)

- **Result.** D₃ = D_fin on the triangle, any alphabets: every carrier set is three window events ⊔ one finite-grid
  pattern. Hence O1 holds on the triangle: the window family determines the state. Restated T1 holds there.
- **Evidence.** hand proof, re-derived by two independent agents (`TRIANGLE_5DE_CHECK.md` C6; `TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`: CONFIRMED WITH FIXES); steps 1–2 machine-checked in `formalization/QuerySystem/QuerySystem/TriangleFinitary.lean`, steps 3–4 `sorry` there; Lean alphabet ℕ; prior art NOT searched (Pták–Pulmannová 1991 hardcopy check pending); not claimed as new.
- **Still open.** Graphs properly containing a triangle; O2 (which families extend) and O3. Residue R: its condition
  "O1" is discharged on the triangle; the ring-extension condition remains.
- **Record.** `TRIANGLE_D3_DFIN_REVERSAL_CHECK.md` (repaired proof), `TRIANGLE_GATE_ATTEMPT.md` (banner).
