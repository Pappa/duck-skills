Type: epic-duck:task
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Document epic-duck flows for ambiguous tickets and remove triage-duck skill promises from canon.
Blocked by:

## Problem Statement

Decision **[0006](0006-decision-triage-activation.md)** cancels a separate **triage-duck** skill but skills and backlog docs still tell agents to expect “triage later” via a future skill. Without explicit **epic-duck** guidance, maintainers may not know how to route **`needs-triage`** and mis-typed items.

## Description

Extend **epic-duck** so “triage” is a documented session mode: classify **Plan**, **Type**, and **Status** for ambiguous tickets using **question-duck**, per the **0006** Answer. Align **rubber-duck**, **setup-duck-skills**, and **`docs/agents/backlog.md`** (and setup seeds that mirror it) so only **epic-duck** handles unanchored and orphan routing.

## Notes

- **0004** Answer still mentions deferred triage decision; add a one-line cross-reference to **0006** in **Comments** or amend the Answer triage bullet when editing is in scope for the implementer.
- Historical spike/decision text may still say “planned triage-duck”; change only live skills and `docs/agents/*` unless the user expands scope.

## Out of Scope

- New ADR unless required for workflow change (prefer skill + `backlog.md`).
- **AGENTS.md** unless it lists triage-duck today (verify before edit).

## Acceptance Criteria

- [x] **`epic-duck/SKILL.md`**: New or expanded section covers ambiguous-ticket triage — user entry via epic-duck; **question-duck** for classification; unanchored **`Plan: (unanchored)`** + **`needs-triage`**; orphan/wrong **Type** / missing **Plan**; **`ready`** only via **amigo-duck** where applicable; no callable triage helper from other skills.
- [x] **`rubber-duck/SKILL.md`**: User-facing triage message points to **epic-duck** only (no **triage-duck**).
- [x] **`setup-duck-skills/SKILL.md`**: Done / consumer list does not promise **triage-duck**; lists the seven in-repo planning skills only.
- [x] **`docs/agents/backlog.md`** and **`setup-duck-skills/backlog-local.md`**: Unanchored / **`needs-triage`** handover names **epic-duck** only (remove “or triage-duck” / “future triage-duck”).
- [x] Plan **0001** Destination and Notes match **0006** (no in-scope **triage-duck** skill) if not already updated in the same change set as this task.
