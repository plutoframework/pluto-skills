---
name: pluto-api
description: Build Pluto API endpoints with route metadata, thin HTTP handlers, operations and explicit state transitions. Use when adding or changing backend features.
---

# pluto-api

## Do

- Inspect the installed CLI, manifest schema and supported contracts before generating. Candidate APIs require explicit candidate dependencies; never invent a released version or silently migrate authored code.
- Use `pluto add endpoint` and canonical declarations. When the installed CLI supports managed gates, Pluto owns gates, entries and registration; authored logic uses private extension points. Otherwise preserve authored files and select an explicit candidate upgrade before relying on required-gate enforcement.
- Keep HTTP, worker and tool entries limited to decoding, trusted caller adaptation, invoking the declared operation and mapping results. Reuse the operation gate across entry paths; do not reproduce its checks in each adapter.
- Operations orchestrate authorization, scoped loading and commits through narrow ports. Domain code owns normalization, validated construction, calculations, resource decisions and lifecycle rules. Data owns persistence; infrastructure adapters own external delivery; composition injects dependencies.
- Use `github.com/plutoframework/pluto-core/state` for explicit domain lifecycles; transitions evaluate facts without I/O.
- Use the project response envelopes and update/check OpenAPI when contracts change.
- Gate unfinished/staged capabilities with `--feature <key>` (default off); evaluate flags server-side before new side effects and test both states. Expose client visibility only when needed.
- Finish code changes with `pluto fmt`, `pluto vet` and relevant tests; fix findings, rerun affected checks and disclose anything not run.
- Test direct operation calls as well as entry adapters. Attempt zero/foreign authority, denied resource access, stale writes, private-method capture and alternate gate implementations; require the intended rejection, not an unrelated error.

## Don't

- Do not move business rules into handlers or make state transitions perform database writes.
- Do not edit managed gates, embed or alias a boundary to replace it, or add an alternate exported business entry point. Repair the owning generator when its supported contract is insufficient.
- Do not treat a successful transition as authorization or persistence; operations still enforce permissions and transactional version checks.
- Do not compress code to evade the 1,000-line source-file ceiling. Follow configured formatting, an 80-column default and blank lines above standalone comment blocks except at file line one.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Endpoint generation](https://plutoframework.github.io/pluto-site/docs/cli/reference.md)
- [Layer responsibilities and enforcement](https://plutoframework.github.io/pluto-site/docs/architecture.md)
- [Feature flags](https://plutoframework.github.io/pluto-site/docs/backend/features.md)
- [Domain state](https://plutoframework.github.io/pluto-site/docs/backend/state.md)
- [Style and testing](https://plutoframework.github.io/pluto-site/docs/conventions.md)
