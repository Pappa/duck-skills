Type: epic-duck:task
Status: ready
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Apply decision 0014 — align skills, docs, and backlog canon to planning vs implementation items and spike 0003 register.
Blocked by:

## Problem Statement

Spike **0003** (v2.4) and decision **[0014](0014-decision-skill-inventory-remediation.md)** record open drift between skills, README, setup seeds, resolved decisions **0002** / **0004**, spike **0011**, and backlog canon. Agents can mis-route rubber vs epic work or publish the wrong `Type:` until remediation lands.

## Description

Implement the **`## Answer`** in **0014** in one pass (same PR acceptable). Split into follow-on tasks only if the user chooses after review.

**Planning vs implementation (summary):**

- **epic-duck** publishes **`Type: epic-duck:decision`**, **`epic-duck:task`**, **`epic-duck:spike`** (planning-era shapes per ADR 0001).
- **rubber-duck** publishes **`Type: task`**, **`Type: spike`** only — implementation/development work; filenames **`NNNN-task-<slug>.md`**, **`NNNN-spike-<slug>.md`**; same counter and `.backlog/items/`.
- Unanchored rubber items: **`Plan: (unanchored)`**, **`Status: needs-triage`**; tell the user the item is not on a feature and will need triage later; **epic-duck** attaches a real `Plan:` when a feature exists.

Update **`docs/agents/backlog.md`** (and setup seeds that mirror it) with implementation item profiles. Extend **amigo-duck** to review planning vs implementation formats. Set **question-duck** / **architect-duck** `disable-model-invocation: true`, **`allow_implicit_invocation: true`** in agent YAML; README not a user entry point for those skills.

## Notes

- **question-duck** lines 8, 26, 30: open/closed wording per **0014** Answer (reserve **Frontier** for backlog).
- **0004** Answer amended in this work — not only skills.
- **spike-duck** typo **L3**: “authoritative”.

## Out of Scope

- **triage-duck** skill (**0006** / **0010**)
- Eval harness (**0013** and related)
- New ADR number unless required — prefer extending `backlog.md` + short note in ADR 0001 consequences if needed

## Acceptance Criteria

- [ ] **`rubber-duck/SKILL.md`**: documents session outcomes (clarity, doc/code change, impl **task**/**spike**); **question-duck** + **architect-duck** (architect never invokes rubber); **no** `epic-duck:decision`; **no** epic↔rubber delegation prose; unanchored publish rule + user-facing triage message; **amigo-duck** before publish.
- [ ] **`epic-duck/SKILL.md`**: invokes **architect-duck** (aligned wording with rubber); **no** delegate-to-rubber; planning types only; **C-epic-labelled**, **R6**, **R7** (spike resolve + optional Comments in templates) addressed in same file edit.
- [ ] **`question-duck/SKILL.md`**: open/closed round rules (lines 8, 26, 30); `disable-model-invocation: true`.
- [ ] **`architect-duck/SKILL.md`**: `disable-model-invocation: true`.
- [ ] **`question-duck/agents/openai.yml`** and **`architect-duck/agents/openai.yml`**: `policy.allow_implicit_invocation: true`; interface text matches SKILL (no typos).
- [ ] **`spike-duck/SKILL.md`**: prefer existing spike item when epic set `Result:`; fix **L3** typo; numbering guidance **C-spike-NNNN**.
- [ ] **`docs/agents/backlog.md`** (+ **`setup-duck-skills/backlog-local.md`** parity): implementation **`Type: task`** / **`Type: spike`**; filenames; **`Plan: (unanchored)`**; rubber vs epic planning table; backlog **Frontier** unchanged.
- [ ] **`setup-duck-skills/backlog-github.md`**: frontier includes **`needs-triage`** (**C-github-frontier**); **R8** triage-duck mention in setup consumer list when shipped.
- [ ] **`README.md`**: planning flow matches **0014**; rubber vs epic; **question-duck** / **architect-duck** not user entry points (**C-readme-rubber**, **R4**).
- [ ] **`amigo-duck/SKILL.md`**: distinct review paths for **`Type: epic-duck:*`** vs **`Type: task`** / **`Type: spike`** (**Q8**).
- [ ] **`0004-decision-planning-pipeline-choreography.md`**: Answer rewritten — rubber impl items only, no rubber decisions, no epic↔rubber delegation, architect via epic/rubber only (**Q10**).
- [ ] **`0002-decision-ready-ticket-quality-bar.md`**: Answer uses **`Status: ready`**, **`Type: epic-duck:*`** only — no `Label:` or bare `Type: decision` (**Q2**).
- [ ] **`../spike/0011-common-fields-and-skill-needs.md`**: historical `Label:` / pre-namespace prose removed or rewritten to ADR canon (**C-0011-stale**).
- [ ] Plan **0001** Notes: still states epic uses **architect-duck**; consistent with epic skill (**C-plan-notes**).
- [ ] **v1 C1–C2**: recorded as verified closed in **0014** (no code change required unless audit finds regression).

## Comments

## amigo-duck review

**Verdict: Approve**

| Axis | Result |
|------|--------|
| Fit | Implements **0014** Answer and user interview outcomes. |
| Complete | AC maps to register IDs; boundaries clear. |
| Plain language | Testable checkboxes per artefact. |
| INVEST | One iteration-sized if focused; user may split after diff review. |
