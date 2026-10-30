---
name: pluto-project
description: Initialize and configure Pluto applications using the CLI and pluto.toml. Use for project scaffolding, tool setup and ecosystem upgrades.
---

# pluto-project

## Do

- Read `pluto.toml`, local agent instructions and `pluto version` before changing a project.
- Use explicit CLI arguments with `--no-input`; inspect command help and `--dry-run` before generation.
- Persist generator choices in `pluto.toml`; load runtime secrets through the configured environment or secret provider.
- Keep the application environment prefix explicit, uppercase and scoped to the app.
- Run `pluto fmt`, `pluto vet` and the relevant project checks after changes.

## Don't

- Do not overwrite authored files or migrate old scaffold schemas implicitly.
- Do not commit real secrets or assume generated development integrations are production-ready.
- Do not add dependencies when an existing Pluto primitive covers the need.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Setup](https://plutoframework.github.io/pluto-site/docs/getting-started.md)
- [Configuration](https://plutoframework.github.io/pluto-site/docs/configuration.md)
- [Commands](https://plutoframework.github.io/pluto-site/docs/cli/reference.md)
