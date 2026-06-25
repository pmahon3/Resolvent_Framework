# Literature Review: Logic Background for Coherence and Completion

*Seed note - 2026-05-02*

## See also

- `notes/unsorted/foundations/coherence_completion/index.md` — front door for the
 working notes this review serves.

## Purpose

This note checks the coherence/completion direction against existing
mathematical logic literature. The aim is to avoid inventing a private
formalism where there is already established language.

The current programme language is:

- local coherent data;
- generous completion;
- realised/admissible part;
- admissibility / licensed descent;
- failure of automatic closure;
- Los obstruction;
- compact versus non-compact failure modes.

The literature suggests that the work should join several existing
conversations rather than present itself as a new foundational vocabulary from
scratch.

## Executive Verdict

The safest positioning is:

> The project studies a specific kind of local-to-global admissibility problem
> at the boundary between first-order definability, finitely additive
> probability, and Stone completion.

Do not present the formalism as a new general theory of coherence yet. Present
the theorem-clean core as an instance of standard abstract model-theoretic
diagnostics:

> ultraproduct non-closure implies non-first-order axiomatizability.

Then present the broader "completion with descent" language as a proposed
organizing perspective, explicitly adjacent to:

- abstract model theory;
- institution theory;
- categorical logic/topos semantics;
- sheaf-theoretic local-global obstruction theory;
- probabilistic logics and randomizations;
- accessible categories / abstract elementary classes.

## 1. Abstract Model Theory and Model-Theoretic Logics

### Conversation

Abstract model theory studies logics beyond first-order logic by comparing
properties such as compactness, Lowenheim-Skolem theorems, interpolation,
definability, and preservation. This is the native home for claims like:

> a property is not first-order axiomatizable because it is not preserved under
> ultraproducts.

Source anchors:

- Barwise and Feferman, *Model-Theoretic Logics*.
 Source: https://philpapers.org/rec/BARML-8

- Makowsky, "Compactness, Embeddings and Definability," in
 *Model-Theoretic Logics*.
 Source: https://www.cambridge.org/core/books/modeltheoretic-logics/compactness-embeddings-and-definability/88CB98ABE6A0ECD087945C0818C2E541

- Vaananen, "Barwise: Abstract Model Theory and Generalized Quantifiers."
 Source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B28D14107B717C59015583CCF73F3900/S1079898600004145a.pdf/barwise_abstract_model_theory_and_generalized_quantifiers.pdf

### How We Join

Our `Los obstruction` is not new as a theorem shape. It is the standard
ultraproduct non-closure diagnostic.

Our contribution, if any, is the application and interpretation:

- the target property is sigma-additivity of a finitely additive charge;
- the lean language is Boolean algebra with rational measure predicates;
- the obstruction is the ultrafilter charge induced by Dirac ultraproducts;
- CE is the exact enriched admissibility condition in the observational
 extension framework.

### Terminology Guidance

Use standard terms when possible:

- "not first-order axiomatizable";
- "not closed under ultraproducts";
- "relative to the ambient theory";
- "compactness / non-compactness";
- "definability."

Use our terms only as interpretive overlays:

- "failure of automatic closure";
- "admissibility";
- "licensed closure."

## 2. Institution Theory

### Conversation

Institution theory abstracts the notion of a logical system by packaging
signatures, sentences, models, and a satisfaction relation stable under change
of notation. It was introduced to compare and combine many logical systems
without committing to one syntax.

Source anchors:

- Goguen and Burstall, *Institutions: Abstract Model Theory for Specification
 and Programming*.
 Source: https://www.lfcs.inf.ed.ac.uk/reports/90/ECS-LFCS-90-106/

- Recent overview, "The Axiomatic Approach to Non-Classical Model Theory."
 Source: https://www.mdpi.com/2227-7390/10/19/3428

- Diaconescu, "Concepts of Interpolation in Stratified Institutions."
 Source: https://www.mdpi.com/2813-0405/1/2/5

### How We Join

Institution theory is relevant because our broader schema talks about multiple
horizons, each potentially with its own:

- local language;
- models;
- admissible refinements;
- satisfaction/realization relation.

The phrase "horizon plurality" should probably be disciplined by institution
theory if it becomes formal. Instead of saying "many horizons" informally, we
may eventually say:

> different observational horizons determine different institutions or
> institution-like fragments, with comparison functors/morphisms between them.

This would prevent the formalism from feeling arbitrary.

### Caution

Institution theory is broad and technical. We should not import it unless
there is an actual need to compare multiple logical systems or signatures.

For the first theorem-clean paper, ordinary first-order model theory is enough.

## 3. Sheaf-Theoretic Local-Global Obstructions

### Conversation

