# Paper II audit verdict — "Distributivity and the Commensurability of EA and Realism" (2026-06-23)

Two-pronged hostile audit (proof-correctness + cross-field prior-art), same method
that retired the note and parked Paper I. **Overall: REVISE — the SURVIVOR. The
central math is SOUND.** No fatal error, no retirement. Blocking fixes are
honesty/citation/scoping, not a broken proof. Consistent with CLAUDE.md (Paper II
= the strongest contribution zone), and the surviving contribution is the
**Type-6 bridge** (McDonald–Bimbó OML duality ↔ van Fraassen realism debate), not
Type-1/Type-4.

## Prong 1 — proof correctness

### CROWN JEWEL: the clustering argument (PR_dual fails for L(H)) — SOUND, with a notation bug
The central novel impossibility ("no normal state on L(H), dim≥3, extends to a
charge on the dual S₀(L(H))") is mathematically CORRECT under the forced reading.
Independently verified (auditor + advisor): fix 2-dim e; s(p_i)+s(e⊖p_i)=s(e) by
orthoadditivity; the 2k lines {p_i, e⊖p_i} are pairwise meet-zero when distinct
(generic, avoidable coincidences); h preserves meets so images are disjoint MOD the
improper filter ω, which is PINNED to measure zero by μ(h(0))=s(0)=0; so k·s(e)≤1
for all k ⟹ s(e)=0 ⟹ no normal state. **This is genuinely UNLIKE Paper I's phantom
points — there the shared abstract point had no pin; here s(0)=0 pins it.** Hence
the σ-LS failure mode does NOT recur in the crown jewel.

BUT two write-up defects (blocking / fixable):
- **`p_i^⊥` NOTATION (footnote ~line 451) — BLOCKING.** Under the standard L(H)
  reading p_i^⊥ = I−p_i, the key equation s(p_i)+s(p_i^⊥)=s(e) is FALSE (gives 1,
  not s(e)) and disjointness fails. The only coherent reading is "orthocomplement
  WITHIN e" = e⊖p_i. Must rewrite as e⊖p_i / add the genericity remark.
  RECOMMENDED (advisor): REPLACE the bespoke footnote with a citation to standard
  KS/Pitowsky non-extendability — sidesteps both the notation bug AND the
  low-novelty-of-the-argument issue; more honest (you USE the impossibility, don't
  claim it). Parallels the Paper-I Choksi call.
- **"no charge on S₀(L(H)) exists" (lines ~591, 612) — OVERSTATED.** Charges exist
  (Diracs). Proven claim = "no charge EXTENDING s." Line 447 already correct; bring
  591/612 into line.

### NOVELTY of the impossibility: LOW. It is KS/Pitowsky non-extendability in MB-dual
dress (the clustering inequality Σs(p_i)≤1 over meet-zero lines IS a Pitowsky 2-dim
inequality; paper half-admits via its own Pitowsky cite). Claim the PR_lat/PR_dual
SPLIT as the contribution, not a new theorem.

### INHERITED DEPENDENCY (Paper-I biconditional) — REAL, CONFINED, + a session-created bug
Paper II imports from mahon2026 the biconditional "μ̂(pure(Ω))=1 ⟺ each ℓ_i
σ-additive" UNCONDITIONALLY (lines 196–197, 222, 564–565) + "free in the Boolean
case" (515, 535–536, 548, 566). The FORWARD direction was just found broken in
Paper I (needs σ-LS realization) AND **Paper I was corrected THIS SESSION to state
it realization-conditionally.** So Paper II now MISREPRESENTS ITS OWN CORRECTED
CITED SOURCE — the exact stale-cross-reference failure. **BLOCKING: hedge these to
match corrected Paper I.** The crown jewel does NOT depend on it (self-contained),
so the central result survives; only the Boolean-half framing needs hedging.

### Ladder / other claims — FINE
EA⟸PR_lat⟸(∗)PR_dual⟸VDR directions correct; VDR⟹PR_dual (Dirac) right;
PR_dual⟹PR_lat correctly hedged conditional via (∗); "witnessed separation not
proven nesting" honest. Horn–Tarski/Pitowsky extension-axis footnote apt. Boolean
(c)/VDR (ultrafilters=2-valued homs) fine.

## Prong 2 — prior-art / novelty
- **EA/PR/VDR trichotomy:** FOLKLORE-ADJACENT. Pieces owned (van Fraassen modal
  dynamical/value state = PR/VDR split; Beltrametti–Cassinelli 1981 statistical vs
  dispersion-free states = the math source — SHOULD CITE). The nested named axis
  indexed by distributivity is not assembled before.
- **Distributivity-as-axis:** OWNED (Stairs 1983, Putnam–Dummett, Bub–Pitowsky
  2010 — paper concedes).
- **PR_lat/PR_dual split:** PARTIALLY OWNED by **Döring 2008 (arXiv:0809.4847)** —
  his states↔measures-on-Sub_cl(Σ) = PR_lat; "no global sections = KS" = PR_dual
  impossibility. Differentiators REAL (Döring finitely-additive/no σ-additivity
  separator, spectral presheaf not MB, no van Fraassen) but they support PACKAGING
  novelty, NOT a new-distinction claim. **CITING + DIFFERENTIATING DÖRING 2008 IS
  BLOCKING — the single largest gap (scout). Inverted note-lesson: there the killer
  was in the paper's OWN bib (FHM); here the overlapping work is MISSING from the
  bib.**
- **Clustering impossibility:** OWNED (KS/Pitowsky).

## Contribution bars
- Type 1/2 (theorem/proof): FAIL — impossibility is KS/Pitowsky.
- Type 4 (vocabulary): WEAK — three-statements test marginal (4th condition, a
  non-trivial RESULT enabled by the vocab, is thin). **DROP the Type-4 lean** —
  splitting across weak-Type-4 + strong-Type-6 invites the stricter bar.
- Type 6 (exposition/bridge): **CLEARS, real, defensible.** MB (2023, Math Logic
  Quarterly) totally disconnected from van Fraassen; bridging them with Gleason/KS
  for a philosophy-of-physics audience is non-trivial assembly across distinct
  communities (quantum logic / topos physics / modal interp / phil sci). Rest the
  contribution HERE, full stop.

## Required actions
**BLOCKING (any submission):** (1) fix p_i^⊥→e⊖p_i, or better REPLACE footnote with
KS/Pitowsky citation. (2) Cite + differentiate Döring 2008. (3) Hedge the inherited
biconditional + "free in Boolean case" to match corrected Paper I (mahon2026).
(4) Scope "existing treatments do not isolate the σ-additive passage" → "in the
phil-of-physics literature, via MB duality, with σ-additivity as the boundary."
**POLISH:** Beltrametti–Cassinelli 1981 cite; "no charge exists"→"no charge
extending s" at 591/612.

## Net
NOT retired, NOT parked. REVISE: apply blocking fixes, consolidate on Type-6.
Strongest in the programme = synthesis/bridge, exactly what survives. Submit-or-not
= user's call. Paper I + the note unaffected by this verdict.
