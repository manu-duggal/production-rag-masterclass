# Engineering Decision Log

> This document records the important engineering decisions made throughout the project.
>
> Every major technical choice should answer:
>
> - What decision was made?
> - Why was it made?
> - What alternatives were considered?
> - What trade-offs were accepted?
>
> This document should evolve together with the project.

---

# Decision 1

## Decision

Build one production-grade project instead of many small demo projects.

### Why

Real engineering projects evolve over time.

Building one system allows us to continuously improve architecture, retrieval quality, evaluation and production readiness.

### Alternatives

- Multiple small tutorial projects

### Trade-offs

Pros

- Much deeper understanding
- Realistic engineering workflow
- Stronger GitHub portfolio
- Easier to discuss in interviews

Cons

- Slower initial progress
- Larger project to maintain

---

# Decision 2

## Decision

Use Git and version control from Day 1.

### Why

Version control is an essential engineering skill.

The repository should show how the system evolved rather than appearing all at once.

### Alternatives

- Build everything locally and upload later

### Trade-offs

Pros

- Professional workflow
- Clear project history
- Easier debugging
- Better collaboration habits

Cons

- Slightly more setup at the beginning

---

# Decision 3

## Decision

Prioritize production engineering over framework-specific tutorials.

### Why

Libraries change.

Engineering principles remain useful.

The goal is to understand why systems are designed in certain ways, not simply how to use a framework.

### Alternatives

- Tutorial-first learning

### Trade-offs

Pros

- Better interview performance
- Stronger problem-solving ability
- Easier adaptation to new tools

Cons

- Slower start
- More conceptual discussions before coding

---

# Future Decisions

This section will grow throughout the project.

Examples include:

- Chunking strategy
- Chunk size
- Embedding model
- Vector database
- Retrieval strategy
- Hybrid Search
- Reranker
- Metadata design
- Prompt template
- Evaluation framework
- Deployment architecture