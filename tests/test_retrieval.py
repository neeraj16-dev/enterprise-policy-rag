import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.indexing import load_indexes
from rag.retrieval import hybrid_retrieve


def test_retrieval_pipeline():
    print("\n--- Loading Pre-built Indices ---")
    handles = load_indexes()
    assert handles["chroma_collection"].count() > 0, "Chroma collection is empty."
    print(f"[PASS] Successfully loaded indices with {len(handles['chunks'])} BM25 chunks and ChromaDB collection.")

    test_cases = [
        {
            "query": "How many days of sick leave can an employee take before submitting a medical certificate?",
            "expected_keyword": "sick",
            "expected_policy": "Leave & Attendance"
        },
        {
            "query": "What are the rules and expiry validity for compensatory off when working weekends?",
            "expected_keyword": "comp-off",
            "expected_policy": "Leave & Attendance"
        },
        {
            "query": "What is the maximum timeline for a respondent to reply to a POSH complaint notice?",
            "expected_keyword": "posh",
            "expected_policy": "Anti Harassment"
        }
    ]

    print("\n--- Running Hybrid Retrieval Domain Tests ---")
    for i, test in enumerate(test_cases, 1):
        query = test["query"]
        print(f"\n[Test Case {i}] Query: '{query}'")
        
        results = hybrid_retrieve(query, handles, top_k=3)
        assert len(results) > 0, f"No results returned for query: {query}"

        top_hit = results[0]
        policy_name = top_hit.metadata.get("policy_name", "")
        section = top_hit.metadata.get("section", "")
        chunk_id = top_hit.metadata.get("chunk_id", "")
        content_preview = top_hit.page_content.replace("\n", " ")[:180]

        print(f"Top Result -> [{policy_name} | {section} | Chunk: {chunk_id}]")
        print(f"Preview: {content_preview}...")

        # Assert relevance
        content_lower = top_hit.page_content.lower()
        assert test["expected_keyword"] in content_lower or test["expected_keyword"] in section.lower(), (
            f"Expected keyword '{test['expected_keyword']}' not found in top hit."
        )

    print("\n[PASS] All hybrid retrieval test cases passed successfully.")


if __name__ == "__main__":
    test_retrieval_pipeline()