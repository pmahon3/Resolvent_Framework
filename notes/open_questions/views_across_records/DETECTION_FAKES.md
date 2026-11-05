# Can detection error fake a twist? (hand puzzle, 2026-11-05)

reviewed: false. ⟦HAND⟧ argument; the four cases are LP-checked (`verification/eps_star_triangle.py` `eps_star`, run inline).

## Setting
True world: frogs, herons and fish all present or all absent together (π = ½). Every true disagreement is 0, and there is
no twist. Camera sees (frogs, herons), eDNA sees (herons, fish), transects see (fish, frogs). Each method has a detection
channel per species: detection probability p and false-positive rate f.

## Results
1. One method with detection p (f = 0, independent): d = π·2p(1−p).
2. Camera and eDNA perfect, transects p = ½: the reported family violates the triangle rule. **ε* = 1/8 (LP).** The
   fingerprint: transects report each species at rate ¼, against ½ elsewhere, so the single-species rates disagree.
   (V/3 = 1/12 does not apply here, since V/3 assumes consistent margins.)
3. **Theorem ⟦HAND⟧ (thinning cannot fake).** Assume no false positives and independent detection across species within each
   method. If every species is reported at the same rate by every method that sees it, the reports admit one classical
   world (ε* = 0). This holds for any true world, any number of species and methods, and any context hypergraph.
   Proof: equal rates force one detection probability p_i per species. Then W = (Z_1B_1, …, Z_nB_n), with independent
   B_i ~ Bern(p_i), has every method's table as a margin. LP check (p = 0.6, 0.8, 0.3): ε* = 0.
4. **Fake twists with no fingerprint**, i.e. every single-species rate consistent:
   - (a) *Detection dependence that differs across methods.* All p = ½. Camera and eDNA detect a pond's species together
     (positively coupled); transects detect exactly one of a pair (negatively coupled, e.g. attention or primer competition).
     **ε* = 1/6.**
   - (b) *False positives.* Transects with p = f = ½ report rate ½, the same as the perfect methods, but their reports carry
     no information. **ε* = 1/6.** A single rate π·p + (1−π)·f cannot pin down the channel (p, f).

## Reading: the seam, now precise
- Consistency of the single-species rates (CbD's visible check) guards against simple thinning, and only that.
- It does not guard against within-method detection dependence or false positives. Those can fake a twist of 1/6, half
  the triangle maximum, invisibly in the margins.
- Ecology's occupancy models identify each method's channel (p and f separately; dependence via repeat visits) from
  **repeat surveys**. Contextuality tests then work on the de-noised tables. Neither theory alone covers the joint:
  occupancy models assume one world, and contextuality tests assume the visible check suffices. The detection-aware test
  = identify the channels from repeat visits, invert them, then test. That is the candidate seam. Prior-art check owed
  (misclassification-aware marginal problems; "measurement error" in Bell/CbD tests).
