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
