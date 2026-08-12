from src.pipelines.query_pipeline import answer_question
from src.vectorstore.faiss_store import FAISSVectorStore
from src.retrieval.retriever import retrieve
from src.generation.prompt_builder import build_prompt
from src.generation.llm import generate_response

store = FAISSVectorStore.load("data/vectorstore")
# query = "How many PTO days do new employees receive?"
# answer = answer_question(
#     query="How many PTO days do new employees receive?",
#     vector_store=store,
# )

# print(answer)
# import time

# start = time.perf_counter()

# documents = retrieve(query, store)

# print(f"Retrieval: {time.perf_counter() - start:.3f}s")

# start = time.perf_counter()

# prompt = build_prompt(query, documents)

# print(f"Prompt: {time.perf_counter() - start:.3f}s")

# start = time.perf_counter()

# answer = generate_response(prompt)

# print(f"LLM: {time.perf_counter() - start:.3f}s")



while True:

    query = input("\nQuestion: ")

    if query.lower() == "exit":
        break

    answer = answer_question(
        query=query,
        vector_store=store,
    )

    print(answer["answer"])