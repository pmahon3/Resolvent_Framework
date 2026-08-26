import QuerySystem.ODBCSections

/-! # Conditional fine/coarse packaging for ODBC

This file records only the stable logical implication used by the Campaign 6
fine/coarse decomposition.  `Fine` and `Coarse` are arbitrary predicates on
finite traces: no claim that they exhaust concrete OML traces, or that either
regime satisfies ODBC, is made here.

`SectionSystem.ODBC` below is the abstract conditional globalization
component. It is not the full mathematical conjunction called ODBC in the
notes; finite/countable section solvability is therefore assumed separately.
-/

open Set Function MeasurableSpace

universe u v

namespace SigmaEssential.Blocks

/-- If every finite trace belongs to one of two regimes, and ODBC is known in
the regime containing that trace, then compatible finite/countable sections
and GSD imply `Phi`.  This makes the open mathematical inputs explicit rather
than encoding fine or coarse ODBC as an axiom or theorem. -/
theorem phi_of_fine_coarse_odbc_sections
    {Omega : Type*} {d : DynkinSystem Omega}
    (atlas : ∀ (_ : Block d) (_ : FinAddState d),
      SectionSystem.{u, v})
    (Fine Coarse : Block d → FinAddState d → Prop)
    (hcover : ∀ B mu, Fine B mu ∨ Coarse B mu)
    (hFineODBC : ∀ B mu, Fine B mu → (atlas B mu).ODBC)
    (hCoarseODBC : ∀ B mu, Coarse B mu → (atlas B mu).ODBC)
    (hfinite : ∀ B mu, (atlas B mu).FiniteSectionSolvable)
    (hcountable : ∀ B mu, (atlas B mu).CountableSectionSolvable)
    (hGSD : ∀ B mu, (atlas B mu).HasGlobalSection →
      ∃ nu : TwoValuedState d, ∀ A ∈ B.sets, (nu.Val A ↔ mu.Val A)) :
    Phi d := by
  intro B mu
  have hODBC : (atlas B mu).ODBC := by
    rcases hcover B mu with hFine | hCoarse
    · exact hFineODBC B mu hFine
    · exact hCoarseODBC B mu hCoarse
  exact hGSD B mu (hODBC (hfinite B mu) (hcountable B mu))

/-- One-regime specialization.  In particular, a proved fine-ODBC theorem
can be inserted here without claiming that countable generation alone proves
that theorem. -/
theorem phi_of_regime_odbc_sections
    {Omega : Type*} {d : DynkinSystem Omega}
    (atlas : ∀ (_ : Block d) (_ : FinAddState d),
      SectionSystem.{u, v})
    (Regime : Block d → FinAddState d → Prop)
    (hregime : ∀ B mu, Regime B mu)
    (hODBC : ∀ B mu, Regime B mu → (atlas B mu).ODBC)
    (hfinite : ∀ B mu, (atlas B mu).FiniteSectionSolvable)
    (hcountable : ∀ B mu, (atlas B mu).CountableSectionSolvable)
    (hGSD : ∀ B mu, (atlas B mu).HasGlobalSection →
      ∃ nu : TwoValuedState d, ∀ A ∈ B.sets, (nu.Val A ↔ mu.Val A)) :
    Phi d := by
  intro B mu
  exact hGSD B mu
    (hODBC B mu (hregime B mu) (hfinite B mu) (hcountable B mu))

#print axioms phi_of_fine_coarse_odbc_sections
#print axioms phi_of_regime_odbc_sections

end SigmaEssential.Blocks
