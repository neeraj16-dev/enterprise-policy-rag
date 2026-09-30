import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


class GroundingVerdict(BaseModel):
    is_grounded: bool = Field(
        description="True if every factual statement, number, SLA, and rule in the answer is backed by the cited text."
    )
    unsupported_claims: List[str] = Field(
        default_factory=list,
        description="List of specific claims or numbers in the answer that lack evidence in the cited text."
    )
    hallucination_score: float = Field(
        ge=0.0, le=1.0,
        description="0.0 for completely grounded in context, 1.0 for completely hallucinated."
    )
    explanation: str = Field(
        description="Concise rationale explaining the grounding verification decision."
    )


class GroundingVerifier:
    def __init__(self, model: Optional[str] = None):
        verifier_model = model or os.getenv("VERIFIER_MODEL", "gemini-3.1-flash-lite")
        self.eval_llm = ChatGoogleGenerativeAI(
            model=verifier_model,
            temperature=0.0
        ).with_structured_output(GroundingVerdict, method="json_mode")

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are an impartial corporate compliance and policy grounding auditor.\n\n"
                "Your task is to audit an Answer against the exact text of the Cited Chunks.\n"
                "Rules:\n"
                "1. If the Answer contains facts, numerical limits, formulas, or rules NOT found in the cited text, flag them.\n"
                "2. Standard grammatical phrasing that preserves meaning is grounded.\n"
                "3. If the answer accurately states that information is not available in the context, mark is_grounded as True."
            ),
            (
                "human",
                "Cited Chunks:\n{cited_text}\n\n"
                "Generated Answer:\n{answer}"
            )
        ])

        self.chain = self.prompt | self.eval_llm

    def verify(
        self,
        generation_output: Dict[str, Any],
        retrieved_docs: List[Document]
    ) -> Dict[str, Any]:
        answer = generation_output.get("answer", "")
        citations = generation_output.get("citations", [])

        # Build case-normalized lookup map for retrieved chunks
        valid_chunk_map = {
            doc.metadata.get("chunk_id", "").strip().lower(): doc
            for doc in retrieved_docs
            if doc.metadata.get("chunk_id")
        }

        valid_citations = []
        phantom_citations = []

        for c in citations:
            cid = c.get("chunk_id", "").strip().lower()
            if cid in valid_chunk_map:
                valid_citations.append(valid_chunk_map[cid])
            else:
                phantom_citations.append(c.get("chunk_id", ""))

        # If answer states that no info is available, it is grounded by definition
        if "do not contain information" in answer.lower():
            return {
                "is_grounded": True,
                "unsupported_claims": [],
                "hallucination_score": 0.0,
                "phantom_citations": phantom_citations,
                "explanation": "The assistant correctly identified that the information is absent from the context."
            }

        if not valid_citations:
            return {
                "is_grounded": False,
                "unsupported_claims": ["No valid cited chunks found in retrieved context."],
                "hallucination_score": 1.0,
                "phantom_citations": phantom_citations,
                "explanation": "The model produced citations that did not match any retrieved chunks."
            }

        cited_text = "\n\n".join(
            [f"[{doc.metadata.get('chunk_id')} | Section: {doc.metadata.get('section')}]: {doc.page_content}"
             for doc in valid_citations]
        )

        eval_result: GroundingVerdict = self.chain.invoke({
            "cited_text": cited_text,
            "answer": answer
        })

        result_dict = eval_result.model_dump()
        result_dict["phantom_citations"] = phantom_citations
        return result_dict