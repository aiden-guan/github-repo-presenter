# GitHub Repo Presenter (Portable Playbook)

Use this playbook whenever a user asks to make a repository **presentable, portfolio-ready, technically credible, visually strong, easier to review, or easier to reproduce**.

It is completely tool-neutral: execute it from any coding agent, IDE assistant, CLI environment, or pair-programming session.

---

## 1. Outcome & Scope

Transform the target repository into an exceptionally polished open-source/product showcase on par with benchmark repositories (**Onlook**, **Twenty**, **Infisical**, **Formbricks**, **Midday**, **Trigger.dev**, **Browser Use**, **Langfuse**, **Plane**, **Excalidraw**).

The repository must read as a compact union of:
- **Product page** (what problem it solves, why it matters, visual proof)
- **Engineering case study** (real technical hurdles, architecture, trade-offs)
- **Technical documentation** (accurate stack, verified setup, API/data flow)

This is a presentation and reproducibility pass. **Never perform a product rewrite or refactor functional code** solely to make the repository look nicer.

---

## 2. The 10 Visitor Goals

Within 30 seconds, a technically sophisticated visitor (engineer, recruiter, or tech lead) must:
1. Understand what the project does within **~5 seconds**.
2. See why the project is interesting within **~15 seconds**.
3. Visually understand the core product without running it.
4. Understand major capabilities without reading large paragraphs.
5. Understand how the system works technically.
6. Identify the most impressive engineering decisions.
7. Run the project locally with minimal friction.
8. Navigate the repository easily via a curated directory tree.
9. Distinguish the project from a generic hackathon or tutorial build.
10. Leave with the impression that the repository was intentionally designed and maintained.

---

## 3. Strict Non-Negotiable Guardrails (Anti-Hallucination)

- **Zero Fabrications**: Never invent live URLs, active users, revenue, benchmarks, features, integrations, performance speedups, deployment status, awards, or star counts.
- **Label Unverified Claims**: If evidence is missing or requires an API key, mark it clearly as unverified or required.
- **Zero Committed Secrets**: Treat `.env`, API keys, tokens, session IDs, private keys, database dumps, and credentials as strictly sensitive. Create or update `.env.example` only with safe placeholders.
- **Zero Fake UI Screenshots**: Never generate fake UI mockups and present them as proof of working code. If visual assets are missing, use code-based visual assets (Mermaid architecture flowcharts, ASCII trees, formatted code snippet tables) and provide an explicit screenshot capture specification for the user.
- **Preserve Unrelated Work**: Check `git status --short --branch` before editing. Never overwrite unrelated dirty files, rewrite Git history, force-push, or delete branches without explicit instruction.

---

## 4. Execution Workflow

### Phase 1: Codebase Deep Dive
**Never begin by rewriting README.md.** Understand the codebase first:
1. Run the read-only inventory if available:
   ```bash
   python3 scripts/audit_repo.py .
   ```
2. Read manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.).
3. Examine key directories (`src/`, `app/`, `components/`, `lib/`, `server/`, `api/`).
4. Review database schemas/migrations (`prisma/`, `drizzle/`, `schema.sql`, `models/`).
5. Check infrastructure configs (`Dockerfile`, `docker-compose.yml`, GitHub Actions).
6. Check test suites and seed scripts.
7. Review existing media assets (`assets/`, `docs/assets/`, `public/`).

From this, deduce:
- The core problem solved and primary user workflow.
- Key technical mechanisms and difficult engineering decisions.
- How the application runs and is verified locally.
- True status and maturity of the codebase.

### Phase 2: Project Archetype Classification
Consult [references/project-types.md](references/project-types.md) and classify the project into one of 8 archetypes:
1. **Product / SaaS**: Lead with product hero, 2x2 visual feature grid, user workflow, client/server/DB architecture, and local vs. deploy paths.
2. **AI / Agent**: Lead with terminal/browser interaction demo, model/tool orchestration diagram, tool execution loop, context management, and honest limitations.
3. **Developer Tool / Library**: Lead with 5-line copy-pasteable code snippet in first viewport, 1-line package install, API ergonomics, and verified benchmarks.
4. **Game / Interactive Graphics**: Lead with gameplay GIF/video, core loop mechanics, controls table, and rendering/physics architecture.
5. **Data / ML**: Lead with problem statement, pipeline DAG flowchart, dataset provenance, and reproducible evaluation commands.
6. **Mobile Application**: Lead with framed device mockups, user journey, offline storage/sync, and Expo/simulator setup.
7. **Infrastructure / Backend**: Lead with system topology diagram, concurrency/resilience model, wire protocol/API, and Docker quickstart.
8. **Personal Experimental**: Lead with provocative hypothesis, proof demo, what was built vs. borrowed, and engineering hurdles.

