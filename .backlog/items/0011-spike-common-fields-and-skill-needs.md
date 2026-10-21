Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Recommend common ticket fields vs per-type exceptions from skill needs and upstream references.
Result: [0011-common-fields-and-skill-needs.md](../spike/0011-common-fields-and-skill-needs.md)
Blocked by:

## Question

Should epic-duck decisions, tasks, spike items, spike findings, and `ready` deliverables share a single **common fields** set (metadata + body conventions), or do skill needs require deliberate per-type exceptions—including `Type: decision` and possibly others?

Investigate in-repo skills under `.cursor/skills/` (how each defines inputs/outputs and backlog artefacts) and compare to related **Matt Pocock** skills under `~/.agents/skills/` (e.g. `writing-for-agents`, `code-review`, `pr`) as an external reference. Deliver a recommendation for [0005-decision-ticket-shapes-and-fields.md](0005-decision-ticket-shapes-and-fields.md) and the ADR.

## Comments

Resolved in [0011-common-fields-and-skill-needs.md](../spike/0011-common-fields-and-skill-needs.md). **0005** unblocked to codify in `backlog.md`, skills, and ADR.
