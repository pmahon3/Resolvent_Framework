# Case study 1: three species that never settle (2026-10-19)

reviewed: false. This is a CASE, not a generalisation. It tests "ideal point = long-run world" by
reflective equilibrium (memory: feedback_reflective_equilibrium). Status labels: **cited** (checked
at abstract level), **hand** (unverified).

## The system

Three species compete in a rock-paper-scissors cycle: 1 beats 2, 2 beats 3, 3 beats 1. This is the
May–Leonard model, SIAM J. Appl. Math. 29(2) (1975), doi 10.1137/0129022, and the replicator
dynamics of rock-paper-scissors. The orbit swings from near "only species 1" to near "only species
2" to near "only species 3", and back. It lingers longer each time, because the heteroclinic cycle
attracts. **cited**

Its long-run averages never settle. Near an attracting heteroclinic cycle, for almost every starting
point, the fraction of time spent near each species does not converge. The running averages spiral
ever closer to the boundary of a polygon (Gaunersdorfer, SIAM 52 (1992) 1476–1489). The planar
two-saddle version is Bowen's example (Takens, Bol. Soc. Bras. Mat. 25 (1994) 107–120). This is
Takens' "historic behaviour". **cited**

## The four questions of the method

1. **Queries.** "What fraction of the time is the system near species i?" More generally: "What is
   the long-run joint frequency of the abundance pattern of species i and j?" There are pair
   windows, one per pair of species, so the window graph is a **triangle**.
2. **Answers.** Long-run frequencies. They have no limit, so a long-run answer needs a way of taking
   a limit along a chosen epoch (a subsequence of times, or an ultrafilter or Banach limit on times).
3. **Joint askability.** One observer, using one way of taking the limit for every question, gives
   jointly consistent answers: a single charge on the state space. Several observers, each with its
   own epoch, are the case where joint questions are not automatically available.
4. **What a world is here.** A long-run *world* is one long-run frequency pattern w = (w₁, w₂, w₃)
   that produces every answer, i.e. one point on the limit polygon.

## Findings

**F1. Ideal worlds exist, but the dynamics does not choose one.** ⟦hand, from the cited result⟧
Each way of taking the limit gives a coherent long-run answer pattern: a point w on the limit
polygon. So "ideal point = long-run world" fits: the long-run world exists only as an idealisation.
But it adds something the theory had no word for: *the system determines a whole loop of ideal
worlds (the polygon), not one*. Which world you get is the observer's choice of epoch. **Pushback
on the concept: "the" ideal point is not canonical.**

**F2. One observer is never pointless.** ⟦hand⟧ If all questions are averaged the same way, the
answers form one charge on everything, so a model exists. Pointlessness needs observers who each
take their own long-run limit.

**F3. Asynchronous observers can agree pairwise yet describe no world.** ⟦hand⟧
- *The setup.* Three field stations each watch one pair of species, and each averages over its own
  epoch. Near species k the abundances are close to "only k". So station (i,j) reports long-run
  masses on its pair:
  - "i only", with mass wᵢ;
  - "j only", with mass wⱼ;
  - "neither", with mass w_k.
- *The reports.* Station (1,2) uses a limit point P, station (2,3) uses Q, and station (3,1) uses R.
- *Agreement on overlaps.* w₂(P) = w₂(Q), w₃(Q) = w₃(R), w₁(R) = w₁(P).
- *What a joint world would need.* Masses a₁, a₂, a₃ on "only species k", and z on "no species
  dominant". The equations force a_k from the reports and z = w₃(P) − w₃(Q); the other two
  expressions for z agree automatically.
- *So a world exists iff z ≥ 0.* If w₃(Q) > w₃(P), the stations' reports agree wherever they
  overlap, yet the derived probability of "no species dominant" is **negative**. No long-run world
  produces them.
- *Geometry* (recomputed by hand). The equations give z = w₃(P) − w₃(Q) = w₁(Q) − w₁(P)
  = w₂(R) − w₂(P). With δ = w₃(Q) − w₃(P), the bad case is δ > 0, and then
  **Q = P + δ(−1, 0, +1) and R = P + δ(0, −1, +1)**. So the three limit points must form a
  translate of the triangle {0, δ(−1,0,1), δ(0,−1,1)} with δ > 0, all lying on the limit polygon.
  The same shape with δ < 0 gives z > 0, which is harmless. Whether a positive copy fits on the
  polygon depends on the polygon's shape and orientation.

**F4. The askable questions expose it.** ⟦hand + the finite triangle result⟧ The observers' window
is the triangle. In finite, probabilistic worlds the triangle's askable questions see every twist
(rigorous at three values). Here the exposing question is "is no species dominant?", whose forced
probability is z < 0. So asynchronous inconsistency is always *detectable* on a triangle. This is a
lived instance of the triangle filling itself in.
**SCOPE (2026-10-20):** the explicit witness z < 0 stands for this case (3 values). The general
"always detectable on a triangle" holds only for ≤ 3 values: at 4 values a triangle can hide a twist
(`definitions_draft.md` §16).

## What this does to the concepts (equilibrium so far)

- *Illuminated:* long-run worlds are ideal points; pointlessness needs several observers
  (unaskable joint questions = asynchronous averaging); the triangle detects it.
- *Strained:* ideal worlds come as a loop (the limit polygon), chosen by the observer's epoch. The
  theory treats an ideal point as given; here it is selected.
- *Not supported:* nothing yet about "world = model" beyond this one case. **Do not generalise.**

## Checks needed before relying on F3

1. Offsets recomputed and the algebra checked numerically (2026-10-19): overlaps agree, the three expressions for z coincide, and a joint world exists iff δ ≤ 0.
2. Compute the actual Gaunersdorfer polygon for a concrete parameter choice, and test whether a
   positively oriented copy fits on it. This is small, a simulation or the closed form.
3. Check that "abundance ≈ 'only k'" is accurate enough for the station reports, or redo them with
   thresholded presence/absence.

## Check 2 and 3 results (2026-10-19) ⟦simulation + exact geometry⟧
- **The limit polygon.** The hand formula V_i ∝ e_i + r e_{i−1} + r² e_{i−2}, with r = b/a, matches
  the simulated replicator turning points to about 2 decimals. Stay durations grow by a/b.
- **The bad configuration is realisable.** For every r tested, and both traversal directions,
  P, P + δ(−1,0,1) and P + δ(0,−1,1) with δ > 0 fit on the limit triangle (exact solve). At
  a/b = 2: P = (0.4, 0.4, 0.2), Q = (0.2, 0.4, 0.4), R = (0.4, 0.2, 0.4), δ = 0.2. These are the
  points 60% of the way along each edge.
- **Real epochs realise it.** Simulated running dominance frequencies come within 0.002 of P, Q and
  R. The three stations' reports agree on the shared species to within 0.001. The implied probability
  of "no species dominant" is **−0.199**.
- **F3 is confirmed in this system**, with reports taken as dominance frequencies (exact, with no
  abundance approximation). Scripts: `verification/case1_polygon_check.py`,
  `verification/case1_epochs.py`. Still a case, not a generalisation.
