# Handoff — invent an intrinsically non-distributive combinatorial primitive

> Historical construction-lane handoff, not the current OML/lattice plan.
> Current navigation: `notes/open_questions/oml_attack/oml_lattice_taxonomy.json`.

*2026-07-01. The one target the whole σ-essential programme now converges on. This is a
HANDOFF PROMPT for a fresh session (or a human working session) to attempt the hardest,
most open-ended move: not evaluating an existing tool, but INVENTING a new object. Read
this whole file first; it front-loads every proven constraint so the swing does not
re-derive dead ground.*

---

## 0. What you are being asked to do (and what would count as success)

**The target.** Invent a combinatorial object — call it a *non-distributive skeleton* —
that is **non-Boolean at its core**: a structure of "contexts" glued along overlaps such
that the gluing itself carries incompatibility (meet-vanishing, not mere comparability),
and along which one could build a concrete σ-complete non-Boolean OML whose global
σ-additive 2-valued thread fails.

**Why this is THE target.** Every road the programme has walked bottoms out here:
- borrowed set-theory combinatorics is BARREN (all Boolean-ambient — see §2),
- the language expresses Ψ but can't dissolve it (Feldman–Wilce σ-completion is an
  ultrapower, destroys concreteness),
- ML is downstream of a construction we don't have,
- and every "glue atomless blocks along [existing object]" attempt died because the
  object was always Boolean.

**Success is NOT "solve Ψ."** Success is one of:
- (a) **a genuinely new object** whose skeleton is provably non-Boolean (meet-vanishing
  incompatibility native to the gluing), stated precisely enough to check against the
  razor (§3) — even if whether it yields a witness stays open;
- (b) a **precise impossibility**: a proof that no such native-non-distributive skeleton
  can exist (which would be real progress toward ¬Ψ, currently NOT earned);
- (c) an honest **"here is exactly the definitional obstruction to even stating such an
  object"** — a located wall, not a vague "couldn't."

A plausible-looking construction that hides the wall is a FAILURE. A clean "dies here,
this is why" is a SUCCESS.

## 1. The problem, minimally (so you can attack without the whole corpus)

Ψ: does there exist a CONCRETE σ-complete non-Boolean irreducible orthomodular lattice
(OML) `L ⊆ P(Ω)` (closed under complement + countable DISJOINT unions; blocks = maximal
Boolean subalgebras overlap but their union is non-Boolean), with a 2-valued state `s₀`
on a finite ⊥-closed subposet `B` that extends to NO global σ-additive 2-valued state on
`L`? The witness `Ω` must be uncountable and non-Polish/non-standard-Borel.

Reduces (PROVED, Lean `localization`) to **Wall A**: with clause (i) freely arranged
(Navara–Pták), a witness ⟺ no non-Dirac σ-additive 2-valued state extends `s₀`.

## 2. THE RAZOR — the one test every candidate must pass (do not skip)

A σ-additive 2-valued state `s` has a true-set filter `ℱ_s = {A : s(A)=1}`. `ℱ_s`
assembles into an actual SET only if it is **meet-closed**. Off-Boolean, meet-closure
FAILS (MO₂: atoms `a,b` have `a∩b≠∅` as sets but `a∧b=0` in the lattice, so
`s(a)=s(b)=1` yet `s(a∧b)=0`). Consequence, verified from two independent directions
(gap-kill Check 2 + the full catalog scout):

> **Every BOOLEAN-AMBIENT combinatorial obstruction blocks a separating/uniformizing
> SET or FUNCTION — and a non-Dirac σ-state routes around it (rescuer), exactly as a free
> ultrafilter routes around a Hausdorff gap. To block a σ-additive 2-valued STATE you need
> a NON-meet-closed coherent {0,1}-assignment across INCOMPATIBLE contexts = a
> non-distributivity phenomenon.**

**THE RAZOR:** your invented object is viable ONLY IF its characteristic obstruction is
intrinsically about a **non-meet-closed {0,1}-coherent assignment** (state-shaped), NOT a
separating/uniformizing set/function (set-shaped). Set-shaped ⟹ rescued ⟹ dead.

Positive control: **Kochen–Specker** passes the razor (genuine state-obstruction) — but is
Ψ-excluded (non-concrete/L(H)/finite, Wright-covered). So a real state-obstruction is
intrinsically non-distributive and does NOT come from the P(ω)/fin catalog. Your object
must be KS-flavored (non-distributive) but concrete, σ, and infinite-witness.

