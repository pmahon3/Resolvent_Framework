# E4 verdict: linearization/extension-screen candidate screen + EPV + W-P rung 1

**Date:** 2026-07-19/20 (E-thread unit 2). **Model:** Opus 4.8, high,
audit-style, fresh context. **Charter:** seed §5 candidate screen + §6 kill
conditions (`notes/unsorted/linearization_extension_screen_seed.md`); handoff
item 7 steps 1–3 (`NEXT_CAMPAIGN_HANDOFF.md`). **Consumers:** E5 / Stage-0
(`SIGMA_LAYER_TARGET.md`, NOT created — DO-NOT holds until this verdict).

Two SEPARATE deliverables (do not conflate — [[feedback_instrumental_seeds]]):
the SEED verdict (promote/absorb/kill on the linearization thread) and the
parked W-P status. "W-P does not promote" is NOT "seed killed."

---

## SEED VERDICT: ABSORB-with-localization

The linearization/extension-screen seed is **INSTRUMENTAL** (inherits
Theorem 2's type); bar = leverage on the parent (a necessary condition, a
candidate pipeline, or a localization). That bar was **already cleared** by
E1/E2 (new corpus-level necessary condition: a σ-essential witness is
non-extendable, value-1 FIP fails at a finite stage ≥ 3; fired on the
Ψ-witness at stage exactly 3). E4's screen decides promote (a live lattice
candidate found) vs absorb (localization banked).

### The screen (seed §5)

Every literature non-extendable state located, tabled by carrier / lattice? /
σ-complete? / DW-wall / FIP-stage:

| Source | Carrier | Lattice? | σ-complete? | Non-extendable state | Note |
|---|---|---|---|---|---|
| DNP 2005 (arXiv math-ph/0311012) Ex 2.2 | MO₄ (10 elts, X=6 pts) | **YES** (MO₄) | **NO (finite)** | 2-valued, no signed-measure extension | finite ⇒ σ-tame; not a witness |
| DNP 2005 Thm 2.3 | X_even (even-card subsets) | rep of MO_{n} | NO (finite) | POSITIVE (all states extend) | the extendable side |
| SDS paper (arXiv:2401.13651) Ex 2.6 | 32-elt difference-closed | **YES (stated: "it is a lattice, 32 elts")** | **NO (finite)** | 2-valued s, no ext over exp S | finite ⇒ σ-tame; not a witness |
| **DNP 2015 (Math. Nachr. 288, 1995–2000)** | difference-closed σ-system | **UNKNOWN — the whole question** | **σ-complete CLAIMED** | 2-valued fails to extend (secondary snippets) | **PAYWALLED; primary text UNVERIFIED** |
| ODL / Order 2022 (stateless SDS-OML) | SDS-closed OML | YES (lattice) | — | state space EMPTY | degenerate; no witness state |
| Pták 2023 (arXiv:2401.13798) | set-repr. point-distinguishing OMP | — | — | every 2-valued state Dirac | positive class; no witness |

**The one live lead — DNP 2015 — stays UNVERIFIED.** Primary text is
paywalled (Wiley HTTP 402); no arXiv/preprint exists (Navara's own
publication list `MNPubl.pdf` [231] gives no PDF). Its σ-complete construction
is claimed, but **whether it is a LATTICE is exactly the unknown**, and I
could not settle it from the primary source. Per the repo's own
hostile-prior-art discipline and [[feedback_verify_by_building]], **UNVERIFIED
≠ a confirmed lattice candidate** — the paywall must not become a guess in
either direction.

### The localization (what the screen banks)

