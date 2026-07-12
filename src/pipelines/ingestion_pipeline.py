from pathlib import Path
from langchain_core.documents import Document
from src.ingestion.loader import load_pdf
from src.parsing.parser import parse_documents
from src.metadata.enricher import enrich_metadata
from src.chunking.chunker import chunk_documents
from src.embeddings.embedder import generate_embeddings
from src.vectorstore.faiss_store import FAISSVectorStore



def discover_pdfs(root_dir: str | Path) -> list[Path]:
    """
    Recursively discover all PDF files under the given directory.

    Args:
        root_dir: Root directory of the knowledge base.

    Returns:
        A sorted list of PDF file paths.
    """

    root_dir = Path(root_dir)

    if not root_dir.exists():
        raise FileNotFoundError(
            f"Directory not found: {root_dir}"
        )

    pdf_files = sorted(root_dir.rglob("*.pdf"))

    return pdf_files



def process_pdf(pdf_path: str | Path) -> list[Document]:
    """
    Process a single PDF through the ingestion pipeline.

    Args:
        pdf_path: Path to the PDF document.

    Returns:
        A list of chunked LangChain Document objects with enriched metadata.
    """

    pdf_path = Path(pdf_path)

    # Load the PDF
    documents = load_pdf(str(pdf_path))

    # Parse document content
    documents = parse_documents(documents)

    # Enrich document metadata
    documents = enrich_metadata(documents)

    # Split into chunks
    chunks = chunk_documents(documents)

    return chunks



def build_knowledge_base(data_dir: str | Path,) -> FAISSVectorStore:
    """
    Build a searchable knowledge base from all PDFs
    under the given directory.
    """

    all_chunks = []

    pdf_files = discover_pdfs(data_dir)

    for pdf_path in pdf_files:
        chunks = process_pdf(pdf_path)
        all_chunks.extend(chunks)

    texts = [
        chunk.page_content
        for chunk in all_chunks
    ]

    embeddings = generate_embeddings(texts)

    vector_store = FAISSVectorStore()

    vector_store.build(
        embeddings=embeddings,
        documents=all_chunks,
    )

    return vector_store