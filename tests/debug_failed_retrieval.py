import json
from rag.indexing import load_indexes
from rag.retrieval import hybrid_retrieve_and_rerank
from rag.reranking import Reranker


def main():
    with open("tests/eval_report.json", "r", encoding="utf-8") as f:
        report = json.load(f)

    handles = load_indexes()
    reranker = Reranker()

    for item in report["details"]:
        if item["hit"] != 0:
            continue

        print("\n" + "=" * 100)
        print("QUESTION:")
        print(item["question"])

        print("\nEXPECTED:")
        print(item["expected_chunk_ids"])

        reranked = hybrid_retrieve_and_rerank(
            query=item["question"],
            handles=handles,
            reranker=reranker,
            fetch_k=15,
            top_n=5
        )

        print("\nRERANKED RESULTS:")

        for rank, (doc, score) in enumerate(reranked, 1):
            print("\n" + "-" * 80)
            print(f"Rank: {rank}")
            print(f"Score: {score:.4f}")
            print(f"Chunk ID: {doc.metadata.get('chunk_id')}")
            print(f"Policy: {doc.metadata.get('policy_name')}")
            print(f"Section: {doc.metadata.get('section')}")
            print(f"Page: {doc.metadata.get('page')}")
            print("\nCONTENT:")
            print(doc.page_content)


if __name__ == "__main__":
    main()