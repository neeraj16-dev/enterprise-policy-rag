import sys
import re
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.ingestion import load_pdf_with_layout
from rag.chunking import structured_chunks
from rag.indexing import (
    build_bm25_index, 
    build_dense_index, 
    load_indexes, 
    COLLECTION_NAME
)


def test_indexing_pipeline():
    print("\n--- 1. Ingesting and Chunking Documents ---")
    docs = load_pdf_with_layout("corpus")
    chunks = structured_chunks(docs)
    total_chunks = len(chunks)
    assert total_chunks > 0, "No chunks available to index."

    print("\n--- 2. Building Indices ---")
    build_bm25_index(chunks)
    build_dense_index(chunks, overwrite=True)

    print("\n--- 3. Verifying Indices Load & Counts ---")
    indices = load_indexes()
    assert indices["bm25"] is not None, "Failed to load BM25 index."
    assert len(indices["chunks"]) == total_chunks, "BM25 chunk payload count mismatch."
    
    collection = indices["chroma_collection"]
    chroma_count = collection.count()
    assert chroma_count == total_chunks, f"ChromaDB count ({chroma_count}) != chunks count ({total_chunks})"
    print(f"[PASS] Successfully verified {chroma_count} records in ChromaDB collection '{COLLECTION_NAME}'.")

    print("\n--- 4. Sanity Retrieval Smoke Test ---")
    test_query = "How many days of sick leave can an FTE take?"
    
    # BM25 test
    query_tokens = re.findall(r"\b\w+\b", test_query.lower())
    bm25_scores = indices["bm25"].get_scores(query_tokens)
    top_bm25_idx = int(bm25_scores.argmax())
    top_bm25_chunk = indices["chunks"][top_bm25_idx]
    
    print(f"Top BM25 Result: [{top_bm25_chunk.metadata['policy_name']} - Section: {top_bm25_chunk.metadata['section']}]")
    assert "sick" in top_bm25_chunk.page_content.lower() or "leave" in top_bm25_chunk.page_content.lower()

    # ChromaDB test (with BGE query prefix)
    query_embedding = indices["embedding_model"].encode(
        f"{indices['query_prefix']}{test_query}"
    ).tolist()
    
    dense_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )
    
    top_dense_meta = dense_results["metadatas"][0][0]
    top_dense_doc = dense_results["documents"][0][0]
    print(f"Top Dense Result: [{top_dense_meta['policy_name']} - Section: {top_dense_meta['section']}]")
    print(f"Content excerpt: {top_dense_doc[:250]}...")
    
    print("\n[PASS] Indexing pipeline operational and ready for hybrid retrieval.")


if __name__ == "__main__":
    test_indexing_pipeline()