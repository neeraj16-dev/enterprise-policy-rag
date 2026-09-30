import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.indexing import load_indexes
from rag.reranking import Reranker
from rag.retrieval import hybrid_retrieve_and_rerank


def test_reranking_pipeline():
    print("\n--- Loading Pre-built Indices ---")
    handles = load_indexes()
    reranker = Reranker()

    test_queries = [
        {
            "query": "What is the maximum PTO carryover allowed into the next year and when does it expire?",
            "expected_policy": "Leave Attendance Policy",
            "expected_term": "march 31"
        },
        {
            "query": "How many consecutive days of no call no show results in job abandonment and termination?",
            "expected_policy": "Leave Attendance Policy",
            "expected_term": "3 consecutive"
        }
    ]

    print("\n--- Running Hybrid Retrieval + Reranking Tests ---")
    for idx, test in enumerate(test_queries, 1):
        query = test["query"]
        print(f"\n[Test {idx}] Query: {query}")

        results = hybrid_retrieve_and_rerank(
            query=query,
            handles=handles,
            reranker=reranker,
            fetch_k=15,
            top_n=3
        )

        assert len(results) > 0, f"No results returned after reranking for: {query}"

        top_doc, top_score = results[0]
        policy = top_doc.metadata.get("policy_name", "")
        section = top_doc.metadata.get("section", "")
        chunk_id = top_doc.metadata.get("chunk_id", "")

        print(f"Top 1 (Score: {top_score:.4f}): [{policy} | {section} | {chunk_id}]")
        print(f"Content:\n{top_doc.page_content[:260]}...\n")

        # Verify semantic precision
        assert test["expected_term"] in top_doc.page_content.lower(), (
            f"Expected term '{test['expected_term']}' not found in top reranked result."
        )

    print("[PASS] Hybrid retrieval + Cross-Encoder reranking pipeline verified.")


if __name__ == "__main__":
    test_reranking_pipeline()