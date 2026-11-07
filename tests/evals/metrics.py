from deepeval.metrics import ExactMatchMetric, PatternMatchMetric

RECOMMEND_FORMAT_PATTERN = r"Recommend: [a-z0-9-]+ — .+"
KNOWN_SKILL_PATTERN = (
    r"^Recommend: (setup-duck-skills|epic-duck|rubber-duck|dev-duck|"
    r"test-duck|review-duck|question-duck|architect-duck|amigo-duck|spike-duck) — .+\.$"
)
TOOL_JSON_PATTERN = (
    r'^\[\{"name": "[a-z0-9-]+", "description": .+\}'
    r'(, \{"name": "[a-z0-9-]+", "description": .+\})*\]$'
)

TRACE_METRICS = [
    ExactMatchMetric(threshold=1),
    PatternMatchMetric(pattern=RECOMMEND_FORMAT_PATTERN, threshold=1),
    PatternMatchMetric(
        pattern=r"Recommend: [a-z0-9-]+ — .+\.$",
        threshold=1,
    ),
]

AGENT_SPAN_METRICS = [
    PatternMatchMetric(pattern=KNOWN_SKILL_PATTERN, threshold=1),
    PatternMatchMetric(
        pattern=r"^Recommend: [a-z0-9-]+ — .+\.$",
        threshold=1,
    ),
]

SEARCH_SKILLS_TOOL_SPAN_METRICS = [
    PatternMatchMetric(pattern=TOOL_JSON_PATTERN, threshold=1),
    PatternMatchMetric(pattern=r"^\[.*\]$", threshold=1),
]

GENERATOR_SPAN_METRICS = [
    PatternMatchMetric(pattern=RECOMMEND_FORMAT_PATTERN, threshold=1),
    PatternMatchMetric(pattern=r"^Recommend: [a-z0-9-]+ — .{20,}\.$", threshold=1),
]

RETRIEVER_CHUNK_PATTERN = (
    r"^[a-z0-9-]+(-[a-z0-9-]+)*: .+(\n[a-z0-9-]+(-[a-z0-9-]+)*: .+)*$"
)

RETRIEVER_SPAN_METRICS = [
    PatternMatchMetric(pattern=RETRIEVER_CHUNK_PATTERN, threshold=1),
]
