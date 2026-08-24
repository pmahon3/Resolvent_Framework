# Receipt — Skeleton A read, same-session adversarial check (2026-07-10, s13)

**What was checked.** The session-13 Skeleton A read
(`oml_lattice_regularity_attack.md` §10): two new elementary theorem-lets
(R = Dirac forcing from (8.1)-inner-regularity; P = coarse diffuse
components fail (8.1) on uncountable Polish, incl. P0 decomposition), the
Maharam 1972 reading claims (M1–M4: Thm 6.1 = topology-free Hahn–Banach
f.a. glue; (8.1) consumed only in the cross-block compact-class σ-upgrade;
no point-realization anywhere; in-block K ∈ 𝔉_α + Hausdorff verbatim), the
Derr–Williamson App. D reading claims (D1–D3: Thm D.6 hypotheses verbatim;
footnote-29 vs (8.1) definitional gap; proof = Prop D.4 → Maharam 8.1 →
Carathéodory), and the consequence C (non-principal blockwise restriction
⟹ D.6 silent on every Polish representation).

**Method.** Fresh-context adversarial reviewer (no thread exposure,
instructed to refute, claims stated self-contained), primary PDFs read
directly: `maharam_1972.pdf` pp. 136–137 + 145–146,
`derr_williamson_2023.pdf` pp. 46–49.

**VERDICT: no refutation found — R(a–c), P (incl. P0), M1–M4, D1–D3, C all
SOUND as stated.** Five caveats, none affecting a conclusion:

1. (M2) The open approximants Gᵢ are (8.1)-compacts of the *complements*,
   turned open via compact ⟹ closed — so Hausdorff is load-bearing twice
   (there and for compactness of ∩Kᵢ). Matches Maharam's own elision.
2. (M1) Thm 6.1 is stated for positive linear maps; the
   functional↔f.a.-measure translation is implicit in Maharam's proof line
   ("which, for convenience, we restrict to the field F"). Substance
   unaffected.
3. (R) Benign silent hypotheses: monotonicity from finite additivity;
   "K ⊂ F" read as ⊆ (1972 convention); value-1 sup *attained* because ν
   is two-valued (sup of a subset of {0,1}).
4. (P0) Uses AC_ω (countable unions of countable sets); X uncountable
   needed for well-definedness — given.
5. (C) Conclusion is conditional on the in-field reading of D.6's "inner
   regular" (the only reading that typechecks and matches the invoked
   Maharam theorem); and failing D.6's hypothesis makes D.6 *silent*, not
   a refutation of σ-extendability. §10 phrases both correctly.

Confirmed textual finding in the primary source: DW footnote 29 defines
inner regularity without K ∈ 𝒜ᵢ, while the invoked Maharam (8.1) requires
it and μᵢ(K) is otherwise undefined — the gap is in the DW text and is
accurately reported in §10d(ii).

**Standing.** Same-session check (weaker than the s12 standard: no
from-scratch scripts — the claims are topological, not finitely
instantiable). ~~A from-scratch fresh-context proof-read of §10 at the
s12 standard remains owed.~~ CLEARED 2026-07-10 s14 — see
`PROOF_READ_2026-07-10_attack_s10.md` (all sound; one scope fix to
§10d(i)'s "exactly", edits ✎s14 applied in place). Awaits user
ratification.
