# Independent s37 downstream oracle

`audit_s37_downstream_oracle.py` is a self-contained verifier for period-p
seven-loop relay rows.  It does not import the production relay core.  It
reconstructs the 29 states and explicitly computes:

- phase-labelled compatibility graphs;
- zero and exactly-one infinite suffixes by graph pruning/flooding;
- rooted state restrictions at each fixed position;
- compatible fixed-position state pairs;
- any-position phase live/free unions, plus the mandatory fixed-root order
  restriction;
- finite quotient Berge girth and master-target block distances; and
- local/cross-cell false orders using the actual quotient atom classes and
  orthogonality relation.

The CLI accepts a list, or an object containing `rows` or `survivors`, with
rows of the form `{p0:[[old,new],...], p1:[...], target:int}`.

## Validation anchors

`audit_s37_downstream_selftest.py` passes on:

1. both s36 period-one width-four candidates, reproducing their banked
   adjacent cross-cell failure, including the missing witness for
   `a1(cell 0) not<=a1(cell 1)^perp`;
2. the stronger fixed-root local-order failure of those candidates; and
3. three period-two width-one maps from the exhaustive zero class, each
   independently failing an operative local condition.

The period-one anchors are intentionally kept period one.  Repeating a map
as two phases is not a valid phasewise invariant under rooted any-position
semantics.

## Period-two width-two application

The completed production checkpoint contains 88,510,464 screened ordered
pairs and **zero operative survivors** for target representatives `a1,a2,a4`.
Consequently there are no rows on which downstream girth, master geometry,
or cross-cell separation can run.  The CLI accepts that checkpoint and
returns an empty audited row list.  This is a vacuous downstream conclusion,
not an independent reproduction of the exhaustive local zero count; the
separate `audit_s37_p2_optimizer.py` supplies the independent fixed-point
and screen validation.

Validation commands:

```sh
python3 audit_s37_downstream_selftest.py
python3 audit_s37_downstream_cli.py \
  census_2026-07-12_s37/s37_p2_k2_checkpoint.json -o /tmp/s37-audit.json
```
