# Five and six quantities, every pair seen: K₅, K₆

reviewed: false. 2026-11-13. Pre-registration first; results appended below. ⟦HAND⟧ = unchecked hand argument.
Notation: `notes/programme/TERMINOLOGY_CROSSWALK.md` §A″. Context: `FOUR_QUANTITIES_GATE.md` (K₄ closed at every
finite size, hand, two readers). An independent check of the gluing lemma is running separately and will compute
K₅(2) and "two K₄'s sharing a triangle" at two values by closure; this file does not repeat that.

## Forcedness check and what is expected
- **Slices.** For K_m, two slices at one quantity differ by a sum of m−1 one-quantity functions with values in
  {−1,0,1}. The T1 argument gives the same dichotomy: simple, or K-type on exactly two quantities ⟦HAND⟧. So "reducible"
  and the merge move make sense for every m, and a reducible set on K_m(n) is in D once the merged grid is settled.
- **Two values.** A sum of pair functions on bits is a real polynomial of degree ≤ 2, so V₀₁(K_m(2)) is the set of
  Boolean functions of degree ≤ 2. From memory, unverified: such a function depends on at most 4 of its variables
  (the degree-d bound of Nisan–Szegedy is d·2^(d−1)). If so, every member of V₀₁(K_m(2)) lives on four quantities and is
  in D by the K₄ theorem, for every m.

## Gate `gate.five_quantities` (pre-registered 2026-11-13, not yet run)
1. **Bits, m = 5 and 6.** Enumerate V₀₁(K₅(2)) and V₀₁(K₆(2)) exactly; for each member count the quantities it
   depends on. Prediction: never more than 4. A member depending on 5 or 6 would be a new irreducible object and
   would refute the remembered bound as used here.
2. **Irreducible sets on K₅ beyond bits.** Enumerate V₀₁(K₅(n)) by slices for n with entries in {2,3}, up to K₅(3) if
   each step stays under 1.5 GB, and count irreducible members. Prediction (by analogy with K₄, no proof): none
   unless every quantity has two values.
- (a) both predictions hold ⇒ every set tested reduces, by verified merges, to a set on bits that depends on ≤ 4
  quantities; with the K₄ theorem this gives D = V₀₁ at the sizes run. Next: try the hand proof "irreducible ⇒ two
  values everywhere" for general m.
- (b) a prediction fails ⇒ the failing set is the object to study; nothing is concluded about D.
**Prior guesses (unvalidated):** part 1 holds 85%; part 2 holds 65%.
