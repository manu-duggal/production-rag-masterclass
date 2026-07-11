from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for a list of texts.
    """

    return embedding_model.embed_documents(texts)


def generate_query_embedding(query: str) -> list[float]:
    """
    Generate an embedding for a user query.
    """

    return embedding_model.embed_query(query)