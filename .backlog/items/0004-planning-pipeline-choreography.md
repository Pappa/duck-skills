Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: When to use epic-duck vs rubber-duck and how skills hand off.
Type: planning
Blocked by:

## Question

When should a user (or agent) choose **epic-duck** vs **rubber-duck** vs standalone **question-duck** / **architect-duck**, and what is the ordered handoff between setup, planning, amigo-duck, spike-duck, and triage-duck?

Resolution must be documentable in skill text and exercisable in eval scenarios.

## Answer

### Which pipeline

| User situation | Skill | What it may change |
|----------------|--------|-------------------|
| Multi-session work, unclear route, or **large feature** | **epic-duck** | **Feature plan** and **any** child artefacts: issues (`Type: planning` \| `task`, optional `Label: ready`), spike items, blocking, plan sections |
| Single-session work at **one ticket / story scale** | **rubber-duck** | **One or more issues and/or spike items** on an **existing** feature only; glossary / ADR as needed. **No** new features or plans |
| Eval / real repo without tracker | **setup-duck-skills** | Run once (eval harness runs this in test setup) |

**question-duck** and **architect-duck** are **not** user-invoked on their own in v1. They run **inside epic-duck and rubber-duck** so shared understanding and recorded design decisions stay consistent.

**triage-duck:** Out of v1 choreography; revisit after evals and core skills mature (**0006** / **0010** deferred).

### Shared behaviours (both epic and rubber)

- **question-duck** — round-based Q&A until assumptions are documented and decisions are sharp.
- **architect-duck** — challenge vocabulary, stress-test scenarios, update **GLOSSARY.md** / **docs/adr/** when decisions land. **Epic-duck invokes architect-duck directly** when needed; rubber does the same within its session. If the user explicitly wants a **rubber-style** domain pass during an epic session, epic-duck may **delegate to rubber-duck**.
- **amigo-duck** — run **before publish** of any backlog **issue** or **spike item** created by epic or rubber.

### Rubber-duck backlog rules

- Attach items to a **named feature plan**; if the user did not name it, **confirm the plan** with the user before writing.
- May create **multiple** issues and/or spike items in one session.
- Terminology: **issue** and **spike item** per `docs/agents/backlog.md` (not a separate “story” type until domain glossary exists).

### Epic-duck backlog rules

- Owns charting, fog, child resolution, and **spike items** for v1 eval paths (**spike-duck** writes findings).
- Does not replace rubber for ticket-sized single-session work when the user only needs one or a few items without plan work.

### Missing backlog

If `docs/agents/backlog.md` or the configured tracker (e.g. `.backlog/`) is missing, **tell the user to run setup-duck-skills** — do not invent tracker layout. Eval harness runs setup as part of test setup.

### Golden paths (evals)

**Epic:** `setup-duck-skills` (harness) → **epic-duck** → **question-duck** (per child) → **architect-duck** (when domain/docs need updating) → **amigo-duck** (pre-publish) → backlog → **spike-duck** (when a spike item exists) → resolve child.

**Rubber:** `setup-duck-skills` (harness) → **rubber-duck** (question-duck + architect-duck) → **amigo-duck** (per published issue/spike item) → backlog on **confirmed** feature.

### Skill text follow-up

Reflect this answer in **epic-duck**, **rubber-duck**, **question-duck**, and **architect-duck** SKILL.md (invocation / `disable-model-invocation` as appropriate). **0013** skill-usage scenarios should exercise both golden paths. **0005** may cross-link terminology.

## Comments

Round 1–2 captured in Answer. Spikes beyond epic-duck and triage timing remain on plan **Not yet specified**.
