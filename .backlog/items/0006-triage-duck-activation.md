Status: needs-detail
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Decide triage-duck role, labels, and activation model.
Type: planning
Blocked by:

## Question

What is **triage-duck** responsible for relative to **amigo-pato** and `docs/agents/ticket-labels.md` (`needs-triage`, `needs-detail`, `ready`, `wontfix`)?

Record and decide between at least these implementation options:

1. **User-activated only** — maintainer invokes triage-duck to classify or advance tickets.
2. **Callable from other skills** — planning skills invoke triage-duck (or shared rules) for auto-triage suggestions or label updates after publish.

Resolution must state default label transitions, who may set `ready`, and whether triage-duck runs before or after amigo-pato in each path.

## Comments
