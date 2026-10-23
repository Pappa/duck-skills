Type: epic-duck:decision
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Decide triage role, status workflow, and activation model.
Blocked by:

## Question

Should there be a **triage-duck** skill? If so, what is **triage-duck** responsible for relative to **amigo-duck** and unified **`Status:`** in `docs/agents/ticket-statuses.md` (`needs-triage`, `needs-detail`, `ready`, `wontfix`, etc.)?

Record and decide between at least these implementation options:

1. **User-activated only** — maintainer invokes triage-duck to classify or advance tickets.
2. **Callable from other skills** — planning skills invoke triage-duck (or shared rules) for auto-triage suggestions or **status** updates after publish.

Resolution must state default **status** transitions, who may set **`Status: ready`**, and whether triage-duck runs before or after amigo-duck in each path.

## Answer

**No separate `triage-duck` skill.** Keep **`needs-triage`** (and the rest of unified **`Status:`**) as backlog vocabulary. **epic-duck** owns classification and routing for ambiguous tickets, with **question-duck** for HITL interviews. Follow-on deliverable **0016** updates epic-duck and aligned docs.

### Scope of “triage” (epic-duck)

- **Unanchored implementation items** — **`Plan: (unanchored)`**, **`Status: needs-triage`** from **rubber-duck**: user invokes **epic-duck**; session picks or creates a feature plan, sets a real **`Plan:`** link, and moves **`Status:`** off **`needs-triage`** when the user confirms.
- **Orphan or mis-typed items** — wrong **`Type:`**, missing **`Plan:`**, or item on the wrong feature: same epic-duck session with **question-duck** to settle plan, kind, and target status.

### Entry points and choreography

- **User invokes epic-duck** (optionally naming a ticket). **rubber-duck** publishes unanchored items and warns only; it does **not** auto-route or call a triage helper.
- **amigo-duck** remains the gate for **`Status: ready`** on deliverable tasks where that gate applies. Epic-duck may set **`needs-detail`**, attach **`Plan:`**, or advance planning children per existing rules; it does **not** skip **amigo-duck** to set **`ready`**.

### Status transitions (defaults)

| From | Typical next | Who |
|------|----------------|-----|
| `needs-triage` | `needs-detail` or attached plan + `needs-detail` | epic-duck session after user confirms classification |
| `needs-detail` | `ready` (deliverables) or stay `needs-detail` | after requirements sharp; **`ready`** only after **amigo-duck** where required |
| Any open child | `in-progress` | epic-duck when session starts work (existing rules) |

Callable-from-other-skills option **rejected** — no hidden triage module; other skills reference **epic-duck** in user-facing text only.

## Comments

Resolved per question-duck round (2026-10-22): fold triage into epic-duck; yes to all five closure questions.
