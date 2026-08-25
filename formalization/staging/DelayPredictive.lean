/-
# The predictive law map, on a standard Borel alphabet

Phase 2 of `notes/open_questions/delay_embedding/PLAN_delay_chapter.md`, first
item: `def:delay-pred-map`.

## The restriction, and why it is here rather than in the chapter

`condDistrib` -- and every route to a conditional law -- needs
`[StandardBorelSpace X] [Nonempty X]`. `DelayEmbedding.lean` is proved for a
bare `[MeasurableSpace X]`, and its structural results (query-system axioms,
upper-directedness, the not-sequentially-upper-directed gap, realizability,
compatibility) deserve that generality. So the predictive layer is a SEPARATE
module with the stronger hypothesis, not an amendment to the chapter. The
blueprint's `sec:delay-gaps` states this reading.

## What is here

* `predLaw P d tau` -- phi_{d,tau}, the conditional law of the next sample
  given the delay window. Built from Mathlib's `condDistrib`, which is exactly
  "conditional law of Y given X" and is the purpose-built tool; an earlier
  attempt went through `Measure.condKernel` on a hand-built joint law and
  stalled on the `IsCondKernel` instance.
* `predLaw_ae_eq_condExp` -- the defining property: phi computes the
  conditional expectation of an indicator of the next sample given the window.
  This is what makes `predLaw` the conditional law rather than an arbitrary
  kernel, and it is the honest content of the definition.

Both axiom-free: [propext, Classical.choice, Quot.sound].

## NOT here, and a correction to the plan

`def:pred-sufficient` is NOT the next easy step. The DelayEmbedding header
glosses predictive sufficiency as "injectivity of phi_{d,tau} on the support".
The source (`archive/superseded_drafts/predictive_experiments`, Definition at
l.515) says something materially different:

    Q is predictively sufficient if for every admissible query Q' there is a
    measurable psi : O_Q -> O_{Q'} with Pi_{Q'} = Pi_Q . psi

-- a factorization condition quantified over ALL other queries, with the
characterization `F indep Q' given Q`. Injectivity of phi is neither the
definition nor obviously equivalent to it.

Formalizing the gloss would produce a clean-compiling theorem about the wrong
statement. The definition must be settled against the source before
`def:pred-sufficient`, `def:markov-order` and `thm:sufficiency` are attempted.
-/
import QuerySystem.DelayEmbedding
import Mathlib.Probability.Kernel.CondDistrib
open MeasureTheory ProbabilityTheory Set
open scoped ENNReal
namespace DelayPredictive
variable {X : Type u} [MeasurableSpace X] [StandardBorelSpace X] [Nonempty X]

/-- **The predictive law map (`def:delay-pred-map`).** `φ_{d,τ}` sends a delay
window to the conditional law of the NEXT sample given that window. -/
noncomputable def predLaw (P : Measure (SensorStream X)) [IsProbabilityMeasure P]
    (d τ : ℕ) : Kernel (DelayOutcome X d) X :=
  condDistrib (fun ω => ω 1) (delayEval d τ) P

/-- **The defining property.** `φ_{d,τ}` computes the conditional expectation of
any bounded observable of the next sample, given the window. -/
theorem predLaw_ae_eq_condExp (P : Measure (SensorStream X)) [IsProbabilityMeasure P]
    (d τ : ℕ) {s : Set X} (hs : MeasurableSet s) :
    (fun ω => (predLaw P d τ (delayEval d τ ω) s).toReal)
      =ᵐ[P] P[(fun ω => (s.indicator (fun _ => (1:ℝ)) (ω 1))) |
              MeasurableSpace.comap (delayEval d τ) inferInstance] :=
  condDistrib_ae_eq_condExp (measurable_delayEval d τ) (measurable_sensorEval 1) hs

end DelayPredictive
