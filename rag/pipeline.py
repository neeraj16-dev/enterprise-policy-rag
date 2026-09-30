import os
import time
from typing import Dict, Any, List, Optional
from langchain_core.documents import Document

from rag.indexing import load_indexes
from rag.reranking import Reranker
from rag.retrieval import hybrid_retrieve_and_rerank
from rag.generation import RagGenerator
from rag.verification import GroundingVerifier


class RAGPipeline:
    def __init__(
        self,
        reranker_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
        generator_model: Optional[str] = None,
        verifier_model: Optional[str] = None,
    ):
        print("Initializing TechV-Flash Enterprise RAG Pipeline...")

        self.handles = load_indexes()
        self.reranker = Reranker(model_name=reranker_model)

        gen_m = generator_model or os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
        ver_m = verifier_model or os.getenv("VERIFIER_MODEL", "gemini-3.1-flash-lite")

        self.generator = RagGenerator(model_name=gen_m)
        self.verifier = GroundingVerifier(model=ver_m)

        print("RAG Pipeline ready.")

    def query(
        self,
        question: str,
        fetch_k: int = 15,
        top_n: int = 3,
        verify: bool = True
    ) -> Dict[str, Any]:
        """
        Executes end-to-end Enterprise RAG:
        Hybrid Retrieval (BM25 + Dense BGE via RRF)
            ↓
        Cross-Encoder Reranking
            ↓
        Structured Gemini Generation
            ↓
        Grounding & Hallucination Verification
        """
        metrics: Dict[str, float] = {}
        total_start = time.perf_counter()

        # Step 1: Retrieval + Reranking
        t0 = time.perf_counter()
        reranked_results = hybrid_retrieve_and_rerank(
            query=question,
            handles=self.handles,
            reranker=self.reranker,
            fetch_k=fetch_k,
            top_n=top_n
        )
        metrics["retrieval_rerank_ms"] = round((time.perf_counter() - t0) * 1000, 2)

        top_docs: List[Document] = [doc for doc, score in reranked_results]

        # Step 2: Generation
        t0 = time.perf_counter()
        gen_output = self.generator.generate(
            question=question,
            docs=top_docs
        )
        metrics["generation_ms"] = round((time.perf_counter() - t0) * 1000, 2)

        # Step 3: Verification
        verification_result = None
        if verify:
            t0 = time.perf_counter()
            verification_result = self.verifier.verify(
                generation_output=gen_output,
                retrieved_docs=top_docs
            )
            metrics["verification_ms"] = round((time.perf_counter() - t0) * 1000, 2)

        metrics["total_latency_ms"] = round((time.perf_counter() - total_start) * 1000, 2)

        retrieved_contexts = [
            {
                "chunk_id": doc.metadata.get("chunk_id"),
                "policy_name": doc.metadata.get("policy_name"),
                "doc_ref": doc.metadata.get("doc_ref"),
                "page": doc.metadata.get("page"),
                "section": doc.metadata.get("section"),
                "content_preview": doc.page_content[:200] + "..."
            }
            for doc in top_docs
        ]

        return {
            "query": question,
            "answer": gen_output.get("answer", ""),
            "citations": gen_output.get("citations", []),
            "verification": verification_result,
            "retrieved_chunks": retrieved_contexts,
            "metrics": metrics
        }