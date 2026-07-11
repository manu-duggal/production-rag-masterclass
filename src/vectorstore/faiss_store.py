import faiss
import numpy as np
from langchain_core.documents import Document


class FAISSVectorStore:
    """
    A simple FAISS-backed vector store that keeps
    embeddings and their corresponding documents together.
    """

    def __init__(self):
        self.index = None
        self.documents: list[Document] = []

    def build(
        self,
        embeddings: list[list[float]],
        documents: list[Document]
    ) -> None:
        """
        Build the FAISS index.
        """

        vectors = np.array(embeddings, dtype=np.float32)

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(vectors)

        self.documents = documents

    def size(self) -> int:
        """
        Return the number of indexed vectors.
        """

        return self.index.ntotal