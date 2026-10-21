Status: in-progress

## Destination

Planning and refinement duck-skills in this repo produce concise, unambiguous backlog tickets (decisions and `ready` deliverables) with documented assumptions and testable acceptance criteria. `setup-duck-skills`, `epic-duck`, `rubber-duck`, and their dependencies behave predictably; new `triage-duck` supports ticket lifecycle; lightweight evals in `evals/` exercise golden paths on a dummy project.

## Notes

**In-scope skills (only):** `setup-duck-skills`, `epic-duck`, `rubber-duck`, `question-duck`, `architect-duck`, `amigo-duck`, `spike-duck`, and new `triage-duck`. Development, implementation, and testing skills are a separate future feature.

**Composition (not duplication):** `rubber-duck` and `epic-duck` both use `question-duck` and `architect-duck`; epic-duck also uses `amigo-duck` and `spike-duck` for plan/backlog work. `question-duck` / `architect-duck` are not standalone user entry points in v1. See [0004-decision-planning-pipeline-choreography.md](0004-decision-planning-pipeline-choreography.md). No merge/dedupe unless evals show systematic agent confusion.

**Done signal:** An agent (or human) runs documented eval scenarios against `evals/sandbox_project` (or copy); run **scores** meet per-skill thresholds; produced tickets reach **amigo-duck Approve** where required (after amigo-duck meta-eval exists); **Usability** is logged in `evals/runs/` artefacts. Token use stays lightweight.

**Eval layout (target):** Dummy repo under `evals/sandbox_project`; harness under `evals/` focusing on planning a dummy software idea through the skills and judging outcomes—not full product implementation. Run logs under `evals/runs/` with artefacts in `evals/runs/artefacts/<scenario>-<date>/` (scores, `model_id`, saved amigo-duck verdicts).

**Skills to consult when resolving children:** `question-duck`, `spike-duck`, `amigo-duck`, `writing-for-agents` (if skill text changes).

## Decisions so far

- [Ready ticket quality bar](0002-decision-ready-ticket-quality-bar.md): One ticket family with `Type: decision` (and possibly other) exceptions; amigo-duck gate for `ready`; scored evals (Ticket quality, Decision resolution metric, Skill usage, Usability) with per-skill pass thresholds; v1 no accepted-gaps workflow; field canon via spike 0011 + 0005 + ADR.
- [Eval harness scope](0007-spike-eval-harness-design.md): Single spike **0007** designs one harness with meta-eval (amigo-duck + gold from **0012**) and skill-path layers; golden cases and skill-usage scenarios stay in **0012** / **0013**; **0007** blocked by **0012**, **0013**.
- [Skill inventory](0003-skill-inventory.md): Eight in-repo skills mapped; **triage-duck** missing; epic-duck vs `backlog.md` spike/`Type` contradiction flagged for **0005**.
- [Common fields](0011-common-fields-and-skill-needs.md): Shared header on items; body profiles for plan, decision, task, ready (`Label: ready` + AC), spike item/findings; terminology aligned in **0005** + ADR.
- [Planning pipeline choreography](0004-decision-planning-pipeline-choreography.md): Epic = plans + all ticket types; rubber = single-session decisions/tasks/spikes on confirmed feature; amigo-duck before publish; missing backlog → setup-duck-skills; v1 spikes via epic-duck; question/architect only via epic or rubber.

## Not yet specified

- **Triage-duck:** Deferred until evals and core skills are in good shape (see [0006-decision-triage-duck-activation.md](0006-decision-triage-duck-activation.md), [0010-implement-triage-duck.md](0010-implement-triage-duck.md)).
- **Spike entry points (future):** v1 spikes opened through **epic-duck**; possible later: **rubber-duck** or direct **spike-duck** without forbidding other paths yet.
- **Accepted gaps (future):** Quality findings (from amigo-duck or eval metrics) the **operator** explicitly tolerates for a run instead of requiring a fix before publish. v1: not used — sub-Approve lowers **Ticket quality**; notes in **Usability**. Later: optional acceptance with a **score penalty**; rename term TBD.

## Out of scope

- Cursor-global or team-kit skills not shipped under this repo’s `.cursor/skills/`.
- Implementation, coding, and testing agent skills (later feature).
- Hosted CI or mandatory cloud eval runners for v1.

## Decisions

| Decision | Overview | Status |
|----------|----------|--------|
| [0002-decision-ready-ticket-quality-bar.md](0002-decision-ready-ticket-quality-bar.md) | Define the quality bar for `ready` tickets and eval pass/fail. | resolved |
| [0004-decision-planning-pipeline-choreography.md](0004-decision-planning-pipeline-choreography.md) | When to use epic-duck vs rubber-duck and how skills hand off. | resolved |
| [0005-decision-ticket-shapes-and-fields.md](0005-decision-ticket-shapes-and-fields.md) | Align ticket shapes with `docs/agents/backlog.md` and skill output. | needs-detail |
| [0006-decision-triage-duck-activation.md](0006-decision-triage-duck-activation.md) | Decide triage-duck role, labels, and activation model. | needs-detail |
| [0008-decision-setup-duck-skills-verification.md](0008-decision-setup-duck-skills-verification.md) | Expected setup behavior and how evals assert it. | needs-detail |
| [0012-decision-amigo-duck-eval-golden-set.md](0012-decision-amigo-duck-eval-golden-set.md) | Define a golden set to validate amigo-duck verdicts before eval automation trusts it. | needs-detail |
| [0013-decision-skill-usage-eval-scenarios.md](0013-decision-skill-usage-eval-scenarios.md) | Define eval scenarios that detect agents misusing or misunderstanding skill and doc text. | needs-detail |

## Tasks

| Task | Overview | Status |
|------|----------|--------|
| [0009-sandbox-project-and-harness.md](0009-sandbox-project-and-harness.md) | Build `evals/sandbox_project` and the lightweight eval harness. | needs-detail |
| [0010-implement-triage-duck.md](0010-implement-triage-duck.md) | Add `triage-duck` skill per decided design. | needs-detail |

## Spikes

| Spike | Overview | Status |
|-------|----------|--------|
| [0003-spike-skill-inventory.md](0003-spike-skill-inventory.md) | Map in-scope skills, dependencies, and artefacts they touch. | resolved |
| [0007-spike-eval-harness-design.md](0007-spike-eval-harness-design.md) | Design one eval harness (meta-eval + skill-path layers), sandbox layout, and token budget. | needs-detail |
| [0011-spike-common-fields-and-skill-needs.md](0011-spike-common-fields-and-skill-needs.md) | Recommend common ticket fields vs per-type exceptions from skill needs and upstream references. | resolved |
