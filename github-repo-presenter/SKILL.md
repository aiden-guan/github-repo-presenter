---
name: github-repo-presenter
description: Audit and polish a GitHub repository so its README, project structure, developer docs, and proof of work are clear, credible, and portfolio-ready. Use when a user wants a vibecoded or unfinished repo made presentable for a portfolio, showcase, hiring review, or public release; do not use for broad code rewrites or changing GitHub account settings.
---

# GitHub Repo Presenter

Make the repository easy to understand, easy to run, and honest about its maturity. Optimize for the first minute of a portfolio review while preserving enough technical depth for an engineer to verify the work.

## Guardrails

- Inspect the worktree before editing. Preserve unrelated dirty changes, existing conventions, and the user's project structure unless a move is clearly necessary and in scope.
- Never invent a live URL, screenshot, testimonial, usage metric, star count, test result, credential, feature, integration, or architecture claim. If evidence is missing, label it as missing or unverified.
- Do not commit secrets. Treat `.env`, API keys, tokens, private URLs, database dumps, generated credentials, and real user data as sensitive. Create or update `.env.example` only with safe placeholders derived from the code.
- Do not rewrite Git history, force-push, delete branches, rename the repository, change its license, or alter remote GitHub settings unless the user explicitly requests that exact action.
- Keep portfolio polish separate from product changes. Do not remove working behavior, add dependencies, or refactor application code only to make the repository look nicer.
- Use real product captures and assets. Never generate a fake UI screenshot and present it as proof of a working feature.
- Badges are optional. Add only badges whose target, meaning, and status are real and maintainable; a badge wall is not evidence of quality.

## Start with an evidence pass

1. Resolve the target repository root and inspect `git status --short --branch`, the current branch, remotes, and the top-level tree.
2. Run the read-only inventory when available:

   ```bash
   python3 /path/to/github-repo-presenter/scripts/audit_repo.py .
   ```

   Use `--json` when a machine-readable inventory is useful. The script is a gap finder, not a quality verdict.
3. Identify the actual project type, entry points, package manager, runtime versions, environment variables, test/lint/build commands, deployment URLs, screenshots, and existing docs. Read the relevant manifest and existing README before proposing replacement text.
4. Separate findings into:
   - **Blocking**: a visitor cannot tell what the project is, cannot start it, or would be misled by a broken or false claim.
   - **High impact**: missing visual proof, missing reproducible setup, unexplained architecture, unsafe environment guidance, or confusing repository clutter.
   - **Polish**: hierarchy, link labels, spacing, metadata suggestions, social preview, and optional badges.

If the user asks for an audit only, stop after the evidence-backed report. If they ask to make the repo presentable, implement the smallest coherent set of changes that addresses the blocking and high-impact gaps.

## Use benchmarks without copying them

For a public-facing or portfolio pass, review two or more relevant benchmark repositories when browsing is available. Prefer projects in the same category or stack, and look at their rendered README and repository surface—not just their source code. Start with [references/benchmark-repos.md](references/benchmark-repos.md), which records high-traction examples and the patterns worth borrowing.

Extract patterns such as:

- a one-sentence product promise before implementation detail;
- a real demo, screenshot, GIF, video, or integration proof near the top;
- separate paths for users, self-hosters, contributors, and maintainers;
- a short, accurate technology/architecture explanation;
- setup commands that are specific enough to reproduce;
- visible contribution, license, security, and support paths where the project actually needs them.

Do not copy prose, branding, assets, layout, or unsupported claims. Stars and forks are time-sensitive signals, not a target or a substitute for proof that the user's project works.

## The portfolio-ready README

Rewrite the existing README in place when possible. Keep the first screen concise and move long instructions to `docs/` only when the project benefits from a separate guide.

Use this order when it fits the project:

