<p align="center">
  <img src="https://raw.githubusercontent.com/plutoframework/pluto/main/assets/readme/banner.svg" alt="Pluto — a small framework, wide open possibilities" width="100%" />
</p>

# Pluto Skills

[Website](https://plutoframework.github.io/pluto-site/) · [Documentation](https://plutoframework.github.io/pluto-site/docs/ai-skills/) · [CLI demo](https://github.com/plutoframework/pluto/blob/main/docs/DEMO.md) · [First issues](https://github.com/plutoframework/pluto/blob/main/CONTRIBUTING.md#starter-tasks)

Short, task-specific guidance for agents building with the Pluto ecosystem.
Each skill contains do/don’t bullets and links to canonical Markdown docs.
No copied manuals, bundled dependencies or install scripts.

## Install

Requires Node.js 22.20+. From your project:

```sh
npx skills add plutoframework/pluto-skills
```

Select the skills and coding agents you use. Installation is project-local by
default; add `-g` for a user-wide installation. Install one skill explicitly:

```sh
npx skills add plutoframework/pluto-skills --skill pluto-api -a codex
```

Pin this collection to a release with
`https://github.com/plutoframework/pluto-skills/tree/v0.3.0`.
Use `npx skills check` to inspect updates and `npx skills update` to apply them.
See the [skills CLI](https://github.com/vercel-labs/skills) for supported agents.

## Choose guidance

| Skill            | Use it for                                                         |
| ---------------- | ------------------------------------------------------------------ |
| pluto-project    | Initialization, config and upgrades                                |
| pluto-api        | Endpoints, operations and domain state                             |
| pluto-security   | Authentication, permissions, tenants and flags                     |
| pluto-data       | SQL, pagination, idempotency, jobs and cache                       |
| pluto-frontend   | React, UI libraries, themes, registries and UI state               |
| pluto-agents     | AI runs, tools and execution authority                             |
| pluto-docs       | READMEs, guides, realistic examples and documentation checks       |
| pluto-maintainer | Framework changes, experience improvements and security validation |

The maintainer skill includes focused implementation, experience and security
references. Load only the reference needed for the task.

Existing project instructions and explicit user choices govern the task.
Installing a skill does not authorize publishing, deployment or paid API calls.

## Agent-readable docs

Start at [docs/llms.txt](https://plutoframework.github.io/pluto-site/docs/llms.txt),
then fetch only the linked `.md` page you need. These are static exports of the
same source as the human docs, with frontmatter removed and links resolved.
Reference pages record their source revision. Check installed versions before
copying a command from newer docs.

## Contribute

Keep each entrypoint under 400 words. Add decision-changing guidance, not a
second manual. Keep links pointed at the relevant Markdown topic.

```sh
python3 scripts/check.py
```

The public repository is installable directly. The skills.sh directory indexes
installation activity; search ranking and indexing timing are external.
