# Categorical Foundations: the inversion, and its phenomenological reading

*Working note — 2026-03-19. Trimmed 2026-06-11: the formal Meas / Giry /
Kleisli / extension development this note originally sketched is now done
properly in the `.tex` files of this directory (see the map below). What is kept
here is the part the `.tex` files do not carry in full: the phenomenological
reading of the inversion.*

## The one idea

The Observable Dynamics Program inverts the classical foundational order of
probability. Classical: posit a probability space, derive observations from it
(**algebra-first**). Program: derive the probability space from the coherence of
observations (**diagram-first**). Categorically the inversion lives at exactly
one place — the free choice of a Giry-monad algebra (the measure) at "Step 3" of
the classical construction — which the program replaces by a *forced* apex of a
diagram of compatible marginals (the Observational Extension Theorem = the left
adjoint / equivalence). That is the whole content; everything else is
functoriality.

## Where the formal development now lives (pointer map)

| Want | File |
|------|------|
| Classical picture: Meas, Giry monad, Kleisli, algebras, Kolmogorov | `categorical_classical.tex` |
| The inversion, query systems as diagrams in Kl(𝒫), predictive query / delay / Rose, classical-vs-program comparison table | `categorical_program.tex` |
| The clean result — Ext ⊣ Forget as the categorical statement of Paper I (categories, functors, equivalence, proof) | `categorical_adjunction.tex` |
| Mathlib has/lacks audit | `mathlib_gaps.md` |

## The phenomenological reading (the residue worth keeping)

The categorical picture makes a phenomenological structure precise. This framing
is *not* in the `.tex` files in this explicit form and is the reason this note
survives:

| Classical (Cartesian) | Program (phenomenological) |
|---|---|
| Probability space assumed as ground | Probability space derived from coherence |
| Monad algebra freely chosen | Monad algebra forced by the diagram |
| Observations are projections of a presupposed whole | The whole is constituted by coherence of the parts |
| **View from nowhere** | **View from the horizon of queries** |
| Algebra-first | Diagram-first |

The Kleisli category is a world of *transitions and relations* — morphisms
primary, objects secondary — closer to a picture where experience is
fundamentally relational (intentional) than to a collection of static facts. The
monad multiplication `𝒫𝒫(X) → 𝒫(X)` — collapsing uncertain beliefs about
distributions into one distribution — is classically a free choice (a prior).
The program's question, in this language: *does the query structure force that
collapse without a free choice?* I.e. is probability **query-primitive** rather
than measure-primitive? (Merleau-Ponty: objectivity is constituted by the
coherence of perspectives, not presupposed beneath them — the `program.tex`
comparison table, row 9, is the mathematical form of exactly this.)

## Open problems, as categorical questions (still open, recorded for re-entry)

- **σ-additivity without topology.** Under what conditions on a diagram in Kl(𝒫)
  does a canonical monad algebra (the apex) exist *without* Polish/tightness
  hypotheses? (Realizability replaces inner regularity in the program's route;
  see `categorical_program.tex`, the "Polish replacement" remark.)
- **Deriving the objects.** Can the measurable spaces `Oᵢ` themselves be derived
  from something more primitive — a category of topological spaces / domains /
  locales mapping into Meas — i.e. σ-algebras from discriminative capacity?
  (This is the locale/sheaf direction; cf. the distributive-frame localic measure
  theory that the descent axis had to be distinguished from.)
- **Realizability as a categorical condition.** When are the projections
  `Ω = lim Oᵢ → Oᵢ` surjective — i.e. when is the limit computed in Meas rather
  than a subcategory?

*Status: dormant conceptual reference, (a)-side / Boolean-era material. Re-engage
only on new input — e.g. a Paper I revision that wants the adjunction framing, or
a return to the Boolean/distributive line. See `README.md` and
`notes/programme/genealogy.md` (the (a)/(b) fork).*
