import sys
from pathlib import Path

import pytest
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case.llm_test_case import ToolCall, ToolCallType
from deepeval.tracing import observe, update_current_span, update_current_trace

_EVAL_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_EVAL_DIR))

from duck_skills.skill_advisor import (  # noqa: E402
    generate_recommendation,
    retrieve_skill_chunks,
    search_skills,
)

from metrics import (  # noqa: E402
    AGENT_SPAN_METRICS,
    GENERATOR_SPAN_METRICS,
    RETRIEVER_SPAN_METRICS,
    SEARCH_SKILLS_TOOL_SPAN_METRICS,
    TRACE_METRICS,
)

dataset = EvaluationDataset()
dataset.add_goldens_from_json_file(file_path=str(_EVAL_DIR / ".dataset.json"))


@observe(type="retriever", metrics=RETRIEVER_SPAN_METRICS)
def retrieve(query: str) -> list[str]:
    chunks = retrieve_skill_chunks(query)
    chunk_text = "\n".join(chunks)
    update_current_span(
        input=query,
        output=chunk_text,
        retrieval_context=chunks,
    )
    return chunks


@observe(type="tool", metrics=SEARCH_SKILLS_TOOL_SPAN_METRICS)
def search_skills_tool(query: str) -> str:
    chunks = retrieve(query)
    result = search_skills(query)
    update_current_span(
        input={"query": query},
        output=result,
        retrieval_context=chunks,
    )
    return result


@observe(type="llm", metrics=GENERATOR_SPAN_METRICS)
def generate(query: str, tool_result: str) -> str:
    answer = generate_recommendation(query, tool_result)
    chunks = retrieve_skill_chunks(query)
    update_current_span(
        input=query,
        output=answer,
        retrieval_context=chunks,
    )
    return answer


@observe(type="agent", metrics=AGENT_SPAN_METRICS)
def advise_skill(query: str) -> str:
    tool_result = search_skills_tool(query)
    answer = generate(query, tool_result)
    tool_call = ToolCall(
        name="search_skills",
        type=ToolCallType.FUNCTION,
        input_parameters={"query": query},
        output=tool_result,
    )
    update_current_span(
        input=query,
        output=answer,
        tools_called=[tool_call],
    )
    update_current_trace(input=query, output=answer)
    return answer


@pytest.mark.parametrize("golden", dataset.goldens)
def test_skill_advisor(golden: Golden):
    advise_skill(golden.input)
    assert_test(golden=golden, metrics=TRACE_METRICS)
