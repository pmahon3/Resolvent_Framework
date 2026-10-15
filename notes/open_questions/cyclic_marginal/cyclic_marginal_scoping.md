# The cyclic marginal problem as the programme's underlying object: claim check and points of tension

*Written 2026-10-15. Scoping and tension note. No contribution type is claimed.
Inputs:*
- *deep-research run `deep_research_2026-10-15.json` (this directory);*
- *the primary sources read for this note: Pivato 2001 and ABKLM 2016 (both on the shelf);*
- *`papers/reconstruction/notes/PRIOR_ART_VERDICT.md`.*

## 1. The claim, as the user put it

> The cycle marginal problem underlies most of what the investigation has been
> driving at.

**Verdict: it holds, and more broadly than first stated.**

| lane | is it the cyclic marginal problem? | where |
|---|---|---|
| flagship, C vs R | Yes, literally. It is LOCAL(G) vs MARG(G) on a ring of windows, and a gap needs a cycle (Vorob'ev 1962, BFMY 1983). | `PRIOR_ART_VERDICT.md` |
| winding criterion, forcing lemma, reach lemma | Yes. This is the shift-structured, all-lengths version: rings over a symbolic language ρ. | skeleton `thm:winding`, `lem:reach` |
| layer E (process) | Yes, through the periodic quotient (see §3). | `hierarchy_and_open_space.md` |
| σ lane, countable witness | **Yes.** On every ring L ≥ 4 the witness is the ultrafilter form of a cyclic marginal obstruction (below). | `collision_vs_generation.md` §"The pattern"; Lean `WindowGluing` (7826c20) |
| σ lane, ZFC Ulam witness | **Unchecked.** (M₁ × Fin 4, three cores.) Not folded in. | — |

The σ-lane row corrects what I said in conversation on 2026-10-15. I had called
the σ lane a separate, non-cyclic source of obstruction (infinity rather than
cycles). That was wrong for the countable witness.
- **The pattern.** The pattern is C_k = {x_k < x_{k+1}} around a ring, so the
  cyclic order has an empty kernel. 7826c20 transports this pattern to every
  L ≥ 4 by a degree-one map ℤ_L → ℤ_4.
- **Its σ-additive analogue is impossible.** That is the analogue with equal
  marginals and P(x_k < x_{k+1}) = 1 for all k.
- **The obstruction is the cycle and infinity together.** The cycle is where
  finite additivity buys contextuality.
- **No σ verdict changes.** This is a structural observation.

## 2. The deep-research map (101 agents; 20 claims confirmed, 5 refuted)

- **Stratum 1 (cyclic coherence vs realizability).** This stratum is crowded.
  - Vorob'ev and junction trees settle the acyclic case.
  - Pivato 2001 poses the shift-invariant extension problem (§3).
  - Wang–Navascués 2018 (Proc. R. Soc. A 474:20170822) settle 2D translation-invariant
    membership for small alphabets. In general it is undecidable or
    non-semialgebraic, but that is on the infinite ℤ², not on finite tori.
- **Stratum 2 (reach lemma).** No proving theorem was found.
  - The closest object is the **no-meet matroid** (Ben-Ameur, Kushik, Maddaloni,
    Neto, Watel, DAM 354, 2024). It concerns synchronous walks that never share a
    vertex, and its rank is the maximum number of vertex-disjoint cycles.
  - It is silent on swaps, SCC period and cocyclic pairs.
  - Kari's stable-pair reduction of road colouring has the same shape but goes
    toward the diagonal, not away from it.
- **Stratum 3 (σ-essential).** Nothing outside the known finite-additivity line.
  The Boolean prototype of "no finite witness" is Schervish–Seidenfeld–Kadane
  conglomerability. That is a rhyme.
- **Stratum 4 (conservativity).** Two genuine homes:
  - Sherali–Adams / Lasserre exactness at treewidth level;
  - k-local LP invariance under C^k equivalence (Atserias–Maneva, Grohe–Otto).

**Coverage caveat.** Strata 2 and 3 were thin, and 11 claims were dropped for
budget. "Not found" is not evidence of absence.

## 3. Pivato 2001: checked against the primary source

*Canad. J. Math.* 53(2), 382–413, arXiv:math/0108081.

**What it has:**
- **On ℤ (§1.1), the single-window problem is trivial.** A locally stationary
  μ_U on an interval always extends, via the Markov construction, and that
  extension has maximal entropy.
- **Periodic extensions (§5 Thm 7, §8.2 Thm 12, Cor 13–14)** get only an
  *open-ball sufficiency* result. Data within ε of a full-support invariant
  measure on a finite module ℤ/P extends periodically.
- Essentially aperiodic and essentially periodic examples are 2D, from tilings.
- No D = 1 periodic criterion appears, and the bibliography cites no D = 1
  periodic-extension literature.

**Differences from the flagship:**

| | Pivato | flagship |
|---|---|---|
| data | one locally stationary window μ_U | a protocol of contexts; EA only, shift-invariance *not* required (`def:core`) |
| question | can this μ_U extend periodically? | does *any* EA datum supported on ρ fail to be realisable on the L-ring? |
| answer | sufficient, open ball | exact iff per L (winding), plus Safe(ρ) eventually periodic |

So Pivato's setting is a sub-case: one window, with realization class
"stationary". He doesn't settle it, and he does not contain the winding
criterion.

**Consequence for layer E.** The process question on ℤ is trivial for a single
window. Its content lives in the **periodic (ring) quotient and in protocol
families**. `hierarchy_and_open_space.md` is amended to say so.

## 4. Points of tension with the sheaf-theoretic approach

### 4a. The main finding: much of the winding criterion's logical form is already general sheaf theory ⟦HAND — reading of ABKLM, not yet checked against the archive proof⟧

The source is Abramsky–Barbosa–Kishida–Lal–Mansfield 2016, *Possibilities
determine the combinatorial structure of probability polytopes* (J. Math. Psych.,
arXiv:1603.07735; read from the primary source).
- **Thm 6.1 / Cor 6.2.** The face lattice of the no-signalling polytope N(Σ) is
  order-isomorphic to the lattice of supports. Vertices are exactly the models of
  minimal support.
- **Prop 6.3.** For **any** scenario Σ, vertices(N(Σ)) is the disjoint union of
  the local deterministic models LD(Σ) and the minimal-support **strongly
  contextual** models MSC(Σ).

The flagship's C is the no-signalling polytope (AB: EA = presheaf compatibility).
So, for any scenario:

  *contextual data supported on ρ exists ⟺ MSC(Σ) has a member supported on ρ.*

That is general and owned by ABKLM. The winding criterion, read through it:
- **Its logical form is owned:** "unsafe ⟺ some minimal strongly contextual
  support exists".
- **What remains is an explicit identification of MSC on ring scenarios:** the
  minimal strongly contextual supports are exactly the layer-injective simple
  cycles of winding ≥ 2 in the layered graph.
- **That identification is the bundle-diagram picture.**
  - The layered graph is the bundle diagram over the ring.
  - A winding-1 cycle is a global section.
  - A simple winding-w cycle is a connected w-fold cover of the circle. It has
    no global section, so it is strongly contextual. The PR box is the Möbius
    double cover.

**What survives as the flagship's own:**
1. the flow-decomposition proof that every vertex of C on a ring *is* one simple
   cycle (circulation polytope), which forces "minimal support = single connected
   cover";
2. the layer-injectivity discriminant (Lean);
3. the all-lengths layer: Safe(ρ) eventually periodic and computable, and the
   forcing lemma / reach lemma.

Item 3 has no counterpart in the sheaf literature found so far. There, scenarios
are fixed, with no length family and no shift structure.

**Owed:**
- Check Araújo–Quintino–Budroni–Terra Cunha–Cabello 2013 (already cited) for an
  explicit list of n-cycle no-signalling vertices. If it has one, item 1 is
  known for binary two-element contexts.
- Check whether the AB / bundle-diagram literature already describes the
  strongly contextual supports of cyclic scenarios as connected covers. Recalled,
  not verified: the Möbius picture of the PR box, and Abramsky et al. 2015,
  *Contextuality, cohomology and paradox*, on Liar cycles.
- Add ABKLM to `PRIOR_ART_VERDICT.md` as **must-cite** for `thm:winding`.

### 4b. Finite vs finitely additive

The sheaf framework's measure-theoretic extension uses σ-additive measures. That
is the continuous-variable sheaf framework (Barbosa et al.), recalled and **not
verified here**. The countable σ-witness (§1) is a cyclic obstruction that exists
*only* finitely additively. If the recollection is right, that witness sits
outside the framework by construction. This is a point of tension, not a
contradiction.

### 4c. Uniformity in L and shift structure

Sheaf scenarios are single, fixed objects. The programme's questions quantify
over a family:
- all L;
- one language ρ;
- realization by a *process* rather than a static joint.

Pivato is the only verified antecedent with shift structure, and it has no
contextuality layer.

### 4d. Cohomology

Only what `reconstruction_audit_full.md:65–71` records is used here:
- the neighbours are Abramsky–Barbosa 2015, Carù 2019 and Montanhano 2021;
- none states a winding or layer-injective decidability criterion.

Any claims about completeness or incompleteness of Čech-cohomology invariants
are **unverified here** and are not used.

## 5. Is a more universal framing approachable from this direction?

**The ceiling is on file.**
- Prusa–Werner 2013/15: every polytope is a local marginal polytope.
- De Loera–Onn: the same for 3-way transportation polytopes.

So no winding-type explicit criterion can hold for all scenarios. ABKLM gives the
universal *form* (MSC supports). The explicit content is scenario-class specific.

**Why the ring works:**
- The overlap structure is a cycle, with π₁ = ℤ.
- C is a circulation polytope, and flow decomposition makes every vertex a single
  simple cycle.
- The minimal strongly contextual supports are therefore the connected covers of
  degree ≥ 2.

**Questions only:**
1. **Boundary class.** How far up does "C is a flow / circulation polytope, so its
   vertices are single cycles in a cover" survive?
   - *Cacti:* every block is a cycle, and the fundamental group is free.
   - *Bounded cyclomatic number.*
   - *1-dimensional nerves:* pairwise single-site overlaps, no triple overlaps.
   - Is MSC there exactly the set of connected covers with non-trivial monodromy?
2. **The other side of the gap.** Sherali–Adams reaches exactness at level
   treewidth + 1. Rings have treewidth 2. So on rings the whole content is the
   level-1-to-level-3 gap, and the winding criterion describes it. Does the
   cover picture describe level-1 vs exact on the boundary class from (1)?
3. **Finitely additive version.** On which classes does the ultrafilter cyclic
   obstruction (§1) exist? Is "degree ≥ 2 connected cover" still the
   discriminant there, given the Katětov argument for graph-type ultrafilters
   (trivial monodromy)?

Nothing here is claimed novel. "Survives the check" is not a novelty claim.

## 6. Next, in order

1. Do the §4a checks: Araújo 2013 n-cycle vertices; bundle and cover descriptions
   in the AB lineage. These decide how much of `thm:winding` is owned.
2. Add ABKLM and Pivato rows to `PRIOR_ART_VERDICT.md` (done with this note).
3. Pursue the §5 boundary-class question only if (1) leaves the flow-decomposition
   identification standing.