The sheaf-theoretic approach to contextuality studies when compatible local
data can be glued into a global section. Contextuality/nonlocality are
identified with obstructions to such global sections. Later work uses
cohomology to detect obstructions.

Source anchors:

- Abramsky and Brandenburger, "The Sheaf-Theoretic Structure of Non-Locality
 and Contextuality."
 Source: https://philpapers.org/rec/ABRTSS
 Open-access metadata/source:
 https://www.mendeley.com/catalogue/775bc5de-3849-3552-a9cb-e6d753431276/

- Abramsky, Mansfield, and Barbosa, "The Cohomology of Non-Locality and
 Contextuality."
 Source: https://www.research.ed.ac.uk/en/publications/the-cohomology-of-non-locality-and-contextuality-2/

- Dzhafarov, "The Contextuality-by-Default View of the Sheaf-Theoretic Approach
 to Contextuality."
 Source: https://philpapers.org/rec/DZHTCV

### How We Join

This is probably the closest match to our local/global/failure-mode language.
They already have:

- local contexts;
- compatible empirical/probabilistic data;
- a global section problem;
- obstruction to global realization.

Our probability problem differs:

- Paper I does not merely ask whether local distributions glue to a global
 assignment;
- Stone completion always supplies a generous completed space of coherent
 distinction patterns;
- the issue is whether the resulting measure descends to realised states or
 escapes to nonprincipal/ideal points;
- CE is a support/descent condition, not just ordinary sheaf gluing.

This is a useful distinction:

> Sheaf contextuality emphasizes obstruction to global section. Paper I
> emphasizes generous global completion plus an admissibility/support condition
> selecting realised states.

### Terminology Guidance

Use:

- "local-global obstruction";
- "global section" only when there is actually a sheaf/presheaf;
- "gluing" only for sheaf-like situations;
- "support/descent" for the Stone/CE situation.

Do not casually call CE "contextuality." The analogy is local-global, not
identical.

## 4. Categorical Logic and Topos Semantics

### Conversation

Categorical logic studies theories, models, classifying categories/topoi, and
internal logic. It provides established machinery for turning syntactic
theories into categories/topoi and interpreting logic in sheaves, Boolean-valued
models, and related structures.

Source anchors:

- Makkai and Reyes, *First Order Categorical Logic*.
 Source: https://link.springer.com/book/10.1007/BFb0066201

- Makkai and Reyes table of contents/source metadata.
 Source: https://link.springer.com/book/10.1007/BFb0066201

- Beke, "Sheafifiable Homotopy Model Categories."
 Source: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/sheafifiable-homotopy-model-categories/D13F781F14FC93FC8B65400D2C8B668F

### How We Join

Our "completion with descent" template resembles categorical logic in spirit:

$$
\text{syntax/local theory}
\quad\leadsto\quad
\text{classifying/completion object}
\quad\leadsto\quad
\text{models/points/realizations}.
$$

Stone duality is the Boolean-algebraic instance:

$$
B\mapsto\operatorname{St}(B).
$$

The realised/principal ultrafilter issue is closely related to points/support
in a completion. If we later want a categorical formalization, categorical
logic/topos semantics is a more natural home than inventing a fresh category
called "horizon."

### Caution

Do not claim a topos-theoretic theorem unless we actually formulate one. For
now:

- Stone duality is enough for Paper I;
- categorical logic is background for possible generalization;
- "completion with descent" should be described as a template, not as a new
 categorical construction.

## 5. Probabilistic Logics and Randomizations

### Conversation

There is an established literature on logics for probability, probability
quantifiers, measurable/nonmeasurable events, and randomizations of models.

Source anchors:

- Fagin, Halpern, and Megiddo, "A Logic for Reasoning about Probabilities."
 Source: https://research.ibm.com/publications/a-logic-for-reasoning-about-probabilities
 Journal source:
 https://www.sciencedirect.com/science/article/pii/089054019090060U

- Hoover, "An analytic completeness theorem for logics with probability
 quantifiers."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/an-analytic-completeness-theorem-for-logics-with-probability-quantifiers/CB272C5032234FF8EC66FB6B65102230

- Hoover, "A probabilistic interpolation theorem."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/a-probabilistic-interpolation-theorem/ABBAA40507B17A1D2753B3A1202E3AD9

- Ben Yaacov and Keisler, "Randomizations of models as metric structures."
 Source: https://www.numdam.org/articles/10.1142/S1793744209000080/

- Andrews and Keisler, "Separable Models of Randomizations."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/separable-models-of-randomizations/1C9F3D9CF1C16979640C2CE5AD829965

### How We Join

This literature prevents overclaiming. We should not say "logic cannot handle
probability." That is false. Many logics handle probability, probability
quantifiers, and randomizations.

Our precise claim is narrower:

