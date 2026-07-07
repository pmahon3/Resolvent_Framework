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
