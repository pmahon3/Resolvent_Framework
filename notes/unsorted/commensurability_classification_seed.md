# Seed — Commensurability classification for dynamical protocols (EA/PR(𝓡))

*2026-07-06. Captured from the design session
(claude.ai/share/059e292f-97f0-4787-808e-c89a88dbced4, post-witness turns) by the
verification session. **Division of labour declared by the user:** the design
session conducts mathematical planning/design/reasoning via discussion; this
repo side verifies (Lean + auditing tools); writing comes after verification.
This seed is the repo-side capture of the design state.*

**Programme reorientation this seed records:** dynamics/reconstruction is
ACTIVE again — as the successor programme to the (now machine-checked) σ-essential
witness, oriented toward practical reconstruction. Route chosen: traditional /
foundations-first. The σ-essential frontier triple (OML conjecture; no-singletons
regime; positive-selection strength question) stands separately — see
`papers/sigma_essential/witness_candidate/VERIFICATION_VERDICT.md` §2–3 and the
taxonomy; this seed is the dynamical/reconstruction side only.

**Claimed type(s):** Type 1 (new theorem — the classification theorems T1/k=2/
axis-reduction, PENDING the derive-then-compare gates below; high prior-art risk
acknowledged up front). Type 3 (unifying framework — EA/PR(𝓡) as the single
vocabulary spanning Paper II's algebraic separation, the witness's set-theoretic
separation, and the observational/dynamical separation; bar: method transfer —
contextuality LP/sheaf machinery producing theorems about dynamical protocols,
not analogies). Type 7 downstream (methodology — CF_d as an aggregation-artifact
detector; bar: demonstrated advantage on concrete problems, deferred to the
pipeline phase). **Bar for Type 1:** each classification claim must survive a
hostile prior-art pass against the declared shelf (below) — the k=2 theorem in
particular is expected to be classical-adjacent (marginal-problem folklore), and
the honest deliverable there may be Type 6 placement rather than Type 1.

---

## 1. Locked definitions (design session; to be transcribed to Lean by user)

- **Protocol**: a family of clopen contexts, each a partition of A^F for a
  finite support F ⊆ ℤ (A a finite alphabet).
- **EA** (empirical adequacy for the protocol): pairwise coherence — agreement
  on the common subalgebra of each pair of contexts.
- **PR(𝓡)**: realisation of the window data by a member of a *declared*
  realisation class 𝓡 (all measures / stationary / supported on a subshift X /
  memory-m Markov …) — the observer's commitment lattice; X-support and
  stationarity are just grades.
- **Contextuality of a model** = EA without PR(𝓡).
- **Commensurability of a protocol** = EA ⟹ PR(𝓡) universally (Paper II's
  word, now doing classification work).
- Axes: two protocol axes (window layout = reporting; coarsening = compression)
  + one commitment axis (𝓡).

## 2. Claims, with verification status

