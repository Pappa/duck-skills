---
name: test-duck
description: Test-driven development (red → green). Invoked by dev-duck or when the user explicitly requests TDD — not a standalone implementation entry point.
disable-model-invocation: true
---

# Test-Driven Development

TDD is the red → green loop. This skill is the reference that makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Every section applies on every cycle: consult them before and during the loop, not after.

When exploring the codebase, read `GLOSSARY.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

Review a sample of existing unit tests from this codebase and follow the style and conventions used already.

## What a good test is

Tests verify behaviour through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Boundaries: where tests go

A **test boundary** is the public interface to test: the layer where external behaviour can be tested without knowledge of or reliance on the internal implementation. Tests verify this external behaviour at boundaries, never against internal implementation details.

**Test at pre-determined boundaries.** Before writing tests, confirm the boundaries under test with the user if they are not clearly specified.

It is not possible or valuable to test every edge-case. Focus on the critical paths, complex logic, conditional branching points and error conditions.

Ask: "What's the public interface of this unit, and which boundaries should be tested?" Give each proposed boundary a one-line note on what it catches and what it misses.

When the shape of that interface is itself in question (how deep the module is, where the boundary belongs, what the interface should expose), call the Skill tool `architect-duck`.

## Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database instead of using the interface). The tell: the test breaks when you refactor but behaviour hasn't changed.
- **Tautological**: the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec.
- **Horizontal slicing**: writing all tests first, then all implementation. Bulk tests verify _imagined_ behaviour: you test the _shape_ of things rather than user-facing behaviour, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in small **vertical slices** instead: one test → one implementation → repeat.

## Rules of the loop

- **Red before green.** First write a failing test, then just enough code to make the test pass. Don't anticipate future tests, or add unnecessary features.
- **One slice at a time.** One test boundary, one test, one functional change per cycle.
- **Refactoring is not part of the loop.** Structural cleanup belongs after review findings are addressed in **dev-duck** (step 4), not in the red → green cycle.