Circumstantial pattern from the ACCESSIBLE neighbours (NOT a proof about DNP
2015's specific object): difference-closed set systems are **generically
orthomodular POSETS, not lattices** — being a lattice is an *extra* hypothesis
on △ (arXiv:2401.13651: "(S,△) is compreg **provided △ is a lattice** … but
there are several compreg **non-lattice** QLs, too"). Every *lattice*
non-extendable example located in print is **FINITE** (MO₄; the 32-elt Ex 2.6)
— hence σ-tame, never a σ-essential witness. The σ-complete constructions rest
on σ-classes (Navara–Pták, "Two-valued measures on σ-classes"), which are
generically set-systems/OMPs. This matches the Ψ-witness's own status (a
σ-complete OM POSET, not a lattice — `sigma_essential_witness.md` Cor 4.4) and
the DW wall.

**Localization banked (seed §5 fallback):** no confirmed σ-complete LATTICE
non-extendable carrier ⇒ *the third engine must act at the SECOND inclusion*
(σ-states catching non-extendable f.a. states), exactly the coarse factor
that Campaigns 11/13 already flagged as the hard one. This is the seed's
intended payoff on an empty screen.

### Why absorb, not kill, and not promote

- **Not kill:** the leverage bar is cleared (E1/E2 necessary condition +
  this localization); [[feedback_instrumental_seeds]] — prior-art is
  bookkeeping, not a kill condition; and a live lead survives.
- **Not promote:** no *confirmed* lattice σ-complete non-extendable carrier.
- **Absorb-with-localization**, with DNP 2015 flagged **ILL / user-bound
  live lead** (relaxed-gate queue): trigger — *if the DNP 2015 σ-complete
  construction is a LATTICE with a non-extendable state, re-audit →
  promote-to-seed into the campaign pipeline.* The thread does not fully
  close; it absorbs with one named live candidate.

Seed §6 kill conditions checked: (a) does NOT fire (E3: the FIP⟺extendable
screen is NOT published — genuine gap). (b) does NOT fire (E1/E2 cleared the
lemma + ✎E1 C2 identification). (c) does not fully fire — the screen is empty
of *confirmed* lattice entries, but the second-inclusion localization is the
surviving sharpened question, so absorb-with-a-live-lead, not close.

---

## W-P STATUS (parked candidate; SEPARATE from the seed verdict)

W-P (`PERSPECTIVITY_WALL_CANDIDATE_2026-07-19.md`) does **NOT promote**;
stays a design heuristic. Two independent signals, same direction:

### Signal 1 — EPV primary source VERIFIED, but mechanism mismatches

Full-PDF read (receipt `EPV_2025_PRIMARY_SOURCE_RECEIPT_2026-07-19.md`).
Both W-P load-bearing claims **CONFIRMED**: (i) the type-I₂ non-extension
DUAL is real and sharp (intro + §6 closing, pp.62–63 — resolves the
discrepancy flag; it was in the body, not the abstract, so the chat was right
and the repo's abstract-fetch simply couldn't see it — **FLAG CLEARED**);
(ii) Prop 3.5 (p.18) = uniform continuity via projection halving + isoclinic
interpolation + symmetry-exchange, exactly W-P's reading. The two ⟦HAND⟧ tags
on W-P's EPV reading are DISCHARGED, and the ⟦HAND⟧ Bunce–Wright/Φ-tameness
comparison can now cite EPV Prop 3.5 + Thm 6.1/6.2 for the positive side.

**But the discharge does not strengthen W-P's witness-shape conjecture.** The
I₂ dual's *mechanism* is **KADISON-ELEMENTARY** (spin factor S₃(C); µ=½ on
rank-one projections forces the linear-algebra contradiction 1/3 = 1/2), NOT
a lim¹/perspectivity-transport phenomenon. So EPV confirms non-extension
lives in the I₂/spin corner, but its SHAPE is the opposite of W-P's
conjectured Hausdorff-gap witness (finite & elementary vs infinite &
cohomological). Only the LOCATION matches (heuristic, already conceded). And
EPV stays JBW\*-only; our concrete Ulam-type carriers are not JBW\* projection
lattices, so EPV neither forces nor forbids anything on them. **EPV cannot
promote W-P.**

