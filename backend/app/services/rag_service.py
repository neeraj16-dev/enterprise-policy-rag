from typing import Dict, Any
from rag.pipeline import RAGPipeline


class RAGService:
    def __init__(self):
        print("Initializing TechV-Flash Policy RAG Service...")
        self.pipeline = RAGPipeline()
        print("RAG service ready.")

    def query(
        self,
        question: str,
        top_n: int = 5,
        verify_grounding: bool = True
    ) -> Dict[str, Any]:
        return self.pipeline.query(
            question=question,
            fetch_k=15,
            top_n=top_n,
            verify=verify_grounding
        )