import sys
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.pipeline import RAGPipeline


def test_end_to_end_pipeline():
    pipeline = RAGPipeline()

    test_query = (
        "What is the standard notice period during probation versus confirmed status, "
        "and are employees permitted to use PTO while serving their notice period?"
    )
    print(f"\n[Test Query]: {test_query}")

    result = pipeline.query(question=test_query, fetch_k=15, top_n=3, verify=True)

    print("\n" + "=" * 50)
    print("           END-TO-END PIPELINE RESULT")
    print("=" * 50)
    print(f"Answer:\n{result['answer']}\n")

    print("Citations:")
    for c in result["citations"]:
        print(f" - [{c.get('doc_ref')}] {c.get('policy_name')} (Section: {c.get('section')}, Page {c.get('page')})")
        print(f"   Quote: \"{c.get('quote')}\"")

    print("\nGrounding Verification:")
    ver = result["verification"]
    print(f" - Is Grounded        : {ver['is_grounded']}")
    print(f" - Hallucination Score: {ver['hallucination_score']}")
    print(f" - Explanation        : {ver['explanation']}")
    if ver.get("phantom_citations"):
        print(f" - Phantom Citations  : {ver['phantom_citations']}")

    print("\nLatency Metrics:")
    for k, v in result["metrics"].items():
        print(f" - {k}: {v} ms")
    print("=" * 50)

    # Invariants
    assert len(result["answer"]) > 0, "No answer generated."
    assert len(result["citations"]) > 0, "No citations generated."
    assert ver["is_grounded"] is True, f"Answer failed grounding verification: {ver['explanation']}"
    assert ver["hallucination_score"] == 0.0, "Detected hallucination in response."
    print("\n[PASS] End-to-end pipeline verification succeeded.")


if __name__ == "__main__":
    test_end_to_end_pipeline()