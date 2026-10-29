---
name: rubber-duck
description: Single-session design and delivery prep — shared understanding, domain docs, and implementation backlog items. Use for rubber-duck sessions or when the user invokes rubber-duck.
disable-model-invocation: true
---

# Rubber duck

Reach a **concrete outcome** in one user-invoked session. Typical outcomes:

1. **Clarity** — shared understanding with the user (no file publish required).
2. **Domain or product docs** — updates to `GLOSSARY.md`, `docs/adr/`, or other repo docs.
3. **Code changes** — when the user explicitly continues into implementation in the same session.
4. **Implementation backlog items** — **`Type: task`** or **`Type: spike`** for development work (see below).

## Skills used in every session

Apply both:

1. **question-duck** — round-based Q&A until assumptions are documented and decisions are sharp.
2. **architect-duck** — system design vocabulary, stress-test scenarios, update `GLOSSARY.md` and `docs/adr/` when terms and decisions land. **architect-duck** never invokes **rubber-duck**.

Read `docs/agents/domain.md` for glossary layout. If missing, tell the user to run `/setup-duck-skills`.

## What rubber-duck does **not** publish

- **No** `epic-duck:plan`, **`epic-duck:decision`**, or other **planning-era** `Type: epic-duck:*` items — use **epic-duck** for feature plans and planning children.
- **No** `epic-duck:task` or `epic-duck:spike` — those are for **planning** work under a feature plan.

## Implementation backlog items

When the session produces follow-on **implementation** work, publish under `.backlog/items/` per `docs/agents/backlog.md`:

| `Type:` | Filename pattern |
|---------|------------------|
| `task` | `<NNNN>-task-<slug>.md` |
| `spike` | `<NNNN>-spike-<slug>.md` |

Use the **shared `NNNN` counter** with all other backlog items.

- **`Plan:`** — link to an **existing** feature plan file when the user has confirmed the feature. If there is **no** feature yet, use **`Plan: (unanchored)`**, set **`Status: needs-triage`**, allocate the correct **NNNN**, and tell the user explicitly: the ticket is **not associated with a feature** and **will need to be triaged later** via **epic-duck**.
- Run **amigo-duck** before publish; use the review path for **`Type: task`** or **`Type: spike`** (not `epic-duck:*`).

**spike** items link findings under `.backlog/spike/`; prefer an existing spike item when **epic-duck** or a prior step already set **`Result:`**.

## Publish checklist

1. Draft item body per `docs/agents/backlog.md`.
2. **amigo-duck** → **Approve** (or user accepts documented gaps).
3. Write file(s); update the parent feature’s **Tasks** / **Spikes** table when **`Plan:`** points at a real plan.

Do not implement large product changes unless the user asks; stopping at understanding plus domain docs or backlog items is normal.
