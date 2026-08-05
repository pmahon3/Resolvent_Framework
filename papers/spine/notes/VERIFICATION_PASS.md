# Spine §4 replacement blocks — verification pass (2026-07-08)

Verifying the design-side replacement blocks (prop:ladder, thm:quarantine,
cor:tower) BEFORE pasting. Three checks flagged by the design side + one bonus.

## 1. prop:ladder first-gap witness (pentagon) — MATH OK, CARRIER DESCRIPTOR WRONG
- CLAIM in proposed text: "depth-3 conflict pentagon ... eight-point clopen
  carrier admitting no finitely additive state ... value 5/2 exceeds ceiling 2".
- VERIFIED (pentagon_chain_immunity_check.py, live re-run): the pentagon is the
  C5 ring on {0,1}^5 = **32 points, NOT 8**. Its half-model (s(a,b)=1/2 for
  a!=b, 0 for a=a) is pairwise-EA, and admits NO finitely additive state on its
  generated closure — because that closure is FINITE (Boolean, 2^32), so
  finitely-additive = a measure = convex combo of point masses, and the
  half-model needs support on proper 2-colorings of C5, of which there are ZERO
  (odd cycle). The α(C5)=2 vs model=5/2 stable-set certificate is one valid way
  to see the non-existence.
- CONCLUSION: the proposition's LOGIC holds (genuine gap-1 witness: pairwise-EA
  without finite coherence) but the CARRIER must be described correctly:
  "the C5 ring protocol on {0,1}^5 (machine-verified)", drop "eight-point", and
  either cite the α(C5) stable-set bound OR the empty-2-coloring support — both
  are the same fact. FIX REQUIRED before paste.

## 2. thm:quarantine part (i) — SOUND (audited step by step)
- Filter step: s(C∩D)+s(C∪D)=s(C)+s(D)=2 by incl-excl for charges; 2-valued =>
  s(C∩D)=1; monotone + ∅∉F => proper filter. VALID.
- Extend to ultrafilter of Clo(X) by ultrafilter lemma. VALID.
- FIP/compactness (THE load-bearer): U = filter of clopen(=closed) sets in
  compact X with FIP => ∩U ≠ ∅. VALID (this is the danger step; it holds).
- s = delta_x|B by the true/false-complement argument. VALID.
- NO dropped case. Part (ii) compactness-collapses σ-add to finite-add on clopens
  (correct); Caratheodory-Hahn + clopen-basis + π-λ (standard). Part (iii)
  Horn-Tarski charge extension then (ii) (citation pending scout).

## 3. BONUS corpus sentence (from the audit, worth adding)
Part (i)'s compactness hypothesis is EXACTLY what the sigma-essential witness
escapes by living at omega_1 (non-compact, FIP fails). So thm:quarantine and the
regularity witness are CONSISTENT, not in tension — the quarantine proves the
witness CANNOT descend to the compact/dynamical regime. This is the "sorted not
piled" claim made rigorous, and it is the design side's structural note
(part (i) = Boolean-baseline atom argument, "finite" upgraded to "compact" =
same proof at two scales) confirmed.

## 4. Citations (Horn-Tarski / Rao-Rao / Caratheodory-Hahn / Stone-clopen)
SCOUT RUNNING — credit line held until it returns.

## PASTE DECISION
Hold until: (a) citation scout returns, (b) prop:ladder carrier descriptor
corrected to the 32-point C5 (not 8-point). Everything else verified sound.

## RESULT (2026-07-08): all checks passed, blocks pasted
- Citations CONFIRMED by scout: Horn-Tarski 1948 (Trans AMS 64:467-497),
  Rao-Rao 1983 (Theory of Charges, Academic Press), Caratheodory-Hahn (textbook).
  Referee-hardening folded into the proofs: (a) Horn-Tarski extension is the
  FINITELY-ADDITIVE case (their countably-additive analogue can fail) — proof
  part (iii) now says so explicitly and part (ii) supplies sigma-additivity from
  compactness separately; (b) Caratheodory uniqueness scoped to finite/sigma-finite.
- prop:ladder carrier CORRECTED: "eight-point" -> the C5 pentagon protocol over
  {0,1}^5 (machine-verified), no-finitely-additive-state via empty-2-coloring /
  alpha(C5)=2 vs 5/2. Gap-1 witness sound.
- thm:quarantine part (i): audited sound (filter->ultrafilter->FIP/compactness->
  point), no dropped case.
- BONUS sentence added (rem:quarantine-scope): compactness is exactly what the
  omega_1 witness escapes => quarantine & witness consistent not in tension;
  part (i) = Boolean-baseline atom argument at compact scale (same proof, two
  scales).
- Compile bug caught+fixed: corollary environment was undefined in the wrapper
  (only surfaced on compile — the lane working). Added it.
- §4 inverted: "two open questions" -> "two bridging results + latticehood
  conjecture". Abstract wrapper line + §2 "classification (cor:tower)" flipped.
- Compiles clean: 5pp, 0 errors, 0 undefined cite/ref, both bibitems resolve.
PASTE COMPLETE. Spine's central sentence is now FACT, not conjecture.

## 2026-08-04 propagation addendum

The “latticehood conjecture” named above was a conjectural third item, not part
of the proved ladder/quarantine sentence. The prior-art/type audit refutes its
literal three-way form using the complete Hilbert lattice's sharpness failure.
The spine now retains only the regularity question `latticehood => Phi`; the
verified ladder and quarantine results are unchanged.
