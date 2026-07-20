# Candidate constraint W-P: the perspectivity-transport obstruction (PARKED)

*Parked Stage-0 companion, NOT installed into `SIGMA_LAYER_TARGET.md`
(which must not exist until E4's verdict — session DO-NOT). Provenance:
LLM-derived (Claude, in chat) 2026-07-19, synthesising three in-repo
threads (the ODBC nerve `oml_distributed_boundary_compactness.md`; the
σ-nerve/torsor/lim¹ material — PARKED/ABSORBED 2026-07-18, keeper
`oml_odbc_sigma_nerve_absorption.md` on the `explore/c-sigma-nerve`
branch, NOT present on this branch; the reconstruction winding/ring-parity
results) against Escolano–Peralta–Villena (arXiv:2509.03213, 3 Sep 2025)
and von Neumann continuous-geometry perspectivity theory.*

**⚠ STATUS — CANDIDATE, NOT A WALL.** Every mathematical claim here is
⟦HAND — one-read, UNVERIFIED⟧. In this repo "wall" = a proven no-go
(Derr–Williamson). W-P is NOT that. Two independent reasons it is
downgraded to *candidate*:

1. **EPV does not constrain our carriers.** EPV is a theorem about
   **JBW\*-algebra projection lattices**. Our carriers are concrete
   σ-class OMLs that are *not* projection lattices of any JBW\*-algebra
   (no Jordan U-operators — the chat concedes this). So EPV neither
   forces tameness on them nor forbids anything on them. The
   "uniform-continuity wall" and W-P are conjectures about a
   hypothetical **Jordan-free lattice analogue** of EPV that *would*
   reach our carriers — and that analogue is admittedly OPEN. Nothing
   here is a proven necessary condition on the witness yet.
2. **The load-bearing mechanism is unverified.** Only the POSITIVE EPV
   direction is confirmed against the primary source (abstract, this
   session): "if 𝔍 contains no type I₂ direct summand, every bounded
   finitely additive measure μ: 𝒫(𝔍) → X admits an extension to a
   bounded linear operator." The two claims W-P leans on — (a) the I₂
   non-extension DUAL (every type I₂ JBW\* algebra carries a
   non-extending positive fa measure) and (b) Proposition 3.5 /
   uniform-continuity-via-halving-and-isoclinic-geometry as the proof
   engine — are **NOT in the abstract**; they are the chat's structural
   reading of the body. They must be verified against the full PDF (an
   E1-style fresh-context read) before any of §2–§7 hardens.

If either downgrade reason survives E4's check, W-P stays a design
heuristic, not a gate, and a later session must not reject a candidate
witness merely for "perspectivity-poverty."

## 1. Why the constraint is even plausible (the external result)

EPV (2025) settled Mackey–Gleason–Bunce–Wright for JBW\*-algebras on the
**positive** side (verified): no type I₂ summand ⇒ every bounded fa
measure on the projection lattice extends to a bounded linear operator —
a tameness-forcing theorem *inside JBW\* algebras*. The chat's reading
(UNVERIFIED) adds a dual I₂ non-extension result and reads the engine as
uniform continuity from projection-halving + isoclinic interpolation. IF
those hold and IF a Jordan-free analogue exists, the consequences below
would follow. Provisional consequences (all conditional):

- Witness lives in the **I₂-rich** locus (spin-factor / MO₂ fibre) —
  the summand the positive theorem excludes. Corroborates the campaign's
  centre-free / activation requirements — but note this is corroboration
  of a *heuristic direction*, not a new proven constraint.
- Witness cannot be a **finite-additivity** phenomenon *if* a Jordan-free
  MGBW analogue closes the bounded-fa question for lattice carriers.
  Consistent with the Campaign-11/13 obstructions and the gap-cohomology
  / derived-limit reading of the σ-stage — again, conditional.

## 2. The mechanism, geometric → order-theoretic (⟦HAND⟧)

EPV engine (per chat, UNVERIFIED — this is the Prop-3.5 claim E4 must
check): bounded fa measures on no-I₂ JBW\* projections are **uniformly
continuous**, produced by **projection halving + isoclinic
interpolation** (norm-close projections bridged by a third isoclinic to
both via small-motion symmetry). "Jaggedness" = failure of this.

Order-theoretic translation (classical von Neumann side — SOLID; the
*equation to the EPV engine* — ⟦HAND⟧): a symmetry-exchange is a
**perspectivity** `p ~ q` iff `∃ c: p ∨ c = q ∨ c = 1, p ∧ c = q ∧ c = 0`;
halving = two perspective pieces summing to 1; isoclinic interpolation =
a bounded-length perspective chain. So *geometric richness = perspectival
richness*, the lattice heart of Murray–von Neumann dimension theory.

> **W-P (local form, CANDIDATE). The carrier is PERSPECTIVITY-POOR:
> elements equal in size under every available measure, close in the
> lattice, joinable by NO short perspective chain, the failure being
> structural (no hidden complement rotates one into the other).**

## 3. Where it would live at the σ-scale (CONDITIONAL on §5)

Local perspectivity-poverty would be necessary-not-sufficient. The
σ-form rests on ONE identification, which §5 gates:

> **Claimed (⟦HAND⟧): perspectivity IS the nerve's bonding transport.**
> In the ODBC nerve (`oml_distributed_boundary_compactness.md`: blocks
> `B ∈ I`, fibres `Y_B(p,μ)`, bonds `ρ^K_J` on `X_p(J)`), perspectivity
> would be the mechanism carrying a state-value between overlapping
> blocks; abundant perspectivity = forced agreement = trivial gluing =
> tameness.

> **W-P (σ form, CONDITIONAL). The perspectivity-transport system over
> the block nerve is COUNTABLY CONNECTED but ω₁-OBSTRUCTED: every
> countable subfamily of blocks perspectivity-connected (no finite
> obstruction — a Jordan-free EPV analogue would see only local
> tameness), while the whole ω₁-system carries a twist no global
> perspectivity trivializes** — a nonvanishing lim¹ of the
> perspective-transport system, the twist a ZFC-nontrivial class
> (Hausdorff gap / nontrivial coherent sequence).

## 4. Corroborations (why it is convergence, not coincidence)

- **Two-scale identity with reconstruction.** Winding + ring-parity
  already show local transport composing nontrivially around a finite
  cycle; perspectivity carrying a residual twist around an ω₁ loop is the
  same shape one cardinal up.
- **I₂ from the lattice side.** MO₂ is the minimal lattice where two
  elements are perspective in more than one way (a circle of common
  complements); that multiplicity is the freedom a nontrivial transport
  needs. So "I₂-rich corner" (EPV heuristic) and "twist-carrying
  perspectivity" (W-P) are the same requirement — IF §5 resolves whole.

## 5. THE gating check (necessary vs sufficient) — resolve FIRST

The §3 identification **perspectivity = full nerve bonding constraint `ρ`**
is load-bearing and unverified:

> **Does perspectivity between two blocks capture the ENTIRE bonding
> constraint, or only part?** If blocks `B, B'` can share a compatible
> state-value (agree under some section in `X_p(·)`) WITHOUT their
> relevant projections being perspective, perspectivity transports
> strictly LESS than the fibre bond.

- **If perspectivity = whole bond:** §3 is the witness spec; build the
  twist into inter-block perspectivities (never inside a block —
  in-block perspectivity is Boolean/rigid; matches the import-sweep law).
- **If perspectivity = only part:** W-P(local) is at most a necessary
  heuristic; the twist rides the REMAINDER of the bonding map, which
  becomes a newly named object one notch above perspectivity — that
  naming becomes the Stage-0 deliverable.

§5 gates whether §6 measures the right thing.

## 6. Finite calibration (cheap, self-falsifying) — after §5

Every finite sub-nerve must be perspectivity-connected: (i) a
perspectivity-disconnected finite sub-nerve would be refuted at finite
scale; (ii) worse, it would be finitely tame for free (finite ⇒
orthogonal families finite ⇒ St_fa = St_σ), so never the witness. Run:
on the pentagon and the amended product-Ulam Ψ-witness, compute the
perspectivity relation on projections, confirm finite/countable
connectivity, and locate the first stage where a countably-existing
perspective bridge fails to close (the finite shadow of the ω₁ twist).
Receipt alongside the existing `X_p(J)` and E2a/E2b calibrations. NOTE:
this calibration is only meaningful once §5 says perspectivity is (all
or the relevant part of) the bond.

## 7. What it would change in the pull-document (IF promoted)

Only after E4 verifies EPV's I₂ dual + Prop 3.5 AND §5 resolves: replace
any "carrier must be non-Polish / jagged" mood-statement with the
operational target *perspectivity countably connected but ω₁-obstructed,
obstruction class in the perspective-transport lim¹, twist in the
inter-block identifications* — which would subsume Derr–Williamson (a
perspectivity-poor coarse-riding carrier is automatically non-Polish)
while being strictly more specific. Until then: heuristic only.
