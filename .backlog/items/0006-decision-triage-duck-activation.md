Type: epic-duck:decision
Status: needs-detail
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Decide triage-duck role, status workflow, and activation model.
Blocked by:

## Question

What is **triage-duck** responsible for relative to **amigo-duck** and unified **`Status:`** in `docs/agents/ticket-labels.md` (`needs-triage`, `needs-detail`, `ready`, `wontfix`, etc.)?

Record and decide between at least these implementation options:

1. **User-activated only** — maintainer invokes triage-duck to classify or advance tickets.
2. **Callable from other skills** — planning skills invoke triage-duck (or shared rules) for auto-triage suggestions or label updates after publish.

Resolution must state default **status** transitions, who may set **`Status: ready`**, and whether triage-duck runs before or after amigo-duck in each path.

## Comments
