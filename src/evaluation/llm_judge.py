import json

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from src.config.settings import GROQ_API_KEY


judge_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0,
)


def _build_prompt(
    template: str,
    **kwargs,
):
    """
    Build an LLM prompt.
    """

    prompt = ChatPromptTemplate.from_template(template)

    return prompt.format_messages(**kwargs)


GENERATION_TEMPLATE = """
You are an expert evaluator for Retrieval-Augmented Generation (RAG) systems.

Your task is to evaluate the quality of the generated answer.

Evaluate ONLY the following three metrics.

------------------------------------------------------------
Question
------------------------------------------------------------
{question}

------------------------------------------------------------
Expected Answer
------------------------------------------------------------
{expected_answer}

------------------------------------------------------------
Retrieved Context
------------------------------------------------------------
{retrieved_context}

------------------------------------------------------------
Generated Answer
------------------------------------------------------------
{generated_answer}

============================================================
Evaluation Criteria
============================================================

1. Correctness

Evaluate how accurately the generated answer matches the expected answer.

Score:
0.0 = Completely incorrect
1.0 = Completely correct

------------------------------------------------------------

2. Groundedness

Evaluate whether every factual statement in the generated answer is supported by the retrieved context.

Score:
0.0 = Entirely hallucinated
1.0 = Fully supported

------------------------------------------------------------

3. Answer Relevance

Evaluate whether the generated answer answers the user's question.

Score:
0.0 = Irrelevant
1.0 = Perfectly answers the question

============================================================
Instructions
============================================================

Return ONLY valid JSON.

{{
    "correctness": {{
        "score": float,
        "reason": string
    }},
    "groundedness": {{
        "score": float,
        "reason": string
    }},
    "answer_relevance": {{
        "score": float,
        "reason": string
    }}
}}

Rules:

- Scores must be between 0.00 and 1.00.
- Round every score to two decimal places.
- Do not include markdown.
- Do not include explanations outside the JSON.
- Output valid JSON only.
"""


RETRIEVAL_TEMPLATE = """
You are an expert evaluator for Retrieval-Augmented Generation (RAG) systems.

Your task is to evaluate ONE retrieved chunk.

------------------------------------------------------------
Question
------------------------------------------------------------
{question}

------------------------------------------------------------
Expected Answer
------------------------------------------------------------
{expected_answer}

------------------------------------------------------------
Retrieved Chunk
------------------------------------------------------------
{retrieved_chunk}

============================================================
Evaluation Criteria
============================================================

1. Relevance

Does this chunk contain information that is useful for answering the user's question?

Score:
0.0 = Completely irrelevant
1.0 = Highly relevant

------------------------------------------------------------

2. Answerability

Does this chunk contain sufficient information to answer the user's question?

Score:
0.0 = Cannot answer the question
1.0 = Completely answers the question

============================================================
Instructions
============================================================

Return ONLY valid JSON.

{{
    "relevance": {{
        "score": float,
        "reason": string
    }},
    "answerability": {{
        "score": float,
        "reason": string
    }}
}}

Rules:

- Scores must be between 0.00 and 1.00.
- Round every score to two decimal places.
- Do not include markdown.
- Do not include explanations outside the JSON.
- Output valid JSON only.
"""


def _parse_response(response) -> dict:
    """
    Parse the JSON response returned by the LLM.
    """

    content = response.content.strip()

    if content.startswith("```"):
        content = content.removeprefix("```json")
        content = content.removeprefix("```")
        content = content.removesuffix("```")
        content = content.strip()

    return json.loads(content)


def judge_generation(
    golden_question: dict,
    query_result: dict,
) -> dict:
    """
    Evaluate the generated answer.
    """

    retrieved_context = "\n\n".join(
        document.page_content
        for document in query_result["retrieved_documents"]
    )

    prompt = _build_prompt(
        GENERATION_TEMPLATE,
        question=golden_question["question"],
        expected_answer=golden_question["expected_answer"],
        retrieved_context=retrieved_context,
        generated_answer=query_result["answer"],
    )

    response = judge_llm.invoke(prompt)

    return _parse_response(response)


def judge_retrieval(
    question: str,
    expected_answer: str,
    retrieved_chunk: str,
) -> dict:
    """
    Evaluate a retrieved chunk.
    """

    prompt = _build_prompt(
        RETRIEVAL_TEMPLATE,
        question=question,
        expected_answer=expected_answer,
        retrieved_chunk=retrieved_chunk,
    )

    response = judge_llm.invoke(prompt)

    return _parse_response(response)