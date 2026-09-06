# GitHub Repo Presenter

Apply these instructions when the user asks to make this repository presentable, portfolio-ready, credible, easier to review, or easier to reproduce.

## Scope

Make the repository easy to understand, easy to run, and honest about its maturity. This is a presentation and reproducibility pass, not permission for a broad product rewrite. Preserve unrelated work and existing project conventions.

## Non-negotiable evidence rules

- Inspect `git status --short --branch`, remotes, the top-level tree, the README, and the relevant manifest before editing.
- Never invent URLs, screenshots, metrics, stars, tests, credentials, features, integrations, architecture claims, or deployment status. Label missing evidence as missing or unverified.
- Never commit secrets. Treat `.env`, API keys, tokens, private URLs, dumps, generated credentials, and real user data as sensitive.
- Do not rewrite history, force-push, delete branches, rename the repository, change its license, or alter remote settings without explicit scope.
- Do not add dependencies, remove working behavior, or refactor product code only to make the repository look nicer.
- Use real screenshots and assets only. Never present generated UI as proof of a working feature.

## Workflow

1. Inventory the project: stack, entry points, package manager, runtime, environment variables, commands, deployment links, screenshots, tests, and existing documentation.
2. Classify findings as **Blocking**, **High impact**, or **Polish**.
3. Improve the README in place when possible. Lead with the product promise, verified visual proof, concrete capabilities, engineering decisions, accurate stack, reproducible quick start, architecture, demo path, status and trade-offs, then relevant contribution/security/license links.
4. Improve repository hygiene only when it increases comprehension or reproducibility. Keep docs, assets, scripts, tests, and examples in clear homes. Preserve lockfiles, migrations, seed data, tests, and meaningful generated artifacts.
5. For public-facing work, study relevant high-traction repositories if browsing is available. Borrow patterns, never prose, branding, assets, unsupported claims, or layouts.
6. Verify with `git diff --check`, the existing project checks when available, documented setup when safe, README link/image checks, a secret/placeholder scan, and a focused diff review.

## Decision rule

If the user asks for an audit only, report evidence and stop. If they ask for implementation, make the smallest coherent set of changes that addresses blocking and high-impact gaps. Keep GitHub metadata recommendations separate from local edits and say explicitly when remote settings were not changed.

## Handoff

End with **Implemented**, **Verified**, **Unverified or blocked**, and **Recommended next step**. Use “documented,” “locally verified,” and “unverified” precisely. Do not call the repository portfolio-ready while a blocking claim or reproduction path remains unverified.
