---
name: spike-duck
description: Investigate and research a question against high-trust primary sources and capture the results as a Markdown file. Use when the user wants a time-boxed spike, deep research, docs or API facts gathered, reading legwork delegated to a background agent, or when the user invokes spike-duck.
---

Spin up a **background agent** to run the spike, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. For domain-specific spikes, search for authoritative sources of domain-knowledge (academic papers, recognised industry bodies, technical books).
3. Write the results to a single Markdown file, citing each claim's source. Use clear, plain language, following the ISO 24495 standard. Avoid jargon that is not specific to the domain being investigated.
4. Add a short (1-3 paragraph) summary of the results under the first subheading, **TLDR**.
5. Save the results per repo conventions (see `docs/agents/backlog.md`).
