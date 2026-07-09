# Engineering Principles

> This document contains the engineering principles discovered throughout the Production RAG Masterclass.
>
> These are not textbook definitions.
>
> They are practical rules that guide engineering decisions when building production AI systems.
>
> This document grows throughout the course.

---

# Knowledge Engineering

## Principle 1

Always retrieve information from the system that owns it.

Example:

- Bank balance → Banking Database
- Flight status → Airline API
- Employee leave balance → HR System

Never duplicate live data inside a vector database.

---

## Principle 2

RAG is not a replacement for databases.

Use RAG for unstructured knowledge.

Use SQL or APIs for structured, transactional data.

---

## Principle 3

The LLM is a reasoning engine, not a database.

The model's job is to understand, reason and generate.

It should not become the source of truth.

---

## Principle 4

Separate stable knowledge from dynamic knowledge.

Stable knowledge belongs inside the model.

Dynamic knowledge should be retrieved.

---

## Principle 5

The source of truth should always remain the source of truth.

Never copy live business data into multiple systems unless there is a strong engineering reason.

---

# Retrieval Engineering

## Principle 6

More indexed data does not automatically produce a better RAG system.

Quality is usually more important than quantity.

---

## Principle 7

Garbage In → Garbage Out.

Poor documents create poor retrieval.

Poor retrieval creates poor answers.

---

## Principle 8

Knowledge curation is part of retrieval quality.

A production engineer spends significant time deciding what should NOT be indexed.

---

## Principle 9

Retrieval without authorization is a security bug.

Just because a document can be retrieved does not mean every user should see it.

---

# Learning Principles

## Principle 10

Understand why before learning how.

Frameworks change.

Engineering principles last.

---

## Principle 11

Optimize for understanding, not memorization.

If the reasoning is understood, implementation becomes much easier.

---

## Principle 12

Document processing happens before user interaction.

Documents should be parsed, cleaned, chunked and embedded before users start querying the system.

---

## Principle 13

A document is not searchable until it has been successfully indexed.

Uploading a document does not immediately make it retrievable.

---

## Principle 14

Every optimization introduces a trade-off.

Preprocessing improves query speed but introduces challenges such as storage, index freshness and re-indexing.

---

## Principle 15

Separate data acquisition from data processing.

The loader acquires data from the source.
The parser converts it into a machine-readable representation.

---

## Principle 16

Parsing quality directly affects retrieval quality.

Poor parsing leads to poor chunking, poor embeddings and poor retrieval.

---

## Principle 17

Not every PDF requires OCR.

Run OCR only when the document does not contain extractable text.

---

## Principle 18

Never destroy information during ingestion unless you intentionally choose to.

Preserve the raw data whenever possible.

---

## Principle 19

Avoid unnecessary format conversions.

Whenever possible, parse the original document format instead of converting it to another format first.

---

## Principle 20

Every unnecessary token occupies context that could contain useful information.

---

## Principle 21

A clean index retrieves better than a large index.

---

## Principle 22

Indexes should evolve incrementally rather than being rebuilt unnecessarily.

---

## Principle 23

Use stable identifiers instead of human-readable names whenever possible.

---

## Principle 24

Metadata should guide retrieval, not influence semantic meaning.

---

# Chunking

## Principle 25

Chunking is an information retrieval problem, not merely a text splitting problem.

The objective is to maximize retrieval quality while preserving enough context for generation.

---

## Principle 26

The quality of retrieval can never exceed the quality of the chunks.

Poor chunk boundaries produce poor embeddings, poor retrieval and ultimately poor answers.

---

## Principle 27

Chunk boundaries should preserve semantic meaning whenever possible.

Prefer splitting on meaningful boundaries such as sections, paragraphs, functions or conversations instead of arbitrary token counts.

---

## Principle 28

The chunk is the atomic unit of retrieval.

Everything downstream—including embeddings, retrieval and generation—depends on the quality of the chunk.

---

## Principle 29

Chunk boundaries should avoid breaking semantic units whenever possible.

