# Joint 2 of universal impossibility: grading = imprimitivity, step 1 = Wielandt

**Date:** 2026-07-09. **Status:** step (2) reduced to classical; step (1) has a
Wielandt proof skeleton, empirically confirmed but NOT proved. ⟦HAND⟧, raw-DFS
oracle = ground truth.

## What Joint 2 is

Universal impossibility's second joint (distinct from the pruning lemma = Joint 1).
For a strongly-connected non-symmetric recurrent-branching language, the intended
argument (seed 2.2t design-lane) is:
  (1) rich-safe (safe at enough lengths to pass a K4-minor frame's circuits)
      ⟹ the unsafe set is residue-structured (cofinitely a union of residue
      classes mod d);
  (2) residue-structured ⟹ one of grading / potential / phase-code (a taming);
  (3) each taming localises the polytope.
Step (2) was the load-bearing unexamined converse.

## Finding 1: grading = Perron–Frobenius imprimitivity (step 2 is classical)

Taming 4 "grading" = transfer digraph fibered over ℤ_d. **Verified computationally**
(`papers/reconstruction/oracles/joint2_wielandt.py` part I): a language is graded-at-some-d ⟺ its
digraph period (gcd of cycle lengths) ≥ 2. Exact match on all examples
(graded-d2, 3-cycle, 2-cycle graded; golden-mean, full2 primitive⟹not graded).

This is classical Perron–Frobenius: a strongly connected digraph has period d ⟺
its vertices d-partition into cyclic classes that arcs advance through ⟺ fibered
over ℤ_d. So the **DICTIONARY** grading ⟺ imprimitivity is classical.

**⚠ BUT step (2) itself is NOT thereby classical (overclaim caught).** Step (2) is
"residue-structured-unsafe ⟹ grading (= imprimitive)", i.e. "unsafe-set-modulus =
digraph-period." **This is FALSE without non-symmetry.** Counterexample from own
data: golden mean `{(0,0),(0,1),(1,0)}` is PRIMITIVE (cycle lengths 1,2, gcd 1)
yet its unsafe set = odds = residue class mod 2 (from the PARITY theorem =
winding/TU, NOT digraph imprimitivity). So residue-structured unsafe sets have ≥2
independent sources (parity/winding AND digraph-period); digraph-period is only one.
Only the dictionary is free; the implication is the real work.

## Finding 2: step (1) is a Wielandt statement (primitive ⟹ cofinitely unsafe)

The real difficulty is the contrapositive of step (1):
  **primitive (period 1) strongly-connected transfer digraph ⟹ cofinitely unsafe
  ⟹ not rich-safe.**

**Empirical confirmation** (`papers/reconstruction/oracles/joint2_wielandt.py` II + `papers/reconstruction/oracles/joint2_deep.py`):
scanned 110 primitive strongly-connected non-symmetric total languages (|A|≤3).
Six appeared "rich-safe" in the small window L≤9 (safe at {3,4,7}) — an ARTIFACT
of the small window. Pushed to L=30: **all are unsafe at every L in [8,30]; safe
set = {3,4,7}, FINITE.** No primitive language is genuinely rich-safe. This is the
Wielandt shape: a primitive digraph goes cofinitely unsafe.

**Proof skeleton (NOT a proof):** Wielandt's theorem — a primitive n×n 0-1 matrix
M has M^k > 0 for all k ≥ (n−1)²+1 (the Wielandt index). So past the index, between
ANY two states there is a walk of EVERY length. A winding-2 simple cycle needs two
vertex-disjoint off-diagonal strands P (a→b) and Q (b→a) of length L swapping
endpoints. Primitivity supplies walks a→b and b→a of every large length; the
remaining content is the **off-diagonal + vertex-disjoint refinement** (that the
two walks can be chosen non-colliding). The length availability is pure Wielandt;
the disjointness refinement is the genuine open combinatorial step.

⚠ The observed last-safe L=7 is PAST the |A|=3 Wielandt index 5, so the bound is
NOT the naive "unsafe for all L ≥ index" — the disjointness refinement shifts the
threshold. The skeleton is real but incomplete; do not claim step (1) proved.

## THE CRUX (CORRECTED 2026-07-09): "non-symmetry" was a MIS-STATEMENT

Earlier framing: "why does non-symmetry force primitive ⟹ cofinitely-unsafe."
**This is WRONG — refuted by golden mean.** Golden mean is PRIMITIVE and (up to the
loop) SYMMETRIC, yet residue-safe at even L. Its safety is NOT a non-symmetry
effect: **safe ⟺ layered ring bipartite (even L) ⟺ signability/TU (taming 3)
fires.** Verified by building (`scratchpad`, safe⟺bipartite exactly, L=3..10). So
golden-mean's residue-safety IS a taming firing, not evidence for a non-symmetry
axis. Non-symmetry was never the discriminator.

**THE CORRECTED CRUX (the real Joint 2):**

  **The tamings are the only sources of residue-safety in a primitive language.**
  I.e. classify the sources of residue-safety; show each is a catalogued taming.

This is exactly "the tamings are complete" — the same theorem that would de-mess
the paper (ten sufficient conditions → one necessary-and-sufficient classification).
The 4 finite-safe non-symmetric candidates and golden-mean are now UNIFIED: each
safe residue is a taming firing (signability on the bipartite residue for gm; the
non-symmetric ones simply have NO safe residue past Wielandt = no taming fires).
Not "the non-symmetric case" — the SOURCES-OF-SAFETY classification. Needs an idea.

## Finding 3 (DOWNGRADED to a question): do Joints 1 and 2 share an engine?

Tempting: both run on transfer-digraph period. But golden mean shows the unsafe
set's period can come from PARITY (winding/TU), decoupled from digraph-period. So
≥2 mechanisms feed the residue structure, and "Joints 1+2 = one period engine" is
too simple. Keep as an open question, not a leaning.

## What is proved vs open (do not overclaim)

- **CLASSICAL (dictionary only):** grading ⟺ digraph imprimitivity (period ≥2).
- **NOT classical (the crux):** step (2) "residue-unsafe ⟹ grading" — FALSE
  without non-symmetry (golden mean counterexample). Real content = non-symmetry
  forces primitive ⟹ cofinitely-unsafe. Wielandt-shaped, empirically confirmed
  L≤30 on all |A|≤3 non-symmetric primitives, NOT proved.
- **UNVERIFIED sub-claim:** "cofinitely-unsafe ⟹ not rich-safe." rich-safe = covers
  a K4-minor frame's circuit-lengths (the seed's no-fork argument was GIRTH-LOCKING,
  P47 — sparse safe sets can't cover diverse circuit lengths), which is SEPARATE
  from Wielandt finiteness. A finite safe set {3,4,7} is not obviously
  frame-non-covering; check whether Wielandt finiteness delivers not-rich-safe or
  still needs girth-locking.
- **OPEN:** the disjointness refinement; exact threshold; past |A|=3; the crux
  above; Joint 1's k≥3 pruning (separate open piece).

## Mechanism independence — RESOLVED 2026-07-09: the triple collapses

The seed's Joint-2 attack names three forcing mechanisms: grading/potential/phase-code.
Do potential and phase-code carry content independent of grading? **No — verified by
building.**
- **phase-code = grading.** A phase-code is a labelling c: states → ℤ_d advanced by
  every arc (c(b)=c(a)+1). That is exactly `is_graded` = fibered over ℤ_d =
  imprimitivity. Identical by definition.
- **potential collapses.** A monotone ℤ-valued potential (p(b)≥p(a) along arcs,
  non-constant) does not exist on a strongly-connected digraph — it must be constant
  (0 of 347 strongly-connected languages admit a non-constant one; structurally,
  increments sum to 0 around any cycle ⟹ all equal). So "potential" is either
  constant (no information) on the irreducible core, or mod-d valued = grading, or —
  for the reducible part — the already-catalogued monotone-collapse (taming 8).

**⟹ no new third mechanism. Joint 2 has ONE crux (sources-of-residue-safety), not
three.** This sizes the problem: the whole exchange-blocking classification reduces to
the single question "the tamings are the only sources of residue-safety," with grading
(imprimitivity) and signability (TU on bipartite residues, per golden-mean) as the two
confirmed sources so far.

## "Rich-safe" PINNED (2026-07-09) — the frame-covering / residue condition

The girth-locking subtarget's key object, made precise. A FORK = a language L + a
K4-minor frame F such that every circuit length of F lies in Safe(L), yet L is
genuinely contextual (escapes all tamings). A subdivided-K4 has 3 independent
cycles; to make all its circuits safe one subdivides edges so circuits land in an
arithmetic progression d·ℤ (the ρ₂₀ pattern: circuits 18, 24 ∈ 6ℤ = Safe(ρ₂₀)).

**So the sharp necessary condition for a fork: safe on a FULL residue class d·ℤ
(d≥2), not merely finitely many lengths.** This is the filter the fork-hunt needs —
and it is exactly the girth-locking claim's contrapositive: if no untamed language
is safe on a full residue class, no fork exists.

**First deep adversarial sweep (`papers/reconstruction/oracles/joint2_fork_hunt_scale.py`):** 1500 primitive,
strongly-connected, non-symmetric, NON-bipartite (⟹ signability excluded), |A|=5
languages — i.e. candidates NOT tamed by grading (primitive) or signability
(non-bipartite) — probed for safety on residue classes d·ℤ up to L=30 (past the
Wielandt index 17, and past the L=9 window that produced 6 false "rich-safe"
positives earlier). **ZERO survived.** Every untamed 5-state candidate goes unsafe
on every residue class past the artifact window. Real evidence for UI (not a window
artifact); the hunt should widen (|A|=6, denser branching, more d) — a hit at any
scale kills UI.

## Girth-locking, first attack — a DETECTOR BUG, not near-forks (2026-07-09)

Attacked the sources-of-safety crux via its contrapositive: "safe on a full residue
class d·ℤ ⟹ tamed by a catalogued mechanism." Enumerated strongly-connected total
languages safe on 2ℤ deep (A=3 to L=20, A=4 to L=16) and ran a taming detector
(signability/grading/twins/determinism).

**Apparent result:** 6 (A=3) + 14 (A=4) UNTAMED survivors — looked like near-forks
(genuinely contextual, safe on 2ℤ, no taming firing). Per the pre-registered gate
this would mean a MISSING taming or a real fork.

**Actual result: the detector was BROKEN.** Decisive check (advisor):
`tamed(golden_mean) = []` — but golden mean IS signability-tamed (safe⟺even, PROVED
this session). A provable inconsistency between the detector and my own theorem.
**Root cause:** signability is "a column signing driven by the FRAME's bipartition
giving TU" (paper) — a property of the layered ring / observation frame, NOT the
target state-graph's 2-colourability. `bipartite_target(rel)` tested the wrong
object, false-negativing exactly the odd-cycle/parity languages (whose signature is
safe⟺L-even). Verified: the first survivor is safe⟺L-even for all L=3..15 = the
odd-cycle facet = frame-signability = TAMED. Every survivor is golden-mean-shaped.

**⟹ NOT near-forks, NOT a threat to UI, NOT a missing taming.** The girth-locking
run tells us nothing about UI until the detector is rebuilt with FRAME-LEVEL
signability (layered-ring bipartition + TU), not target 2-colouring.

**The deeper lesson (why this matters for the paper):** silently under-detecting one
of the catalogued tamings is plausibly part of WHY the catalogue reads as
stamp-collecting — you cannot feel a classification is complete while your own
instrument mis-tests one of its members. Getting the detector right IS part of
making the tamings feel principled.

**NEXT:** rebuild the taming detector at the frame/layered-ring level (signability =
even-cycle-TU / odd-cycle-facet; the parity certificate), re-run girth-locking. The
count that survives THAT detector is the real signal about UI.

## Corrected detector + the two-carrier structure (2026-07-09, second attack)

Rebuilt the taming detector at the mechanism level (v1 tested target-graph
2-colouring = wrong object). v2 tests residue-safety against TWO confirmed sources:
- **grading** = safe-status depends only on L mod (digraph period p≥2);
- **parity** = safe exactly on even L (the odd-cycle/independent-set certificate).

v2 **catches golden mean** (`parity`), fixing the v1 inconsistency. Re-run:
- A=3 FULL enumeration: 14 safe-on-2ℤ languages, **0 survive** v2 (all grading or
  parity). Girth-locking holds at A=3 under the corrected detector.
- A=4: full enumeration too slow inline; sampled runs consistent (primitive+safe-2ℤ
  are parity-explained) BUT the sample is near-empty (1 hit) AND the check is
  partly CIRCULAR (`parity_explained` = safe-on-evens ≈ the safe-on-2ℤ filter). So
  A=4 is NOT real evidence. Recorded as such.

**Settled by hand (structural, not scan): grading ≠ parity — two DISTINCT carriers.**
Golden mean is primitive (loop ⟹ period 1) yet parity-safe, and admits NO grading
labelling (the loop 0→0 would need 0=1 mod 2). So:
- **grading** = the TRANSFER DIGRAPH factors onto ℤ_d (a directed cycle, loop-free);
- **parity** = the LAYERED RING is bipartite at even L ⟹ König/TU on the
  independent-set polytope (FSTAB=STAB).
Two different objects (transfer digraph vs layered ring), two different integrality
routes. The honest unifying frame: "a small quotient makes the relevant polytope
integral," but on DIFFERENT carriers — not one cyclic principle at p=2.

**HYPOTHESIS (thin data, NOT a theorem — do not round up):** on a PRIMITIVE language,
the only source of residue-safety is parity. Golden mean is the one confirmed
primitive-parity witness; the A=4 sample is too thin and too circular to support it.
NEXT (by thinking, not scanning): prove or break "primitive + residue-safe ⟹
parity-carrier (bipartite layered ring)", with LISC as the falsifier — that is the
theorem-or-missing-taming, and it settles on a hand example, not a scan.

## PARITY-ONLY, corrected framing + evidence (2026-07-09, next session)

**⚠ A LOAD-BEARING CORRECTION — the "bipartite layered ring" carrier was WRONG
(confirmation-bias-guard catch #3, advisor+oracle-verified).**

Ran the NON-CIRCULAR witness channel (`papers/reconstruction/oracles/parity_only_witness_channel.py`): enumerate
primitive strongly-conn total langs, compute the ACTUAL safe set via raw LISC with
NO d-pre-filter, then read off residue structure. Surfaces (not filters) two
refuters: R1 = safe on d·ℤ, d≠2; R2 = safe on evens but layered ring not bipartite.

- **A=3 FULL (139 primitives, Lmax=16): 9 infinite-safe, EVERY one safe exactly on
  evens (d=2), R1=0, R2=0.** The 9 witnesses are DISTINCT langs (not just golden
  mean) — kills the "fit to one example" worry for d=2.

**But R2 is a TAUTOLOGY — dead channel (do NOT count R2=0 as evidence):**
- The layered graph maps homomorphically onto C_L via (i,s)↦i; C_L is bipartite at
  even L; a proper 2-colouring pulls back along any homomorphism. So **the layered
  ring is bipartite at EVERY even L for EVERY ρ.** `layered_ring_bipartite` can't
  return False at even L ⟹ R2 structurally cannot fire. Same shape as the v1
  detector bug.
- **"bipartite layered ring ⟹ safe" is FALSE.** Verified on the oracle: the FULL
  relation (all A² arcs) has layered_ring_bipartite=True at L=4,6,8,10,12 yet
  lisc2_raw=UNSAFE at all of them. Direct counterexample.

**The inherited "parity carrier = bipartite layered ring ⟹ König/TU" conflated TWO
graphs:**
- **layered graph** (L×A verts): bipartite auto at even L — IRRELEVANT to safety.
- **ring C_L** (L site-verts): bipartite ⟺ L even — THIS is what the parity thm's
  TU/König uses, but ONLY via the golden-mean reduction (configs = indep sets of
  C_L; target = one edge). GOLDEN-MEAN-SPECIFIC, not a general carrier.

**What SURVIVES (real, non-tautological):** R1=0 — "primitive + infinite-safe ⟹
d=2" stands as genuine evidence (a 6ℤ-safe lang would be caught at d=6; none was).

**Redirect (the false integrality line is BLOCKED):** node-arc incidence of ANY
digraph is TU ⟹ circulation polytope ALWAYS integral ⟹ fractionality comes ONLY
from per-layer normalization (winding-w vertex → mass 1/w), NOT bipartiteness. So
"safe = no winding-≥2 LISC" is a pure WALK-EXISTENCE/COLLISION question =
exactly the "off-diagonal + vertex-disjoint refinement" already named as the open
step. Sharpened on the 9 witnesses: **why do vertex-disjoint winding-2 threads
exist at ODD L but COLLIDE at EVEN L?** That L-parity collision IS the content of
"safe on evens" — TU never enters. NEXT: work this collision question by hand.
A=4 full enum running (`wc_A4.out`) as the wider R1 channel.

### R1 evidence backbone (non-circular, STRONG) + crossing-parity falsifier (FIRED)

**A=4 FULL enum (25575 primitives, Lmax=14): 64 infinite-safe, EVERY one safe
exactly on evens (d=2). R1=0.** Combined with A=3 (139 primitives, 9 infinite-safe,
all d=2): **primitive + infinite-safe ⟹ safe exactly on evens, 0 counterexamples
across ~25,700 primitives.** This R1 backbone is REAL (safe set computed by raw
LISC, residue read off after — no d pre-filter). (R2=0 stays a tautology — ignore.)

**The winding-2 LISC structure (`collision_all9.py`): per-layer state-pairs
ALTERNATE.** 7/9 A=3 witnesses: two-state support, pair {a,b} at every layer
(golden-mean/odd-cycle half-point). 2/9 (w2,w3): three-state support but pairs
alternate between two fixed pairs, period 2 in layer index. Unifying object = a
2-fold cover of the layer cycle: unordered pair {s_i,t_i} per layer, consecutive
pairs joined PARALLEL or CROSSED; single winding-2 cycle ⟺ ODD # crossings.

**Crossing-parity MECHANISM (`crossing_parity.py`) — advisor-mandated falsifier
FIRED (this is a GOOD outcome, caught before proof-writing):**
- Candidate: unsafe at L ⟺ pair-graph closed walk of length L with ODD crossing
  parity; safe-on-evens ⟺ crossing-label cohomologous to constant-1 (Z₂ potential
  φ on pairs, edge-label = 1+Δφ ⟹ total = L mod 2 ⟹ odd ⟺ L odd).
- **RESULT: my pair-graph oracle MATCHES all NEGATIVES (full relation + 8 random
  unsafe-at-even) but MISPREDICTS all 9 WITNESSES at even L** (says unsafe, oracle
  says safe). So crossing-parity as I coded it is NECESSARY-not-SUFFICIENT.
- **Diagnosis:** my dedup key (layer, frozenset-pair) let the 2-fold cover REUSE an
  unordered pair ⟹ found a swap-closing walk that is NOT a simple 2L-cycle. The
  missing constraint = SIMPLICITY / global vertex-disjointness of the two threads =
  EXACTLY the "vertex-disjoint refinement" already flagged as the open step. Odd
  crossings is required; the simple/covering structure is what forbids even L.
- ⚠ Do NOT round the Z₂-cohomology story up to a theorem — the falsifier shows it's
  incomplete. The real content lives in simplicity, not in the parity label alone.
- Likely the combinatorial shadow of the parity thm's det(I+P)=1−(−1)^L; if it
  cleanly characterizes safe-on-evens it is an INTRINSIC re-derivation of the
  parity mechanism, not a new taming. NEXT: fix the oracle to enforce simplicity,
  re-test at both parities incl. negatives; if "odd-crossing + simple ⟺ unsafe"
  matches, THEN attempt "primitive ⟹ even-L forces even-crossing-or-non-simple".

### MECHANISM VALIDATED (2026-07-09) — the 2-fold-cover / swap-monodromy characterization

Both prior mismatches were CODING bugs on the closure line (advisor-located), NOT a
real incompleteness — and my "simplicity is the missing constraint" diagnosis was
WRONG (dropped): a 2-fold cover with two DISTINCT states per layer is automatically
simple (each thread is a section over the layer cycle ⟹ all 2L layered vertices
distinct). v1 bug = frozenset dedup over-accepted; v2 bug = an extra (L+1)-th
closure arc inverted the length-parity. Fixed (`crossing_parity_v2.py`, closure =
`a==b0 and b==a0` at layer L).

**VALIDATED CHARACTERIZATION (matches raw LISC on ALL 1600 random A=3/A=4 langs ×
L=3..10, 0 mismatch; + 9 witnesses + 9 negatives at both parities):**

  **unsafe at L ⟺ ∃ a 2-fold cover of the layer cycle by legal arcs (an ordered
  thread-pair (a_i,b_i), a_i≠b_i per layer, each arc (a_i,a_{i+1}),(b_i,b_{i+1})∈ρ)
  that closes with SWAP MONODROMY after exactly L steps (returns to (b_0,a_0)).**

Swap monodromy = ODD # of crossed transitions = the single-winding-2-cycle
condition. This is the INTRINSIC re-derivation of the parity mechanism (combinatorial
shadow of det(I+P)=1−(−1)^L). **NOT a new taming; do NOT round up.**

**What it does NOT yet give:** "primitive ⟹ safe-set = evens." That still needs:
**primitivity forces the swap-closure to be achievable at ODD L and obstructed at
EVEN L.** The validated predicate makes this a clean stateable question. If
"primitive ⟹ swap-closes only at odd L" is where it gets hard, THAT is the
`win.named_lemma` floor (a single clean open lemma = completes the paper's arc).
Do NOT let the green harness round up to the theorem. NEXT: attempt the forcing.
Oracle: `crossing_parity_v2.py`.

### Forcing attempt — cohomology reformulation FAILED as coded (2026-07-09)

Reformulated the validated predicate as a Z₂-cover: swap-monodromy walk = closed
walk in the UNORDERED-pair graph bar-D with odd Z₂-monodromy (D→bar-D the
sigma-cover, sigma:(a,b)↦(b,a)). Candidate forcing claim: **safe-on-evens ⟺ the
signed graph (bar-D, sign=monodromy+1) is BALANCED** (⟺ monodromy cohomologous to
const-1 ⟺ total monodromy = L mod 2 ⟺ odd only at odd L).

**RESULT (`z2_potential.py`): FALSE as coded. A=3: 19/800 mismatches, ALL
balanced=True but safe_on_evens=False (over-accepts). Not a tautology (counts
non-trivial: 33 balanced, 14 safe-on-evens of 800) — so the predicate has real
content but is WRONG/incomplete.** Likely my balance check misses long odd signed
cycles (only caught 2-cycles + BFS-2-colour) OR the ascending-frame sign
convention (spi^sqi) is miscounting monodromy. Example miss:
[(0,1),(1,0),(1,1),(1,2),(2,1),(2,2)] period 1, balanced=True but unsafe-on-evens.

⚠ CONFIRMATION-BIAS GUARD: do NOT patch the cohomology encoding a 3rd time solo.
The VALIDATED object is `crossing_parity_v2` (swap-monodromy, 1600 langs 0-mismatch).
The balance reformulation is a DERIVED claim and is empirically false as written —
either the sign convention is wrong or safe-on-evens is NOT simply "balanced" and
needs the primitivity hypothesis to enter differently. STATE THIS HONESTLY, get
advisor eyes before the next encoding. Session's net gain = the validated
swap-monodromy characterization + strong R1 backbone (~25,700 primitives, 0 cex);
the clean forcing lemma is NOT yet in hand.

### BALANCE CHARACTERIZATION VALIDATED (2026-07-09) — the forcing lemma is now clean

The cohomology reformulation FAILED only because my balance check DROPPED bar-D
SELF-LOOPS (advisor-located, trace-verified: node {1,2} in
[(0,1),(1,0),(1,1),(1,2),(2,1),(2,2)] has a parallel self-loop (2,1)→(2,1) via
(2,2),(1,1)∈ρ = sign m+1=1 = frustration, giving unsafe at L=4; my check skipped
len-1 edges). All 19 mismatches were ONE-DIRECTIONAL (balanced=True/safe=False =
under-detecting frustration) = the signature of dropped frustration edges, NOT a
wrong sign convention (that mismatches both ways). Fixed: a parallel self-loop
(m=0) on bar-D ⟹ imbalance.

**VALIDATED EQUIVALENCE (A=3 FULL enum 144 langs 0-mismatch; A=4 800-sample
0-mismatch; NOT a tautology — bal=soe=12 of 144, both non-trivial):**

  **safe-on-evens ⟺ swap-monodromy walk exists only at odd L ⟺ the signed graph
  (bar-D, sign = monodromy+1) is BALANCED**

where bar-D = unordered-pair graph (vertices {a,b}, a≠b); an arc from an ordered
(a,b)→(c,d) [(a,c),(b,d)∈ρ] carries monodromy m=0 (parallel, order-preserving in
the ascending frame) or 1 (crossed); sign = m+1. Balanced ⟺ every closed walk has
monodromy ≡ length (mod 2) ⟺ ∃ Z₂-potential φ on pairs with m = 1+Δφ. This IS the
intrinsic re-derivation of the parity mechanism (shadow of det(I+P)=1−(−1)^L).
Oracle+detector: `z2_potential.py`.

**⟹ THE FORCING LEMMA (the parity-only content, `win.named_lemma` floor), now
clean and stateable:**

  **PRIMITIVE ⟹ [ (m+1)-signed bar-D is BALANCED  OR  the safe set is finite ].**

Equivalently: a PRIMITIVE language with an INFINITE safe set has balanced signed
bar-D (⟹ safe-set = evens). This is exactly "primitive ⟹ parity is the only
source of residue-safety." Data: A=3 all 9 primitive-infinite-safe are balanced;
~25,700 primitives 0 counterexample to safe⟹evens. ⚠ HOLD THE LINE: balance⟺
safe-on-evens is a re-CHARACTERIZATION, NOT the forcing. The forcing (primitive ⟹
balanced-or-finite-safe) is the OPEN content and is NOT touched by the harness.
Balance does not obviously interact with primitivity — that gap IS the lemma.
NEXT: attempt to prove the forcing, or fence it as the paper's stated open lemma.

### THE CLEAN REDUCTION (2026-07-09 landing) — cycle-space / ℤ₂×ℤ₂ reframe

Advisor-directed. Map two functionals on closed walks of bar-D (through a
basepoint): **length mod 2** and **monodromy mod 2**. This is a homomorphism from
bar-D's cycle group to ℤ₂×ℤ₂; let **G** = its image. Then (bar-D strongly
connected; the 3/139 disconnected cases handled separately):

| G | meaning | safety |
|---|---------|--------|
| diagonal {(0,0),(1,1)} | mono ≡ length | safe-on-EVENS |
| full ℤ₂×ℤ₂ | odd-mono at both length-parities | FINITE safe (cofinitely unsafe) |
| {(0,0),(0,1)} mixed | odd-mono only at even length; no odd closed walk | (would be safe-on-odds-ish) |
| {(0,0),(1,0)} mixed | no odd-mono ever = σ-cover D→bar-D disconnected | safe at ALL L |

**TWO LEMMAS:**
- **L-A (re-characterization, ✅ PROVED below for s.c. bar-D, COFINITELY, via the
  G-homomorphism, no empirics; disconnected bar-D = per-component obligation, not
  automatic — see caveat):** balanced ⟺ G ⊆ diagonal ⟺ safe-on-evens.
- **L-B (THE FORCING, the open content):** **PRIMITIVE ⟹ G is diagonal or full,
  never mixed.** = two Perron–Frobenius exclusions:
  - exclude {(0,0),(0,1)}: primitive ⟹ bar-D has an odd-length closed walk
    (bar-D aperiodic). [tested via barD_period]
  - exclude {(0,0),(1,0)}: primitive+s.c. ⟹ a crossed cycle exists (σ-cover
    connected). **This also EXPLAINS why NO safe-on-odds language was ever found
    (safe_res=[1]) — that would need this excluded G; a hole not previously named.**

**EMPIRICS (G-type census): A=3 FULL 139 primitives = 9 diagonal + 130 full, 0
MIXED. A=4 sample 1500 = 2 diagonal + 1498 full, 0 mixed. A=5 sample 1500 = all
full, 0 mixed.** ~3100 primitives, 0 mixed. Also: primitive-unbalanced ⟹ finite
safe holds 130/130 at A=3 (0 forcing violations).

**PROOF of L-A (⟦HAND⟧, structural, no empirics; bar-D strongly connected).**
Fix a basepoint P₀ in bar-D. Every closed walk W at P₀ has two ℤ₂ invariants:
its length λ(W)=|W| mod 2 and its monodromy μ(W)=Σ(edge signs) mod 2, where the
edge sign is 0 (parallel) / 1 (crossed) in the σ-cover D→bar-D. Both λ and μ are
homomorphisms (closed-walk concatenation adds lengths and adds monodromies mod 2),
so (λ,μ): {closed walks at P₀} → ℤ₂×ℤ₂ is a homomorphism; let G be its image (a
subgroup, independent of P₀ up to conjugation since bar-D is s.c.).
  By the VALIDATED characterization, unsafe at L ⟺ ∃ a swap-monodromy closure of
  length L ⟺ ∃ a closed walk W with λ(W)≡L (mod 2) and μ(W)=1 (odd monodromy =
  swap). So: **L is unsafe ⟺ (L mod 2, 1) ∈ G.**
  Now safe-on-evens = [every even L safe] ∧ [some odd L unsafe]
    = [(0,1)∉G] ∧ [(1,1)∈G].
  (i) balanced ⟺ every closed walk has μ≡λ ⟺ G ⊆ diagonal {(0,0),(1,1)}.
  (ii) balanced ⟹ (0,1)∉G [not on diagonal] and, since bar-D is s.c. and carries
  a crossed edge in the s.c. non-trivial case, (1,1)∈G ⟹ safe-on-evens.
  (iii) safe-on-evens ⟹ (0,1)∉G; and (1,0)∈G would force (by adding to (1,1)∈G)
  the element (0,1)∈G, contradiction, so (1,0)∉G; hence G∩({0,1}×{0,1}) avoids
  both (0,1),(1,0) ⟹ G ⊆ diagonal ⟹ balanced. ∎
  [The (1,1)∈G existence in (ii) is exactly the crossed-cycle fact that L-B's 2nd
  exclusion supplies for primitive languages; for GENERAL s.c. bar-D it is the
  hypothesis distinguishing safe-on-evens from safe-at-ALL-L (G={(0,0),(1,0)}).]

So L-A is PROVED for STRONGLY-CONNECTED bar-D modulo standard basepoint
independence; the ONLY open content is L-B (primitive ⟹ G diagonal-or-full).

**⚠ VERIFY-BY-BUILDING CAVEAT (the identity's s.c. hypothesis BITES).** Checked the
key identity "unsafe at L ⟺ (L mod 2,1)∈G" against the oracle (A=3 FULL). For L
large it holds EXCEPT on exactly the bar-D-NON-s.c. languages (e.g.
[(0,2),(1,2),(2,0),(2,1)]: language s.c. but bar-D NOT s.c.; naive single-basepoint
G={(0,0)} misses the crossed odd cycle living in another component, mispredicting
unsafe at L=11,13). So for disconnected bar-D the NAIVE global G is WRONG — the
"handled per component" clause is NOT automatic and must be spelled out (take the
image over the component carrying the relevant closure). The COMPONENT-AGNOSTIC
oracle that is correct throughout = `signed_balance` (checks ALL edges/self-loops
for frustration), which matched safe-on-evens with 0 mismatch on A=3 FULL incl.
these cases. Net: L-A holds; its clean G-image statement is s.c.-bar-D-scoped, and
the disconnected case is a spelled-out-per-component obligation, not a freebie.
(Small-L artifacts also present: the identity is a COFINITE statement — at small L
a parity class in G may not yet be realizable at that exact length.)

**⚠ SCOPE CAVEAT (blind spot, advisor-flagged):** EVERYTHING runs on `lisc2_raw` =
winding-EXACTLY-2. Full safety = no LISC winding ≥2 for ANY k. This instrument is
STRUCTURALLY BLIND to a winding-≥3 gap (same shape as the R2 tautology). So the
result as validated is about **winding-2 safety**. Joint 1 (pruning lemma,
TR_k=LISC_k all k, CLOSED) is the intended bridge from winding-2 to full safety —
if it bridges cleanly, parity-only lifts to full safety in one line; if not, the
result is SCOPED to winding-2 and the UI connection is not yet made. RESOLVE
before claiming full-safety parity-only.

⚠ Joint 1 gives unsafe = ∪_{k≤|A|} LISC_k (a UNION, NOT a containment
LISC_k⊆LISC_2). So a winding-≥3 LISC could in principle add an even unsafe length
the winding-2 oracle never sees. **DISCRIMINATOR RUN (advisor-directed,
`pruning_lemma_fine.py::LISC_windings`, kmax=3): all 9 A=3 witnesses SAFE at even
L=4,6,8,10 for windings 2 AND 3; golden-mean CALIBRATION anchor (theorem-grade
safe-at-even via thm:parity) returns empty winding-set at those L = oracle
trustworthy.** ⟹ the winding-2→full-safety bridge HOLDS EMPIRICALLY for these
witnesses (parity-only survives as a FULL-safety statement, not winding-2-only).
NOT proof: kmax=3 at A=3 only; the general containment is unproven — the honest
lift is Joint-1 applied per-length, still owed.

**NET (honest landing = win.named_lemma floor REACHED):** parity-only ⟸ [L-A:
validated, provable via G-homomorphism] ∧ [L-B forcing = 2 PF exclusions:
validated ~3100 primitives 0-cex, OPEN] ∧ [Joint-1 winding-2→full bridge: closed,
verify it applies]. L-B is the single clean open lemma = completes the paper's arc
(sharpens 'ten stamps + vague conjecture' → 'one clean PF-exclusion lemma'). Do
NOT push a 3rd self-designed padding proof this session (that pattern produced 2
closure bugs). Fence L-B honestly: the padding argument does NOT yet cover the
3/139 bar-D-disconnected cases + the 2 PF exclusions are unproven. Oracles
(persisted in papers/reconstruction/oracles/): `parity_only_z2_balance.py` (= z2_potential:
balance/G-type detector + safe-on-evens oracle), `parity_only_swap_monodromy.py`
(= crossing_parity_v2: validated winding-2 = swap-monodromy, 1600 langs
0-mismatch), `parity_only_witness_channel.py` (= witness_channel: non-circular R1
enumeration).

## CROSSED-CYCLE EXCLUSION — attack opened (2026-07-09, next session start)

Attacking L-B's EASIER half (user-selected): the {(0,0),(1,0)} exclusion.

**TARGET (verified well-posed):** primitive + s.c. ρ ⟹ ∃ a crossed cycle in bar-D
= an odd-monodromy closed walk = a walk in the ordered-pair digraph D from some
(a,b) to (b,a). This excludes G={(0,0),(1,0)} ⟹ proves **primitive ⟹
NOT-safe-at-all-L**, and turns "no safe-on-odds language exists" into a theorem.
A clean win here = HALF of L-B + that corollary (the aperiodicity exclusion + the
winding-2→full bridge stay open).

**VERIFY-FIRST (advisor-mandated, done):**
- crossed-cycle (D-reachability (a,b)⇝(b,a)) ⟺ NOT-safe-at-all-L: **0 mismatches,
  A=3 FULL** (144 s.c. langs). Reframe is EXACT, not just necessary.
- **Kronecker lever HOLDS:** D = ρ⊗ρ restricted to off-diagonal vertices; primitive
  ρ ⟹ ρ⊗ρ strongly connected on ALL ordered pairs. Verified 0 failures / 139 A=3
  primitives via matrix-power reachability.
  ⚠ LESSON: my FIRST combined script reported "5 failures" — a BUG in inline
  reverse-reachability code, NOT a real crack. The confirmation-bias guard cuts BOTH
  ways: a sloppy check manufactured a phantom OBSTRUCTION just as it can manufacture
  phantom confirmation. Independent matrix-power re-impl settled it (0). Same
  discipline (re-verify independently) that caught the earlier phantom confirmations.

**RETARGET (advisor lever, confirmed):** since ρ⊗ρ is s.c. on all pairs, (a,b)
ALREADY reaches (b,a) in the full product. The ONLY content of the crossed-cycle
claim = some such path can AVOID THE DIAGONAL (stay in D = off-diagonal). So:
  **primitive + s.c. ⟹ some off-diagonal (a,b) reaches (b,a) by a ρ⊗ρ-path that
  never touches a diagonal vertex.**

**MECHANISM to find (hand, next):** "no crossed cycle" = every swap-route is FORCED
through the diagonal (the two threads must COLLIDE to swap). That is a rigidity;
pure permutations (threads can't pass without meeting) are IMPRIMITIVE (period =
cycle length), so primitivity with ≥2 states already excludes the determinism case.
Proof idea: primitivity = arcs beyond a single cycle = a ROUTING GADGET (fork/branch)
letting one thread detour while the other passes. Find the gadget on the simplest
witness; that is likely the whole proof. Oracle: `has_crossed_cycle` in this session's
scratchpad; the reframe + Kronecker facts verified above.

### CROSSED-CYCLE — mechanism pinned; the "fork" proof-idea REFUTED (2026-07-10)

Persisted the oracle (`crossed_cycle_exclusion.py` + 4 probe scripts, all in
papers/reconstruction/oracles/). Re-confirmed the theorem holds at scale, then found the CORRECT
discriminator — which is NOT the one the attack-open note guessed.

**Foundation re-verified (independent re-impl of last session's scratchpad oracle):**
- primitive ⟹ crossed cycle: **0 counterexamples, A=3 FULL (144) + A=4 FULL
  (25,696 s.c. langs).** Theorem solid at scale.
- `crossed_cycle_exclusion.py::has_crossed_cycle` = D-reachability (a,b)⇝(b,a) on
  the off-diagonal ordered-pair digraph. This IS the ground-truth oracle now.

**THE KEY STRUCTURAL LAW (census of the NO-CROSS languages — the complement):**
- no-cross ⟹ **IMPRIMITIVE with ODD period ≥3** (A=3: 2 langs, both period 3;
  A=4: 12 langs, all period 3; A=5 sample: periods 3 and 5 only). **NEVER period 2,
  NEVER even, NEVER period 1.** (`crossed_cycle_potential.py` asserts no-cross ⟹
  period≥2, held for all.)
- no-cross is STRICTLY STRONGER than imprimitive: there ARE imprimitive langs WITH a
  crossed cycle (A=3: 3; A=4: 109). So the theorem is one-directional **primitive ⟹
  crossed**; "crossed ⟺ primitive" is FALSE. Contrapositive = no-cross ⟹ imprimitive
  (period≥2), and that's all we need.
- Every no-cross lang admits a consistent Z₂ sign on off-diag pairs
  (`sign_consistent=True`, `crossed_cycle_mechanism.py`) AND its ℤ_d grading (d=odd
  period) distributes states so cross-grade swaps are killed by grading
  (`crossed_cycle_grading.py`).

**⚠ THE ATTACK-OPEN PROOF-IDEA IS REFUTED (confirmation-bias guard, this session).**
The note above proposed: "primitivity = a fork/branch beyond a permutation lets one
thread detour; pure permutations are the only rigid (no-cross) case." **FALSE.** The
12 no-cross A=4 langs ALL have fork=True AND merge=True (out-deg≥2 and in-deg≥2) —
they are NOT permutations, they have routing gadgets, yet still no crossed cycle
(`crossed_cycle_direct.py`). So fork-existence is NOT the discriminator. The real
discriminator is the **ODD GRADING**, not the presence of a branch.

**THE CORRECT MECHANISM (the grading/potential argument — proof route, NOT yet a
proof):** Along any D-arc (a,b)→(c,d) both coordinates advance the ℤ_d grading by
the SAME +1, so **g(a)−g(b) mod d is INVARIANT along every D-walk.** A swap
(a,b)⇝(b,a) needs g(a)−g(b) ≡ g(b)−g(a), i.e. **2·(g(a)−g(b)) ≡ 0 mod d.** For d
ODD this forces g(a)=g(b): cross-grade swaps are impossible; only same-grade pairs
could swap. In the no-cross langs the (few) same-grade off-diag pairs also fail to
swap. **Primitive = d=1 = grading trivial = every pair "same grade" = the invariant
is VACUOUS**, which is exactly why primitivity should force a crossed cycle. The
remaining gap: prove "no-cross ⟹ a nontrivial ODD grading exists" (construct the
grading FROM the no-cross hypothesis), then primitive (d=1) ⟹ crossed by
contradiction. The odd-ness and the same-grade residual case are the two things to
nail. NEXT: construct the grading directly from no-cross (the Z₂-sign consistency +
odd period census both say it exists), OR prove the same-grade swap directly via
Kronecker s.c. on the same-grade sub-block.

**⚠ Advisor UNAVAILABLE this session (repeated timeouts).** Load-bearing checks were
re-verified by independent re-implementation instead (foundation 0-cex at A=4 FULL).
The grading argument above is a ROUTE, verified in its necessary direction (grading
kills cross-grade swaps) but NOT yet closed (no-cross ⟹ odd-grading-exists is the
open construction). Do NOT round it up to a proof.

**Oracles (persisted, papers/reconstruction/oracles/):**
- `crossed_cycle_exclusion.py` — `has_crossed_cycle` ground truth + primitive⟹crossed
  verifier (0-cex A=3+A=4 FULL).
- `crossed_cycle_mechanism.py` — no-cross census + Z₂-sign consistency.
- `crossed_cycle_grading.py` — ℤ_d grading of no-cross langs, same-grade pair readout.
- `crossed_cycle_direct.py` — fork/merge census (REFUTES the fork proof-idea).
- `crossed_cycle_potential.py` — asserts no-cross ⟹ period≥2 (odd) across the census.

### CROSSED-CYCLE — MASTER LEMMA: crossed ⟺ antipodal-free even closed walk (2026-07-10, session 4)

Supersedes routes (A) grading-construction and (B) same-grade-Kronecker from the
section above — a third, direct route closed most of the distance in one step.

**⟦HAND⟧ MASTER LEMMA (token-riding).** If G has a closed walk W of even length 2m
with W(t) ≠ W(t+m) for all t ∈ [0,m], then (W(0),W(m)) ⇝ (W(m),W(0)) in D.
*Proof.* Ride W with two tokens offset by m: token1 = W(t), token2 = W(t+m),
t = 0..m. Consecutive positions are G-arcs (consecutive W-steps), so each step is a
D-arc; the antipodal condition W(t)≠W(t+m) is exactly off-diagonality; at t=m the
pair is (W(m), W(2m)) = (W(m), W(0)). ∎

**⟦HAND⟧ CONVERSE.** If (a,b) ⇝ (b,a) in D via pair walk (x_t,y_t), t=0..m, then
W = x_0..x_m y_1..y_m is a closed walk (x_m = b = y_0, y_m = a = x_0) of even
length 2m, and W(t+m) = y_t ≠ x_t = W(t). ∎

**So: crossed cycle exists ⟺ G has an antipodal-free even closed walk.** The whole
exclusion problem is now INTRINSIC to G (no pair digraph needed). Machine-checked
both directions (`crossed_cycle_master_lemma.py`): every certificate walk is
re-verified as an explicit D-path (`verify_swap_path`), and the converse
construction is asserted on every crossed lang (A=3 FULL 144, A=4 4000 langs,
`sweep_equivalence`).

**⟦HAND⟧ COROLLARIES (necessary conditions for no-cross).**
- **Cor 1: no-cross ⟹ no even simple cycle.** Antipodal tokens on an even simple
  cycle never coincide (offset m ≢ 0 mod 2m).
- **Cor L: no-cross ⟹ no loops** (n≥2, s.c.). Loop vertex v lies on a simple cycle
  C of length ℓ≥2; ℓ even → Cor 1; ℓ odd → W = loop·C works (Cor 2 with p=1).
- **Cor 2: two odd simple cycles of DISTINCT lengths p≠q sharing EXACTLY ONE
  vertex x ⟹ crossed.** W = C₁·C₂ based at x: the only possible antipodal clash
  is an "index-locked" shared vertex C₁(i) = C₂(i + (q−p)/2) with i ∈ [0,p); the
  lone shared vertex x has indices (0,0) and (q−p)/2 ≢ 0 mod q, so no clash.
- **Consequence: no-cross ⟹ ALL simple cycle lengths odd ⟹ period = gcd is odd.
  The census law "no-cross ⟹ odd period ≥3" REDUCES to the primitive case**
  (primitive ⟹ crossed gives period ≥2; odd ∧ ≥2 ⟹ ≥3).

**Oracle results (`crossed_cycle_master_lemma.py`, all assertions green):**
- Predictions P1 (no loops) + P2 (all simple cycles odd) HOLD on every no-cross
  lang found: A=3 (2), A=4 FULL (12), A=5 sample (4), n=6 period-3 hunt (124).
  Counts cross-validate session 3 exactly (25,696 = 25,575 prim + 12 + 109).
- Discriminating direction at n=6 (first size where a 6-cycle fits in a period-3
  graph, grading-legal but Master-Lemma-forbidden): 235/235 period-3 graphs WITH
  an even simple cycle are crossed.
- **Candidate-walk family explains 100% of primitives** at A=3 (139/139),
  A=4 FULL (25,575/25,575), A=5 sample (12,623/12,623). Breakdown: single even
  simple cycle ≈99.3%; shared-base two-odd-cycle walk (laps ≤3) covers ALL the
  rest; **the disjoint-cycles case was NEVER needed at A≤5.**
- Canonical minimal hard case (C5 + chord: cycles {3,5} sharing 3 vertices,
  even-cycle-free, primitive): W = C₃·C₅ works at EVERY base with laps (1,1).

**THE REMAINING GAP (sharply narrowed).** Prove: primitive + no loops + all simple
cycles odd ⟹ some shared-base walk C_p^a·C_q^b (p≠q odd) is antipodal-free.
Lock analysis for a=b=1, q>p, base x: fails iff some shared vertex v has
C₂-index = C₁-index + (q−p)/2 exactly. Freedom to burn: choice of base point
(shifts all index pairs), order (C₂·C₁), lap counts (a,b). Same-length pairs
(p=q) provably NEVER work (m ≡ 0 mod p forces a clash) — distinct lengths are
essential, and primitivity (gcd 1, all odd) guarantees they exist. NOTE the
imprimitive no-cross langs must and do defeat every family member (oracle
soundness assertion: a working walk in a no-cross lang would be a contradiction —
never fired).

**⚠ PRIOR-ART FLAG (owed before any novelty claim).** (1) The equivalence
"swap-reachability in the deleted tensor square ⟺ antipodal-free even closed
walk" is elementary — plausibly known (automata theory / symbolic dynamics /
even-cycle literature). (2) Thomassen's even-dicycle theorem (every strongly
2-connected digraph has an even directed cycle, JAMS ~1992 ⟦from memory —
VERIFY⟧) + Cor 1 would give: no-cross ⟹ not strongly 2-connected — structural
leverage for the remaining gap, and a sign this area is well-ploughed. Run the
HOSTILE cross-field prior-art scout BEFORE writing this into the paper.

**Discipline.** Advisor not consulted this session (was down session 3); every
⟦HAND⟧ claim above is machine-verified by an independent fresh implementation
(new oracle does not import the old one). One bug caught by the assertions
during development (walk-generator lap concatenation; converse construction
off-by-one) — the certificate-checking layer (`verify_swap_path`,
`check_equivalence` asserts) is what caught both. Keep it.

### CROSSED-CYCLE — LOCK-AVOIDANCE LEMMA PROVED: primitive ⟹ crossed (2026-07-10, session 5)

The gap flagged above is CLOSED. ⟦HAND + machine-verified stepwise⟧ — every
load-bearing computation below carries an oracle assert that ran green on the
exhaustive universes listed at the end; not Lean-formalized.

**LOCK-AVOIDANCE LEMMA.** Let U be a digraph in which every simple directed
cycle has odd length, containing two simple cycles of distinct lengths with a
common vertex. Then some pair (A, B) of simple cycles of distinct odd lengths
p' < q' with a common vertex x has the laps-(1,1) walk W = A·B based at x
antipodal-free. In particular U has an antipodal-free even closed walk, hence
(Master Lemma) a crossed cycle.

**THEOREM (crossed-cycle exclusion, the {(0,0),(1,0)} branch of L-B).** For
strongly connected G on ≥ 2 vertices: no crossed cycle ⟹ no loops, every
simple cycle odd, and ALL simple cycles have the SAME length d = period(G),
an odd number ≥ 3. Contrapositives: **primitive ⟹ crossed**, and the census
law "no-cross ⟹ odd period ≥ 3" is now a THEOREM (not merely reduced to the
primitive case). The remaining open half of L-B is unchanged: exclude
{(0,0),(0,1)} (bar-D aperiodic — the hard half).

**Derivation of the theorem from the lemma.** No-cross ⟹ no even simple
cycles (Cor 1) + no loops (Cor L). If two distinct simple-cycle lengths
existed: (chain-connectivity, below) some two cycles of DISTINCT lengths
share a vertex; the lemma then gives an antipodal-free even closed walk ⟹
crossed (Master Lemma): contradiction. So all simple cycles have one odd
length d; period = gcd of simple-cycle lengths = d; d ≠ 1 (no loops), d ≠ 2
(even), so d ≥ 3 odd. ∎

**Chain-connectivity (kills the disjoint case).** In a strongly connected
digraph the simple cycles form a connected "sharing chain": for cycles C, C'
take x ∈ C, y ∈ C', paths x→y→x; the closed walk's support is a connected
arc-balanced digraph, so its cycle decomposition chains by shared vertices
from x to y. Walking a chain from a p-cycle to a q-cycle (p ≠ q), some
adjacent pair has distinct lengths and shares a vertex. So "two distinct
lengths exist" ⟹ "a SHARED distinct-length pair exists" — the two-path
disjoint construction of session 4's oracle is never needed.

**Proof of the lemma** (by contradiction; suppose a TOTAL STALL: every
shared distinct-length odd pair fails at every base at laps (1,1)).

Setup, for a pair (D, D') with |D| = p < q = |D'|, both odd, shared set S,
coordinates i (position on D) and j (position on D'), δ := (q−p)/2,
m := (p+q)/2, and base u ∈ S:

1. *(1,1) lock analysis (exact iff).* W = D·D' at u fails the antipodal test
   ⟺ ∃ v ∈ S∖{u} with J = I + δ, where I = (i_v − i_u) mod p ∈ [1, p−1] and
   J = (j_v − j_u) mod q. ("v kills u.") The only clash channel is the
   straddle window [0, p]; the two same-segment channels are empty/impossible
   at (1,1), and self-clash is impossible. [Oracle assert H1, validated as an
   iff against the semantic walk test on every pair/base swept.]
2. *Kill symmetry.* v kills u ⟺ u kills v (the difference vectors are exact
   negatives: (p−I) + δ = q − J). Failure at all bases = every vertex of S
   covered by a "kill edge". [Assert H2.]
3. Choose the failing pair (D, D') minimizing p + q, and among its ordered
   kills (u → v) choose one minimizing the directed D-distance I =: dmin.
4. *Hybrid.* The kill forces both hybrid closed walks D[u→v]·D'[v→u] and
   D[v→u]·D'[u→v] to have length exactly m (arithmetic identity from
   J = I + δ). [69k machine checks.]
5. If the hybrid H = D[u→v]·D'[v→u] is a SIMPLE cycle: it is odd (all-odd U),
   length m ≠ p, shares u with D: the pair (D, H) has sum p + m < p + q and
   also fails (total stall) — contradicting sum-minimality. So H is
   non-simple.
6. *Decomposition.* H peels into k ≥ 2 simple cycles covering its arc
   multiset; each piece contains at least one D-provenance arc (a pure-D'
   piece would be a closed subwalk of the simple q-cycle D', forcing length
   q > m — impossible). [Assert: decomposition validity; piece provenance.]
7. If some piece E has length e ≠ p: e ≤ m − 1 < q, E shares a vertex with
   D, so (E, D) is a shared distinct-length odd pair of sum e + p < p + q —
   contradiction as in 5. So ALL pieces have length exactly p ("2c"), giving
   k = m/p ≥ 2 and q = (2k−1)p (so this last case only exists when p | q).
8. *Peeling chain.* The peel of H has the form: shared vertices
   u = x_k, x_{k−1}, …, x_1, x_0 = v with pieces
   P_t = D[x_t → x_{t−1}] · D'[x_{t−1} → x_t], each a simple p-cycle;
   a_t := D-length of P_t's segment, Σ a_t = I = dmin, a_t ≥ 1. [Asserted via
   provenance-aware peeling; note D ∩ D' may share arcs, so provenance is by
   position, not arc identity.]
9. *Endgame.* Fix any piece P_t and consider the pair (P_t, D') — distinct
   odd lengths (p, q), shared. By the total stall it fails at every base; in
   particular its base x_t is killed within this pair. But inside
   S(P_t, D') = {D'-run vertices} ∪ {endpoints} ∪ {original shared vertices
   strictly interior to the D-segment}: run vertices never kill run vertices,
   and the endpoints never kill each other (both by direct computation — the
   kill equation degenerates to δ = 0 or q = m or q = p + δ, all false). So
   the killer w of x_t is strictly interior to the D-segment and satisfies
   the exact equation τ(w) = τ(x_t) + δ (mod q), where τ(y) := (j_y − i_y)
   mod q. That equation says precisely that (x_t → w) is an ordered kill of
   the ORIGINAL pair (D, D'), of directed distance ≤ a_t − 1 < dmin —
   contradicting the minimality of dmin. And if a_t = 1 the segment has no
   interior at all, so x_t is unkilled and (P_t, D') did not fail — also a
   contradiction. ∎ [Assert suite: probe_endgame — killer interiority,
   τ-equation, shorter ordered kill, clean-piece freeness, Σ a_t = I.]

**Refuted intermediates (kept for honesty; both machine-refuted).** (i) The
first descent attempt "(M): some kill edge of a failing pair has a SIMPLE
hybrid" is FALSE — 80 counterexamples at (7,13), where all kill hybrids
decompose 5+5. (ii) "δ-odd pairs never fail at all bases" (P(a)) is FALSE at
the same instances. The failing pair's rescue is a smaller-SUM pair (5,7),
not a smaller gap — hence the sum measure in step 3. (iii) Genuine 2c stalls
EXIST (all kill hybrids all-length-p): first at (5,15), s = 4, e.g. shared
coordinates (ĩ,j̃) = (0,0),(1,11),(2,7),(3,3) — an all-odd union
{5,5,5,5,5,15} whose glueing pair fails at all bases with every hybrid
peeling 5+5. These are exactly why step 9 exists. A hand-built all-dirty
(9,27) candidate that would defeat the weaker "clean-piece" repair forces
EVEN hybrid cycles (18-cycles) and is not all-odd — consistent with the
theorem.

**Consequences for the walk family.** Session 4's empirical family
(laps ≤ 3, disjoint path-joined variants) collapses: SOME pair of odd cycles
of distinct lengths (hybrids allowed) always works at laps (1,1) from a
shared base — laps and path-joining are never needed. (For a FIXED pair,
laps genuinely cannot rescue a failure: order is a rotation, odd laps leave
the offset unchanged mod q, even laps self-clash when p | q.) The n = 6
period-3 hunt's "grading-legal but Master-Lemma-forbidden" discriminator is
subsumed: all-same-length is now proved necessary for no-cross.

**Oracles (persisted, papers/reconstruction/oracles/), all asserts green:**
- `lock_avoidance_lemma.py` — glued two-cycle universe (the lemma's EXACT
  universe: every candidate walk lives in the union of the pair, so glueings
  are exhaustive, not a census sample); sweeps p ∈ {3,5,7}, q ≤ 13(19),
  s ≤ 4 (~hundreds of thousands of glueings, ~5.8k–38k failing pairs);
  asserts H1 (iff), H2, H3 (consecutive hybrids simple), certificate-checks
  every positive with `verify_swap_path`. Result: every all-odd glueing with
  distinct lengths is explained by a MIN-GAP pair at (1,1); 0 exceptions.
- `lock_avoidance_probe_M.py` — refutes intermediates (M) and P(a); verifies
  the hybrid-length-m identity 69,064×.
- `lock_avoidance_probe_descent.py` — sum-descent case analysis on all 5,775
  failing pairs (q ≤ 13): case counts 68,744 simple / 224 mixed / 96
  equal-e≠p / 0 stalls; 0 descent failures.
- `lock_avoidance_probe_endgame.py` — step-9 dichotomy on every failing
  pair's minimal ordered kill; the four genuine (5,15) stalls verify.
- `lock_avoidance_rho0_927.py` — exhaustive class-ρ₀ search at (9,27), the
  smallest all-dirty-stall territory: 72,171 configs, 2,358 all-odd with
  failing pairs, 0 L1 violations; 7,458 failing pairs, ALL 2c minimal-kill
  endgames verified, 0 assertion failures.

**HOSTILE PRIOR-ART SCOUT (run this session, before the paper touches any of
this — verdicts + citations):**
- *The equivalence (crossed ⟺ antipodal-free even closed walk):* NOT FOUND
  as a named theorem; judged elementary/folkloreable. Closest named objects
  are genuinely different: Gao–Shao, "Double vertex digraphs of digraphs,"
  Discrete Math. 309(8):2432–2444 (2009) (ordered pairs, but ASYNCHRONOUS —
  one token moves per step); Fernandes–Lintzmayer–Peña–Santos–
  Trujillo-Negrete–Zamora, "A study on token digraphs," arXiv:2410.20189
  (unordered pairs, asynchronous — swap not even expressible). No source
  found with synchronous dynamics on ordered pairs minus diagonal, nor the
  term "antipodal-free".
- *Primitive ⟹ crossed:* classical layer known — primitivity of the FULL
  tensor square A⊗A (McAndrew, PAMS 14:322–328, 1963; undirected ancestor
  Weichsel, PAMS 1962) — but the diagonal-AVOIDANCE content was not located
  anywhere (swept: Wielandt/exponent, scrambling index, synchronizing
  automata / road coloring — Trahtman's stable pairs are collision-SEEKING,
  the opposite). Treat as plausibly new, pending the two paywalled follow-ups
  below.
- *⚠ THOMASSEN CITATION CORRECTED (the session-4 from-memory flag was
  WRONG).* "Strongly 2-connected ⟹ even dicycle" is FALSE — Seymour has a
  7-vertex strongly-2-connected counterexample. The true statements:
  Thomassen, "The even cycle problem for directed graphs," JAMS 5(2):217–229
  (1992): strong digraphs with min in-/out-degree ≥ 3 (corollary forms:
  every 3-regular-or-more digraph; every strongly 3-connected digraph)
  contain an even dicycle. McCuaig, "Even dicycles," JGT 35(1):46–68 (2000):
  there is a UNIQUE strongly 2-connected digraph with no even dicycle, plus
  a structure theory. Also: Thomassen, EJC 6(1):85–89 (1985) (min out-degree
  alone never suffices); Seymour–Thomassen, JCTB 42(1):36–45 (1987)
  (characterization of even digraphs — the foundational structure result for
  our "no loops + all cycles odd" hypothesis class); Robertson–Seymour–
  Thomas, Ann. Math. 150(3):929–975 (1999) + McCuaig, EJC 11 #R79 (2004)
  (recognition/Pfaffian side); Gorsky et al., arXiv:2311.16816 (STOC 2024)
  (modern odd-digraph structure theory). The session-4 leverage note
  "no-cross ⟹ not strongly 2-connected" is therefore WRONG as stated; the
  correct forms: no-cross ⟹ not strongly 3-connected, and if strongly
  2-connected then G is McCuaig's unique exception.
- *OWED (scout follow-ups):* full-text verification of Gao–Shao 2009 and of
  "Multi-agent pathfinding on strongly connected digraphs" (ScienceDirect,
  2025) — both paywalled this session; definitions recovered from abstracts,
  theorem statements unverified.

**Status flags.** Everything in this section: ⟦HAND + machine-verified
stepwise⟧, zero-sorry-equivalent at the oracle level, NOT Lean-formalized.
SCOPE fence unchanged: winding-2; the full-safety bridge remains
spot-checked, not proved. The bar-D aperiodic half of L-B remains OPEN.
