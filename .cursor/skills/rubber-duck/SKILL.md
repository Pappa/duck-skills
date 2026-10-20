---
name: rubber-duck
description: Relentless interview to sharpen a plan or design while updating glossary entries and ADRs as terms and decisions crystallise. Use for rubber-duck sessions, collaborative design, or when the user invokes rubber-duck.
disable-model-invocation: true
---

# Rubber duck

Sharpen a plan or design in conversation **and** persist the domain model as you go.

In one session, apply both:

1. **question-duck** — round-based decision tree until shared understanding.
2. **architect-duck** — challenge vocabulary, stress-test scenarios, update `GLOSSARY.md` and `docs/adr/` when terms and decisions land.

Read `docs/agents/domain.md` for glossary layout. If missing, tell the user to run `/setup-duck-skills`.

Do not implement product code in this skill; stop at shared understanding plus updated domain docs unless the user explicitly asks to continue.
