# Thesis

`thesis.tex` — master document assembling all six papers.

**Title:** *Discriminative Foundations for Probability and Dynamics*

## Structure

Each paper has a `*_body.tex` file containing only its body content
(no `\documentclass`, no preamble). The standalone paper `.tex` files
`\input` their body files; the thesis picks them up via `\subimport`.

Bibliography and acknowledgements in body files are guarded by
`\ifcsname thesismode\endcsname\else ... \fi` so they appear in
standalone compilation but are suppressed in the thesis (which
has a single combined bibliography and acknowledgements page).

## Body file status

| Paper | Body file | Status |
|-------|-----------|--------|
| Paper −1 | `discriminability_foundations_body.tex` | done |
| Paper 0  | `prokhorov_extension_body.tex` | done |
| Paper 1  | `observational_foundations_body.tex` | done |
| Paper 2  | `predictive_operator_theory_body.tex` | done |
| Paper 3  | `predictive_experiments_body.tex` | done |
| Paper 4  | `observational_probability_body.tex` | done |

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
bibtex thesis
pdflatex thesis.tex
pdflatex thesis.tex
```

## Shared files

- `notation.tex` — shared macro definitions
- `references.bib` — combined bibliography (deduplicated from all six paper bib files)
- `../papers/acknowledgements.tex` — shared acknowledgements text

## Notes

- `thesis.tex` defines `\def\thesismode{}` which suppresses per-chapter
  bibliography and acknowledgements calls in the body files.
- `thesis.tex` defines the `aside` environment (mdframed-based) for
  provisional philosophical scaffolding present in Paper −1.
- When a paper's `references.bib` is updated, regenerate `thesis/references.bib`
  by deduplicating across all six paper bib files.
