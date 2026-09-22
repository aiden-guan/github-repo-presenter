# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and adheres to [Semantic Versioning](https://semver.org/).

---

## [1.1.0] — 2026-09-22

### Summary
Major architectural upgrade transforming the toolkit into an elite, portfolio-ready repository presentation and maintenance engine on par with benchmark open-source projects (Onlook, Twenty, Infisical, Formbricks, Midday, Trigger.dev, Browser Use).

### Architectural & Functional Highlights
| Component / Layer | Improvement |
| :--- | :--- |
| **Classification Engine** | Added evidence-based scoring for 8 distinct project archetypes (SaaS, AI Agent, Dev Tool, Game, Data/ML, Mobile, Infra, Personal). |
| **Automated Validation** | Added zero-dependency `validate_readme.py` checking relative links, on-disk images, Mermaid syntax, package scripts, env vars, and secret leaks. |
| **Changelog Automation** | Added `update_changelog.py` to automatically synthesize git commits into clean, professional, visually cohesive changelogs. |
| **Engineering Depth** | Established the 4-part Problem-Approach-Why-Tradeoff (PAWT) framework for documenting non-trivial engineering challenges. |
| **Visual Presentation** | Replaced vertical image waterfalls with structured 2-column feature grids, 2x retina asset guidelines, and demo interaction recipes. |

### Detailed Changes

#### Added
- **Archetype Classification**: Added `references/project-types.md` with tailored section orders and presentation priorities for 8 software categories.
- **Visual System**: Added `references/visual-system.md` detailing 2-column feature tables, aspect ratio standardization (`16:9`/`4:3`), and GIF demo capture rules.
- **Engineering Deep Dives**: Added `references/engineering-deep-dives.md` with concrete PAWT archetypes (agent orchestration, state sync, sandboxes, codegen pipelines).
- **Quality Rubric**: Added `references/quality-rubric.md` defining a 12-dimension internal 1–5 scoring matrix with automated refinement pass triggers.
- **Changelog Guide**: Added `references/changelog-and-updates.md` setting the visual standard for clean, professional repository release notes.
- **Validation Script**: Added `scripts/validate_readme.py` to automate Markdown link, image, script, and secret validation with `--strict` mode.
- **Changelog Script**: Added `scripts/update_changelog.py` for automated git-to-changelog generation and prepending.

#### Changed / Refactored
- **Core Orchestrator**: Completely rewrote `SKILL.md` and `PORTABLE_PROMPT.md` around a mandatory 6-phase reasoning loop: Codebase Deep Dive → Archetype Classification → Visual Strategy → Architecture & PAWT → README Hygiene → Automated Validation.
- **Repository Inventory**: Upgraded `scripts/audit_repo.py` to calculate archetype confidence scores, detect API routes/schemas, and categorize tech stack layers.
- **Benchmark Analysis**: Expanded `references/benchmark-repos.md` with deep structural breakdowns of 10 industry leaders (Onlook, Twenty, Infisical, Formbricks, Midday, Trigger.dev, Browser Use, Langfuse, Plane, Excalidraw).
- **Agent Templates**: Upgraded `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/github-repo-presenter.mdc`, and `.github/copilot-instructions.md` with the new workflow and automatic changelog maintenance.

#### Fixed
- **Repository Hygiene**: Added comprehensive `.gitignore` to prevent tracking Python bytecode (`__pycache__`), OS artifacts (`.DS_Store`), and editor caches.
- **Documentation Parity**: Resolved missing tech stack layering and added system architecture Mermaid flowchart in root `README.md`.

### Verification Proof
- `python3 scripts/validate_readme.py README.md --strict` passed with 0 errors and 0 warnings.
- `python3 -m py_compile scripts/*.py` verified zero syntax errors across all scripts.
- `python3 scripts/update_changelog.py --preview` tested successfully against local git history.

---

## [1.0.0] — 2026-09-05

### Summary
Initial release of the portable, agent-agnostic GitHub repository presentation toolkit.

### Detailed Changes

#### Added
- **Core Playbook**: Introduced `PORTABLE_PROMPT.md` defining tool-neutral repository audit and presentation workflows.
- **Audit Tool**: Added `scripts/audit_repo.py` for read-only repository inventory and gap identification.
- **Adapter Installer**: Added `scripts/install_adapter.py` for safe copying of instruction templates.
- **Agent Adapters**: Created initial instruction templates for `AGENTS.md`, `CLAUDE.md`, Cursor, and GitHub Copilot.
- **Surface Checklists**: Added `references/benchmark-repos.md`, `references/github-surfaces.md`, and `references/agent-conventions.md`.
