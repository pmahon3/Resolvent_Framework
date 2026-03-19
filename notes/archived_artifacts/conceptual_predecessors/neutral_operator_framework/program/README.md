# Parallel documents bundle

Structure:
- `references.bib` (root)
- `elements/elements.tex` (technical development; BibTeX-based)
- `prose/prose.tex` (prose companion; imports labels from `elements` via `xr-hyper`; BibLaTeX/Biber-based)

## Build order

### Option A: explicit commands

1) Build the technical document first (creates `elements.aux` for external refs):

```bash
cd elements
pdflatex elements.tex
bibtex elements
pdflatex elements.tex
pdflatex elements.tex
```

2) Then build the prose companion (now external refs resolve):

```bash
cd ../prose
pdflatex prose.tex
biber prose
pdflatex prose.tex
pdflatex prose.tex
```

### Option B: latexmk (recommended)

If you use `latexmk`, run it in this order:

```bash
cd elements && latexmk -pdf elements.tex
cd ../prose && latexmk -pdf prose.tex
```

## Cross-references

`prose/prose.tex` imports labels from `elements/elements.tex` using:

```tex
\usepackage{xr-hyper}
\externaldocument[E-]{../elements/elements}
\providecommand{\Eref}[1]{\ref{E-#1}}
```

So `\Eref{<label>}` in prose points to the numbered object in the technical companion.