1. **Identity** — project name, a plain-language value proposition, and one or two verified links such as Demo, Docs, or API reference.
2. **Visual proof** — a real screenshot, short recording, diagram, or terminal example. Use descriptive alt text and repository-relative paths. If no proof exists, say so and place the gap in the handoff rather than inventing one.
3. **What it does** — three to six concrete capabilities framed around user outcomes, not vague framework slogans.
4. **Why it is interesting** — the important engineering decisions, constraints, integrations, data flow, performance work, or security properties that the author can explain.
5. **Built with** — a compact list of technologies actually found in the repository, grouped by role. Explain unusual choices; do not list every transitive dependency.
6. **Quick start** — prerequisites, install command, environment setup, database/seed steps, dev command, and the commands used to verify the project. Reproduce these commands locally when feasible. Mark anything not run as unverified.
7. **How it works** — an architecture diagram or concise flow for projects with multiple services, auth, payments, queues, AI, or a non-obvious data model. Do not add a diagram that the source cannot support.
8. **Demo path** — safe demo credentials, seed data, a test account, or a short walkthrough only when the user supplied or verified it. Never expose real credentials.
9. **Status, trade-offs, and limits** — distinguish prototype, active project, deployed app, and production-ready claims. Include known limitations and sensible next steps when they help a reviewer understand scope.
10. **Contributing, support, security, and license** — link to the files or channels that exist. Add community files only when the project is intended to receive outside contributions and the owner can maintain them.

For a personal showcase, add a short `Engineering notes` or `Decisions and trade-offs` section if it helps demonstrate understanding. It should explain decisions the author can defend, not inflate the technology list. If AI-assisted development is relevant, disclose it briefly and keep human-verified design, testing, and trade-offs visible.

## Repository hygiene

Make only changes that improve comprehension or reproducibility:

- Keep the root focused on the entry points a visitor needs. Prefer `docs/`, `assets/`, `scripts/`, `tests/`, and `examples/` for material that has a clear home.
- Fix obvious README links, image paths, heading hierarchy, code fences, and command formatting.
- Add or improve a truthful `.gitignore` for the detected stack. Do not ignore source files or hide meaningful project artifacts.
- Add `.env.example` only when the application uses environment variables and the required names can be confirmed from code or existing documentation. Include comments for where values come from, not real values.
- Preserve lockfiles, migrations, tests, seed data, and configuration that are part of the project's actual workflow.
- Add `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue templates, or CI only when the repository's audience and maintenance capacity justify them. Do not create empty or ceremonial files.
- Do not delete generated files or restructure directories just because they look untidy. Flag tracked build output, logs, large binaries, and secrets for explicit cleanup when the target is not unambiguous.
- Prefer documenting an existing command over inventing a new script. If a small script addition is necessary, verify it and explain the behavior change.

For GitHub-hosted projects, keep local edits distinct from remote presentation settings. A separate handoff may recommend a concise repository description, a homepage/demo URL, lower-case hyphenated topics, a social preview image, and profile pins. Do not claim those settings changed unless they were actually updated and read back.

Read [references/github-surfaces.md](references/github-surfaces.md) for the current GitHub-facing checklist and limits.

## Verify before calling it presentable

Run the least expensive checks that prove the edits are safe and useful:

- `git diff --check` for whitespace errors;
- the project's existing lint, typecheck, test, build, or validation commands when available;
- the documented install/start path when it can be run without credentials or destructive data changes;
- local existence of every README image and relative link target;
- a search for accidental secrets, real credentials, private hostnames, and placeholder text left in public-facing files;
- `git status --short` and a focused diff review.

Do not report a deployment, live demo, authenticated flow, external integration, or security property as verified unless it was tested through that path. A clean README and a passing local build prove less than a working deployed product.

## Handoff format

End with four short sections:

- **Implemented** — files changed and the user-visible improvement;
- **Verified** — commands or observations that actually passed;
- **Unverified or blocked** — missing URLs, credentials, deployment access, remote settings, or checks that could not be run;
- **Recommended next step** — the highest-leverage remaining action, if any.

Use language such as “documented,” “locally verified,” “observed,” and “unverified” precisely. Do not call a repository “portfolio-ready” while a blocking claim or reproduction path remains unverified.
