from src.retrieval.retriever import retrieve
from src.retrieval.bm25 import BM25Retriever
from src.vectorstore.faiss_store import FAISSVectorStore


def _reciprocal_rank_fusion(
    dense_documents: list,
    sparse_documents: list,
    k: int = 60,
):
    """
    Fuse dense and BM25 rankings using Reciprocal Rank Fusion.
    """

    scores = {}

    # ----------------------------------------
    # Dense Retrieval
    # ----------------------------------------

    for rank, document in enumerate(
        dense_documents,
        start=1,
    ):
        chunk_id = document.metadata["chunk_id"]

        scores.setdefault(
            chunk_id,
            {
                "document": document,
                "score": 0.0,
            },
        )

        scores[chunk_id]["score"] += 1 / (k + rank)

    # ----------------------------------------
    # BM25 Retrieval
    # ----------------------------------------

    for rank, document in enumerate(
        sparse_documents,
        start=1,
    ):
        chunk_id = document.metadata["chunk_id"]

        scores.setdefault(
            chunk_id,
            {
                "document": document,
                "score": 0.0,
            },
        )

        scores[chunk_id]["score"] += 1 / (k + rank)

    ranked_documents = sorted(
        scores.values(),
        key=lambda item: item["score"],
        reverse=True,
    )

    return [
        item["document"]
        for item in ranked_documents
    ]


def retrieve_hybrid(
    query: str,
    vector_store: FAISSVectorStore,
    bm25: BM25Retriever,
    k: int = 5,
):
    """
    Hybrid retrieval using Dense Search + BM25 + Reciprocal Rank Fusion.
    """

    dense_documents = retrieve(
        query=query,
        vector_store=vector_store,
        k=k,
    )

    sparse_result = bm25.retrieve(
        query=query,
        k=k,
    )

    fused_documents = _reciprocal_rank_fusion(
        dense_documents=dense_documents,
        sparse_documents=sparse_result["retrieved_documents"],
    )

    return fused_documents[:k]