---
name: pluto-docs
description: Write and review Pluto READMEs, guides and examples using published APIs, realistic integrations and executable source. Use for ecosystem documentation authoring and maintenance.
---

# pluto-docs

## Do

- Read the [authoring guide](https://plutoframework.github.io/pluto-site/docs/maintainers/documentation.md) and the owning repository's instructions.
- Lead with actual application usage and the real adapter. State prerequisites, supported versions and application-owned wiring.
- Keep authorization, tenant boundaries, transaction ownership and failure handling visible.
- Use local data to teach pure primitives; use real integration code to teach external capabilities.
- Label excerpts and link complete source. Check copied snippets against that source.
- Put scripted providers, mock transports and fixture sessions in labeled testing sections after the application example.
- Run affected formatters, linters and docs checks. Compile examples against published pins; test adapters with controlled transports when live calls are unnecessary.
- Update the source repository before refreshing site snapshots. Verify Markdown exports and links.
- Report separately what compiled, what ran against mocks and what reached a real service.

## Don't

- Do not present canned output as inference, printed success as delivery or fixture issuance as a login flow.
- Do not remove deterministic tests or require paid calls for docs CI.
- Do not invent APIs, imply unfinished scaffolding works or hide required callbacks.
- Do not copy manuals into skills, expose secrets or infer permission to publish or make live calls.