> In the lean first-order language of Boolean algebras with finitely additive
> charge, sigma-additivity is not first-order axiomatizable.

And the Paper I claim is:

> In the directed observational extension problem, CE is the exact
> admissibility criterion for sigma-additive observable probability.

### Terminology Guidance

Say:

- "not first-order axiomatizable in this lean language";
- "requires non-first-order admissibility";
- "probability logics provide richer languages where probability is built in or
 treated by additional syntax/semantics."

Avoid:

- "probability is beyond logic";
- "logic cannot express probability";
- "countable additivity cannot be handled formally."

## 6. Accessible Categories and Abstract Elementary Classes

### Conversation

Accessible categories and abstract elementary classes provide language-free or
less syntax-bound frameworks for model theory, including classes of structures
with directed colimits, coherence axioms, and non-elementary behaviour.

Source anchors:

- Adamek and Rosicky, *Locally Presentable and Accessible Categories*.
 Source: https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/7F726C19BA30E5C10AE394741B80813D/9780511600579int_pxi-xiv_CBO.pdf/introduction.pdf

- Makkai and Pare, *Accessible Categories: The Foundations of Categorical Model
 Theory*.
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/michael-makkai-and-robert-pare-accessible-categories-the-foundations-of-categorical-model-theory-contemporary-mathematics-vol-104-american-mathematical-society-providence1989-viii-176-pp/E3EBD0E2AE73B63532B0FA31620195E8

- Lieberman and Rosicky, "Metric Abstract Elementary Classes as Accessible
 Categories."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/metric-abstract-elementary-classes-as-accessible-categories/8A675D9AD42386100A868CAA6F76F534

- "Category-theoretic aspects of abstract elementary classes."
 Source: https://www.sciencedirect.com/science/article/pii/S0168007211000753

### How We Join

This literature is relevant if we want to move beyond a fixed first-order
language into:

- categories of observational systems;
- directed colimits/refinements;
- non-elementary classes;
- metric or probabilistic structures;
- language-free model theory.

Important terminology warning:

> "coherent accessible category" is already a technical phrase in this area.

So our use of "coherence" must be disciplined. If we enter this literature, we
should either adopt their terminology precisely or avoid conflicting use.

### Caution

This is probably not needed for the first coherence/completion paper. It may
become useful if we try to formalize the category of query systems and their
refinements.

## 7. How To Reframe Our Current Language

Current phrase:

> local coherence

Safer literature-aware phrase:

> compatible local data, or first-order/local structure.

Current phrase:

> generous completion

Safer literature-aware phrase:

> Stone completion, classifying/completion object, or global section space,
> depending on the setting.

Current phrase:

> realised part

Safer literature-aware phrase:

> support on principal points, points of a topos, global sections, or intended
> realizations, depending on the setting.

Current phrase:

> admissibility

Safer literature-aware phrase:

> support condition, descent condition, extension criterion, or regularity
> condition.

Current phrase:

> failure of automatic closure

Safer literature-aware phrase:

> non-closure under ultraproducts, obstruction to global realization, failure
> of compactness, or failure of descent.

## 8. Revised Mathematical Positioning

The coherence/completion direction should be positioned as follows:

1. **The theorem-clean core is abstract model theory.**
 Sigma-additivity is not first-order axiomatizable in
 $\mathcal L_{\mathrm{BA},\mu}$ because the class is not closed under
 ultraproducts.

2. **The Paper I extension theorem is a Stone/support result.**
 Finitely additive data extend to the Stone completion; CE is the condition
 ensuring support on realised/principal states.

3. **The broader schema is local-global admissibility.**
 It is adjacent to sheaf obstruction theory and categorical logic, but not
 identical to either.

4. **The philosophy is scaffolding.**
 Terms such as horizon, stable openness, and licensed closure should guide
 the programme internally, but the public mathematical language should be
 definability, ultraproducts, compactness, Stone support, descent, and
 local-global obstruction.

## 9. Immediate Research Questions

1. Can CE be formulated as a **support/descent condition** in a way that is
 visibly parallel to sheaf local-global obstruction language, while preserving
 the distinction that Stone completion exists but support may escape?

2. Is the right general abstraction a sheaf/presheaf problem, an institution
 problem, a categorical-logic problem, or simply a family of examples?

3. Can the "completion with descent" template be expressed using established
 terms:

 $$
 \text{local data}
 \to
 \text{completion/classifying object}
 \to
 \text{support/descent condition}?
 $$

4. Does accessible-category model theory provide a natural category of query
 systems, or would that be unnecessary overhead?

5. Which future example most naturally joins an existing literature:

 - fibre mixing: continuous logic / metric structures;
 - valuation: institutions or enriched categories;
 - zeta: probably not logic-first yet;
 - reconstruction: sheaf/local-global or factor theory?

