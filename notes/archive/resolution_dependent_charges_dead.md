# Seed Note: Resolution-Dependent Charges

## Phase: 1 (seed) — DEAD

## The observation

All sheaf-theoretic frameworks for probability (Zafiris, Biesel,
Abramsky-Brandenburger) assume that local data — states, charges,
probability measures on Boolean contexts — are exact. A charge on
a finite Boolean algebra assigns a sharp number to each element.
Compatibility between stages is exact restriction. The gluing
question is whether exact local data assemble into an exact global
object.

But in the programme's setup (directed refinement of finite Boolean
algebras), the charge at a given stage of refinement is not a sharp
reading of a pre-existing global measure. It is all the information
there is at that resolution. The fineness of the partition is
constitutive of what observation means at that stage.

## The idea

A charge at stage i should carry intrinsic width reflecting the
resolution of the observation. This width is not (or not only)
epistemic uncertainty about a "true value" — it is constitutive
of what observation at that resolution *is*.

ℓ_i(E) = 0.3 does not mean "the true value is 0.3 ± error."
It means "0.3 is what this value IS at this resolution." The
width is part of the value, not something you subtract to recover
a sharper truth.

## What changes if this is taken seriously

1. **Compatibility becomes softer.** Instead of exact restriction
   (ℓ_j restricts to ℓ_i on B_i ⊆ B_j), compatibility is:
   values at coarser stages are consistent with values at finer
   stages *within the widths that each stage carries*. The
   compatibility condition is resolution-dependent.

2. **CE changes character.** Standard CE: an exact compatible
   family extends to a σ-additive measure. With intrinsic width:
   the question becomes whether the narrowing process converges
   — whether the widths shrink to zero in the limit, producing
   a σ-additive measure. CE failure might mean the widths don't
   shrink, or shrink to something that isn't σ-additive.

3. **The sheaf condition changes.** A sheaf says: compatible local
   sections glue to a unique global section. With intrinsic width,
   gluing might produce a *range* of global objects. The question
   becomes about the diameter of that range as resolution increases.
   Uniqueness of the glued object is not given — it's something
   that emerges (or fails to emerge) in the limit.

