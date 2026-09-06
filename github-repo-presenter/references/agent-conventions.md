# Agent and IDE instruction conventions

The portable workflow lives in `PORTABLE_PROMPT.md`. These are the adapter locations currently documented by major coding agents and IDEs:

| Tool or environment | Recommended adapter | Notes |
| --- | --- | --- |
| Cross-agent default | `AGENTS.md` at the target repository root | Broadest shared option. Several agent CLIs recognize it. |
| Claude Code | `CLAUDE.md` at the target repository root | The included adapter imports `AGENTS.md`, so the workflow has one source of truth. |
| Cursor | `.cursor/rules/github-repo-presenter.mdc` | Cursor project rules use MDC frontmatter. The legacy root `.cursorrules` file is still supported but deprecated. |
| Windsurf / Cascade | `AGENTS.md` or `.windsurf/rules/` | `AGENTS.md` is the simplest portable path; use a Windsurf rule when activation or path scoping is needed. |
| GitHub Copilot | `.github/copilot-instructions.md` | Repository-wide instructions are supported by Copilot Chat, CLI, cloud agent, and several IDE integrations. |
| Any other agent | `PORTABLE_PROMPT.md` | Attach it, paste it, or ask the agent to read it before working. |

The installer in `scripts/install_adapter.py` copies the available adapters without overwriting existing files unless `--force` is explicitly provided.

Vendor references:

- [Claude Code memory and instruction files](https://code.claude.com/docs/en/memory)
- [Cursor project rules](https://docs.cursor.com/context/rules)
- [Windsurf Cascade memories and rules](https://docs.windsurf.com/windsurf/cascade/memories)
- [GitHub Copilot custom-instruction support](https://docs.github.com/en/copilot/reference/custom-instructions-support)
