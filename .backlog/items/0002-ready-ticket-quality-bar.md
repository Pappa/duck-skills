Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Define the quality bar for `ready` tickets and eval pass/fail.
Type: planning
Blocked by:

## Question

What is the canonical quality bar for backlog tickets this toolkit must produce (decision issues vs `ready` deliverables), and how do evals decide pass vs fail besides ad-hoc judgment?

Resolution must cover: relationship to **amigo-pato** axes; minimum fields per ticket type; handling accepted gaps; friction log format for eval runs.

## Answer

### Ticket families and exceptions

- **One family** of ticket shapes and properties across epic-duck **issues**, **spike items**, **spike findings**, and **`Label: ready` deliverables**, so skills compose without ad-hoc templates.
- **`Type: planning`** is the primary **exception**: different body structure and different eval assessment than other issue types. **Other types may also be exceptions** once common-fields analysis (spike [0011-spike-common-fields-and-skill-needs.md](0011-spike-common-fields-and-skill-needs.md)) and [0005-ticket-shapes-and-fields.md](0005-ticket-shapes-and-fields.md) complete.
- Exact **common fields** vs per-type fields are **not decided here**; spike **0011** recommends, then **0005** + an ADR record the canon.

### Quality gate (tickets)

- **`Label: ready` deliverables:** Must reach **amigo-pato Verdict: Approve** on all four axes (fit, complete/unambiguous, ISO plain language, full INVEST) before publish.
- **Non-ready issues (task, spike items, etc.):** **amigo-pato** on fit + complete/unambiguous + plain language; INVEST applied per amigo-pato (light for decision-shaped work).
- **`Type: planning`:** Same amigo-pato path as other decision issues, **plus** the **Planning resolution** metric below on eval runs.
- **Meta-quality:** Ship evals that validate **amigo-pato** behavior (golden set) and **skill usage** (agents follow invoked skills and docs) before treating amigo-pato as a hard gate in automation — see issues [0012-amigo-pato-eval-golden-set.md](0012-amigo-pato-eval-golden-set.md) and [0013-skill-usage-eval-scenarios.md](0013-skill-usage-eval-scenarios.md).

### Accepted gaps (v1 and future)

- **v1:** No **accepted gaps** workflow in tickets. Anything short of **Approve** lowers the **Ticket quality** subscore; operator context goes under **Usability** in the run record.
- **Future (plan backlog):** Allow an operator to tolerate specific quality findings for a run, with a **score penalty** instead of blocking publish. Working term **Accepted gaps** (rename TBD): *quality findings from amigo-pato or the eval metrics that the operator explicitly tolerates for that run instead of requiring a fix before publish.*

### Eval model: score, then threshold

- Eval runs **score**; they do not emit a single boolean pass/fail unless a **threshold** is applied for a given **skill** or scenario.
- **Subscores (0–5 each):**
  1. **Ticket quality** — derived from **amigo-pato** (Approve ≈ 5; Revise maps down by severity of findings).
  2. **Planning resolution** — only for `Type: planning`; see metric below. Omit or mark N/A for other types.
  3. **Skill usage** — agent followed the invoked skill(s) and relevant repo docs (setup, backlog, ticket-labels, SKILL.md).
  4. **Usability** — operator burden: extra turns, confusion, manual edits, tooling friction (higher = worse unless inverted in harness docs).
- **Total:** weighted sum (weights defined in harness spike [0007-spike-eval-harness-design.md](0007-spike-eval-harness-design.md)).
- **Pass/fail:** per-skill (or per-scenario) **threshold on total**; optional **floor** on Ticket quality (e.g. must be ≥ 3).

### Planning resolution metric

Measures whether a planning ticket fulfilled its **decision** job (not a duplicate full amigo-pato review). Score **0–5** = count of criteria met (1 point each):

| Criterion | Pass (1) |
|-----------|----------|
| **Single decision** | One clear `## Question`; not multiple unrelated decisions. |
| **Resolvable scope** | Completable in one child session; not disguised implementation or an epic. |
| **Testable done** | Before resolve: clear what `## Answer` must contain; after resolve: Answer settles the question. |
| **Assumptions surfaced** | Material assumptions are in the ticket or linked, not only in chat. |
| **Plan integration** | Correct `Plan:` link; honest blockers; resolution fits **Decisions so far** or explicit out-of-scope. |

### Run artefacts

Each eval run produces:

- A run log markdown file under `evals/runs/` (exact naming in **0007**).
- An artefact directory: `evals/runs/artefacts/<scenario>-<date>/` containing at least: **`score`** (subscores + total), **`model_id`**, saved **amigo-pato** verdict output (file + link from run log), tickets produced (paths), **Usability** notes, and operator notes.

### Follow-on work

- Spike **0011** — common fields and skill needs (blocked by **0003**).
- **0005** — field canon, backlog.md alignment, ADR (blocked by **0011**).
- **0012**, **0013** — eval layers for amigo-pato and skill usage.
- Implementation with **0007** / **0009**.

## Comments
