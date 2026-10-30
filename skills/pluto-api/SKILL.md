---
name: pluto-api
description: Build Pluto API endpoints with route metadata, thin HTTP handlers, operations and explicit state transitions. Use when adding or changing backend features.
---

# pluto-api

## Do

- Use `pluto add endpoint` to create endpoints; do not hand-assemble route registration, models and metadata. Keep route names, descriptions, paths and permissions in the generated path metadata.
- Keep grouped handlers limited to decoding, transport validation, calling operations and response mapping.
- Put business rules in operations/domain code behind small consumer-owned interfaces.
- Use `github.com/plutoframework/pluto-core/state` for explicit domain lifecycles; transitions evaluate facts without I/O.
- Use the project response envelopes and update/check OpenAPI when contracts change.
- Gate unfinished/staged capabilities with `--feature <key>` (default off); evaluate flags server-side before new side effects and test both states. Expose client visibility only when needed.
- Finish code changes with `pluto fmt`, `pluto vet` and relevant tests; fix findings, rerun affected checks and disclose anything not run.
- Test operations independently; cover HTTP parsing and meaningful transition/guard failures separately.

## Don't

- Do not move business rules into handlers or make state transitions perform database writes.
- Do not treat a successful transition as authorization or persistence; operations still enforce permissions and transactional version checks.
- Do not compress code to evade the 1,000-line source-file ceiling. Follow configured formatting, an 80-column default and blank lines above standalone comment blocks except at file line one.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Endpoint generation](https://plutoframework.github.io/pluto-site/docs/cli/reference.md)
- [Feature flags](https://plutoframework.github.io/pluto-site/docs/backend/features.md)
- [Domain state](https://plutoframework.github.io/pluto-site/docs/backend/state.md)
- [Style and testing](https://plutoframework.github.io/pluto-site/docs/conventions.md)
