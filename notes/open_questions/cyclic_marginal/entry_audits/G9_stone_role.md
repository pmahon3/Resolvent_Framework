# Entry audit G9: Stone's role on D (thm.pointless_not_mixture, thm.repointing_price)

reviewed: false. 2026-10-27. `/audit pure`, THEORY-ITEMS mode, entry-level cap v2.1. Types 3/4 only.
Shelf first: `SHELF_INDEX.json` (no Bhaskara Rao, Phelps, Alfsen, Loomis–Sikorski entries; Burešová–Pták 2024 on shelf),
taxonomy `owned_regions` (own.stone_space_of_logic, own.coherence_extension, own.dravecky_sipos_flight_subcarrier,
own.compressed_threshold, own.ncycle_facets), `stone_role_prior_art.md` + addendum, repo grep (Loomis–Sikorski gap
already recorded for Paper I: `notes/taxonomies_index.json` CE entry; `covered_leads/mixing_barycenter_transfer_rhyme.md`
"P(N) is Krein–Milman-trivial"). Then 5 standard web searches (snippet level only).

Read levels used below: **R** = primary text read this pass; **H** = hand-verified here, textbook location not opened;
**S** = secondary/snippet.

---

## Entry 1: thm.pointless_not_mixture

### Strip the vocabulary

Taxonomy definitions (`obj.trichotomy`, `obj.state`): ideal point = restriction to D of an ultrafilter on Ω, i.e. an
element of ρ(βΩ); pointless = two-valued state on D not in ρ(βΩ). K(D) = finitely additive probability states on D,
pointwise topology.

Let ba₁(Ω) = finitely additive probabilities on P(Ω) and R: ba₁(Ω) → K(D) restriction (continuous, affine).

- (a) ba₁(Ω) = cl conv {δ_U : U ∈ βΩ}, and its extreme points are exactly the ultrafilter 0/1 charges.
  Textbook Krein–Milman + "extreme probability charges on a Boolean algebra are the 0/1 charges"
  (Bhaskara Rao & Bhaskara Rao, *Theory of Charges*; **S**, body not opened, no theorem number claimed).
- (b) Hence cl conv ρ(βΩ) = R(ba₁(Ω)) = **the coherent (power-set-extendable) states on D**. ⟦H⟧ (R continuous affine,
  ba₁ compact, so R(ba₁) is compact convex, contains ρ(βΩ), and lies in cl conv ρ(βΩ).)

So the entry's actual statement is:

> **A two-valued state on D that extends to some finitely additive probability on P(Ω) extends to a two-valued one
> (an ultrafilter).**

