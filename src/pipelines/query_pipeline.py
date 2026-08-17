import time

from src.generation.llm import generate_response
from src.generation.prompt_builder import build_prompt
from src.retrieval.bm25 import BM25Retriever
from src.retrieval.hybrid import retrieve_hybrid
from src.retrieval.retriever import retrieve
from src.vectorstore.faiss_store import FAISSVectorStore


def answer_question(
    query: str,
    vector_store: FAISSVectorStore,
    bm25: BM25Retriever | None = None,
) -> dict:
    """
    Answer a user question using the knowledge base.
    """

    total_start = time.perf_counter()

    # ----------------------------------------
    # Retrieve Relevant Documents
    # ----------------------------------------

    retrieval_start = time.perf_counter()

    if bm25 is None:

        retrieved_documents = retrieve(
            query=query,
            vector_store=vector_store,
        )

    else:

        retrieved_documents = retrieve_hybrid(
            query=query,
            vector_store=vector_store,
            bm25=bm25,
        )

    retrieval_ms = (
        time.perf_counter() - retrieval_start
    ) * 1000

    # ----------------------------------------
    # Build Prompt
    # ----------------------------------------

    prompt = build_prompt(
        query=query,
        documents=retrieved_documents,
    )

    # ----------------------------------------
    # Generate Answer
    # ----------------------------------------

    generation_start = time.perf_counter()

    answer = generate_response(prompt)

    generation_ms = (
        time.perf_counter() - generation_start
    ) * 1000

    total_ms = (
        time.perf_counter() - total_start
    ) * 1000

    # ----------------------------------------
    # Return
    # ----------------------------------------

    return {
        "answer": answer,
        "retrieved_documents": retrieved_documents,
        "performance": {
            "retrieval_ms": round(retrieval_ms, 2),
            "generation_ms": round(generation_ms, 2),
            "total_ms": round(total_ms, 2),
        },
    }