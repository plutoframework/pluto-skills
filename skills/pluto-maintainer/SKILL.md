---
name: pluto-maintainer
description: Maintain Pluto libraries, generators, examples and documentation. Use for framework bugs, features, UI/UX, developer or agent experience, and scoped security investigation; application feature work uses the application skills.
---

# pluto-maintainer

## Mission

- Make Go APIs and full-stack apps fast to build, explicit to understand and safe by default.
- Prefer standard Go, small dependency surfaces, readable code and typed, testable boundaries.
- Keep framework mechanics in shared primitives; generate application intent and authored extension points.

## Do

- Read the target repository's `AGENTS.md`, checks, published API and relevant docs. Identify affected modules, generators and consumers before editing; change only authorized repositories.
- Reproduce the problem or define observable acceptance criteria. Fix the owning layer, then verify the real consumer path.
- Use the CLI for supported application scaffolding. Maintainers edit generator source/templates directly, then rebuild and exercise the CLI; do not patch generated output to hide generator defects.
- Preserve compatibility and secure defaults. Declare breaking changes, dependency costs and migration needs explicitly.
- Gate unfinished/staged application behavior off by default; test both states. Flags cannot make unsafe migrations or broken public contracts safe to merge.
- Run repository formatters, linters and required checks after the final edit. Report failures, skips and untested boundaries accurately.

- Lead docs with real application wiring; keep simulations in labeled testing sections.

## Read for the task

- [Documentation authoring](https://plutoframework.github.io/pluto-site/docs/maintainers/documentation.md): realistic examples, source checks and publishing.
- [Implementation](references/implementation.md): bugs, features, generator and release validation.
- [Experience](references/experience.md): UI/UX, DX and agent ergonomics.
- [Security](references/security.md): trust boundaries, safe reproduction and evidence.
- [Ecosystem conventions](https://plutoframework.github.io/pluto-site/docs/conventions.md): canonical application rules.

## Don't

- Do not turn a focused task into an ecosystem rewrite or add dependencies without justification.
- Do not bypass lint/tests, overwrite authored code, weaken access checks or invent framework guarantees.
- Do not publish, deploy, disclose vulnerabilities or make paid/live calls without task authorization.
- Do not call a change secure from scanner output, passing tests or self-review alone.
