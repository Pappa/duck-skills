Status: in-progress

## Destination

Planning and refinement duck-skills in this repo produce concise, unambiguous backlog tickets (decision issues and `ready` deliverables) with documented assumptions and testable acceptance criteria. `setup-duck-skills`, `epic-duck`, `rubber-duck`, and their dependencies behave predictably; new `triage-duck` supports ticket lifecycle; lightweight evals in `evals/` exercise golden paths on a dummy project.

## Notes

**In-scope skills (only):** `setup-duck-skills`, `epic-duck`, `rubber-duck`, `question-duck`, `architect-duck`, `amigo-pato`, `spike-duck`, and new `triage-duck`. Development, implementation, and testing skills are a separate future feature.

**Composition (not duplication):** `rubber-duck` orchestrates `question-duck` + `architect-duck` in one session. `epic-duck` uses `question-duck`, `amigo-pato`, and `spike-duck` per its workflow. No merge/dedupe of those skills unless evals show systematic agent confusion.

**Done signal:** An agent (or human) runs documented eval scenarios against `evals/sandbox_project` (or copy); run **scores** meet per-skill thresholds; produced tickets reach **amigo-pato Approve** where required (after amigo-pato meta-eval exists); **Usability** is logged in `evals/runs/` artefacts. Token use stays lightweight.

**Eval layout (target):** Dummy repo under `evals/sandbox_project`; harness under `evals/` focusing on planning a dummy software idea through the skills and judging outcomes—not full product implementation. Run logs under `evals/runs/` with artefacts in `evals/runs/artefacts/<scenario>-<date>/` (scores, `model_id`, saved amigo-pato verdicts).

**Skills to consult when resolving children:** `question-duck`, `spike-duck`, `amigo-pato`, `writing-for-agents` (if skill text changes).

## Decisions so far

- [Ready ticket quality bar](0002-ready-ticket-quality-bar.md): One ticket family with `planning` (and possibly other) exceptions; amigo-pato gate for `ready`; scored evals (Ticket quality, Planning resolution metric, Skill usage, Usability) with per-skill pass thresholds; v1 no accepted-gaps workflow; field canon via spike 0011 + 0005 + ADR.

## Not yet specified

- **Triage-duck activation:** user-invoked skill only vs also callable by other skills for auto-triage (see [0006-triage-duck-activation.md](0006-triage-duck-activation.md)).
- **Accepted gaps (future):** Quality findings (from amigo-pato or eval metrics) the **operator** explicitly tolerates for a run instead of requiring a fix before publish. v1: not used — sub-Approve lowers **Ticket quality**; notes in **Usability**. Later: optional acceptance with a **score penalty**; rename term TBD.

## Out of scope

- Cursor-global or team-kit skills not shipped under this repo’s `.cursor/skills/`.
- Implementation, coding, and testing agent skills (later feature).
- Hosted CI or mandatory cloud eval runners for v1.

## Issues

| Issue | Overview | Status |
|-------|----------|--------|
| [0002-ready-ticket-quality-bar.md](0002-ready-ticket-quality-bar.md) | Define the quality bar for `ready` tickets and eval pass/fail. | resolved |
| [0004-planning-pipeline-choreography.md](0004-planning-pipeline-choreography.md) | When to use epic-duck vs rubber-duck and how skills hand off. | needs-detail |
| [0005-ticket-shapes-and-fields.md](0005-ticket-shapes-and-fields.md) | Align ticket shapes with `docs/agents/backlog.md` and skill output. | needs-detail |
| [0006-triage-duck-activation.md](0006-triage-duck-activation.md) | Decide triage-duck role, labels, and activation model. | needs-detail |
| [0008-setup-duck-skills-verification.md](0008-setup-duck-skills-verification.md) | Expected setup behavior and how evals assert it. | needs-detail |
| [0009-sandbox-project-and-harness.md](0009-sandbox-project-and-harness.md) | Build `evals/sandbox_project` and the lightweight eval harness. | needs-detail |
| [0010-implement-triage-duck.md](0010-implement-triage-duck.md) | Add `triage-duck` skill per decided design. | needs-detail |
| [0012-amigo-pato-eval-golden-set.md](0012-amigo-pato-eval-golden-set.md) | Define a golden set to validate amigo-pato verdicts before eval automation trusts it. | needs-detail |
| [0013-skill-usage-eval-scenarios.md](0013-skill-usage-eval-scenarios.md) | Define eval scenarios that detect agents misusing or misunderstanding skill and doc text. | needs-detail |

## Spikes

| Spike | Overview | Status |
|-------|----------|--------|
| [0003-spike-skill-inventory.md](0003-spike-skill-inventory.md) | Map in-scope skills, dependencies, and artefacts they touch. | needs-detail |
| [0007-spike-eval-harness-design.md](0007-spike-eval-harness-design.md) | Design lightweight eval scenarios, layout, and token budget. | needs-detail |
| [0011-spike-common-fields-and-skill-needs.md](0011-spike-common-fields-and-skill-needs.md) | Recommend common ticket fields vs per-type exceptions from skill needs and upstream references. | needs-detail |
