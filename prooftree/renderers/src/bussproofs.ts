import type { ProofStep } from '../../core/src/index'

// ─── Unicode → LaTeX ─────────────────────────────────────────────────────────

function unicodeToLatex(s: string): string {
  return s
    .replace(/∀/g, '\\forall ')
    .replace(/∃/g, '\\exists ')
    .replace(/→/g, '\\to ')
    .replace(/↔/g, '\\leftrightarrow ')
    .replace(/∧/g, '\\land ')
    .replace(/∨/g, '\\lor ')
    .replace(/¬/g, '\\lnot ')
    .replace(/⊢/g, '\\vdash ')
    .replace(/≤/g, '\\leq ')
    .replace(/≥/g, '\\geq ')
    .replace(/≠/g, '\\neq ')
    .replace(/∈/g, '\\in ')
    .replace(/∉/g, '\\notin ')
    .replace(/⊆/g, '\\subseteq ')
    .replace(/∩/g, '\\cap ')
    .replace(/∪/g, '\\cup ')
    .replace(/∅/g, '\\emptyset ')
    .replace(/σ/g, '\\sigma ')
    .replace(/μ/g, '\\mu ')
    .replace(/ν/g, '\\nu ')
    .replace(/ω/g, '\\omega ')
    .replace(/Ω/g, '\\Omega ')
    .replace(/ℕ/g, '\\mathbb{N}')
    .replace(/ℤ/g, '\\mathbb{Z}')
    .replace(/ℚ/g, '\\mathbb{Q}')
    .replace(/ℝ/g, '\\mathbb{R}')
    .replace(/ℂ/g, '\\mathbb{C}')
    .replace(/↦/g, '\\mapsto ')
    .replace(/λ/g, '\\lambda ')
    .replace(/⟨/g, '\\langle ')
    .replace(/⟩/g, '\\rangle ')
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

// ─── Renderer ────────────────────────────────────────────────────────────────

function renderStep(step: ProofStep, depth: number): string {
  const conc = `$${sequent(step)}$`
  const lbl = `\\texttt{${escapeLatex(step.tactic)}}`

  if (depth === 0 || step.children.length === 0) {
    return `\\AxiomC{${conc}}\n`
  }

  const premises = step.children.map(c => renderStep(c, depth - 1)).join('')
  const n = step.children.length

  const inferCmd =
    n === 1 ? `\\UnaryInfC{${conc}}\n` :
    n === 2 ? `\\BinaryInfC{${conc}}\n` :
    n === 3 ? `\\TrinaryInfC{${conc}}\n` :
              `\\UnaryInfC{${conc}} %% (${n} premises, collapsed)\n`

  return premises + `\\RightLabel{${lbl}}\n` + inferCmd
}

export interface BussOptions {
  depth?: number
}

/** Render ProofStep[] as a bussproofs LaTeX proof tree. */
export function toBussproofs(steps: ProofStep[], opts: BussOptions = {}): string {
  const depth = opts.depth ?? 30
  const inner = steps.map(s => renderStep(s, depth)).join('')
  return `\\begin{prooftree}\n${inner}\\end{prooftree}`
}

/** Render as a complete standalone LaTeX document. */
export function toBussproofDocument(
  steps: ProofStep[],
  thmName: string,
  opts: BussOptions = {}
): string {
  const tree = toBussproofs(steps, opts)
  return [
    '\\documentclass{article}',
    '\\usepackage{amsmath,amssymb}',
    '\\usepackage{bussproofs}',
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
