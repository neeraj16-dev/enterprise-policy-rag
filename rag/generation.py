import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


class Citation(BaseModel):
    chunk_id: str = Field(description="The exact chunk_id of the source chunk used.")
    policy_name: str = Field(description="Name of the corporate policy (e.g., Leave & Attendance Policy).")
    doc_ref: str = Field(description="Document reference code (e.g., HR-POL-002).")
    section: str = Field(description="The section or clause title where the rule is stated.")
    page: int = Field(description="1-based page number.")
    quote: str = Field(description="Exact snippet or sentence from the context supporting the answer.")


class GroundedAnswer(BaseModel):
    answer: str = Field(
        description="A clear, professional, and comprehensive answer strictly grounded in the provided policy context. Include tables or lists if explaining multi-tiered rules or workflows."
    )
    citations: List[Citation] = Field(
        default_factory=list,
        description="List of specific chunks and clauses explicitly used to construct the answer."
    )


def format_context_for_prompt(docs: List[Document]) -> str:
    """Formats retrieved document chunks with clear metadata boundaries for the LLM."""
    context_blocks = []
    for doc in docs:
        cid = doc.metadata.get("chunk_id", "N/A")
        policy = doc.metadata.get("policy_name", "N/A")
        doc_ref = doc.metadata.get("doc_ref", "N/A")
        page = doc.metadata.get("page", 0)
        section = doc.metadata.get("section", "N/A")

        header = f"--- CHUNK ID: {cid} | POLICY: {policy} | REF: {doc_ref} | PAGE: {page} | SECTION: {section} ---"
        context_blocks.append(f"{header}\n{doc.page_content}")

    return "\n\n".join(context_blocks)


class RagGenerator:
    def __init__(self, model_name: Optional[str] = None):
        selected_model = model_name or os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
        self.llm = ChatGoogleGenerativeAI(
            model=selected_model,
        )
        self.structured_llm = self.llm.with_structured_output(GroundedAnswer, method="json_mode")

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are the official Enterprise Policy Intelligence Assistant for TechV-Flash.\n"
                "Your objective is to provide accurate, authoritative, and strictly grounded answers "
                "to employee queries regarding company policies, benefits, compliance, and procedures.\n\n"
                "Core Operational Guidelines:\n"
                "1. Base your answer STRICTLY and EXCLUSIVELY on the provided context. Never extrapolate or assume.\n"
                "2. If the context does not contain the answer, explicitly state: 'The provided policy documents do not contain information regarding this inquiry.'\n"
                "3. Pay strict attention to numerical limits, deadlines, SLAs, formulas, and approval authorities.\n"
                "4. When describing tables or multi-step workflows, present them clearly using structured markdown.\n"
                "5. In the 'citations' array, include every chunk from which facts, numbers, or rules were extracted."
            ),
            (
                "human",
                "Context:\n{context}\n\n"
                "Question: {question}"
            )
        ])

        self.chain = self.prompt | self.structured_llm

    def generate(self, question: str, docs: List[Document]) -> Dict[str, Any]:
        formatted_context = format_context_for_prompt(docs)
        response: GroundedAnswer = self.chain.invoke({
            "context": formatted_context,
            "question": question
        })

        return response.model_dump()