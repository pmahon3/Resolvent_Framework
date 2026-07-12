# s37 period-two width-two production result

The exhaustive labeled census completed over all `9,408^2 = 88,510,464`
ordered pairs of individually two-cell-girth-valid width-two ports for the
seven-loop face `C={a0,a3,a11}`.

For each ordered pair, the exact rooted period-two state fixpoints were run
for target representatives `a1,a2,a4`.  The operative counts were

- `a1`: 0;
- `a2`: 0;
- `a4`: 0.

Thus reflection gives zero also for `a13,a12,a10`.  Because no pair passes
the local face-free/nonlive/order-determining screen, three-cell girth and
downstream geometry cannot restore a survivor and need not be evaluated.
The conclusion is a bounded no-go for this face at period two and width two.

The production run is recorded in `s37_p2_k2_checkpoint.json`; it completed
all 9,408 first-port chunks and 88,510,464 ordered pairs.  The C++ engine
anchors the 29 states and independently reconstructs exactly 9,408 valid
ports at startup.  An external audit matched the established Python oracle
on all period-two width-one cases and 6,000 deterministic width-two samples,
including cases separating `E1[0]` from any-position `live[0]`.
