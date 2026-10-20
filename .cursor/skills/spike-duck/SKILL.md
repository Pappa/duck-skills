---
name: spike-duck
description: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a time-boxed spike, docs or API facts gathered, reading legwork delegated to a background agent, or when the user invokes spike-duck.
---

Spin up a **background agent** to run the spike, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. For domain-specific spikes, search for authritative sources of domain-knowledge (academic papers, recognised industry bodies, technical books).
3. Write the findings to a single Markdown file, citing each claim's source. Use clear, plain language, following the ISO 24495 standard. Avoid jargon that is not specific to the domain being investigated.
4. Add a short (1-3 paragraph) summary of the findings under the first subheading, **TLDR**.
5. Save findings per repo backlog conventions (see `docs/agents/backlog.md`).

## Local markdown layout

When the repo uses `.backlog/`:

1. Allocate the next shared `NNNN` under `.backlog/items/` (same counter as features and issues).
2. Create or update the spike **item** at `.backlog/items/<NNNN>-spike-<slug>.md` with `Plan:` backlink, `Overview:`, `Question`, and `Result:` pointing to the findings path.
3. Write findings to `.backlog/spike/<NNNN>-<slug>.md`. At the top, link back: `Spike: [<NNNN>-spike-<slug>.md](../items/<NNNN>-spike-<slug>.md)`.
4. Set spike item `Status: resolved` when the result file is complete; update the parent feature plan **Spikes** table and **Decisions so far** when epic-duck or the user expects it.

If the repo has no `.backlog/` convention yet, put the file somewhere sensible and say where.
