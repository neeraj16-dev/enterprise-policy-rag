import sys
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.indexing import load_indexes
from rag.reranking import Reranker
from rag.generation import RagGenerator
from rag.evaluation import RAGEvaluator


def test_evaluation_pipeline():
    handles = load_indexes()
    reranker = Reranker()

    generator = RagGenerator(model_name="gemini-3.5-flash-lite")
    evaluator = RAGEvaluator(model="gemini-3.1-flash-lite")

    dataset_path = "tests/eval_dataset.json"

    # 4.2s delay ensures strict compliance under the 15 RPM cap
    results = evaluator.evaluate_testset(
        testset_path=dataset_path,
        handles=handles,
        reranker=reranker,
        generator=generator,
        top_n=3,
        request_delay=4.2
    )

    print("\n" + "=" * 50)
    print("           BENCHMARK SCORECARD")
    print("=" * 50)
    print(f"Hit Rate @ 3         : {results['hit_rate_at_k'] * 100:.1f}%")
    print(f"Mean Reciprocal Rank : {results['mean_reciprocal_rank']:.3f}")
    print(f"Avg Faithfulness     : {results['avg_faithfulness'] * 100:.1f}%")
    print(f"Avg Answer Relevance : {results['avg_answer_relevance'] * 100:.1f}%")
    print(f"Avg Ground Truth     : {results['avg_ground_truth_score'] * 100:.1f}%")
    print("=" * 50)

    assert results["hit_rate_at_k"] >= 0.8, f"Hit rate ({results['hit_rate_at_k']}) below 80% benchmark target."
    assert results["avg_faithfulness"] >= 0.8, f"Faithfulness ({results['avg_faithfulness']}) below 80% benchmark target."

    with open("tests/eval_report.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("Detailed report saved to tests/eval_report.json")


if __name__ == "__main__":
    test_evaluation_pipeline()