# Operational Boundary Theorem — Specification

*Working note — 2026-05-20*

## Statement (informal)

Let (G_k, Λ) be a valued refinement system on a Boolean algebra B
with resolution dimension D_Λ.  Let μ = μ_c + μ_p be the
Yosida-Hewitt decomposition of a probability charge on B, with
ε = ‖μ_p‖.  Suppose μ_c has Hölder-type smoothness s relative to
the valuation scale.

Given n i.i.d. samples from μ observed at resolution G_k, the
minimax rate for estimating the σ-additive component μ_c at the
optimal resolution k*(n) is:

  R(n, s, D, ε) ≍ n^{−2s/(2s+D)} ∨ ε^{2s/(s+1)}

where the first term is the classical nonparametric rate (with D_Λ
replacing ambient dimension) and the second is the contamination
floor.

## Precise setup

### Refinement system

(G_k)_{k≥0}: increasing sequence of finite Boolean subalgebras of B.
N_k = |At(G_k)|.  Valuation Λ(k).  Resolution dimension:

  D_Λ = lim sup_k  log N_k / Λ(k).

Assume D_Λ exists as a limit (not just lim sup) and is finite
positive.

### Charge decomposition

μ is a probability charge (μ(B) = 1, μ ≥ 0, finitely additive).
YH decomposition: μ = (1−ε)μ_c + ε μ_p where μ_c is a σ-additive
probability, μ_p is a purely finitely additive probability, and
ε = ‖μ_p‖ ∈ [0,1].

At each resolution k, both μ_c and μ_p restrict to probability
distributions on At(G_k):

  p^(k) = μ_c|_{G_k},  q^(k) = μ_p|_{G_k}.

The observation model at resolution k is multinomial with
probabilities:

  r^(k) = (1−ε)p^(k) + ε q^(k).

This is Huber's ε-contamination model on a finite alphabet of
size N_k.

### Smoothness

μ_c has smoothness s relative to Λ if: the bias of approximating
μ_c by its restriction to G_k satisfies

  ‖μ_c − Proj_{G_k} μ_c‖ ≤ C · e^{−s Λ(k)}.

This is the analogue of Hölder β-smoothness in the valued-
refinement setting.  "Proj" here means the conditional expectation
/ coarsening to G_k.

Actually: μ_c|_{G_k} is exact (restriction, not approximation).
The bias comes from using G_k to estimate a functional of μ_c
that lives at a finer resolution.  Need to specify the estimation
target precisely.

### Estimation target

**Option A (density estimation analogue):** Estimate the probability
vector p^(k) at a specified resolution k from n samples.  The error
is ‖p̂_n − p^(k)‖² where p̂_n is some estimator.

At fixed k, this is multinomial estimation with contamination:
- Variance: O(N_k / n)
- Contamination bias: O(ε²) (from Liu-Gao)
- No smoothness parameter s — this is just finite alphabet
  estimation.

To get the rate n^{−2s/(2s+D)}, we need to OPTIMIZE over k,
introducing a bias term from the approximation.

**Option B (functional estimation):** Estimate μ_c(A) for some
A ∈ σ(∪_k G_k) that may not belong to any single G_k.  The bias
from using G_k comes from approximating A by elements of G_k.

This is closer to the density estimation setup: the "resolution" k
controls the bias/variance tradeoff.

**Option C (distribution estimation in TV):** Estimate μ_c in total
variation over ∪_k G_k.  The bias at level k is the TV distance
between μ_c and its best G_k-measurable approximation.

## The bias/variance/contamination tradeoff

At resolution k:

1. **Variance:** Estimating a distribution on N_k atoms from n
   samples has squared error O(N_k/n) = O(e^{D·Λ(k)}/n).

2. **Approximation bias:** The target μ_c is approximated by its
   restriction to G_k with error O(e^{−s·Λ(k)}) (smoothness s).

3. **Contamination bias:** The PFA component contributes
   ε · q^(k) to the observations.  Under arbitrary contamination,
   the irreducible cost is O(ε^{2β₀/(β₀+1)}) in the Liu-Gao
   framework, where β₀ is the target smoothness.

   In the finite-alphabet setting at resolution k, the
   contamination cost is simpler: the empirical estimator targets
   r^(k) = (1−ε)p^(k) + ε q^(k), and the bias for estimating
   p^(k) from observations of r^(k) is ε · ‖q^(k) − p^(k)‖,
   which is O(ε) in TV, O(ε²) in squared loss.

Total squared error at resolution k:

  E_k(n) ≍ e^{D·Λ(k)}/n + e^{−2s·Λ(k)} + ε²

Optimizing over k: the first two terms balance at
Λ(k*) = log(n)/(2s+D), giving the rate n^{−2s/(2s+D)}.

The total optimal rate is:

  R*(n) ≍ n^{−2s/(2s+D)} ∨ ε²

## What's the theorem?

The formula R*(n) ≍ n^{−2s/(2s+D)} ∨ ε² has three ingredients:

(a) The nonparametric rate on G_k is controlled by N_k ≍ e^{D·Λ(k)}.
(b) The approximation bias decays as e^{−s·Λ(k)} (smoothness).
(c) The contamination floor is ε² (PFA mass).

Each ingredient is known:
- (a) is standard multinomial estimation.
- (b) is the definition of smoothness in the refinement system.
- (c) is Huber / Liu-Gao.

The theorem's content is: **in the valued-refinement framework,
(a)-(c) combine to give R* with D_Λ as the dimension parameter,
and the crossover between the n-dependent and ε-dependent regimes
occurs at n ∼ ε^{−(2s+D)/s}.**

## Is this more than a substitution?

The honest question: is D_Λ doing real work, or is this just
"replace d by D_Λ in a known formula"?

D_Λ does real work IF:
1. The valued-refinement setting covers examples where the standard
   Liu-Gao setup doesn't apply (non-Euclidean, non-metric, fractal,
   Boolean-algebraic refinements).
2. The proof requires verifying non-trivial conditions on the
   refinement system (metric entropy bounds, moment conditions)
   that are not automatic.
