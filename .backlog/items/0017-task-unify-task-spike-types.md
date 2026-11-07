Type: task
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Single `Type: task` / `Type: spike` for epic-duck and rubber-duck; update canon and backlog.
Blocked by:

## Problem Statement

Task and spike ticket kinds used duplicate `Type:` values for epic vs rubber publishers, forcing parallel docs and amigo-duck branches without a behavioural difference.

## Description

Collapse planning-only task/spike types into **`Type: task`** and **`Type: spike`**. Keep **`Type: epic-duck:plan`** and **`Type: epic-duck:decision`** as epic-duck-only kinds.

Update SSOT (`docs/agents/backlog.md`, ADR 0001, setup seeds, skills), remote child label guidance, and rewrite backlog decision/spike prose to current vocabulary. Migrate item files **0003**, **0011**, **0015**, **0016** to `Type: task` / `Type: spike`.

## Acceptance Criteria

- [x] `docs/agents/backlog.md` and `setup-duck-skills/backlog-local.md` use the unified kind table and single task/spike templates.
- [x] ADR 0001 namespace covers plan/decision only under `epic-duck:`; task/spike documented as shared.
- [x] `epic-duck`, `rubber-duck`, `amigo-duck`, `setup-duck-skills` skills and remote `backlog-*.md` seeds aligned.
- [x] All `.backlog/items/*` use `Type: task` or `Type: spike` where applicable; resolved decisions/spikes rewritten to match.
- [x] Canon under `skills/`, `docs/`, and `.backlog/` uses only `Type: task` / `Type: spike` for task and spike items.

## Comments