### Signal 2 — rung 1: the perspectivity=bond identification FAILS

Receipt `verification/wp_rung1_perspectivity_vs_bond.py/.json` (payload
fa19b0c1, two-seed replay). On the pentagon (E2a build; perspectivity
computed on the abstract lattice = representation-invariant):

> **Perspectivity is NON-SELECTIVE: every atom is perspective to every other
> atom — same-block 15/15 AND different-block 30/30.** (Any incompatible
> "far" atom is a common complement.) This is structural to finite
> homogeneous (Greechie) OMLs, not a pentagon accident.

A relation that relates *everything* cannot faithfully proxy any structured
value-1 bond. W-P §3 identifies perspectivity with the ODBC nerve bond ρ; that
identification **fails** — the two are relations of different type
(perspectivity = Murray–von Neumann *dimensional equivalence*, rank-sensitive;
bond ρ = *state-agreement on a shared boundary*, a measure-type, rank-blind
relation). W-P's witness spec REQUIRES a perspectivity-POOR carrier, which
finite homogeneous OMLs structurally are not.

**No finite object rescues this** — Greechie homogeneity makes every finite
such OML perspectivity-universal (object-hunting for a selective miniature is
rung-2 work, and the selective carrier is exactly the not-yet-built rung-2
infinite lattice). This is *not* a failure of rung 1; it is rung 1's answer.

*Scope honesty:* the script's "bond" is a CO-CHARGING PROXY (both events
value-1 under a common state), NOT the exact ODBC boundary-agreement ρ of
Thm 4.2. The robust, verdict-bearing finding is the perspectivity
non-selectivity (rep-invariant, needs no bond computation). The proxy's
10 "bonded-not-perspective" pairs (all atom↔coatom) are ILLUSTRATION only —
state-agreement is rank-blind where perspectivity is rank-sensitive — and a
near-tautological shadow of atom-universality, not a second refutation
direction and not a theorem about ρ.

### The Stage-0 note W-P owes (name the remainder, at the type level)

Perspectivity does not capture the bond because it is the wrong *type* of
relation: a dimensional-equivalence (rank-sensitive, and on homogeneous
carriers non-selective) cannot proxy a state-agreement bond (rank-blind,
structured by which value-1 charges a section forces to match on a boundary).
Deciding whether *any* perspectivity-vs-bond identification holds requires a
perspectivity-**poor** carrier — the not-yet-built infinite rung-2 lattice.
Until such an object exists and is checked, W-P is a heuristic, never a gate;
a later session must not reject a candidate witness for "perspectivity
poverty."

### W-P disposition

- Rung 1: identification fails (non-selectivity). Rung 2/3: do NOT start
  (require the infinite lattice; object-hunting is scope creep).
- EPV: both claims verified, mechanism mismatched; discharge the ⟦HAND⟧
  tags, keep W-P a heuristic.
- W-P remains PARKED CANDIDATE, downgraded further: not a wall, not a gate,
  identification-refuted-on-finite-carriers, mechanism-mismatched-vs-EPV.
  It stays a *direction* (the σ-scale lim¹ / coarse-factor mood), not a
  constraint. NOT installed into `SIGMA_LAYER_TARGET.md`.

---

## Net E4 outcome

- **Seed:** ABSORB-with-localization ("engine acts at inclusion 2"); DNP 2015
  = ILL/user-bound live lead (promote-on-lattice-confirmation trigger).
- **W-P:** does not promote; heuristic only; EPV ⟦HAND⟧ tags discharged +
  EPV-dual discrepancy flag CLEARED; rung-1 identification fails.
- **Stage 0:** `SIGMA_LAYER_TARGET.md` remains uncreated (DO-NOT satisfied);
  it will gain, when E5 runs, the linearization necessary condition, the
  second-inclusion localization, and the W-P *direction* (as heuristic, not
  a target clause). E5 is the next unit.
