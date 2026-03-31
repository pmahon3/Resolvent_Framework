import type { ProofStep } from '../../core/src/index'

function renderStep(step: ProofStep, indent: number): string {
  const pad = '  '.repeat(indent)
  const hypStr = step.hyps.length === 0
    ? ''
    : `[${step.hyps.map(h => `${h.name} : ${h.type}`).join(', ')}] `
  const line = `${pad}${step.tactic}: ${hypStr}⊢ ${step.goal}`
  const children = step.children.map(c => renderStep(c, indent + 1)).join('\n')
  return children ? `${line}\n${children}` : line
}

export interface PlainTextOptions {
  depth?: number
}

/** Render ProofStep[] as an indented plain-text proof outline. */
export function toPlainText(steps: ProofStep[], _opts: PlainTextOptions = {}): string {
  return steps.map(s => renderStep(s, 0)).join('\n')
}
