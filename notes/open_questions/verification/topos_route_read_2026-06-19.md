# Topos / Bohrification route to a σ-Loomis–Sikorski for concrete OMLs — literature read

*2026-06-19. A machinery/literature read of the topos-quantum-logic programme as a
candidate for route (iii) of `oml_onboarding` §4.3 (a countable-join-preserving,
measure-carrying σ-Stone duality for concrete OMLs). NOT a construction attempt.
Feeds the §4.4 "What the topos route does and doesn't buy" addition in both
`oml_onboarding.{tex,md}`.*

## VERDICT: SAME-WALL-WITH-MACHINERY

The topos route is the one machinery that supplies a genuinely point-free **and**
σ-additive (directed-continuous) valuation on a quantum logic — so it is the
natural candidate to crack route (iii). It does not crack it. In every
construction the σ-additive valuation lives on a **distributive** object, and the
bridge to the non-distributive lattice routes its countable additivity through
**per-context Boolean blocks**. The non-distributivity is relocated into
base-poset variation (`𝒞(A)`) and a coarse-graining map (daseinisation), never
carried by the measure. This is the topos analogue of the universal floor
(faithful set-rep ⟹ Boolean): a measure that meets the non-distributive structure
faithfully forces it Boolean.

It is **SAME-WALL**, not ALREADY-ANSWERED: the programme *sidesteps* the wall (an
internally distributive Gelfand spectrum is a design goal, so constructive Gelfand
duality goes through) — it does **not** prove σ-essential impossibility for
concrete OMLs. The §5 prize stays open, neither inhabited nor closed.

The route ticks **three of four** requirements
(point-free × σ-additive × directed-system-built) and misses **exactly the one
that is the crux**: *native non-distributivity*. "Machinery engages three of four"
≠ "a handle."

## The crux, settled per source (the σ-valuation lives on the DISTRIBUTIVE object)

### Bohrification — Heunen–Landsman–Spitters, "Bohrification" (Deep Beauty chapter, arXiv:0909.3468)

Read from the full PDF text (pdftotext) of "Bohrification". NB: the numbered
results below (Def 6.11, Def 6.17, Thm 6.15, Thm 6.19) are from *this* chapter,
**not** from the companion CMP paper "A topos for algebraic quantum theory"
(arXiv:0709.4364), which has its own numbering — the construction is the same.

- A state on `A` becomes a **continuous probability valuation**
  `μ : O(Σ(A)) → [0,1]_l` on the internal Gelfand spectrum `Σ(A)`, which is an
  internal **locale** — "a compact regular **frame**" (§§2, 6; the frame
  `O(Σ(A))` is "regular", line 824) — hence internally distributive.
- **Def 6.11** (verbatim sense): a continuous probability valuation on a locale
  `X` is a monotone `μ : O(X) → [0,1]` with `μ(1)=1`, modular
  (`μ(U)+μ(V)=μ(U∧V)+μ(U∨V)`), and **`μ(⋁ᵢUᵢ) = ⋁ᵢ μ(Uᵢ)` for directed families**.
  That directed-join continuity **is** the localic / Scott-continuous form of
  σ-additivity — but asked of a *frame*, where `⋁` is distributive.
- **Where the non-commutativity sits:** in the base poset `𝒞(A)` of commutative
  subalgebras (the topos `T(A) = [𝒞(A), Set]`) and the intuitionistic internal
  logic. The valuation never integrates over a non-distributive lattice.

**The apparent counterexample, and its defusal (Theorem 6.19).**
Thm 6.19 gives a bijection between (a) quasi-states on `A`; (b) **probability
measures on `Proj(A)`** — the genuinely non-distributive object; (c) probability
valuations on `P_A`; (d) continuous probability valuations on `Σ(A)`. So it
*looks* like a σ-measure on a non-distributive OML. Two independent defusals:

