import type { ProofStep } from '../../../core/src/index'

/** A mock proof of `p → p` via intro + exact. */
export const MOCK_IMP_SELF: ProofStep[] = [
  {
    id: '0',
    tactic: 'intro',
    hyps: [],
    goal: 'p → p',
    subgoals: ['p ⊢ p'],
    children: [
      {
        id: '1',
        tactic: 'exact',
        hyps: [{ name: 'h', type: 'p' }],
        goal: 'p',
        subgoals: [],
        children: [],
      },
    ],
  },
]

/** A mock proof of `p ∧ q` via constructor. */
export const MOCK_AND_INTRO: ProofStep[] = [
  {
    id: '0',
    tactic: 'constructor',
    hyps: [{ name: 'hp', type: 'p' }, { name: 'hq', type: 'q' }],
    goal: 'p ∧ q',
    subgoals: ['p', 'q'],
    children: [
      {
        id: '1',
        tactic: 'exact',
        hyps: [{ name: 'hp', type: 'p' }, { name: 'hq', type: 'q' }],
        goal: 'p',
        subgoals: [],
        children: [],
      },
      {
        id: '2',
        tactic: 'exact',
        hyps: [{ name: 'hp', type: 'p' }, { name: 'hq', type: 'q' }],
        goal: 'q',
        subgoals: [],
        children: [],
      },
    ],
  },
]

/** Returns a named mock proof, or MOCK_IMP_SELF as default. */
export function getMock(name?: string): ProofStep[] {
  if (name === 'and_intro') return MOCK_AND_INTRO
  return MOCK_IMP_SELF
}
