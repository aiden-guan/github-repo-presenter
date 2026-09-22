# GitHub Repo Presenter

When asked to audit, present, polish, or update this repository for portfolio review, open-source release, or technical evaluation, execute these instructions:

## Non-Negotiable Grounding Laws
- Inspect `git status --short --branch`, remotes, manifests, and source files before editing.
- Never invent URLs, screenshots, metrics, benchmarks, stars, tests, credentials, features, integrations, or deployment status.
- Never commit secrets. Treat `.env` and credentials as sensitive. Provide safe `.env.example`.
- Never generate fake UI screenshots as proof of features. Use Mermaid diagrams or code tables if real assets are missing.
- Do not perform broad product refactors solely to make presentation look nicer.

## Execution Workflow
1. **Codebase Deep Dive**: Inspect entry points, routes, schemas, Docker files, and tests to ground all claims in source code.
2. **Archetype Classification**: Classify project (SaaS, AI/Agent, Dev Tool, Game, Data/ML, Mobile, Infra, Personal Experimental) and adapt presentation priorities.
3. **Visual Strategy**: Craft a high-impact first viewport (name, 1-sentence value proposition, key links, visual proof). Use structured 2-column feature grids (`| Feature A | Feature B |`) rather than vertical screenshot dumps.
4. **Architecture & Engineering Deep Dives**:
   - Create a clean Mermaid system diagram with subgraphs and an end-to-end numbered workflow (steps 1–5).
   - Document non-obvious technical challenges using the **Problem-Approach-Why-Tradeoff (PAWT)** framework.
5. **README & Hygiene**:
   - Organize tech stack by responsibility (Client, Backend, Database, Infra).
   - Write like a senior systems engineer; ban marketing fluff (*revolutionary, cutting-edge, seamless, delve*).
   - Provide a tested quickstart and clean repository root.
6. **Automated Validation**:
   - Run `validate_readme.py` to ensure zero broken links, missing images, secret leaks, or placeholder text.
   - Internally score against the 12-dimension quality rubric (refine any dimension < 4).

## Automatic Changelog Maintenance (On Updates & Pushes)
Whenever changes are committed, pushed, or released:
- Automatically capture the update in `CHANGELOG.md`.
- Group commits into `Added`, `Changed / Refactored`, `Fixed`, `Documentation`, and `Tooling`.
- Enforce visual cohesion: executive summary, architectural highlights table, categorized changes, and verified proofs.

## Handoff
End with **Implemented**, **Locally Verified**, **Unverified / Awaiting Owner Action**, and **Screenshot / Media Capture Checklist**.
