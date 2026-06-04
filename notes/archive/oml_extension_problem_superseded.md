# The Extension Problem for Orthomodular Observation Algebras

> **SUPERSEDED (2026-06-04).** For posing and contextualizing the open
> problem, see the standalone survey
> `notes/open_questions/oml_onboarding.{tex,md}`, which replaces this
> note's problem-statement function. This file is retained as the
> **system of record** for content the survey deliberately omits: the
> PR_lattice/PR_dual "two grades" vocabulary and the Paper II
> PR-correction audit trail (see §"Two grades" / "PAPER II ERROR FIXED").
> Do not extend this note; record new problem-statement work in the survey.

## Problem statement

Let A be an orthomodular lattice with a state s : A → [0,1]
(s(1) = 1, s(a + b) = s(a) + s(b) when a ⊥ b).  The McDonald-
Bimbó dual S₀(A) = (F(A), ⊆, ⊥_A, P(A), T(S)) is a compact
topological space.

Define μ on the clopen ⊥-stable sets CO(S₀(A))† by:

  μ(h(a)) = s(a),     where h(a) = {x ∈ F(A) : a ∈ x}.

**Question:** Does μ extend to a σ-additive measure on the
Baire (or Borel) σ-algebra of S₀(A)?

This is the direct OML analogue of Paper I's stone_measure_exists.

## Why it's hard: the structural obstacle

In the Boolean case (Paper I):
- h : A → Clop(St(A)) is a Boolean algebra isomorphism
- The clopens form a Boolean algebra
- s is finitely additive on this Boolean algebra
- Standard extension (Carathéodory / Choksi) applies
- Compactness gives σ-subadditivity for free

In the OML case:
- h : A → CO(S₀(A))† is an OML isomorphism
- CO(S₀(A))† is an OML, NOT a Boolean algebra
- s is additive on orthogonal pairs only, not arbitrary unions
- **Carathéodory does not apply** — no Boolean algebra of sets
- Compactness holds (Lemma 3.5 of McDonald-Bimbó), but the
  σ-subadditivity argument needs orthogonality structure

The gap: in the Boolean case, "finitely additive on a compact
Boolean algebra of clopens" automatically extends.  In the OML
case, "orthogonally additive on a compact OML of clopen ⊥-stable
sets" does NOT automatically extend — the extension requires
additional input.

## Where Gleason's theorem enters

For the prototypical case A = L(H) (closed subspaces of Hilbert
space, dim(H) ≥ 3):

- Gleason's theorem: every state on L(H) is of the form
  s(P) = tr(ρP) for a density operator ρ
- This gives a σ-additive measure ON THE LATTICE L(H) — the DESCENT
  side only