Sentences, paragraphs, tables, functions and conversations should remain intact whenever practical.

---

## Principle 30

The simplest solution is often sufficient, provided it satisfies the business requirements.

Do not introduce complex chunking strategies until simpler approaches prove insufficient.

---

## Principle 31

Chunk size is a business decision as much as a technical decision.

The optimal chunk size depends on document structure, query patterns, latency requirements, cost and retrieval quality.

---

## Principle 32

Always preserve the highest level of semantic structure possible.

Prefer sections over paragraphs, paragraphs over sentences and sentences over individual words whenever size constraints allow.

---

## Principle 33

Recursive chunking preserves document structure, not true semantic understanding.

It follows separators and formatting rather than comprehending the underlying meaning.

---

## Principle 34

The semantic unit depends on the document type.

For example:

- HR Policy → Section
- Source Code → Function/Class
- FAQ → Question–Answer Pair
- Chat → Conversation
- Research Paper → Section/Subsection

---

## Principle 35

Semantic similarity is often a better chunk boundary than formatting.

Documents with weak structure may benefit from meaning-aware chunk boundaries.

---

## Principle 36

Document structure itself carries valuable information.

Well-designed headings, sections and formatting often represent business logic that should be preserved.

---

## Principle 37

Overlap preserves local context across chunk boundaries.

Its purpose is to reduce information loss when concepts span adjacent chunks.

---

## Principle 38

Overlap is a trade-off between context preservation and redundancy.

Increasing overlap improves local context but also increases storage, indexing cost and duplicate retrieval.

---

## Principle 39

Overlap improves good chunking but cannot rescue poor chunking.

If chunk boundaries are fundamentally wrong, increasing overlap is rarely the correct solution.

---

## Principle 40

Overlap should preserve context, not create redundancy.

Use only enough overlap to bridge neighboring chunks without overwhelming retrieval with duplicate information.

---

## Principle 41

Retrieve with focused chunks and generate with richer context.

Small chunks improve retrieval precision while larger contexts improve answer quality.

---

## Principle 42

Relationships between chunks are as important as the chunks themselves.

Parent–Child chunking preserves document hierarchy and enables better retrieval-generation trade-offs.

---

## Principle 43

Vector databases are optimized for semantic retrieval, not as the primary source of truth.

Store embeddings in the vector database while preserving original documents in an appropriate storage system.

---

## Principle 44

Sliding windows increase the probability that important information appears completely within at least one chunk.

They improve coverage but do not guarantee perfect retrieval.

---

## Principle 45

Stride controls the balance between coverage and redundancy.

Smaller strides improve coverage while increasing duplicate information and storage cost.

---

## Principle 46

Chunk size is a balance between retrieval precision and generation context.

Small chunks improve precision.
Large chunks improve context.

Neither is universally better.

---

## Principle 47

Chunking should adapt to the data rather than forcing the data into arbitrary boundaries.

Different document types require different chunking strategies.

---

## Principle 48

Never optimize before identifying the bottleneck.

Inspect retrieved chunks, boundaries, overlap and retrieval behavior before modifying the chunking strategy.

---

# Embedding Engineering

## Principle 49

Embeddings represent semantic meaning, not keywords.

Documents with similar meanings should be located close together in the vector space even if they share few or no common words.

---

## Principle 50

Embedding quality depends on chunk quality.

A coherent chunk produces a more meaningful embedding than a chunk containing unrelated topics.

---

## Principle 51

Embedding models learn meaning from context rather than predefined rules.

Semantic relationships emerge from observing how words and phrases appear together across large corpora.

---

## Principle 52

Similarity should be measured using the metric for which the embedding model was designed.

Using an incompatible similarity metric can significantly reduce retrieval quality.

---

## Principle 53

Vector dimensionality alone does not determine embedding quality.

Higher-dimensional embeddings increase representation capacity but do not automatically produce better semantic understanding.

---

## Principle 54

Query and document embeddings must be generated using compatible embedding models.

Embeddings from different models should not be compared directly.

---

## Principle 55

Embedding generation belongs to the ingestion pipeline whenever possible.

