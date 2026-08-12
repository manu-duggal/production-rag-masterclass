import math


def compute_recall_at_k(expected_sources: set[str], retrieved_sources: list[str]) -> float:
    """
    Compute Recall@K.

    Recall@K = Relevant Retrieved / Total Relevant
    """

    if not expected_sources:
        return 0.0

    relevant = len(
        expected_sources.intersection(retrieved_sources)
    )

    return relevant / len(expected_sources)


def compute_precision_at_k(expected_sources: set[str], retrieved_sources: list[str]) -> float:
    """
    Compute Precision@K.

    Precision@K = Relevant Retrieved / Retrieved
    """

    if not retrieved_sources:
        return 0.0

    relevant = len(
        expected_sources.intersection(retrieved_sources)
    )

    return relevant / len(retrieved_sources)


def compute_mrr(expected_sources: set[str], retrieved_sources: list[str]) -> float:
    """
    Compute Mean Reciprocal Rank (per question).

    Returns the reciprocal rank of the first relevant document.
    """

    for rank, source in enumerate(retrieved_sources, start=1):
        if source in expected_sources:
            return 1.0 / rank

    return 0.0


def compute_ndcg(expected_sources: set[str], retrieved_sources: list[str]) -> float:
    """
    Compute Normalized Discounted Cumulative Gain (per question).

    Assumes binary relevance.
    """

    dcg = 0.0

    for rank, source in enumerate(retrieved_sources, start=1):
        relevance = 1 if source in expected_sources else 0
        dcg += relevance / math.log2(rank + 1)

    ideal_hits = min(
        len(expected_sources),
        len(retrieved_sources),
    )

    if ideal_hits == 0:
        return 0.0

    idcg = sum(
        1 / math.log2(rank + 1)
        for rank in range(1, ideal_hits + 1)
    )

    return dcg / idcg


def compute_average_relevance(
    retrieved_chunk_evaluations: list[dict],
) -> float:
    """
    Compute the average relevance score across all retrieved chunks.
    """

    if not retrieved_chunk_evaluations:
        return 0.0

    total_score = sum(
        chunk["evaluation"]["relevance"]["score"]
        for chunk in retrieved_chunk_evaluations
    )

    return round(
        total_score / len(retrieved_chunk_evaluations),
        2,
    )


def compute_average_answerability(
    retrieved_chunk_evaluations: list[dict],
) -> float:
    """
    Compute the average answerability score across all retrieved chunks.
    """

    if not retrieved_chunk_evaluations:
        return 0.0

    total_score = sum(
        chunk["evaluation"]["answerability"]["score"]
        for chunk in retrieved_chunk_evaluations
    )

    return round(
        total_score / len(retrieved_chunk_evaluations),
        2,
    )