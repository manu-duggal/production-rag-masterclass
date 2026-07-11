from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents: list[Document]) -> list[Document]:
    """
    Split documents into smaller chunks while preserving metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ],
    )

    chunks = splitter.split_documents(documents)

    for index, chunk in enumerate(chunks, start=1):
        chunk.metadata["chunk_id"] = index

    return chunks