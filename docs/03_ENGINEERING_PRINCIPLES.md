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
