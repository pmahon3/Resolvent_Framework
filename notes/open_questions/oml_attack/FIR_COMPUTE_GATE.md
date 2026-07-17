# Fir attended-compute gate

Updated: 2026-07-16 (America/Vancouver).

## Service and authentication

- Official status:
  `https://status.alliancecan.ca/system/Fir`.
- Classification: **OUTAGE**. The official page reports an outage and open
  filesystem and login-node incidents.
- SSH ControlMaster: inactive, checked locally with
  `python3.11 fir_poc.py connection-status`.
- No connection, transfer, remote preparation, Slurm submission, monitoring,
  retrieval or cleanup was attempted.

## POC status

The attended harness is outside this repository at `/Users/pmahon/fir-poc`.

- Local unit suite: 17/17 pass.
- `prepare --dry-run`: pass; no network or remote mutation.
- Dry-run source SHA-256:
  `e1075c8974326a449429a6f3e82c963f586124dbbf1196f98370747e6affad10`.
- Dry-run input SHA-256:
  `c2cde5257490e9eeb36da88be233e4916aa2d9aabd45b7037fc9c8e7325cfdd8`.
- Compute-node smoke, 8-task array, receipt retrieval, aggregate verification
  and deterministic retries 2/6: **not run**.

Research production use is therefore unauthorized until the outage clears,
the user approves one attended Duo connection, and every prescribed POC gate
passes through the reused ControlMaster.

## Prospective mathematical workload

No production job is specified or submitted. The local critical-context
census has now split all 16 divergent doubletons using only ten old controls.
No full-old scan is required, so the prospective parameter set

```text
32 divergent roots x 18,676 old events = 597,632 old/new contexts
```

has been cancelled as mathematically unnecessary. The exact-context result
instead proves a noncompression boundary and pivots the mathematics to
bounded cut locality/cylindrical reflection.

A 9,334-pair parameter space exists, but the four-context local pilot has
shown that it is not currently the discriminating workload: two exact old
contexts already reopen a two-upper repair interval. The following remains a
deferred dry specification, not a proposed production job:

```text
Mathematical proposition:
  For every old complement-pair not already in the 16-event control, classify
  exact closure after adjoining that cylinder pair on both copies; record
  whether the Neg-023 cut join persists, becomes cylindrical, or latticehood
  fails.
Exact finite parameter set:
  9,334 old complement-pairs (9,336 pairs in the 18,676-event old OML, minus
  the two generator pairs already present).
Why the workload is exhaustive:
  Replacing an adjoined event by its complement gives the same extension.
Shard definition:
  Canonical complement-pair rank intervals; count awaits local pilot.
Producer:
  Open; must be frozen before submission.
Independent verifier:
  Open; must independently recompute closure and cut/lattice verdicts.
Negative witness:
  Old indices, generated-family hashes, first failed cut or changed
  least-upper mask, and cylindricity sections.
What a complete positive result proves:
  Exact Level-1 classification of every single-old-context extension.
Explicit nonclaims:
  No multi-context/full-old closure, finite assembly, sigma-completion, ODBC,
  MBRC, or Phi theorem.
Estimated CPU per shard:
  Open pending local pilot.
Estimated memory per shard:
  Open pending local pilot.
Expected output size:
  Open pending receipt prototype.
Slurm array and concurrency:
  Deferred; no submission.
Source commit:
  Open; must be an immutable producer/verifier commit.
Input-manifest hash:
  Open.
```

The next computation is the small exact repair classification of the two
known intervals and remains local. There is currently no justified Fir
research submission.

The later restricted `ARR-K8A` comparison now passes after hostile repair:
one pointed five-profile isomorphism transports all three split atoms and
yields 504 word-level selectors (payload `f666a2cb...`). Complete full-old
physical refinement is not yet specified and is not a Fir production
candidate.

The full-old physical-signature gate also completes locally (payload
`1e65c4c7...`) and proves that one simultaneous subset selector exists.
The next task is structural compact-MDD adjunction and cut preservation, not
an exact shard space. It is therefore still not a Fir production workload.

## Required next gate

When the official service is no longer `OUTAGE`, recheck it once. If usable,
request user approval before `python3.11 fir_poc.py connect`, reuse the one
attended master, and complete the smoke/array/fetch/verify/retry POC before
staging any research source.
