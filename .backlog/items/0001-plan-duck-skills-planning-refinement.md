Type: epic-duck:plan
Status: in-progress

## Destination

Planning and refinement duck-skills in this repo produce concise, unambiguous backlog tickets (decisions and `ready` deliverables) with documented assumptions and testable acceptance criteria. `setup-duck-skills`, `epic-duck`, `rubber-duck`, and their dependencies behave predictably; **epic-duck** (with **question-duck**) routes ambiguous tickets and **`needs-triage`** items; lightweight evals in `evals/` exercise golden paths on a dummy project.

## Notes

**In-scope skills (only):** `setup-duck-skills`, `epic-duck`, `rubber-duck`, `question-duck`, `architect-duck`, `amigo-duck`, `spike-duck`. Development, implementation, and testing skills are a separate future feature.

**Composition (not duplication):** `rubber-duck` and `epic-duck` both use `question-duck` and `architect-duck` (orchestrators invoke them; not user entry points). **epic-duck** also uses `amigo-duck` and `spike-duck` for planning backlog work. **epic-duck** publishes `epic-duck:*` planning items; **rubber-duck** publishes implementation `Type: task` / `Type: spike`. See [0004-decision-planning-pipeline-choreography.md](0004-decision-planning-pipeline-choreography.md) and [0014-decision-skill-inventory-remediation.md](0014-decision-skill-inventory-remediation.md).

**Done signal (current):** Planning skills produce tickets that reach **amigo-duck Approve** where required when authored or changed; backlog shapes match ADR and `docs/agents/*`. **Automated eval harness and golden-set scoring are temporarily out of scope** (token budget); see **Out of scope**.

**Done signal (when evals return):** Documented eval scenarios against `evals/sandbox_project` (or copy); run **scores** meet per-skill thresholds per [0002-decision-ready-ticket-quality-bar.md](0002-decision-ready-ticket-quality-bar.md); **Usability** logged under `evals/runs/` artefacts. Token use stays lightweight.

**Skills to consult when resolving children:** `question-duck`, `spike-duck`, `amigo-duck`, `writing-for-agents` (if skill text changes).

## Decisions so far

- [Ready ticket quality bar](0002-decision-ready-ticket-quality-bar.md): One ticket family; amigo-duck gate for **`Status: ready`**; scored evals (Ticket quality, Decision resolution metric, Skill usage, Usability) with per-skill pass thresholds; v1 no accepted-gaps workflow.
- [Skill inventory](../spike/0003-skill-inventory-v2.4.md): v2 synthesis — seven skills in repo; ADR 0001 shapes aligned; **0004** vs epic/rubber `SKILL.md` choreography drift (high); v1 retained at [0003-skill-inventory.md](../spike/0003-skill-inventory.md).
- [Ticket shapes and fields](0005-decision-ticket-shapes-and-fields.md): `Type: epic-duck:*` (first line), unified **`Status:`** (incl. `ready`), deliverable task body sections, spike findings TLDR; ADR `docs/adr/0001-backlog-ticket-shapes.md`.
- [Common fields](0011-common-fields-and-skill-needs.md): Spike input to **0005**; superseded for headers by ADR 0001.
- [Planning pipeline choreography](0004-decision-planning-pipeline-choreography.md): Epic = plans + planning `epic-duck:*` children; rubber = single-session impl **`Type: task`** / **`Type: spike`** (and clarity/doc/code); amigo-duck before publish; see **0014** for full split (amends **0004** in remediation).
- [Skill inventory remediation](0014-decision-skill-inventory-remediation.md): Dispositions for spike **0003** register; planning vs impl backlog families; unanchored `Plan: (unanchored)`; question-duck open/closed rounds; **spike entry** — planning via **epic-duck** (`epic-duck:spike` → **spike-duck**); implementation via **rubber-duck** (`Type: spike` → **spike-duck**); **spike-duck** uses existing spike item when **`Result:`** is set (**C-spike-NNNN**). See also [0004](0004-decision-planning-pipeline-choreography.md) golden paths.
- [Triage without triage-duck](0006-decision-triage-activation.md): No standalone triage skill; epic-duck + question-duck classify ambiguous tickets; amigo-duck still gates **`ready`**; **0010** wontfix; **0016** documents flows in skills and canon.

## Not yet specified

- **Accepted gaps (future):** Quality findings (from amigo-duck or eval metrics) the **operator** explicitly tolerates for a run instead of requiring a fix before publish. v1: not used — sub-Approve lowers **Ticket quality**; notes in **Usability**. Later: optional acceptance with a **score penalty**; rename term TBD.

## Out of scope

- **Eval harness:** Automated golden-set meta-eval, skill-usage scenarios, harness design, setup assertions, and sandbox implementation. Descoped to limit token spend on repeated model runs; **may be prioritised again later** (new tickets). Resolved quality bar in **0002** still describes the target model when evals resume.
- Cursor-global or team-kit skills not shipped under this repo’s `.cursor/skills/`.
- Implementation, coding, and testing agent skills (later feature).
- Hosted CI or mandatory cloud eval runners for v1.

## Decisions

| Decision | Overview | Status |
|----------|----------|--------|
| [0002-decision-ready-ticket-quality-bar.md](0002-decision-ready-ticket-quality-bar.md) | Define the quality bar for `ready` tickets and eval pass/fail. | resolved |
| [0004-decision-planning-pipeline-choreography.md](0004-decision-planning-pipeline-choreography.md) | When to use epic-duck vs rubber-duck and how skills hand off. | resolved |
| [0005-decision-ticket-shapes-and-fields.md](0005-decision-ticket-shapes-and-fields.md) | Align ticket shapes with `docs/agents/backlog.md` and skill output. | resolved |
| [0006-decision-triage-activation.md](0006-decision-triage-activation.md) | Decide triage role, status workflow, and activation model. | resolved |
| [0014-decision-skill-inventory-remediation.md](0014-decision-skill-inventory-remediation.md) | Close every open discrepancy from spike 0003 (v2.4 register + v2.1 follow-ons). | resolved |

## Tasks

| Task | Overview | Status |
|------|----------|--------|
| [0015-task-remediate-skill-inventory-findings.md](0015-task-remediate-skill-inventory-findings.md) | Apply decision 0014 across skills, docs, and backlog canon. | resolved |
| [0016-task-epic-duck-ambiguous-ticket-triage.md](0016-task-epic-duck-ambiguous-ticket-triage.md) | Document epic-duck triage flows; drop triage-duck promises from canon. | resolved |

## Spikes

| Spike | Overview | Status |
|-------|----------|--------|
| [0003-spike-skill-inventory.md](0003-spike-skill-inventory.md) | Map in-scope skills, dependencies, and artefacts they touch. | resolved |
| [0011-spike-common-fields-and-skill-needs.md](0011-spike-common-fields-and-skill-needs.md) | Recommend common ticket fields vs per-type exceptions from skill needs and upstream references. | resolved |
