---
name: pluto-api
description: Build Pluto API endpoints with route metadata, thin HTTP handlers, operations and explicit state transitions. Use when adding or changing backend features.
---

# pluto-api

## Do

- Scaffold through `pluto add endpoint`; keep route names, descriptions, paths and permissions in the generated path metadata.
- Keep grouped handlers limited to decoding, transport validation, calling operations and response mapping.
- Put business rules in operations/domain code behind small consumer-owned interfaces.
- Use `github.com/plutoframework/pluto-core/state` for explicit domain lifecycles; transitions evaluate facts without I/O.
- Use the project response envelopes and update/check OpenAPI when contracts change.
- Test operations independently; cover HTTP parsing and meaningful transition/guard failures separately.

## Don't

- Do not move business rules into handlers or make state transitions perform database writes.
- Do not treat a successful transition as authorization or persistence; operations still enforce permissions and transactional version checks.
- Do not compress code to evade the 1,000-line source-file ceiling. Follow configured formatting, an 80-column default and blank lines above standalone comment blocks except at file line one.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Endpoint generation](https://plutoframework.github.io/pluto-site/docs/cli/reference.md)
- [Domain state](https://plutoframework.github.io/pluto-site/docs/backend/state.md)
- [Style and testing](https://plutoframework.github.io/pluto-site/docs/conventions.md)