## 3. What is DEAD — do NOT re-propose (each is logged, primary-source or Lean-certified)

- **Every set-theory catalog object as a skeleton** (MAD families, ladder systems /
  non-uniformizable colorings, Suslin/Aronszajn trees, Todorcevic walks/coherent
  sequences, the whole gap spectrum incl. analytic/tight, towers). ALL Boolean-ambient,
  ALL fail the razor, for ONE reason (a maximal coherent {0,1}-assignment in a Boolean
  ambient is an ultrafilter = meet-closed by definition). `fact.catalog_barren`.
- **Segregated carriers** (∏ₙMO₂, MO_κ, horizontal sums): contextuality on a central
  Boolean factor ⟹ σ-states concentrate on points ⟹ Dirac-only ⟹ extends. A witness must
  be irreducible / non-central.
- **Finite-block / Greechie / linear-chain**: finite blocks ⟹ S_df^σ = S_df, no phantoms.
- **Band families** (AD-indexed with the specific closure): dichotomy ∪-closed⟹Boolean /
  not⟹not-a-lattice. Lean-certified (`band_family_dead`).
- **Atomless blocks + COUNTABLE gluing of Polish measure algebras**: stays
  Polish-representable ⟹ DW D.6 kills it. *(s13: kill needs D.6's binding
  inner-regularity leg too — holds here per-instance only if blockwise
  restrictions are compactly witnessed; verdict Addendum s13.)*
- **Any construction that EXHIBITS a global σ-additive 2-valued state extending `s₀`**:
  that state is a RESCUER (polarity gate, Lean `builds_state_implies_not_witness`). The
  witness is a NON-existence — you must show no extension EXISTS, not build one.
- **The disjointification identity `(a∨b)∧a⊥=b∧a⊥`** is FALSE on OMLs; any step needing it,
  or needing `L` intersection-closed, Booleanizes and dies (Lean `costume_kills_witness`).
- **Filter-shaped largeness primitives** (ultrafilter transcription / quantum filter /
  embedding j:V→M / weaken-ultra): all bottom at the wall (`fact.filter_space_exhausted`).
- **¬Ψ invariants** (commutator-degree / σ-cohomology / definability rank / graded RDP):
  no attackable invariant, each = wall-renamed or definability-non-sequitur
  (`fact.invariant_space_exhausted`).

## 4. The one OPEN cell + the exact shape of what is needed

- **Open cell:** `open.atomless_uncountable_AD` — atomless blocks, UNCOUNTABLE-AD gluing,
  non-Polish, non-segregated. Killed by neither the DEAD-list nor the Luzin collapse
  (atomic-only). But its combinatorial ROUTE-IN is barren (§2/§3) — so a witness here needs
  a skeleton that is NOT a borrowed catalog object.
