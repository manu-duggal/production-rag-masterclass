import pickle
import time
from pathlib import Path

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi


class BM25Retriever:
    """
    BM25 document retriever.
    """

    def __init__(self):
        self.bm25 = None
        self.documents = []
        self.tokenized_corpus = []

    def build(
        self,
        documents: list[Document],
    ) -> None:
        """
        Build the BM25 index.
        """

        self.documents = documents

        self.tokenized_corpus = [
            document.page_content.lower().split()
            for document in documents
        ]

        self.bm25 = BM25Okapi(
            self.tokenized_corpus
        )

    def save(
        self,
        directory: str,
    ) -> None:
        """
        Save the BM25 index.
        """

        directory = Path(directory)
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            directory / "bm25.pkl",
            "wb",
        ) as file:
            pickle.dump(
                {
                    "bm25": self.bm25,
                    "documents": self.documents,
                    "tokenized_corpus": self.tokenized_corpus,
                },
                file,
            )

    @classmethod
    def load(
        cls,
        directory: str,
    ):
        """
        Load a BM25 index.
        """

        directory = Path(directory)

        with open(
            directory / "bm25.pkl",
            "rb",
        ) as file:
            data = pickle.load(file)

        retriever = cls()

        retriever.bm25 = data["bm25"]
        retriever.documents = data["documents"]
        retriever.tokenized_corpus = data["tokenized_corpus"]

        return retriever

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> dict:
        """
        Retrieve the top-k BM25 documents.
        """

        if self.bm25 is None:
            raise ValueError(
                "BM25 index has not been built."
            )

        start = time.perf_counter()

        tokenized_query = (
            query.lower().split()
        )

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True,
        )[:k]

        retrieval_ms = (
            time.perf_counter() - start
        ) * 1000

        retrieved_documents = [
            self.documents[index]
            for index in ranked_indices
        ]

        return {
            "retrieved_documents": retrieved_documents,
            "performance": {
                "retrieval_ms": round(
                    retrieval_ms,
                    2,
                )
            },
        }

    def size(self) -> int:
        """
        Number of indexed documents.
        """

        return len(
            self.documents
        )