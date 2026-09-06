# GitHub Repo Presenter

`github-repo-presenter` is a portable, agent-agnostic toolkit for turning an unfinished or AI-assisted repository into a credible portfolio showcase. The core workflow is a plain Markdown playbook, so it works with any coding agent or IDE. Thin adapters are included for common instruction-file conventions, and the Codex skill remains available for people who use Codex.

It audits the repository, improves the README and supporting docs, surfaces engineering decisions, and verifies what can actually be claimed. It does not rewrite product code just to make a repository look polished.

## Quick start for any agent or IDE

Clone the toolkit once:

```bash
git clone https://github.com/aiden-guan/github-repo-presenter.git ~/github-repo-presenter
```

Then point your agent at the portable workflow from inside the project you want to polish:

```text
Read ~/github-repo-presenter/github-repo-presenter/PORTABLE_PROMPT.md and apply it to this repository. Make the smallest evidence-backed changes needed to make the project credible, reproducible, and portfolio-ready.
```

The canonical workflow is [github-repo-presenter/PORTABLE_PROMPT.md](github-repo-presenter/PORTABLE_PROMPT.md). It is ordinary Markdown and does not require a particular model, editor, CLI, or plugin system.

## Install an instruction-file adapter

The included installer copies the right adapter into a target repository. It refuses to overwrite an existing instruction file unless `--force` is supplied.

```bash
python3 ~/github-repo-presenter/github-repo-presenter/scripts/install_adapter.py \
  --target /path/to/your/project \
  --adapter agents
```

Available adapters:

- `agents` — `AGENTS.md`, the broadest cross-agent option;
- `claude` — `AGENTS.md` plus `CLAUDE.md` importing it;
- `cursor` — `.cursor/rules/github-repo-presenter.mdc`;
- `copilot` — `.github/copilot-instructions.md`;
- `all` — installs every adapter above.

The adapters follow the documented conventions for [Claude Code](https://code.claude.com/docs/en/memory), [Cursor](https://docs.cursor.com/context/rules), [Windsurf](https://docs.windsurf.com/windsurf/cascade/memories), and [GitHub Copilot](https://docs.github.com/en/copilot/reference/custom-instructions-support). `AGENTS.md` is also recognized by several newer coding-agent CLIs, so it is the best default when you do not know which tool a contributor uses.

## Codex install

Codex loads user skills from `~/.agents/skills` and supports symlinked skill folders. For a clone-based install:

```bash
mkdir -p ~/.agents/skills
ln -sfn ~/github-repo-presenter/github-repo-presenter ~/.agents/skills/github-repo-presenter
```

For a local development checkout:

```bash
mkdir -p ~/.agents/skills
ln -sfn "/Users/aidenguan/Documents/ChatGPT/Github Skill/github-repo-presenter" ~/.agents/skills/github-repo-presenter
```

Then invoke it with:

```text
$github-repo-presenter Audit this repository and make it portfolio-ready.
```

Restart Codex if the skill does not appear immediately. The Codex-specific entrypoint is [github-repo-presenter/SKILL.md](github-repo-presenter/SKILL.md); it delegates to the same portable workflow used by every other adapter.

## What is included

- `PORTABLE_PROMPT.md` — the tool-neutral source of truth;
- `templates/` — copyable instruction files for common agents and IDEs;
- `scripts/install_adapter.py` — safe adapter installer for a target repository;
- `scripts/audit_repo.py` — read-only repository inventory and gap finder;
- `references/benchmark-repos.md` — high-traction examples and presentation patterns;
- `references/github-surfaces.md` — GitHub-facing presentation checklist;
- `references/agent-conventions.md` — supported instruction-file locations and links to vendor documentation;
- `SKILL.md` and `agents/openai.yaml` — optional Codex integration.

The workflow preserves unrelated work, avoids fabricated proof, and distinguishes implemented, locally verified, remotely configured, and unverified work.
