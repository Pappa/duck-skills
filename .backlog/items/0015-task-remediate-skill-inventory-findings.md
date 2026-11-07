Type: task
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Apply decision 0014 — align skills, docs, and backlog canon to publisher rules and spike 0003 register.
Blocked by:

## Problem Statement

Spike **0003** (v2.4) and decision **[0014](0014-decision-skill-inventory-remediation.md)** record open drift between skills, README, setup seeds, resolved decisions **0002** / **0004**, spike **0011**, and backlog canon. Agents can mis-route rubber vs epic work or publish the wrong `Type:` until remediation lands.

## Description

Implement the **`## Answer`** in **0014** in one pass (same PR acceptable). Split into follow-on tasks only if the user chooses after review.

**Publisher rules (summary):**

- **epic-duck** publishes **`Type: epic-duck:plan`**, **`Type: epic-duck:decision`**, and may publish **`Type: task`** / **`Type: spike`** under a plan.
- **rubber-duck** publishes **`Type: task`** and **`Type: spike`** only — not plan or decision.
- Unanchored rubber items: **`Plan: (unanchored)`**, **`Status: needs-triage`**; tell the user the item is not on an epic and will need triage later; **epic-duck** attaches a real `Plan:` when an epic exists.

Update **`docs/agents/backlog.md`** (and setup seeds that mirror it). Set **question-duck** / **architect-duck** `disable-model-invocation: true`, **`allow_implicit_invocation: true`** in agent YAML; README not a user entry point for those skills.

## Notes

- **question-duck** lines 8, 26, 30: open/closed wording per **0014** Answer (reserve **Frontier** for backlog).
- **0004** Answer amended in this work — not only skills.
- **spike-duck** typo **L3**: “authoritative”.

## Out of Scope

- **triage** behaviour (**0006**)
- Eval harness (descoped on plan **0001**)
- New ADR number unless required — prefer extending `backlog.md` + short note in ADR 0001 consequences if needed

## Acceptance Criteria

- [x] **`rubber-duck/SKILL.md`**: documents session outcomes (clarity, doc/code change, impl **task**/**spike**); **question-duck** + **architect-duck** (architect never invokes rubber); **no** `epic-duck:decision`; **no** epic↔rubber delegation prose; unanchored publish rule + user-facing triage message; **amigo-duck** before publish.
- [x] **`epic-duck/SKILL.md`**: invokes **architect-duck** (aligned wording with rubber); **no** delegate-to-rubber; planning types only; **C-epic-labelled**, **R6**, **R7** (spike resolve + optional Comments in templates) addressed in same file edit.
- [x] **`question-duck/SKILL.md`**: open/closed round rules (lines 8, 26, 30); `disable-model-invocation: true`.
- [x] **`architect-duck/SKILL.md`**: `disable-model-invocation: true`.
- [x] **`question-duck/agents/openai.yml`** and **`architect-duck/agents/openai.yml`**: `policy.allow_implicit_invocation: true`; interface text matches SKILL (no typos).
- [x] **`spike-duck/SKILL.md`**: prefer existing spike item when epic set `Result:`; fix **L3** typo; numbering guidance **C-spike-NNNN**.
- [x] **`docs/agents/backlog.md`** (+ **`setup-duck-skills/backlog-local.md`** parity): **`Type: task`** / **`Type: spike`**; filenames; **`Plan: (unanchored)`**; publisher table; backlog **Frontier** unchanged.
- [x] **`setup-duck-skills/backlog-github.md`**: frontier includes **`needs-triage`** (**C-github-frontier**).
- [x] **`README.md`**: planning flow matches **0014**; rubber vs epic; **question-duck** / **architect-duck** not user entry points (**C-readme-rubber**, **R4**).
- [x] **`amigo-duck/SKILL.md`**: review paths per **`Type:`** (**Q8**).
- [x] **`0004-decision-planning-pipeline-choreography.md`**: Answer rewritten — rubber impl items only, no rubber decisions, no epic↔rubber delegation, architect via epic/rubber only (**Q10**).
- [x] **`0002-decision-ready-ticket-quality-bar.md`**: Answer uses **`Status: ready`**, current **`Type:`** vocabulary — no `Label:` or bare `Type: decision` (**Q2**).
- [x] **`../spikes/0011-common-fields-and-skill-needs.md`**: historical `Label:` / pre-namespace prose removed or rewritten to ADR canon (**C-0011-stale**).
- [x] Plan **0001** Notes: still states epic uses **architect-duck**; consistent with epic skill (**C-plan-notes**).
- [x] **v1 C1–C2**: recorded as verified closed in **0014** (no code change required unless audit finds regression).

## Comments

## amigo-duck review

**Verdict: Approve**

| Axis | Result |
|------|--------|
| Fit | Implements **0014** Answer and user interview outcomes. |
| Complete | AC maps to register IDs; boundaries clear. |
| Plain language | Testable checkboxes per artefact. |
| INVEST | One iteration-sized if focused; user may split after diff review. |