Generate document embeddings once and reuse them during retrieval to minimize query latency.

---

## Principle 56

Embedding models compress semantic information rather than storing complete document meaning.

An embedding captures the dominant semantics of its input but cannot preserve every detail.

---

# Vector Search

## Principle 57

Vector databases optimize retrieval speed through indexing rather than exhaustive comparison.

Efficient indexing enables semantic search to scale to millions of embeddings.

---

## Principle 58

Approximate Nearest Neighbor search trades a small amount of retrieval accuracy for significant improvements in search latency.

The trade-off should be chosen according to business requirements.

---

## Principle 59

Exact Nearest Neighbor search is appropriate when retrieval accuracy is more important than latency.

Examples include medical, legal and other high-risk applications.

---

## Principle 60

The choice of Top-K is a balance between recall, precision, latency and context size.

Retrieving more documents is not always better.

---

## Principle 61

Higher Top-K increases the candidate pool but also increases context dilution, token usage and computational cost.

---

## Principle 62

Cosine similarity measures semantic alignment rather than vector magnitude.

For most modern embedding models, direction is more informative than length.

---

## Principle 63

Index configuration should be evaluated together with embedding quality.

Poor retrieval is not always caused by the embedding model.

---

## Principle 64

Search quality should be evaluated before increasing infrastructure complexity.

Measure retrieval performance before introducing more sophisticated indexing or reranking techniques.

---

# Reranking

## Principle 65

Bi-encoders optimize retrieval efficiency by encoding queries and documents independently.

Their primary strength is scalability.

---

## Principle 66

Cross-encoders optimize retrieval quality by evaluating the query and document together.

Their primary strength is relevance estimation.

---

## Principle 67

Cross-encoder relevance scores are query-dependent and therefore cannot be precomputed.

---

## Principle 68

Rerankers improve the ordering of retrieved candidates.

They cannot recover documents that were never retrieved.

---

## Principle 69

The effectiveness of a reranker depends on the quality of the candidate set it receives.

Poor retrieval cannot be fully corrected by reranking.

---

## Principle 70

Reranking should be introduced only when measurable improvements justify the additional latency and operational cost.

---

## Principle 71

Production systems should adapt retrieval pipelines to query complexity whenever practical.

Simple queries do not always require reranking.

---

## Principle 72

Retrieval confidence can guide dynamic routing decisions.

When retrieval confidence is already high, additional reranking may provide little benefit.

---

## Principle 73

Infrastructure decisions should be driven by production constraints rather than benchmark rankings alone.

Latency, privacy, scalability and operational complexity are as important as model accuracy.

---

# Retrieval Evaluation

## Principle 74

Retrieval quality should be measured using objective evaluation metrics rather than subjective impressions.

---

## Principle 75

Evaluation requires a trusted ground-truth dataset.

Without reliable relevance labels, retrieval metrics have limited meaning.

---

## Principle 76

Compare retrieval systems using identical evaluation datasets and identical evaluation conditions.

---

## Principle 77

Each retrieval metric measures a different aspect of system quality.

Precision, Recall, MRR and NDCG should be interpreted together rather than in isolation.

---

## Principle 78

Offline evaluation measures retrieval quality.

Online evaluation measures user impact.

Both are necessary for production systems.

---

## Principle 79

Production deployments should follow a staged evaluation process.

Offline validation should precede controlled rollout and online monitoring.

---

## Principle 80

User interactions are one of the most valuable sources of future evaluation data.

Production feedback should continuously improve the evaluation dataset.

---

## Principle 81

Improving one retrieval metric may reduce another.

Optimization should always be guided by business objectives rather than individual metric values.

---

## Principle 82

Evaluate one pipeline component at a time whenever possible.

Changing multiple components simultaneously makes root-cause analysis significantly more difficult.

---

## Principle 83

Business success is the final evaluation metric.

Strong retrieval metrics are valuable only when they improve the user experience and business outcomes.

---

# Generation Engineering

## Principle 84

Generation quality depends on retrieval quality.