1. **Primary (σ-essential; concreteness-free).** A "probability measure on a
   countably complete OML `X`" is, by **Def 6.17(a)** verbatim, a map
   `μ : X → [0,1]_l` that "on any countably complete Boolean sublattice of `X`
   restricts to a morphism of countably complete Boolean algebras." So the
   countable additivity is **defined block-by-block on the Boolean
   sub-structure** and glued by naturality over `𝒞(A)`; it never crosses a
   non-distributive (non-commuting) join. This is the **antithesis** of
   σ-essential contextuality — the prize demands contextuality witnessed by the
   countable whole and by *no* Boolean sub-structure, whereas the topos route
   confines *all* its countable additivity *inside* Boolean contexts. (The proof
   of (c)⟺(d) makes this mechanical: "valuations on a compact regular frame are
   determined by their behaviour on a generating lattice.")
2. **Secondary (non-concrete).** The non-distributive object is `Proj(A)`, the
   projection lattice of a (Rickart) C*-algebra — the Gleason/`L(H)`-type lattice,
   non-concrete by Kochen–Specker (no two-valued states at dim ≥ 3). So
   Bohrification **recasts the Gleason occupant** (the top row of the §4.4
   prior-art table) in topos language; it does not reach the concrete class on
   which the open frontier turns.

### Döring–Isham (spectral presheaf) — Döring, "Quantum States and Measures on the Spectral Presheaf" (arXiv:0809.4847); Wolters comparison (arXiv:1010.2031)

Read from the full PDFs (pdftotext).

- **Target distributive.** Measures live on `Sub_cl(Σ)` (= Wolters' `O_cl Σ`),
  the clopen subobjects of the spectral presheaf: "a **complete Heyting
  algebra**" / "a **locale**" (Döring §III; Wolters). Döring §IV.A explicitly:
  `Sub_cl(Σ)` "is **not a Boolean algebra, hence it is not a σ-algebra, either**."
  (Bi-Heyting / co-Heyting structure: UNCONFIRMED in these two sources — Döring
  only states negation is a *pseudo*-complement. Not load-bearing here.)
- **Daseinisation breaks the homomorphism — exactly, and for the structural
  reason.** `δ : Proj(H) → Sub_cl(Σ)` is a monotone coarse-graining, not a lattice
  homomorphism. Wolters (eq. 130–131): outer `δ^o` "**preserves all joins** of the
  projection lattice `P(A)`, **but not the meets. It cannot preserve both, as
  `O_cl Σ` (and likewise `OΣ*`) is distributive, whereas `P(A)` is
  nondistributive.**" Inner `δ^i` "**preserves all meets** of `P(A)`, but
  generally **does not preserve the joins**." Döring's own list: `δ(P∨Q)=δ(P)∨δ(Q)`
  (joins, equality) but `δ(P∧Q) ≤ δ(P)∧δ(Q)`, "not of the form `δ(R)`" (meets, only
  inequality). This is the exact topos twin of the MB finitary wall (Rmk 2.10) —
  *worse* in flavour but structurally the same distributive-target obstruction.
  ⚠ CORRECTION to a stale advisor framing carried in early: daseinisation does
  **not** "break even finite joins" — outer `δ^o` preserves *all* joins; *meets*
  break. Use the source.
- **Why only FINITELY additive.** The operative cause is the **state class**, not
  daseinisation. Döring §IV.B verbatim: type-III algebras "do not possess any
  normal states ... but ... do have physically important states like KMS states.
  ... **As a consequence, the measures we define are finitely additive only in
  general, not σ-additive.**" The measure axiom (eq. 30) is purely modular finite
  additivity `μ(S₁∨S₂)+μ(S₁∧S₂)=μ(S₁)+μ(S₂)`. σ-additivity is recovered only
  **"locally σ-additive"** (eq. 42) — countable additivity for families pairwise
  disjoint *at a single context `V`* — and Corollary IV.2: this holds ⟺ the state
  is normal. Across contexts there is *no* additivity, only monotonicity in the
  poset.
- **The apparent counterexample, and its defusal.** Döring (lines 972–973): "It is
  clear by construction that **m is σ-additive on projections.**" `Proj(H)` is the
  non-distributive object. **Defused:** the σ-additivity is asserted only over
  countable families of pairwise-**orthogonal** projections (eq. 24–25). Pairwise
  orthogonal ⟹ commuting ⟹ single context ⟹ Boolean block. The non-distributivity
  is never exploited; every σ-statement retreats to a commuting/Boolean
  sub-structure. (Same shape as the HLS Def 6.17(a) defusal.)

### Two mechanisms — keep distinct (both reduce to the same wall)

- **Döring:** daseinisation **cannot preserve both joins and meets** because the
  target is distributive and the source is not (Wolters' one-liner). The σ-failure
  is in the *map* into the distributive target.
- **HLS:** σ-additivity is **defined per-Boolean-block** (Def 6.17(a)) and never
  demands a cross-non-distributive-join σ-statement in the first place. The
  σ-content is *fibered over Boolean contexts* and glued over `𝒞(A)`.

Both land on the one wall: **σ-additivity is available only on the
distributive / per-context-Boolean pieces** — exactly where Loomis–Sikorski
already applies ("the first arrow is free"). It degrades to finite additivity
precisely when a single global measure is demanded across the non-distributive
whole.

## The f.a.-vs-σ diagnosis (item 3 of the brief)

YES — the Bohrification colimit hits the programme's finitely-additive-vs-σ gap
**exactly**, and the location is precise: σ-additivity (directed-continuity) is
available *precisely where the object is distributive* (the internal frame; the
per-context Boolean σ-algebras where Loomis–Sikorski holds), and the construction
provides *no* σ-additive valuation on a genuinely non-distributive object. The
gluing/colimit over the context poset does **not** produce a non-distributive
σ-measure object; it relocates the non-distributivity into base variation +
daseinisation/internal-logic and measures the **distributive quotient/target**.
That is the topos analogue of faithful-set-rep ⟹ Boolean — the same wall, reached
with sheaf-theoretic machinery.

## The one finding that would have flipped this — looked for, found the opposite

A σ-additivity statement **crossing a genuinely non-distributive (non-commuting)
join** anywhere in either construction. Both source-reads surfaced the
near-misses ("σ-additive on projections" / Thm 6.19's measure on `Proj(A)`) and
*both* dissolve into per-Boolean-block / pairwise-orthogonal additivity on
inspection. No counter-evidence found. Localic valuations (Vickers, Simpson,
Coquand–Spitters "Integrals and valuations") are on frames = distributive by
definition — same side of the line.

## Sources

- Heunen, Landsman, Spitters, *Bohrification*, in *Deep Beauty* (ed. Halvorson,
  CUP 2011) 271–313. arXiv:0909.3468. (Def 6.11, 6.17; Thm 6.15, 6.19 — the read.)
- Heunen, Landsman, Spitters, *A topos for algebraic quantum theory*, CMP 291
  (2009) 63–110. arXiv:0709.4364. (The companion paper; same construction, own
  numbering.)
- Döring, *Quantum States and Measures on the Spectral Presheaf*, Adv. Sci. Lett.
  2 (2009) 291–301. arXiv:0809.4847. (§III, §IV.A–B; eqs. 24–25, 30, 42; Cor IV.2.)
- Wolters, *A comparison of two topos-theoretic approaches to quantum theory*, CMP
  317 (2013) 3–53. arXiv:1010.2031. (eqs. 130–131; Thm 2.2; Def 4.2, Prop 4.4.)
