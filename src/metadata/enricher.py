import re
from langchain_core.documents import Document


def extract_policy_id(text: str) -> str | None:
    """Extract the policy ID from the first page."""

    match = re.search(r"Policy ID:\s*([A-Z0-9-]+)", text)

    if match:
        return match.group(1)

    return None


def extract_department(policy_id: str | None) -> str | None:
    """Determine the department from the policy ID."""

    if policy_id is None:
        return "General"

    if "-HR-" in policy_id:
        return "HR"

    if "-IT-" in policy_id:
        return "IT"

    if "-FIN-" in policy_id:
        return "Finance"

    return "General"


def extract_title(text: str) -> str | None:
    """Extract the document title from the first page."""

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if len(lines) >= 2:
        return lines[1]

    return None


def enrich_metadata(document_pages: list[Document]) -> list[Document]:
    """
    Enrich metadata for a single PDF.

    Args:
        document_pages: List of LangChain Documents representing
                        the pages of one PDF.

    Returns:
        A new list of enriched Document objects.
    """

    if not document_pages:
        return []

    # Extract document-level metadata once
    first_page = document_pages[0]

    policy_id = extract_policy_id(first_page.page_content)
    department = extract_department(policy_id)
    title = extract_title(first_page.page_content)

    enriched_documents = []

    for page in document_pages:
        metadata = page.metadata.copy()

        metadata["policy_id"] = policy_id
        metadata["department"] = department
        metadata["title"] = title

        enriched_documents.append(
            Document(
                page_content=page.page_content,
                metadata=metadata,
            )
        )

    return enriched_documents