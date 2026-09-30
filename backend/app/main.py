from contextlib import asynccontextmanager
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes import router
from backend.app.services.rag_service import RAGService


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.rag_service = None
    app.state.rag_ready = False

    async def initialize_rag():
        try:
            print("Starting background RAG service initialization...")
            rag_service = await asyncio.to_thread(RAGService)
            app.state.rag_service = rag_service
            app.state.rag_ready = True
            print("RAG service successfully initialized and ready for queries.")
        except Exception as e:
            app.state.rag_ready = False
            print(f"RAG service initialization failed: {e}")

    # Launch model warmup in background task
    asyncio.create_task(initialize_rag())
    yield

    app.state.rag_service = None
    app.state.rag_ready = False


app = FastAPI(
    title="TechV-Flash Enterprise Policy Intelligence Service",
    description="Enterprise-grade hybrid search, cross-encoder reranked, and citation-grounded Policy QA API.",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)