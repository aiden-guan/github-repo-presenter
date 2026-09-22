# Clean, Professional, and Visually Cohesive Changelogs

A repository's changelog (`CHANGELOG.md`) is one of the most critical trust signals for prospective users, enterprise adopters, and technical reviewers. It bridges the gap between raw Git commits and high-level product evolution.

A changelog that is either missing, an unedited copy-paste of 50 commit subjects, or filled with vague entries like *"fixed bugs and updated things"* damages credibility.

An elite changelog is **structured**, **scannable**, and **visually cohesive** with the rest of the repository.

---

## 1. The Standard Visual Structure for Changelog Entries

Every version or milestone entry in `CHANGELOG.md` should follow this cohesive format:

```markdown
## [Version / Tag] — YYYY-MM-DD

### Summary
One or two crisp, executive sentences explaining the primary motivation and impact of this update.

### Architectural & Functional Highlights
| Component / Layer | Change | Impact |
| :--- | :--- | :--- |
| **<Component>** | <What was added or refactored> | <Tangible outcome, performance gain, or capability> |
| **<Component>** | <What was added or refactored> | <Tangible outcome, performance gain, or capability> |

### Detailed Changes

#### Added
- **<Area>**: Description of new feature or user-facing capability.
- **<Area>**: Description of new configuration option or endpoint.

#### Changed / Refactored
- **<Area>**: Description of architectural refactor or behavior change.
- **<Area>**: Performance optimization with concrete details.

#### Fixed
- **<Area>**: Description of bug fix, root cause resolved, or edge case handled.

#### Documentation & Presentation
- **<Area>**: Updates to README, architecture diagrams, or reference guides.

### Verification Proof
- <Automated test suite, validation script, or verification command that passed>.
```

---

## 2. Categorization Rules

Group changes using standard, recognizable categories:

| Category Heading | When to Use | Conventional Commit Mapping |
| :--- | :--- | :--- |
| **`Added`** | New features, public APIs, CLI flags, or capabilities. | `feat`, `feat(...)` |
| **`Changed / Refactored`** | Modifications to existing behavior, architectural refactors, or optimizations. | `refactor`, `perf`, `style` |
| **`Fixed`** | Bug fixes, security patches, or crash resolutions. | `fix`, `fix(...)` |
| **`Documentation & Presentation`** | README overhauls, new diagrams, guides, or docsite updates. | `docs`, `docs(...)` |
| **`Tooling & Hygiene`** | CI workflows, build scripts, linters, or package configs. | `chore`, `test`, `ci` |
| **`Breaking Changes`** | Any backward-incompatible API, schema, or configuration modification. | `BREAKING CHANGE`, `feat!`, `fix!` |

---

## 3. Writing Style for Changelogs

### Principles
1. **Focus on Outcomes**: Describe what the change enables or resolves, not just the file edited.
   - *Weak*: *"Edited auth.py line 45."*
   - *Strong*: *"Added JWT token refresh rotation to prevent stale session disconnects."*
2. **Imperative & Active Tone**: Use active voice (*"Add"*, *"Implement"*, *"Fix"*, *"Refactor"*).
3. **Bold Anchors**: Prefix each bullet with the relevant component or module name in bold (`- **Auth**: ...`, `- **Orchestrator**: ...`) for visual scannability.
4. **No Fluff**: Strictly ban buzzwords (*"seamlessly improved"*, *"groundbreaking fix"*). State the technical reality directly.

---

## 4. Automated Workflow with Git

Whenever a repository is updated or changes are pushed:

1. **Inspect Outgoing or Recent Commits**:
   ```bash
   git log @{u}..HEAD --oneline
   # or since the last release tag:
   git log $(git describe --tags --abbrev=0)..HEAD --oneline
   ```
2. **Synthesize the Entry**:
   - Filter out duplicate commits or minor typos.
   - Aggregate related commits into a single cohesive bullet.
   - Generate the highlight table for significant releases.
3. **Prepend to `CHANGELOG.md`**:
   - Insert the new entry immediately below the `# Changelog` header.
   - Preserve all historical version blocks untouched.
4. **Verify**:
   - Ensure all internal links, anchors, and markdown tables render cleanly.
   - Run `python3 scripts/validate_readme.py CHANGELOG.md`.

---

## 5. Banned Changelog Anti-Patterns

- ❌ **Raw Git Log Dumps**: Dumping commit hashes and raw unedited commit messages directly into the file.
- ❌ **The "Various Bug Fixes" Trap**: A single bullet saying *"Various bug fixes and performance improvements"* without naming what was fixed.
- ❌ **Unorganized Chronological Lists**: Listing 30 mixed items in chronological order without grouping by category.
- ❌ **Missing Dates**: Omitting ISO 8601 release dates (`YYYY-MM-DD`).
- ❌ **Undocumented Breaking Changes**: Burying a breaking change in the middle of a minor bullet list.
