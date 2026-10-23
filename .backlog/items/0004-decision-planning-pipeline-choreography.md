Type: epic-duck:decision
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: When to use epic-duck vs rubber-duck and how skills hand off.
Blocked by:

## Question

When should a user choose **epic-duck** vs **rubber-duck**, and what is the ordered handoff between setup, planning, amigo-duck, and spike-duck?

Resolution must be documentable in skill text and exercisable in eval scenarios.

## Answer

### Which pipeline

| User situation | Skill | What it may change |
|----------------|--------|-------------------|
| Multi-session work, unclear route, or **large feature** | **epic-duck** | **Feature plan** and **planning** children: `Type: epic-duck:decision`, `epic-duck:task`, `epic-duck:spike`; plan sections, blocking, fog |
| Single-session work toward a **concrete outcome** | **rubber-duck** | Clarity, doc/code changes, **`GLOSSARY.md` / ADRs**, and **implementation** backlog items: **`Type: task`**, **`Type: spike`** only — **not** `epic-duck:decision` or other `epic-duck:*` planning types |
| Eval / real repo without tracker | **setup-duck-skills** | Run once (eval harness runs this in test setup) |

**question-duck** and **architect-duck** are **not** user entry points. They run **inside epic-duck and rubber-duck** (`disable-model-invocation` on the leaf skills; implicit invocation from orchestrators).

**epic-duck** and **rubber-duck** are **not** invoked by each other — only by the user.

**Ambiguous ticket routing:** No separate triage skill — **epic-duck** + **question-duck** classify **`needs-triage`** and orphan items per resolved **0006**.

### Shared behaviours (epic and rubber)

- **question-duck** — round-based Q&A until assumptions are documented (open/closed question sets per question-duck skill).
- **architect-duck** — challenge vocabulary, stress-test scenarios, update **GLOSSARY.md** / **docs/adr/** when decisions land. **Epic-duck** and **rubber-duck** each invoke **architect-duck** the same way when domain docs need updating during their session.
- **amigo-duck** — run **before publish** of any backlog item they create (planning `epic-duck:*` or implementation `task` / `spike`).

### Rubber-duck backlog rules

- Prefer items on a **confirmed** feature plan (`Plan:` → plan file). If the user has no plan yet, may write **`Plan: (unanchored)`**, **`Status: needs-triage`**, correct **NNNN**, and tell the user the ticket is **not associated with a feature** and **will need to be triaged later**.
- May create **`Type: task`** and **`Type: spike`** implementation items (`NNNN-task-<slug>.md`, `NNNN-spike-<slug>.md`). **No** `epic-duck:decision`. **No** new feature plans.
- **spike-duck** writes findings for implementation spikes.

### Epic-duck backlog rules

- Owns charting, fog, child resolution, and **planning** spike items (`Type: epic-duck:spike`).
- Publishes only **`Type: epic-duck:decision`**, **`epic-duck:task`**, **`epic-duck:spike`** under a feature plan.
- May attach a real **`Plan:`** to unanchored implementation items created by rubber.

### Missing backlog

If `docs/agents/backlog.md` or the configured tracker (e.g. `.backlog/`) is missing, **tell the user to run setup-duck-skills** — do not invent tracker layout.

### Golden paths (evals)

**Epic:** `setup-duck-skills` (harness) → **epic-duck** → **question-duck** (per child) → **architect-duck** (when domain/docs need updating) → **amigo-duck** (pre-publish) → backlog → **spike-duck** (when a planning spike item exists) → resolve child.

**Rubber:** `setup-duck-skills` (harness) → **rubber-duck** (question-duck + architect-duck) → **amigo-duck** (per published `task` / `spike`) → backlog when applicable.

### Skill text follow-up

Reflected in skill files via decision **[0014](0014-decision-skill-inventory-remediation.md)** and task **0015**.

## Comments

Supersedes pre-0014 bullets that allowed rubber **decisions** or epic→rubber delegation. Canon: `docs/agents/backlog.md`, ADR 0001 (planning namespace) + implementation `Type: task` / `Type: spike`.
