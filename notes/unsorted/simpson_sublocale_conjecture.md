# Seed Note: CE as Spatiality of Simpson's Measure-1 Sublocale

## Phase: 1 (seed) — needs Phase 2 audit before ANY development

## The conjecture

For a Boolean algebra B with Stone space St(B) and a finitely
additive charge ℓ (= regular Borel measure μ̂ on St(B)):

> CE holds (ℓ is σ-additive) ⟺ Simpson's smallest measure-1
> σ-sublocale of O(St(B)) is spatial (has enough points).

## Context

Simpson (2012) "Measure, Randomness and Sublocales" (APAL 163)
showed: every probability valuation on a fitted σ-locale has a
smallest σ-sublocale of full measure. This is frame-constructible.

The conjecture says: CE ↔ this sublocale is spatial. Intuitively:
the measure concentrates on a "point-determined" part of the locale
iff the charge is σ-additive.

## Why it MIGHT be true

- CE = support on pure(Ω) = support on points
- Spatiality = determined by points
- The smallest measure-1 sublocale being spatial would mean "the
  measure is determined by its behavior on points" ↔ "mass lives
  on points" ↔ CE

## Why it might be FALSE or TRIVIAL

- St(B) is itself spatial (sober). Does spatiality of sublocales
  behave differently?
- The locale theory community hasn't stated this. Possible reasons:
  (a) obvious to them, (b) false, (c) requires extra assumptions,
  (d) genuinely hard and open
- Layer 2 finding: CE/non-CE valuations are indistinguishable on
  general opens. So the distinction must come from the σ-sublocale
  structure, not from continuity properties.

## What the audit needs to determine

1. Read Simpson (2012): what exactly IS the smallest measure-1
   σ-sublocale? How is it constructed? What properties does it have?
2. For St(B) specifically: what does the construction give?
3. Is spatiality of this sublocale equivalent to anything already
   known (e.g., Radon-ness, τ-additivity, regularity)?
4. Has anyone else connected Simpson's work to σ-additivity of
   charges on Boolean algebras?

## Risk assessment (from thesis advisor)

- This is "learn a new field to prove one theorem"
- Locale-theoretic measure theory is adjacent to but not overlapping
  with Stone duality expertise
- The conjecture was formulated BEFORE reading the primary literature
- The pipeline says: read Simpson first, THEN assess tractability

## Status: DEAD (2026-05-16, Phase 2 audit)

The conjecture collapses in both directions:

**⟸ FALSE:** Take B = P(ω), U a free ultrafilter, ℓ = δ_U (purely
finitely additive). The measure on βω is a Dirac mass at the point
U. Simpson's smallest measure-1 sublocale = {U}, which is trivially
spatial. CE fails but spatiality holds.

**⟹ TRIVIALLY TRUE (for all measures, not just CE):** On compact
Hausdorff spaces classically, every Radon measure has spatial support.
Simpson's sublocale is at least as large as the support → spatial
regardless of CE. Cannot distinguish CE from non-CE.

**Root cause:** The non-spatiality phenomenon in Simpson's work is
CONSTRUCTIVE — it's about algorithmically random points that can't be
exhibited without choice. In classical mathematics with full AC (which
is where Stone duality, ultrafilters, and Yosida-Hewitt live), the
phenomenon disappears. The locale machinery doesn't bite classically.

**Consequence for the programme:** Simpson's σ-sublocale is not the
right tool for characterizing CE frame-internally. The condition
"μ̂(pure(Ω)) = 1" is inherently about POINTS — exactly what locale
theory abstracts away from. A frame-internal CE characterization
(beyond Layer 1: σ-additivity on clopens) may not exist.
