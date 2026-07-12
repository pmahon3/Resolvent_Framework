# s38 period-three width-one census

`s38_p3_k1_census.cpp` exhausts all `196^3 = 7,529,536` ordered triples
of labeled width-one interfaces for the seven-loop face.  It evaluates the
exact rooted three-phase fixed points for target representatives `a1,a2,a4`.

The checkpoint reports the established phasewise operative count and, inside
that count, `root_order`: cases where the actual boundary-cell suffix mask
`E1[0]` order-separates the finite cell.  Only `root_order` cases are retained
as survivors.  This implements the root-cell gate required by session 36.

Build and run:

```sh
c++ -O3 -std=c++17 s38_p3_k1_census.cpp -o /tmp/s38_p3_k1
/tmp/s38_p3_k1 --checkpoint s38_p3_k1_checkpoint.json
```
