# Agent & IDE Instruction Conventions

The primary, tool-neutral source of truth is [PORTABLE_PROMPT.md](../PORTABLE_PROMPT.md). To allow coding agents and IDE assistants to automatically discover and enforce these presentation standards, thin adapters are provided for major tools:

| Tool / Environment | Adapter File Location | Behavior & Conventions |
| :--- | :--- | :--- |
| **Cross-Agent Standard** | `AGENTS.md` (root) | Recognized by modern autonomous coding agents. Broadest shared standard. |
| **Claude Code** | `CLAUDE.md` (root) | Imports `AGENTS.md` so instructions remain unified in a single source of truth. |
| **Cursor** | `.cursor/rules/github-repo-presenter.mdc` | Project rule with frontmatter (`alwaysApply: false`). Activates on repo presentation tasks. |
| **Windsurf / Cascade** | `AGENTS.md` or `.windsurf/rules/` | Cascade natively consumes `AGENTS.md`; custom rule can be placed in `.windsurf/rules/`. |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Supported across VS Code, JetBrains, Visual Studio, and GitHub Copilot CLI. |
| **Codex** | `SKILL.md` / `agents/openai.yaml` | Standard Codex skill directory format, placed in `~/.agents/skills/`. |
| **Any Chat / CLI Agent** | `PORTABLE_PROMPT.md` | Paste or point the agent directly: *"Read `PORTABLE_PROMPT.md` and apply it to this repository."* |

---

## Installing Adapters Automatically

Use the included safe installer script from the toolkit root:

```bash
# Preview what would be installed
python3 github-repo-presenter/scripts/install_adapter.py --target /path/to/project --adapter agents --dry-run

# Install a specific adapter (refuses to overwrite existing files without --force)
python3 github-repo-presenter/scripts/install_adapter.py --target /path/to/project --adapter claude

# Install all supported adapters
python3 github-repo-presenter/scripts/install_adapter.py --target /path/to/project --adapter all
```
