# Domain docs

How planning and engineering skills consume domain documentation in this repo.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root, or
- **`GLOSSARY-MAP.md`** when present — follow it to the relevant per-context `GLOSSARY.md` files.
- **`docs/adr/`** — ADRs that touch the area you are changing. In multi-context repos, also check `src/<context>/docs/adr/`.

If a file does not exist, proceed silently. Do not nag the user to create glossaries up front.

## Layout

**Single-context** (default):

```
/
├── GLOSSARY.md
├── docs/adr/
└── src/
```

**Multi-context** (`GLOSSARY-MAP.md` at root):

```
/
├── GLOSSARY-MAP.md
├── docs/adr/
└── src/<context>/GLOSSARY.md
```

## Vocabulary

Use glossary terms in issue titles, specs, and ticket descriptions. Avoid synonyms the glossary rejects.

If a needed concept is missing from the glossary, either reconsider the naming or note the gap for a future **software-design** pass.

## ADR conflicts

If work contradicts an ADR, say so explicitly:

> _Contradicts ADR-0007 (…), but worth reopening because…_
