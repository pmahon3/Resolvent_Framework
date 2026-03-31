#!/usr/bin/env node
/**
 * prooftree CLI
 *
 * Usage:
 *   prooftree render --format bussproofs [--input proof.json] [--doc]
 *   prooftree render --format ebproof    [--input proof.json] [--doc] [--thm NAME]
 *   prooftree render --format plaintext  [--input proof.json]
 *   prooftree mock   --name imp_self     [--format bussproofs]
 *
 * With no --input, reads ProofStep[] JSON from stdin.
 * With --doc, wraps output in a standalone LaTeX document.
 */

import { readFileSync } from 'fs'
import { parse } from '../../core/src/index'
import { fromStdin } from '../../adapters/file/src/index'
import { getMock } from '../../adapters/mock/src/index'
import {
  toBussproofs, toBussproofDocument,
  toEbproof, toEbproofDocument,
  toPlainText,
} from '../../renderers/src/index'
import type { ProofStep } from '../../core/src/index'

function usage(): never {
  console.error(`
prooftree — ProofStep renderer

Commands:
  render  --format <fmt> [--input <file>] [--doc] [--thm <name>] [--depth <n>]
  mock    [--name <mock>] [--format <fmt>] [--doc]

Formats: bussproofs | ebproof | plaintext

With no --input, reads JSON from stdin.
With --doc, wraps LaTeX in a standalone document.
  `.trim())
  process.exit(1)
}

function parseArgs(argv: string[]): Record<string, string | boolean> {
  const args: Record<string, string | boolean> = {}
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i]
    if (a.startsWith('--')) {
      const key = a.slice(2)
      const next = argv[i + 1]
      if (next && !next.startsWith('--')) {
        args[key] = next
        i++
      } else {
        args[key] = true
      }
    } else {
      args['command'] = a
    }
  }
  return args
}

function render(steps: ProofStep[], args: Record<string, string | boolean>): string {
  const fmt = (args['format'] as string) ?? 'plaintext'
  const doc = args['doc'] === true
  const thm = (args['thm'] as string) ?? 'theorem'
  const depth = args['depth'] ? parseInt(args['depth'] as string) : undefined

  switch (fmt) {
    case 'bussproofs':
      return doc ? toBussproofDocument(steps, thm, { depth }) : toBussproofs(steps, { depth })
    case 'ebproof':
      return doc ? toEbproofDocument(steps, thm, { depth }) : toEbproof(steps, { depth })
    case 'plaintext':
      return toPlainText(steps)
    default:
      console.error(`Unknown format: ${fmt}. Use bussproofs | ebproof | plaintext`)
      process.exit(1)
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  const command = (args['command'] as string) ?? 'render'

  let steps: ProofStep[]

  if (command === 'mock') {
    steps = getMock(args['name'] as string | undefined)
  } else if (command === 'render') {
    if (args['input']) {
      const raw = readFileSync(args['input'] as string, 'utf8')
      steps = parse(raw)
    } else {
      steps = await fromStdin()
    }
  } else {
    usage()
  }

  console.log(render(steps, args))
}

main().catch(err => { console.error(err); process.exit(1) })
