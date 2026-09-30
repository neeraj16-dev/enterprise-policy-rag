import sys
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.indexing import load_indexes
from rag.reranking import Reranker
from rag.retrieval import hybrid_retrieve_and_rerank
from rag.generation import RagGenerator


def test_generation_pipeline():
    print("\n--- Initializing Pipeline Components ---")
    handles = load_indexes()
    reranker = Reranker()
    generator = RagGenerator()

    query = "What is the formula for leave encashment, what leaves qualify, and what is the minimum balance required?"
    print(f"\nQuery: {query}")

    # 1. Retrieval + Cross-Encoder Reranking
    reranked_results = hybrid_retrieve_and_rerank(
        query=query,
        handles=handles,
        reranker=reranker,
        fetch_k=15,
        top_n=3
    )

    final_docs = [doc for doc, score in reranked_results]
    assert len(final_docs) > 0, "No documents passed to generation stage."

    # 2. Generation with Grounded Structured Output
    print("\nGenerating grounded answer via Gemini...")
    output = generator.generate(question=query, docs=final_docs)

    print("\n--- Model Output ---")
    print(json.dumps(output, indent=2))

    # Assertions
    assert "answer" in output and len(output["answer"]) > 0, "Empty answer returned."
    assert "citations" in output and len(output["citations"]) > 0, "No citations generated."

    first_cite = output["citations"][0]
    assert "doc_ref" in first_cite and first_cite["doc_ref"] != "N/A"
    assert "quote" in first_cite and len(first_cite["quote"]) > 0

    print("\n[PASS] Generation pipeline verified with grounded citations.")


if __name__ == "__main__":
    test_generation_pipeline()