from pathlib import Path

from src.evaluation.llm_judge import (
    judge_generation,
    judge_retrieval,
)
from src.evaluation.metrics import (
    compute_mrr,
    compute_ndcg,
    compute_precision_at_k,
    compute_recall_at_k,
    compute_average_relevance,
    compute_average_answerability,
)


def evaluate_question(
    golden_question: dict,
    query_result: dict,
) -> dict:
    """
    Evaluate a single question against the golden dataset.
    """

    # ----------------------------------------
    # Ground Truth
    # ----------------------------------------

    expected_sources = {
        golden_question["expected_source"]
    }

    retrieved_documents = query_result["retrieved_documents"]

    # ----------------------------------------
    # Retrieved Sources
    # ----------------------------------------

    retrieved_sources = list(
        dict.fromkeys(
            Path(document.metadata["source"]).stem
            for document in retrieved_documents
        )
    )

    # ----------------------------------------
    # Document-Level Retrieval Metrics
    # ----------------------------------------

    document_level_metrics = {
        "recall_at_k": compute_recall_at_k(
            expected_sources,
            retrieved_sources,
        ),
        "precision_at_k": compute_precision_at_k(
            expected_sources,
            retrieved_sources,
        ),
        "mrr": compute_mrr(
            expected_sources,
            retrieved_sources,
        ),
        "ndcg": compute_ndcg(
            expected_sources,
            retrieved_sources,
        ),
    }

    # ----------------------------------------
    # Chunk-Level Retrieval Evaluation
    # ----------------------------------------

    retrieved_chunk_evaluations = []

    for rank, document in enumerate(
        retrieved_documents,
        start=1,
    ):

        evaluation = judge_retrieval(
            question=golden_question["question"],
            expected_answer=golden_question["expected_answer"],
            retrieved_chunk=document.page_content,
        )

        retrieved_chunk_evaluations.append(
            {
                "rank": rank,
                "source": Path(document.metadata["source"]).stem,
                "chunk_id": document.metadata["chunk_id"],
                "page": document.metadata["page_label"],
                "page_content": document.page_content,
                "evaluation": evaluation,
            }
        )

    evidence_level_metrics = {
        "average_relevance": compute_average_relevance(
            retrieved_chunk_evaluations
        ),
        "average_answerability": compute_average_answerability(
            retrieved_chunk_evaluations
        ),
    }

    retrieval_metrics = {
        "document_level": document_level_metrics,
        "evidence_level": evidence_level_metrics,
    }

    # ----------------------------------------
    # Generation Evaluation
    # ----------------------------------------

    generation_metrics = judge_generation(
        golden_question=golden_question,
        query_result=query_result,
    )

    # ----------------------------------------
    # Return Evaluation Result
    # ----------------------------------------

    return {
    "question_id": golden_question["id"],
    "question": golden_question["question"],
    "expected_source": golden_question["expected_source"],
    "answer": query_result["answer"],
    "retrieved_documents": [
        {
            "page_content": document.page_content,
            "metadata": document.metadata,
        }
        for document in retrieved_documents
    ],
    "retrieved_chunk_evaluations": retrieved_chunk_evaluations,
    "retrieval": retrieval_metrics,
    "generation": generation_metrics,
    "performance": query_result["performance"],
}