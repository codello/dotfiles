---
name: idiomatic-design
description: Baseline instructions for creating idiomatic code in new and existing code bases.
---

# Idiomatic Design

Design an ideal implementation for the user's request within the context of the language and framework in use. Do not derive the design from the code that is already there. Use existing code as evidence, not authority.

The code being idiomatic and easy to understand is the prime directive. Other aspects such as refactoring effort, diff size, and backwards compatibility are secondary. If the ideal design is non-trivial, explain it in a few sentences before writing code.

## What counts as idiomatic

Determine the idiom from authoritative sources, in this order of precedence:

1. The repository's own explicit contracts: formatter, linter, and editor configs, plus the language/framework versions pinned in manifests or lockfiles.
2. Official style guides and documentation for that language/framework version.
3. Dominant community convention for the ecosystem.

Never infer "the convention" from the surrounding codebase alone. A pattern repeated ten times in a repo is still non-idiomatic if the language or framework says otherwise. Repetition establishes local habit, not convention.

## Core rule

Existing code is evidence, not authority.

1. Compare the existing code against the idiomatic baseline above.
2. Where they agree, follow the existing code — consistency is free.
3. Where they conflict, the existing code is a discovered issue, not an established pattern. Do not imitate it, extend it, or route around it. Design the ideal implementation and refactor the conflicting code to match.

This overrides any default instruction to "match the style of the surrounding code" wherever the surrounding style is non-idiomatic.

## Designing

- Design new code as if the non-idiomatic parts did not exist: start from the ideal shape, then integrate.
- When a task touches code whose structure is the problem, replace the structure instead of patching around it.
- Target the language/framework version actually in use, not idioms from an older era of the codebase.

## Refactoring

- Large-scale refactorings are acceptable. If the ideal design requires moving, renaming, or rewriting code beyond the immediate task, do it.
- Where practical, keep mechanical moves separate from behavioral changes so the refactor stays reviewable.
- If a refactor grows far beyond what the task implies, state the scope in a sentence or two and proceed. The user has accepted large refactorings; do not stall asking for permission.

## Reviewing

- During code review, point out non-idiomatic code and suggest the idiomatic alternative. Do not accept non-idiomatic code without comment.
- Report sources for idioms when they are not obvious. Justify why an issue is non-idiomatic, don't just assert it. Cite the authoritative source(s).

## Discovered issues

When pre-existing code violates language/framework idioms:

- Fix it when it is within the scope of the current task.
- When it is out of scope, report it briefly (file, what is non-idiomatic, what the idiomatic form would be) instead of silently copying it.
- A discovered issue never justifies writing non-idiomatic code yourself.

## Boundaries

- Conventions that do not conflict with language/framework idioms remain binding: naming schemes, module layout, formatting and lint configs, API contracts.
- If two approaches are both genuinely idiomatic and the choice is significant, ask the user.
- Do not use this skill to override deliberate, documented design decisions; challenge those on their merits instead.