Proof in two lines either way ⟦H, checked⟧: the fibre R⁻¹(s) of an extreme s is a closed face of ba₁(Ω), so its
Krein–Milman extreme points are ultrafilters; or the addendum's route (two-valued ⇒ extreme in K(D); Milman's converse:
ext cl conv C ⊆ C for compact C). Both ingredients are textbook functional analysis (Milman converse: Phelps,
*Lectures on Choquet's Theorem*, standard; **H**, location not opened). "Two-valued ⇒ extreme" is the one-line
s(E) ∈ {0,1} squeeze, folklore for dispersion-free states in quantum logic (Gudder 1979; **S**, not located).

The taxonomy already uses this fact silently: `own.coherence_extension` reads "for two-valued states: ideal point =
coherent/extendable; pointless = non-coherent". That identification **is** thm.pointless_not_mixture. The entry adds
nothing over the owned region except the convex-geometric phrasing.

### Pure verdict: **KNOWN (trivial consequence of standard techniques)**

Not UNCLEAR: no owner is suspected and unread; the statement is Krein–Milman/Milman plus the definition of coherence,
and the cap's "nearest prior work read beyond abstract" requirement concerns NOVEL verdicts. The cited textbook
locations are not opened (honest read level: H/S), but the argument is self-contained and checked.

### The "independent failures" clause (split off)

- "At 3×4×4 R4 fails" = a non-binary extreme state of K(D) outside the hull of points. OWNED: `own.compressed_threshold`
  (Sullivant 2006 Thm 2.4; Ohsugi–Hibi 2010), `thm.triangle_hiding_classification` (equivalence owned, 2026-10-26),
  `own.ncycle_facets` / Araújo et al. 2013 Thm 2 (non-deterministic no-disturbance vertices).
- "At 3×4×4 R1 holds" is NOT a general fact about finite carriers (Burešová–Pták 2024 p.6: finite `4even` has a
  non-Dirac two-valued state, **R**). It holds for glued carriers via `fact.finite_alphabet_points` (windows are full
  power sets, Dynkin uniqueness). That id is missing from `uses`.
- So "R1-failure ⇒ R4-failure, not conversely" = (trivial lemma above) + (owned finite non-binary extremes). Correct, not
  new.

### Type 3 / Type 4

- Type 3: **FAIL.** No method transfers; Krein–Milman/Choquet applied in its home setting.
- Type 4: **FAIL.** "Pointless ⇒ outside the mixture hull" is stateable in standard vocabulary ("non-coherent
  two-valued charge"); no new statement.

### Referee estimate: **REJECT-LIKELY** (as a stand-alone claim)
Venue class: none (fine as a remark/lemma in an exposition). Value carried by: none. Main risk: "this is Krein–Milman
plus the definition of coherence."

### Proposed status line
```json
"status": "KNOWN (entry audit G9 2026-10-27): trivial consequence. cl conv rho(beta Omega) = coherent states (Krein-Milman on ba(P(Omega))); entry = 'a coherent two-valued state extends to an ultrafilter' (face argument / Milman converse), already presupposed by own.coherence_extension. Keep as an expository lemma. The finite half (R1 holds, R4 fails at 3x4x4) rests on fact.finite_alphabet_points + own.compressed_threshold.",
"uses": ["thm.triangle_pointless", "own.coherence_extension", "fact.finite_alphabet_points", "own.compressed_threshold"]
```

---

## Entry 2: thm.repointing_price

### Strip the vocabulary

Map e(E) = {s ∈ S(D) : s(E)=1}. Claim: every two-valued state on (S(D), e[D]) is Dirac (owned), and e preserves finite
but not countable disjoint unions. In general: **e is a σ-homomorphism iff every two-valued state on D is σ-additive**
⟦H⟧ (a witness s with s(Eₙ)=0, s(⋃Eₙ)=1 lies in e(⋃Eₙ) \ ⋃e(Eₙ); conversely σ-additivity of all s gives equality).

### Owners

- Re-pointing: **Burešová–Pták 2024, arXiv:2401.13798, Thm 3.1** (**R**, pp.5–6): with S = S₂(P,L), (S,U) is
  SOMP-isomorphic to (P,L) and every two-valued state on it is Dirac. Their stated price is **cardinality** (|S₂| may be
  2^(2^|P|)), not σ. So the σ-remark is not in B–P.
- Loss of countable unions: the **Boolean** case is the textbook Stone vs Loomis–Sikorski gap: the Stone map of a
  σ-algebra is a Boolean but not a σ-isomorphism; Loomis–Sikorski repairs it by quotienting the Baire σ-algebra of the
  Stone space by meagre sets (Sikorski, *Boolean Algebras*; Halmos; **S**: snippet confirmation, arXiv:2402.19235 and
  arXiv:2010.00681 state it, bodies not opened). The programme already hit this wall: Paper I "σ-Loomis–Sikorski
  realization gap" (`notes/taxonomies_index.json`, CE entry).
- The OMP generalisation (S₂ in place of the ultrafilter space) is a verbatim transfer; Navara 1984 and Navara–Pták
  1983 (shelf, read) work exactly with non-σ-additive two-valued states on σ-classes. **Folklore**, not located as a
  stated sentence.

### Misplaced cause (substantive correction)

The witness need not be pointless. Any D containing an infinite disjoint sequence of nonempty sets (D₃ with an infinite
alphabet does) has a **free-ultrafilter restriction**, an *ideal point*, with s(Eₙ)=0 for all n and s(⋃Eₙ)=1. So the
countable-union loss already happens on a Boolean σ-algebra with no pointless states at all. "Pointlessness is relative
to Ω together with the σ-structure of D" overclaims: the σ-loss comes from finite additivity, not from pointlessness.

Honest residue, a dichotomy ⟦H⟧:
- re-point on S₂(D): all two-valued states Dirac, σ-structure lost (already by ideal points);
- re-point on the σ-additive two-valued states S_σ(D): σ kept, but finitely additive pointless states stay non-Dirac.
  On D₃, S_σ(D₃) = the Ω-points (`own.dravecky_sipos_flight_subcarrier`: σ-additive two-valued states on D₃ are Dirac
  on each window and glue to a point). So this branch returns exactly the original scaffold Ω, and the residue
  reduces to "the triangle's pointless states are necessarily finitely additive", which is already recorded and owned
  in that region.

### Pure verdict: **KNOWN (folklore; Boolean case textbook)**

Re-pointing OWNED (B–P Thm 3.1, read); σ-loss OWNED in the Boolean case (Stone/Loomis–Sikorski, snippet level) and a
verbatim transfer to concrete logics; the dichotomy residue reduces to an owned region.

### Type 3 / Type 4

- Type 3: **FAIL.** Loomis–Sikorski transferred to concrete logics verbatim; no new technique.
- Type 4: **FAIL.** "Pointlessness is relative to the scaffold" is the answers-first stance restated; the one new-looking
  sentence (σ-relativity) is wrong as attributed (see above).

### Referee estimate: **REJECT-LIKELY**
Venue class: none. Value carried by: none. Main risk: "Stone representations are not σ-homomorphisms; this is why
Loomis–Sikorski exists."

### Proposed status line
```json
"status": "KNOWN (entry audit G9 2026-10-27): re-pointing = Bureshova-Ptak 2024 Thm 3.1 (read; their price = cardinality); countable-union loss = Stone vs Loomis-Sikorski gap (Boolean, textbook), verbatim on concrete logics. CORRECTION: the witness can be an ideal point (free ultrafilter), so the sigma-loss is caused by finite additivity, not pointlessness. Residue = dichotomy: re-point on S2 (lose sigma) or on S_sigma = Omega-points on D3 (keep pointless states), reducing to own.dravecky_sipos_flight_subcarrier.",
"scope": "two-valued finitely additive states on sigma-classes containing an infinite disjoint sequence of nonempty members",
"uses": ["own.stone_space_of_logic", "own.dravecky_sipos_flight_subcarrier"]
```

---

## Proposed `owned_regions` update (extend the existing region, not a new one)

```json
{
  "id": "own.stone_space_of_logic",
  "name": "Stone space of a concrete logic; re-pointing; convex hull of ideal points",
  "status": "owned",
  "one_line": "Taking S2(D) as points makes every two-valued state Dirac (Bureshova-Ptak 2024 Thm 3.1) but the representation preserves only finite disjoint unions (Stone vs Loomis-Sikorski; witness can be an ideal point). cl conv rho(beta Omega) = coherent states (Krein-Milman on ba(P(Omega))); two-valued states are extreme, so a two-valued state is in the hull iff it is an ideal point (Milman converse). Compatible window families = limit of local Stone spectra (van den Berg-Heunen Prop 8). State spaces of OMLs are arbitrary compact convex sets (Shultz 1974; Navara 1992). NOT owned: the point/ideal/pointless split relative to Omega as a function of the window graph.",
  "detail": "stone_role_prior_art.md; entry_audits/G9_stone_role.md",
  "owned_by": {
    "cite": "Bureshova-Ptak arXiv:2401.13798 Thm 3.1; Loomis-Sikorski / Sikorski, Boolean Algebras; Krein-Milman + Milman converse (Phelps, Lectures on Choquet's Theorem); Bhaskara Rao & Bhaskara Rao, Theory of Charges (extreme charges = 0/1); van den Berg-Heunen 2012; Shultz JCTA 1974; Cannon-Doring 2018",
    "region": "re-pointing of concrete logics; non-sigma Stone representation; convex hull of ideal points = coherent states",
    "verified": "Bureshova-Ptak Thm 3.1 + remarks and van den Berg-Heunen Prop 8 read; Loomis-Sikorski and Bhaskara Rao extreme-charge fact snippet/secondary; Krein-Milman/Milman hand-verified, textbook location not opened; Svozil->Wright 1990 attribution still unverified, do not cite"
  }
}
```

## Bearing on WHY.md

Neither entry is about the loop. Both say that "no point behind a coherent view" is not cured by mixing (convex
hulls of ideal points never reach it) and is cured by re-pointing only at the cost of countable composition. That is a
**hidden idealisation** (finite vs countable additivity), not a circle. The loop-dependent content lives elsewhere
(`thm.triangle_pointless`, the graph classification).

## Unread sources that would sharpen (not change) these verdicts

Bhaskara Rao & Bhaskara Rao (body: extreme charges, Thm 3.2.10); Phelps (Milman converse location); Gudder 1979
(dispersion-free ⇒ pure); Sikorski, *Boolean Algebras* (Loomis–Sikorski section). None is a candidate owner of anything
the entries claim beyond what is stated above.
