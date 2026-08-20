from sentence_transformers import CrossEncoder


# Load Model Once


reranker = CrossEncoder(
    "BAAI/bge-reranker-base",
)


def rerank(
    query: str,
    documents: list,
    top_k: int = 5,
):
    """
    Rerank retrieved documents using a CrossEncoder.
    """

    if len(documents) <= top_k:
        return documents


    # Build Query-Document Pairs


    pairs = [
        (
            query,
            document.page_content,
        )
        for document in documents
    ]


    # Compute Relevance Scores


    scores = reranker.predict(
        pairs,
    )


    # Sort Documents

    ranked_documents = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True,
    )

    # Return Top-K


    return [
        document
        for document, _ in ranked_documents[:top_k]
    ]