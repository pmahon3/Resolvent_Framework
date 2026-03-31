import { readFileSync } from 'fs'
import { parse } from '../../../core/src/index'
import type { ProofStep } from '../../../core/src/index'

/** Read and validate a ProofStep[] JSON file from disk. */
export function fromFile(path: string): ProofStep[] {
  const raw = readFileSync(path, 'utf8')
  return parse(raw)
}

/** Read from stdin (for pipe usage). */
export async function fromStdin(): Promise<ProofStep[]> {
  const chunks: Buffer[] = []
  for await (const chunk of process.stdin) chunks.push(chunk)
  return parse(Buffer.concat(chunks).toString('utf8'))
}
