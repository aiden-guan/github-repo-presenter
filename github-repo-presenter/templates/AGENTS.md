# GitHub Repo Presenter

Apply these instructions whenever the user asks to make this repository **presentable, portfolio-ready, technically credible, visually strong, easier to review, or easier to reproduce**.

## Outcome & Scope

Transform the repository into an exceptionally polished open-source showcase on par with benchmark repositories (Onlook, Twenty, Infisical, Formbricks, Midday, Trigger.dev, Browser Use, Langfuse, Plane, Excalidraw).

The repository must feel like a compact combination of **product page**, **engineering case study**, and **technical documentation**. This is a presentation and reproducibility pass—do not perform broad code rewrites or refactor functional application logic solely to make the repository look nicer.

## Non-Negotiable Grounding Laws (Anti-Hallucination)

- **Zero Fabrications**: Never invent live URLs, active users, revenue, benchmarks, features, integrations, performance speedups, deployment status, awards, or star counts.
- **Label Unverified Claims**: If evidence is missing or requires an API key, mark it clearly as unverified or required.
- **Zero Committed Secrets**: Treat `.env`, API keys, tokens, session IDs, private keys, and credentials as strictly sensitive.
- **Zero Fake UI Screenshots**: Never generate fake UI mockups and present them as proof of working code. If visual assets are missing, use code-based visual assets (Mermaid architecture flowcharts, ASCII trees, formatted code snippet tables) and provide an explicit screenshot capture specification for the user.
- **Preserve Unrelated Work**: Check `git status --short --branch` before editing. Never overwrite unrelated dirty files, rewrite Git history, force-push, or delete branches without explicit instruction.

## 6-Phase Execution Workflow

1. **Codebase Deep Dive**: Never begin by rewriting README.md. Inspect manifests, source files (`src/`, `app/`, `lib/`, `api/`), schemas, Docker configs, and tests to ground all claims in actual code.
2. **Project Archetype Classification**: Classify the project into its primary archetype (Product/SaaS, AI/Agent, Developer Tool/Library, Game, Data/ML, Mobile App, Infrastructure/Backend, Personal Experimental) and adapt presentation priorities accordingly.
3. **Visual Strategy**: Craft a high-impact first viewport (project name, 1-sentence value proposition, key links, visual proof). Use structured 2-column feature grids (`| Feature A | Feature B |`) instead of vertical screenshot waterfalls.
4. **Architecture & Engineering Deep Dives**:
   - Construct a clean Mermaid diagram with distinct subgraphs and an end-to-end numbered workflow (steps 1–5) referencing actual code modules.
   - Document 1-3 substantial engineering challenges using the **Problem-Approach-Why-Tradeoff (PAWT)** framework.
5. **README Information Architecture & Hygiene**:
   - Organize the tech stack by responsibility (Client, Backend, Database, Infrastructure).
   - Write like a senior systems engineer; ban all marketing fluff (*revolutionary, cutting-edge, seamless, delve, game-changing*).
   - Provide a verified quick start and safe `.env.example`.
   - Curate a clean repository root and functional directory tree.
6. **Automated Validation & Quality Scoring**:
   - Validate with `validate_readme.py` (checks relative links, images, headings, mermaid syntax, package scripts, env variables, secrets, and buzzwords).
   - Self-evaluate against the internal 12-dimension quality rubric (Clarity, Hierarchy, Visuals, Credibility, Depth, Demo, Architecture, Setup, Scannability, Hygiene, Accuracy, Originality). Refine any score < 4 before completion. (Never print numerical scores into the README).

## Automatic Changelog Maintenance (On Updates & Pushes)

Whenever changes are committed, pushed, or released:
- The agent must automatically capture the update in `CHANGELOG.md`.
- Inspect git commits (`git log @{u}..HEAD` or recent commits) and categorize into `Added`, `Changed / Refactored`, `Fixed`, `Documentation`, and `Tooling`.
- Run `python3 scripts/update_changelog.py --write` or follow [references/changelog-and-updates.md](references/changelog-and-updates.md).
- Enforce visual cohesion: executive summary, architectural highlights table, categorized changes, and verified proofs.

## Handoff

End with **Implemented**, **Locally Verified**, **Unverified / Awaiting Owner Action**, and **Screenshot / Media Capture Checklist**. Use “documented,” “locally verified,” and “unverified” precisely.
