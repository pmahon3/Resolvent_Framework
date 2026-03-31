import type { ProofStep } from '../../core/src/index'

function unicodeToLatex(s: string): string {
  return s
    .replace(/∀/g, '\\forall ').replace(/∃/g, '\\exists ')
    .replace(/→/g, '\\to ').replace(/↔/g, '\\leftrightarrow ')
    .replace(/∧/g, '\\land ').replace(/∨/g, '\\lor ').replace(/¬/g, '\\lnot ')
    .replace(/⊢/g, '\\vdash ').replace(/≤/g, '\\leq ').replace(/≥/g, '\\geq ')
    .replace(/≠/g, '\\neq ').replace(/∈/g, '\\in ').replace(/∉/g, '\\notin ')
    .replace(/⊆/g, '\\subseteq ').replace(/∩/g, '\\cap ').replace(/∪/g, '\\cup ')
    .replace(/∅/g, '\\emptyset ').replace(/σ/g, '\\sigma ').replace(/μ/g, '\\mu ')
    .replace(/ℕ/g, '\\mathbb{N}').replace(/ℚ/g, '\\mathbb{Q}')
    .replace(/ℝ/g, '\\mathbb{R}').replace(/ℂ/g, '\\mathbb{C}')
    .replace(/⟨/g, '\\langle ').replace(/⟩/g, '\\rangle ')
}

function escapeLatex(s: string): string {
  return s.replace(/_/g, '\\_').replace(/%/g, '\\%').replace(/&/g, '\\&')
}

function sequent(step: ProofStep): string {
  const goalStr = unicodeToLatex(step.goal)
  if (step.hyps.length === 0) return goalStr
  const hypStr = step.hyps.map(h => `${unicodeToLatex(h.name)} : ${unicodeToLatex(h.type)}`).join(',\\, ')
  return `${hypStr} \\vdash ${goalStr}`
}

function renderStep(step: ProofStep, depth: number): string {
  const conc = `$${sequent(step)}$`
  const lbl = `\\texttt{${escapeLatex(step.tactic)}}`

  if (depth === 0 || step.children.length === 0) {
    return `\\hypo{${conc}}\n`
  }

  const premises = step.children.map(c => renderStep(c, depth - 1)).join('')
  const n = step.children.length
  return premises + `\\infer${n}[${lbl}]{${conc}}\n`
}

export interface EbproofOptions {
  depth?: number
}

/** Render ProofStep[] as an ebproof LaTeX proof tree. */
export function toEbproof(steps: ProofStep[], opts: EbproofOptions = {}): string {
  const depth = opts.depth ?? 30
  const inner = steps.map(s => renderStep(s, depth)).join('')
  return `\\begin{prooftree}\n${inner}\\end{prooftree}`
}

/** Render as a complete standalone LaTeX document. */
export function toEbproofDocument(
  steps: ProofStep[],
  thmName: string,
  opts: EbproofOptions = {}
): string {
  const tree = toEbproof(steps, opts)
  return [
    '\\documentclass{article}',
    '\\usepackage{amsmath,amssymb}',
    '\\usepackage{ebproof}',
    '\\begin{document}',
    '',
    `\\noindent\\textbf{Theorem:} \\texttt{${escapeLatex(thmName)}}`,
    '',
    '\\bigskip',
    '',
    tree,
    '',
    '\\end{document}',
  ].join('\n')
}
