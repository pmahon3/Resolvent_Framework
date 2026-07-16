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
bounded cut locality/cylindrical reflection. There is currently no justified
Fir research workload. A future job must wait for an exact finite parameter
space arising from that theorem, then receive a full pre-submission
specification and local resource pilot.

## Required next gate

When the official service is no longer `OUTAGE`, recheck it once. If usable,
request user approval before `python3.11 fir_poc.py connect`, reuse the one
attended master, and complete the smoke/array/fetch/verify/retry POC before
staging any research source.
