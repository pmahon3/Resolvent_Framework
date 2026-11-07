# Equilibrium gates: definitions vs intended meaning (convex gluing framework)

reviewed: false. 2026-11-06. Set by the user's request: definitions and the semantic content of the theorems must be brought into reflective
equilibrium (cf. memory feedback-reflective-equilibrium: generalisations must survive concrete applied cases before they are recorded as theory).
**Rule:** a definition passes a gate only if it classifies every test case as intended. On a failure, revise the definition *or* the intuition, and record
which and why. No theorem in `CONVEX_GLUING_FRAMEWORK.md` is stated as settled until its definitions pass.

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
  *no-twist ⇒ ordinary or ideal point*. **Decision owed (user).**

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
| G4 pointless | tension: **decision owed** (recommend: ideal points are not pointless) |
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