The LLM cannot reliably compensate for missing or irrelevant context.

---

## Principle 85

The quality of generated answers depends more on the quality of the provided context than the size of the context.

More context is not always better.

---

## Principle 86

Conversation memory preserves dialogue.

Retrieved context provides external knowledge.

Both solve different engineering problems.

---

## Principle 87

Retrieve only when additional external knowledge is required.

Reuse conversation memory whenever it already contains sufficient information.

---

## Principle 88

Conversation history should be managed with the same discipline as retrieved context.

Long conversations can also cause context dilution.

---

## Principle 89

Context ordering influences reasoning quality.

Present related information in a logical order whenever possible.

---

## Principle 90

Context compression should remove irrelevant information without changing the meaning of the original content.

---

## Principle 91

Grounding is a prompt design problem as much as a retrieval problem.

The model should clearly understand that retrieved knowledge is the source of truth.

---

## Principle 92

Prompt templates should be centralized rather than duplicated across the application.

Updating one template should improve the behavior of the entire system.

---

## Principle 93

Conversation state and retrieved knowledge should complement each other rather than replace one another.

---

## Principle 94

Query rewriting should preserve the user's intent while making the retrieval query more explicit.

---

## Principle 95

Query rewriting should clarify ambiguity rather than introduce new assumptions.

---

## Principle 96

Not every user query benefits from query rewriting.

Rewrite only when it improves retrieval quality.

---

# Hybrid Search

## Principle 97

Semantic search and lexical search solve different retrieval problems.

Neither is universally better.

---

## Principle 98

Exact identifiers such as error codes, IDs and function names are often better handled through lexical matching.

---

## Principle 99

Hybrid search combines complementary retrieval signals instead of replacing one retrieval method with another.

---

## Principle 100

Retrieval strategies should reflect the distribution of production queries rather than theoretical capabilities.

---

## Principle 101

Retrieval scores produced by different algorithms are not directly comparable without an appropriate fusion strategy.

---

## Principle 102

Score fusion should produce a unified candidate set before reranking performs fine-grained relevance optimization.

---

## Principle 103

Fusion weights should be tuned using production evaluation rather than arbitrary defaults.

---

# Production Engineering

## Principle 104

Cache deterministic computations whenever the cost of recomputation exceeds the cost of storing the result.

---

## Principle 105

Frequently repeated and stable queries provide the greatest benefit from caching.

---

## Principle 106

Caching should occur as early in the pipeline as possible to avoid unnecessary downstream computation.

---

## Principle 107

Knowledge updates should invalidate dependent caches as soon as possible.

Event-driven invalidation is generally preferable when knowledge changes can be detected.

---

## Principle 108

Logs record what happened.

Observability explains why it happened.

---

## Principle 109

Metrics reveal system-wide trends.

Logs explain individual requests.

Both are required for effective production debugging.

---

## Principle 110

Every major stage of the pipeline should expose sufficient metrics and logs for debugging and performance analysis.

---

## Principle 111

Monitoring should detect production problems before users report them.

---

## Principle 112

Production monitoring should include technical metrics, retrieval metrics and user-experience metrics.

---

## Principle 113

Alert thresholds should represent meaningful deviations rather than normal operational variation.

---

## Principle 114

Knowledge freshness is a production metric.

A system can be technically healthy while serving outdated information.

---

## Principle 115

Deployment metadata is valuable during debugging.

Many production regressions originate from configuration or deployment changes rather than algorithmic failures.

---

## Principle 116

Every production optimization should justify its operational cost through measurable improvements in system quality or user experience.

---

## Principle 117

Engineering decisions should be guided by measurable evidence rather than intuition.

Use evaluation metrics, logs, monitoring and user feedback to identify the real bottleneck before optimizing.

---

## Principle 118

Improve one pipeline component at a time whenever possible.

Isolating changes makes root-cause analysis significantly easier.

---

## Principle 119

Production improvements should be validated through controlled rollouts before full deployment.

---

## Principle 120

The quality of a production RAG system is determined by the quality of the entire pipeline rather than the language model alone.