import re
from langchain_core.documents import Document


def parse_documents(documents: list[Document]) -> list[Document]:
    """
    Parse and normalize LangChain Document objects.

    Args:
        documents: List of raw documents returned by the loader.

    Returns:
        A new list of cleaned Document objects.
    """

    parsed_documents = []

    for document in documents:
        text = document.page_content

        # Remove leading/trailing whitespace
        text = text.strip()

        # Replace multiple spaces with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Replace multiple blank lines with a single blank line
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        parsed_documents.append(
            Document(
                page_content=text,
                metadata=document.metadata.copy()
            )
        )

    return parsed_documents