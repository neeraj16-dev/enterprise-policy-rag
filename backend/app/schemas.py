from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        description="Company policy or compliance inquiry",
        example="What is the maximum PTO carryover allowed into the next calendar year?"
    )
    top_n: int = Field(default=3, ge=1, le=10, description="Number of reranked chunks to feed the generator")
    verify_grounding: bool = Field(default=True, description="Run online grounding verification guardrail")


class CitationModel(BaseModel):
    chunk_id: str
    policy_name: Optional[str] = "Corporate Policy"
    doc_ref: Optional[str] = "N/A"
    section: Optional[str] = "General"
    page: int
    quote: Optional[str] = ""


class VerificationModel(BaseModel):
    is_grounded: bool
    unsupported_claims: List[str] = Field(default_factory=list)
    hallucination_score: float
    explanation: str
    phantom_citations: List[str] = Field(default_factory=list)


class ChunkMetadata(BaseModel):
    chunk_id: Optional[str] = None
    policy_name: Optional[str] = None
    doc_ref: Optional[str] = None
    page: Optional[int] = None
    section: Optional[str] = None
    content_preview: str


class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: List[CitationModel]
    verification: Optional[VerificationModel] = None
    retrieved_chunks: List[ChunkMetadata]
    metrics: Dict[str, float]