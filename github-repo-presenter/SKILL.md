---
name: github-repo-presenter
description: Audit and polish a repository so its README, project structure, developer docs, and proof of work are clear, credible, reproducible, and portfolio-ready. Use for vibecoded or unfinished repositories, portfolio showcases, hiring reviews, or public releases; the core workflow is tool-agnostic and also works in other coding agents and IDEs. Do not use for broad code rewrites or changing GitHub account settings.
---

# GitHub Repo Presenter (Codex adapter)

This is the optional Codex entrypoint for the portable repository-presentation toolkit. The source of truth is [PORTABLE_PROMPT.md](PORTABLE_PROMPT.md), which is ordinary Markdown and can be used by any coding agent or IDE.

When this skill is invoked:

1. Read `PORTABLE_PROMPT.md` before acting.
2. Run `scripts/audit_repo.py` against the target repository when the path is available.
3. Use the benchmark and GitHub-surface references only when relevant to the target.
4. Preserve unrelated work, avoid fabricated proof, and report verified versus unverified claims precisely.

Do not broaden a presentation pass into a product rewrite, remote-account change, history rewrite, force-push, or destructive cleanup without explicit scope.
