from src.pipelines.query_pipeline import answer_question
from src.retrieval.bm25 import BM25Retriever
from src.vectorstore.faiss_store import FAISSVectorStore

# ----------------------------------------
# Configuration
# ----------------------------------------

USE_HYBRID = True

# ----------------------------------------
# Load Retrieval Indexes
# ----------------------------------------

vector_store = FAISSVectorStore.load(
    "data/vectorstore"
)

bm25 = None

if USE_HYBRID:
    bm25 = BM25Retriever.load(
        "data/bm25"
    )

# ----------------------------------------
# Interactive Query Loop
# ----------------------------------------

while True:

    query = input("\nQuestion: ")

    if query.lower() == "exit":
        break

    result = answer_question(
        query=query,
        vector_store=vector_store,
        bm25=bm25,
    )

    print("\nAnswer\n")
    print(result["answer"])

    print("\nRetrieved Documents\n")

    for rank, document in enumerate(
        result["retrieved_documents"],
        start=1,
    ):
        print(
            f"{rank}. "
            f"{document.metadata['title']} "
            f"(Chunk {document.metadata['chunk_id']})"
        )

    print("\nPerformance\n")
    print(result["performance"])