## 10. Deeper Touchpoint: Keisler Measures and Type Spaces

### Conversation

In model theory, a Keisler measure is a finitely additive probability measure on
a Boolean algebra of definable sets. Equivalently, over suitable parameter
sets, it can be represented as a regular Borel probability measure on a Stone
space of types.

Source anchors:

- Simon, *A Guide to NIP Theories*.
 Source: https://www.cambridge.org/core/books/guide-to-nip-theories/8A59D4B12F74C1FB513A02C7F6BA2E86

- Chernikov and Simon, "Definably amenable NIP groups."
 Source: https://arxiv.org/abs/1304.5989

- Hrushovski, Pillay, and Simon, "Generically stable and smooth measures in NIP
 theories."
 Source: https://arxiv.org/abs/1009.3052

- Chernikov, Kaplan, and Simon, "Groups and fields with NTP2."
 Source: https://arxiv.org/abs/1110.2806

### How We Join

This is a very serious adjacent literature because it already has:

- Boolean algebras of definable sets;
- finitely additive probability measures;
- Stone spaces of types;
- regular Borel measures on those Stone spaces;
- questions of definability, smoothness, finite satisfiability, invariance,
 and extension.

The similarity to Paper I is strong at the Stone/support level:

$$
\text{Boolean algebra of distinctions}
\quad\leadsto\quad
\text{Stone space}
\quad\leadsto\quad
\text{regular Borel measure}.
$$

The difference is also important. Keisler measures are usually accepted as
finitely additive measures on definable sets or regular measures on type
spaces. Paper I is asking when compatible finitely additive observational data
descends to a sigma-additive probability on realised observable states, rather
than merely living on the Stone/type completion.

### Possible Useful Problem Interface

Ask whether CE has an analogue in Keisler-measure language:

> Given a Keisler measure represented on a Stone space of types, what condition
> says that the measure is supported on realised types, or descends to a
> sigma-additive measure on an intended realised sample space?

This may already be classical under names like:

- smoothness of measures;
- definability of measures;
- finite satisfiability;
- support on realised types;
- Radon support or concentration on a definable/standard part.

We should not claim novelty here without a focused review.

### Risk

This literature is large and technically mature. It may absorb our Stone
language into known model-theoretic measure theory. That is good for
positioning, but dangerous for novelty claims.

The safe claim is:

> Paper I's CE/support picture is naturally comparable to the type-space
> representation of Keisler measures, but its target is observational descent to
> realised states.

## 11. Deeper Touchpoint: Boolean Algebras and Strictly Positive Measures

### Conversation

The existence of strictly positive measures on Boolean algebras and compact
totally disconnected spaces is a long-standing set-theoretic topology theme.
This directly touches the ultralimit representation and Strategy D notes.

Source anchors:

- Fremlin, *Measure Theory*, especially volumes/sections on measure algebras
 and compact spaces.
 Source: https://www1.essex.ac.uk/maths/people/fremlin/mt.htm

- Plebanek, "On compact spaces carrying Radon measures of uncountable Maharam
 type."
 Source: https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/257/3/113737/on-compact-spaces-carrying-radon-measures-of-uncountable-maharam-type

- Dzamonia and Plebanek, "Strictly positive measures on Boolean algebras."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/strictly-positive-measures-on-boolean-algebras/90D562383049E5EE99243B73C0811BC6

- Kelley, "Measures on Boolean algebras."
 Source: https://www.ams.org/journals/pams/1959-010-05/S0002-9939-1959-0107803-2/

### How We Join

The CE/support question has a Stone-space formulation:

> finitely additive charge on a Boolean algebra gives a measure on the Stone
> completion; CE asks whether support remains on the realised/principal part.

The ultralimit representation problem in the future notes already lands in
this literature:

> for which Boolean algebras is the Stone space sufficiently supported by
> sigma-additive/probabilistic points?

### Possible Open-Problem Interface

The Strategy D frontier from the current notes is genuinely close to
set-theoretic topology:

> Does there exist a non-sigma-complete non-atomic Boolean algebra admitting no
> sigma-additive probability?

Equivalent/topological versions involve compact totally disconnected spaces
with restricted Radon-measure support. This may be independent of ZFC or
require forcing/special set-theoretic assumptions.

This is probably the most concrete open-problem interface already in the repo.

### Risk

This line is technically demanding and may leave the observational programme
behind. It is useful as a frontier for the companion note, not necessarily as
the main route for the coherence/completion philosophy.

## 12. Deeper Touchpoint: Abstract Elementary Classes and Accessibility

### Conversation

