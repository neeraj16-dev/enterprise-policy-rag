import asyncio
from fastapi import APIRouter, HTTPException, Request, status
from backend.app.schemas import QueryRequest, QueryResponse

router = APIRouter()


def get_rag_service(request: Request):
    if not getattr(request.app.state, "rag_ready", False):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="RAG Service is still initializing. Please try again shortly."
        )

    rag_service = getattr(request.app.state, "rag_service", None)
    if rag_service is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="RAG Service failed to initialize."
        )

    return rag_service


@router.get("/")
def root():
    return {
        "service": "TechV-Flash Enterprise Policy Intelligence RAG Service",
        "status": "running",
        "docs": "/api/docs"
    }


@router.get("/health")
def health_check(request: Request):
    get_rag_service(request)
    return {
        "status": "healthy",
        "service": "TechV-Flash Enterprise Policy Intelligence RAG Service"
    }


@router.post("/api/v1/query", response_model=QueryResponse)
async def query_rag(request: Request, query_request: QueryRequest):
    rag_service = get_rag_service(request)

    # Offload heavy synchronous ML inference & LLM calls to threadpool
    result = await asyncio.to_thread(
        rag_service.query,
        question=query_request.query,
        top_n=query_request.top_n,
        verify_grounding=query_request.verify_grounding
    )
    return result