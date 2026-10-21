Status: needs-detail
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Define a golden set to validate amigo-duck verdicts before eval automation trusts it.
Type: planning
Blocked by:

## Question

What minimal **golden set** of draft tickets and expected **amigo-duck** outcomes (Approve vs Revise, which axes fail) proves the skill is reliable enough to drive the **Ticket quality** eval subscore?

Resolution must cover: number of cases, ticket types represented (`ready`, `planning`, spike), how expected verdicts are maintained, and how harness runs compare agent-or-script output to gold without excessive tokens.

## Comments

Spike [0007-spike-eval-harness-design.md](0007-spike-eval-harness-design.md) is blocked on this issue resolving (meta-eval layer consumes the golden set).
