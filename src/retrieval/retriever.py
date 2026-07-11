import numpy as np
from langchain_core.documents import Document
from src.embeddings.embedder import generate_query_embedding
from src.vectorstore.faiss_store import FAISSVectorStore


def retrieve(
    query: str,
    vector_store: FAISSVectorStore,
    k: int = 5,
) -> list[Document]:
    """
    Retrieve the top-k most relevant document chunks
    for a user query.
    """

    if vector_store.index is None:
        raise ValueError(
            "Vector store has not been built."
        )

    k = min(k, vector_store.size())

    query_embedding = generate_query_embedding(query)

    query_vector = np.array(
        [query_embedding],
        dtype=np.float32,
    )

    _, indices = vector_store.index.search(
        query_vector,
        k,
    )

    retrieved_documents = []

    for index in indices[0]:
        if index == -1:
            continue

        retrieved_documents.append(
            vector_store.documents[index]
        )

    return retrieved_documents