### 2.1 Re-verified in THIS environment (2026-07-06, `commensurability_checks.py` — all pass)
1. **Minimal EA/PR separation** (3 outcomes, 2 contexts: "is it 3?" / "is it
   1?", both answered yes): common subalgebra trivial ⟹ EA vacuous;
   unrealisable. Lesson: pairwise EA is much cheaper than intuitive
   consistency — "conflict" intuitions smuggle in a realisation.
2. **First pairwise-complete separation at k=3** (contexts x₁, x₂, x₁⊕x₂ on
   {0,1}²): all three context pairs cell-complete (hence pairwise
   commensurable by the k=2 theorem), yet s(R₁)=s(C₁)=1, s(D₁)=0 is coherent
   with value 2 against realisable ceiling 1. Certificate = Fréchet–Bonferroni
   μ(R₁)+μ(C₁) ≤ 1+μ(R₁∩C₁) ≤ 1+μ(D₁), powered by incidence R₁∩C₁ ⊆ D₁ —
   "even the parity example is incidence in disguise."
3. **Wrap-4-cycle parity model** (edge contexts round C₄; eq/eq/eq/anti,
   uniform singles): pairwise coherent, EMPTY global support — unrealisable.
4. **Even/odd exclusivity cycles**: fractional packing C₄ = 2 = classical
   (even exclusivity cycles probabilistically inert); C₅ = 5/2 > 2 (odd cycles
   carry violation; KCBS/pentagon = the period-10 model's invariant). Even
   cycles matter only through the reporting axis.

### 2.2 Hand-derived, NOT yet machine-verified ⟦HAND — unverified⟧
- **k=2 theorem**: two coarse contexts on a common window are commensurable
  iff within each coherence block (connected component of the
  cell-intersection graph) every cell of one meets every cell of the other.
  Sufficiency: complete bipartite support makes the per-block transportation
  problem feasible for any equal-total margins. Necessity: an empty cell-pair
  inside a block supports the concentrated "it's here / it's there" model.
  Subsumes the two-window tame case (full-window contexts ⟹ blocks = shared
  coordinates' values, within which cylinder cells always intersect).
- **T1 architecture** (gapped full-window protocols): official acyclicity
  notion = database-theoretic α-acyclicity (GYO reduction) ≡ running
  intersection. Sufficiency = the gluing lemma. Necessity via two gadget
  families matched to the two failure modes: chordless cycles → the parity
  model (claim 3's gadget, generalized); conformality failures → odd-cycle
  anticorrelation models.
- **Axis-reduction theorem (TARGET, head of queue)**: the compression axis
  reduces to the reporting axis over a constrained alphabet — a coarse context
  is a full context on derived variables (rows = x₁, diagonals = x₁⊕x₂)
  satisfying functional constraints; so coarsening-contextuality = reporting-
  contextuality relative to the constraint variety, the same mechanism as
  X-support. If proved: taxonomy compresses to reporting acyclicity + an
  incidence axis (constraints, whether dynamical or compressive).
- ~~**Bonferroni normal-form conjecture**~~ **REFUTED as stated, 2026-07-06 —
  by our own pentagon; stratified replacement below.** Refutation re-verified
  in this environment (`pentagon_chain_immunity_check.py`, all four parts):
  the pentagon half-model (contexts = edge-pairs (x_j, x_{j+1}) of C₅ on
  {0,1}⁵; s(1,0)=s(0,1)=½, s(1,1)=s(0,0)=0) is EA, unrealisable, and satisfies
  EVERY pointwise-valid elementary chain certificate (11,272 in this
  environment's parameterization; 8,527 in the design session's — counts are
  parameterization-dependent, immunity is the invariant), while the stable-set
  bound Σ μ(a_j) ≤ α(C₅) = 2 detects it at 5/2.

### 2.2a The corrected structure (design session, 2026-07-06, second pass)
- **Empty-intersection lemma (unification)**: cells c₁…c_m from distinct
  contexts with ⋂ c_t = ∅ give the pointwise-valid Σ 1_{c_t} ≤ m−1, violated
  by the model concentrating on each c_t. The 3-outcome example, the k=2
  necessity gadget, the wrap-C₄ parity certificate, and the triangle/
  conformality gadget are all instances (m = 2, 4). Four atlas entries, ONE
  Lean lemma.
- **Stratified conjecture**:
  - **Family I (chains)** — Σ 1_{c_t} ≤ (m−1) + 1_E through incidence
    ⋂ c_t ⊆ E; subsumes exclusivity (E = ∅) and inclusion (m = 1). Complete
    for conformality/reporting-type obstructions; **provably complete at k=2**
    (the k=2 theorem = the base case of the stratification).
  - **Family II (stable-set facets)** — exclusivity-graph coverage bounds.
    Edge certificates suffice iff the cross-context exclusivity graph is
    bipartite (König); edges + cliques iff perfect (Lovász–Fulkerson–Chvátal);
    odd holes (pentagon minimal) demand odd-cycle inequalities and beyond —
    the Cabello–Severini–Winter hierarchy, Lovász perfect-graph theory behind
    it. Perfection is poly-time decidable (Chudnovsky–Cornuéjols–Liu–Seymour–
    Vušković), so this branch of the criterion is algorithmically real.
- **Two sharpenings from this side's re-verification (hand back to design):**
  (1) The pentagon half-model is *empty-support* unrealisable — its zero-set
  forces exactly-one-per-edge, impossible on the odd cycle — the same brute
  fact as the wrap-C₄ gadget; it evades chains not by realisability-type but
  because its mass is spread: every cell value ≤ ½, so no bound of the form
  m−1 can ever be violated. The chain/coverage split is a split in the
  BOUND'S ARITHMETIC (m−1 vs α < m−1), not in the unrealisability mechanism.
  (2) Family II certificates are not pointwise-valid on Ω (all-ones violates
  the odd-cycle inequality on {0,1}⁵); they are valid MODULO THE ZERO-SET
  (support restriction). So the stratification is also a stratification of
  validity modes — Family I pointwise on Ω, Family II conditional on the
  constraint variety — which is the same mechanism the axis-reduction theorem
  identifies (frustration migrating into the variety).
- **Axis-reduction, sharpened by the RCD case**: reduced to derived variables
  (u = x₁, v = x₂, w = u⊕v) the reporting hypergraph is three disjoint
  singletons — acyclic — so with constraint varieties, acyclicity no longer
  suffices; after reduction the classification is a marginal problem over a
  constraint language — CSP-dichotomy shape (Bulatov–Zhuk flavor; DIRECTION,
  not claim).
- **Complexity floor (honesty)**: Pitowsky — correlation-polytope membership
  is NP-complete, so no finite certificate normal form exists at the MODEL
  level; the classification target stays at the protocol level (the ∀∃
  question), where structure like perfection can still give clean criteria.
- ~~**Open design question**: is Family I ∪ Family II complete...~~
  **ANSWERED BY THE HARNESS (2026-07-06 evening): NO — twice over. See §2.2b.**

### 2.2b Harness results (exhaustive, exact-rational; `commensurability_harness.py`)

**Prediction-ledger outcomes** (all predictions logged pre-run):
- **P1 (ELSE empty at ≤6): REFUTED TWICE.**
  (a) n=4, k=3: three protocols whose witnesses evade all inequalities of both
  families but violate **affine incidence syzygies** — pointwise integer
  IDENTITIES among overlapping cells (e.g. −1₍₀₎+1₍₁₎+1₍₀₂₎+1₍₀₃₎ ≡ 1 on N) =
  R's hull equations. Named **Family 0**; pure linear algebra; with it, n ≤ 4
  is fully complete.
  (b) n=5, k=3: two protocols beyond even Family 0+I+II. Hand-verified record
  (`else_n5_verification.py`, all four parts pass): protocol
  {0|1|234}, {0|12|34}, {0|13|24}, witness q = (½,0,½|½,½,0|½,½,0) —
  EA-coherent, unrealisable, immune to ALL chains, cliques, odd-holes AND
  syzygies; detected by the **weighted pointwise inequality**
  q(B₁₂)+q(C₁₃) ≤ 2·q(A₁)+q(A₂₃₄) (coefficient 2, mixed signs — the
  I3322-flavor weighted class predicted at 7–8 outcomes arrives at n=5).
  **Fourth mechanism.**
- **P2 (minimal Family-II at 5–6 outcomes): REFUTED** — cliques bite at
  n=3, k=3 already (cross-context triangle of singletons: Σ ≤ 1 vs chains'
  best Σ ≤ 2; witness = ½-spread, majority-commitment lemma in action). The
  5–6 estimate conflated "Family II needed" with "odd-hole needed."
- **k=2 certificate-completeness correction**: "Family I complete at k=2"
  FAILS as a certificate claim — n=5, k=2 protocols need cliques with TWO
  cells from one context (chains take one cell per context and cannot see
  them). The protocol-level k=2 iff-theorem (blocks complete-bipartite) is
  untouched.
- **P3**: the weighted class arrived at n=5, not 7–8.
- **Odd-holes: NOT yet needed anywhere** (all of k=2 incl. n=6; n≤4 k=3;
  n=5 k=3 partial). The C₅-gap may still need larger n — or cliques may
  dominate at all small scales.

**Atlas so far** (exact; JSONL files): n=3: 4 protocols (1 clique-needing);
n=4: 46 (6 cliques, 3 syzygies); n=5 k=2: 41 (2 cliques); n=6 k=2: 146
(17 cliques, 72 Family-I, 57 R=C); n=5 k=3 partial at interruption of record:
82 Family-I / 29 syzygy / 27 cliques / 2 ELSE-weighted. n=5 k=3 and n=6 k=3
runs continuing (tracked watcher).

### 2.2c Final ≤6 atlas + reclassifications + v2 calibrations (2026-07-07)

**Final sweep results** (n=6 k=3 DESCOPED — projected 40–160 h, not "cheap";
rerun later optimized if the trichotomy needs the datum):
- n=5 k=3 COMPLETE: 339 canonical protocols — 92 R=C / 135 Family-I /
  54 cliques / **2 NEED_ODDHOLES (first sightings — the pentagon in
  coarse-partition costume: {0|12|34},{01|2|34},{03|1|24}; minimal
  odd-hole-needing protocol = n=5, k=3, vindicating the design session's
  quantitative instinct for the odd-hole reading of P2)** / 48 syzygies /
  8 ELSE-weighted (ALL witnesses ½-spread — majority-commitment corroborated
  at every instance).
- Totals ≤6 (k=2 complete everywhere; k=3 complete to n=5): all five
  mechanisms sighted, none beyond.

**Structural reclassifications (design session, endorsed after verification):**
1. **Multiset-domination is universally true, hence contentless** — these are
   0/1 polytopes; every facet has an integer normal, splits by sign, constants
   absorb via context sums (each context sums to 1 pointwise). Two lines. The
   content relocates to the QUANTITATIVE half.
2. **Family 0 reclassified: syzygies are the gauge group**, not a certificate
   family — the lattice of pointwise identities (hull equations + context
   sums) to quotient by before weight is defined. Invariants: w(facet) =
   min ‖λ‖∞ over integer representatives mod gauge; w(protocol) = max over
   facets. Taxonomy = weight spectrum + shape labels per weight.
3. **Protocol-level vs model-level completeness must be tagged everywhere.**
   Reconciliation of the k=2 "contradiction": edges are protocol-complete at
   k=2 (the k=2 theorem — incommensurable ⟹ some edge violated by SOME
   model) but model-incomplete (the ½-spread clique witness). Harness
   verdicts are MODEL-level. Classification needs protocol-level; the CF
   diagnostic needs model-level.

**The trichotomy (the corrected big picture):** k=2 — weight-1,
protocol-complete (the theorem). k=3, full product support, coordinate
contexts — always commensurable (product measure; two lines). k=3 with a
variety — UNIVERSAL: De Loera–Onn (every rational polytope is a face of a
3-way transportation polytope; faces = punctures), so no weight bound, model
membership NP-complete (Pitowsky floor hit at three contexts), no finite facet
taxonomy. All hardness lives in the variety, where the axis-reduction said.
Shelf additions: Avis–Imai–Ito–Sasaki covariance map (bipartite Bell ≅ cut
polytopes — mixed-weight facets are EXPECTED early arrivals), De Loera–Onn
universality. **Successor question (next design turn): the dichotomy hunt —
which constraint languages (dynamics, compressions) generate tame protocol
families vs universality; anchors: interval cylinder varieties = tame (the
tame theorem) vs DLO punctures = universal; first open case: golden-mean SFT.**

**v2 calibrations (`harness_v2_calibrations.py`):**
- (c) 2×2×2 coordinate protocol → R_EQUALS_C ✓ (product-measure anchor PASS).
- (d) cube-minus-2 punctures (all 3 Hamming classes, n=6): ALL
  FAMILY_I_COMPLETE, gauge-weight LB = 1 — **prediction "weight ≥ 3 at
  reachable scale" NOT confirmed at this scale** (logged as a miss; minimal
  weight-3 lives beyond 6-point punctured cubes — larger grids presumably
  needed for the DLO mechanism to bite).
- The n=5 fourth-mechanism facet **gauge-reduces to weight-LB 1**: the
  "weighted" mechanism is not high-weight mod gauge — it is a weight-1 facet
  whose SHAPE (multiple negatives across contexts) escapes chains ∪ cliques ∪
  holes. Weight alone does not separate the fourth mechanism; shape labels
  are load-bearing. (Caveat: LP relaxation = lower bound only; integrality of
  minimizers not yet certified — v2.1 item.)

### 2.2d P4–P6 (polymorphism transfer) — DELTA AUTOPSY, 2026-07-07
Pre-registered predictions run exactly (`golden_mean_tests.py`):
- **P4 MISS**: golden-mean length-3 variety + coordinate contexts is
  INcommensurable (FAMILY_I_COMPLETE). Autopsy: {x₁=1} and {x₂=1} are disjoint
  ON THE VARIETY, so the concentrated model q(x₁=1)=q(x₂=1)=1 is EA-coherent
  (bipartitions → trivial common subalgebras → single block) yet unrealisable.
- **P6 MISS, uniformly** (all 20 monotone AND/OR triples on the full cube):
  same mechanism — derived-variable bipartitions freely produce disjoint
  cross-context cells; pairwise EA has no channel.
- **P5 "PASS" downgraded to VACUOUS**: incommensurable as predicted, but by
  the same trivial exclusivity mechanism as the misses, not by the XOR/
  polymorphism mechanism. Not evidence for the conjecture; retest under the
  corrected formulation.
**The autopsy is decisive and uniform: partition-vs-scope is THE breaking
delta** (the other declared delta, realisability-vs-optimization, was never
reached — the structure side collapsed first). The transfer conjecture as
formulated is dead; the reformulation target is precise: the protocol must
include the SCOPE contexts (full joint partitions over supports, plausibly
including Γ's constraint scopes), so that EA aligns with BLP local
consistency — with scope/interval contexts included, the golden-mean case is
the tame theorem's regime (running intersection) and commensurability should
return. Corrective rule adopted alongside (design side, P3 diagnosis): every
prediction gets a **scale-sanity pass** (does the mechanism have combinatorial
room at this n?); shape is the primary taxonomy key, weight the secondary
curve; weight certification = pair (exhibited integer representative, exact
rational dual LB) — never certify LP-minimizer integrality.
Shelf additions (derive-then-compare): Feder–Vardi width-1, Dalmau–Pearson set
polymorphisms, Barto–Kozik bounded width (nearest prior statement of the
question), Thapper–Živný + Kolmogorov–Krokhin–Rolínek, Grohe.

### 2.2e Scope-context reformulation round (2026-07-07, second design pass)
- **Free theorem (acyclic ⟹ commensurable for EVERY language)**: with scope
  contexts included, each p_S is supported on its relation; RIP conditional-
  product glue lands inside V with no condition on Γ. The tame theorem's true
  generality; the language is silent on trees. P4′ (golden-mean path, pair
  windows) = instance, machine-PASS (`ring_parity_tests.py`). Lean: existing
  gluing lemma + one line of support tracking. Derive-then-compare vs
  Wainwright–Jordan tree-exactness (expect folklore-adjacent for the full
  language; the all-Γ variety-supported form is the claim).
- **Pre-emptive kill (the ledger's first)**: transfer-v2-as-KOTYZ killed BY
  HAND BEFORE registration. Separating object: golden-mean NAND on C₅ — the
  ½-(01)/½-(10) edge model is scope-coherent, unrealisable (2-coloring of an
  odd cycle), yet golden-mean has min ⟹ symmetric polymorphisms of every
  arity ⟹ BLP decides satisfiability (KOTYZ). **The commensurability line
  sits strictly above the satisfiability-width line**; deciding emptiness ≠
  projecting polytopes. KOTYZ + Barto–Kozik reclassified: satisfiability-
  level, provably below our line. Wainwright–Jordan enters as vocabulary
  (local/marginal polytope).
- **Ring-parity verdicts, exact (`ring_commensurability.py`; tooling note —
  at k ≥ 4 use the separation-only test: the family ladder's LPs carry the
  whole chain family as rows and blow up):** C₃ INCOMMENSURABLE (facet gap ½;
  correct counting certificate: legal configs carry ≤ α(C₃)=1 one vs model
  E[#1s]=3/2 — the design paste's "≥2 on triangle-legal" had the inequality
  inverted, conclusion unchanged), C₅ INCOMMENSURABLE (gap ¼), **P7: C₄
  COMMENSURABLE** (C=R, 8 facets + 8 hull eqs exact), **P8: C₆ COMMENSURABLE**
  (C=R, 12 facets + 12 hull eqs exact). **Parity clean at L=3..6; the P8 gate
  FIRES — parity-theorem proof attempt warranted next design turn**
  (transfer-matrix gluing around even rings the likely mechanism).
- **Safe-topology map** (the reformulated classification): acyclicity settles
  everything language-independently, so Γ enters only through cyclic
  structures; the object is Γ ↦ {cycle structures where local = marginal}.
  Candidate theorem: golden-mean's safe topologies are exactly the bipartite
  ones. Dynamical reading (closing the oldest loop): cyclic scope structure =
  recurrence — sliding pair-windows on a period-L orbit identify time mod L —
  so **golden-mean dynamics produces contextual scope data precisely on
  odd-period orbits**; frustration needs cyclic time; on ℤ-intervals every
  world is tame.
- **Q-comp split (permanent)**: scope-inclusion trivializes single-window
  compression wildness (a full joint realises its own coarsenings — RCD
  becomes commensurable once the 2×2 joint is reported). Compressions matter
  exactly when full joints are NOT reportable (bandwidth-limited,
  aggregation-native observation) — that programme keeps the ≤6 atlas as its
  evidence base; first-order target: **witnessed exclusivity** (commensurable
  ⟹ every cross-context exclusive cell-pair separated by a common-subalgebra
  event; concentrated model = the universal violator). Two questions, two
  programmes, one atlas each; conflating them was v1's error.

### 2.2f Parity theorem PROVED + P9–P12 all HIT (2026-07-07, third design pass)
**Theorem (golden-mean ring parity)**: C_L commensurable ⟺ L even. ⟦HAND —
machine-corroborated on every checkable joint (`parity_theorem_checks.py`)⟧:
- **Reduction lemma** (C ≅ FSTAB(C_L), R ≅ STAB(C_L) in vertex-marginal
  coordinates): **P11 EXACT** — the harness's own EA system has rank exactly
  15−5=10 at L=5 and the affine lift q(u) satisfies it identically; EA sees
  precisely the shared events the lemma claims, no more.
- **Parity mechanism**: det(incidence C_L) = 1−(−1)^L verified L=3..8; every
  proper square submatrix forest-TU (det ∈ {−1,0,1}) verified L=3..7. Even ⟹
  TU ⟹ integral vertices ⟹ commensurable (transfer-matrix glue survives as
  the sampling remark). Odd ⟹ unique fractional vertex u ≡ ½: **P12 PASS**
  (FSTAB(C₅) = 11 integral + 1 fractional, exactly; likewise 4+1 at L=3;
  all-integral at L=4 (7) and L=6 (18)). The EA/PR gap on an odd golden-mean
  ring is A SINGLE POINT.
- **Corollaries matching measured data**: separating facet = odd-cycle
  Σu ≤ (L−1)/2 with relative violation 1/(L−1) — the measured gaps ½ (C₃) and
  ¼ (C₅) are its fingerprint. Half-model has **CF = 1** (support argument
  machine-checked: no legal config dominates exactly-one-per-edge) — the
  golden-mean ring's PR-box. Obstruction-zoo unification: same STAB odd-cycle
  shape as the pentagon's coverage bound — compression (Q-comp) and
  recurrence reach the SAME polyhedral obstruction by different observational
  routes; the classification tracks which protocols reach which exhibits.
- **Dynamical reading, now a theorem**: golden-mean dynamics yields contextual
  scope data exactly on odd-period recurrence — alternation cannot close an
  odd ring, observed.
**v3 landscape (safe-topology spectrum over binary languages)**: {≤}: ALL
rings safe (**P10 PASS**, L=3..6 exact; graded on the V-induced cell
structure — the empty (0,1) cell is not reportable; relation-level derivation
agrees here); NAND: even only (the theorem); XOR: even safe (**P9 PASS**,
L=4,6; odd = degenerate, empty variety — reported not scored); full: none
(wrap-C₄/AQBCC). More constraint can mean MORE tame. **Next design turn: the
safe-topology invariant** (circular-chromatic / cohomological flavor — what
algebraic invariant of ρ reads off the safe-length profile).
Shelf: Hoffman–Kruskal/König (TU step — expect full overlap, ours is the
3-line special case), Chvátal t-perfection (carries the complete odd-ring
facet description; we need only the single facet), AQBCC (full-language
cycles). C₃ counting-certificate correction acknowledged design-side.
**Lean ladder, proof's load-bearing joints in order**: (1) common-subalgebra/
reduction lemma, (2) forest-TU, (3) unique-fractional-vertex.

### 2.2g Winding/circulation round — P13 MISSES informatively, necklace criterion survives everything (2026-07-07/08)
Run: `winding_invariant_tests.py` (circulation-level, certified per-language by
the RANK GATE = EA rowspace ≡ conservation rowspace, PASS everywhere run;
harness cross-checks at small L all agree).
- **P13 MISS ×2 (the decisive one, and the miss is the finding)**: ternary
  3-cycle+loop-at-0; predicted Safe = 3ℤ; observed **Safe = {3}** (L=4..9 all
  unsafe; L=6,9 contradict the prediction; L=6 confirmed at protocol level by
  the full harness, gap ½). Autopsy: the L=6 frustrating object is the
  uniform circulation on the **primitive period-4 orbit `0120`** (3-cycle
  once + loop once), closing only after 2 wraps since 4 ∤ 6 — a
  **NON-CONSTANT necklace**, already covered by the design side's own
  backward theorem. The prediction considered only constant necklaces
  (sub-digraph gcd/Perron–Frobenius period); but ρ is APERIODIC (cycle
  lengths {1,3}, gcd 1) and still frustrates almost everywhere. **Spectral
  aperiodicity of sub-dynamics ≠ tameness**; the obstruction generators are
  the PRIMITIVE PERIODIC ORBITS (the numerical semigroup of orbit periods
  interacting with L through winding of simple layered cycles, capped at
  |A|). L=3 is safe because no winding-≥2 SIMPLE layered cycle exists at all
  there (a period-p orbit needs winding p/gcd(p,L) ≤ |A| and no state
  collisions).
- **Necklace criterion: 100% consistent on ALL data.** Completeness check at
  L=3..9: necklace-exists ⟺ unsafe at every L; moreover every winding-≥2
  simple cycle in the ρ₁₃ data is section-free-supported. Together with NAND
  (P14: L=8,10 safe with ZERO winding-≥2 cycles; P15: exhaustive — 0
  necklaces among 7^L assignments at even L=4,6,8, positive controls at odd
  L fire) and P16 (974 uniform ternary instances, 0 hits: no bad vertex with
  section-carrying support anywhere), the standing of the two conjecture
  halves: **backward (necklace ⟹ unsafe) = theorem; forward (unsafe ⟹
  necklace) = unrefuted by everything computed, proof attempt LICENSED** —
  and every incommensurable instance so far is STRONGLY contextual
  (section-free support), so the P16 separation phenomenon remains unseen.
- **P14 HIT** (NAND safe L=8,10, rank gates pass), **P15 HIT** (with
  controls), **P16 MISS-as-registered** (licensing).
- **Corrected invariant target for the next design turn**: not sub-digraph
  period — the safe-length profile is governed by the primitive-orbit period
  spectrum through the simple-winding mechanism, with the polyhedral hull
  condition still the exact statement. Observed profiles: {≤}: all; equality:
  all; NAND: even; XOR: even (odd degenerate); ρ₁₃ (aperiodic!): {3}; full:
  none. The dynamical sentence stands and sharpens: contextual data from a
  recurrent world = observations living on a hidden k-fold cover of the
  observed clock, and the covers that bite are those of primitive orbits
  whose period does not divide the clock.

### 2.2h Winding characterization — PREDICTIVE; P17–P20 all HIT; the semantics bifurcation (2026-07-08)
Run: `winding_theorem_checks.py`. The theorem's corroborations and its first
fresh-prediction validation:
- **P17 HIT (Lemma 1 + gate)**: exact vertex enumeration of the EA polytope C
  (cell coordinates, zero-set method) equals the set of normalized simple
  layered cycles EXACTLY — NAND L=5 (12=12), ρ₁₃ L=4 (6=6), full-binary L=3
  (12=12), XOR L=4 (2=2). Set identity, not just counts.
- **P18 HIT**: Safe(ρ₁₃) recomputed purely from the primitive-orbit criterion
  (winding k = q/gcd(q,L) ≥ 2 + injective wrap) = {3} across L=3..9,
  matching the polytopes. The L=9 witness is an 18-period primitive orbit
  (001200120120012012) — composite necklaces get intricate, the criterion
  tracks them.
- **P19 HIT**: all 8 winding-2 simple cycles of the full language at L=4 are
  anti-periodic (w_{i+4} = 1−w_i) — the binary corollary corroborated.
- **P20 HIT — THE THEOREM IS NOW PREDICTIVE**: ρ₂₀ = disjoint 2-cycle ⊕
  3-cycle; predicted Safe = 6ℤ before harness contact; computed
  Safe_circ(ρ₂₀) = {6, 12} on L=2..12 (odd-coprime L degenerate-unsafe, as
  the criterion says). First non-parity, non-postdicted profile.
- **P20b — the honesty-ledger caveat, exhibited and CHARACTERIZED (the
  substantive hand-back):** ρ₂₀'s transfer digraph is disconnected, and at
  L=2,3,4 the rank gate FAILS (a component whose period ∤ L has ALL its arcs
  V-unrealized — they lie on no section, so they are not EA cells). There
  the two objects genuinely diverge: **EA-on-V is COMMENSURABLE at every
  tested L (2,3,4,6)** while the circulation object is unsafe off 6ℤ. Both
  semantics are meaningful and answer different observational questions:
  **closure-level** (the world closes on the clock; only V-realized events
  are reportable; invisible strands cannot frustrate data) vs
  **aggregation-level** (data = pair frequencies aggregated from a possibly
  hidden cover; relation-level cells are observable even when no single
  mod-L configuration exists — the covering story taken seriously). The gate
  is exactly the boundary: gate-pass ⟹ the semantics coincide and the
  theorem speaks unconditionally; gate-fail ⟹ the application must DECLARE
  which observation model it means. For the reconstruction programme this is
  a design decision, not a nuisance: aggregated multi-run data lives at the
  aggregation level; single-trajectory windowed data at the closure level.
- Gate-failure mode now characterized: EA cells = arcs on winding-1 cycles;
  circulation arcs = arcs on ANY cycle; they differ iff some arc lies only
  on winding-≥2 cycles — possible only when sections are locally absent
  (disconnected/period-forcing languages), the caveat's precise content.
Ledger after this round: **13 hits / 7 informative misses / 1 vacuous / 2
dead conjectures / 1 pre-emptive kill.** Next design turn (per the paste):
the covering-space statement of the proof (Gross–Tucker voltage framing) and
the Lean ladder — gate lemma, Lemma 1 (flow decomposition), Lemma 2
(functional-digraph two-liner, the load-bearing novelty), mixture-support
step, assembly.

### 2.2i Junctions round — P21/P22/P23/P24 all HIT; junctions innocent; reduction identity machine-confirmed (2026-07-08)
Run: `junction_tests.py`. The Lean pack (gate lemma / Lemma 1 / Lemma 2 /
mixture-support / assembly + the decidable-orbit-criterion suggestion) is
recorded for the user's Lean side; verification results:
- **The junction gate-analogue PASSES at all three structures** (rank exactly
  #cells − #vertices, NAND edge-affine lift identical) — declared failure
  mode (b) did not occur; C = FSTAB(G) beyond rings at these instances. The
  figure-eight diagonal-cycle death (hand analysis: junction coherence kills
  the winding-(1,1) object) is implicit in the geometry: no such vertex
  exists in FSTAB.
- **P21 HIT**: fig8(4,4) — zero fractional FSTAB vertices → SAFE.
- **P22 HIT**: fig8(3,4) — 8 fractional vertices, ALL outside STAB → UNSAFE;
  inherited triangle-facet gap exactly ½; full-harness protocol-level
  cross-check agrees (INCOMMENSURABLE, gap ½, n=17).
- **P24 HIT (the least-confident call)**: theta(2,2,2) = K₂,₃ — zero
  fractional vertices → SAFE; harness cross-check agrees (n=11).
  **Path-sharing junctions created no new frustration at this scale**: the
  world is "interlocking recurrences compose their safety" — wedge-innocence
  supported, holonomy interaction NOT a third mechanism here, the
  classification stays spectral/intersection on unicyclic-glued structure
  (as far as tested; theta at larger even girth and ring-plus-chord remain
  the design side's stress continuations).
- **P23 HIT — the bifurcation is a reduction, machine-confirmed**:
  Safe_closure(ρ₂₀, L) = Safe(ρ₂₀|_{V(L)}, L) HOLDS at every L = 2..12
  (restriction deletes the invisible component off 6ℤ; degenerate L
  trivially equal). One theorem, two semantics, an L-dependent language
  restriction between them.
**Ledger: 17 hits / 7 informative misses / 1 vacuous / 2 dead conjectures /
1 pre-emptive kill.**

### 2.2j K₄-minor experiment + lifting controls — P25/P26/P27 all HIT (2026-07-08)
Run: `k4_and_lifting_tests.py`. Wainwright–Jordan/Padberg reveal recorded
(novelty ledger for the graph theory: language/variety refinement + orbit
criterion + dynamical reading = OURS; full-support polyhedral frame =
Padberg–Barahona–Seymour; binary half-integrality retro-explains every
half-model witness and P16's alphabet-3 need).
- **P25 HIT — SAFE branch, and the gate holds at a K₄ minor**: even-subdivided
  K₄ (NAND): gate PASSES (rank 26 exact, lift identical), zero fractional
  FSTAB vertices. **The language refinement tames the minor obstruction.**
  Mechanism identified (this side, pre-stated before the run): for NAND,
  evenizing every circuit ⟺ bipartitizing the graph, and bipartite FSTAB is
  integral REGARDLESS of minors — so NAND cannot distinguish Circuit
  Localization from minor theory. **Sharpened follow-up (P25′, design-side
  choice): a language whose safe-circuit condition ≠ bipartiteness — e.g.
  ρ₂₀-beads on K₄ with every edge subdivided to length 6 (all circuits 18,
  24 ∈ 6ℤ = Safe(ρ₂₀), every circuit safe, K₄ minor retained, alphabet 5
  breaks half-integrality). That is where the two theories genuinely part
  ways; NAND could not take us there.**
- **P26 HIT**: theta(3,3,2): gate passes; 7 fractional vertices, all outside
  STAB; 5-circuit odd-cycle gap exactly ½. The lifting lemma works in the
  path-sharing regime.
- **P27 HIT — totality necessity, matched pair**: standalone C₃-NAND unsafe
  (gap ½); dead-end tail {(1,1)} → the half-model cannot lift, G safe (V
  collapses to one config) — intersection formula FAILS without totality;
  equality (total) tail → inheritance restored (gap ½). The lemma's
  hypothesis is necessary and sufficient at the control.
**Ledger: 20 hits / 7 informative misses / 1 vacuous / 2 dead conjectures /
1 pre-emptive kill.** Circuit Localization stands unrefuted with its
inheritance direction controlled both ways; the decisive composition-side
test is P25′.

### 2.2k P25′/P28 + the third taming — the fork remains unreached; NE3 ruled out (2026-07-08)
Run: `p25prime_tests.py`. Lifting-lemma proof (with the interface clause) and
fork-preparation recorded from the design side; results:
- **P25′ HIT — but the fork is unreached for a THIRD structural reason.**
  Machine-checked pre-run finding: **ρ₂₀ is the permutation (01)(234)** —
  deterministic, every state exactly one continuation. For permutation beads,
  LOCAL(G) collapses to the **holonomy-invariant simplex** {u : π^c u = u ∀
  cycle classes} and MARG = conv(fixed states) — so aggregation-level Safe ⟺
  holonomy group H = {id}, and the K₄ minor NEVER VOTES. At all-lengths-6:
  cycle sums (6,6,6) ⟹ H = id ⟹ SAFE (aggregation); closure level: |V| = 5
  and every edge context separates all 5 ⟹ EA = full agreement ⟹ C = Δ(V)
  = R ⟹ SAFE. The covering-space frame is LITERAL for permutation
  languages: safety = trivial holonomy.
- **P28 HIT, mode-corrected**: one path at length 5 ⟹ cycle sums {0,5} ⟹
  H = ⟨π⁵⟩ = ⟨π⟩, orbits {0,1},{2,3,4}, NO fixed states ⟹ MARG = ∅,
  LOCAL = a 1-dim invariant segment ⟹ UNSAFE — but in the DEGENERATE mode:
  the inherited circuits (ρ₂₀-rings L=17, 23) are variety-empty, so the
  certificate is section-emptiness/CF=1, not the registered ½-type facet
  gap (which cannot arise: ρ₂₀'s unsafe rings have no sections to gap
  against). Inheritance direction confirmed; digit inapplicable.
- **Round-3 scout: NE3 (proper 3-coloring, nondeterministic, dense) RULED
  OUT** — aggregation-UNSAFE at every L = 3..7, with EVERY winding-≥2 vertex
  outside conv(sections) (27/34/175/342/1307 bad). Bonus gate datum: at L=3
  the gate fails in the OPPOSITE direction from ρ₂₀'s (EA ⊋ circulation —
  the triangle variety is RIGID: every edge pair determines the third
  vertex, so contexts are discrete partitions); passes at L=4,5.
- **The taming synthesis (hand back):** three candidate fork experiments,
  three structural tamings — NAND (evenize ⟺ bipartitize ⟹ FSTAB
  integral), ρ₂₀ (determinism ⟹ holonomy simplex), NE3 (no safe lengths at
  all). The fork needs a language that is simultaneously (i)
  nondeterministic, (ii) nonempty aggregation-safe set, (iii) safe-condition
  not integrality-forcing. **Design question with theorem potential: does
  such a language exist — or does branching force the safe set thin (ρ₁₃:
  {3}) / empty (NE3), while rich safe sets force determinism-or-parity, so
  that Circuit Localization is TRUE because its hypotheses can never put a
  minor in play?** The repeated "structural taming" may BE the
  decomposition theorem's mechanism, discovered experiment-first.
**Ledger: 22 hits (P25′, P28 mode-corrected) / 7 informative misses / 1
vacuous / 2 dead conjectures / 1 pre-emptive kill.**

### 2.2l P29/P30 — criterion validated; the hunt executed; the fork narrows to ONE candidate (2026-07-08/09)
Run: `swap_spectrum_scan.py` + triage (`commensurability_fork_candidates.json`,
`commensurability_fork_survivors.json`).
- **P29 HIT**: the swap/tuple shift-reachability criterion (theorem-let A,
  polytope-free) reproduces ALL seven recorded profiles exactly (NAND evens,
  ρ₁₃ {3}, ρ₂₀ 6ℤ, FULL2 none, implication/equality all, NE3 none).
  Theorem-let B corroborated within the L ≤ 40 window (every unsafe set
  eventually periodic; note: my period detector has a window-edge artifact —
  ρ₂₀ reported "period 1 from 37" where the true period 6 is visible in the
  set; detector, not criterion).
- **P30 executed — the impossibility scenario is dead, and the cascade is
  the finding.** Exhaustive ≤4 states (canonical, total, branching, q ≤ 6)
  + minimally-branching 5-state slice: 333 genuine pre-candidates at ≤4.
  Filter cascade:
  (1) "3q,4q-safe" is NECESSARY NOT SUFFICIENT — NAND itself passes at q=2;
  (2) **taming #5 discovered: TRANSIENT BRANCHING** — 149/333 have all
  branching off the recurrent core (deterministic recurrent part ⟹ holonomy
  taming with decoration; closed walks never see the branch);
  (3) 184 survivors with RECURRENT branching, and their q-parity is stark:
  **181 even-q only (2,4,6) + 2 even-q sparse (4) + exactly ONE odd-q — and
  that one is the design side's own taming-#4 exemplar** (0→1, 1→{2,3},
  2→0, 3→0: two 3-cycles sharing a path, graded over ℤ₃, singleton fibers
  {0},{1} — forced-cut factorization predicted).
- **The fork narrows to one registrable object**: ρ* = {(0,0),(0,2),(1,1),
  (2,0)} — loops at 0,1 + 2-cycle 0↔2; recurrent branching at 0; Safe =
  evens BUT the parity comes from the swap dynamics, NOT base bipartiteness
  (the base has odd cycles — loops); not deterministic, not graded (gcd 1),
  not transient. **No known taming obviously applies.** The experiment:
  ρ* on K₄ all-edges-subdivided-to-2 (10 vertices, 12 edges, alphabet 3;
  circuits 6, 8 ∈ Safe). Circuit Localization predicts safe; whether the K₄
  minor finally bites is genuinely open — awaiting design-side registration
  (P31), with the theta-digraph at q=3 as the taming-#4 machine-confirmation
  control (P32 suggestion).
- Candidate theorem-let C (from the parity starkness, design side to
  formalize or refute): recurrent branching forces unsafety at odd lengths
  (all odd-q survivors at ≤4 states are graded); if true, the fork lives
  only in even-q parity-family languages, and the decomposition theorem's
  remaining case is exactly "even-q safety without bipartite base."
**Ledger: 23 hits / 7 informative misses / 1 vacuous / 2 dead conjectures /
1 pre-emptive kill; P30 fulfilled-as-registered (ranked list, non-empty).**

### 2.2m P31/P32/P33 — taming #6, the control confirmed, and the filter-limit theorem-shaped lesson (2026-07-09)
Run: `p31_p32_round.py`.
- **Mis-triage caught pre-run (mine, on the record): ρ* is DISCONNECTED as a
  relation digraph** ({0,2} ⊔ {1}); on connected G the 1-sector mass is
  globally constant, so ρ* = NAND(0,2) ⊕ point — its "novel" swap-parity is
  NAND's own. **Taming #6: direct-sum decomposition** (machine-checked:
  sector separation on path-3): Safe(ρ₁⊕ρ₂) reduces componentwise; the
  earlier "connected" triage field existed but the survivor pass never
  applied it.
- **P31 HIT as registered** (prediction safe — correct), decided by the
  decomposition lemma + the STORED P25 verdict (NAND on even-subdivided K₄:
  gate PASS, zero fractional vertices). Not the fork; the exchange-graded
  reading of ρ* dissolves — its pair-cycle IS NAND's, relabeled.
  (Theorem-let D unaffected as arithmetic; its "level-one autonomy" witness
  needs a CONNECTED example or it stays unwitnessed.)
- **P32 HIT — taming #4 machine-confirmed on K₄, with the mechanism as an
  observable**: theta-digraph at q=3: |V| = 144 = 64+64+16 exactly as the
  three phase sectors predict; **dim C = dim R = 18 = 2 (sector mixing) +
  6+6+4 (free binary choices)** — the rank drop is visible in the harness
  output, not just the verdict; 20/20 exact random-direction LPs give
  max_C = max_R (full facet pass infeasible at n=144 — scope declared; the
  hand factorization argument covers it).
- **P33 corrected**: with connectivity + decomposition + recurrent-
  connectivity filters, **13 TRUE candidates** remain
  (`commensurability_fork_final.json`) — and the list is its own lesson:
  **NAND itself is the minimal entry.** Structural digraph filters CANNOT
  decide fork-capability: the tamings are polytope-level facts about the
  DERIVED constraint structure, not digraph-level facts about ρ. The
  genuinely open object is the first candidate with no known reduction:
  **ρ₅ = {(0,1),(0,2),(1,0),(1,1),(2,0)}** (3 states, connected, recurrent
  branching at 0 AND 1, loop ⟹ aperiodic base, Safe = evens, qs = 2,4,6) —
  awaiting design-side hand-analysis (NAND-reduction hunt) or cold
  registration of its q=2-subdivided-K₄ test.
**Ledger: 25 hits / 7 informative misses / 1 vacuous / 2 dead conjectures /
1 pre-emptive kill / 1 recorded mis-triage (corrected same-day).**

### 2.2n P34/P35 — the decisive round: ρ₅ holds at the K₅ boundary; taming-#7 proof licensed; fork hunt CLOSED (2026-07-09)
Run: `rho5_k4_k5_tests.py`. Mode-switch policy in force (fork registrations
frozen after this round).
- **ρ₅ hand-facts all machine-verified**: pair digraph = 6 off-diagonal
  pairs / 12 arcs, BIPARTITE with swap-pairs in opposite classes; triple
  dynamics = 3 two-cycles, no rotations (winding-3 empty); entropy
  λ ≈ 1.801938 with λ³ = λ² + 2λ − 1 exactly (≠ φ: not NAND in costume).
  **Level-one autonomy has its witness**: the bipartiteness lives natively
  in the pair dynamics over an aperiodic, odd-cycled base.
- **P34 HIT**: 2-subdivided K₄: |V| = 265, gate PASS, dim C = dim R = 20,
  120/120 exact LP directions agree — safe at sampling grade.
- **P35 HIT — THE decisive one**: 2-subdivided K₅ (15 vertices, 20 edges,
  |V| = 3434): **gate PASSES at the K₅ minor**, dim C = dim R = 30, 200/200
  exact rational LP directions (all 100 coordinates + 100 random) give
  max_C = max_R. For the first time in five fork attempts the minor had
  genuine room — bipartite target, Barahona–Mahjoub boundary, NO stable-set
  integrality theorem behind ρ₅ — and safety held. Scope declared: sampling
  grade (facet pass infeasible at n = 3434); certification path = the
  taming-#7 proof.
- **Consequences per the pre-declared policy**: fork-candidate registrations
  FROZEN. The design lane pivots to proving **taming #7: pair-bipartite
  languages are safe on all bipartite graphs** (attack: mod-2 potential on
  the pair-lifted constraint matrix, TU-flavored, ring forest argument as
  base case). If it closes, combined with the scan classification, **Circuit
  Localization follows for every branching language at small scale — the
  theorem assembled out of the six tamings**, which is what the pattern was
  saying all week. Lean queue: Lemma 2, then taming #7.
**Ledger: 27 hits / 7 informative misses / 1 vacuous / 2 dead conjectures /
1 pre-emptive kill / 1 corrected mis-triage.**

### 2.2o Taming #7 PROVED — every joint machine-verified; θ-sweep certifies P35; P36 splits the hypothesis (2026-07-10)
Run: `taming7_verification.py`. Taming #7 is now a theorem (design side), with
this side confirming each load-bearing joint exactly.
- **The retroactive datum (this side's harness had been reporting it)**: P34
  dim C = 20 = 2·10, P35 dim C = 30 = 2·15 — ρ₅ is MARGINAL-DETERMINED (five
  cells affine in endpoint marginals, kernel zero), two free coords/vertex.
  The ring proof's reduction was never golden-mean-specific; it's a language
  property the dimension counts were certifying for two rounds.
- **Proof joints, all machine-verified**: (J1) the five affine-lift formulas
  exact on every cell-vertex; (J2) the (s,y)-collapse — cell-nonneg ⟺
  {s_i+s_j≥1, s_j+y_i≤1, s_i+y_j≤1, 0≤y≤s≤1} — exact on the 5⁴ rational grid;
  (J3) integral (s,y) points decode to EXACTLY ρ₅'s five legal pairs; (J4)
  Heller–Tompkins signing by the bipartition of subdivided K₅ gives every row
  ≤2 nonzeros of opposite sign, and 4000 random square submatrices all have
  det ∈ {0,±1} (TU supporting evidence; HT theorem itself = shelf/classical).
  **⟹ C = R on every bipartite G; P35 upgrades from sampling-grade to
  theorem-certified, K₅ minor and all.**
- **P37 HIT — the θ-sweep is a constructive realisation, certified**: on 8
  exact C-vertices of the P35 (3434-section) instance, the anti-comonotone
  θ-sweep (threshold θ on the + class, 1−θ on the −) yields a LEGAL section
  on every θ-interval and the interval-length mixture reproduces q EXACTLY in
  rational arithmetic, 8/8. The "mod-2 potential" is a literal algorithm; the
  Lean-friendly proof route (finite case analysis + Lebesgue-on-an-interval,
  no TU library). Ring even-half / NAND-on-bipartite / P25 / P34 / P35 are
  now instances of one statement.
- **P36 splits the hypothesis — one direction clean, one open (as the design
  side predicted the posture should be)**: over 220 marginal-determined,
  connected, recurrent-branching languages ≤4 states: pair-bipartite ⟺
  cumulative-signable AGREE on 207; **CS-not-PB = 0 (the hard direction: no
  signable language fails pair-bipartite — signability ⟹ pair-bipartite, a
  clean implication)**; PB-not-CS = 13 candidate splitters (incl. ρ₁₃'s base
  0→{1,2},1→0,2→0 pattern), meaning pair-bipartite may be STRICTLY WEAKER
  than cumulative-signable — OR the cumulative-basis operationalization
  misses signings the general HT condition would catch. **Actionable for the
  design side**: the 13 PB-not-CS languages are the exact test set for
  "is pair-bipartite sufficient for safety, or only signability?" — run one
  on a bipartite-with-K₅-minor frame to decide. (This side flags: our
  signability check is cumulative-basis-restricted; a PB-not-CS language that
  is nonetheless SAFE on subdivided K₅ would show the restriction, not the
  theorem, is what PB-not-CS caught.)
- **Residual open class for Circuit Localization now precisely named**:
  branching languages that are NOT marginal-determined (u-reduction fails;
  extended formulations the plausible tool).
**Ledger: 29 hits / 7 informative misses / 1 vacuous / 2 dead conjectures /
1 pre-emptive kill / 1 corrected mis-triage. Taming #7 = the programme's
second proved theorem after parity; Circuit Localization follows for
marginal-determined branching languages on bipartite structure.**

### 2.2p Endgame triage — P38a/P39 miss informatively; the 13 are REAL non-TU forks; non-MD safety EXISTS (2026-07-10)
Run: `endgame_triage.py` + direct polytope confirmations. Two of three
predictions missed, both load-bearing; corrections recorded.
- **P38a MISS (benign): ZERO of the 13 dissolved** under all alphabet
  orderings (predicted >= half were basis artifacts). The good outcome — the
  TU triage then showed all 13 are GENUINELY non-TU (7-30 non-{0,+-1}
  subdeterminants each in 6000 samples), so they are real PB-non-TU objects,
  not cumulative-basis artifacts. Pair-bipartite is strictly weaker than TU.
- **P39 MISS (substantive - corrects the endgame plan): the non-MD safe set
  is NOT empty.** A 3-state non-MD recurrent-branching language has a full
  even-safe set, POLYTOPE-CONFIRMED at exact-facet level (not just the
  swap-criterion): rho = {(0,0),(0,2),(1,0),(1,1),(1,2),(2,0)} is
  COMMENSURABLE at L=4 (n=8) and L=6 (n=19), INCOMMENSURABLE at L=3 - kernel
  dim 1, |rho|=6 > 2|A|-1=5, pair-bipartite FALSE. So the MD counting bound
  is necessary for the affine-lift PROOF, not for the safety PHENOMENON - the
  swap-criterion (safe = evens) agrees with the polytope even off MD and off
  pair-bipartite. The "non-MD => vacuous" plan is dead; non-MD safety is a
  real region needing its own mechanism (extended formulations, non-empty
  target).
- **The MD-bound pattern still holds as stated** (NAND/golden/rho5 sit AT the
  bound 2|A|-1; FULL2, NE3 exceed it and are unsafe-everywhere) - but it is
  now known to be a proof-machinery boundary, not a safety boundary.
- **P38b is now the whole ballgame, sharpened**: all 13 PB-languages are
  non-TU, so NONE is covered by taming #7 (theta-sweep provably won't exist -
  non-TU kills the global alignment). The minimal one, rho =
  {(0,1),(0,2),(1,0),(2,0)} (|A|=3, the graded-d2 exemplar - also taming-#4's
  object, now revealed PB-non-TU), goes to subdivided-K5 with prediction
  WITHHELD: safe => integrality-below-TU (RHS-specific, new proof idea,
  theta-sweep absent); unsafe => THE FORK (circuit-innocent minor-type
  contextuality; autopsy = restrict to circuits [all safe] then locate
  witness support's cycle-space class). The genuinely open decisive
  experiment - awaiting design-side registration of P38b.
**Ledger: 30 hits / 9 informative misses (P38a, P39 added) / 1 vacuous / 2
dead conjectures / 1 pre-emptive kill / 1 corrected mis-triage. Endgame
reduced to P38b (the 13 non-TU forks) + non-MD safety mechanism.**

### 2.2q Taming #8 (twin expansion) PROVED; P41 hit; but P40 REFUTES the dissolution prediction — 11 twin-free forks remain (2026-07-10)
Run: `twin_taming_tests.py` + corrected re-run + non-TU spot-checks.
- **Taming #8 verified**: states 1,2 of rho_min are non-reflexive twins
  (identical in/out neighborhoods, no self-loops - machine-confirmed);
  collapse -> strict alternation (deterministic). The phase-mixture
  constructive proof runs: rho_min SAFE on subdivided-K5 (|V|=1056,
  dim C = dim R = 16, 80/80 exact LPs, NO TU) - "decomposition conditioned on
  forced phase," a genuine below-TU integrality mechanism (resolves the P38b
  "new proof idea" question for the twin sub-case).
- **P41 HIT**: reflexive twin-expansion of equality's fixed point produces a
  full-2-language block {0,2}; ring-safe set EMPTY 3..9 - reflexive twinning
  is an UNSAFETY generator, confirming taming #8's scope condition is
  load-bearing.
- **P40 REFUTES the registered "rho_min's class dissolves" prediction.**
  Twin-collapse (detector fixed after I flagged + hand-verified a doubted
  case) of the 13: only **2 dissolve to strict alternation; 11 reduce to
  SMALLER twin-free quotients that remain MD, pair-bipartite, non-signable,
  and NON-TU** (quotients spot-checked: 8 and 16 bad subdeterminants). So
  twin-expansion is a real taming but NOT the mechanism behind the 13 -
  eleven genuine twin-free fork candidates survive, the smallest now
  |A|=3 {(0,1),(0,2),(1,1),(2,0)} and {(0,2),(1,0),(1,1),(2,0)}. The
  twin-tower classification conjecture (as a route to closing the fork by
  structure) is REFUTED at this scale; the fork does not reduce to signable/
  deterministic cores via twinning.
**Consequence: P38b is back as the genuinely decisive experiment, now on the
minimal twin-free quotient** {(0,1),(0,2),(1,1),(2,0)} (|A|=3, subdivided-K5),
prediction withheld - safe => a below-TU integrality mechanism BEYOND the
phase-mixture (which only covers twins); unsafe => THE FORK. The catalogue did
NOT close the case; the decisive run is required.
**Ledger: 31 hits (taming #8, P41) / 10 informative misses (P40 dissolution)
/ 1 vacuous / 2 dead conjectures / 1 pre-emptive kill / 1 corrected
mis-triage / 1 corrected detector-bug (same-round, hand-verified).**

### 2.2r Taming #9 (monotone collapse) + the orientation scoping + P42 FINDS THE OBJECT: the P4-path language (2026-07-10)
Run: `symmetry_split_p42_p43.py` + structural interrogation.
- **Scope correction logged as a DEFINITION (design side)**: "Safe on G" is
  ORIENTATION-DEPENDENT for non-symmetric languages; the dynamically
  meaningful frame = every arc forward-in-time, every vertex recurrent
  (tournament-oriented, strongly connected). Mixed-orientation frames model
  no dynamical observation. The minor-theoretic side (Barahona-Mahjoub, cut
  polytopes) is UNDIRECTED theory -> transfers to SYMMETRIC languages only.
- **Taming #9 (monotone collapse) verified**: non-symmetric relations induce
  monotone potentials on uniformly-directed subdivision paths; strong
  connectivity forces them constant, collapsing C to conv(sections). rho† =
  {(0,1),(0,2),(1,1),(2,0)} on directed theta(2,2,2): dim C = dim R = 4 (C=R,
  sections only) - the confound that would have poisoned P38b-as-specified
  (verdict "safe" = rigidity, not below-TU integrality). ALL 10 non-symmetric
  quotients of the 11 collapse on the directed frame (2 arc-transient =
  taming #5 at arc level; 8 by potential-collapse, dims matching exactly at
  |V| up to 21).
- **P42 IS NOT EMPTY - it finds the object.** Exactly ONE symmetric fork
  survivor at <=4 states, identical to the lone symmetric member of the 11:
  **{(0,1),(0,3),(1,0),(1,2),(2,1),(3,0)} = the P4-PATH language** (undirected
  graph = path 3-0-1-2 = the A4 Dynkin diagram; hom-into-a-path). Symmetric,
  twin-free, MD, pair-bipartite, NON-signable (all orderings), NON-TU, Safe =
  evens (unsafe at odd L=3..11, exact). **This is the honest P38b carrier the
  endgame was reaching for**: a natural, NAMED, symmetric language; undirected
  frame so no orientation confound; minor theory fully engaged; nothing
  catalogued tames it (not signable, not twin, not graded, not deterministic,
  not collapse - symmetric so #9 inapplicable).
**P38b, finally well-posed: the P4-path language on subdivided-K5 (undirected),
prediction genuinely withheld.** Safe => a below-TU integrality mechanism for
hom-into-a-path (new mathematics, the θ-sweep/phase-mixture don't reach it);
unsafe => THE FORK - circuit-innocent, minor-type contextuality from a Dynkin
diagram, and the covering-space/cut-polytope frame becomes the proof language.
Six candidates dissolved by taming; the seventh is a path graph and does not.
**Ledger: 33 hits (taming #9, P43-via-lemma) / 10 informative misses / 1
vacuous / 2 dead conjectures / 1 pre-emptive kill / 1 corrected mis-triage /
1 corrected detector bug. NINE tamings. The impossibility route is NOT open
(P42 non-empty); the decisive experiment is required and now cleanly posed.**

### 2.2s Taming #10 (phase decoupling) + counting theorem + Circuit Localization CLOSES for symmetric MD (2026-07-10)
Run: `taming10_forest.py` + standalone counting/P46. The A4-path dissolves,
and the mechanism that kills it classifies the whole symmetric-MD world.
- **Taming #10 (bipartite-target phase decoupling) verified**: the P4-path is
  a TWISTED DOUBLE of NAND. J10 exact: all 36 homs C6->P4 carry a global
  phase (G-class -> single P4-class), and 2 x |independent sets of C6| =
  2 x 18 = 36 = |homs| - two NAND copies braided over one phase scalar t.
  C_t = t.FSTAB (+) (1-t).FSTAB, R_t = t.STAB (+) (1-t).STAB; on bipartite G,
  FSTAB=STAB (taming #7) => C=R. Non-signable/non-TU in raw coords is exactly
  what FIBERED-TU looks like to a flat detector.
- **P44 HIT to the sharp number**: P4-path on subdivided-K5 SAFE, dim C =
  dim R = **31 = 1 + 2*15** (one phase scalar + two independent 15-vertex-
  marginal copies) - the falsifiable fibered signature; |V|=2900, 80/80 LPs.
- **P45 HIT**: claw K_{1,3} on subdivided-K5 SAFE, dim 31 (tree theorem's
  first non-path instance). (5-spider: harness dim-R routine doesn't scale to
  its ~>5x10^5 homs - a tooling limit, NOT a math question; the claw already
  instances the tree theorem; flagged, not hidden.)
- **COUNTING THEOREM confirmed as a BIJECTION**: over 1819 symmetric-loopless
  MD targets (<=6 states) ZERO are non-forests, and all 1441 connected trees
  ARE MD -> symmetric-loopless-MD <=> forest, exactly. |rho|=2|E| <= 2|A|-1
  forces |E| <= |V|-1 = forest = bipartite = phase-decouples. The A4-path was
  the GENERIC member of a class taming #10 sweeps wholesale.
- **P46 EMPTY**: no loopy symmetric MD, pair-bipartite, non-signable survivor
  at <=4 states - the loopy remainder is fully tamed by signability/decoupling.
- **=> CIRCUIT LOCALIZATION CLOSES FOR THE SYMMETRIC MD CLASS**: every
  symmetric MD language is forest-target (tamed by #10 + tree recursion) OR
  has loops within signable/twin/decoupling reach (P46 empty). The fork is
  EXPELLED from symmetric MD by structure - seven dissolutions were the
  impossibility theorem assembling.
**The fork's two remaining habitats, both named and both beyond marginals:**
(1) NON-MD SYMMETRIC - where the classical hard targets live (odd cycles,
NE3: 2|E|=2|V| > 2|V|-1; the CSP-hard languages are PRECISELY the ones the
marginal reduction cannot see - coincidence or the whole story), governed by
rho39-style extended formulations - now the frontier's center of mass;
(2) NON-SYMMETRIC - governed by taming #9 collapse + holonomy, pending the
directed-obstruction formulation.
**Ledger: 36 hits (taming #10, P44, P45-claw, counting theorem, P46) / 10
informative misses / 1 vacuous / 2 dead conjectures / 1 pre-emptive kill /
1 corrected mis-triage / 1 corrected detector bug. TEN tamings. Symmetric MD
Circuit Localization = the programme's proved endpoint on that class.**

### 2.2t P47/P48/P49: the universal impossibility conjecture — symmetric fully expelled, SCC reduction, last-candidate scan EMPTY (2026-07-08)
Run: `universal_conjecture.py` + `_p47check.py` (dim-based, exact) after a
swap-criterion/polytope DISCREPANCY was caught and resolved (below).
- **⚠ TOOLING DEFECT surfaced and corrected (this side's, on the record):**
  the swap-criterion `unsafe_set` reported C4/C5/C6-TARGET languages unsafe at
  ALL lengths - WRONG. Polytope ground truth (exact, `_p47check.py`) contra-
  dicts it at C5-target L=2 (SAFE) and the girth-locked safe lengths. The
  criterion (theorem-let A) was validated by P29 on the RECORDED profiles but
  never on Cₙ-TARGETS; it has a multi-outcome-target bug. The design side's
  hand BFS was RIGHT; my swap-run was wrong. Polytope used for P47.
- **P47 (corrected, polytope-exact) - symmetric non-MD EXPELLED, cleaner than
  predicted:** cyclic-target safe sets are SPARSE and GIRTH-LOCKED -
  C4-target SAFE at even L (4,6; bipartite); C5-target SAFE only at 5,7
  (near its girth, "missing 2" as registered); C6-target SAFE only at 6
  ("missing 4" as registered). Girth-locked sparse safe sets CANNOT make all
  seven circuits of a K4-minor frame (which carry several distinct lengths)
  simultaneously safe. So every cyclic symmetric H is fork-incapable, and with
  last round's forest result, **the fork cannot live anywhere in the symmetric
  world.** Moral resolved on the coincidence side: the CSP-hard targets aren't
  the fork's habitat - they're unsafe almost everywhere, the opposite.
- **P48 (SCC reduction lemma = taming #9's true form) - VERIFIED, sharp
  signature exact:** rho39's only predecessor of state 1 is 1 itself
  (machine-confirmed), so on any recurrent ring u(1) is a sealed membrane:
  L=4 (n=8) and L=6 (n=19) both COMMENSURABLE (exact facets), and the sharp
  signature holds - state 1 appears ONLY in the all-1 section (membrane
  cells p(10),p(12) carry no recurrent flux). The non-MD kernel coordinate
  WAS the membrane flux; recurrence seals it; what remains = all-1 mixed with
  NAND-in-costume, tamed by #7. General lemma: for any out-closed union U of
  SCCs, U-mass is monotone along arcs -> constant on strongly connected
  frames -> commensurability reduces to strongly connected languages,
  wholesale.
- **P49 (the last fork candidates) - EMPTY:** exhaustive scan of strongly
  connected, non-symmetric, recurrent-branching languages <=4 states with
  Safe ⊇ {6,8}, screened vs the catalogue: ZERO untamed survivors (scanned 0
  reaching the Safe-{6,8} + nondegenerate filter - the demand itself is
  nearly unsatisfiable at small scale). **The universal impossibility
  conjecture is UNREFUTED at <=4 states.**
**THE UNIVERSAL CONJECTURE, on the record (NOT asserted - final case genuinely
open):** the fork does not exist - Circuit Localization holds universally for
total languages on gate-passing time-realizable frames - because blocking
exchanges at a rich length set forces one of the ten catalogued structures
(determinism, grading, twins, signability, phase-decoupling, collapse, SCC
reduction, ...), and every catalogued structure localizes the polytope. After
symmetric expulsion (P47 + forests) and SCC reduction (P48), the fork's entire
possible residence = strongly connected, non-symmetric, recurrent-branching,
rich-safe-set languages on time-realizable frames; P49 finds none at <=4
states. Design-lane attack: the exchange-blocking classification (avoiding
pair-exchanges at 6,8 => cofinitely-even by theorem-let B's AP structure =>
grading/potential/phase-code), provable via Wielandt-bounded finitely-many
residue classes.
**Ledger: 38 hits (P47-corrected, P48, P49) / 10 informative misses / 1
vacuous / 2 dead conjectures / 1 pre-emptive kill / 1 corrected mis-triage /
2 corrected tooling defects (detector + swap-on-targets). TEN tamings +
SCC-reduction meta-lemma. Symmetric world fully fork-free; universal
conjecture unrefuted at small scale.**

### 2.2u CORRECTION + P50-P52: third tooling defect (dim-test), verdict-grade ladder, expulsion witness-certified (2026-07-08)
This round is primarily a CORRECTION of 2.2t, with defects on both lanes.
- **THIRD TOOLING DEFECT (this side's, decisive): `_p47check.py`'s
  dim-equality test is NECESSARY-NOT-SUFFICIENT.** dim C = dim R does NOT
  prove C = R. Machine-confirmed: C4-target L=4 has dim C = dim R = 17, YET
  the design side exhibited an EXACT rational witness in C\R (all-halves
  backtracker orbit, EA-coherent, unrealisable). **=> My 2.2t verdicts
  "C4-target safe on even rings" and "C6-target safe at {6}" are WRONG and are
  RETRACTED.** The corrected picture: cyclic symmetric targets are unsafe at
  essentially all usable lengths; C5-target's {5,7} "safe" is CLOSURE-LEVEL
  RIGIDITY (at L=5 the variety = 10 rotations, every context is the discrete
  partition, EA collapses to the simplex - the gate-failure semantics, NOT a
  circulation-safe fact).
- **The symmetric expulsion theorem STANDS, with STRENGTHENED (witness-grade)
  evidence:** the backtracker orbits at C4-L4/L6 and C6-L6 are genuine
  Lemma-1/2 objects (EA-coherent, layer-injective, outside R). Cyclic
  symmetric targets are unsafe almost everywhere => cannot make a K4-frame's
  circuits safe => fork-incapable. The fork remains expelled from the entire
  symmetric world (MD = forests, 2.2s; non-MD = exchange richness, now
  certificate-grade).
- **Design-side instrument failures, logged (theirs, owned):** (1) their
  first L=4 "witness" was the doubled rotation - NOT layer-injective
  (s0=s4), realizable by mixing two rotation sections; the injectivity clause
  (the one that saved rho13's L=3) caught it - the fine print earning its
  keep, belongs in the Lean statement verbatim. (2) the C6-L6 first attempt
  had an illegal arc, corrected by difference-flip-then-hold (orbit
  [0,5,0,1,2,1,2,3,4,5,0,5], collision-free, layer-injective).
- **P52 - VERDICT-GRADE LADDER (policy amendment, on the record):**
  witness-certified-unsafe > exact-enumeration/theorem-certified-safe >
  everything else; **random-direction LPs DEMOTED to screening - never again
  the basis of a "safe" entry** (my 150-direction sweep returned a FALSE SAFE
  0/150 at C4-L6 where a witness sits in C\R). Retroactive audit: this
  touches exactly P32 (20/20 - already covered by hand factorization) and P35
  (200/200 - superseded by taming #7's proof); both survive because THEOREMS
  stood behind the samples. That was luck; now it's discipline.
- **P50/P51 (owed to the design side)**: run the two exhibited witnesses
  (C4-L4, C6-L6) through the EXACT membership pipeline; if C excludes them,
  diff EA constraint systems component-by-component to localize; a fast exact
  in-R membership test replaces the dim-check as the safe-certifier.
- **Swap-criterion fix spec (semantics-aware)**: the C5-L2 disagreement is
  TWO things - the multi-outcome bug (real, fix) AND the bifurcation (the
  swap criterion is aggregation/circulation-level, so at rigidity points like
  C5-L5 it SHOULD disagree with the EA polytope, both right about different
  objects). Corrected validation suite: reproduce C4-unsafe-at-evens and
  C6-unsafe-at-6 (circulation facts, witness-backed); FLAG rather than fail at
  C5-L5. A criterion that agrees with EA everywhere would be WRONG.
- **Semantics discipline for the impossibility proof (design lane)**: state
  it at DECLARED semantics throughout (circulation-level, gate-conditional) -
  today showed the two levels genuinely diverge on natural examples, and any
  theorem without its semantics tag will be "refuted" by a true fact about
  the other level.
**Ledger: 38 hits (P47 REGRADED to witness-certified, not retracted - the
expulsion holds; 2 sub-verdicts C4/C6-"safe" retracted) / 10 informative
misses / ... / 3 corrected tooling defects (detector, swap-on-targets,
dim-sufficiency). The frontier is UNCHANGED IN CONTENT, UPGRADED IN EVIDENCE:
symmetric world fork-free at certificate grade; universal impossibility
conjecture stands, final case = SCC non-symmetric.**

### 2.2v P53 amendment: C5's last "safe" lengths fall — cyclic symmetric targets unsafe at EVERY gate-holding length (2026-07-08)
Run: `c5_calibration.py` (standalone exact, no heavy import). Verified in THIS
environment, closing the last soft spot under the symmetric expulsion theorem.
- **C5-target L=7 UNSAFE (witness-certified here)**: the uniform-edge coherent
  point lies OUTSIDE R, exact residual 36/5. All 70 sections are
  adjacent-distinct (the whole L=7 variety is the alternation family), and the
  odd cycle admits no closing 2-colouring, so the coherent edge-marginal point
  is unrealisable = the pentagon's alternation wound 7 times (design-session
  orbit 0101010-wound-7). The earlier "L=7 safe" was the SAME dim/sampling
  instrument bug (2.2u), now witness-refuted.
- **C5-target L=5 GATE-DEGENERATE (not safe)**: every context is the discrete
  partition (all 10 cells are singletons, max cell size 1), so EA forces full
  agreement and C = simplex = R trivially --- safe-looking by RIGIDITY/gate
  collapse, NOT a circulation-safe length. Reclassified: gate-degenerate.
- **AMENDMENT to 2.2t/2.2u**: the "C5-target safe at {5,7}" entry is STRUCK
  entirely --- 5 is gate-degenerate, 7 is witnessed-unsafe. **The clean,
  strengthened statement: cyclic symmetric targets are unsafe at EVERY
  gate-holding length; NO genuine safe lengths exist anywhere in the symmetric
  world.** One bug (dim-equality + random-sampling, false-safe bias), one
  correction, sweeping C4-evens + C6-evens + C5-{5,7} all in the same direction.
- **P53 doubles as the swap-criterion fix's ACCEPTANCE TEST**: the corrected
  criterion must tell the two failure modes apart --- witnessed-unsafe (L=7)
  vs gate-degenerate (L=5) --- so `c5_calibration.py` is the calibration case
  no criterion-based sweep may bypass until it passes.
- **Symmetric expulsion theorem now rests entirely on certificate-grade
  ground**: forests tamed (taming #10, proved) + every cyclic symmetric target
  unsafe at all gate-holding lengths (witness-grade, no exceptions). No
  dim-certificates, no random sweeps, no survivor lengths remain in any
  symmetric verdict.
- **Injectivity clause reaffirmed (Lean, verbatim)**: it caught the design
  side's doubled-rotation error (2.2u) AND is the true unsafe/rigidity
  discriminant here (the padded-alternation witnesses turn on layer-injectivity).
  Leads Lemma 2 in the Lean queue.
**Ledger: frontier UNCHANGED (strongly connected non-symmetric class; universal
impossibility conjecture unrefuted) --- now with certificate-grade ground under
ALL symmetric verdicts and no dim-equality/sampling shortcut anywhere. Policy
foregrounded: every "safe" that mattered re-derived from a theorem or exact
enumeration; every "unsafe" from an exhibited witness; instruments trusted only
where they agree with one of those.**

### 2.2w P54 counterexample hunt: fork-free through 9 edges at 5 states (2026-07-08)
Run: `p54_hunt_sparse.py` (edge-stratified, canonical-deduped, exact). The
conjecture opened as a counterexample hunt per the design-side call --- try
hardest to build the strongly-connected non-symmetric survivor P49 missed,
5 states, safe-set demand RELAXED to any rich even set (>=2 of {6,8,10,12}
safe, nondegenerate).
- **Result (certificate-grade, bounded honestly): FORK-FREE through m=9 edges.**
  Edge-stratified exhaustive search, sparse first (where a minimal fork lives ---
  rho5 was 5 edges): m=5: 0 reps; m=6: 8; m=7: 92; m=8: 583; m=9: 2331 canonical
  SCC-non-symmetric-branching representatives. Every one is tamed by the CHEAP
  catalogue (determinism / grading / twin / MD+PB) before the safe-set test is
  even reached --- ZERO fork candidates at any stratum. The region where a
  minimal fork would hide is clear.
- **Full-density scan (all edge counts): IN PROGRESS.** The unstratified
  5-state scan (`_p54c`, 18M SCC-non-sym-branching arc-sets) is grinding in the
  background; it flushes any fork candidate the instant one appears and none has
  in 3+ minutes. NOT recorded as "empty" until it completes --- the honest grade
  today is fork-free-through-9-edges, not fork-free-at-5-states.
- **Method discipline (the night's lesson applied):** safe verdicts here are the
  integer-exact shift-reachability criterion (theorem-let A), NOT dim-equality
  or random sampling; any surviving candidate was to be forced to
  exact-witness grade before recording. None survived, so the discipline was not
  tested against a positive --- but it was in place.
- **What this earns the proof attempt:** the sparse strata are exactly where the
  exchange-blocking classification's base cases live, and they came back empty
  the way the symmetric candidates did under witness pressure. The design-lane
  proof attempt (exchange-blocking => grading/potential/phase-code via
  Wielandt-bounded residue classes) is earned on evidence through 9 edges ---
  with the standing flag that **theorem-let B (eventual periodicity at the
  tuple level) is itself unproven** and is the load-bearing lemma to establish
  separately, not assume (the exact analogue of the dim-equality shortcut).
**Frontier: unchanged --- strongly connected non-symmetric class, universal
impossibility conjecture unrefuted, now fork-free through 9 edges at 5 states on
top of the empty P49 (<=4 states, {6,8}). Full-density 5-state confirmation
pending.**

**The emerging reframe (hand to design side):** over V = N every certificate
seen — chains, cliques, odd-holes, syzygies, the new weighted one — is
pointwise-valid on N, because over V = N *every* valid inequality is (valid on
R's vertices = valid on R). So the classification is really a **facet-shape
taxonomy of R = conv(cell-incidence vectors)** — the correlation-polytope
facet theory (Pitowsky) specialized to partition protocols — and the
stratification measures which integer shapes suffice at which scale. Candidate
unifying shape for everything seen so far: **pointwise multiset-domination**
inequalities Σ_{c∈M₁} 1_c ≤ Σ_{c∈M₂} 1_c (integer multiplicities both sides;
chains = (m−1)·Ω-side special case via context-normalization, cliques/holes =
1·Ω and 2·Ω targets, syzygies = both directions, the n=5 certificate =
{B₁₂,C₁₃} ⪯ {A₁,A₁,A₂₃₄}). Design questions: (i) is every facet of these
polytopes multiset-domination (integer coefficients), and does the needed
multiplicity grow with n (Pitowsky's floor says SOME complexity must grow)?
(ii) should the harness gain a Family-III screen (all pointwise integer
inequalities with |coeff| ≤ w) to measure the weight-growth curve?

### 2.3 Layer-1 licensing results (roadmap; to be proved before pipeline work)
- **C1**: full-window coherence always extends to a trajectory measure
  (interval running-intersection + gluing + compactness; stationary and
  Markov/max-entropy corollaries).
- **C1′ (quarantine)**: finite-alphabet delay logics are compact/clopen, so
  the σ-essential pathology provably cannot occur in the data regime — the
  reconstruction foundations are *secured*, not threatened, by the witness.
  (Clopen charges are measures; finite certificates via Farkas.)
- Vorob'ev-transfer hypothesis check for outcome-identified hypergraphs.

## 3. Prior-art shelf (declared BEFORE the compare step — derive-first method)
Vorob'ev 1962 (consistency of marginal systems); Kellerer 1964 (marginal
problems); Rüschendorf (Fréchet classes); junction trees / running
intersection (Beeri–Fagin–Maier–Yannakakis, GYO); Abramsky–Brandenburger 2011
(sheaf contextuality; the strata map onto Paper II's ladder: probabilistic =
EA-without-PR, logical/strong = VDR blocked); KCBS / exclusivity-graph theory
(C₅, fractional packing); Leggett–Garg (temporal contextuality — MUST be
placed by us before a scout places it for us); Dzhafarov–Kujala CbD (already
in the library). **Added 2026-07-06 (second pass):** Cabello–Severini–Winter
(graph-theoretic hierarchy — expect substantial overlap with Family II; the
dynamical-realisation layer expected to remain ours); Grötschel–Lovász–
Schrijver; Strong Perfect Graph Theorem + recognition algorithm (CCLSV);
Pitowsky (correlation-polytope NP-completeness = the complexity floor);
Bulatov–Zhuk CSP dichotomy (for the axis-reduction direction only).

## 4. Verification ladder (user's code/Lean side, UPDATED after the second pass)
1. **The empty-intersection lemma** — one parameterized lemma; the 3-point
   example, k=2 necessity gadget, wrap-C₄ certificate, and conformality gadget
   are its m = 2 and m = 4 instances (formerly ladder steps 1–3, collapsed).
2. The pentagon chain-immunity check — the refutation record; finite,
   re-runnable (`pentagon_chain_immunity_check.py` — DONE in this environment,
   all four parts pass).
3. Bipartite ⟺ edge-completeness on small exclusivity graphs (König side of
   Family II).
4. The k=2 completeness proof — now also the statement "Family I is complete
   at k=2," the base case of the stratification.
5. GYO/α-acyclicity infrastructure for T1.
Open mathematical work, by leverage: axis-reduction theorem; T1 necessity in
full (gadget on every GYO core); Family I ∪ II completeness for single-window
protocols (or the third mechanism — exhaustive search over ≤ 6-outcome
protocols first).

## 5. Honest boundaries (recorded at capture)
- Reconstruction deliverable = "statistical Takens" (process = measure +
  shift), NOT manifold recovery — the dead bridge theorem showed geometric and
  algebraic reconstruction are inequivalent; manifold recovery is a separate
  inverse problem with injectivity hypotheses we do not assume.
- A single fully-observed series is never contextual (one path = a joint
  sample); Layer-3 applicability = aggregated/multi-run/coarse/limited data.
- The k=2 theorem and C1 are expected to be classical or classical-adjacent;
  the candidate novelty concentrates in the dynamical-realisation layer, the
  axis-reduction theorem, and the Bonferroni normal form. Park honestly if the
  compare step occupies them.
