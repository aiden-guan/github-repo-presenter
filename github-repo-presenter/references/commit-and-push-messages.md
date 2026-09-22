# Clean, Professional, and Visually Cohesive Commit & Push Messages

A repository's presentation does not stop at `README.md`. A visitor, collaborator, or technical recruiter inspecting the **Git commit history** and **push notifications** evaluates engineering discipline immediately.

A commit log filled with:
```text
update
fix bug
changes
wip
more fixes
asdf
```
instantly shatters the technical credibility built by a polished README.

Conversely, clean, structured, and visually cohesive commit and push messages demonstrate intentional design, rigorous testing, and engineering professionalism.

---

## 1. Anatomy of an Elite Commit Message

An elite commit message follows a 3-tier structure:

```text
<type>(<scope>): <concise, imperative summary under 72 chars>

<Context & Intent: 1-2 dense sentences explaining WHY this change exists>

### Key Changes
- **<Component/Area>**: <Specific implementation or behavioral change>
- **<Component/Area>**: <Specific implementation or behavioral change>

### Verification
- <Automated test command, validation script, or reproducible observation that passed>
```

### The Header Line (Subject)
- **Format**: `<type>(<scope>): <summary>`
- **Length**: Maximum **72 characters** (hard limit: 50–72 characters for GitHub UI legibility).
- **Mood**: Imperative, active voice (*"add"*, not *"added"* or *"adds"*).
- **Casing**: Lowercase summary, no trailing period.
- **Allowed Types**:
  - `feat`: New feature, capability, or user-facing addition
  - `fix`: Bug fix or error resolution
  - `refactor`: Structural code change with zero behavior change
  - `perf`: Concrete performance or memory optimization
  - `docs`: Documentation, README, or reference material
  - `style`: Formatting, whitespace, or visual presentation polish
  - `test`: Adding, updating, or fixing automated tests
  - `chore`: Tooling, configs, dependencies, or repository hygiene
- **Scope**: Lowercase noun or directory (`(architecture)`, `(auth)`, `(validator)`, `(readme)`, `(engine)`).

---

## 2. Body Structure & Visual Cohesion

### Context & Intent (The "Why")
Never just repeat what the diff shows. State the engineering motivation:
- **Poor**: *"Changed the timeout in worker.py to 30."*
- **Elite**: *"Background sync jobs timed out prematurely on high-latency database replicas. Increases the timeout ceiling to 30s and adds exponential backoff retry handling."*

### Key Changes (Grouped by Layer)
Use bold category anchors to make the diff immediately scannable:
```text
### Key Changes
- **Core Engine**: Implement exponential backoff in `WorkerPool.dispatch()`.
- **Database**: Add retry transaction wrapper for transient connection drops.
- **Configuration**: Expose `SYNC_TIMEOUT_SECONDS` with a 30s default in `.env.example`.
```

### Verification Proof
Always declare how the change was verified before committing:
```text
### Verification
- `pytest tests/test_workers.py` passed (14 unit tests).
- Verified retry logic under simulated 504 gateway timeout.
- `scripts/validate_readme.py --strict` passed with 0 errors.
```

---

## 3. Push Messages & Release Summaries

When pushing a batch of commits to a remote branch, creating a Pull Request, or announcing a repository update:

### Standard Push Summary Template
```markdown
## Repository Update: <Feature/Milestone Name>

**Summary**: <One crisp sentence stating what was accomplished in this update>.

### Highlights
| Area | Summary of Improvement |
| :--- | :--- |
| **Architecture** | Replaced in-memory state with Redis streams for resilient worker dispatch. |
| **Presentation** | Added 2-column feature grid and Mermaid data flow to `README.md`. |
| **Verification** | Added zero-dependency `validate_readme.py` and passing test suite. |

### Commits Included
- `9b8c279` feat(orchestration): introduce distributed worker queue
- `e77495a` docs(architecture): document system topology with Mermaid diagram
- `a238b91` test(workers): add idempotency test suite for duplicate events
```

---

## 4. Concrete Examples Across Scenarios

### Example A: Feature Addition
```text
feat(validator): add automated README link and secret scanner

Introduce zero-dependency Python script to validate README Markdown links,
on-disk image existence, Mermaid diagram syntax, and scan for secret leaks.

### Key Changes
- **Scripts**: Create `scripts/validate_readme.py` checking relative paths and API keys.
- **Rules**: Add strict CLI mode (`--strict`) to fail on non-fatal warnings.
- **Hygiene**: Update `.gitignore` to prevent committing compiled pycache files.

### Verification
- `python3 scripts/validate_readme.py README.md --strict` passed.
- Tested failure cases against dead links, fake tokens, and missing images.
```

### Example B: Architectural Refactor
```text
refactor(state): decouple client UI mutations from WebSocket transport

Directly applying server WebSocket events caused UI rubber-banding during
high-frequency canvas drag operations.

### Key Changes
- **Store**: Add local optimistic delta queue in `stores/canvas.ts`.
- **Reconciliation**: Apply Lamport timestamp ordering on incoming patches.
- **Documentation**: Update Architecture section in README with new state flow.

### Verification
- End-to-end canvas drag tested across two concurrent local browser sessions.
- Zero observed position jumping under simulated 150ms latency.
```

### Example C: Repository Presentation Polish
```text
docs(showcase): restructure README with 2-column feature grid and PAWT deep dives

Elevate repository presentation to elite open-source standard with crisp
5-second value proposition, structured visual grids, and defensible engineering.

### Key Changes
- **Hero**: Refactor first viewport with clean value proposition and live demo links.
- **Capabilities**: Replace vertical screenshot stack with 2-column feature table.
- **Engineering**: Document agent loop safety using Problem-Approach-Why-Tradeoff.
- **Stack**: Categorize technologies by layer (Client, Backend, Database, Infra).

### Verification
- `validate_readme.py` executed: 0 errors, 0 warnings.
- All image links verified locally on disk.
```

---

## 5. Strictly Banned Commit Anti-Patterns

Never write or accept commit/push messages with:
- ❌ **Single-word subjects**: `fix`, `update`, `clean`, `stuff`, `done`, `wip`, `test`.
- ❌ **Vague descriptions**: `fixed some bugs`, `made it better`, `addressed comments`.
- ❌ **Emoji Overload**: Leading commits with 5 different emojis that clutter git log terminals (`✨🔥🚀🎉`).
- ❌ **Unformatted text walls**: 500 words in a single unpunctuated paragraph.
- ❌ **Unverifiable claims**: Saying *"tested and 100% production ready"* with zero verification details.
- ❌ **Misleading types**: Tagging a major breaking architectural change as `style` or `chore`.
