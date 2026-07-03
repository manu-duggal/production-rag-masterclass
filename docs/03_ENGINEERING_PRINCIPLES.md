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