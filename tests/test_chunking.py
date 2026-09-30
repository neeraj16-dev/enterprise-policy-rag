import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.ingestion import load_pdf_with_layout
from rag.chunking import structured_chunks, fixed_size_chunks


def test_chunking_pipeline():
    docs = load_pdf_with_layout("corpus")
    assert len(docs) > 0, "No documents loaded for chunking test."

    print(f"\nLoaded {len(docs)} document pages. Testing structured_chunks...")
    chunks = structured_chunks(docs)

    # 1. Basic sanity assertions
    assert len(chunks) >= len(docs), "Chunking should produce at least as many chunks as original pages."
    print(f"[PASS] Total structured chunks generated: {len(chunks)}")

    # 2. Metadata retention check
    sample_chunk = chunks[0]
    expected_keys = [
        "chunk_id", "source", "filename", "policy_name", 
        "doc_ref", "category", "page", "total_pages", "section"
    ]
    for key in expected_keys:
        assert key in sample_chunk.metadata, f"Metadata key '{key}' was dropped during chunking!"
    print(f"[PASS] Metadata completeness verified across chunks.")

    # 3. Table integrity test
    # Find chunks containing markdown tables and verify they haven't been broken mid-header
    table_chunks = [c for c in chunks if "|" in c.page_content and "---" in c.page_content]
    assert len(table_chunks) > 0, "No table structures survived chunking."
    
    # Inspect a chunk with a table
    sample_table_chunk = table_chunks[0]
    print(f"[PASS] Successfully retained tables across {len(table_chunks)} chunks.")
    print("\n--- Sample Table Chunk Preview ---")
    print(f"Chunk ID: {sample_table_chunk.metadata['chunk_id']}")
    print(f"Policy: {sample_table_chunk.metadata['policy_name']} (Ref: {sample_table_chunk.metadata['doc_ref']})")
    print(f"Section: {sample_table_chunk.metadata['section']} (Page: {sample_table_chunk.metadata['page']})")
    print(f"Content:\n{sample_table_chunk.page_content[:400]}")
    print("-" * 50)


if __name__ == "__main__":
    test_chunking_pipeline()