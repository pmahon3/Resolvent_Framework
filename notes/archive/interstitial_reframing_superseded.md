# Interstitial Reframing

## The through-line

At each stage, what appears to be a construction is revealed to be already contained
in what came before. The observer does not construct probability, dynamics, or
reconstruction — each is disclosed by the coherence of their prior commitments and
the structure of the world they are embedded in.

The unifying register: each transition names the *residual openness* remaining after
the previous paper, then shows the next paper closes it — not by adding new assumptions
but by drawing out what was already implicit.

The word "forced" was considered and set aside. The mathematics does not coerce the
observer; it *reveals* what coherent observation already contains. The register is
disclosure, not compulsion.

---

## Four-paper structure (as of 2026-04-06)

The program has consolidated from six papers to four. See `program_overview.md`
for the full structure. The transitions are:

### I → II: From probability to dynamics

**Residual openness after Paper I:** The observer has a probability measure $P$ on
$(\Omega, \sigma(\mathcal{C}))$. But the relationship between their measurements at
different times is unconstrained. It is unclear whether the observer's predictions
cohere temporally — whether there is a consistent dynamical structure at all.

**What Paper II discloses:** The Koopman operator and the semigroup law are not
additional structure imposed on the system. They are read off from the spectral
structure of $(Q, P)$. The minimal predictive query $Q_*$ is determined, not chosen.
Temporal coherence of prediction is a consequence of the same observable compatibility
that determined $P$.

Philosophical register: the observer's future-orientation is constitutive of what it
means to measure; Paper II shows that orientation has a determinate form given $P$.

### II → III: From dynamics to reconstruction

**Residual openness after Paper II:** The semigroup is characterised abstractly. The
form of the observation and the structure of the dynamics are unspecified. It is
unclear whether the abstract operator $K_t$ is accessible to a real observer with
only local, temporally bounded sensor access — or whether the state space can be
recovered from measurements alone.

**What Paper III discloses:** Under a spectral condition on the observation function
(cyclicity for the Koopman operator), the time-delayed measurements of $h$ generate
the full observable $\sigma$-algebra. The state space is recovered — not constructed
— from the structure already present in the observations. The Stone space of the
observable algebra, introduced in Paper I as a technical tool, reappears here as the
object being reconstructed.

Philosophical register: the observer embedded in time, with only local sensor access,
finds that enough history discloses the state. The minimal sufficient window is
determined by the measure and the dynamics jointly, not chosen.

### III → IV: From reconstruction to finite-sample detection

**Residual openness after Paper III:** The reconstruction equivalence is established
at the population level. But a real observer has only finite data. It is unclear
whether reconstruction is detectable from a finite sample, at what rate, and
with what certificate.

**What Paper IV discloses:** The σ-algebra approximation error δ(L) is estimable
from data without oracle knowledge of the mixing rate, dimension, or smoothness.
The elbow stopping rule L̂* achieves the minimax-optimal rate without these inputs
because it operates upstream of the rate: asking whether the algebra has captured
ℬ, not at what rate it is converging. The conditional variance identity identifies
the precise mediating object connecting the algebraic witness δ̂ and the
information-theoretic witness Ĥ₂ — both measure the same failure of separation
across delay fibres.

Philosophical register: the observer's finite-sample limitation is not an obstacle
but a clarifying constraint. It discloses that reconstruction is not a qualitative
threshold but a quantitative transition detectable from within the data.

---

## Notes on register

- The philosophical content should be available to a reader who looks for it, without
  being foregrounded as philosophy.
- The language of *disclosure* and *determination* is already present in the
  mathematics — "uniquely determined by", "reads off from", "is equivalent to" —
  and can carry the register without explicit philosophical vocabulary.
- No phenomenological terminology needed; the resonance with observation-first
  philosophy is structural, not terminological.
- "Forced" and "elimination" have been replaced by "disclosed" and "contained" to
  better reflect the register: the mathematics reveals what was implicit, rather than
  imposing new constraints.

---

## Old interstitial content (I → 0 transition, six-paper structure)

The earlier version of this document developed interstitials for the transitions
−1→0, 0→1, 1→2, 2→3 under the six-paper structure. That content remains valid
at the level of individual arguments and can be drawn on when writing the
introductory and closing sections of each paper. The philosophical observations
about CE as a commitment about the infinite (−1→0), intentionality (0→1),
Koopman-Perron duality (1→2), and the minimal sufficient window (2→3) are all
still relevant — they now live within papers rather than between them.
