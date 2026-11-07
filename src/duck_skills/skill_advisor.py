"""Recommend duck-skills from natural-language queries."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

_SKILLS_DIR = Path(__file__).resolve().parents[2] / "skills"
_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
_NAME = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
_DESCRIPTION = re.compile(
    r"^description:\s*(?:>\-?\s*\n(?:\s+.+\n)+|(.+?))(?:\n[a-zA-Z#]|\Z)",
    re.MULTILINE,
)


@dataclass(frozen=True)
class SkillRecord:
    name: str
    description: str
    corpus: str


def _parse_description(block: str) -> str:
    folded = re.search(
        r"description:\s*>\-\s*\n((?:\s+.+\n?)+)", block, re.MULTILINE
    )
    if folded:
        lines = [
            ln.strip()
            for ln in folded.group(1).splitlines()
            if ln.strip()
        ]
        return " ".join(lines)
    single = re.search(r"^description:\s*(.+)$", block, re.MULTILINE)
    if single:
        return single.group(1).strip().strip("'\"")
    return ""


@lru_cache(maxsize=1)
def load_skills() -> list[SkillRecord]:
    records: list[SkillRecord] = []
    for skill_md in sorted(_SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        match = _FRONTMATTER.match(text)
        if not match:
            continue
        block = match.group(1)
        name_match = _NAME.search(block)
        if not name_match:
            continue
        name = name_match.group(1).strip()
        description = _parse_description(block)
        body = text[match.end() :].strip()
        corpus = f"{name} {description} {body[:500]}".lower()
        records.append(SkillRecord(name=name, description=description, corpus=corpus))
    return records


def _tokenize(query: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", query.lower())
    stop = {
        "a",
        "an",
        "the",
        "for",
        "to",
        "i",
        "my",
        "how",
        "what",
        "which",
        "do",
        "use",
        "need",
        "want",
        "with",
        "when",
        "should",
    }
    return [t for t in tokens if t not in stop and len(t) > 1]


def _score_skill(skill: SkillRecord, tokens: list[str]) -> float:
    score = 0.0
    for token in tokens:
        if token == skill.name or token in skill.name:
            score += 4.0
        if token in skill.corpus:
            score += 1.0
    return score


def retrieve_skill_chunks(query: str, *, limit: int = 3) -> list[str]:
    tokens = _tokenize(query)
    ranked = sorted(
        load_skills(),
        key=lambda skill: _score_skill(skill, tokens),
        reverse=True,
    )
    chunks: list[str] = []
    for skill in ranked:
        if not tokens or _score_skill(skill, tokens) <= 0:
            continue
        chunks.append(f"{skill.name}: {skill.description}")
        if len(chunks) >= limit:
            break
    if not chunks and ranked:
        top = ranked[0]
        chunks.append(f"{top.name}: {top.description}")
    return chunks


def search_skills(query: str) -> str:
    chunks = retrieve_skill_chunks(query)
    payload = []
    for chunk in chunks:
        name, _, desc = chunk.partition(": ")
        payload.append({"name": name, "description": desc})
    return json.dumps(payload, ensure_ascii=False)


def run_skill_advisor(query: str) -> str:
    """Entry point: one user question in, one skill recommendation out."""
    tool_result = search_skills(query)
    return generate_recommendation(query, tool_result)


def generate_recommendation(query: str, tool_result: str) -> str:
    candidates = json.loads(tool_result)
    if not candidates:
        line = "Recommend: rubber-duck — No matching skill; start with a rubber-duck session"
    else:
        top = candidates[0]
        line = f"Recommend: {top['name']} — {top['description']}"
    if not line.endswith("."):
        line += "."
    return line
