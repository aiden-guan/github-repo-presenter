# GitHub-Facing Presentation & Surface Checklist

A repository's GitHub presentation extends beyond `README.md`. The repository metadata, social preview, topics, and community health files create the initial impression across GitHub search, profile pages, and social media unfurls.

This reference specifies how to audit, configure, and recommend enhancements for these surfaces.

---

## 1. Repository Metadata (About Section)

The GitHub "About" box in the top-right corner is viewed before the README:

### Repository Description
- **Max length**: 350 characters (Aim for 80-140 characters).
- **Rule**: State what the project does in plain, concrete language. Omit fluff ("A revolutionary app").
- **Good Examples**:
  - *"Self-hosted feedback analysis engine that clusters error logs and generates reproducible GitHub issues."*
  - *"Deterministic terminal agent for automated browser navigation with visual verification."*
- **Bad Examples**:
  - *"My final project for CS101."*
  - *"An awesome Next.js app with AI features."*

### Website / Homepage URL
- Must link to the **live product**, **hosted demo**, or **documentation site**.
- If no live deployment exists, leave blank or link to the specific section of the README (e.g., `#architecture`). Never point to an expired Vercel preview or localhost URL.

### Topics (Discovery Tags)
- Use **5 to 10 lowercase, hyphenated topics**.
- Cover:
  1. *Core domain*: `llm-agent`, `data-pipeline`, `developer-tools`, `game-engine`.
  2. *Key technology*: `typescript`, `nextjs`, `fastapi`, `postgres`, `webgl`.
  3. *Architecture/pattern*: `rag`, `crdt`, `microvm`, `zero-knowledge`.
- Avoid spammy or generic topics (`cool`, `awesome`, `project`, `code`).

---

## 2. Social Media Preview (Open Graph Card)

When a GitHub repository link is shared on X/Twitter, LinkedIn, Slack, or Discord, GitHub renders the repository social preview card.

### Dimensions & Formatting
- **Recommended resolution**: **1280 × 640 pixels** (2:1 aspect ratio).
- **Format**: PNG or WebP under 1 MB.
- **Visual Composition**:
  - Dark or high-contrast neutral background.
  - Large, crisp project logo and title.
  - A single, high-contrast tagline summarizing the core outcome.
  - A subtle, high-fidelity UI preview or architecture snippet floating on the right side.
  - Generous padding (at least 60px safe margin around borders).
- **Anti-Pattern**: Do not use an unedited, low-resolution raw screenshot of the full webpage where text is unreadable at thumbnail scale.

---

## 3. Root Directory Hygiene & Organization

A clean root directory signals that the maintainer is disciplined:

### Root Directory Best Practices
- Keep root files strictly focused on repository entry points:
  - `README.md`
  - `LICENSE`
  - Manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.)
  - `.gitignore`
  - `.env.example`
- Move auxiliary files into clear subdirectories:
  - `assets/readme/` or `docs/assets/` for README graphics.
  - `docs/` for extended technical guides or RFCs.
  - `scripts/` for setup, build, and verification scripts.
  - `tests/` for automated test suites.

### Strict Tracking Rules
Never commit these into the repository:
- Operating system files (`.DS_Store`, `Thumbs.db`)
- Build outputs (`dist/`, `build/`, `.next/`, `.turbo/`, `target/`, `out/`)
- Cache directories (`.cache/`, `.pytest_cache/`, `__pycache__/`)
- Environment files with credentials (`.env`, `.env.local`, `.env.production`)
- Temporary SQLite databases (`*.db`, `*.sqlite`, `*.sqlite3`)
- Large video recordings or raw datasets (use external releases or git LFS if strictly necessary)

---

## 4. Community Health & Governance Files

Add community files only when the repository's intended audience and maintenance capacity justify them. Adding empty boilerplate templates to a personal weekend project creates unnecessary bureaucratic clutter.

| File | When to Include | When to Omit |
| :--- | :--- | :--- |
| **`LICENSE`** | **Always**. Essential for clarity on whether code can be viewed, copied, or modified. (MIT, Apache 2.0, AGPL). | Never omit on public repositories. |
| **`.env.example`** | Whenever the project uses environment variables. Include comments explaining where values come from. | When the project requires zero environment variables. |
| **`CONTRIBUTING.md`** | Multi-maintainer or active open-source projects inviting external pull requests. | Personal portfolio showcases or experimental solo projects. |
| **`SECURITY.md`** | Projects handling user authentication, payments, encryption, or multi-tenant data. | Non-networked games, static demos, or offline CLI experiments. |
| **Issue / PR Templates** | Repositories receiving recurring community bug reports or feature suggestions. | Solo projects without public issues enabled. |

---

## 5. Security & GitHub Settings Boundary

The skill operates within the local repository boundary. It can inspect local configurations and recommend GitHub settings, but cannot and must not claim to have modified remote account settings (e.g., branch protection rules, secret scanning, or GitHub Actions secrets) without explicit user intervention.
