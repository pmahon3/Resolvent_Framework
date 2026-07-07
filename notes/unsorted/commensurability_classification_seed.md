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
- **Bonferroni normal-form conjecture (the deep one)**: commensurability fails
  exactly when the cell-incidence lattice generates a Bonferroni-type valid
  inequality not implied by coherence; general-k criterion = a combinatorial
  normal form for such certificates.

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
in the library).

## 4. Verification ladder (user's code/Lean side, in the design session's order)
1. The 3-point and RCD examples (trivial encodings; pin EA and PR
   definitionally).
2. The k=2 theorem (both directions finite).
3. The wrap-cycle gadget with its max-cut certificate.
4. GYO/α-acyclicity infrastructure for T1.
Open mathematical work, by leverage: axis-reduction theorem; T1 necessity in
full (gadget on every GYO core); Bonferroni normal form.

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
