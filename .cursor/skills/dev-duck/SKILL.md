---
name: dev-duck
description: Implement backlog tickets or user-provided requirements using test-duck and review-duck.
disable-model-invocation: true
---

# Dev duck

Implement one or more features specified in a backlog ticket or requirements the user provides.

## Spec and session baseline

If the user gives a ticket reference (by name or number), fetch it from the backlog per `docs/agents/backlog.md` and confirm the title before starting work. If the reference is ambiguous, ask. If the user provides no information about which ticket to work on or provides a reference to a feature plan, list the `ready` tasks and spikes, and recommend the order they should be worked on.

Treat that ticket file as the **spec** for **review-duck** unless the user points elsewhere.

At session start, record the review baseline: `git rev-parse HEAD` (the commit before implementation changes). Pass this SHA to **review-duck** as the fixed point when reviewing this work.

## Software design

When module shape or test boundaries are unclear call the Skill tool `architect-duck`.

## Implementation pipeline

1. Agree **test boundaries** with the user if they are not already clear.

2. If the implementation requires changes to source code, call the Skill tool `test-duck` to delegate unit testing to it.

3. Run type checking, linting, and tests as this repo's tooling expect — regularly during work and again before review.

4. Once the implementation of code and unit tests are complere, call the Skill tool `review-duck`. Use the session baseline SHA as the fixed point. Pass the backlog ticket path (or user spec path) as the spec source.

5. Address review findings (including structural improvements deferred from the TDD loop). Re-run type checking, linting, and tests.