Abstract elementary classes (AECs) and accessible categories study
non-elementary classes of structures with coherent embeddings, directed
colimits, tameness, categoricity transfer, and semantic rather than syntactic
control.

Source anchors:

- Baldwin, *Categoricity* / guide material on AECs.
 Source: https://homepages.math.uic.edu/~jbaldwin/pub/AEClec.pdf

- Grossberg, "A Course in Model Theory I: An Introduction to Abstract
 Elementary Classes."
 Source: https://arxiv.org/abs/1209.6426

- Boney, "Tameness from large cardinal axioms."
 Source: https://arxiv.org/abs/1303.5697

- Lieberman and Rosicky, "Metric abstract elementary classes as accessible
 categories."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/metric-abstract-elementary-classes-as-accessible-categories/8A675D9AD42386100A868CAA6F76F534

### How We Join

This is relevant only if query systems become a semantic category:

- objects: observational/query systems with compatible charges;
- morphisms: refinement or interpretation maps;
- directed colimits: increasing observational horizons;
- non-elementary property: CE or other admissibility conditions.

The AEC/accessibility literature could provide vocabulary for "local data under
directed refinement" without forcing everything into first-order syntax.

### Possible Open-Problem Interface

Ask:

> Is there a natural accessible category of observational systems whose
> elementary/accessibility-theoretic closure properties reflect CE or failure of
> CE?

This is speculative. It should not become the main line unless there is a
concrete categorical theorem.

### Risk

AEC terminology includes "coherence" in technical senses. Entering this
literature requires terminological precision. It may also be too far from the
current theorem package.

## 13. Deeper Touchpoint: Continuous Logic and Metric Structures

### Conversation

Continuous logic generalizes model theory to metric structures, with
ultraproducts, compactness, definability, and applications to probability,
operator algebras, Banach spaces, and randomizations.

Source anchors:

- Ben Yaacov, Berenstein, Henson, and Usvyatsov, "Model theory for metric
 structures."
 Source: https://www.math.ucla.edu/~ineeman/223S.1.13s/ContinuousLogic.pdf

- Ben Yaacov and Usvyatsov, "Continuous first order logic and local stability."
 Source: https://arxiv.org/abs/0801.4303

- Ben Yaacov and Keisler, "Randomizations of models as metric structures."
 Source: https://www.numdam.org/articles/10.1142/S1793744209000080/

### How We Join

This is probably the right logical setting for fibre mixing or dynamical
examples if they become theorem-clean. The fibre-mixing note already points in
this direction:

- lag-by-lag properties may be continuous-logical;
- uniformity across lags may escape expressibility;
- ultraproducts can preserve local/lagwise statements while losing uniform
 constants.

### Possible Open-Problem Interface

Ask whether some dynamical admissibility condition has the same form as CE:

> locally/lagwise good behaviour is preserved by continuous-logical
> ultraproducts, but the uniform condition needed for witness equivalence is
> lost in the limit.

This would be a strong second example if fibre mixing is resolved.

### Risk

Until the fibre-mixing mathematics is settled, this remains prospective.

## 14. More Exhaustive Search Process

To extend this review later, use passes rather than one broad search:

1. **Abstract model theory pass:** Lindstrom theorem, preservation theorems,
 generalized quantifiers, compactness failures.
2. **Probability logic pass:** Hoover, Keisler, Fagin-Halpern-Megiddo,
 randomizations, measure quantifiers.
3. **Keisler measure pass:** NIP, smooth/generically stable measures, type
 spaces, support on realised types.
4. **Boolean algebra / set-theoretic topology pass:** strictly positive
 measures, Radon-measure-free compacta, Maharam type, Kelley conditions,
 Fremlin/Plebanek/Kunen/Fedorchuk.
5. **Sheaf/categorical logic pass:** contextuality, classifying topoi, local
 sections, descent, gluing, points.
6. **Continuous logic pass:** metric structures, ultraproducts, randomizations,
 dynamical systems, uniformity gaps.
7. **Accessible categories/AEC pass:** directed colimits, non-elementary
 classes, tameness, coherent embeddings.

Each pass should produce:

- core references;
- native terminology;
- nearest theorem forms;
- open problems;
- whether CE/completion genuinely contributes or is only analogous.

## 15. Results of First Seven-Pass Review

*Note: these passes cover the same seven areas as §§1–13 above, with more
specific references and native-terminology lists. Readers familiar with the
earlier sections can skip to §16 (Ranked Opportunity Map) for the synthesis.*

### Pass 1: Abstract Model Theory

Native terms:

- abstract logic;
- compactness;
- preservation;
- ultraproduct closure;
- interpolation;
- Beth definability;
- generalized quantifiers;
- Lindstrom-style characterization.

Core sources:

- Barwise and Feferman, *Model-Theoretic Logics*.
 Source: https://philpapers.org/rec/BARML-8
