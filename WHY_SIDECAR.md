# WHY sidecar: observations that bear on the question

reviewed: false. **Drafted by Claude for the author, not the author's words.** `WHY.md` is the compass and stays in the author's
voice. This sidecar collects dated observations from the work that refine, extend or temper it. The author reads and rewrites or
absorbs them in an own-words pass. Newest first. Each entry gives the claim, its status (owned / ours / lens), and where it lives.

---

## 2026-11-10 (late night): richness ↔ synchrony, and observability that depends on the phase (lens; night science; corrected after a summary-level check)
- **The author's upshot:** the practical object is phenomena (networks) that can switch regimes from **maximal
  richness to total synchrony**. **The switch changes the very nature of the phenomenon's observability.** This is the
  thread joining the two entries below.
- **Mechanism (share/total decomposition; lens):** a shared finite resource has a total T split into shares sᵢ, so
  node i receives sᵢ·T.
  - *Share variance:* the shares sum to 1, so each node has at least one negative covariance (Chayes 1960). All
    pairs are negative only for special share laws (Dirichlet). The result is compensatory structure with high
    effective dimension. *(Corrected: not "the centre hidden". If T does not move at all there is no cause to hide;
    with a little movement in T it is a weak common factor.)*
  - *Total variance:* the total hits every node with the same sign. The result is synchrony: effective dimension ≈ 1,
    with the centre all you can see.
  - **The regime change needs no new coupling,** only variance shifting from the shares to the total (T stalls or
    binds). Same network, same constraint, different phase. *(Known: Forbes–Rigobon 2002; Boyer–Gibson–Loretan 1999.)*
- **Against owned theory:**
  - Kuramoto (rising coupling to a mean field): here the mean field's own variance rises instead.
  - Moran effect: a shared driver, but one that does not also produce a compensatory phase.
  - Hubbell zero-sum dynamics.
  - The Loreau–de Mazancourt synchrony decomposition.
  - Houlahan et al. 2007: compensatory dynamics are rarer than expected, a caution.
  - Finance: "correlations go to one in a crisis"; the absorption ratio (Kritzman) as effective dimension.
- **Observability depends on the phase (the core point):**
  - Standard critical transitions become *more* legible near the tipping point: critical slowing down, rising
    variance and autocorrelation (Scheffer et al.; owned).
  - Here the approach is *masked*. Share competition scrambles the centre's signature (the 2026-11-06 antibalanced
    result), so correlation-based warnings are suppressed by the dynamics that create the risk. What follows is
    abrupt legibility.
  - **The blindness feeds back:** observers inside the system read low correlation as diversification, act on it
    (leverage, concentration on the shared resource) and raise the stakes. Owned economic cousins: Minsky,
    "stability is destabilising"; Brunnermeier–Sannikov's volatility paradox. Antibalanced hiding supplies the
    structural reason the stability *looks* real.
  - **Warning signs live in the total, not the correlations:** measure the centre directly (the variance of T against
    share churn) instead of inferring it from the nodes. *(Corrected: if the nodes add up to the whole total, the
    variance of T is the sum of all the covariances, so this is the same data, not new information. It helps only
    when T is observed independently. And Kritzman et al. report their ratio rising before turbulence, which cuts
    against "masked".)*
- **For the stance (answers first):** with the questions one can ask held fixed, whether they reveal a centre depends
  on the phase. *(Corrected: this is the standard notion that what can be identified depends on where the truth sits;
  keep it as vocabulary, not as a new seam. In econometrics a variance regime shift usually* helps *identification,
  Rigobon 2003.)*
- **Prediction withdrawn.** "The share/total ratio should shift before correlation rises" cannot work: in this model
  correlation is a function of that ratio, so they carry the same information.
- **What the check turned up (ours, unclaimed; hand + simulation, one agent, unchecked):** there is a range where
  every pair of nodes is positively correlated and the model-free common-cause test still registers nothing. Example,
  5 nodes with even shares: correlations turn positive early, but the test only responds once the total's swings are
  about four times larger. With very uneven shares it never responds. This is a fact about the tool's sensitivity
  (the applied "power" gap of 2026-11-06), not a new theory.
