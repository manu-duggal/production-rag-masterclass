from langchain_core.documents import Document


SYSTEM_PROMPT = """
You are an enterprise internal knowledge assistant.

Use ONLY the provided context to answer the user's question.

Rules:
- Do not make up information.
- If the answer is not present in the context, say:
  "I couldn't find that information in the provided documents."
- Cite the document title and page number for every answer.
- If multiple documents contribute to the answer, cite all relevant sources.
""".strip()


def build_prompt(
    query: str,
    documents: list[Document],
) -> str:
    """
    Build a prompt from retrieved documents.
    """

    context_blocks = []

    for i, document in enumerate(documents, start=1):

        metadata = document.metadata

        context = f"""
Context {i}

Document: {metadata.get("title", "Unknown")}
Policy ID: {metadata.get("policy_id", "N/A")}
Department: {metadata.get("department", "N/A")}
Page: {metadata.get("page_label", "Unknown")}

Content:
{document.page_content}
""".strip()

        context_blocks.append(context)

    formatted_context = "\n\n" + ("-" * 80) + "\n\n".join(context_blocks)

    prompt = f"""
{SYSTEM_PROMPT}

======================== CONTEXT ========================

{formatted_context}

=========================================================

Question:
{query}

Answer:
""".strip()

    return prompt