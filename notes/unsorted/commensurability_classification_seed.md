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
