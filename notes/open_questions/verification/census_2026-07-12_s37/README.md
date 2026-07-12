# s37 period-two width-two production census

`s37_p2_k2_census.cpp` is a resumable, exact labeled-pair census for the
9,408 individually valid width-two ports on the seven-loop cell.  It uses
29-bit successor relations and evaluates the rooted period-two fixpoints for
targets `a1,a2,a4`; reflection supplies `a13,a12,a10` only after audit.

The checkpoint range is half-open in first-port indices.  Independent ranges
can therefore run concurrently and their ordered counts can be added; after
an interruption, restart at `completed_first_ports` into a new range file. The
state screen precedes exact quotient girth because girth barely filters this
class; this is an execution-order optimization and does not weaken the final
survivor pipeline.

Build and smoke-test:

```sh
c++ -O3 -std=c++17 s37_p2_k2_census.cpp -o /tmp/s37_p2_k2
/tmp/s37_p2_k2 --start 0 --end 1 --checkpoint /tmp/s37-smoke.json
```
