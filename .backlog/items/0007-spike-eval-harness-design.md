Type: epic-duck:spike
Status: out-of-scope
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Design one eval harness (meta-eval + skill-path layers), sandbox layout, and token budget.
Result: [0007-eval-harness-design.md](../spike/0007-eval-harness-design.md)
Blocked by:

## Question

How should `evals/sandbox_project` and **one** lightweight harness under `evals/` be structured so agents can run planning-skill evals without excessive tokens?

Do **not** split into separate harness spikes: a single design covers two **layers** in one result doc (per [0002-decision-ready-ticket-quality-bar.md](0002-decision-ready-ticket-quality-bar.md)):

1. **Meta-eval layer** — invoke **amigo-duck** on fixtures; compare output to the golden set from [0012-decision-amigo-duck-eval-golden-set.md](0012-decision-amigo-duck-eval-golden-set.md); persist verdicts under `evals/runs/artefacts/<scenario>-<date>/`.
2. **Skill-path layer** — sandbox + setup → epic or rubber (and triage when defined); score **Decision resolution**, **Skill usage** (per [0013-decision-skill-usage-eval-scenarios.md](0013-decision-skill-usage-eval-scenarios.md)), and **Usability**; roll up weighted **Ticket quality** and total score with per-skill thresholds.

Resolution must propose: directory layout; run log + artefact schema (`score`, `model_id`, saved amigo-duck output); 1–2 minimal **integration** scenarios (pipeline smoke, not full case catalogs); copy vs in-repo execution; what stays in **0012** / **0013** vs this spike; and what is out of scope for v1.

## Comments

Recorded decision: no second spike for amigo-duck-only harness; case lists and skill-usage traps remain decisions **0012** / **0013**.

Temporarily **out of scope** on plan **0001** (eval token budget); may be reprioritised later.
