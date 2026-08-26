import QuerySystem.BoundaryDescent

/-! # Abstract compatible-section core of ODBC

This file formalizes only the inverse-system logic of ODBC.  It deliberately
does not assert that an abstract system is realized by an OML block atlas.
-/

open Set Function MeasurableSpace

universe u v

namespace SigmaEssential.Blocks

/-- Local eligible-lift spaces together with their pairwise boundary
compatibility relation. In an OML application `I` indexes local coordinates;
a set `J : Set I` indexes a subsystem. This abstract type does not encode the
note-level existentially varying common witness `mu_J`. -/
structure SectionSystem where
  I : Type u
  X : I → Type v
  Compatible : ∀ {i j}, X i → X j → Prop

namespace SectionSystem

variable (S : SectionSystem.{u, v})

/-- A choice of one eligible lift at every index in a subsystem. -/
def PartialSection (J : Set S.I) := ∀ i, i ∈ J → S.X i

/-- Pairwise boundary compatibility of a subsystem section. -/
def IsCompatible {J : Set S.I} (s : S.PartialSection J) : Prop :=
  ∀ i (hi : i ∈ J) j (hj : j ∈ J), S.Compatible (s i hi) (s j hj)

/-- Existence of a compatible section over exactly `J`. -/
def HasSection (J : Set S.I) : Prop :=
  ∃ s : S.PartialSection J, S.IsCompatible s

/-- Existence on every finite subsystem. -/
def FiniteSectionSolvable : Prop := ∀ J : Set S.I, J.Finite → S.HasSection J

/-- Existence on every countable subsystem.  This is intentionally stronger
than coordinatewise nonemptiness and includes compatibility in the quantifier. -/
def CountableSectionSolvable : Prop := ∀ J : Set S.I, J.Countable → S.HasSection J

/-- A global compatible section. -/
def HasGlobalSection : Prop := S.HasSection Set.univ

/-- Abstract ODBC: compatible finite and countable subsystem sections
globalize.  OML eligibility/cut-saturation hypotheses belong in the theorem
which proves this proposition for the concrete atlas system. -/
def ODBC : Prop :=
  S.FiniteSectionSolvable → S.CountableSectionSolvable → S.HasGlobalSection

theorem countableSectionSolvable_implies_finite
    (h : S.CountableSectionSolvable) : S.FiniteSectionSolvable :=
  fun J hJ => h J hJ.countable

theorem odbC_of_countable_compactness
    (h : S.CountableSectionSolvable → S.HasGlobalSection) : S.ODBC := by
  intro _ hc
  exact h hc

end SectionSystem

/-- Honest abstract implication into `Phi`: an application must supply, for
each finite trace, its concrete eligible-lift system, compatible subsystem
sections, and the GSD extraction from a *global* section. -/
theorem phi_of_odbc_sections {Omega : Type*} {d : DynkinSystem Omega}
    (atlas : ∀ (_ : Block d) (_ : FinAddState d), SectionSystem)
    (hODBC : ∀ B mu, (atlas B mu).ODBC)
    (hfinite : ∀ B mu, (atlas B mu).FiniteSectionSolvable)
    (hcountable : ∀ B mu, (atlas B mu).CountableSectionSolvable)
    (hGSD : ∀ B mu, (atlas B mu).HasGlobalSection →
      ∃ nu : TwoValuedState d, ∀ A ∈ B.sets, (nu.Val A ↔ mu.Val A)) :
    Phi d := by
  intro B mu
  exact hGSD B mu (hODBC B mu (hfinite B mu) (hcountable B mu))

#print axioms SectionSystem.countableSectionSolvable_implies_finite
#print axioms SectionSystem.odbC_of_countable_compactness
#print axioms phi_of_odbc_sections

end SigmaEssential.Blocks
