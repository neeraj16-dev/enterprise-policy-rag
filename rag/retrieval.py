import re
from typing import List, Dict, Any, Tuple, Optional
from langchain_core.documents import Document


def retrieve_bm25(
    query: str, 
    bm25_index, 
    chunks: List[Document], 
    top_k: int = 20,
    filter_category: Optional[str] = None
) -> List[Document]:
    """
    Retrieves top_k chunks using BM25 Okapi keyword matching with optional category filtering.
    """
    tokenized_query = re.findall(r"\b\w+\b", query.lower())
    scores = bm25_index.get_scores(tokenized_query)

    ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    results: List[Document] = []
    for idx in ranked_indices:
        doc = chunks[idx]
        if filter_category and doc.metadata.get("category") != filter_category:
            continue
        results.append(doc)
        if len(results) >= top_k:
            break

    return results


def retrieve_dense(
    query: str, 
    collection, 
    model, 
    top_k: int = 20,
    query_prefix: str = "Represent this sentence for searching relevant passages: ",
    filter_dict: Optional[Dict[str, Any]] = None
) -> List[Document]:
    """
    Retrieves top_k dense vector chunks from ChromaDB with instruction prefixing and metadata filtering.
    """
    # BGE query instruction prefix is crucial for retrieval accuracy
    prefixed_query = f"{query_prefix}{query}" if query_prefix else query
    query_vector = model.encode([prefixed_query]).tolist()

    query_params: Dict[str, Any] = {
        "query_embeddings": query_vector,
        "n_results": top_k
    }

    if filter_dict:
        query_params["where"] = filter_dict

    results = collection.query(**query_params)

    retrieved_docs: List[Document] = []
    if results and "documents" in results and results["documents"]:
        for text, meta in zip(results["documents"][0], results["metadatas"][0]):
            retrieved_docs.append(Document(page_content=text, metadata=meta))

    return retrieved_docs


def reciprocal_rank_fusion(
    ranked_lists: List[List[Document]], 
    k: int = 60, 
    top_k: int = 10
) -> List[Document]:
    """
    Fuses multiple ranked lists using Reciprocal Rank Fusion (RRF).
    Score(d) = sum(1 / (k + rank))
    """
    rrf_scores: Dict[str, float] = {}
    doc_store: Dict[str, Document] = {}

    for doc_list in ranked_lists:
        for rank, doc in enumerate(doc_list, start=1):
            chunk_id = doc.metadata.get("chunk_id")
            if not chunk_id:
                continue

            doc_store[chunk_id] = doc
            if chunk_id not in rrf_scores:
                rrf_scores[chunk_id] = 0.0

            rrf_scores[chunk_id] += 1.0 / (k + rank)

    sorted_chunk_ids = sorted(rrf_scores.keys(), key=lambda cid: rrf_scores[cid], reverse=True)
    return [doc_store[cid] for cid in sorted_chunk_ids[:top_k]]


def hybrid_retrieve(
    query: str, 
    handles: Dict[str, Any], 
    top_k: int = 5,
    filter_category: Optional[str] = None
) -> List[Document]:
    """
    Executes hybrid retrieval combining BM25 keyword search and dense ChromaDB search via RRF.
    """
    filter_dict = {"category": filter_category} if filter_category else None
    query_prefix = handles.get("query_prefix", "Represent this sentence for searching relevant passages: ")

    bm25_docs = retrieve_bm25(
        query=query, 
        bm25_index=handles["bm25"], 
        chunks=handles["chunks"], 
        top_k=20,
        filter_category=filter_category
    )

    dense_docs = retrieve_dense(
        query=query, 
        collection=handles["chroma_collection"], 
        model=handles["embedding_model"], 
        top_k=20,
        query_prefix=query_prefix,
        filter_dict=filter_dict
    )

    fused_docs = reciprocal_rank_fusion([bm25_docs, dense_docs], k=60, top_k=top_k)
    return fused_docs


def hybrid_retrieve_and_rerank(
    query: str,
    handles: Dict[str, Any],
    reranker: Any,
    fetch_k: int = 15,
    top_n: int = 4,
    filter_category: Optional[str] = None
) -> List[Tuple[Document, float]]:
    """
    Executes hybrid retrieval followed by cross-encoder neural reranking.
    """
    candidate_docs = hybrid_retrieve(
        query=query,
        handles=handles,
        top_k=fetch_k,
        filter_category=filter_category
    )

    reranked_docs = reranker.rerank(
        query=query,
        docs=candidate_docs,
        top_n=top_n
    )

    return reranked_docs