3. The ε² floor has different structure in the Boolean-algebraic
   setting (e.g., the PFA component's restriction to G_k has
   properties that arbitrary contamination doesn't).

Point 1 is the strongest: the valued-refinement framework applies
to the Cantor system (D = log2/log3), spectral refinements, logical
refinements, and other non-Euclidean settings where Liu-Gao's ℝ^d
framework doesn't directly apply.

Point 3 might yield something: the PFA component is not arbitrary
contamination — it is a PFA charge, which means it satisfies finite
additivity across resolutions.  This structural constraint might
give a tighter bound than the worst-case ε² from Liu-Gao.

## Floor inconsistency (resolved)

Lines above had two different floors: ε² (bare multinomial) and
ε^{2s/(s+1)} (Liu-Gao smoothness-leveraged). These are different.

In Liu-Gao, the contamination floor depends on smoothness because
the estimator can smooth over local contamination — higher
smoothness lets you average over more cells, diluting the
contamination.  Their three-term rate is:

  R_LG ≍ n^{−2β₀/(2β₀+d)} ∨ ε^{2(1∧m)}  ∨  n^{−2β₁/(2β₁+d)} ε^{2/(2β₁+d)}

where β₀ is target smoothness, m = β₀/d, β₁ = β₀/(1+β₀).

In our setting at fixed resolution k: estimation of p^(k) on N_k
atoms with contamination ε is multinomial — no smoothness structure
within a single level.  The contamination bias is O(ε) in TV,
O(ε²) in squared loss.  This is the correct single-level floor.

Smoothness enters when OPTIMIZING over k: the approximation bias
e^{−s·Λ(k)} is the analogue of Liu-Gao's inter-scale structure.
But within a given level, there's no kernel smoothing — we're
on a finite set.

**Resolution:** The correct floor in our setting is ε² (squared
loss) at each level.  The Liu-Gao ε^{2β₀/(β₀+1)} floor comes
from their specific kernel estimator leveraging within-level
smoothness — which is absent in the multinomial-on-atoms setup.

HOWEVER: multi-resolution structure changes this.  See below.


## Key question for novelty

Does the finite-additivity constraint on μ_p give a tighter
contamination floor than arbitrary contamination?


## Multi-resolution analysis (the key calculation)

### Setup: Cantor system as test case

B = Clop({0,1}^N), G_k = k-bit cylinder algebra.  N_k = 2^k.
Λ(k) = k log 2.  D_Λ = 1.

Take μ_p = δ_U (ultrafilter charge).  At resolution k:
  q^(k) = δ_{A_U^(k)}  (point mass on one atom).

Observation distribution:
  r^(k)(A) = (1−ε)p^(k)(A) + ε·1_{A = A_U^(k)}.

### The chain structure

The contaminated atoms A_U^(1) ⊇ A_U^(2) ⊇ ... form a nested
chain.  At each level, exactly one atom carries excess mass ε.
Each A_U^(k) refines to exactly one contaminated child at level
k+1.

In ARBITRARY contamination (Liu-Gao model applied level by level),
the contamination at level k is independent of the contamination
at level k+1.  Any atom could be contaminated at each level
independently.

In PFA contamination, the contaminated atoms MUST form a chain.
This is a structural constraint.

### Detection via chain test

Consider a test: at each level k, identify the most suspicious
atom (largest empirical mass minus expected).  Under PFA
contamination, these must form a chain.  Under no contamination,
they are essentially independent.

Signal at level k: excess mass ε on one atom out of 2^k.
Noise: empirical fluctuation O(1/√n) per atom.

The signal-to-noise per level: ε√n.  This is < 1 precisely when
n < 1/ε² (the interesting regime where contamination floor
dominates the 1/n sampling rate).

BUT: the chain constraint gives CUMULATIVE information.  If we
observe K levels, the probability of the suspicious atoms forming
a chain by chance is:

  P(chain | H₀) ≈ ∏_{k=1}^{K-1} (1/2) = 2^{−(K−1)}

(At each level, the child of the previous suspicious atom is
itself the most suspicious atom with probability ≈ 1/2 under
uniformity.)

Under contamination (H₁): P(chain | H₁) ≈ 1 (the signal
guarantees the chain, up to noise).

So a chain test achieves:
  - Type I error: 2^{−K}
  - Power: ~1 (when ε√n is not too small)

This means: with K = log₂(1/α) levels, we can detect PFA
contamination with confidence 1−α.  Detection is possible even
when ε√n = O(1), because the chain structure provides geometric
amplification of a weak per-level signal.

### Quantifying the improved floor

After detecting the chain, the estimator can SUBTRACT the
contamination along the detected chain.  The subtraction error
is O(1/√n) per level (estimation error of the excess mass).

Post-subtraction squared error: O(1/n) per atom along the chain,
summed over K levels = O(K/n).

The contamination floor becomes:
  - Detection: succeeds when K ≳ log(n)/log(2) (exponential
    amplification beats the per-level ambiguity)
  - Subtraction: adds O(K/n) = O(log(n)/n) error

So the PFA contamination floor is NOT ε².  It is:

  O(1/n · log n)   (when detection succeeds)

OR more precisely: detection succeeds when n ≳ (1/ε²) · (1/K),
i.e., the threshold for detection is LOWER than the n ~ 1/ε²
needed for single-level detection.

WAIT — this needs more care.

### Careful analysis

At level k, the empirical mass on atom A is:
  r̂_n(A) = (#{samples in A})/n ~ Binomial(n, r^(k)(A))/n.

Under contamination on atom A₀ = A_U^(k):
  E[r̂_n(A₀)] = (1−ε)p^(k)(A₀) + ε
  Var(r̂_n(A₀)) = r^(k)(A₀)(1−r^(k)(A₀))/n ≤ 1/(4n).

The excess mass ε is detectable at level k when:
  ε >> √(1/n)  ⟺  n >> 1/ε².

This is the SAME threshold as before.  The per-level SNR is ε√n.

Now, the chain test across K levels.  The test statistic is:
  T = ∑_{k=1}^{K} Z_k where Z_k = 1 if child of level-k winner
      is the level-(k+1) winner.

Under H₁: E[Z_k] → 1 as ε√(n/N_k) → ∞.  But n/N_k = n/2^k
decreases with k.  At level k, SNR is ε√(n/2^k)... no wait.

Actually: we observe n samples total, not n per level.  A sample
in atom A ∈ At(G_K) contributes to all coarser levels.  At level
k, the effective sample size in each atom is ~n/N_k = n/2^k on
average.  So:

  Std dev of r̂_n(A) at level k ≈ √(1/(n/N_k)) · (1/N_k)
    ... no, this is multinomial.

Let me be precise.  We have n i.i.d. samples from the true
distribution r^(K) on At(G_K) (the finest observed level).
The coarsening to level k just sums: r̂^(k)(A) = ∑_{A'⊆A} r̂^(K)(A').

For a single atom A at level k:
  n · r̂^(k)(A) ~ Binomial(n, r^(k)(A)).
  Var(r̂^(k)(A)) = r^(k)(A)(1−r^(k)(A))/n.

If p^(k) is roughly uniform: p^(k)(A) ≈ 1/N_k = 1/2^k.
Then r^(k)(A₀) ≈ (1−ε)/2^k + ε for the contaminated atom.
And Var ≈ [(1−ε)/2^k + ε] · [1 − ...] / n ≈ ε/n (for ε >> 1/2^k).

The signal (excess over neighbors): ε − 0 = ε (contaminated atom
has ε more mass than a typical atom).
The noise: √(ε/n).

SNR at level k: ε / √(ε/n) = √(nε).

This is INDEPENDENT of k!  The SNR for detecting the contaminated
atom is √(nε) at every level (as long as ε >> 1/2^k, which holds
for k < log₂(1/ε)).

So across K ≈ log₂(1/ε) useful levels, we have K independent
tests each with SNR √(nε).  The combined evidence is:

  Combined SNR ≈ √K · √(nε) = √(K·n·ε).

Detection threshold: combined SNR > c, i.e., n > c²/(Kε).

Compare to single-level threshold: n > c²/ε² (i.e., ε√n > c).

Multi-resolution threshold: n > c²/(Kε) where K ≈ log(1/ε).
This is MUCH weaker: we need n ~ 1/(ε·log(1/ε)) rather than
n ~ 1/ε².

### The improvement

Single-level contamination floor: dominates when n < 1/ε²,
contributing ε² to squared error.

Multi-resolution detection floor: contamination detectable when
n > 1/(ε · log(1/ε)).  After detection and subtraction, the
contamination contribution to error is O(1/n) (not ε²).

So the improved rate with multi-resolution PFA-aware estimation:

  R*(n) ≍ n^{−2s/(2s+D)} ∨ (ε / (n·log(1/ε)))^{1/2}  ???

No — let me be more careful about what happens after detection.

### Post-detection analysis

Once the chain is detected, the estimator knows WHICH atoms
carry the contamination.  It can:
(a) Subtract estimated excess from those atoms.
(b) Ignore those atoms entirely and estimate p^(k) from the
    uncontaminated atoms.

Option (b): at level k, we lose one atom.  The estimator uses
(N_k − 1) atoms to reconstruct p^(k).  Since p^(k) sums to 1,
the lost atom's probability is determined by the others.  So
there's no loss in estimation rate — we just need p^(k)(A₀),
which is 1 − ∑_{A≠A₀} p^(k)(A).  The estimation error on
p^(k)(A₀) is the sum of estimation errors on the others:
O(N_k/n) in total squared error — same as before.

So post-detection, the contamination contributes NOTHING to the
error.  The rate becomes purely:

  R_post(n) = n^{−2s/(2s+D)}

with no contamination floor!

### The REAL contamination floor

The contamination floor comes from the regime where detection
FAILS: n < 1/(ε · K) = 1/(ε · log(1/ε)).

When detection fails, we're back to the single-level situation
where we can't distinguish contamination from signal, and the
contamination bias ε² remains.

But the crossover is at n ~ 1/(ε · log(1/ε)), not n ~ 1/ε².

In the Liu-Gao arbitrary-contamination model, the floor
persists until n ~ 1/ε².  With PFA structure (chain
constraint), the floor only persists until n ~ 1/(ε · log(1/ε)).

Actually wait.  If detection fails, the estimator doesn't know
which atom is contaminated, and the bias is ε at each atom,
contributing ε² to squared error.  The rate in this regime is
ε² (not n-dependent).

So the overall rate:
- If n > 1/(ε · log(1/ε)): detection succeeds, rate is n^{−2s/(2s+D)}.
- If n < 1/(ε · log(1/ε)): detection fails, rate is ε².

The crossover: n^{−2s/(2s+D)} = ε² when n = ε^{−(2s+D)/s}.
Detection threshold: n = 1/(ε · log(1/ε)).

Is the detection threshold below the crossover?
  1/(ε · log(1/ε)) vs ε^{−(2s+D)/s}
  = ε^{−1} / log(1/ε) vs ε^{−(2s+D)/s} = ε^{−2 − D/s}

Since 2 + D/s > 1 (both D, s > 0), we have ε^{−2−D/s} >> ε^{−1},
so the crossover n happens WELL ABOVE the detection threshold.
Detection succeeds long before the classical rate catches up
to ε².

THIS MEANS: the ε² floor is ELIMINATED for PFA contamination.
The rate is purely n^{−2s/(2s+D)} with no contamination floor!

### Sanity check

Is this too good?  Let me check the argument.

The claim: with K = log₂(1/ε) resolution levels, each
contributing √(nε) SNR for chain detection, the combined test
detects PFA contamination when n > c/(ε · log(1/ε)).  After
detection, subtraction eliminates the bias.

For the classical rate to equal ε²: n ~ ε^{−(2s+D)/s}.
For detection: n ~ 1/(ε · log(1/ε)).

Since (2s+D)/s > 1, the detection threshold is always reached
first.  So whenever ε² would dominate the rate, the chain test
has already detected and eliminated the contamination.

THIS IS THE THEOREM'S NOVEL CONTENT.

### Caveat: adversary adaptation

The above assumes the adversary uses an ultrafilter charge (worst
case for single-level contamination).  Could a PFA adversary do
worse by spreading the contamination?

Any PFA charge is a convex combination of ultrafilter charges
(Krein-Milman on finitely additive probabilities).  So μ_p =
∫ δ_U dν(U) for some probability ν on the ultrafilters.

At level k: q^(k) = ∫ δ_{A_U^(k)} dν(U) — a mixture of point
masses on atoms.  This is a general distribution on At(G_k),
BUT with the constraint that it arises from a measure on
ultrafilter chains.

The constraint: q^(k) and q^(k+1) must be consistent. In terms
of the mixing measure ν: this is automatic (ν doesn't depend
on k).

So the adversary can choose ANY distribution on ultrafilter
chains (= paths through the infinite binary tree).  This is a
probability measure on {0,1}^N — which can be ANY probability
measure!

Wait — that means q^(k) can be ANY probability on At(G_k)
(since any distribution on {0,1}^N marginalizes to some
distribution on k-bit strings).  So the structural constraint
is: {q^(k)} must be a CONSISTENT family (projective system),
i.e., they must come from a single measure on the inverse limit.

But {0,1}^N IS the inverse limit of the G_k system.  And any
consistent family of distributions on {G_k} comes from a
measure on {0,1}^N (Kolmogorov extension).  BUT — μ_p is PFA,
not σ-additive!  So μ_p does NOT come from a measure on {0,1}^N.
It comes from a charge.

A PFA charge on the clopen algebra of {0,1}^N has the property
that its restrictions to G_k DO form a projective system, BUT
this projective system does NOT extend to a σ-additive measure
on the product σ-algebra.

HOWEVER: the restrictions q^(k) = μ_p|_{G_k} are just
probability distributions on FINITE sets.  Any consistent
family of finite-dimensional distributions CAN be extended to
a σ-additive measure (by Kolmogorov).  So the q^(k) look
exactly like the marginals of some σ-additive measure on {0,1}^N!

THIS KILLS THE ARGUMENT.

The restrictions of a PFA charge to finite subalgebras are
INDISTINGUISHABLE from the marginals of some σ-additive measure.
Therefore: at any finite collection of resolution levels, the
contamination from a PFA charge looks exactly like contamination
from a σ-additive measure.  There is NO structural constraint
visible at finite resolution.

### Resolution

The multi-resolution chain detection idea was based on the
assumption that PFA contamination comes from a point mass
(ultrafilter charge).  But the adversary can use arbitrary
convex combinations, and the resulting finite-dimensional
marginals are unrestricted — any projective family works.

The PFA nature of μ_p is invisible at every finite resolution.
The contamination floor IS ε² — same as arbitrary contamination.

## Verdict

**The finite-additivity constraint does NOT improve the
contamination floor.**

Reason: the restrictions of a PFA charge to finite Boolean
subalgebras form a projective system that is indistinguishable
from the marginals of some σ-additive measure.  The PFA
character only manifests in the infinite limit (failure to
extend to the generated σ-algebra) — which is never observed
at any finite resolution.

This is precisely the "epistemic inaccessibility" observation
from the original operational boundary seed note: the boundary
between σ-additive and PFA cannot be seen at any finite
resolution.  It can only be felt operationally through the
rate at which estimation converges — and that rate is the same
whether the contamination is PFA or arbitrary.

## Revised assessment

The theorem R*(n) ≍ n^{−2s/(2s+D_Λ)} ∨ ε² is:
1. Correct.
2. A valid instantiation of Liu-Gao in the refinement setting.
3. NOT novel beyond the substitution D_Λ for d.
4. The PFA structural constraint adds nothing to the minimax rate.

Per CLAUDE.md: "Park honestly. If known, stop."

The operational boundary observation (PFA manifests as
convergence-rate plateau) is already folded into lit review §2.9.
The theorem adds no new mathematics beyond what's in Liu-Gao
(1−ε contamination on finite alphabets) plus the
bias-variance-resolution tradeoff (standard nonparametric theory).

## What was learned

The ultrafilter charge argument (single-scale adversary is bad)
is correct but misleading.  The real insight is deeper:

**Kolmogorov extension theorem guarantees that any PFA charge
looks σ-additive at finite resolution.**

This is why the boundary is epistemically inaccessible.  It's
not just "hard to detect" — it's provably indistinguishable
at any finite stage.  The Kolmogorov extension theorem is the
mechanism behind the inaccessibility.

This observation strengthens the §2.9 synthesis paragraph
and should be added there.

## Status: PARK (the chain-detection route)

The chain-detection route does not yield a new theorem.  The rate
formula is correct but routine.  The novel-sounding PFA structure
is invisible at finite resolution by Kolmogorov extension.
Folded as strengthened exposition in §2.9.


# ================================================================
# PART II: The ε̂(n) trajectory
# ================================================================

*2026-05-20 — new direction, post Kolmogorov-extension kill*

## The shift

The Kolmogorov extension kill says: at fixed n, you cannot
distinguish PFA from σ-additive.  But it does NOT say: the
*sequence* ε̂(n) as n → ∞ is uninformative.

The kill operates at each finite resolution separately.  It says
nothing about the *dynamics* of how the answer evolves with data.

New object: ε̂(n) = the minimum PFA mass compatible with n
observations, under smoothness assumptions on the σ-additive part.

## Definition

### The variational problem

Fix a refinement system (G_k, Λ) and smoothness class S_s = the
set of σ-additive probabilities μ_c on B satisfying:

  ‖μ_c|_{G_k} − μ_c|_{G_j}‖_TV ≤ C · e^{−s·Λ(j)}  for j ≤ k.

(Approximation quality of coarser by finer level.)

Given n i.i.d. samples X_1,...,X_n from the true charge μ,
observed at resolution G_K (the finest accessible level), define:

  ε̂(n) = inf { ε ∈ [0,1] :
    ∃ p ∈ S_s, ∃ probability q on At(G_{k*(ε,n)}),
    such that ‖r̂_n − (1−ε)p − ε q‖² ≤ δ²(n, k*(ε,n)) }

where:
- r̂_n is the empirical distribution on At(G_{k*})
- k*(ε, n) is the resolution that balances variance and
  approximation bias given contamination ε:
  Λ(k*) = log(n/(1 + nε²)) / (2s + D)  [approximately]
- δ²(n,k) = C · N_k/n is the sampling tolerance (multinomial
  concentration)

Informally: ε̂(n) is the smallest contamination fraction such that
the empirical distribution at the optimal resolution is within
sampling error of some (smooth σ-additive) + ε·(arbitrary) mixture.

### Optimization over k

The resolution k itself depends on ε (because contamination
changes the optimal resolution).  This creates a fixed-point
problem:

  k*(ε) optimizes the bias-variance tradeoff given contamination ε.
  ε̂(n) is the smallest ε such that the data is compatible with
  S_s at resolution k*(ε).

In practice this is solved by profiling: for each candidate ε,
compute k*(ε), check compatibility, and take the infimum.

## The two regimes (the theorem candidate)

### Claim

Under regularity conditions on the refinement system:

(A) If μ is σ-additive with smoothness s (ε₀ = 0):
    ε̂(n) = O(n^{−s/(2s+D)})  almost surely.

(B) If μ has PFA mass ε₀ > 0:
    ε̂(n) → ε₀ as n → ∞,
    and ε̂(n) ≥ ε₀ − O(n^{−s/(2s+D)}) for large n.

### Why (A) holds

If the true μ is σ-additive with smoothness s, then the empirical
distribution at optimal resolution k*(n) satisfies:

  ‖r̂_n − p^(k*)‖ = O(√(N_{k*}/n)) = O(n^{−s/(2s+D)})

(This is the classical rate.)  So ε = 0 is compatible with the
data up to error δ(n) = O(n^{−s/(2s+D)}).  Therefore ε̂(n) ≤ δ(n).

More precisely: ε̂(n) = 0 with high probability once n is large
enough (the true p is in S_s and the empirical is within tolerance
of it with ε = 0).

### Why (B) holds

If μ has genuine PFA mass ε₀ > 0, the observation distribution is:

  r^(k) = (1−ε₀)p^(k) + ε₀ q^(k).

At resolution k, the empirical r̂_n converges to r^(k).  For
large n, r̂_n ≈ r^(k).

Now: can r^(k) be explained as a smooth distribution with ε < ε₀?
Only if (1−ε₀)p^(k) + ε₀ q^(k) ≈ (1−ε)p' + ε q' for some
p' ∈ S_s|_{G_k} and ε < ε₀.

Rearranging: p' ≈ [(1−ε₀)p + ε₀ q − ε q'] / (1−ε).

For p' to be in S_s (smooth), it must satisfy the approximation
bounds across resolutions.  The term ε₀ q^(k) introduces structure
at resolution k that CANNOT be explained by a smooth p' without
invoking contamination mass at least ε₀.

WHY?  Because q^(k) (the PFA restriction) can have arbitrarily
high-frequency structure relative to p^(k).  More precisely:
the PFA component is not constrained to be smooth — it can put
mass on individual atoms in patterns that violate the smoothness
bound.  To absorb this mass into p', you'd need p' to deviate
from S_s by O(ε₀).  The only alternative is to "spend"
contamination budget ε ≥ ε₀ − O(δ(n)).

Key: this is where the smoothness assumption S_s does real work.
Without a smoothness constraint on μ_c, you can't distinguish
μ_c from μ_p at all (both are just distributions on finite sets).
WITH smoothness, the PFA component's high-frequency structure
becomes incompatible with the smooth class as resolution increases.

### The convergence diagnostic

The observable is the TRAJECTORY of ε̂(n):

- σ-additive: ε̂(n) ~ n^{−s/(2s+D)} → 0 polynomially.
- PFA mass ε₀: ε̂(n) → ε₀ > 0, stabilizing.

A RATE TEST distinguishes these:

  Test: does ε̂(n) · n^{s/(2s+D)} → 0 or → ∞?

  Under H₀ (σ-additive): the product → constant (rate-matched).
  Under H₁ (PFA mass): the product → ∞ (ε̂ decays slower than
  the σ-additive rate).

This is a well-defined hypothesis test.  And it is NOT blocked
by Kolmogorov extension, because:

- Kolmogorov extension says: at fixed n, you can't distinguish.
- The rate test says: the SEQUENCE ε̂(1), ε̂(2), ..., ε̂(n) has
  different asymptotics under H₀ vs H₁.

The boundary is invisible at any single snapshot but visible
in the dynamics.

## Why Kolmogorov extension doesn't kill this

At each fixed n, the data is compatible with BOTH hypotheses.
There exists a σ-additive explanation AND a PFA explanation.
Kolmogorov extension guarantees this.

But: under H₀, the σ-additive explanation with ε = 0 becomes
INCREASINGLY tight (the tolerance δ(n) shrinks to 0).  Under H₁,
it doesn't — the minimum ε stays bounded away from 0.

The distinction is asymptotic, not pointwise.  No single
observation distinguishes.  The sequence does.

This is exactly the sense in which the boundary is "felt" without
being "seen": you can never say at finite n "there IS PFA mass."
But you can say "the rate at which the PFA-free explanation
improves is slower than it should be under σ-additivity."

## Connection to Lepski / adaptive estimation

The trajectory ε̂(n) is closely related to Lepski's adaptive
bandwidth selection:

- Lepski's method: increase resolution until the estimate stops
  improving.  The stopping point detects the effective smoothness.

- ε̂(n) trajectory: as n increases, check whether the minimum
  contamination needed decreases at the σ-additive rate.  If it
  doesn't, the effective smoothness is exhausted — you've hit the
  contamination floor.

The difference: Lepski adapts k given fixed n.  The ε̂(n)
trajectory adapts the INTERPRETATION given increasing n.

## What's the theorem, precisely?

### Statement (candidate)

Let (G_k, Λ) be a valued refinement system with resolution
dimension D_Λ ∈ (0,∞).  Let S_s be a smoothness class relative
to Λ.  Let μ be a probability charge on B with Yosida-Hewitt
decomposition μ = (1−ε₀)μ_c + ε₀ μ_p.

Define ε̂(n) as the minimum-contamination estimator (variational
problem above).  Then:

(i)  If ε₀ = 0 (σ-additive): ε̂(n) = O_P(n^{−s/(2s+D_Λ)}).

(ii) If ε₀ > 0 (PFA mass): ε̂(n) → ε₀ a.s., and for all
     δ > 0, P(ε̂(n) < ε₀ − δ) → 0.

(iii) The rate test T_n = ε̂(n) · n^{s/(2s+D_Λ)} satisfies:
      - Under H₀: T_n = O_P(1).
      - Under H₁: T_n → ∞ in probability.

     Therefore T_n is a consistent test for the presence of PFA
     mass (power → 1 as n → ∞).

### What's new here?

(i) is essentially the minimax rate (the smooth component is
estimable at rate n^{−s/(2s+D)}, so ε̂ inherits this rate).
This is known.

(ii) is the consistency of the minimum-contamination estimator
for the true ε₀.  This is related to but not identical to
Huber's contamination estimation literature.  In Huber's model
the contamination fraction is a fixed parameter; here ε₀ is
determined by the Yosida-Hewitt decomposition.

(iii) is the new content: the rate of ε̂(n) discriminates the
two regimes.  This is a CONSISTENT TEST for PFA mass.

But: consistent tests with power → 1 as n → ∞ are not novel per
se.  The question is whether the rate of convergence to power 1,
and the structure of the test, has new content.

## Critical gap in the argument

The argument for (ii) relies on: "q^(k) can have arbitrarily
high-frequency structure that smooth p' can't absorb."

But: Kolmogorov extension says the adversary can choose q^(k)
to BE the marginals of some σ-additive measure.  So q^(k) CAN
be smooth!

If the adversary chooses μ_p to be a PFA charge whose
finite-resolution marginals happen to be smooth (i.e., q^(k) ∈ S_s
for all k), then:

  r^(k) = (1−ε₀)p^(k) + ε₀ q^(k) = (1−ε₀)p^(k) + ε₀ q^(k)

And (1−ε₀)p + ε₀ q is a convex combination of two smooth
distributions — which is itself smooth!

In this case: ε̂(n) → 0 even though ε₀ > 0.  The rate test
has NO power against smooth PFA contamination.

### Is smooth PFA contamination possible?

YES.  Take any σ-additive probability ν on the Cantor space
{0,1}^N with smooth marginals.  Its marginals q^(k) = ν|_{G_k}
are smooth.  Now: the PFA charge μ_p with the SAME marginals
(which exists by Kolmogorov extension — wait, no, Kolmogorov
extension gives the σ-additive measure ν itself, not a PFA charge
with those marginals).

Actually: can a PFA charge have the same finite-resolution
marginals as a σ-additive measure?

YES — this is exactly what Kolmogorov extension says (in reverse).
Given a σ-additive ν, there exists a PFA charge with the same
marginals on all G_k?  No — the σ-additive ν IS the unique
extension.  A different PFA charge with the same marginals on all
G_k would have to agree with ν on all of ∪_k G_k, which generates
the full σ-algebra, so by density they'd agree on σ(∪_k G_k)...
but a PFA charge is only defined on the algebra, not the σ-algebra.

Let me be more precise.  On the ALGEBRA B = ∪_k G_k (not its
σ-closure):

- ν restricted to B is σ-additive (ν is a measure on the σ-algebra,
  its restriction to B is σ-additive).
- A PFA charge μ_p on B with μ_p|_{G_k} = ν|_{G_k} for all k
  must agree with ν on ∪_k G_k = B.  So μ_p = ν on B.  But ν|_B
  is σ-additive.  Contradiction: μ_p was supposed to be PFA.

THEREFORE: a PFA charge CANNOT have the same marginals as a
σ-additive measure on all G_k.

Wait — this contradicts what I said in the Kolmogorov extension
kill above!  Let me re-examine.

### Re-examining the Kolmogorov extension argument

The kill argument said: "the restrictions of a PFA charge to
finite subalgebras form a projective system that is
indistinguishable from the marginals of some σ-additive measure."

But what I just showed is: if a charge agrees with a σ-additive
measure on ALL finite subalgebras G_k, then it agrees on the
whole algebra B = ∪_k G_k, and hence IS σ-additive on B.

So the Kolmogorov extension argument was WRONG?

No — the subtlety is:

The projective system {q^(k)}_{k≥0} CAN be extended to a
σ-additive measure ν on σ(∪_k G_k) by Kolmogorov extension.
But that ν is defined on the σ-ALGEBRA, not just the algebra B.

The PFA charge μ_p is defined on B.  Its marginals {q^(k)} are
also the marginals of ν.  But μ_p ≠ ν|_B!

Wait, that CAN'T be right either.  If μ_p and ν agree on every
G_k, and B = ∪_k G_k, then for any E ∈ B, E ∈ G_k for some k,
so μ_p(E) = q^(k)(E) = ν(E).  Therefore μ_p = ν on B.

But ν|_B is σ-additive.  So if μ_p agrees with ν on all finite
subalgebras, μ_p is σ-additive.  Contradiction.

THEREFORE: the marginals of a PFA charge on B = ∪_k G_k CANNOT
be the same as the marginals of any σ-additive measure.

THE KOLMOGOROV EXTENSION KILL WAS WRONG.

### What went wrong in the kill argument

The error was: "Any consistent family of finite-dimensional
distributions CAN be extended to a σ-additive measure (by
Kolmogorov)."

This is true — but the σ-additive measure lives on the
σ-ALGEBRA σ(B), not on B.  And the PFA charge μ_p is defined
on B = ∪_k G_k.  If μ_p's marginals matched ν's marginals on
every G_k, then μ_p = ν on B (since B = ∪_k G_k).  But ν|_B
is σ-additive.  So μ_p would be σ-additive.  Contradiction.

The correct statement: the marginals {q^(k)} of a GENUINELY PFA
charge on B = ∪_k G_k form a projective system that does NOT
extend to a σ-additive measure on B.  It extends to a σ-additive
measure on σ(B) by Kolmogorov — but that extension, restricted
back to B, gives a DIFFERENT charge (the σ-additive part from YH).

So the marginals of μ_p are NOT the marginals of any σ-additive
measure on B.

But wait: at any FINITE collection of levels {G_1,...,G_K}, can
the marginals {q^(1),...,q^(K)} be those of a σ-additive measure?

YES — any finite projective family extends to a σ-additive measure
on σ(G_K) = G_K (since G_K is a finite algebra, every charge on it
is σ-additive).  So at any FINITE stage, q^(1),...,q^(K) look like
the marginals of a measure on At(G_K).

The distinction: at any FIXED finite K, indistinguishable.  But as
K → ∞, the family {q^(k)} reveals itself as non-extendable.  This
is an ASYMPTOTIC property, visible only in the limit.

### Reconciliation

The Kolmogorov extension kill IS correct in the following sense:
at any fixed finite resolution (fixed K), a PFA charge is
indistinguishable from a σ-additive measure.  No finite-sample
test at fixed resolution can distinguish them.

But the ε̂(n) trajectory operates in a DIFFERENT limit: n → ∞
with K = k*(n) → ∞.  As n grows, the optimal resolution k*(n)
also grows.  In this joint limit (n → ∞, k → ∞), the PFA
structure DOES become visible — because you're eventually probing
all resolutions.

The key insight: the boundary is invisible at fixed resolution,
but visible in the TRAJECTORY of increasing resolution driven by
increasing data.

This is the precise sense of "felt but not seen":
- At any snapshot: can't see it (Kolmogorov extension at finite K).
- In the trajectory: can feel it (the sequence ε̂(n) reveals the
  asymptotic failure of extendability).

## Revised theorem statement

The critical insight is that k*(n) → ∞ as n → ∞.  As k grows,
the PFA charge's marginals reveal their non-extendability.

Specifically: if μ_p is genuinely PFA on B = ∪_k G_k, then
{q^(k)}_{k≥0} is a projective system that does NOT extend to a
σ-additive measure on B.  This means: there exists a sequence of
events (E_k) with E_k ∈ G_k, E_k ↓ ∅, such that μ_p(E_k) ↛ 0.

(This is the definition of non-σ-additivity: a vanishing sequence
whose charges don't vanish.)

At resolution k, q^(k)(E_k ∩ At(G_k)) = μ_p(E_k) ≥ c > 0 for
all k.  But E_k has N_k · e^{−αk} atoms (it's getting smaller),
so q^(k) puts mass ≥ c on a set of ≤ N_k · e^{−αk} atoms.

This means: q^(k) has at least c mass concentrated on a set of
vanishing relative size (fraction e^{−αk} of atoms).  This is a
CONCENTRATION property of q^(k) that σ-additive measures with
smoothness s cannot match.

A smooth distribution p ∈ S_s has mass on any set of m atoms
bounded by O(m/N_k + e^{−s Λ(k)}).  For the vanishing set E_k
with m ~ N_k · e^{−αk} atoms:

  p(E_k) ≤ O(e^{−αk} + e^{−s Λ(k)}) → 0.

But q^(k)(E_k) ≥ c > 0.  So r^(k)(E_k) = (1−ε₀)p(E_k) + ε₀ c
≥ ε₀ c > 0, while any smooth explanation with ε = 0 gives
r^(k)(E_k) → 0.

The incompatibility is detectable once we can estimate r^(k)(E_k)
with enough precision: need n · r^(k)(E_k) >> 1, i.e., n >> 1/(ε₀c).

AFTER that threshold: ε̂(n) cannot go below ε₀ c / (constant),
and the rate test detects PFA mass.

## Summary: what's real here

1. At fixed resolution (fixed K): PFA is invisible. (Correct, not
   killed.)

2. In the trajectory (n → ∞, k*(n) → ∞): the non-σ-additivity
   of μ_p manifests as concentration on vanishing sets — detectable
   once n is large enough.

3. The ε̂(n) trajectory has different asymptotics under H₀ (→ 0
   polynomially) vs H₁ (→ ε₀ > 0).

4. The rate test T_n = ε̂(n) · n^{s/(2s+D)} is consistent.

5. The Kolmogorov extension kill was too hasty: it applies at fixed
   K, but the estimation problem involves K growing with n.

## The smoothness-concentration bound (load-bearing calculation)

### Correct smoothness definition

The inter-resolution TV definition is wrong (marginals are exact
by definition, TV between levels is always 0 for a consistent
system).  The correct definition uses a DENSITY model:

Let λ^(k) = uniform on At(G_k) (each atom has mass 1/N_k).
Write p^(k) = f_k · λ^(k), i.e., p^(k)(A) = f_k(A)/N_k for a
function f_k: At(G_k) → ℝ_+ with ∑ f_k = N_k.

**Hölder-s smoothness on Cantor space:** The density f of μ_c
with respect to λ (uniform = coin-flipping measure) satisfies:

  |f(x) − f(y)| ≤ L · d(x,y)^s = L · 2^{−s·|x∧y|}

where |x∧y| = length of common prefix.  The Hölder ball:

  S_s(L) = { f : ‖f‖_∞ ≤ M, |f(x)−f(y)| ≤ L·d(x,y)^s }.

At level k, the atom mass is:
  p^(k)(A) = ∫_A f dλ = (f̄_A ± O(L·2^{−sk})) · 2^{−k}

where f̄_A is the average of f on A.  Therefore:

  p^(k)(A) ≤ (‖f‖_∞ + O(L·2^{−sk})) · 2^{−k} ≤ M · 2^{−k}

(bounded density ⟹ atom mass at most M/N_k).

### The ultrafilter calculation

Contamination: q^(k) = δ_{A_U^(k)} (mass 1 on one atom).
Observation: r^(k)(A_U^(k)) = (1−ε)p^(k)(A_U^(k)) + ε ≈ ε
for large k (since p^(k)(A_U^(k)) ≤ M·2^{−k} → 0).

Smooth explanation with ε' < ε: need p'(A_U^(k)) ≥ (ε−ε')/(1−ε').
This requires (ε−ε')/(1−ε') ≤ M·2^{−k}, i.e.:

  k ≤ log₂(M(1−ε')/(ε−ε'))

For ε' = 0: k ≤ log₂(M/ε).  Beyond this resolution, no smooth
explanation with ε' = 0 is compatible with the observation.

Therefore: for k > log₂(M/ε), the variational ε̂ must satisfy
ε̂ ≥ ε − M·2^{−k}·(1−ε̂).  As k → ∞: ε̂ → ε.

THIS CLOSES THE GAP FOR ULTRAFILTER CONTAMINATION.

### General PFA contamination (the hard case)

The adversary is not restricted to ultrafilter charges.  A general
PFA charge μ_p has marginals q^(k) that are arbitrary distributions
(any projective family), subject to: {q^(k)} does NOT extend to a
σ-additive measure on B.

Key question: can the adversary choose μ_p such that q^(k) ∈ S_s(L')
for some fixed L' at EVERY k?  If so, then r^(k) = (1−ε)p + εq is
a mixture of two smooth densities ⟹ smooth ⟹ ε̂ = 0 ⟹ test
has no power.

Claim: this is IMPOSSIBLE (for any fixed L').

Proof: If q^(k) has density g_k ∈ S_s(L') with respect to λ^(k),
then q^(k)(A) ≤ L'·2^{−k} for all atoms A ∈ At(G_k).  In
particular, max_A q^(k)(A) → 0 as k → ∞.

Now: μ_p is PFA on B = ∪_k G_k.  Non-σ-additivity means: ∃
sequence of events E_j ∈ B with E_j ↓ ∅ and μ_p(E_j) ≥ c > 0.

Pick j large enough that E_j ∈ G_{k_j} for some k_j, and E_j
consists of m_j atoms at level k_j.  Since E_j ↓ ∅: for any
fixed atom A ∈ At(G_K), eventually E_j ∩ A = ∅.  In particular,
at level k_j: E_j is a union of m_j atoms out of 2^{k_j}.

q^(k_j)(E_j) = μ_p(E_j) ≥ c.  But if g_{k_j} ∈ S_s(L'), then:
q^(k_j)(E_j) = ∑_{A ⊆ E_j} q^(k_j)(A) ≤ m_j · L' · 2^{−k_j}.

So: c ≤ m_j · L' · 2^{−k_j}, i.e., m_j ≥ c · 2^{k_j} / L'.

This means m_j/2^{k_j} ≥ c/L'.  The relative size of E_j at level
k_j is at least c/L'.

But E_j ↓ ∅: for j' > j, E_{j'} ⊆ E_j, so at level k_j, E_{j'}
is a subset of E_j's atoms.  As j → ∞, must have E_j ↓ ∅ —
meaning ∩ E_j = ∅.

Hmm — this doesn't immediately give a contradiction.  Let me
think more carefully.

E_j ↓ ∅ in B means: ∩ E_j = ∅ (no element of B is in all E_j).
But each E_j has relative size ≥ c/L'.  A nested sequence of
clopen sets with λ(E_j) ≥ c/L' for all j and ∩ E_j = ∅ is
IMPOSSIBLE in a compact space: clopens are closed, decreasing
nested closed sets in a compact space have non-empty intersection
(if they're all non-empty).

Wait: E_j ↓ ∅ means ∩ E_j = ∅ AND the E_j are decreasing.  In
a compact space, decreasing closed non-empty sets have non-empty
intersection.  But E_j is clopen (in B = Clop(2^N)).  If λ(E_j) ≥
c/L' > 0 for all j, then E_j ≠ ∅ for all j.  Decreasing clopens
with non-empty intersection ⟹ ∩ E_j ≠ ∅.  Contradiction with
E_j ↓ ∅.

WAIT: ∩ E_j = ∅ in B (the Boolean algebra) means there is no
E ∈ B with E ⊆ E_j for all j and E ≠ ∅.  But if E_j is clopen
in 2^N, then ∩ E_j as SUBSETS of 2^N can be non-empty (the
intersection just isn't clopen, or rather, the intersection of
the corresponding subsets of the Cantor space is non-empty but
the infimum in B is 0).

Actually, for B = Clop(2^N): the infimum of a decreasing sequence
(E_j) in B is the largest clopen below all E_j.  If ∩ E_j (as
subsets) is a closed non-empty non-clopen set, then inf_B E_j = ∅
even though the set-theoretic intersection is non-empty.

But: in the Cantor space, decreasing clopens with non-vanishing
measure ALWAYS have non-empty set-theoretic intersection (compactness).
And if the intersection is non-empty, it contains a point x.  The
singleton {x} is NOT clopen (Cantor space has no isolated points),
so inf_B E_j = ∅ is possible.  But: μ_p(E_j) ≥ c means μ_p "puts
mass on the shrinking neighborhoods of x."  And λ(E_j) ≥ c/L'
means the clopens DON'T shrink (they maintain non-trivial measure).

Hmm, this contradicts "E_j ↓ ∅ in B."  Let me re-examine.

If λ(E_j) ≥ c/L' > 0 for all j, and E_j are decreasing clopens,
then they DON'T go to ∅ in measure.  Can they go to ∅ in B?

In a σ-additive measure space: E_j ↓ ∅ ⟹ λ(E_j) → 0.  So if
λ(E_j) ≥ c/L' > 0, then E_j DOES NOT decrease to ∅ in any
σ-additive sense.

But μ_p is PFA!  The witness (E_j ↓ ∅ with μ_p(E_j) ≥ c) requires
E_j ↓ ∅ in B, which means: there is no non-zero lower bound in B.
For clopen sets in a compact space, E_j ↓ ∅ in the Boolean algebra
⟺ ∩ E_j = ∅ as subsets (since a clopen is determined by which
points it contains, and inf in the BA of clopens is ∩).

So E_j ↓ ∅ means the clopens have empty intersection.  In a compact
space: decreasing clopens with empty intersection must have
λ(E_j) → 0 (by σ-additivity of λ).

THEREFORE: if λ(E_j) → 0 is forced (by E_j ↓ ∅ in a compact space),
then the bound q^(k_j)(E_j) ≤ m_j · L' · 2^{−k_j} = L' · λ(E_j)
with λ(E_j) → 0 gives:

c ≤ q^(k_j)(E_j) ≤ L' · λ(E_j) → 0.

Contradiction for j large enough!

THIS IS THE PROOF.  A smooth PFA charge (with density bounded by
L' at every level) on a compact refinement system cannot exist,
because smoothness + E_j ↓ ∅ ⟹ q(E_j) → 0, contradicting
μ_p(E_j) ≥ c.

### The theorem

**On a compact refinement system (compact Stone space), every
PFA charge has marginals that eventually leave any fixed Hölder
ball S_s(L).**

Proof: Suppose μ_p is PFA with q^(k) ∈ S_s(L) for all k.  Then
for any atom A ∈ At(G_k): q^(k)(A) ≤ L/N_k.  For any E ∈ G_k
consisting of m atoms: q^(k)(E) ≤ L·m/N_k = L·λ(E).  So μ_p is
absolutely continuous with respect to λ (the uniform measure) on
every G_k, with Radon-Nikodym derivative bounded by L.

Now: μ_p is PFA ⟹ ∃ E_j ↓ ∅ with μ_p(E_j) ≥ c > 0.  But
E_j ↓ ∅ in Clop(2^N) ⟹ λ(E_j) → 0 (compactness + σ-additivity
of λ).  And μ_p(E_j) ≤ L·λ(E_j) → 0.  Contradiction.  □

### Consequence for ε̂(n)

Since the PFA marginals q^(k) eventually leave S_s(L), there
exists k₀ = k₀(μ_p, L) such that for k > k₀:

  q^(k) ∉ S_s(L)

i.e., q^(k) has some atom with density > L (concentration beyond
what smoothness allows).  At these resolutions, the contamination
IS distinguishable from a smooth component.

As n → ∞ and k*(n) → ∞, eventually k*(n) > k₀, and the
estimator can detect the contamination.  Therefore ε̂(n) → ε₀.

The RATE at which k*(n) crosses k₀ determines the detection rate.
Since k*(n) ~ log(n)/(2s+D):

  Detection occurs when log(n)/(2s+D) > k₀,
  i.e., n > exp((2s+D)·k₀).

After detection: ε̂(n) ≥ ε₀ − O(n^{−s/(2s+D)}).

## Status: ALIVE — concentration bound closed

The direction survives.  The proof is:

1. PFA charges cannot be uniformly smooth (compact + E_j ↓ ∅ +
   bounded density ⟹ contradiction via λ(E_j) → 0).
2. Therefore PFA marginals eventually exhibit super-smooth
   concentration.
3. The ε̂(n) trajectory detects this once k*(n) is large enough.
4. The rate test T_n = ε̂(n)·n^{s/(2s+D)} is consistent.

### Open questions (genuine)

1. **Rate of departure:** How fast does q^(k) leave S_s(L)?
   The proof gives existence of k₀ but no rate.  The rate depends
   on the specific PFA charge.  Can we get a UNIFORM rate (over
   all PFA charges with ‖μ_p‖ ≥ ε₀)?

2. **Novelty check:** Is this "consistent estimation of
   contamination fraction in Huber's model" (known: Beran,
   Donoho-Liu, Diakonikolas-Kane-Stewart)?  Or does the
   YH-specific mechanism (smoothness separation forced by PFA
   structure) add new content?

3. **The k₀ dependence:** The detection threshold exp((2s+D)·k₀)
   depends on the specific PFA charge (through k₀).  A minimax
   result would need: sup over PFA charges with ‖μ_p‖ ≥ ε₀, inf
   over estimators, what is the detection rate?

4. **Beyond Cantor:** The proof uses compactness of the Stone
   space.  All Boolean algebras have compact Stone spaces, so
   this is not a restriction.  But: the Hölder condition depends
   on the metric, which depends on the valuation Λ.  Need to
   verify the argument generalizes to general valued refinements.
