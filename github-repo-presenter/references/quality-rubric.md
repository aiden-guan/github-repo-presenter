# Quality Control Rubric & Internal Evaluation Matrix

This rubric defines the internal quality bar for evaluating repository presentations. It is used exclusively for **self-auditing and iterative refinement**.

> [!IMPORTANT]
> **Strict Rule**: Never print numerical scores or raw evaluation rubrics into a user's README or public repository documents. This matrix is strictly an internal guide for the agent to assess whether a presentation meets the elite standard or requires another refinement pass.

---

## The 12 Evaluation Dimensions (1–5 Scale)

| Dimension | Description | Score 1 (Failing) | Score 3 (Mediocre / Student) | Score 5 (Elite Open-Source Standard) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Clarity** | Time to understand the project | Confusing name, no summary, starts with npm commands or badge wall. | Generic sentence ("A modern web app for teams"). Needs 30+ seconds of reading. | Understandable in <5 seconds. Immediate, unambiguous purpose and target user. |
| **2. Visual Hierarchy** | Eye movement and viewport balance | Disorganized text dump; inconsistent heading levels; noisy badges. | Standard GitHub template layout; repetitive heading styles; text-heavy. | Distinctive hero section; intentional typography cadence; breathing whitespace; zero clutter. |
| **3. Visual Quality** | Screenshots, diagrams, and assets | Blurry, full-desktop raw screenshots with browser tabs/OS taskbars. | Single full-width screenshot or none; unstyled raw Mermaid diagram. | 2x retina assets; clean framing; structured 2-column feature grids; crisp SVGs. |
| **4. Technical Credibility** | Grounding and proof | Generic buzzwords ("revolutionary", "seamless"); unsubstantiated metrics. | Claims match dependencies, but lacks concrete implementation details. | Zero hallucinations; claims verified against actual code; honest boundaries and trade-offs. |
| **5. Technical Depth** | Engineering insights | Only lists technologies; basic CRUD described as complex engineering. | Mentions some architectural patterns without explaining problems or trade-offs. | Explains non-obvious engineering challenges using Problem-Approach-Why-Tradeoff framework. |
| **6. Demo & Proof Quality** | Demonstrating working software | No visual demo; dead links; imaginary features. | Static screenshot of login page or empty dashboard. | High-fidelity GIF/video or step-by-step walkthrough showing input → interaction → result. |
| **7. Architecture Communication** | Systems & data flow clarity | No diagram or incomprehensible spaghetti diagram. | Generic 3-box diagram (Client → Server → DB) with no module context. | Accurate Mermaid diagram with clear tiers, accompanied by numbered module-level workflow. |
| **8. Setup & Reproducibility** | Friction-free local execution | Missing commands; broken prerequisites; assumes global environment tools. | Standard `npm install && npm start` without env configs or DB setup steps. | Tested, working quickstart; clear `.env.example` guidance; separates quickstart from dev setup. |
| **9. Scannability** | Fast information retrieval | Giant walls of paragraphs (15+ lines); excessive bolding everywhere. | Standard bullets but lacks visual anchoring or rhythm. | Skimmable in 30 seconds; tables, structured lists, callout quotes, clean code fences. |
| **10. Repository Organization** | Root hygiene and structure | Cluttered root directory; stray logs, `.DS_Store`, untracked build artifacts. | Standard flat structure with unorganized assets. | Curated functional directory tree; clean asset folders (`assets/readme/`); truthful `.gitignore`. |
| **11. Accuracy & Truthfulness** | Honesty regarding status & scope | Claims "production ready" for a weekend hack; fabricated benchmark numbers. | Implies features exist that are only stubs in code. | Precisely distinguishes implemented vs unverified vs roadmap; discloses limits honestly. |
| **12. Originality** | Tone and distinctive identity | Reads like an automated ChatGPT template output or generic boilerplate. | Inoffensive but boring and indistinguishable from 1,000 other repos. | Confident, precise engineering voice; tailored to the specific software archetype. |

---

## Refinement Trigger Protocol

Before finalizing a repository review or presentation pass:

1. **Evaluate all 12 dimensions internally**.
2. **If ANY dimension scores below 4**:
   - Do NOT deliver the output immediately.
   - Execute an automatic **refinement pass** targeting the specific deficient dimension:
     - *If Visual Hierarchy < 4*: Tighten the hero section, replace vertical image stack with a 2-column feature grid, or reorder sections.
     - *If Technical Depth < 4*: Re-inspect codebase for custom middleware, state handling, worker queues, or serialization logic, and add a Problem-Approach-Why-Tradeoff block.
     - *If Architecture < 4*: Rewrite Mermaid diagram to use subgraphs and add a 5-step numbered walkthrough matching source file names.
     - *If Setup Quality < 4*: Re-check package manager lockfiles, cross-reference scripts with `package.json`, and ensure `.env.example` exists.
     - *If Clarity < 4*: Rewrite the first sentence to be completely free of marketing filler.

---

## The Pre-Delivery Anti-Pattern Checklist

Ensure NONE of the following anti-patterns exist in the final README:

- [ ] **Badge Wall**: More than 4 badges in the hero section.
- [ ] **Raw Commands First**: Shell code block appearing before explaining what the project is.
- [ ] **Logo Ocean**: Centered logo taking up half the viewport with massive empty margin.
- [ ] **Marketing Fluff**: Words like "revolutionary", "cutting-edge", "game-changing", "seamless", "delve".
- [ ] **Hallucinated Claims**: Metrics (stars, requests/sec, user count) not directly verifiable in repo files.
- [ ] **Raw Desktop Screenshots**: Screenshots showing browser address bar, bookmarks, or OS clock.
- [ ] **Vertical Image Dump**: 3 or more full-width images stacked sequentially without grid structure.
- [ ] **Empty Sections**: Headings containing boilerplate like "Coming soon", "TBD", or "[Insert here]".
- [ ] **Generic Tech List**: Long bulleted list of 25 packages without architectural categorization.
- [ ] **Unverifiable Benchmark**: Bar chart or speed claims without reproducible benchmark scripts.
- [ ] **Exposed Secrets**: Real API keys, database connection strings, or JWT secrets in code fences.
- [ ] **Broken Relative Links**: Links to files, docs, or images that do not exist on disk.