- It does NOT give the extension to the DUAL S₀(L(H)): that is the
  extension axis, and the clustering argument (entry point #1, "Two
  axes" / "Status of axis (A)" below) shows it FAILS for every normal
  state. Gleason resolves descent, not extension. (The two-axis split
  is exactly what separates "measure on L(H)" from "measure on S₀(L(H))".)

For general OMLs, Gleason-type results are not available even on the
descent side.  The extension problem is the theorem:

**Theorem (to prove or disprove):** Under what conditions on the
OML A does every state s extend to a σ-additive measure on
S₀(A)?

## What's different from the Boolean case

| Feature | Boolean (Paper I) | OML (this problem) |
|---------|------------------|-------------------|
| Dual space | St(A) = ultrafilters | S₀(A) = all filters |
| Distinguished subset | pure(Ω), not canonical | P(A), canonical |
| Clopens | Boolean algebra | OML (non-distributive) |
| Additivity | full (finite) | orthogonal pairs only |
| Extension (to dual) | automatic (Carathéodory) | fails for normal states (#1); Gleason is descent-side |
| Realization constrained? | No | Yes (Kochen-Specker) |

## Two axes: extension and descent (sharpened 2026-06-02)

The bridge from a state on A to a measure on S₀(A) splits into two
distinct axes that the Boolean case fuses but the OML case separates.
S₀(A) is a Stone space (McDonald-Bimbó Cor. 3.7). Its *full* clopen
algebra CO(S₀(A)) is Boolean; the state lives only on the ⊥-stable
clopens CO(S₀(A))† — the OML, = image of h (Thm. 3.9). These share
only meet (∩); join, complement, and bottom all differ (OML bottom
is {ω}, not ∅).

**(A) Extension axis.** Extend the orthogonally-additive set function
μ from the ⊥-stable clopens to a finitely additive charge on the
*full* Boolean algebra of clopens — the classical Boolean extension
problem (Horn-Tarski 1948). Because h preserves meets, a∧b = 0 forces
h(a)∩h(b) = h(0): meet-zero elements map to *disjoint* clopens. So a
charge must satisfy, for every pairwise-meet-zero family {aᵢ},
Σ s(aᵢ) ≤ 1 — a Pitowsky correlation-polytope / Bell-Boole inequality
system. σ-additivity does not help here.

**(B) Compactness.** Once (A) succeeds, the charge extends to a
σ-additive Borel measure automatically (Stone space, compactness gives
σ-subadditivity for free). This step is unconditional.

**The obstruction is meet-zero vs orthogonal (CORRECTED 2026-06-03).**
Earlier this note called axis (A) "the Pták-Pulmannová frontier needing
a new idea." That was wrong. Three strengthening conditions on s
(Pták-Pulmannová 1994, Def. 2):
1. *State* — additive on orthogonal pairs (a ≤ b⊥).
2. *Valuation* — additive on meet-zero pairs (a∧b=0); binary;
   strictly stronger, since meet-zero is coarser than orthogonality in
   a non-distributive OML.
3. *Extends to a Boolean charge* — the n-ary condition Σ s(aᵢ) ≤ 1 for
   every pairwise-meet-zero family; strictly stronger again.

Axis (A) is condition (3). **It can fail for every state.** On MO₃
(three 2×2 blocks pasted at 0,1) all six atoms are pairwise meet-zero,
so orthoadditivity forces the three complementary pairs to sum to 3
while a charge demands ≤ 1 — no state extends. Verified by independent
LP (`verification/mo3_extension.py`, 216-state grid + maximally-mixed: all
infeasible). The maximally-mixed s ≡ ½ *is* a valuation (satisfies (2))
yet fails (3) at {p,q,r} where ½+½+½ = 3/2 > 1. So the obstruction is
the meet-zero/orthogonal gap — **not** σ-additivity and **not**
non-contextuality.

Pták-Pulmannová 1994 Theorem 1 ("unital set of subadditive states ⟹
Boolean") is about the *supply* of valuations, NOT whether a given
state extends — a different statement. Citing it as the extension
obstruction was the error.

**The concrete/non-concrete boundary (CORRECTED 2026-06-03 — earlier
claim refuted).** An earlier version of this section claimed: "for
concrete (set-representable) OMLs the lattice meet is set intersection,
so meet-zero = orthogonal, and (A) reduces to Pitowsky
non-contextuality." **This is false.** A set-representable OMP (P, L)
requires only complement- and *disjoint-union*-closure (Burešová-Pták
arXiv:2401.13798, Def 1.1); intersection-closure is NOT required — it
would force Boolean. The lattice meet a∧b is the greatest L-member
contained in A∩B, so a∧b ⊆ A∩B with equality iff A∩B ∈ L. Hence
*orthogonal ⟹ meet-zero always, but meet-zero ⇏ orthogonal* for
incompatible pairs.

- MO₂ is an explicit concrete logic (P={1,2,3,4}, L = {∅, {1,2}, {3,4},
  {1,3}, {2,4}, P}) where {1,2}∧{1,3} = 0 yet {1,2}∩{1,3} = {1} ≠ ∅:
  meet-zero without orthogonality. Verified independently
  (`verification/concrete_meetzero_vs_orthogonal.py`).
- **MO₃ is itself concrete** (set-representable: it has 2³ ordering
  two-valued states, Gudder's representation theorem). So MO₃ — the
  flagship "meet-zero ≠ orthogonal" example above — is a *concrete*
  logic. The boundary that matters is therefore NOT concrete vs
  non-concrete.
- The real dividing line is a **richness / atomicity** condition:
  meet-zero = orthogonal iff every nonempty A∩B (A,B ∈ L) contains a
  nonzero member of L (sufficient: singletons ∈ L). This property has
  no established standard name (cousins, all distinct: Jauch-Piron;
  Tkadlec "regional"; Burešová-Pták "point-distinguishing"). MO₂, MO₃
  fail it.
- *Terminology trap:* MO₃'s famous non-representability is von Neumann
  *coordinatization* (not a subspace lattice of a projective geometry),
  a different notion from set-representability. Do not conflate.

**Status of axis (A):**
- *Rich/atomic concrete OMLs* (singletons in L, or the weaker
  intersection-richness): meet-zero = orthogonal; (A) reduces to the
  classical marginal / Pitowsky non-contextuality problem.
- *Non-rich concrete OMLs (MO₂, MO₃) and non-concrete OMLs (L(H)):* the
  meet-zero/orthogonal gap is non-empty; (A) is strictly stronger and
  can fail universally.
- *Finite case:* a decidable LP — NOT a structurally resistant frontier.
- *Infinite case* (L(H)): RESOLVED for normal states (entry point #1,
  2026-06-03). A clustering argument inside one 2-plane — k distinct
  lines pᵢ, all pairwise meet-zero, force Σ[s(pᵢ)+s(pᵢ⊥)] = k·s(e) ≤ 1
  for every k — kills any state with s(e)>0 for even one finite-dim e,
  i.e. EVERY normal (Gleason) state. σ-completeness is irrelevant;
  extension is finitary. The argument is analytic (a 1-line deduction
  from orthoadditivity); `verification/lh_infinite_extension.py`
  instance-checks the inequality (finite k, lines in ℝ², charge LP
  infeasible once k·s(e)>1) — it does NOT touch infinite-dim S₀(L(H)).
  The only escapees are SINGULAR states (s(e)=0 on all finite-dim e),
  which exist (ultrafilter vector states, H separable; Calkin pullbacks)
  and form a clean dichotomy with normal states: lift to a functional φ
  on B(H) via Mackey-Gleason/Bunce-Wright (valid — B(H) has no type I₂
  summand), Takesaki gives φ = φ_n + φ_s (both positive, φ_s annihilates
  K(H) — a statement at the φ level, AFTER the lift), and s(e)=0 ∀
  finite-dim e ⟹ ρ=0 by rank-one projections. The density φ_n=tr(ρ·) is
  named by predual duality B(H)_* = trace class, NOT by Gleason. No third
  class (decomposition unique). Hand-verified (foundations cited with
  hypotheses checked, gluing by hand): `verification/lh_singular_dichotomy.md`.
  Whether a singular orthoadditive state extends — meet-zero families now
  infinite-dim subspaces, σ-additivity OF THE STATE the operative
  condition — is the OPEN sliver.

## The descent question

σ-additivity of the state governs *descent*, not extension. Even
once μ extends to a measure μ̂ on S₀(A):

- Boolean: does μ̂ concentrate on pure(Ω)? Answer: iff
  σ-additive. Unconstrained choice of Ω.
- OML: does μ̂ concentrate on P(A)? Answer: ???
  P(A) is part of the structure.  The Kochen-Specker obstruction
  means not all filters can be simultaneously realized.  The
  Bub-Clifton theorem says the state determines a maximal
  Boolean subalgebra of definite values.

So the descent is not a free choice — the algebra + state
together constrain which filters are "realized."

**Caveat on the descent mechanism.** The McDonald-Bimbó duality is
*finitary*. The identity h(∨ₙ aₙ) = (∪ₙ h(aₙ))^⊥⊥ holds for *finite*
joins but is false in general for countable joins — finitary OML
homomorphisms do not preserve infinite suprema. So even the
σ-additivity ⟹ concentration story (the analogue of Paper I's
descent argument) requires additional σ-completeness + continuity
hypotheses that the 2023 duality does not supply. Making the descent
argument rigorous in the OML setting is itself open.

**The finitary-to-σ bridge: open, with three named routes blocked
(entry point #2, 2026-06-03).** Paper I's descent runs on a
*Loomis-Sikorski* engine: σ-additive measures on the Stone space
correspond to σ-homomorphisms off the ideal points, which is what
makes "σ-additive ⟺ concentrates on pure(Ω)" go through. The OML
descent question is whether that engine has an OML analogue — i.e.
whether a σ-complete OML admits a Loomis-Sikorski-type representation
(quotient of a σ-tribe of sets by a σ-ideal) and/or a countable-join-
preserving σ-Stone duality. The literature settles this only for the
*known routes*, all of which are blocked:
- **RDP / effect-algebra route — blocked.** Loomis-Sikorski holds for
  σ-complete MV-algebras (Dvurečenskij, *J. Austral. Math. Soc.* 68(2)
  (2000) 261–277) and for monotone σ-complete effect algebras *with
  RDP* (Dvurečenskij 2005). But a lattice effect algebra has RDP iff it
  is an MV-algebra (Riečanová; Paseka), and an OML that is an MV-algebra
  (all pairs compatible) is Boolean (Kalmbach). So **OML + RDP ⟺
  Boolean** — the RDP machinery has nothing non-Boolean to act on.
- **MacNeille-completion route — blocked.** Harding (*Order* 8 (1991)
  93–103): the MacNeille completion of an OML need not be orthomodular,
  so one cannot complete to absorb countable joins. (Harding notes the
  embed-into-complete-OML question is itself longstanding open.)
- **σ-Stone-duality route — none exists.** McDonald-Bimbó is
  irreducibly finitary (join → biorthogonal hull); their "future work"
  lists only Sasaki operations, no σ-version. Freytes (*Soft Computing*
  24 (2020) 10257–10264) gives an *equational/Hilbert-style* theory of
  σ-complete OMLs but **no** set/tribe representation.
- **Concentration carrier.** In the Boolean case "σ-additive ⟺
  concentrates on points" needs a point space; for OMLs that may not
  exist (Greechie stateless lattices are non-concrete). But this is a
  red herring for the *live* case: L(H) is non-concrete yet Gleason
  hands it a clean lattice measure (non-concreteness no obstacle there),
  and MO₃ is concrete. The genuinely open
  class is **concrete, non-Boolean, infinite σ-OMLs** — where the
  non-concreteness obstruction is *absent* and the RDP argument blocks
  only one route.

**Status of #2: OPEN, not impossible. STRESS-TESTED 2026-06-04 (two
hostile primary-source searches, both MISS — claim survives).** No
impossibility theorem exists for the concrete-infinite-non-Boolean σ-OML
class, and no σ-Loomis–Sikorski / countable-join-preserving σ-Stone
duality exists. Both negative claims survived a deliberate attempt to
overturn them:
- *Impossibility half — MISS.* The only no-go results (Greechie 1971,
  Voráček–Pták 2023 stateless OML, Tkadlec–Svozil two-valued
  nonexistence) are FINITE or two-valued; none bites on a single state's
  σ-additivity for the infinite class. Nothing stronger than
  Pták–Pulmannová 1994 (supply of valuations) surfaced. *Sharpening:*
  the positive side has exactly one occupant, P(H)+Gleason — which is
  NON-concrete (Kochen–Specker: no separating two-valued states, so not
  set-representable). So "concrete" is the load-bearing qualifier; the
  open frontier is precisely concrete ∩ non-Boolean ∩ infinite ∩
  σ-complete, and the closest concrete-σ literature (Navara–Pták
  σ-classes) handles only two-valued states. BF01883240 ("Measures on
  infinite-dim orthomodular spaces") classified: non-archimedean
  generalized-power-series spaces, measures NOT separating — does not
  supply a concrete separating σ-measure, does not overturn the MISS.
- *Duality half — MISS, now from PRIMARY TEXT.* Confirmed directly in
  the source PDFs that BOTH OML dualities take infinite joins as a
  CLOSURE, not a set union: Cannon–Döring `⋁ᵢSᵢ = cls(⋃ᵢSᵢ)`,
  McDonald–Bimbó join `= (⋃h(aₙ))^⊥⊥`. Neither mentions σ/countable/
  Loomis/tribe. RDP route (forces Boolean), MacNeille route (Harding),
  Freytes (equational only) all re-confirmed. *Overclaim guard:* do NOT
  say "no non-Boolean σ-OML is set-representable" — Gudder concrete
  logics are set-representable non-Boolean orthoposets; they are just
  point-ful posets, not a σ-LS universality theorem.
The contribution here
is a *map of the dead routes* — RDP forces Boolean, MacNeille breaks
orthomodularity, MB is finitary — which sharpens "needs a new idea"
into "needs a representation that bypasses all three." The remaining
Phase-4 question (the user's): what minimal σ-completeness + continuity
hypotheses make "σ-additivity ⟺ concentration on P(A)" *statable* for
this class. The fastest route is to re-derive Paper I's descent step by
step and mark the exact step that needs a σ-OML object MB cannot supply.

**The Yosida-Hewitt connection.** De Simone-Navara (2001) decompose
OMP states as s = s_σ + s_wpfa (σ-additive + weakly purely finitely
additive). By the axis split above, the wpfa component governs the
*descent* axis — the analogue of ℓ_p in Yosida-Hewitt — NOT the
extension axis. A natural-looking conjecture ("s extends iff
s_wpfa = 0") is therefore mis-targeted: wpfa = 0 concerns descent
(does the σ-additive state's measure concentrate on P(A)?), while
extension (axis A) is blocked by non-distributivity regardless of
the wpfa component. The decomposition theory and the extension
problem live on different axes.

## Two grades of probabilistic realism (PR_lattice / PR_dual) — 2026-06-03

The two axes above, re-expressed in Paper II's EA/PR/VDR vocabulary,
split "probabilistic realism (PR)" into two grades that the Boolean case
fuses and non-distributivity separates. This is the same extension/descent
split, named in the realism language — NOT a separate construction.

- **PR_lattice(s):** a σ-additive measure on the *lattice* A agreeing
  with s. For L(H), dim ≥ 3, Gleason supplies this for every σ-additive
  state.
- **PR_dual(s):** a σ-additive Borel measure μ̂ on the *dual* S₀(A) with
  μ̂(h(a)) = s(a) that concentrates on the physical points, μ̂(P(A)) = 1.
  This is extension (axis A) followed by descent (the σ-side).

**Settled: a witnessed one-directional SEPARATION (not a proven nesting).**
L(H) normal states *separate* the grades: they clear PR_lattice (Gleason)
and fail PR_dual (entry point #1 — no charge on S₀(L(H)) exists at all, so
a fortiori none concentrating). This is the cleanest statement of #1's
significance in the realism vocabulary, and it dissolves the (a)/(b)
tension over how to fix Paper II: one asserts BOTH grades — Gleason clears
PR_lattice for L(H), and PR_dual fails — suppressing neither.

**NOT settled: the nesting PR_dual ⟹ PR_lattice (audit 2026-06-03).** The
reverse inclusion is NOT free. Restricting a dual measure μ̂ to the
⊥-stable clopens recovers s only as a *finitely* orthoadditive state;
PR_lattice needs σ-additivity on the lattice, s(⋁ₙaₙ)=Σₙs(aₙ). The gap is
μ̂(D), D = h(⋁ₙaₙ) ∖ ⋃ₙh(aₙ), and concentration on P(A) does NOT force
μ̂(D)=0 — because D contains *principal* filters (↑p with p=span(v), v
infinite-support, aₙ=span(eₙ): p ≤ ⋁ₙaₙ but p ≰ aₙ ∀n). Confirmed against
the McDonald-Bimbó primary source: filters carry NO σ-prime condition, P(A)
= principal (not prime) filters; see `verification/mb_primeness_check.md`.
So PR_dual ⟹ PR_lattice needs an extra σ-continuity hypothesis (μ̂ null on
countable-join defects) the finitary duality does not supply — the SAME
finitary wall as #2. Earlier this section wrote "⊋ strict stratification",
which was internally inconsistent with that wall; corrected to
separation-not-nesting. Boolean case: the two grades coincide (Stone gives
μ̂ unconditionally, descent ⟺ σ-additivity), which is why Paper II could
write a single "PR".

**Philosophically secular.** The stratification commits to no metaphysics
about which grade is "the real one": a Born-rule realist reads off
PR_lattice, a relational realist reads off PR_dual, a fictionalist reads
EA. The framework marks the distinctions and serves all three (van
Fraassen's stance). The Whitehead/process reading of "descent to P(A) =
concrescence" is an optional *lens* on why a relational realist privileges
PR_dual — not an axiom in the framework.

**Open (the refined question): does descent do any INDEPENDENT work?**
Every known PR_dual failure is an *extension* failure. In finite dim,
descent is vacuous (only non-principal point is ω, already killed by
s(0)=0; verified `verification/pr_dual_inhabitation.py` — PR_dual on MO₂
collapses to the extension LP). The descent half can be strictly weaker
than extension only in INFINITE dim, where free non-principal filters can
carry mass — and that is exactly where entry point #2 bites: descent is
not rigorously *statable* (MB duality finitary, no σ-Loomis-Sikorski). So:

> **Conjecture / open question (precondition included).** Is there a σ-OML
> regime in which descent is BOTH statable AND strictly weaker than
> extension — i.e. a non-distributive OML + state that EXTENDS to a charge
> on S₀(A) but fails to CONCENTRATE on P(A)? The only candidate is the
> singular-state sliver from #1 (does a singular state that extends
> concentrate?), which runs into the #2 statability wall. The answerable
> meta-frontier is the statability gate (#2), not the witness itself.

If such a witness exists, PR_dual becomes a genuine third grade (clearing
the "new vocabulary" three-statements bar). Until then PR_lattice/PR_dual
is **honest bookkeeping** — a witnessed one-directional SEPARATION (#1, not
a proven nesting), with the descent half not yet shown independent of
extension. NOT claimed as a new theorem.

**Paper II integration is the user's pending call.** Whether to fold the
two-grade vocabulary into Paper II's Commensurability theorem (vs. simply
flipping the L(H) row to "PR fails for normal states") is a
mathematical-architecture decision, not resolved here.

## What's at stake: relational probability without realizations (2026-06-03)

The descent residue (#2) has a motivation beyond technical completeness.
Paper I's finding: *realization* — which points are "real" — is structure
ADDED to a coherent assignment, not forced by it. In the McDonald-Bimbó
setting, realization = concentration on the dual points P(A) ⊆ S₀(A). A
σ-additive probability on a non-distributive OML that does NOT pass through
such concentration would be probability built from the entailment relation
alone — **relational, point-free probability**, the non-Boolean analogue of
the localic (pointless) measures distributivity already permits. This is
the real stake of branch (a) (the σ-OML duality): it is the *engine* for
relational probability without realizations.

**TWO POINT-SPACES — do not equivocate (caught 2026-06-03, advisor).**
"Realization" and "point-free" slide between two different point-spaces:
- **(A)** the rays/vectors of H — L(H) and the Gleason density ρ in
  s = tr(ρ·) are *built from these*.
- **(B)** the MB dual filters P(A) ⊆ S₀(A) — what #1 shows the measure
  fails to concentrate on.

The programme DEFINES realization = concentration on P(A) = **(B)**. But
"no sample space / point-free" means no **(A)**. The L(H) separation
(PR_lattice holds via Gleason, PR_dual fails by #1) shows a lattice measure
need not descend to the **(B)** points — but it does NOT exhibit
point-freeness: Gleason removes (B) while resting ENTIRELY on (A), and is
in fact a *representation* theorem (every lattice state reduces to the point
datum ρ). So **L(H)/Gleason witnesses the SEPARATION, not point-freeness,
and cannot be the existence proof.** Do NOT write "for L(H) we already
built relational probability without realizations; Gleason is the existence
theorem" — it is backwards. The honest claim: the point-free witness must be
BUILT (residue #2), and since L(H)/Gleason does not supply it, #2 is the
*only* candidate engine — which strengthens, not weakens, the case for (a).
(Written into the .tex §"What is at stake".) See
`~/.claude/.../memory/oml_two_point_spaces.md`.

## Prior art and novelty verdict (literature scout 2026-06-03/04)

**Verdict: PARTIALLY OCCUPIED — the precise slot is open.** Every existing
point-free / directed-context construction of quantum probability gives up
exactly one of the three needed properties, landing on one side of the
σ-additivity-on-a-non-distributive-structure line:

- **Gleason tradition** (Varadarajan, Kalmbach, Pták-Pulmannová): σ-additive
  on a non-distributive OML, but real-valued on a FIXED lattice — not
  point-free, not directed-system-built.
- **Döring 2009** ("Quantum States and Measures on the Spectral Presheaf",
  arXiv:0809.4847): point-free measures over the directed poset of abelian
  subalgebras — but provably only FINITELY ADDITIVE (linearity of the
  state), on the distributive Heyting algebra of clopen subobjects.
- **Heunen-Landsman-Spitters / Bohrification** (CMP 2009, arXiv:0709.4364;
  "Bohrification" 2011): point-free quantum probability over the directed
  poset of commutative subalgebras. **VERIFIED 2026-06-04 (read in full):
  their internal valuation IS σ-additive** — a *continuous* (Scott-
  continuous) valuation, μ(⋁↑Uᵢ)=⋁μ(Uᵢ) on directed families (Def 11 /
  Def 6.11). But it factors through an internally DISTRIBUTIVE locale;
  externally σ-additive only PER countably complete Boolean sublattice of
  Proj(A), glued over contexts. Non-distributivity tamed by retreat to
  commutative contexts, not carried natively. (Earlier guess "HLS might be
  finite" was WRONG — flipped on reading. So the distinction is NOT
  "σ vs finite"; it is distributive-detour vs native-non-distributive.)
- **Localic valuations** (Vickers, Simpson, Coquand-Spitters): point-free
  σ-additive (Scott-continuous), but valuations are defined on FRAMES,
  distributive by definition; no orthomodular analogue exists.
- **OML Stone dualities**: TWO finitary ones — McDonald-Bimbó (filter
  spectrum, used here) and Cannon-Döring 2013/2018 (spectral presheaf).
  Both PURELY STRUCTURAL; neither carries a measure on the non-distributive
  dual, neither has a σ-version. (MB chosen over Cannon-Döring because it
  carries P(A) explicitly = the realization datum.)
- Also confirmed: **Abramsky-Brandenburger is finitary** (X,O finite),
  does not see σ-additivity — prior claim verified.

**The unoccupied conjunction (= the descent residue):** point-free ×
σ-additive × NATIVELY non-distributive OML × directed observation system ×
realization (P(A)) as separable structure. Döring gives up σ-additivity;
Bohrification/localic give up native non-distributivity; Gleason gives up
point-freeness. **Novel atom:** the σ-OML representation itself + the
collective-exhaustion extension mechanism delivering σ-additivity
point-free where Döring reaches only finite. The
directed-context→non-distributivity IDEA on its own is NOT new (it is the
shape of Bohrification, and of Gunji et al. 2026 colimit-over-Boolean
generation of OMLs). Novelty gate PASSED conditionally: the slot is open,
but the contribution IS building the σ-duality + proving the theorem — not
the framing. Full record:
`~/.claude/.../memory/oml_relational_prob_novelty.md`.

## Connections

- **Paper I:** the Boolean special case; Stone construction;
  unconditional measure on St(C); descent requires Ω
- **McDonald-Bimbó 2023:** the OML duality providing S₀(A)
- **Gleason 1957:** σ-additive LATTICE measure for L(H), dim ≥ 3
  (descent/lattice level — NOT dual-space extension, which fails for
  normal states, see #1)
- **Bub-Clifton 1996:** uniqueness of definite-value subalgebra
- **Döring-Isham 2008:** topos approach; spectral presheaf; 
  states ↔ measures on presheaf
- **Döring 2009 (arXiv:0809.4847):** measures on the spectral presheaf —
  point-free over directed contexts but FINITELY ADDITIVE; closest rival
- **Heunen-Landsman-Spitters 2009/2011 (Bohrification):** point-free
  σ-additive (Scott-continuous) quantum probability, but via an internally
  DISTRIBUTIVE locale / per-Boolean-context; the canonical occupant of the
  adjacent slot
- **Cannon-Döring 2013/2018:** rival OML Stone duality (spectral presheaf);
  purely structural, no measure on the dual
- **Derr-Williamson 2023:** pre-Dynkin systems; coherent partial
  probabilities; related but different generalization (partial
  precision on Boolean algebra vs full precision on non-Boolean)

## The structural diagnosis (literature audit 2026-05-17;
## RESCOPED to the descent axis 2026-06-03)

**Scope note (2026-06-03):** This section was written before the
two-axis correction and originally read as a diagnosis of the whole
problem. It is correct as a diagnosis of the **descent / σ-additivity**
axis only. The **extension** axis is NOT structurally resistant — it
is the classical Horn-Tarski/Pitowsky problem (see "Two axes" above),
decidable in the finite case. The Pták-Pulmannová result below
concerns the *supply* of valuations, not whether a given state
extends.

**Key finding (descent axis):** Pták-Pulmannová (1994) proves that
conditions strong enough to force σ-additivity on OML states collapse
the OML back to a Boolean algebra.  This is the structural
reason no KVP analogue exists for OMLs on the σ-additivity side.

Specifically: if every nonzero element carries a subadditive state
(unital w.r.t. subadditive states), the lattice must be Boolean (PP
1994 Thm 1, via Prop 2: every subadditive state is a valuation).
This is a statement about the *supply* of valuations across the
lattice — NOT a statement that a given state fails to extend. The
non-distributivity of OMLs is load-bearing on the descent side.

### Why the descent side is harder than "find the right condition"

In the Boolean case, KVP (Fremlin Theorem 391D) gives:
  measurable ⟺ Dedekind σ-complete + weakly (σ,∞)-distributive + chargeable

Each condition is algebraic and non-trivially constraining.  For OMLs:
- Dedekind σ-completeness makes sense but is very strong
- Weak (σ,∞)-distributivity has no clean OML analogue
- Chargeability (existence of a strictly positive finitely additive
  measure) has no known structural characterization on OMLs

The σ-additivity/descent side requires genuinely new ideas, not
adaptation of Boolean techniques. (The extension side, by contrast,
is classical — see "Two axes" above.)

### What the recent literature shows

**Positive results (special cases):**
- Gleason (1957): L(H), dim ≥ 3 — the prototype (lattice-level
  σ-additivity; not dual-space extension, cf. #1)
- Bunce-Wright (1992): JBW-algebras; σ-additivity via
  operator-algebraic structure
- Chetcuti-Dvurečenskij (2003, 2005): lattice effects algebras;
  positive results when the algebra has "enough structure"
  (completeness conditions close to von Neumann)

**Negative/obstructive results:**
- Pták-Pulmannová (1994): unital subadditive → Boolean (the killer)
- Navara (1992): regularity does NOT force σ-additivity on
  general OMPs; Béaver-Cook is special to von Neumann algebras
- Pták (1987): exotic OML state spaces; obstruction is
  combinatorial (Greechie pasting), not from center

**Recent incremental work (2020s):**
- Voráček-Pták (2023): signed measures on OMPs
- Burešová-Pták (2023): variations on regularity conditions
- De Simone-Navara (ongoing): YH-type decompositions for OMPs

**Assessment (descent axis):** The field is active but no one has
found the right condition.  The gap between "too weak" (allows
non-σ-additive states) and "too strong" (collapses to Boolean)
appears structurally robust.  This is not a problem where more
reading will unstick it — it needs a new idea. (This applies to the
σ-additivity/descent axis; the extension axis is classical.)

### Construction tools

All known exotic OML state spaces are built by **Greechie pasting**
(confirmed by Wilce 2009, Handbook of Quantum Logic ch. 24;
Shultz 1974; Pták 1987).  Any progress on the extension problem
likely requires either:
- A new pasting technique that controls σ-additivity, or
- An approach that bypasses the state space entirely (e.g.,
  categorical/topos-theoretic)

## Assessment (rewritten 2026-06-03 to match the two-axis correction)

Once split into its two axes, this is not a single open problem but
a settled axis and an open one.

**Extension axis: largely settled, partly degenerate.** Classical
Boolean extension problem (Horn-Tarski 1948) / Pitowsky polytope
feasibility. Governed by the meet-zero/orthogonal gap, which is
non-empty whenever the concrete representation is non-rich (and a
fortiori in any non-distributive OML). Finite case = decidable LP;
can fail for *every* state (MO₃). NOT a structurally resistant
frontier. Two earlier framings of this axis were mistaken: (i) "the
Pták-Pulmannová frontier needing a new idea" — PP 1994 concerns the
*supply* of valuations, and extension is strictly stronger than the
valuation condition; (ii) "concrete OMLs reduce (A) to Pitowsky
non-contextuality because meet = intersection" — false, since
concreteness requires only disjoint-union closure, and MO₂/MO₃ are
concrete logics with meet-zero ≠ orthogonal (see the
concrete/non-concrete boundary discussion above). The gap closes only
under a richness/atomicity hypothesis, not under concreteness.

**Descent axis: genuinely open, dead routes mapped (entry point #2).**
Whether a measure on S₀(A) concentrates on physical points P(A), and
the analogue of Paper I's "σ-additivity ⟺ concentration," cannot even
be stated rigorously without σ-completeness + continuity hypotheses,
because the McDonald-Bimbó duality is finitary (countable-join identity
fails). The descent argument runs on a Loomis-Sikorski engine; the
three known routes to an OML analogue are all blocked (RDP forces
Boolean; MacNeille breaks orthomodularity per Harding; no σ-Stone
duality exists, Freytes gives only an equational theory) — but NO
impossibility theorem is known for the live class (concrete, non-
Boolean, infinite σ-OMLs). This is the live residue, sharpened from
"needs a new idea" to "needs a representation bypassing all three
blocked routes." See the descent-mechanism section above for the full
route map.

**Infinite extension case: resolved for normal states; singular case
open (entry point #1).** The finite MO₃ counterexample is silent on
L(H), but a clustering argument inside one 2-plane (k distinct lines,
pairwise meet-zero, k·s(e) ≤ 1 for all k) kills every state with s(e)>0
on some finite-dim e — i.e. every normal (Gleason) state. σ-completeness
is irrelevant (extension is finitary). Only singular states (s(e)=0 on
all finite-dim e; ultrafilter/Calkin states) escape the argument; they
form a clean dichotomy with the normal states (Takesaki / Bunce-Wright).
Whether a singular orthoadditive state extends is the open residue.

**The singular discriminator is still OPEN — finite-vs-countable not
settled (corrected 2026-06-04, was over-stated).** The prior handoff
posed "settle finite-vs-countable first: does the singular extension
obstruction get reached with finite or countable meet-zero families? —
that decides whether branch (b) dodges the σ-wall." That is the right
first move and it is NOT yet done. What IS established (per
`verification/lh_singular_dichotomy.md`): for a singular state the
relevant pairwise-meet-zero families are *infinite-dimensional* subspaces
with trivial intersection (not lines), and the line-clustering finitary
kill (`lh_infinite_extension.py`) is *vacuous* there (s(e)=0 on every
finite-dim e). What is NOT established: that the obstruction therefore
requires a *countable* family. A FINITE family of infinite-dimensional
pairwise-meet-zero subspaces with Σs(aᵢ) > 1 is unanalyzed — "the known
finitary route is vacuous" is NOT "the obstruction is provably countable"
(the same blocked-routes-≠-impossible slip the thread is careful about
for #2). So:
- The normal case was settleable because it is finitary (the clustering
  LP); σ-completeness was irrelevant there.
- The singular case loses the LINE-clustering route, but whether a finite
  obstruction exists among infinite-dim subspaces is open. If finite,
  branch (b) dodges the σ-wall and is a self-contained operator-algebra
  problem (Calkin / Bunce–Wright) to attack ahead of (a). If countable,
  (b) is entangled with the same finitary-to-σ bridge as (a).
- **So branch (b) is CONDITIONALLY more tractable**, gated on the
  finite-vs-countable hinge. Settling that hinge is the concrete first
  move — and it is human mathematical work, not yet done.
- *(Earlier "SETTLED = infinitary, both branches gate on the σ-wall" was
  an over-read of the dichotomy file, which calls the extension question
  OPEN; no new math justified the upgrade. Weakened back per the
  weaken-don't-overclaim rule.)*

**Novelty:** The formulation via McDonald-Bimbó duality appears to be
new; identifying the extension axis with classical Horn-Tarski/
Pitowsky feasibility de-mystifies it. For L(H), Gleason gives the
σ-additive measure on the LATTICE L(H) itself, but this lattice-level
rigidity does NOT transfer to the dual: the clustering argument (#1)
shows the passage to a charge on S₀(L(H)) fails for every normal
state. Since extension fails there is no dual measure to descend, so
the descent question does not arise for normal states on L(H).

**Status:** Extension axis settled (finite; infinite L(H) resolved for
normal states, singular case the open sliver — its finite-vs-countable
discriminator still OPEN, so branch (b) is CONDITIONALLY more tractable,
gated on settling that hinge; see the discriminator block above). Descent
axis open, three
known routes blocked (RDP/MacNeille/σ-Stone), no impossibility theorem
(both negatives stress-tested 2026-06-04 against primary sources, MISS).
**Novelty gate (2026-06-03/04): PASSED conditionally** — scout verdict
PARTIALLY OCCUPIED; the point-free × σ-additive × native-non-distributive
slot is genuinely unoccupied (Döring=finite, Bohrification/localic=
distributive, Gleason=not-point-free), but the contribution IS building
the σ-OML duality + σ-additivity theorem, not the framing. Reframed as
the engine for "relational probability without realizations."
Not a current active lead; the bar-clearing work is mathematical (user's).
