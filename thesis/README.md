# Thesis scaffold

## Structure

`thesis.tex` — master document. Uses `\subimport` to pull in each paper.

Each paper directory needs a `*_body.tex` file containing only the paper's
body content (no `\documentclass`, no `\begin{document}`, no preamble).
The standalone paper `.tex` file should `\input` its own body file, so
the body is maintained in exactly one place.

## How to create a `_body.tex` for a paper

In each paper's `.tex` file:
1. Move everything between `\begin{document}` and `\end{document}`
   into `papername_body.tex`
2. Replace that block in the standalone file with `\input{papername_body}`
3. The thesis picks up `papername_body.tex` via `\subimport`

## Status

| Paper | Body file | Status |
|-------|-----------|--------|
| Paper −1 | `discriminability_foundations_body.tex` | TODO |
| Paper 0  | `prokhorov_extension_body.tex` | TODO |
| Paper 1  | `observational_foundations_body.tex` | TODO |
| Paper 2  | `predictive_operator_theory_body.tex` | TODO |
| Paper 3  | `predictive_experiments_body.tex` | TODO |
| Paper 4  | `observational_probability_body.tex` | TODO |

## Interstitial chapters

| File | Connects |
|------|---------|
| `interstitial_minus_one_to_zero.tex` | Paper −1 → Paper 0 |
| `interstitial_zero_to_one.tex` | Paper 0 → Paper 1 |
| `interstitial_one_to_two.tex` | Paper 1 → Paper 2 |
| `interstitial_two_to_three.tex` | Paper 2 → Paper 3 |
| `interstitial_three_to_four.tex` | Paper 3 → Paper 4 |

## Compilation

From `thesis/`:
```
pdflatex thesis.tex
```

Note: will not compile until all `_body.tex` files exist.
