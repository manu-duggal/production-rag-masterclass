import time

from src.evaluation.evaluator import evaluate_question
from src.evaluation.report_writer import save_report
from src.pipelines.query_pipeline import answer_question
from src.retrieval.bm25 import BM25Retriever
from src.vectorstore.faiss_store import FAISSVectorStore


def _compute_summary_metrics(
    results: list[dict],
) -> dict:
    """
    Compute aggregate evaluation metrics.
    """

    num_questions = len(results)

    if num_questions == 0:
        return {}

    summary = {
        "retrieval": {
            "document_level": {
                "recall_at_k": 0.0,
                "precision_at_k": 0.0,
                "mrr": 0.0,
                "ndcg": 0.0,
            },
            "evidence_level": {
                "average_relevance": 0.0,
                "average_answerability": 0.0,
            },
        },
        "generation": {
            "correctness": 0.0,
            "groundedness": 0.0,
            "answer_relevance": 0.0,
        },
        "performance": {
            "retrieval_ms": 0.0,
            "generation_ms": 0.0,
            "total_ms": 0.0,
        },
    }

    for result in results:

        # ----------------------------------------
        # Document-Level Retrieval
        # ----------------------------------------

        summary["retrieval"]["document_level"]["recall_at_k"] += (
            result["retrieval"]["document_level"]["recall_at_k"]
        )

        summary["retrieval"]["document_level"]["precision_at_k"] += (
            result["retrieval"]["document_level"]["precision_at_k"]
        )

        summary["retrieval"]["document_level"]["mrr"] += (
            result["retrieval"]["document_level"]["mrr"]
        )

        summary["retrieval"]["document_level"]["ndcg"] += (
            result["retrieval"]["document_level"]["ndcg"]
        )

        # ----------------------------------------
        # Evidence-Level Retrieval
        # ----------------------------------------

        summary["retrieval"]["evidence_level"]["average_relevance"] += (
            result["retrieval"]["evidence_level"]["average_relevance"]
        )

        summary["retrieval"]["evidence_level"]["average_answerability"] += (
            result["retrieval"]["evidence_level"]["average_answerability"]
        )

        # ----------------------------------------
        # Generation
        # ----------------------------------------

        summary["generation"]["correctness"] += (
            result["generation"]["correctness"]["score"]
        )

        summary["generation"]["groundedness"] += (
            result["generation"]["groundedness"]["score"]
        )

        summary["generation"]["answer_relevance"] += (
            result["generation"]["answer_relevance"]["score"]
        )

        # ----------------------------------------
        # Performance
        # ----------------------------------------

        summary["performance"]["retrieval_ms"] += (
            result["performance"]["retrieval_ms"]
        )

        summary["performance"]["generation_ms"] += (
            result["performance"]["generation_ms"]
        )

        summary["performance"]["total_ms"] += (
            result["performance"]["total_ms"]
        )

    # ----------------------------------------
    # Average Document-Level Retrieval Metrics
    # ----------------------------------------

    for metric in summary["retrieval"]["document_level"]:
        summary["retrieval"]["document_level"][metric] = round(
            summary["retrieval"]["document_level"][metric] / num_questions,
            2,
        )

    # ----------------------------------------
    # Average Evidence-Level Retrieval Metrics
    # ----------------------------------------

    for metric in summary["retrieval"]["evidence_level"]:
        summary["retrieval"]["evidence_level"][metric] = round(
            summary["retrieval"]["evidence_level"][metric] / num_questions,
            2,
        )

    # ----------------------------------------
    # Average Generation Metrics
    # ----------------------------------------

    for metric in summary["generation"]:
        summary["generation"][metric] = round(
            summary["generation"][metric] / num_questions,
            2,
        )

    # ----------------------------------------
    # Average Performance Metrics
    # ----------------------------------------

    for metric in summary["performance"]:
        summary["performance"][metric] = round(
            summary["performance"][metric] / num_questions,
            2,
        )

    return summary


def run_evaluation(
    golden_dataset: list[dict],
    vector_store: FAISSVectorStore,
    experiment_name: str,
    bm25: BM25Retriever | None = None,
) -> dict:
    """
    Evaluate the entire golden dataset.
    """

    results = []

    for index, golden_question in enumerate(
        golden_dataset,
        start=1,
    ):

        print(
            f"Evaluating question {index}/{len(golden_dataset)}..."
        )

        query_result = answer_question(
            query=golden_question["question"],
            vector_store=vector_store,
            bm25=bm25,
        )

        evaluation_result = evaluate_question(
            golden_question=golden_question,
            query_result=query_result,
        )

        results.append(evaluation_result)

        # ----------------------------------------
        # Prevent hitting Groq free-tier rate limits
        # ----------------------------------------

        if index != len(golden_dataset):
            time.sleep(30)

    summary_metrics = _compute_summary_metrics(
        results
    )

    report = {
        "summary_metrics": summary_metrics,
        "results": results,
    }

    save_report(
        report=report,
        experiment_name=experiment_name,
    )

    return report