### Phase 3: Visual Presentation System
Consult [references/visual-system.md](references/visual-system.md):
- **First Viewport**: Project name, one-sentence promise, primary links (`Live Demo`, `Docs`, `Quickstart`), and high-impact visual proof.
- **Feature Grids**: Replace vertical screenshot waterfalls with clean 2-column comparison tables or feature grids (`| Feature A | Feature B |`).
- **Framing**: Crop all OS taskbars, browser chrome, and debug noise. Use standard aspect ratios (`16:9` or `4:3`) and 2x retina clarity.
- **Demonstrations**: Capture the primary interaction loop (Input → Interaction → Result) as a short, compressed GIF or video (<5MB).
- **Missing Assets**: When UI screenshots are unavailable, use Mermaid system diagrams, data flow charts, and detailed CLI code blocks.

### Phase 4: Architecture & Engineering Deep Dives
1. **Architecture Communication**:
   - Construct a clear Mermaid diagram (`flowchart LR` or `flowchart TD`) with distinct subgraphs (`Client`, `Gateway`, `Services`, `Persistence`).
   - Accompany with an end-to-end numbered workflow (steps 1–5) referencing actual source modules.
2. **Interesting Engineering (PAWT Framework)**:
   Consult [references/engineering-deep-dives.md](references/engineering-deep-dives.md). For 1-3 substantial engineering challenges, document:
   - **Problem**: The exact constraint, bottleneck, or concurrency/state hazard.
   - **Approach**: What was implemented in the codebase.
   - **Why**: Why this design was chosen over obvious alternatives.
   - **Tradeoff**: What was sacrificed, complicated, or bounded.

### Phase 5: README Information Architecture & Repository Hygiene
Consult [references/readme-architecture.md](references/readme-architecture.md) and [references/github-surfaces.md](references/github-surfaces.md):
1. Recommended Section Sequence:
   - Hero (Identity, 1-sentence value proposition, verifiable badges, hero visual)
   - What it does & why it exists
   - Core capabilities (structured visual grid)
   - Product walkthrough
   - Architecture & system flow (Mermaid + numbered workflow)
   - Interesting engineering (PAWT blocks)
   - Technology stack (categorized by responsibility: Client, Backend, Storage, Infra)
   - Getting started (Prerequisites, Quick Start, Full Dev Setup)
   - Configuration (`.env.example` reference)
   - Curated repository structure (functional tree)
   - Verification & testing commands
   - Roadmap, status & honest limits
   - License
2. Writing Style:
   - Concise, active voice, written like a senior systems engineer.
   - Ban all marketing fluff (*revolutionary, cutting-edge, seamless, delve, game-changing*).
   - Use concrete specifics over vague slogans.
3. Clean Repository Root:
   - Remove tracking of generated artifacts (`.DS_Store`, build caches, logs).
   - Ensure a truthful `.gitignore` and safe `.env.example`.

### Phase 6: Automated Validation & Quality Rubric
1. **Automated Validation**:
   ```bash
   python3 scripts/validate_readme.py README.md --strict
   ```
   Verifies that all relative links resolve, images exist on disk, heading hierarchy is sound, scripts match `package.json`, environment variables match `.env.example`, and zero secrets or buzzwords exist.
2. **Internal Rubric Self-Check**:
   Consult [references/quality-rubric.md](references/quality-rubric.md). Internally rate the repository across the 12 dimensions:
   1. Clarity
   2. Visual hierarchy
   3. Visual quality
   4. Technical credibility
   5. Technical depth
   6. Demo quality
   7. Architecture communication
   8. Setup quality
   9. Scannability
   10. Repository organization
   11. Accuracy
   12. Originality
   *Trigger Rule: If any dimension scores < 4, perform a targeted revision pass before completing.* (Never print numerical scores into the README).

---

## 5. Handoff Structure

Conclude every repository presentation pass with four clear sections:
- **Implemented**: Exact files modified or created and the user-visible presentation enhancements.
- **Locally Verified**: Commands executed and validation tests that passed (e.g., `validate_readme.py`, test commands, link checks).
- **Unverified / Awaiting Owner Action**: External items requiring owner keys, live DNS, deployment triggers, or GitHub remote settings (e.g., repository description, topics, social preview upload).
- **Screenshot / Media Capture Checklist**: If new UI captures are recommended, list exact route, viewport dimensions, interaction state, and destination filename.
