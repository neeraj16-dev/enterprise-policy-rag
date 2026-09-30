import sys
from pathlib import Path

# Add project root to sys.path so 'rag' package is resolvable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.ingestion import load_pdf_with_layout


def test_pdf_ingestion():
    docs = load_pdf_with_layout(corpus_dir="corpus")

    # 1. Verification of document load
    assert len(docs) > 0, "Ingestion failed: No documents were extracted from corpus/"
    print(f"\n[PASS] Total document pages loaded: {len(docs)}")

    # 2. Schema check on first document
    sample_doc = docs[0]
    required_keys = ["source", "filename", "policy_name", "doc_ref", "category", "page", "total_pages"]
    for key in required_keys:
        assert key in sample_doc.metadata, f"Missing required metadata key: '{key}'"

    # 3. 1-based indexing verification
    assert sample_doc.metadata["page"] >= 1, "Page indexing must start from 1, not 0"
    print(f"[PASS] Metadata schema and 1-based page indexing verified.")

    # 4. Table extraction check across corpus
    table_docs = [doc for doc in docs if "|" in doc.page_content and "---" in doc.page_content]
    assert len(table_docs) > 0, "No markdown tables detected in any extracted documents."
    print(f"[PASS] Markdown tables detected across {len(table_docs)} document pages.")

    # 5. Inspect a page containing a markdown table
    inspect_doc = table_docs[0]
    print("\n--- Sample Document with Extracted Table ---")
    print(f"Policy: {inspect_doc.metadata['policy_name']}")
    print(f"Ref: {inspect_doc.metadata['doc_ref']} | Category: {inspect_doc.metadata['category']}")
    print(f"Page: {inspect_doc.metadata['page']}/{inspect_doc.metadata['total_pages']}")
    print("Content Preview (first 500 chars):\n")
    print(inspect_doc.page_content[:500])
    print("-" * 50)


if __name__ == "__main__":
    test_pdf_ingestion()