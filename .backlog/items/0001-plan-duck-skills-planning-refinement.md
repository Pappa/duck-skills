Status: in-progress

## Destination

Planning and refinement duck-skills in this repo produce concise, unambiguous backlog tickets (decision issues and `ready` deliverables) with documented assumptions and testable acceptance criteria. `setup-duck-skills`, `epic-duck`, `rubber-duck`, and their dependencies behave predictably; new `triage-duck` supports ticket lifecycle; lightweight evals in `evals/` exercise golden paths on a dummy project.

## Notes

**In-scope skills (only):** `setup-duck-skills`, `epic-duck`, `rubber-duck`, `question-duck`, `architect-duck`, `amigo-pato`, `spike-duck`, and new `triage-duck`. Development, implementation, and testing skills are a separate future feature.

**Composition (not duplication):** `rubber-duck` orchestrates `question-duck` + `architect-duck` in one session. `epic-duck` uses `question-duck`, `amigo-pato`, and `spike-duck` per its workflow. No merge/dedupe of those skills unless evals show systematic agent confusion.

**Done signal:** An agent (or human) runs documented eval scenarios against `evals/sandbox_project` (or copy); produced tickets pass **amigo-pato** Approve (or accepted gaps are recorded); friction is logged for follow-up. Token use stays lightweight.

**Eval layout (target):** Dummy repo under `evals/sandbox_project`; harness under `evals/` focusing on planning a dummy software idea through the skills and judging outcomes—not full product implementation.

**Skills to consult when resolving children:** `question-duck`, `spike-duck`, `amigo-pato`, `writing-for-agents` (if skill text changes).

## Decisions so far

## Not yet specified

- **Triage-duck activation:** user-invoked skill only vs also callable by other skills for auto-triage (see [0006-triage-duck-activation.md](0006-triage-duck-activation.md)).
- Exact eval rubric beyond amigo-pato verdict + friction log (e.g. required sections per ticket type).

## Out of scope

- Cursor-global or team-kit skills not shipped under this repo’s `.cursor/skills/`.
- Implementation, coding, and testing agent skills (later feature).
- Hosted CI or mandatory cloud eval runners for v1.

## Issues

| Issue | Overview | Status |
|-------|----------|--------|
| [0002-ready-ticket-quality-bar.md](0002-ready-ticket-quality-bar.md) | Define the quality bar for `ready` tickets and eval pass/fail. | needs-detail |
| [0004-planning-pipeline-choreography.md](0004-planning-pipeline-choreography.md) | When to use epic-duck vs rubber-duck and how skills hand off. | needs-detail |
| [0005-ticket-shapes-and-fields.md](0005-ticket-shapes-and-fields.md) | Align ticket shapes with `docs/agents/backlog.md` and skill output. | needs-detail |
| [0006-triage-duck-activation.md](0006-triage-duck-activation.md) | Decide triage-duck role, labels, and activation model. | needs-detail |
| [0008-setup-duck-skills-verification.md](0008-setup-duck-skills-verification.md) | Expected setup behavior and how evals assert it. | needs-detail |
| [0009-sandbox-project-and-harness.md](0009-sandbox-project-and-harness.md) | Build `evals/sandbox_project` and the lightweight eval harness. | needs-detail |
| [0010-implement-triage-duck.md](0010-implement-triage-duck.md) | Add `triage-duck` skill per decided design. | needs-detail |

## Spikes

| Spike | Overview | Status |
|-------|----------|--------|
| [0003-spike-skill-inventory.md](0003-spike-skill-inventory.md) | Map in-scope skills, dependencies, and artefacts they touch. | needs-detail |
| [0007-spike-eval-harness-design.md](0007-spike-eval-harness-design.md) | Design lightweight eval scenarios, layout, and token budget. | needs-detail |
