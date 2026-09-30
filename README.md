# 🏛️ Enterprise Policy Intelligence RAG Platform

> Production-ready, citation-grounded Retrieval-Augmented Generation (RAG) platform architected for strict enterprise compliance, regulatory verification, and multi-tier corporate policy Q&A.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-14+-000000?logo=next.js&logoColor=white)](https://nextjs.org)
[![ChromaDB](https://img.shields.io/badge/Vector%20Store-ChromaDB-orange)](https://www.trychroma.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📌 Overview

Enterprise policies (HR codes, separation agreements, financial payroll rules, compliance frameworks) are filled with numerical thresholds, strict deadlines, and tiered approval matrices. Standard RAG architectures fail on such corpora due to document overlap, loss of table formatting, and unverified citations.

This platform implements a **hybrid retrieval (BM25 + Dense BGE) with Reciprocal Rank Fusion**, cross-encoder neural reranking, **strictly structured generation (Pydantic schemas)**, and an **automated LLM-as-a-judge grounding verifier** that inspects and certifies every answer before delivery.

---

## ⚡ Core Performance Scorecard

Evaluated systematically across **51 multi-clause compliance questions** with ground-truth validation:

| Metric | Target | Result | Status |
| :--- | :---: | :---: | :---: |
| **Hit Rate @ 3** | ≥ 80.0% | **96.1%** | ✅ Exceeded |
| **Mean Reciprocal Rank (MRR)** | ≥ 0.700 | **0.892** | ✅ Exceeded |
| **Faithfulness Score** | ≥ 90.0% | **99.8%** | ✅ Exceeded |
| **Answer Relevance** | ≥ 85.0% | **97.6%** | ✅ Exceeded |
| **Ground Truth Accuracy** | ≥ 85.0% | **92.5%** | ✅ Exceeded |

---

## 🏗️ System Architecture

```text
User Inquiry
    │
    ▼
[ Hybrid Retrieval Engine ]
    ├── Sparse Retrieval: BM25 (Exact terms, SLAs, Policy IDs)
    └── Dense Retrieval: BAAI/bge-small-en-v1.5 + ChromaDB
    │
    ▼
[ Reciprocal Rank Fusion (RRF, k=60) ] ──▶ Top 15 Candidates
    │
    ▼
[ Cross-Encoder Neural Reranker ]
    └── cross-encoder/ms-marco-MiniLM-L-6-v2 ──▶ Top 3 Focused Chunks
    │
    ▼
[ Structured Generation via LangChain ]
    └── Gemini Model with Pydantic JSON Mode
        ├── Synthesizes Answer
        └── Attaches Citations (doc_ref, policy_name, clause, verbatim quote)
    │
    ▼
[ Online Grounding Verifier Guardrail ]
    ├── Verifies claims against cited text
    ├── Flags phantom citations & out-of-context extrapolations
    └── Calculates Hallucination Score (0.0 = Certified Grounded)
    │
    ▼
FastAPI Non-Blocking Response ──▶ Next.js Enterprise Dashboard
```

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12, FastAPI, Uvicorn, Pydantic v2
- **Frontend:** Next.js (App Router), TypeScript, Tailwind CSS, Lucide Icons
- **RAG & Orchestration:** LangChain, Google Gemini API (`gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`)
- **Embeddings & Vector Store:** `BAAI/bge-small-en-v1.5`, ChromaDB
- **Lexical & Reranking:** BM25, `cross-encoder/ms-marco-MiniLM-L-6-v2`
- **Evaluation:** Custom Ragas-style LLM-as-a-judge suite
- **DevOps:** Docker, Docker Compose (Multi-stage builds with standalone node runner)

---

## 📂 Project Structure

```text
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py            # API endpoints (/query, /health)
│   │   ├── services/
│   │   │   └── rag_service.py       # Async threadpool orchestration
│   │   ├── main.py                  # Lifespan startup & CORS setup
│   │   └── schemas.py               # Pydantic request & response contracts
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/                         # Next.js UI components & API client
│   ├── public/
│   ├── Dockerfile
│   ├── next.config.js               # Standalone output configuration
│   └── package.json
│
├── rag/
│   ├── chunking.py                  # Structure & header-aware chunker
│   ├── indexing.py                  # ChromaDB vector store & BM25 indexer
│   ├── retrieval.py                 # Dense + sparse RRF fusion search
│   ├── reranking.py                 # Cross-encoder inference wrapper
│   ├── generation.py                # Structured Gemini prompt chain
│   ├── verification.py              # Online grounding guardrail
│   ├── evaluation.py                # LLM-as-a-judge evaluation suite
│   └── pipeline.py                  # Master RAG pipeline controller
│
├── tests/
│   ├── eval_dataset.json            # 51-query benchmark dataset
│   ├── test_reranking.py            # Retrieval & cross-encoder assertions
│   ├── test_generation.py           # Structured output tests
│   └── test_evaluation.py           # Automated evaluation runner
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start

### 1. Prerequisites

- Docker & Docker Compose installed
- Google Gemini API Key

### 2. Environment Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
VERIFIER_MODEL=gemini-3.1-flash-lite
EVAL_JUDGE_MODEL=gemini-3.1-flash-lite
```

### 3. Run with Docker Compose

```bash
docker compose up --build -d
```

- **Frontend Dashboard:** [http://localhost:3000](http://localhost:3000)
- **FastAPI OpenAPI Docs:** [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

## 🧪 Local Development & Evaluation

To run tests and benchmark the pipeline locally without containers:

```bash
# 1. Activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r backend/requirements.txt

# 3. Test Retrieval & Reranker Precision
python -m tests.test_reranking

# 4. Run the 51-Query Benchmark Evaluation
python -m tests.test_evaluation
```

---

## 🛡️ Grounding Verification Schema

Responses from `/api/v1/query` return verifiable citations alongside an automatic hallucination audit:

```json
{
  "query": "What is the maximum PTO carryover allowed into the next calendar year?",
  "answer": "Full-Time Employees (FTEs) may carry over a maximum of 5 unused PTO days into the following calendar year. These carried-over days must be utilized by March 31st of the new year, or they will expire.",
  "citations": [
    {
      "chunk_id": "TechV-Flash_Leave_Attendance_Policy_p1_c03",
      "policy_name": "Leave Attendance Policy",
      "doc_ref": "HR-POL-002",
      "section": "1.2 Carryover Policy",
      "page": 1,
      "quote": "FTEs may carry over a maximum of 5 unused PTO days into the following calendar year."
    }
  ],
  "verification": {
    "is_grounded": true,
    "unsupported_claims": [],
    "hallucination_score": 0.0,
    "explanation": "The answer accurately reflects the carryover policy for FTEs as stated in the provided text.",
    "phantom_citations": []
  },
  "metrics": {
    "retrieval_rerank_ms": 4563.68,
    "generation_ms": 1686.71,
    "verification_ms": 9085.70,
    "total_latency_ms": 15336.13
  }
}
```