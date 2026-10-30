---
name: pluto-data
description: Implement Pluto persistence, pagination, idempotency, jobs and cache boundaries. Use for SQL-backed operations, retries and background delivery.
---

# pluto-data

## Do

- Use PostgreSQL and sqlc query boundaries; include tenant predicates in every scoped read/write.
- Commit business changes, expected-version checks, durable audit records and outbox enqueue in the same transaction when required.
- Use Core bounded pagination and bind cursors to the query context.
- Use the same-transaction idempotency API when a business write and replay completion must be atomic.
- Make job handlers safe under at-least-once delivery; scope cache keys by app, environment and tenant.
- Test transaction rollback, competing writes, duplicate delivery and tenant isolation with real backing services where relevant.

## Don't

- Do not use a cursor, cache entry or idempotency key as authorization.
- Do not claim generic HTTP replay capture is atomic with the business write, or jobs provide exactly-once delivery.
- Do not use memory stores as durable production storage or silently retry uncertain writes without reconciliation.
- Do not make a cache authoritative for sessions, permissions or business correctness.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Core data primitives](https://plutoframework.github.io/pluto-site/docs/backend/core.md)
- [Jobs and outbox](https://plutoframework.github.io/pluto-site/docs/backend/jobs.md)
- [Concurrent transitions](https://plutoframework.github.io/pluto-site/docs/backend/state.md)