4. **The local-to-global question gains a parameter.** The
   extension problem is no longer binary (glues / doesn't glue)
   but graded by resolution. At each stage you have a set of
   possible global extensions compatible with the width at that
   stage. The CE question becomes: does this set contract to a
   singleton (or at least to a set of σ-additive measures)?

## What this is NOT

- **Not imprecise probability (Walley).** Walley has interval-valued
  credences but exact compatibility conditions. The intervals are
  epistemic — you don't know which precise credence is right. Here,
  the width is constitutive, not epistemic, and the compatibility
  condition itself is resolution-dependent.

- **Not measurement error.** Measurement error is noise added to a
  true signal. Here there is no true signal at the given resolution
  — the width IS the signal at that resolution.

- **Not fuzzy sets / fuzzy logic.** Too coarse, wrong level of
  abstraction.

- **Not continuous model theory (Ben Yaacov).** That changes the
  logic to [0,1]-valued. This changes the *observations*, not
  the logic.

## What it might connect to

- **Information geometry / Fisher metric:** The Fisher metric
  measures distinguishability at a given sample size. At finite
  resolution, nearby distributions are indistinguishable — this
  is a form of intrinsic width. But Fisher geometry presupposes
  a parametric family.

- **Operator algebras / noncommutative probability:** In quantum
  mechanics, observables have intrinsic uncertainty (Heisenberg).
  But that's from noncommutativity, not from resolution. The
  Boolean case has no noncommutativity — yet the programme's
  setup still has finite resolution.

- **Topological/uniform structures on charge spaces:** The set of
  charges compatible with a given finite-stage observation might
  form a neighbourhood in some natural topology on the space of
  charges. The directed system then defines a filter of
  neighbourhoods. Convergence of this filter = CE?

- **The programme's own machinery:** The directed system of finite
  Boolean algebras already has a natural notion of resolution
  (fineness of partition). The charges at each stage are points
  in a simplex (the probability simplex on the atoms of B_i).
  The refinement map sends a charge on B_j to a charge on B_i
  (coarsening). The "width" might be: the fiber of this map —
  all charges on B_j that coarsen to the same charge on B_i.

## Making it concrete: fibers and the σ-additive defect

### The fiber as intrinsic width

In the programme's setup (Paper I), at stage i with charge ℓ_i
on B_i, define the *fiber*:

W_i(ℓ_i) = {compatible families in lim←Δ_n that project to ℓ_i}

This is a compact convex subset of the projective limit of
simplices. It is all the global extensions consistent with
observation at stage i. The "width" of W_i(ℓ_i) is the
constitutive ambiguity of observation at resolution i.

For a finite set of observations S = {(i₁,ℓ_{i₁}), ...,(i_n,ℓ_{i_n})}
from potentially *incomparable* stages:

W_S = ∩_k W_{i_k}(ℓ_{i_k})

Nested chains give nested fibers (trivial intersection to a
thread). Incomparable observations give nontrivial intersection
geometry — the fiber widths interact.

### The σ-additive defect

Every thread ℓ in W_S decomposes via Yosida-Hewitt: ℓ = ℓ^σ + ℓ^pfa.
Define the *σ-additive defect at stage S*:

d(S) = sup{‖ℓ^pfa‖ : ℓ ∈ W_S}

This is the worst-case purely finitely additive norm over all
threads consistent with observations S.

Properties:
- d(S) is computable from finitely many observations (finite-
  dimensional optimization at each stage)
- d(S) is monotone decreasing as S grows
- d(S) → 0 iff the observations force σ-additivity

### The key move: rates, not limits

The standard CE theorem (Paper I, Theorem 1.2) asks: is the limit
σ-additive? Binary answer. The completion assumption (the projective
limit exists and you're sampling a thread from it) is a point-space
presupposition.

The rate formulation stays relational:
- At each finite stage you have d(S), a computable quantity
- You observe how d(S) changes as S grows
- You commit to σ-additivity not by asserting the limit exists but
  by observing that the rate of contraction of d(S) is incompatible
  with a persistent purely finitely additive component

The commitment is defeasible but quantified. You don't assume CE —
you track the empirical evidence for or against it through the rate
at which the defect contracts.

### What the rate sees that the limit doesn't

- d(S) → 0 fast: the directed system's geometry forces σ-additivity;
  CE is empirically warranted with quantified confidence
- d(S) → 0 slowly: observations are consistent with σ-additivity
  but the geometry doesn't strongly constrain; CE is a weak
  commitment
- d(S) doesn't converge: the directed system's geometry is
  compatible with persistent purely finitely additive components;
  CE is unwarranted

Different directed systems with the same abstract partial order
but different refinement maps π_ij could have different contraction
rates. The rate is a geometric invariant of the directed system
invisible to both Łoś (algebraic — CE not first-order) and the
standard CE theorem (binary — CE holds or doesn't).

### Connection to the programme's questions

- **Question 1 (what must be added):** What's added is not an axiom
  (CE) but a commitment justified by a rate. Structure (σ-additivity,
  hence genuine probability) emerges when the rate warrants it.

- **Question 2 (reconstruction without points):** The rate
  formulation never assumes the projective limit exists. It works
  with the sequence {d(S)} directly — finite-dimensional, computable,
  relational.

- **Question 3 (local-to-global extension):** The contraction rate
  of d(S) is controlled by the geometry of the site (the refinement
  maps), not by the individual charges. This is an answer to "what
  conditions on the site control global extension" — the conditions
  are geometric (fiber contraction rate), not topological (sheaf
  condition on a Grothendieck topology).

## Pre-audit computation results (2026-05-17)

### The candidate claim (CONTRADICTED)

Original claim: d(S) is a computable geometric invariant whose
contraction rate is controlled by the geometry of the refinement
maps, characterizes CE empirically, and is invisible to exact
sheaf theory.

### What the computation shows

**d(S) reduces to tail mass / tightness.** At stage n with
observed charge ℓ_n on B_n:

d(S) = sup{‖ℓ^pfa‖ : ℓ ∈ W_S} = ℓ_n(T_n)

where T_n = "mass not pinned to identifiable atoms at stage n."
This is a property of the *observed charges*, not a geometric
invariant of the refinement maps.

### Three examples

1. **Fair coin (CE holds).** B_n = 2^n atoms (dyadic intervals).
   At stage n, every atom has mass 2^{-n}. The fiber W_n is the
   full simplex on 2^{n+1} atoms consistent with coarsening.
   d_n = 1 − (mass pinned to atoms identifiable at stage n) = 1
   at every finite stage. (No atom is "identified" until the limit.)

2. **Ultrafilter charge (CE fails).** Same B_n. Charge concentrates
   on one atom at each stage, consistent along a branch. d_n = 1
   at every finite stage (the concentration point shifts but never
   pins to a specific real). Indistinguishable from fair coin by d.

3. **Geometric (ℓ_n(a_k) = (1-p)p^{k-1}, p < 1).** Mass pinned to
   first atom: (1-p). Tail mass: p^n. d_n = p^n → 0 exponentially.
   CE holds and the rate sees it.

### Why d(S) fails as originally formulated

- d = 1 for both fair coin (CE holds) and ultrafilter (CE fails)
  at every finite stage. Fatal for empirical distinguishability.
- The rate is controlled by the *charges* (how mass distributes
  among atoms), not by the *refinement maps* (which are the same
  in all three examples: dyadic subdivision).
- This is tightness, a classical concept. Not new.

### What the inf-defect sees

Define: d_inf(S) = inf{‖ℓ^pfa‖ : ℓ ∈ W_S}

- Fair coin: d_inf = 0 at every finite stage (the thread that IS
  Lebesgue measure lives in W_n, and it's σ-additive).
- Ultrafilter: d_inf = 1 (every thread consistent with the
  ultrafilter charge IS purely finitely additive).

This discriminates CE/non-CE at every finite stage but is binary
(0 vs 1) — no intermediate rates.

## Astbury (1981) — READ (2026-05-17). Verdict: subsumes the seed.

Astbury, K.A. "Order convergence of martingales in terms of
countably additive and purely finitely additive martingales."
Ann. Probab. 9(2), 266–275.

### What Astbury does

Decomposes every martingale of bounded variation uniquely into a
countably additive martingale + a purely finitely additive (PFA)
martingale (Yosida-Hewitt applied to the associated set functions).
Gives necessary and sufficient conditions for order convergence in
terms of these two components.

### How the seed's objects appear in Astbury

1. **The PFA condition (p. 267, conditions (a)+(b)) IS tail mass.**
   For each ε > 0, ∃σ ∈ θ and D ∈ B_σ with ∫|1_D f_τ| dμ < ε
   for all τ ≫ σ, and μ(E\D) < ε. This is exactly d_n = ℓ_n(T_n)
   — the seed's "fiber defect" restated in martingale language.

2. **Theorem 4.4 settles the rate question — binary.**
   Partitions E into (A, B) where:
   - On A: ∃ positive PFA martingale with lim sup = ∞
   - On B: every PFA martingale order-converges to 0

   No intermediate rates. The PFA component either persists (on A)
   or dies (on B), set by set. This kills the "graded rate"
   hypothesis entirely.

3. **Section 4 (Theorems 4.1, 4.2) constructs PFA martingales
   explicitly** from the directed system using stable sets and
   Lemma 3.1. The construction is structural, not ad hoc.

### What this means for the three sub-questions

1. **PFA-component convergence:** ANSWERED by Astbury. The fibers
   story is a geometric repackaging of his conditions (a)+(b).

2. **inf-defect beyond binary:** KILLED by Theorem 4.4. The (A,B)
   partition is binary at the set level. No intermediate rates
   exist structurally.

3. **Transportation-polytope geometry:** Astbury's framework uses
   directed sets with common refinements but does not quantify
   finite-stage transport-polytope constraints at common
   refinements of incomparable observations. This gap is real
   but too narrow to sustain a seed — it would at best refine the
   finite-stage witness of Astbury's (A,B) partition, not produce
   something structurally new.

### Useful residue

Astbury (1981) is a clean citation for Paper I's CE discussion
alongside Biesel (2024): both confirm that the PFA component as
obstruction to σ-additivity is classical and well-understood. The
Yosida-Hewitt decomposition applied to martingales along
filtrations was already standard by 1981.

## Status: DEAD (2026-05-17)

The seed is dead at two levels:

1. **The candidate claim (d(S) as geometric invariant) collapsed
   to tail mass** — a property of the charges, not the refinement
   maps. Contradicted by concrete computation.

2. **The tail-mass / PFA-component question is subsumed by Astbury
   (1981).** The decomposition, the convergence conditions, and the
   binary (A,B) partition are all in the 1981 paper. No novel
   content remains.

The intuition about resolution-dependent charges and constitutive
width (§§ "The observation" through "What this is NOT") remains
philosophically sound — it is a real feature of the programme's
setup that Zafiris and Biesel don't accommodate. But the
mathematical sharpening attempted here (fiber defect, contraction
rates, empirical CE) does not produce anything beyond classical
martingale theory.

## Post-mortem: interval-charge framework (2026-05-17)

After the fiber-defect route died, explored whether the
*constitutive width* intuition could be sharpened differently:
interval-valued charges with inclusion-compatibility.

### The construction

ℓ_i : B_i → I([0,1]) (closed intervals), with compatibility:
j ≥ i ⟹ ℓ_j(E) ⊆ ℓ_i(E) for E ∈ B_i. Finer observation
narrows the interval — constitutive width shrinks with resolution.

### Kohlas-Casanova (2021) — READ. Does NOT subsume.

"Algebraic Theory of Conditional Beliefs" (Int. J. Approx. Reason.
135:43–76). Framework for imprecise probability: information
algebras with combination (aggregation) and extraction
(marginalization). Compatibility (Definition 23) is EXACT
marginalization: ε_{S_i}(D) = D_i. No inclusion-compatibility,
no directed limits, no σ-additivity, entirely finitary. The
interval-charge construction with inclusion-compatibility is not
in their framework.

### Three theorem attempts — all collapse

1. **"Inclusion-compatible family extends to σ-additive measure iff
   [condition]":** The "iff" condition IS CE restated. Circular.

2. **"Non-trivial contraction produces canonical credal set":**
   Decreasing nested compact convex sets → limit = intersection.
   This is projective limits of compact convex sets (known) and
   credal sets (Lewis 1993, Walley 1991). No new content.

3. **"Contraction rate controlled by refinement geometry":**
   Already killed by the tightness computation (§ "Pre-audit
   computation results"). Adding interval structure doesn't change
   that the rate is controlled by how charges distribute mass, not
   by the refinement maps. Same fatal flaw in different clothing.

### Verdict

Constitutive width is a genuine philosophical contribution: the
observation that width at a given resolution is not epistemic
uncertainty but is constitutive of what observation at that
resolution IS. No precedent found in five traditions checked
(Walley/imprecise, KC/information algebras, Edalat/domain theory,
Choquet/capacities, Astbury/martingales).

But it produces no theorem. Every mathematical sharpening collapses
to known objects. The contribution is expositional — useful for
Paper I and Paper II's framing of why directed refinement matters —
not theorem-producing.

### Pattern (four CE-adjacent seeds killed, 2026-05-15 to 2026-05-17)

1. CE-as-sheaf/gluing → Zafiris + Biesel: dictionary translation
2. Fiber defect / contraction rate → tightness computation: charge
   property, not geometric invariant
3. PFA-component convergence → Astbury (1981): classical, binary
4. Interval-charge framework → three collapses: no theorem

The programme's CE territory is expositional/foundational, not
theorem-producing. The structurally different angles (Vickers/locale
theory, Caramello/Morita equivalence) remain unexplored — these
approach CE from topology/logic rather than extension geometry.