- Vaananen, "The Craig Interpolation Theorem in abstract model theory."
 Source: https://link.springer.com/article/10.1007/s11229-008-9357-z
- Makowsky and Shelah, "The theorems of Beth and Craig in abstract model
 theory. I. The abstract setting."
 Source: https://cris.technion.ac.il/en/publications/the-theorems-of-beth-and-craig-in-abstract-model-theory-i-the-abs
- Petria and Diaconescu, "Abstract Beth definability in institutions."
 Source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7E4839A275E3C2C24993F31A6F3018FA/S0022481200006034a.pdf/abstract-beth-definability-in-institutions.pdf

Nearest theorem form:

> semantic non-preservation under a logic's preservation operations obstructs
> syntactic definability/axiomatizability.

How CE joins:

The countable-additivity note is a clean instance of this pattern:

$$
P_\sigma
\text{ is not preserved under ultraproducts}
\quad\Rightarrow\quad
P_\sigma
\text{ is not first-order axiomatizable.}
$$

Possible contribution:

Not the theorem-shape itself, which is standard. The contribution is the
specific Boolean-charge witness and the connection to CE as an exact
admissibility condition in the observational extension problem.

### Pass 2: Probabilistic Logic

Native terms:

- probability quantifiers;
- probabilistic propositional logic;
- measurable/nonmeasurable events;
- randomizations;
- neocompact sets;
- law structures;
- complete axiomatizations for probability languages.

Core sources:

- Keisler, "Probability Quantifiers," in *Model-Theoretic Logics*.
 Source: https://www.cambridge.org/core/books/modeltheoretic-logics/probability-quantifiers/81FB17B801B70287EAE45427EDD1CC73
- Fagin, Halpern, and Megiddo, "A Logic for Reasoning about Probabilities."
 Source: https://research.ibm.com/publications/a-logic-for-reasoning-about-probabilities
- Keisler and Lotfallah, "Almost everywhere elimination of probability
 quantifiers."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/almost-everywhere-elimination-of-probability-quantifiers/02E1E75663DA49C0A4902E5611826F9E
- Keisler, "Quantifier elimination for neocompact sets."
 Source: https://philpapers.org/rec/KEIQEF
- Ben Yaacov and Keisler, "Randomizations of models as metric structures."
 Source: https://numdam.org/articles/10.1142/S1793744209000080/

Nearest theorem form:

> enrich the language/semantics so probability is part of the logical
> environment, then prove completeness, elimination, or preservation results.

How CE joins:

CE should not be framed as "logic cannot express probability." Probability
logic already does that in richer settings. The precise claim is:

> sigma-additivity is not first-order axiomatizable in the lean Boolean
> algebra-with-charge language; CE is an enriched observational admissibility
> criterion.

Possible contribution:

The lean-language obstruction plus exact observational extension theorem may
serve as a bridge between finitely additive probability semantics and richer
probability logics.

### Pass 3: Keisler Measures and Type Spaces

Native terms:

- Keisler measure;
- definable sets;
- type space;
- regular Borel measure on a Stone space;
- NIP;
- generically stable measure;
- smooth measure;
- finite satisfiability;
- definability of measures;
- unique extension / stationarity.

Core sources:

- Simon, *A Guide to NIP Theories*.
 Source: https://www.cambridge.org/core/books/guide-to-nip-theories/8A59D4B12F74C1FB513A02C7F6BA2E86
- Hrushovski, Pillay, and Simon, "Generically stable and smooth measures in NIP
 theories."
 Source: https://www.ams.org/tran/2013-365-05/S0002-9947-2012-05626-1/
- Simon, "Finding generically stable measures."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/finding-generically-stable-measures/6B2A3BF6F9D493EE40211249FB0B5276
- Gannon, "Local Keisler measures and NIP formulas."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/local-keisler-measures-and-nip-formulas/D48D065C7EE5254728B8B032F4F7E834

Nearest theorem form:

> finitely additive measures on Boolean algebras of definable sets correspond
> to regular Borel measures on Stone/type spaces; additional model-theoretic
> hypotheses control definability, smoothness, finite approximation, and
> uniqueness of extensions.

How CE joins:

This is likely the closest model-theoretic conversation to the Stone/support
side of Paper I. Paper I's question can be compared to:

> when does a measure on the Stone/type completion descend to or concentrate on
> realised/standard points?

Possible contribution:

Maybe not theorem-level without more work. But CE as support/descent on Stone
completion should be compared carefully with smoothness, finite satisfiability,
and support properties of Keisler measures.

### Pass 4: Boolean Algebra and Set-Theoretic Topology

Native terms:

