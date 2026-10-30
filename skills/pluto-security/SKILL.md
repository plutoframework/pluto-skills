---
name: pluto-security
description: Integrate Pluto authentication, RBAC, tenant checks and feature flags. Use when changing access control, credential flows or client-visible capabilities.
---

# pluto-security

## Do

- Derive identity and tenant scope from verified server-side authentication.
- Check permissions and resource/tenant ownership in application operations, including calls made outside HTTP.
- Use published Pluto Auth credential flows and the configured Origin, limiter and delivery boundaries.
- Use Core feature evaluation; preserve explicit false overrides and expose only declared client-visible flags in caller context.
- Keep security middleware enabled; apply explicit migrations and test cross-tenant and denied-access cases.

## Don't

- Do not accept roles, tenant authority or permissions from request/model arguments.
- Do not substitute a feature flag or hidden frontend control for authorization.
- Do not cache credential responses, log secrets or store session credentials in browser storage.
- Do not grant business membership during public enrollment or expose development issuance routes in production.

## Docs

Read only the topic needed; match examples to the installed package version.

- [Auth](https://plutoframework.github.io/pluto-site/docs/backend/auth.md)
- [Credentials](https://plutoframework.github.io/pluto-site/docs/backend/credentials.md)
- [RBAC](https://plutoframework.github.io/pluto-site/docs/backend/rbac.md)
- [Flags](https://plutoframework.github.io/pluto-site/docs/backend/features.md)
