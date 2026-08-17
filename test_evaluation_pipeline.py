import json

from src.pipelines.evaluation_pipeline import run_evaluation
from src.retrieval.bm25 import BM25Retriever
from src.vectorstore.faiss_store import FAISSVectorStore


# ----------------------------------------
# Load Retrieval Indexes
# ----------------------------------------

vector_store = FAISSVectorStore.load(
    "data/vectorstore"
)

bm25 = BM25Retriever.load(
    "data/bm25"
)

# ----------------------------------------
# Load Golden Dataset
# ----------------------------------------

with open(
    "data/evaluation/golden_dataset.json",
    "r",
    encoding="utf-8",
) as file:
    golden_dataset = json.load(file)

# ----------------------------------------
# Run Evaluation
# ----------------------------------------

results = run_evaluation(
    golden_dataset=golden_dataset,
    vector_store=vector_store,
    bm25=bm25,
    experiment_name="hybrid_v1",
)

# ----------------------------------------
# Display Results
# ----------------------------------------

print(
    json.dumps(
        results,
        indent=4,
        default=str,
    )
)