# GitHub Repo Presenter

Use this playbook when a user asks to make a repository presentable, portfolio-ready, credible, easier to review, or easier to reproduce. It is tool-neutral: apply it from any coding agent, IDE, CLI, or chat interface.

## Outcome

Make the repository easy to understand, easy to run, and honest about its maturity. Optimize for the first minute of a portfolio review while preserving enough technical depth for an engineer to verify the work.

This is a presentation and reproducibility pass, not permission for a broad product rewrite. Work on the target repository, not on this toolkit, unless the user explicitly asks to improve the toolkit itself.

## Guardrails

- Inspect the worktree before editing. Preserve unrelated dirty changes, existing conventions, and the user's project structure unless a move is clearly necessary and in scope.
- Never invent a live URL, screenshot, testimonial, usage metric, star count, test result, credential, feature, integration, or architecture claim. If evidence is missing, label it missing or unverified.
- Do not commit secrets. Treat `.env`, API keys, tokens, private URLs, database dumps, generated credentials, and real user data as sensitive. Create or update `.env.example` only with safe placeholders derived from the code.
- Do not rewrite Git history, force-push, delete branches, rename the repository, change its license, or alter remote settings unless the user explicitly requests that exact action.
- Keep portfolio polish separate from product changes. Do not remove working behavior, add dependencies, or refactor application code only to make the repository look nicer.
- Use real product captures and assets. Never generate a fake UI screenshot and present it as proof of a working feature.
- Badges are optional. Add only badges whose target, meaning, and status are real and maintainable; a badge wall is not evidence of quality.

## Evidence pass

1. Resolve the target repository root. Inspect `git status --short --branch`, the current branch, remotes, and the top-level tree.
2. If this toolkit is available, run the read-only inventory:

   ```bash
   python3 /path/to/github-repo-presenter/scripts/audit_repo.py .
   ```

   Use `--json` when a machine-readable inventory helps. The script is a gap finder, not a quality verdict.
3. Identify the actual project type, entry points, package manager, runtime versions, environment variables, test/lint/build commands, deployment URLs, screenshots, and existing docs. Read the relevant manifest and README before proposing replacement text.
4. Separate findings into:

   - **Blocking** — a visitor cannot tell what the project is, cannot start it, or would be misled by a broken or false claim.
   - **High impact** — missing visual proof, missing reproducible setup, unexplained architecture, unsafe environment guidance, or confusing repository clutter.
   - **Polish** — hierarchy, link labels, spacing, metadata suggestions, social preview, and optional badges.

If the user asks for an audit only, stop after the evidence-backed report. If the user asks to make the repo presentable, implement the smallest coherent set of changes that addresses blocking and high-impact gaps.

## Benchmarks without imitation

For a public-facing or portfolio pass, review two or more relevant benchmark repositories when browsing is available. Prefer projects in the same category or stack, and inspect their rendered README and repository surface—not just their source code. Start with [references/benchmark-repos.md](references/benchmark-repos.md) when it is available.

Extract patterns such as:

- a one-sentence product promise before implementation detail;
- a real demo, screenshot, GIF, video, diagram, or terminal example near the top;
- separate paths for users, self-hosters, contributors, and maintainers;
- a short, accurate technology and architecture explanation;
- setup commands specific enough to reproduce;
- visible contribution, license, security, and support paths where the project actually needs them.

Do not copy prose, branding, assets, layout, or unsupported claims. Stars and forks are time-sensitive signals, not a target or a substitute for proof that the user's project works.

## README structure

Rewrite the existing README in place when possible. Keep the first screen concise and move long instructions to `docs/` only when the project benefits from a separate guide.

Use this order when it fits the project:

1. **Identity** — project name, plain-language value proposition, and one or two verified links such as Demo, Docs, or API reference.
2. **Visual proof** — real screenshot, short recording, diagram, or terminal example. Use descriptive alt text and repository-relative paths. If no proof exists, say so and record the gap in the handoff rather than inventing one.
3. **What it does** — three to six concrete capabilities framed around user outcomes, not vague framework slogans.
4. **Why it is interesting** — engineering decisions, constraints, integrations, data flow, performance work, or security properties that the author can explain.
5. **Built with** — compact list of technologies actually found in the repository, grouped by role. Explain unusual choices; do not list every transitive dependency.
6. **Quick start** — prerequisites, install command, environment setup, database or seed steps, dev command, and verification commands. Reproduce these commands locally when feasible and mark anything not run as unverified.
7. **How it works** — architecture diagram or concise flow for projects with multiple services, auth, payments, queues, AI, or a non-obvious data model. Do not add a diagram the source cannot support.
8. **Demo path** — safe demo credentials, seed data, test account, or short walkthrough only when the user supplied or verified it. Never expose real credentials.
9. **Status, trade-offs, and limits** — distinguish prototype, active project, deployed app, and production-ready claims. Include known limitations and sensible next steps when they help a reviewer understand scope.
10. **Contributing, support, security, and license** — link to files or channels that exist. Add community files only when the repository's audience and maintenance capacity justify them.

For a personal showcase, add a short `Engineering notes` or `Decisions and trade-offs` section when it demonstrates understanding. Explain decisions the author can defend; do not inflate the technology list. If AI-assisted development is relevant, disclose it briefly and keep human-verified design, testing, and trade-offs visible.

## Repository hygiene

Make only changes that improve comprehension or reproducibility:

- Keep the root focused on the entry points a visitor needs. Prefer `docs/`, `assets/`, `scripts/`, `tests/`, and `examples/` for material that has a clear home.
- Fix obvious README links, image paths, heading hierarchy, code fences, and command formatting.
- Add or improve a truthful `.gitignore` for the detected stack. Do not ignore source files or hide meaningful artifacts.
- Add `.env.example` only when environment variables are confirmed from code or existing docs. Include comments for where values come from, not real values.
- Preserve lockfiles, migrations, tests, seed data, and configuration that are part of the actual workflow.
- Add `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue templates, or CI only when the audience and maintenance capacity justify them. Do not create empty ceremonial files.
- Do not delete generated files or restructure directories just because they look untidy. Flag tracked build output, logs, large binaries, and secrets for explicit cleanup when the target is not unambiguous.
- Prefer documenting an existing command over inventing a new script. If a small script addition is necessary, verify it and explain the behavior change.

For GitHub-hosted projects, keep local edits distinct from remote presentation settings. A handoff may recommend a concise repository description, homepage or demo URL, lower-case hyphenated topics, social preview image, and profile pins. Do not claim those settings changed unless they were actually updated and read back.

## Verification

Run the least expensive checks that prove the edits are safe and useful:

- `git diff --check` for whitespace errors;
- the project's existing lint, typecheck, test, build, or validation commands when available;
- the documented install or start path when it can run without credentials or destructive data changes;
- local existence of every README image and relative link target;
- a search for accidental secrets, real credentials, private hostnames, and placeholder text left in public-facing files;
- `git status --short` and a focused diff review.

Do not report a deployment, live demo, authenticated flow, external integration, or security property as verified unless it was tested through that path. A clean README and a passing local build prove less than a working deployed product.

## Handoff

End with four short sections:

- **Implemented** — files changed and the user-visible improvement;
- **Verified** — commands or observations that actually passed;
- **Unverified or blocked** — missing URLs, credentials, deployment access, remote settings, or checks that could not be run;
- **Recommended next step** — the highest-leverage remaining action, if any.

Use “documented,” “locally verified,” “observed,” and “unverified” precisely. Do not call a repository portfolio-ready while a blocking claim or reproduction path remains unverified.
