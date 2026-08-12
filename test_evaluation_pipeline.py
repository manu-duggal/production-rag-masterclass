import json
from src.pipelines.evaluation_pipeline import run_evaluation
from src.vectorstore.faiss_store import FAISSVectorStore


# ----------------------------------------
# Load Vector Store
# ----------------------------------------

vector_store = FAISSVectorStore.load(
    "data/vectorstore"
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
# Smoke Test (First Question Only)
# ----------------------------------------

results = run_evaluation(
    golden_dataset=golden_dataset,
    vector_store=vector_store,
    experiment_name="baseline",
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