from pathlib import Path
import fitz


def load_pdf(file_path: str) -> str:
    """
    Load a PDF file and extract its text content.

    Args:
        file_path: Path to the PDF file.

    Returns:
        The extracted text from all pages.

    Raises:
        FileNotFoundError: If the PDF does not exist.
    """

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")

    pages = []

    with fitz.open(pdf_path) as doc:
        for page in doc:
            pages.append(page.get_text())

    return "\n".join(pages)