- **The exact requirement (the sharpening that IS this handoff's reason to exist):** the
  non-distributivity must be **NATIVE TO THE SKELETON**. You cannot glue a non-distributive
  object along a Boolean (meet-closed, hence rescued) skeleton and get the obstruction —
  skeleton and non-distributivity are inseparable. So the invented object's *index/gluing
  structure itself* must have meet-vanishing incompatibility, not just its fibers.

## 5. Concrete starting angles (not solutions — disciplined places to push)

Each is a HYPOTHESIS for where a native-non-distributive skeleton might come from. Attack
adversarially with the razor at every step.

1. **A "quantum" analogue of an AD family / gap.** Existing AD families live in P(ω)/fin
   (Boolean). Is there a coherent notion of an almost-disjoint / gap structure valued in a
   NON-distributive effect algebra or OML — where "almost-disjoint" means orthogonality in
   the lattice, and the "gap" is a non-meet-closed coherence? (Razor check: does its
   obstruction block a state or still a set?)
2. **The test-space / manual side (Foulis–Randall) as the skeleton generator.** Effect
   algebras/manuals make context+incompatibility PRIMITIVE (survey §3s: they natively give
   #1). Can a MANUAL (a hypergraph of overlapping operations) be built whose LOGIC is a
   concrete σ-OML with the required non-central incompatibility — i.e. build the skeleton
   as a manual, not as a set-family? Feldman–Wilce σ-orthosum is intrinsic here (unique).
   The open q: can such a manual be CONCRETE and non-Polish without its σ-completion going
   abstract (ultrapower)?
3. **Contextuality-native combinatorics (Abramsky–Barbosa partial Boolean algebras).**
   pBAs are the base grammar (survey §3s: #1/#2/#5 native). Is there an UNCOUNTABLE pBA
   whose gluing is a genuinely non-commeasurable (incompatible) uncountable structure —
   a "large pBA" — carrying a σ-structure? This is the closest existing home for
   "non-distributive at the skeleton"; the question is whether it can be pushed to
   uncountable + σ + concrete.
4. **A new primitive from scratch:** define an abstract "incompatibility skeleton" (a set
   of contexts + a symmetric non-transitive compatibility relation + overlap data) with
   its OWN closure/coherence axioms designed so that (a) finite patterns extend locally
   (Wright), (b) a global σ-additive 2-valued coherent selection is blocked by the skeleton
   itself, (c) it does NOT reduce to a Boolean ambient. Then ask: is it inhabited? Is it
   concrete? This is the frame-change / new-primitive act in its purest form.

## 6. Discipline (non-negotiable — this is where self-deception lives)

- **Run the razor on EVERY candidate.** Set-shaped obstruction ⟹ rescued ⟹ dead. No
  exceptions; the whole session died here repeatedly.
- **Polarity:** if you find yourself BUILDING a global state, you built a rescuer, not a
  witness. Stop.
- **Boolean-ambient check:** if the skeleton lives in P(ω)/fin, 2^κ, or any tree/lattice
  that is distributive, it is meet-closed and dead. The skeleton must be non-distributive.
- **Concreteness vs abstract:** an ultrapower / free construction / abstract completion
  that "has" the σ-structure but whose points are equivalence-classes is NOT concrete (=
  Feldman–Wilce hinge, dead for inhabitation). The object must be literal sets, or provably
  set-representable, at the σ-level.
- **Strength honesty:** consistency strength is UNKNOWN both directions. Do NOT assume
  measurable-cardinal strength is needed (LB refuted §3f) NOR that it is not (UB unearned).
  If your object needs a large cardinal, say so and flag forcing is the WRONG engine
  (Lévy–Solovay, strength-preserving).
- **Flag ⟦HAND⟧ on all novel construction; ⟦HAND — unverified⟧ when load-bearing.** Verify
  by building the smallest instance and reading primary sources, not by grep/summary.
- **Advisor before committing to an approach and before declaring done.** Sharpen guardrail:
  do not relabel a death as a refinement.

## 7. Pointers (load on demand, not upfront)

- Zoom-out: `notes/open_questions/sigma_essential_taxonomy.json` (99 entries; `$meta.the_shape`).
- Full attack record: `notes/open_questions/sigma_essential/sigma_essential_large_cardinal_bounds.md`
  §3k–§3s; construction swings: `notes/open_questions/sigma_essential/sigma_essential_construction_runs.md`.
- The razor + catalog scout: construction_runs.md (2026-07-01 sections).
- Language inventory (pBA base grammar, Feldman–Wilce, the 5 primitives): bounds §3s.
- Lean scaffold (Wall A open-prop, detectors, Ψ pinned): `SigmaEssentialOpenCore.lean`
  (§8–§9 = the σ-gap + `psi_iff_concreteSigma`); `SigmaEssentialConjectures.lean`
  (`IntrinsicK`, costume-detector). PDF: `feldman_wilce_1993.pdf` in the lit library.
- Authoritative state: `notes/programme/program_overview.md` (2026-07-01 block).

## 8. The honest frame (read last, hold throughout)

This is the "invent a new world" act from the how-do-humans-do-math thread: reconceive the
ambient so the object is forced (the forcing/hyperreals/schemes pattern), not search the
existing space harder. It may not succeed — genuinely-new primitives are rare and the
"new-world" and "impossibility" branches are currently INDISTINGUISHABLE on evidence
(uniform bridge-collapse points at both). The value of the swing is: either the object, or
a precise located obstruction to even stating it, or an impossibility. All three are real.
Do not manufacture a fourth (a plausible object that hides the wall). The convergence of
every road onto this one target is itself the finding that earns the swing.