- strictly positive finitely additive measure;
- strictly positive Radon measure;
- Stone space;
- compact zero-dimensional space;
- ccc Boolean algebra;
- Maharam type;
- Kelley condition;
- measure algebra problem;
- set-theoretic independence;
- MA + not CH;
- Radon-measure support.

Core sources:

- Horn and Tarski, "Measures in Boolean algebras."
 Source: https://www.ams.org/journals/tran/1948-064-03/S0002-9947-1948-0028922-8/
- Kelley, "Measures on Boolean algebras."
 Source: https://www.ams.org/journals/pams/1959-010-05/S0002-9939-1959-0107803-2/
- Dzamonia and Plebanek, "Strictly positive measures on Boolean algebras."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/strictly-positive-measures-on-boolean-algebras/4F54776BD18D7185D0EEBA0F85F16948
- Fremlin, *Measure Theory*.
 Source: https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
- Jech, "Measures on Boolean algebras."
 Source: https://arxiv.org/abs/1705.01006

Nearest theorem form:

> characterize Boolean algebras or Stone spaces carrying measures with specified
> positivity, separability, nonatomicity, or Radon support properties.

How CE joins:

This is the most concrete open-problem interface already present in the repo.
The Strategy D question belongs here:

> does there exist a non-sigma-complete non-atomic Boolean algebra admitting no
> sigma-additive probability?

Possible contribution:

Potentially real, but technically difficult. This line could produce
standalone set-theoretic topology/Boolean algebra questions independent of the
broader observational programme.

### Pass 5: Sheaf and Categorical Logic

Native terms:

- local section;
- global section;
- measurement cover;
- compatible family;
- contextuality;
- cohomological obstruction;
- classifying topos;
- points/models;
- descent/gluing.

Core sources:

- Abramsky and Brandenburger, "The Sheaf-Theoretic Structure of Non-Locality
 and Contextuality."
 Source: https://www.researchgate.net/publication/48199583_The_Sheaf-Theoretic_Structure_Of_Non-Locality_and_Contextuality
- Abramsky, Mansfield, and Barbosa, "The Cohomology of Non-Locality and
 Contextuality."
 Source: https://www.research.ed.ac.uk/en/publications/the-cohomology-of-non-locality-and-contextuality/
- Makkai and Reyes, *First Order Categorical Logic*.
 Source: https://link.springer.com/book/10.1007/BFb0066201
- Johnstone, *Sketches of an Elephant*.
 Source: https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/peter-t-johnstone-sketches-of-an-elephant-a-topos-theory-compendium-oxford-logic-guides-vols-43-44-oxford-university-press-oxford-2002-xxii-1160-pp/0EC56FB698297E8E7EC563BB63C37F0B

Nearest theorem form:

> compatible local data may or may not glue to global sections; obstruction can
> be expressed sheaf-theoretically or cohomologically.

How CE joins:

The local-global analogy is real, but CE is not simply a global-section
obstruction. Paper I has a different shape:

> Stone completion exists, but the measure may fail to be supported on realised
> points.

So the closest public language is:

> support/descent after completion,

not generic "contextuality."

Possible contribution:

Mainly conceptual positioning unless a sheaf/presheaf model of observational
charges is constructed.

### Pass 6: Continuous Logic and Metric Structures

Native terms:

- continuous first-order logic;
- metric structures;
- continuous ultraproducts;
- compactness;
- axiomatizability;
- probability algebras;
- randomizations;
- uniformity gaps;
- model-theoretic forcing in analysis.

Core sources:

- Ben Yaacov, Berenstein, Henson, and Usvyatsov, "Model theory for metric
 structures."
 Source: https://www.math.ucla.edu/~ineeman/223S.1.13s/ContinuousLogic.pdf
- Ben Yaacov and Pedersen, "A proof of completeness for continuous first-order
 logic."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/proof-of-completeness-for-continuous-firstorder-logic/369544904681E43C6BD206D0DDCDA07B
- Ben Yaacov and Keisler, "Randomizations of models as metric structures."
 Source: https://numdam.org/articles/10.1142/S1793744209000080/
- Ben Yaacov, "Model theoretic forcing in analysis."
 Source: https://www.sciencedirect.com/science/article/pii/S0168007208001516

Nearest theorem form:

> metric/probabilistic analytic structures can be treated model-theoretically;
> ultraproducts and compactness remain central; axiomatizability admits
> ultraproduct-style characterizations.

How CE joins:

This is the natural setting for future metric/dynamical examples, especially
fibre mixing. The likely obstruction form is not sigma-additivity but loss of
uniform constants under ultraproducts.

Possible contribution:

Potentially a second example if fibre mixing produces a theorem:

> lagwise/finite observational conditions are preserved, but the uniform
> admissibility condition required for witness equivalence fails in the limit.

