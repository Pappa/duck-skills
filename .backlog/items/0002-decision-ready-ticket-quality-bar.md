Type: epic-duck:decision
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Define the quality bar for `ready` tickets and eval pass/fail.
Blocked by:

## Question

What is the canonical quality bar for backlog tickets this toolkit must produce (decisions vs `ready` deliverables), and how do evals decide pass vs fail besides ad-hoc judgment?

Resolution must cover: relationship to **amigo-duck** axes; minimum fields per ticket type; handling accepted gaps; friction log format for eval runs.

## Answer

### Ticket families and exceptions

- **Planning family** — `Type: epic-duck:plan`, `epic-duck:decision`, `epic-duck:task`, `epic-duck:spike` (see ADR 0001 and `docs/agents/backlog.md`).
- **Implementation family** — plain **`Type: task`** and **`Type: spike`** from **rubber-duck** (development work; filenames `NNNN-task-<slug>.md`, `NNNN-spike-<slug>.md`).
- **Spike findings** — `.backlog/spike/*` with `Spike:` backlink and **TLDR** only (no `Type:`).
- Field canon: [0005-decision-ticket-shapes-and-fields.md](0005-decision-ticket-shapes-and-fields.md), decision **[0014](0014-decision-skill-inventory-remediation.md)**.

### Quality gate (tickets)

- **`Status: ready` deliverables** (`Type: epic-duck:task` or **`Type: task`**): Must reach **amigo-duck Verdict: Approve** on all four axes (fit, complete/unambiguous, ISO plain language, full INVEST) before publish.
- **Non-ready tasks and spike items:** **amigo-duck** on fit + complete/unambiguous + plain language; INVEST per amigo-duck (light for decision-shaped and spike-item work).
- **`Type: epic-duck:decision`:** Same amigo-duck path as other decisions, **plus** the **Decision resolution** metric below on eval runs (when evals are in scope).
- **Meta-quality:** Ship evals that validate **amigo-duck** behavior (golden set) and **skill usage** (agents follow invoked skills and docs) before treating amigo-duck as a hard gate in automation (eval harness work descoped from plan **0001**; details TBD if reprioritised).

### Accepted gaps (v1 and future)

- **v1:** No **accepted gaps** workflow in tickets. Anything short of **Approve** lowers the **Ticket quality** subscore; operator context goes under **Usability** in the run record.
- **Future (plan backlog):** Allow an operator to tolerate specific quality findings for a run, with a **score penalty** instead of blocking publish. Working term **Accepted gaps** (rename TBD): *quality findings from amigo-duck or the eval metrics that the operator explicitly tolerates for that run instead of requiring a fix before publish.*

### Eval model: score, then threshold

- Eval runs **score**; they do not emit a single boolean pass/fail unless a **threshold** is applied for a given **skill** or scenario.
- **Subscores (0–5 each):**
  1. **Ticket quality** — derived from **amigo-duck** (Approve ≈ 5; Revise maps down by severity of findings).
  2. **Decision resolution** — only for `Type: epic-duck:decision`; see metric below. Omit or mark N/A for other types.
  3. **Skill usage** — agent followed the invoked skill(s) and relevant repo docs (setup, backlog, ticket-statuses, SKILL.md).
  4. **Usability** — operator burden: extra turns, confusion, manual edits, tooling friction (higher = worse unless inverted in harness docs).
- **Total:** weighted sum (weights TBD when harness work is reprioritised).
- **Pass/fail:** per-skill (or per-scenario) **threshold on total**; optional **floor** on Ticket quality (e.g. must be ≥ 3).

### Decision resolution metric

Measures whether a decision ticket fulfilled its **decision** job (not a duplicate full amigo-duck review). Score **0–5** = count of criteria met (1 point each):

| Criterion | Pass (1) |
|-----------|----------|
| **Single decision** | One clear `## Question`; not multiple unrelated decisions. |
| **Resolvable scope** | Completable in one child session; not disguised implementation or an epic. |
| **Testable done** | Before resolve: clear what `## Answer` must contain; after resolve: Answer settles the question. |
| **Assumptions surfaced** | Material assumptions are in the ticket or linked, not only in chat. |
| **Plan integration** | Correct `Plan:` link; honest blockers; resolution fits **Decisions so far** or explicit out-of-scope. |

### Run artefacts

Each eval run produces:

- A run log markdown file under `evals/runs/` (exact naming TBD).
- An artefact directory: `evals/runs/artefacts/<scenario>-<date>/` containing at least: **`score`** (subscores + total), **`model_id`**, saved **amigo-duck** verdict output (file + link from run log), tickets produced (paths), **Usability** notes, and operator notes.

### Follow-on work

- Spike **0011** — common fields and skill needs (blocked by **0003**).
- **0005** — field canon, backlog.md alignment, ADR (blocked by **0011**).

## Comments

Field canon (headers, `Type: epic-duck:*`, **`Status: ready`** gate wording): [0005](0005-decision-ticket-shapes-and-fields.md), `docs/adr/0001-backlog-ticket-shapes.md`.
