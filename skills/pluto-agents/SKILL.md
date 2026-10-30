---
name: pluto-agents
description: Build typed Pluto Agent runs and tools with verified dependencies and RBAC. Use when adding AI capabilities or external API tools to a Pluto application.
---

# pluto-agents

## Do

- Use typed run dependencies for verified identity, tenant scope and application services.
- Register tools explicitly; narrow the allowed tool set per run and enforce policy at the execution boundary.
- Call application operations for business actions so RBAC, tenant and resource checks remain effective.
- Wrap external API tools in the same permission/resource boundaries; keep destinations and credentials server-controlled.
- Require host-owned approval and idempotency for writes where the application policy demands them.
- Test with scripted providers and HTTP mocks first; verify denied runs make zero external calls.

## Don't

- Do not let the model select its authority, role, credentials or arbitrary outbound destinations.
- Do not describe token accounting as a hard billing cap or cooperative cancellation as guaranteed interruption.
- Do not promise durable recovery or exactly-once execution from in-memory runs/replay guards.
- Do not make live paid model calls unless the user authorized that test.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Agent API and limits](https://plutoframework.github.io/pluto-site/docs/backend/agents.md)
- [Tool authorization](https://plutoframework.github.io/pluto-site/docs/backend/rbac.md)
- [Telemetry privacy](https://plutoframework.github.io/pluto-site/docs/backend/telemetry.md)