### Pass 7: AECs and Accessible Categories

Native terms:

- abstract elementary class;
- accessible category;
- coherent accessible category;
- directed colimit;
- tameness;
- Galois type;
- categoricity transfer;
- good frame;
- concrete directed colimit.

Core sources:

- Boney and Vasey, "A survey on tame abstract elementary classes."
 Source: https://people.math.harvard.edu/~wboney/papers/BVTameSurvey.pdf
- Grossberg, "A Course in Model Theory I: An Introduction to Abstract
 Elementary Classes."
 Source: https://arxiv.org/abs/1209.6426
- Lieberman and Rosicky, "Metric abstract elementary classes as accessible
 categories."
 Source: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/metric-abstract-elementary-classes-as-accessible-categories/8A675D9AD42386100A868CAA6F76F534
- Lieberman and Rosicky, "Classification theory for accessible categories."
 Source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D24EF02A95152385B63EE841736CAB47/S0022481214000851a.pdf/classification_theory_for_accessible_categories.pdf

Nearest theorem form:

> semantic categories of structures with directed colimits and coherent
> embeddings can support classification theory beyond first-order syntax.

How CE joins:

This is relevant only if query systems become a genuine semantic category with
directed refinements and colimits. It may eventually help formalize
observational systems without forcing them into a fixed language.

Possible contribution:

Speculative. Main current value is a terminology warning: "coherence" and
"coherent accessible category" are already technical terms.

## 16. Ranked Opportunity Map

### Most Concrete

Boolean algebra / set-theoretic topology.

Reason:

- already linked to existing Strategy D notes;
- clear native problems about measures on Boolean algebras and Stone spaces;
- possible ZFC/independence frontier.

### Most Thematically Aligned

Keisler measures and type spaces.

Reason:

- finitely additive measures on definable Boolean algebras;
- Stone/type space representation;
- support/extension/smoothness language;
- close to Paper I's Stone/support picture.

### Best Second-Example Candidate

Continuous logic for fibre mixing.

Reason:

- metric/probabilistic structures;
- ultraproducts and compactness;
- natural language for uniformity gaps.

### Best Conceptual Comparator

Sheaf/categorical local-global obstruction.

Reason:

- already has local compatibility and global obstruction;
- useful contrast with CE's completion-plus-support shape.

### Use With Caution

Institution theory and AEC/accessibility.

Reason:

- powerful abstract homes;
- high overhead;
- risk of making the project look more general than theorems justify.

## 17. Possible Open Questions We Might Actually Ask

1. **CE/Keisler comparison.**
 What is the exact relationship between CE-type support on realised Stone
 points and smoothness/finite satisfiability/definability conditions for
 Keisler measures?

2. **Stone support/descent theorem form.**
 Can Paper I's Stone construction be recast in a standard support/descent
 theorem form recognizable to categorical logic or sheaf theorists?

3. **Boolean algebra Strategy D.**
 Does there exist, consistently or in ZFC, a non-sigma-complete non-atomic
 Boolean algebra admitting no sigma-additive probability? What is the exact
 Stone-space version in terms of Radon support?

4. **Continuous-logic uniformity obstruction.**
 Can fibre mixing be formulated as a uniform condition not reducible to
 lagwise continuous-logical axioms, with an ultraproduct witness losing the
 uniform constant?

5. **Institutional horizon comparison.**
 If valuation examples mature, can different valuations be treated as
 different institutions or reduct/enrichment pairs, with comparison functors?

6. **Completion versus global section.**
 Is there a formal local-global framework distinguishing:

 - no global section exists;
 - a completion exists but support escapes;
 - completion exists and descent/support is licensed?

 CE belongs to the second-to-third transition, not the first.

## 18. Revised Bottom Line After Passes

The review suggests three disciplined public entry points:

1. **Abstract model theory:** non-first-order axiomatizability via
 ultraproduct non-closure.
2. **Stone/type-space measure theory:** finitely additive data as measures on
 completions; CE as support/descent to realised states.
3. **Local-global obstruction theory:** comparison class, with the key
 distinction that CE is not merely absence of a global section but failure of
 support after completion.

The internal philosophical slogan remains useful:

> open horizon / licensed closure.

The public mathematical translation should be:

> local compatible data, completion, support/descent condition, and preservation
> obstruction.

## Bottom Line

The current mathematical direction is not arbitrary if it is disciplined by the
existing literature.

The public-facing mathematical conversation should be:

> abstract model theory + Stone duality/support + local-global obstruction.

The internal philosophical language can remain:

> open horizon / licensed closure.

The bridge is:

> failure of automatic closure = non-closure under the relevant limiting or
> completion operation; admissibility = the support/descent/extension condition
> that rules out the failure mode.
