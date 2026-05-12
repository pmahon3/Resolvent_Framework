# The Structure of Coherence Conditions

## The question

Are the four coherence levels a linear hierarchy, or is the
structure richer?

## The four conditions

1. **Consistency** — a 2-valued homomorphism exists on each
   Boolean context separately
2. **Contextual coherence** — a state s : A → [0,1] exists
   (compatible across all contexts)
3. **Probabilistic coherence** — s extends to a σ-additive
   measure on the dual space
4. **Value-definite coherence** — a dispersion-free state exists
   (global 2-valued homomorphism)

## Three kinds of obstruction

| Transition | Kind | Obstruction | Territory |
|-----------|------|-------------|-----------|
| 1 → 2 | Scope (pasting) | Contextuality | Abramsky-Brandenburger |
| 2 → 3 | Regularity (continuity) | σ-additivity | Paper I |
| 3 → 4 | Sharpness (collapse to {0,1}) | Kochen-Specker | Algebraic |

These are three different KINDS of obstruction:
- Topological (do local sections paste?)
- Analytic (does the pasted section have good limits?)
- Algebraic (can probabilities be sharpened to certainties?)

## Is the ordering forced?

Question: does 4 ⟹ 3 ⟹ 2 ⟹ 1?

- 4 ⟹ 2: YES. A dispersion-free state is a state (it's additive
  on orthogonal pairs, with values in {0,1} ⊂ [0,1]).
- 4 ⟹ 3: Does a dispersion-free state automatically give a
  σ-additive measure? On a Boolean algebra, yes (ultrafilters
  give point masses, which are σ-additive). On an OML, the
  question is moot because 4 fails.
- 3 ⟹ 2: YES. A σ-additive measure restricts to a state.
- 2 ⟹ 1: YES. A global state restricts to each context.

So the IMPLICATION chain 4 ⟹ 3 ⟹ 2 ⟹ 1 does hold (where
it makes sense). The issue is: are the converses independent?

- 1 ⇏ 2: Can you have consistent contexts that don't paste?
  YES — this is contextuality. Abramsky-Brandenburger examples.
- 2 ⇏ 3: Can you have a state that's not σ-additive?
  YES — this is Paper I. Finitely additive charges.
- 3 ⇏ 4: Can you have a σ-additive measure with no
  dispersion-free state? YES — this is Kochen-Specker.

So the converses are independently falsifiable. The four levels
ARE linearly ordered by implication, and the converses fail at
each step for different reasons.

## But are they on the same axis?

The implications hold, but the OBSTRUCTIONS are on different axes:

```
         Scope          Regularity       Sharpness
    1 --------→ 2 ----------→ 3 ----------→ 4
      pasting     continuity    collapse
      (sheaf)     (analytic)    (algebraic)
```

The transitions live on different mathematical axes. Calling this
a "hierarchy" is technically correct (it's a linear order) but
potentially misleading (it suggests the steps are of the same
kind).

## Alternative framings

### Option A: Keep the hierarchy, name the axes

Present it as a hierarchy but label each transition with its
mathematical character:

"Four levels of coherence, connected by three different kinds
of obstruction: pasting (topological), continuity (analytic),
and sharpening (algebraic)."

### Option B: Grid structure

Two dimensions:
- Extension (local → global → σ-additive)
- Sharpness (probabilistic → deterministic)

```
                  Extension →
              Local    Global    σ-additive
Sharpness ↑
Deterministic   1d      ??        4
Probabilistic   1p      2         3
```

Where:
- 1p = local probabilistic consistency (trivial)
- 1d = local deterministic consistency (level 1)
- 2 = global probabilistic (state, level 2)
- 3 = σ-additive probabilistic (level 3)
- 4 = σ-additive deterministic (level 4)
- ?? = global deterministic without σ-additivity

The "??" cell is interesting: can you have a global 2-valued
homomorphism that's not σ-additive? On a Boolean algebra, every
2-valued homomorphism is automatically σ-additive (it's a point
mass). So "??" = automatic for Boolean. For OMLs, the question
is moot because even "??" fails (KS).

This means the grid partially collapses:

- Boolean: the sharpness dimension collapses (deterministic =
  probabilistic at every extension level). The grid is 1D.
- OML: the sharpness dimension opens up. The grid is genuinely 2D.

### Option C: Flag bundle

The coherence conditions form a "flag" — a nested chain of
subspaces:

States ⊇ σ-additive states ⊇ dispersion-free states

The question at each level is which of these subsets is non-empty.
The flag is the natural linear ordering. The obstructions
(contextuality, non-σ-additivity, KS) are the reasons each
inclusion can be strict.

## Assessment

The hierarchy IS genuinely linear (implications hold). But the
transitions are of three different mathematical characters. The
most honest presentation:

**Keep the hierarchy, but present it as a filtration with three
named obstruction types.** Don't call it "four levels on the same
ladder" — call it "three doors, each requiring a different key."

The grid structure (Option B) is more informative but harder to
present. It might be better for a technical audience.

The flag structure (Option C) is the cleanest mathematical
framing: it's a descending chain of subsets of the state space.