- **Status:** lens. Mechanism assembled from owned pieces; no seam survives as first stated. Checked 2026-11-10 against the literature at summary level only (abstracts, no full papers): `notes/open_questions/views_across_records/PHASE_IDENTIFIABILITY_PRIOR_ART.md`.
  Worth a full read: Loreau–de Mazancourt 2008, which appears to state the share/total split in other words.
- **Honest distance:**
  - "Maximal" and "total" are idealised ends; real transitions are partial.
  - Systems with several resources can have partial centres.
  - Nothing has been shown on data yet.

## 2026-11-10 (night): is information a finite resource? (lens; night science, from a conversation; corrected after a summary-level check)
- **The author's question:** "is information a finite resource? … it depends, specifically on what the information is
  about." Refinement offered: it depends on *which operations count as free* and on *which questions can be jointly
  asked*, more than on the subject matter.
- **Four kinds:**
  1. **Copies:** non-rival, so not finite. What sits in the span V of the askable is shared by everyone once a context
     reveals it.
  2. **Derivations:** unlimited in volume, bounded in content. By the data processing inequality, processing cannot
     add information about the world (owned). *(Corrected: this is not the mechanism of AI model collapse. Collapse is
     estimation error compounding when generated data replace real data, Shumailov et al. 2024, and it is avoided
     when real data keep accumulating.)* Synthetic data adds nothing beyond what its generator already holds.
  3. **Contact:** new information *about* something needs a measurement, record or transaction. It is finite in
     rate and costly. Grossman–Stiglitz (1980): prices cannot be fully informative when information is costly
     (owned; corrected wording).
  4. **Absent:** the joint question no context asks (outside V). It is unavailable at *any* price until a new context
     exists (an instrument, a record, or reality itself, e.g. an option's expiry).
- **Resource-theory form:** fix the free operations (copying, processing). Information about the world is then a
  resource, and the data processing inequality is its monotone. Contextuality has been treated as a resource in the
  same way (Abramsky–Barbosa–Mansfield 2017; owned).
- **Where it parts from the economics:** *(corrected)* complete-markets models assume every question can be asked at
  some price; Grossman–Stiglitz itself does not. "Absent, not merely scarce" is already known as missing or
  incomplete markets. What is specific here is only the cause: the gap can come from a loop in which questions can be
  asked together.
- **Bridges (lens):**
  - *AI scaling:* if the binding input is fresh contact with the world rather than compute, extra capex runs into the
    data processing inequality, which would give the logistic curve. A bend in capability slope while compute keeps
    rising would point to the informational reading.
  - *Markets:* coupling through a shared finite resource is information the price system structurally lacks.
  - *Ecology:* populations register a shared driver only through contact with it; synchrony is the record of that
    contact.
- **Against the four questions:** *Loop:* yes; the absent kind lives on loops. *Unaskable joint question:* that is
  the absent category itself. *Hidden idealisation:* the economics presumes every question is priceable.
  *Circle, or composition?* Not yet clear.
- **Status:** lens. The four kinds and the resource-theory reading are assembled from owned pieces. "Absent ≠ scarce"
  is owned (missing markets). "The AI bend would be informational" is conjectural and unsourced. Checked 2026-11-10 against the literature at summary level only (abstracts, no full papers): `notes/open_questions/views_across_records/PHASE_IDENTIFIABILITY_PRIOR_ART.md`.
- **Where:** conversation only (trading session, 2026-11-10). Companion entry: the option-markets entry below.

## 2026-11-10 (later): option markets as a gluing problem (lens; from a trading conversation; corrected after a summary-level check)
- **Claim (lens):** option prices are local views. Each chain is a context: a single name, or an ETF read as a linear
  *projection* of its basket. No-arbitrage is the claim that the contexts glue into one global pricing measure.
  - EA ↔ pairwise no-arbitrage (ETF vs its basket, CDS vs bond, calendar spreads).
  - PR ↔ one risk-neutral measure.
  - A Farkas certificate of non-gluing ↔ an arbitrage portfolio. The fundamental theorem of asset pricing is this
    duality exactly only for finitely many states; in general it needs extra closure conditions (Harrison–Kreps
    1979; Dalang–Morton–Willinger 1990; owned; corrected).
  - Bid–ask turns equalities into intervals (Jouini–Kallal 1995; owned).
  - *(Added.)* This whole reading is mostly the field's own, in other words: "arbitrage = Dutch book = outside a
    marginal polytope" is de Finetti and Pitowsky, and Steeger–Teh 2018 already ties Dutch books to the
    Abramsky–Brandenburger hierarchy.
- **Trees glue, in time:** one stock's expiries form a chain. Marginals increasing in convex order always glue into a
  martingale (Strassen 1965; owned). *(Corrected: the tree analogy is loose; the martingale condition is Strassen's,
  not Vorob'ev's.)*
- **Loops, across overlapping baskets:**
  - Single-name chains alone are disjoint contexts, so they always glue (vacuous).
  - Overlapping baskets make the context hypergraph cyclic: NVDA, AVGO and AMD sit in SMH, QQQ and XLK at once.
  - Dealers enforce coherence pairwise (each ETF against its own basket).
  - The hidden-twist analogue: every two-instrument check passes, yet there is no global measure. The certificate is
    then an arbitrage needing legs in every context round the loop, so limits to arbitrage gain a *topological*
    component.
  - Nearby owned ground: PSD completion is guaranteed on chordal patterns (Grone–Johnson–Sá–Wolkowicz 1984); the
    dependence-uncertainty literature (Rüschendorf, Puccetti, Embrechts, Wang); martingale transport bounds for one
    asset across expiries (Beiglböck–Henry-Labordère–Penkner 2013; corrected, not cross-asset); overlapping baskets
    as static-arbitrage bounds (d'Aspremont–El Ghaoui 2006; Hobson–Laurence–Wang 2005).
- **Antibalanced competition hides the finite-resource centre:** this applies the 2026-11-06 Crystal Lake observation.
  - A sector of firms competing pairwise for the same contracts shows low correlation and high dispersion. In the AI
    compute cluster, 2026, the absorption ratio is near a record low [data claim, unchecked].
  - On the zooplankton finding, scattered pairwise competition is exactly what hides a shared driver. So low
    correlation is not evidence that no shared finite resource (power, capital, end-user revenue) binds them.
  - Centres map as follows:
    - pricing kernel or shared resource = shared driver;
    - dealers' common balance sheets and vol-surface models = shared protocol (a method effect; question 5, "rule or
      cause?").
- **Real loop, star-shaped questions:** the actual exposure graph is cyclic (circular financing among chip vendor,
  labs, clouds and lenders). The questions one can ask (instruments) form roughly a star: single names plus a few
  indices. The loop's closure is a joint question no context asks, so no price must reflect it (WHY question 2).
- **Status:** lens, and mostly a restatement of known finance in this programme's words. A sheaf-theoretic account
  of no-arbitrage was not found in two searches (a weak negative). Possible question: gluing with overlapping
  *linear-projection* (basket) contexts rather than pair tables. Not claimed. Checked 2026-11-10 against the literature at summary level only (abstracts, no full papers): `notes/open_questions/views_across_records/PHASE_IDENTIFIABILITY_PRIOR_ART.md`.
- **Honest distance:**
  - The triangle results concern pair-marginal tables, but option data gives one-dimensional marginals plus
    projections: a different marginal problem.
  - Bid–ask noise may swamp any hidden incoherence (as in the merging gap).
  - The model-free common-cause test could in principle run on daily implied-vol co-movements, but option panels are
    short (power).
- **Where:** conversation only. Applied side: `~/Projects/trading`.

## 2026-11-10: the triangle hides nothing above its windows (ours, unclaimed; hand + partial Lean)
- **Claim:** on the triangle of three pair-queries, every question the carrier can ask is three window questions plus
  one question on a finite coarse-graining. So an answer pattern is fixed by what the windows say.
- **Against the four questions.** *Loop:* yes, and all of it shows at the windows (three answers of 1 where at most
  two can hold at any point). *Unaskable joint question:* the infinite cyclic order is the one question the carrier
  cannot ask. *Hidden idealisation:* none above the windows; "anything hidden sits in patchworks of patchworks"
  (2026-11-06) is withdrawn, and the 2026-11-07 entry's "open case" is closed on the triangle. *Circle, or
  composition?* Composition.
- **Status:** hand proof, two independent checks; **fully machine-checked** the same day (`TriangleFinitary.lean`: `mem_dfin`, `state_ext`, `normal_form`, no `sorry`; alphabet ℕ); prior art: one weak scout pass, nearest sources unread; not claimed. Triangle only; longer cycles and graphs containing a triangle are not covered.
- **Where:** `notes/open_questions/views_across_records/TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`.
- **Honest distance:** a statement about idealised yes/no answer patterns. Lens only for data merging.

## 2026-11-07: PBR and the product assumption (lens; unread, from memory)
- **Claim (lens):** the Pusey–Barrett–Rudolph theorem (*Nature Physics* 2012) [unverified] gets "one world behind the
  state" (ψ-ontic) from *preparation independence*: independent parts combine as the **product** of their marginals.
  The triangle work finds that this is exactly what local views cannot guarantee. Every finite coarse-graining of an
  answer pattern looks like the product point of its marginals, but the windows carry *which* joint sits over those
  marginals (e.g. p⊗q vs q⊗p), and the twist lives there (`TRIANGLE_GATE_ATTEMPT.md` §5c; Hindman–Strauss §11.1).
- **Status:** lens only. PBR is points-first (an ontic space Λ, σ-additive measures); the programme is answers-first,
  and its open case is finitely additive and two-valued, outside PBR's frame. Nothing here bears on PBR's proof.
- **Prior art to check before using:** critiques of preparation independence (Hall; Emerson–Serbin–Sutherland–Veitch;
  Schlosshauer–Fine) [unverified]; Leifer 2014, "Is the quantum state real?" [unverified]; Spekkens' ψ-epistemic
  programme and preparation contextuality [unverified]. None is on the shelf.
- **For the question:** PBR is a "centre" theorem bought with a product assumption. Order without a centre, if it
  exists, has to live where joints are not products of their parts.

## 2026-11-06 (latest): an abstraction over the map (lens; to draft when wanted)
- **Local-to-global (gluing):** local pieces on overlapping parts of a whole. Three questions:
  - **existence** (any global object?);
  - **uniqueness** (only one?);
  - **location** (an ordinary point, or at infinity?).

  These are asked over different kinds of local data (coefficients):
  - *group values* (holonomy; frustration as a ℤ₂ class; HodgeRank's harmonic part);
  - *probabilities* (marginal problem / contextuality / ε*; Gibbs phases = non-uniqueness; boundary conditions at infinity);
  - *cones* (covariance decompositions; centres needed; non-unique minimal centres);
  - *yes/no states* (pointless coherence; ultrafilter choices; ideal points / the invisible dictator);
  - *observations of spacetime* (Manchak: non-uniqueness).
- **Owned language:** sheaf/Čech obstructions; Abramsky–Brandenburger; Robinson; DLR consistency; discrete Hodge theory; Harary balance.
- **Not seen anywhere:** the grid itself (results across fields as cells of the same three questions × coefficients, with the empty cells marked,
  e.g. uniqueness and location for cones). Possible framework/exposition contribution (Types 3/6). Close to `theory_shape.md`. Draft a one-page grid
  when the author wants it.

## 2026-11-06 (latest): how twist returns practically (lens; owned)
- **Three practical forms of twist:**
  1. *Frustration* (of −R, i.e. a loop that is not antibalanced): reveals that a centre is needed (used in the synchrony tests).
  2. *Holonomy*: pairwise conversions or calibrations that do not close round a loop, so there is no common scale. Owned: geodesy loop misclosure;
     metrology; AHP/Koczkodaj; synchronization. **HodgeRank** (Jiang–Lim–Yao–Ye 2011) splits pairwise comparisons into gradient + local loops (curl) +
     global loops (harmonic). The harmonic part, "pairwise fine, globally twisted", is a clean, owned mathematical home for WHY's image "the twist lives
     in the loop".
  3. *Cyclic order*: intransitive competition, Condorcet cycles. Owned as question and answer (Kendall & Babington Smith 1940; Allesina & Levine
     2011; Godoy et al. 2017).
- **Practically:** the strict "no world at all" twist is rare (decoherence). Twist returns as *no common scale* and *no global order*.
- **Ecology:** no open dataset with a true A–B, B–C, A–C calibration loop was found (`CALIBRATION_DATA_SCOUT.md`). The closure question for multi-method
  surveys is left as a lens. Files: `notes/open_questions/views_across_records/CALIBRATION_LOOPS_PRIOR_ART.md`.

## 2026-11-06 (latest): seam B closed. "Consensus no one holds" is a centre at infinity, not pointless (owned)
- **Reversal of the 2026-11-05 lens:** I had suggested finitely additive "consensus no one holds" might be pointless coherence. For exact consensus that is
  **false**. Independent sources forced to agree give an *ultrafilter*: a common value "at infinity", i.e. an **ideal point**. This is the invisible dictator of
  infinite-electorate social choice (Kirman & Sondermann 1972).
- **For the question:** even when no individual holds the consensus, the consensus still has a centre. It is pushed to infinity, not abolished. In physics
  the same shape is the boundary condition at infinity that selects one ordered phase (Gibbs measures). Pointlessness, order with no centre even at infinity,
  needs twist, and consensus has none. **So "order without a centre", if it exists, lives in twisted loops, not in agreement.**
- Residue (conditional, `SEAM_B_PRIOR_ART.md`): on infinite-valued rings, whether all-pairs-agree states always come from ultrafilters. The expected answer is yes.

## 2026-11-06 (latest): decoupling the shape of the centre from dynamics
- **Claim (ours; owned pieces):** what you see in levels is the *interaction-closure* of what happens at once. Small local shocks spread by
  long-memory interaction look like one big centre. Innovations (same-time shocks after removing the lagged dynamics) separate the two.
  Validated by simulation.
- **Polish beech:** after removing the dynamics, the same-time shocks still need a centre binding stands > ~370 km apart (cause arity ≥ 4). The order is held
  by something acting now across the region (or the shared protocol), not by local relations whose history has spread.
  **Corrected (prior art):** propagation *within* a year (e.g. pollen) also looks same-time. So the result excludes relations accumulated *across years*,
  not within-year relations. The closure statement itself is owned (trek rule), and as first stated it was vacuous; its content is the truncated bound. `notes/open_questions/views_across_records/DYNAMIC_CLOSURE.md`.
- **For the question:** this is the first case where the tools say *which kind* of non-pairwise order holds a real system together, a present regional
  centre rather than accumulated relations. It does not decide between nature and observer.

## 2026-11-06 (later): one record, which world? PARKED (revisit if it comes up again)

- **Claim (lens):** with a single record (the universe), "does it add up to one world?" is trivially yes. "*Which* world, described how?" is never
  fixed by data alone. It needs a selection principle: independence of settings, typicality of the initial state, simplicity, a state-fixing theory,
  or a global constraint. The law/initial-state split is itself one such choice ("centre in law" vs "centre in the past").
- **Formal anchors (owned; from memory, unread):**
  - cosmology: Glymour 1977; Malament 1977; Manchak 2009, "Can we know the global structure of spacetime?" (observationally indistinguishable,
    non-isometric spacetimes are generic);
  - inference: Kelly 1996 *The Logic of Reliable Inquiry* and the Ockham efficiency theorems; Wolpert's No Free Lunch; MDL / Solomonoff;
  - statistics: identifiability;
  - quantum: Bell + Hall's measurement dependence.
- **Alternatives to the law–state split:**
  - Unger & Smolin 2014, the "cosmological fallacy";
  - Hartle–Hawking no-boundary (the theory fixes the state);
  - all-at-once / global-constraint views (Wharton; Price & Wharton), which are close to the programme's answers-first stance and its cones;
  - Humean best-system laws.
- **Possible seam (unscoped):** the programme mostly asks *existence* of a gluing (can local views form one world?). Manchak-type results concern
  *uniqueness* of gluing (do they form only one?), and his constructions cut and paste local regions. A gluing-uniqueness counterpart to the cone
  theory might exist. Not checked.
- **Why parked:** heavily owned territory; it pulls toward abstract physics, away from the ecology and anarchism fire; another thread was in flight.
  Suggested reading for the author: Manchak 2009 (short).

## 2026-11-06: from the views-across-records work (`notes/open_questions/views_across_records/README.md`)

1. **Tempering the bridges (most important).** Real local views mostly *do* add up.
   - Simultaneous records always glue, and two records always glue (acyclic).
   - Brain EEG, lake plankton and lake physics all glued.
   - Structural reason: decoherence, i.e. the environment keeps redundant joint records of everything macroscopic (Zurek; owned).
   - Pointless, non-classical coherence is rare in nature *for a reason*. The lens holds, but the "Bridges into the world" read more
     optimistically than the evidence supports.
   - Where it bites: records that are separate, closing loops, strongly tied, and tied differently across records.
2. **The question has a second half: what holds the order, and what shape is it?**
   - *Static relations cap coordination:* with only pairwise links, three sites can agree at most (3√2 − 2)/4 ≈ 56%, under any physics
     (Gisin et al. 2020; owned).
   - The continuous, many-site version is scaled diagonal dominance (formerly "a correlation budget per site" here; Kela et al. 2020, Boman et al. 2005; owned).
   - Beyond the cap, coordination needs a **centre**:
     - *in space*, a shared driver;
     - *in time*, accumulated history, which requires long memory (a ≳ 0.9; the general reason is that the effective centre is the
       trek-rule closure of the innovation (shock) common causes, weighted by ρ(B)^{2k});
     - *in the observer*, a shared protocol (a method or batch effect).
3. **"Loops are where order without a centre lives", sharpened.** A centre larger than a pair can be revealed (from correlations) only on
   loops that are **not antibalanced**, where the signs round the loop do not multiply to (−1)^{length} (formerly "frustrated" here: frustration of −R, the reverse of Harary's usage on triangles). Antibalanced structure is always
   explainable by pairs (Boman et al. 2005; owned).
   - Same parity as the original cycle twist.
   - The signal fades with loop length (sec(π/L) − 1 ≈ π²/2L²).
   - Trees always glue (Vorob'ev; owned), as WHY says.
4. **Ostrom, refined: polycentric order is the hardest to see.** (The word is V. Ostrom–Tiebout–Warren's (Amer. Polit. Sci. Rev. 55(4), 1961, 831–842) and E. Ostrom's (Amer. Econ. Rev. 100(3), 2010, 641–672). Lens only: their governance sense and the hypergraph sense here are different things.)
   - A single small centre (reaching 3 sites) is invisible.
   - Different polycentric structures can explain the same correlations (the minimal set of centres is not unique).
   - "Regionality" in levels can be local interaction spread over time.
   - The order closest to "without a centre" is the least observable. (Ours, assembled from owned pieces; validated by simulation.)
5. **Intransitive and competitive structure, empirically.** In zooplankton communities, competition scattered between pairs hides shared
   drivers (antibalanced triangles). Guild-against-guild competition does not (Crystal Lake: 43% negative correlations, zero antibalanced
   triangles). (Ours; one lake; lens.)
6. **Centre in law vs centre in cause.**
   - Everyone running the same rule (shared DNA, shared physical laws) creates no coordination. Only shared *inputs* or a shared *origin* do.
   - A shared law makes a shared cause legible everywhere.
   - At cosmic scale, "a shared origin of everything" can explain any correlation (superdeterminism), so it needs an independent bound,
     like no-signalling. (Lens, from a conversation.)
7. **Honest distance, updated.**
   - There is now one real-data tool: a model-free test that coordination requires a common cause, with its minimum cause arity and spatial
     extent. Asymptotic validity is proved; size is validated by simulation.
   - **Positive control (Polish beech):** a centre is required; it reaches at least 4 of 10 stands; it is regional (local centres within
     368 km cannot carry it). Weather and protocol are not yet separable.
   - **Applied gap: power.** Only strong, wide centres are visible in ~50 years of data.
   - The merging / hidden-case gap from 2026-10-22 remains open.
8. **Candidate additions to the four questions:**
   - (5) *Is this a shared rule or a shared cause?*
   - (6) *Is the centre acting now, or spread from the past?*
