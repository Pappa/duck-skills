---
name: dev-duck
description: Implement backlog tickets or user-provided requirements using test-duck and review-duck.
disable-model-invocation: true
---

# Dev duck

Implement one or more features specified in a backlog ticket or requirements the user provides.

## Spec and session baseline

If the user gives a ticket reference (by name or number), fetch it from the backlog per `docs/agents/backlog.md` and confirm the title before starting work. If the reference is ambiguous, ask. Treat that ticket file as the **spec** for **review-duck** unless the user points elsewhere.

At session start, record the review baseline: `git rev-parse HEAD` (the commit before implementation changes). Pass this SHA to **review-duck** as the fixed point when reviewing this work.

## Implementation pipeline

1. Read and follow `.cursor/skills/test-duck/SKILL.md` for the full red → green loop. Agree **test boundaries** with the user when not already clear (see test-duck). Do not bulk-write tests; one vertical slice at a time.

2. Run type checking, linting, and tests as test-duck and this repo's tooling expect — regularly during work and again before review.

3. Read and follow `.cursor/skills/review-duck/SKILL.md`. Use the session baseline SHA as the fixed point. Pass the backlog ticket path (or user spec path) as the spec source.

4. Address review findings (including structural improvements deferred from the TDD loop). Re-run type checking, linting, and tests.

When module shape or test boundaries are unclear during test-duck, read and follow `.cursor/skills/architect-duck/SKILL.md`.
