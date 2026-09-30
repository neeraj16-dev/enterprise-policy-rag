import os
import json
import time
import re
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from rag.retrieval import hybrid_retrieve_and_rerank
from rag.generation import RagGenerator
from dotenv import load_dotenv

load_dotenv()


class GenerationEvalScores(BaseModel):
    faithfulness_score: float = Field(
        ge=0.0, le=1.0,
        description="Score from 0.0 to 1.0 indicating how faithfully the answer is supported exclusively by the provided context."
    )
    answer_relevance_score: float = Field(
        ge=0.0, le=1.0,
        description="Score from 0.0 to 1.0 indicating how directly and concisely the answer addresses the question."
    )
    ground_truth_score: float = Field(
        ge=0.0, le=1.0,
        description="Score from 0.0 to 1.0 indicating how accurately the generated answer conveys the facts in the ground truth."
    )
    critique: str = Field(
        description="Concise justification of the assigned scores."
    )


class RAGEvaluator:
    def __init__(self, model: Optional[str] = None):
        eval_model = model or os.getenv("EVAL_JUDGE_MODEL", "gemini-3.1-flash-lite")
        self.judge = ChatGoogleGenerativeAI(
            model=eval_model,
            temperature=0.0
        ).with_structured_output(GenerationEvalScores, method="json_mode")

        self.judge_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are an impartial RAG benchmark evaluator for enterprise compliance and company policy QA.\n\n"
                "Evaluate the generated answer against the provided Question, Context, and Ground Truth.\n\n"
                "Scoring Criteria (0.0 to 1.0):\n"
                "1. Faithfulness:\n"
                "   Does every statement in the answer originate directly from the Context? Penalize outside assumptions.\n\n"
                "2. Answer Relevance:\n"
                "   Does the answer directly address the user's specific policy inquiry without redundant padding?\n\n"
                "3. Ground Truth Accuracy:\n"
                "   Does the answer accurately capture the vital rules, timelines, SLAs, numerical thresholds, or approval workflows given in the Ground Truth?\n\n"
                "Evaluation Constraints:\n"
                "- Do NOT rely on outside legal or corporate HR assumptions.\n"
                "- Base your decision strictly on the provided Context and Ground Truth."
            ),
            (
                "human",
                "Question:\n{question}\n\n"
                "Context:\n{context}\n\n"
                "Ground Truth:\n{ground_truth}\n\n"
                "Generated Answer:\n{answer}"
            )
        ])

        self.judge_chain = self.judge_prompt | self.judge

    @staticmethod
    def calculate_retrieval_metrics(
        retrieved_docs: List[Any],
        expected_section: Optional[str] = None,
        expected_ids: Optional[List[str]] = None
    ) -> Dict[str, float]:
        """
        Hit is 1.0 if any top retrieved chunk matches:
        1. Exact or partial expected chunk ID.
        2. Expected section text found in either doc metadata['section'] or doc.page_content.
        """
        hit = 0.0
        reciprocal_rank = 0.0

        target_keywords = []
        if expected_section:
            # Strip section numbers like '1.1 ' to match the core topic name
            core_section = re.sub(r"^\d+(\.\d+)*\s*", "", expected_section).strip().lower()
            target_keywords.append(expected_section.strip().lower())
            if core_section:
                target_keywords.append(core_section)

        for rank, doc in enumerate(retrieved_docs, start=1):
            chunk_id = doc.metadata.get("chunk_id", "").strip().lower()
            section_meta = doc.metadata.get("section", "").strip().lower()
            content = doc.page_content.lower()

            # Check 1: Chunk ID match
            id_match = False
            if expected_ids:
                id_match = any(exp.strip().lower() in chunk_id or chunk_id in exp.strip().lower() for exp in expected_ids if exp)

            # Check 2: Section or keyword containment
            sec_match = False
            for kw in target_keywords:
                if kw in section_meta or kw in content:
                    sec_match = True
                    break

            if id_match or sec_match:
                hit = 1.0
                reciprocal_rank = 1.0 / rank
                break

        return {
            "hit": hit,
            "reciprocal_rank": reciprocal_rank
        }

    def evaluate_testset(
        self,
        testset_path: str,
        handles: Dict[str, Any],
        reranker: Any,
        generator: RagGenerator,
        top_n: int = 3,
        request_delay: float = 4.2
    ) -> Dict[str, Any]:
        with open(testset_path, "r", encoding="utf-8") as f:
            testset = json.load(f)

        total_queries = len(testset)
        if total_queries == 0:
            return {"error": "Test set is empty", "total_queries": 0}

        hits = 0.0
        mrr_total = 0.0
        total_faithfulness = 0.0
        total_relevance = 0.0
        total_ground_truth_score = 0.0
        detailed_results = []

        print(f"\n--- Starting Evaluation on {total_queries} queries (Delay: {request_delay}s between calls) ---")

        for i, item in enumerate(testset, 1):
            question = item["question"]
            expected_cids = item.get("expected_chunk_ids", [])
            expected_section = item.get("expected_section")
            ground_truth = item.get("ground_truth", "")

            print(f"[{i:02d}/{total_queries:02d}] Evaluating: {question[:60]}...")

            # 1. Retrieval & Cross-Encoder Reranking
            reranked = hybrid_retrieve_and_rerank(
                query=question,
                handles=handles,
                reranker=reranker,
                fetch_k=15,
                top_n=top_n
            )
            top_docs = [doc for doc, score in reranked]
            retrieved_cids = [doc.metadata.get("chunk_id", "") for doc in top_docs]

            # 2. Section-Aware Retrieval Metric Evaluation
            retrieval_metrics = self.calculate_retrieval_metrics(
                retrieved_docs=top_docs,
                expected_section=expected_section,
                expected_ids=expected_cids
            )
            hits += retrieval_metrics["hit"]
            mrr_total += retrieval_metrics["reciprocal_rank"]

            # 3. Generator Call
            gen_output = generator.generate(question=question, docs=top_docs)
            answer = gen_output.get("answer", "")

            # Preserves RPM budget for generator
            if request_delay > 0:
                time.sleep(request_delay)

            # 4. LLM Judge Assessment
            context_str = "\n\n".join([doc.page_content for doc in top_docs])
            eval_scores: GenerationEvalScores = self.judge_chain.invoke({
                "question": question,
                "context": context_str,
                "ground_truth": ground_truth,
                "answer": answer
            })

            total_faithfulness += eval_scores.faithfulness_score
            total_relevance += eval_scores.answer_relevance_score
            total_ground_truth_score += eval_scores.ground_truth_score

            detailed_results.append({
                "question": question,
                "expected_section": expected_section,
                "expected_chunk_ids": expected_cids,
                "retrieved_chunk_ids": retrieved_cids,
                "ground_truth": ground_truth,
                "generated_answer": answer,
                "hit": retrieval_metrics["hit"],
                "reciprocal_rank": retrieval_metrics["reciprocal_rank"],
                "faithfulness": eval_scores.faithfulness_score,
                "answer_relevance": eval_scores.answer_relevance_score,
                "ground_truth_score": eval_scores.ground_truth_score,
                "critique": eval_scores.critique
            })

            print(
                f"     Hit: {retrieval_metrics['hit']:.0f} | "
                f"RR: {retrieval_metrics['reciprocal_rank']:.2f} | "
                f"Faith: {eval_scores.faithfulness_score:.2f} | "
                f"Rel: {eval_scores.answer_relevance_score:.2f} | "
                f"GT: {eval_scores.ground_truth_score:.2f}"
            )

            # Delay before next question to preserve judge RPM
            if request_delay > 0 and i < total_queries:
                time.sleep(request_delay)

        summary = {
            "total_queries": total_queries,
            "hit_rate_at_k": hits / total_queries,
            "mean_reciprocal_rank": mrr_total / total_queries,
            "avg_faithfulness": total_faithfulness / total_queries,
            "avg_answer_relevance": total_relevance / total_queries,
            "avg_ground_truth_score": total_ground_truth_score / total_queries,
            "details": detailed_results
        }
        return summary