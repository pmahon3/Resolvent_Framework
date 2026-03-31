/**
 * @prooftree/core
 *
 * The ProofStep type and pure utilities.
 * No Lean API, no rendering logic, no side effects.
 * This is the only contract shared between source adapters and renderers.
 */

import Ajv from 'ajv'
import schema from '../../schema/ProofStep.json'

// ─── Types ───────────────────────────────────────────────────────────────────

export interface Hypothesis {
  name: string
  type: string
}

export interface Position {
  line: number
  col: number
}

/**
 * A single tactic step in a proof.
 *
 * - `hyps` and `goal` describe the state *before* the tactic runs.
 * - `subgoals` lists the goals *after* the tactic runs (empty = QED at this branch).
 * - `children[i]` is the sub-proof tree that discharges `subgoals[i]`.
 */
export interface ProofStep {
  id: string
  tactic: string
  hyps: Hypothesis[]
  goal: string
  subgoals: string[]
  children: ProofStep[]
  pos?: Position
}

// ─── Validation ──────────────────────────────────────────────────────────────

const ajv = new Ajv({ allErrors: true })
const validateStep = ajv.compile(schema)

/** Validate raw JSON data against the ProofStep schema. Throws on failure. */
export function validate(data: unknown): ProofStep[] {
  if (!Array.isArray(data)) {
    throw new Error('ProofStep data must be a JSON array')
  }
  for (const item of data) {
    if (!validateStep(item)) {
      throw new Error(
        'Invalid ProofStep: ' + ajv.errorsText(validateStep.errors)
      )
    }
  }
  return data as ProofStep[]
}

/** Parse and validate a JSON string. */
export function parse(json: string): ProofStep[] {
  return validate(JSON.parse(json))
}

// ─── Tree utilities ───────────────────────────────────────────────────────────

/** Flatten a proof tree into a pre-order list of all steps. */
export function flatten(steps: ProofStep[]): ProofStep[] {
  const result: ProofStep[] = []
  function visit(step: ProofStep) {
    result.push(step)
    for (const child of step.children) visit(child)
  }
  for (const step of steps) visit(step)
  return result
}

/** Return all steps at exactly the given depth (root = depth 0). */
export function atDepth(steps: ProofStep[], depth: number): ProofStep[] {
  if (depth === 0) return steps
  return steps.flatMap(s => atDepth(s.children, depth - 1))
}

/** Find a step by id anywhere in the tree. Returns null if not found. */
export function findById(steps: ProofStep[], id: string): ProofStep | null {
  for (const step of flatten(steps)) {
    if (step.id === id) return step
  }
  return null
}

/** Return the maximum depth of the proof tree. */
export function maxDepth(steps: ProofStep[]): number {
  if (steps.length === 0) return 0
  return 1 + Math.max(...steps.map(s => maxDepth(s.children)))
}

/** Return steps with children truncated at the given depth. */
export function truncate(steps: ProofStep[], depth: number): ProofStep[] {
  if (depth === 0) return steps.map(s => ({ ...s, children: [] }))
  return steps.map(s => ({ ...s, children: truncate(s.children, depth - 1) }))
}

/** Count total number of steps in the tree. */
export function count(steps: ProofStep[]): number {
  return flatten(steps).length
}
