# Learning Checkpoints

> This document tracks progress throughout the Production RAG Masterclass.
>
> It is intentionally concise.
>
> Detailed explanations live in the conversations and the codebase.
>
> This file records what has been mastered and the current learning milestone.

---

# Current Phase

🟡 Phase 10 — Production Implementation

---

# Completed Checkpoints

## ✅ Checkpoint 1 — Why RAG Exists

Can confidently explain:

- Why LLMs hallucinate
- Static vs Dynamic Knowledge
- Fine-tuning vs Retrieval
- Why RAG exists
- Why production systems use retrieval

Status

✔ Confident

---

## ✅ Checkpoint 2 — AI System Architecture

Can confidently explain:

- LLM vs RAG
- APIs
- SQL
- Tools
- Source of Truth
- Modern AI application architecture

Status

✔ Confident

---

## ✅ Checkpoint 3 — Knowledge Engineering

Can confidently explain:

- Structured Data
- Semi-Structured Data
- Unstructured Data
- Multimodal Data
- Knowledge Curation
- What belongs inside a Vector Database

Status

✔ Confident

---

## ✅ Checkpoint 4 — Production Knowledge Ingestion

Can confidently explain:

### RAG Lifecycle

- Offline Pipeline
- Online Pipeline
- Document Lifecycle
- Query Lifecycle

### Data Ingestion

- Connectors
- Document Loaders
- Parsers
- OCR
- Cleaning
- Metadata
- Duplicate Detection
- Incremental Indexing

### Engineering Concepts

- Why metadata should live outside chunks
- Metadata filtering
- Versioning
- Access control
- Index freshness
- Why preprocessing exists
- Trade-offs of preprocessing

Status

✔ Confident

---

## ✅ Checkpoint 5 — Chunking

Can confidently explain:

### Why Chunking Exists

- Why chunking is required in RAG
- Relationship between chunk quality and retrieval quality
- Retrieval precision vs generation context

### Chunking Strategies

- Fixed-Size Chunking
- Recursive Chunking
- Semantic Chunking
- Sliding Window Chunking
- Parent–Child Chunking

### Chunk Design

- Choosing chunk size
- Chunk overlap
- Semantic boundaries
- Natural document structure
- Document-specific chunking strategies

### Production Engineering

- Trade-offs between chunking strategies
- Parent–Child architecture
- Storage implications
- Debugging chunking-related retrieval issues
- Choosing chunking strategies based on business requirements

Status

✔ Confident

---

## ✅ Checkpoint 6 — Embeddings

Can confidently explain:

### Embedding Fundamentals

- Distributional Hypothesis
- Semantic Representation
- Vector Space
- Dense Vector Embeddings
- Why embeddings exist

### Embedding Engineering

- Cosine Similarity
- Euclidean Distance
- Embedding dimensions
- Embedding generation
- Query embeddings vs document embeddings
- Compatible embedding models

### Production Concepts

- Choosing embedding models
- Domain-specific embeddings
- Embedding quality
- Embedding pipelines
- Relationship between chunk quality and embedding quality

### Practical

- Generated embeddings using Sentence Transformers
- Compared embeddings using cosine similarity
- Interpreted embedding tensors
- Built semantic similarity experiments

Status

✔ Confident

---

## ✅ Checkpoint 7 — Vector Databases & Retrieval

Can confidently explain:

### Vector Databases

- Why vector databases exist
- Vector indexing
- Approximate Nearest Neighbor (ANN)
- Exact Nearest Neighbor (ENN)
- IVF
- HNSW
- Similarity search

### Retrieval

- Cosine Similarity
- Top-K Retrieval
- Search depth
- Context dilution
- Recall vs Precision trade-offs

### Production Concepts

- ANN vs ENN
- Choosing similarity metrics
- Choosing Top-K
- Latency vs retrieval quality
- Scaling semantic search

Status

✔ Confident

---

## ✅ Checkpoint 8 — Reranking

Can confidently explain:

### Reranking Fundamentals

- Why rerankers exist
- Bi-Encoder vs Cross-Encoder
- Candidate retrieval
- Query-document interaction

### Production Concepts

- Dynamic routing
- When reranking is useful
- When reranking is unnecessary
- Open-source vs API rerankers
- Cost vs latency vs quality trade-offs

### Engineering Decisions

- Choosing reranker models
- Retrieval confidence
- Query routing
- Business-driven reranking decisions

Status

✔ Confident

---

## ✅ Checkpoint 9 — Retrieval Evaluation

Can confidently explain:

### Offline Evaluation

- Ground-truth datasets
- Evaluation methodology
- Controlled experiments

### Retrieval Metrics

- Precision@K
- Recall@K
- Mean Reciprocal Rank (MRR)
- NDCG

### Production Evaluation

- Offline vs Online Evaluation
- A/B Testing
- User feedback loops
- Evaluation datasets
- Business metrics
- Metric trade-offs

### Engineering Decisions

- Choosing metrics based on product requirements
- Diagnosing retrieval failures
- Measuring retrieval improvements
- Continuous evaluation in production

Status

✔ Confident

---

## ✅ Checkpoint 10 — Generation & Context Engineering

Can confidently explain:

### Prompt Engineering

- Prompt construction
- Prompt templates
- Grounding
- Citation-aware prompting

### Context Engineering

- Context ordering
- Context compression
- Context window management
- Context quality vs quantity

### Conversational RAG

- Conversation memory
- Retrieved context
- Retrieval routing
- Query rewriting

### Production Concepts

- Hallucination reduction
- Response synthesis
- Multi-document generation
- Production prompt pipelines

Status

✔ Confident

---

## ✅ Checkpoint 11 — Hybrid Search

Can confidently explain:

### Retrieval Strategies

- BM25
- Semantic Search
- Hybrid Search
- Score Fusion
- Reciprocal Rank Fusion (RRF)
- Weighted Fusion

### Engineering Decisions

- Lexical vs semantic retrieval
- Choosing retrieval strategies
- Production query patterns
- Fusion trade-offs

Status

✔ Confident

---

## ✅ Checkpoint 12 — Production Engineering

Can confidently explain:

### Production Infrastructure

- Caching
- Cache invalidation
- Logging
- Observability
- Monitoring
- Alerting

### Production Operations

- Production metrics
- Deployment monitoring
- Pipeline debugging
- Knowledge freshness
- Production architecture

### Engineering Decisions

- Data-driven optimization
- Staged rollouts
- Business-driven engineering
- End-to-end production pipeline

Status

✔ Confident

---

# Current Focus

🟡 Production Implementation

Upcoming Topics

- Repository Architecture
- Folder Structure
- Configuration Management
- Environment Setup
- Production Codebase
- Modular Design
- End-to-End Implementation

Status

Ready to Begin

---

# Upcoming Modules

- Production Implementation
- Testing
- Production Optimization
- Deployment
- Capstone Project