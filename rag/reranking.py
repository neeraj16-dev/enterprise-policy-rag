import torch
from typing import List, Tuple, Optional
from sentence_transformers import CrossEncoder
from langchain_core.documents import Document


class Reranker:
    def __init__(
        self, 
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2", 
        device: Optional[str] = None
    ):
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        print(f"Loading cross-encoder model: {model_name} on device: {device}...")
        self.device = device
        self.model = CrossEncoder(model_name, max_length=512, device=device)

    def rerank(
        self, 
        query: str, 
        docs: List[Document], 
        top_n: int = 5,
        batch_size: int = 16
    ) -> List[Tuple[Document, float]]:
        """
        Reranks a list of candidate documents against the query using cross-attention scoring.
        Returns a sorted list of (Document, score) tuples.
        """
        if not docs:
            return []

        pairs = [[query, doc.page_content] for doc in docs]
        scores = self.model.predict(
            pairs, 
            batch_size=batch_size, 
            show_progress_bar=False
        )

        doc_score_pairs = list(zip(docs, [float(s) for s in scores]))
        doc_score_pairs.sort(key=lambda x: x[1], reverse=True)

        return doc_score_pairs[:top_n]