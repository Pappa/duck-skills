Type: epic-duck:decision
Status: ready
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Decide how to close every open skill/doc discrepancy from spike 0003 (v2.4).
Blocked by:

## Question

For each open finding from skill inventory spike **0003** ([v2.4 synthesis](../spike/0003-skill-inventory-v2.4.md); detail in [v2.1](../spike/0003-skill-inventory-v2.1.md)–[v2.3](../spike/0003-skill-inventory-v2.3.md)), what is the **disposition** (fix now, defer with owner, or explicitly accept as-is) and **what changes** (file paths, wording rules)?

Resolution must produce a single **`## Answer`** that addresses **every row** below. For each row: **disposition**, **owner artefact** (skill, doc, backlog item, or none), and **acceptance** (how we know it is done). Do **not** re-litigate ADR 0001 shapes or re-open **0004** choreography intent — only align skills and docs to **0004** and current canon.

### Register (v2.4 — required)

| ID | Severity | Topic |
|----|----------|-------|
| C-0004-rubber | High | Rubber backlog children + **amigo-duck** before publish per **0004** vs `rubber-duck/SKILL.md` (domain-only today) |
| C-0004-epic-arch | High | Epic invokes **architect-duck** / may delegate **rubber-duck** per **0004** vs `epic-duck/SKILL.md` invoke list |
| C-readme-rubber | Medium | `README.md` planning flow implies rubber → tickets vs rubber skill |
| C-0002-stale | Medium | **0002** Answer still uses `Label: ready`, bare `Type: decision` |
| C-0011-stale | Medium | Spike **0011** still proposes `Label: ready` (superseded by **0005**/ADR) |
| C-epic-labelled | Low | Epic “labelled `epic-duck:plan`” vs local **`Type:`** |
| C-github-frontier | Low | `setup-duck-skills/backlog-github.md` frontier omits **`needs-triage`** |
| C-spike-NNNN | Low | **spike-duck** may allocate `NNNN` when epic-duck already created spike item |
| C-frontier-term | Low | “Frontier” homonym: **question-duck** vs epic/backlog |
| C-plan-notes | Low | Plan **0001** Notes: epic uses **architect-duck**; epic `SKILL.md` omits |

### Additional findings (v2.1 — required)

| ID | Severity | Topic |
|----|----------|-------|
| R4 | Low | README lists **question-duck** / **architect-duck** as model-invoked vs **0004** v1 entry-point rule |
| R6 | Low | Spike resolve bookkeeping: `backlog.md` vs `epic-duck/SKILL.md` work-through |
| R7 | Low | Optional **`## Comments`** on child templates in epic-duck vs `backlog.md` / ADR |
| R8 | Low | **setup-duck-skills** consumer list omits **triage-duck** (planned) |

### Cosmetic / hygiene (v2.3 — required)

| ID | Topic |
|----|-------|
| L3 | **spike-duck** typo “authritative” in `SKILL.md` |

### Explicitly out of this decision’s scope

- **triage-duck** behaviour and activation — decision **0006** and task **0010**
- **Eval harness** findings and **0013** — out of scope on plan **0001**
- **v1 C1–C2** — already resolved (ADR 0001); no action unless Answer records “verified closed”
- **R9** / v2.4 “resolved since v1” rows — confirm closed only; no new design

### Cross-cutting rules the Answer must state

1. Whether remediation is **one deliverable task** or **multiple tasks** after this decision (and if tasks are created, their slugs or numbers).
2. Whether **resolved** backlog items (**0002**, spike **0011**) get **Answer amendments**, **Comments** pointers to **0005**/ADR, or **wontfix** on historical prose.
3. Order of operations when **0004** skill edits touch the same files as low-severity wording fixes.

## Comments

## amigo-duck review

**Verdict: Approve**

| Axis | Result |
|------|--------|
| Fit | Matches user intent: one decision to disposition all spike 0003 open findings. |
| Complete | Enumerates v2.4 register, v2.1 extras, cosmetic L3; boundaries to 0006/0010 and eval out-of-scope are explicit. |
| Plain language | Tables scan by ID; resolution outputs are defined (disposition, artefact, acceptance). |
| INVEST | Decision-sized; testable Answer checklist per row. |

**Assumption:** “Resolve” means agreed disposition and change spec — implementation may land in follow-on **epic-duck:task** items created in the same Answer.
