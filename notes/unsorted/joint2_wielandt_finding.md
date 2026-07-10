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
(`scratchpad/joint2_wielandt.py` part I): a language is graded-at-some-d ⟺ its
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

**Empirical confirmation** (`scratchpad/joint2_wielandt.py` II + `joint2_deep.py`):
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

**First deep adversarial sweep (`scratchpad/fork_hunt_scale.py`):** 1500 primitive,
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

Ran the NON-CIRCULAR witness channel (`scratchpad/witness_channel.py`): enumerate
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
(persisted in notes/unsorted/): `parity_only_z2_balance.py` (= z2_potential:
balance/G-type detector + safe-on-evens oracle), `parity_only_swap_monodromy.py`
(= crossing_parity_v2: validated winding-2 = swap-monodromy, 1600 langs
0-mismatch), `parity_only_witness_channel.py` (= witness_channel: non-circular R1
enumeration).
