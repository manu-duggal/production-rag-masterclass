import faiss
import numpy as np
from langchain_core.documents import Document
from pathlib import Path
import pickle

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


    def save(self, save_dir: str | Path) -> None:
        """
        Save the vector store to disk.
        """

        if self.index is None:
            raise ValueError("Vector store has not been built.")

        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(save_dir / "faiss.index"),
        )

        with open(save_dir / "documents.pkl", "wb") as file:
            pickle.dump(self.documents, file)

        
    @classmethod
    def load(cls, save_dir: str | Path) -> "FAISSVectorStore":
        """
        Load a vector store from disk.
        """

        save_dir = Path(save_dir)

        vector_store = cls()

        vector_store.index = faiss.read_index(
            str(save_dir / "faiss.index")
        )

        with open(save_dir / "documents.pkl", "rb") as file:
            vector_store.documents = pickle.load(file)

        return vector_store