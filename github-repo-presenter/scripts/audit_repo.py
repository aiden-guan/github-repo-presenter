#!/usr/bin/env python3
"""Read-only inventory and archetype classifier for GitHub repository presentation audits.

Uses only the Python standard library. Never modifies target files.
Reports evidence, project archetype classification, tech stack breakdown,
and prioritized presentation gaps.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


MANIFESTS = [
    "package.json",
    "pnpm-workspace.yaml",
    "yarn.lock",
    "pnpm-lock.yaml",
    "package-lock.json",
    "bun.lock",
    "bun.lockb",
    "pyproject.toml",
    "requirements.txt",
    "Pipfile",
    "Cargo.toml",
    "go.mod",
    "Gemfile",
    "composer.json",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "Podfile",
    "Package.swift",
    "pubspec.yaml",
]

README_CANDIDATES = ["README.md", "README", "readme.md", "Readme.md"]
LICENSE_CANDIDATES = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"]
COMMUNITY_FILES = [
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CITATION.cff",
]
GENERATED_NAMES = {
    ".DS_Store",
    "Thumbs.db",
    "node_modules",
    ".next",
    ".turbo",
    ".cache",
    ".parcel-cache",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
    "__pycache__",
    "coverage",
    "dist",
    "build",
    "target",
    "out",
}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".mp4", ".mov"}
SECRET_HINTS = (".env", ".pem", ".key", ".p12", ".pfx", "credentials", "secrets")


def run_git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def read_text(path: Path, limit: int = 256_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except (OSError, UnicodeError):
        return ""


def first_existing(root: Path, candidates: list[str]) -> Path | None:
    for candidate in candidates:
        path = root / candidate
        if path.is_file():
            return path
    return None


def relative_files(root: Path, limit: int = 5000) -> list[Path]:
    files: list[Path] = []
    ignored_parts = {".git", "node_modules", ".next", ".turbo", "target", "build", "dist", ".venv", "venv", "__pycache__"}
    for path in root.rglob("*"):
        if len(files) >= limit:
            break
        if not path.is_file() or any(part in ignored_parts for part in path.parts):
            continue
        files.append(path.relative_to(root))
    return files


def classify_project(root: Path, manifests: list[str], files: list[Path]) -> dict[str, Any]:
    """Detect project archetype with evidence-based scoring."""
    scores: dict[str, int] = {
        "Product / SaaS": 0,
        "AI / Agent": 0,
        "Developer Tool / Library": 0,
        "Game / Interactive Graphics": 0,
        "Data / Machine Learning": 0,
        "Mobile Application": 0,
        "Infrastructure / Backend": 0,
        "Personal Experimental": 0,
    }
    reasons: dict[str, list[str]] = {k: [] for k in scores}

    file_str = " ".join(str(f).lower() for f in files[:1000])

    # AI / Agent signals
    ai_keywords = ["openai", "anthropic", "langchain", "langgraph", "llamaindex", "instructor", "crewai", "ollama", "transformers"]
    for kw in ai_keywords:
        if kw in file_str:
            scores["AI / Agent"] += 3
            reasons["AI / Agent"].append(f"Found '{kw}' in codebase/paths")
            break
    if any("prompt" in p.name.lower() or "agent" in p.name.lower() or "eval" in p.parts for p in files):
        scores["AI / Agent"] += 4
        reasons["AI / Agent"].append("Found agent/prompt/eval directory or filenames")

    # Mobile Application signals
    if any(m in manifests for m in ("pubspec.yaml", "Podfile", "Package.swift")):
        scores["Mobile Application"] += 6
        reasons["Mobile Application"].append("Found mobile manifest (pubspec/Podfile/Package.swift)")
    if any(p.name in ("app.json", "expo-env.d.ts") or "ios" in p.parts or "android" in p.parts for p in files):
        scores["Mobile Application"] += 5
        reasons["Mobile Application"].append("Found iOS/Android or Expo project structure")

    # Game signals
    game_keywords = ["three", "phaser", "pixi", "godot", "unity", "pygame", "raylib", "wgpu", "canvas", "gameloop"]
    for kw in game_keywords:
        if kw in file_str:
            scores["Game / Interactive Graphics"] += 4
            reasons["Game / Interactive Graphics"].append(f"Found game engine hint '{kw}'")
            break
    if any("sprites" in p.parts or "shaders" in p.parts or "scenes" in p.parts for p in files):
        scores["Game / Interactive Graphics"] += 4
        reasons["Game / Interactive Graphics"].append("Found sprites/shaders/scenes directories")

    # Data / ML signals
    if any(m in manifests for m in ("requirements.txt", "pyproject.toml", "Pipfile")):
        data_keywords = ["pandas", "numpy", "torch", "scikit-learn", "polars", "dbt", "airflow", "mlflow", "jupyter"]
        for kw in data_keywords:
            if kw in file_str:
                scores["Data / Machine Learning"] += 3
                reasons["Data / Machine Learning"].append(f"Found ML/data dependency hint '{kw}'")
                break
    if any(p.suffix == ".ipynb" or "notebooks" in p.parts or "dataset" in p.parts for p in files):
        scores["Data / Machine Learning"] += 4
        reasons["Data / Machine Learning"].append("Found Jupyter notebooks or dataset folders")

    # Infrastructure / Backend signals
    infra_files = ["docker-compose.yml", "docker-compose.yaml", "Dockerfile", "Makefile", "k8s", "proto"]
    for inf in infra_files:
        if (root / inf).exists() or any(inf in p.parts for p in files):
            scores["Infrastructure / Backend"] += 2
            reasons["Infrastructure / Backend"].append(f"Found infra configuration '{inf}'")
    if "go.mod" in manifests or "Cargo.toml" in manifests:
        scores["Infrastructure / Backend"] += 2
        scores["Developer Tool / Library"] += 2
        reasons["Infrastructure / Backend"].append("Built with systems language (Go/Rust)")

    # Product / SaaS signals
    saas_dirs = ["app", "pages", "components", "routes", "server", "prisma", "drizzle"]
    found_saas_dirs = [d for d in saas_dirs if (root / d).is_dir() or any(d in p.parts for p in files)]
    if len(found_saas_dirs) >= 2:
        scores["Product / SaaS"] += 5
        reasons["Product / SaaS"].append(f"Found web/SaaS directories: {', '.join(found_saas_dirs[:3])}")
    if any("next" in str(p) or "remix" in str(p) or "vite" in str(p) for p in files):
        scores["Product / SaaS"] += 3
        reasons["Product / SaaS"].append("Found web application framework indicators")

    # Developer Tool / Library signals
    pkg = root / "package.json"
    if pkg.is_file():
        text = read_text(pkg)
        if '"exports"' in text or '"types"' in text or '"bin"' in text:
            scores["Developer Tool / Library"] += 4
            reasons["Developer Tool / Library"].append("package.json exports library or CLI binary")
    if any(p.parts and p.parts[0] in ("lib", "packages", "crates", "cmd") for p in files):
        scores["Developer Tool / Library"] += 3
        reasons["Developer Tool / Library"].append("Found library/CLI source structure (lib/packages/cmd)")

    # Fallback to Personal Experimental if low total signals or solo recent repo
    top_archetype = max(scores, key=lambda k: scores[k])
    if scores[top_archetype] <= 2:
        scores["Personal Experimental"] += 4
        reasons["Personal Experimental"].append("Focused single-purpose codebase or exploratory prototype")

    sorted_archetypes = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    primary = sorted_archetypes[0][0]
    secondary = sorted_archetypes[1][0] if sorted_archetypes[1][1] > 2 else None

    return {
        "primary": primary,
        "primary_score": scores[primary],
        "secondary": secondary,
        "evidence": reasons[primary],
        "scores": scores,
    }


def analyze_tech_stack(root: Path, manifests: list[str]) -> dict[str, list[str]]:
    """Group detected technologies by architectural responsibility."""
    stack: dict[str, list[str]] = {
        "client": [],
        "backend": [],
        "database_or_storage": [],
        "ai_or_ml": [],
        "infrastructure": [],
    }

    # Inspect package.json
    pkg_path = root / "package.json"
    if pkg_path.is_file():
        try:
            data = json.loads(read_text(pkg_path))
            all_deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            for dep in all_deps:
                if dep in ("react", "vue", "svelte", "next", "remix", "tailwind", "tailwindcss", "radix-ui", "three"):
                    stack["client"].append(dep)
                elif dep in ("express", "fastify", "hono", "nest", "@nestjs/core", "trpc", "@trpc/server"):
                    stack["backend"].append(dep)
                elif dep in ("prisma", "@prisma/client", "drizzle-orm", "pg", "mongodb", "ioredis", "redis", "supabase"):
                    stack["database_or_storage"].append(dep)
                elif dep in ("openai", "anthropic", "langchain", "@langchain/core", "ai", "llamaindex"):
                    stack["ai_or_ml"].append(dep)
                elif dep in ("docker", "turbo", "tsx", "vite"):
                    stack["infrastructure"].append(dep)
        except json.JSONDecodeError:
            pass

    # Inspect Python files
    py_path = root / "pyproject.toml"
    req_path = root / "requirements.txt"
    py_text = (read_text(py_path) if py_path.is_file() else "") + "\n" + (read_text(req_path) if req_path.is_file() else "")
    if py_text:
        lowered = py_text.lower()
        if "fastapi" in lowered or "flask" in lowered or "django" in lowered or "tornado" in lowered:
            stack["backend"].append("FastAPI/Python Web Framework")
        if "sqlalchemy" in lowered or "psycopg2" in lowered or "asyncpg" in lowered or "pymongo" in lowered or "redis" in lowered:
            stack["database_or_storage"].append("SQLAlchemy/Postgres/Redis")
        if "openai" in lowered or "anthropic" in lowered or "langchain" in lowered or "torch" in lowered or "transformers" in lowered:
            stack["ai_or_ml"].append("OpenAI/PyTorch/AI Framework")

    # Infrastructure files
    if (root / "Dockerfile").is_file():
        stack["infrastructure"].append("Docker")
    if (root / "docker-compose.yml").is_file() or (root / "docker-compose.yaml").is_file():
        stack["infrastructure"].append("Docker Compose")
    if (root / ".github" / "workflows").is_dir():
        stack["infrastructure"].append("GitHub Actions")

    return {k: sorted(set(v)) for k, v in stack.items()}


def readme_signals(readme: Path | None, root: Path) -> dict[str, Any]:
    if readme is None:
        return {
            "path": None,
            "bytes": 0,
            "headings": [],
            "images": 0,
            "links": 0,
            "code_fences": 0,
            "mermaid_diagrams": 0,
            "signals": {},
        }

    text = read_text(readme)
    headings = [
        re.sub(r"\s+#*$", "", match.group(1)).strip()
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    ]
    lowered = text.lower()
    terms = {
        "summary": bool(re.search(r"^#{1,6}\s+(about|overview|what|introduction)", lowered, re.MULTILINE))
        or len(text.strip()) >= 180,
        "features": bool(re.search(r"^#{1,6}\s+.*(feature|capabilit)", lowered, re.MULTILINE)),
        "setup": bool(re.search(r"^#{1,6}\s+.*(getting started|quick start|installation|setup|development)", lowered, re.MULTILINE)),
        "usage_or_demo": bool(re.search(r"(demo|live demo|try it|usage|walkthrough|recording)", lowered)),
        "stack_or_architecture": bool(re.search(r"(tech stack|built with|architecture|how it works|system flow)", lowered)),
        "engineering_highlights": bool(re.search(r"(engineering|trade-off|tradeoff|decisions|under the hood|deep dive)", lowered)),
        "testing": bool(re.search(r"(test|lint|typecheck|build|verification)", lowered)),
        "limitations_or_status": bool(re.search(r"(status|roadmap|limitations|known issues|trade-offs|tradeoffs)", lowered)),
        "contributing": bool(re.search(r"(contribut|pull request|issues)", lowered)),
        "license": bool(re.search(r"license", lowered)),
        "security": bool(re.search(r"security|vulnerabilit", lowered)),
    }
    return {
        "path": str(readme.relative_to(root)),
        "bytes": readme.stat().st_size,
        "headings": headings,
        "images": len(re.findall(r"!\[[^\]]*\]\([^)]*\)", text)),
        "links": len(re.findall(r"\[[^\]]+\]\([^)]*\)", text)),
        "code_fences": len(re.findall(r"^```", text, re.MULTILINE)) // 2,
        "mermaid_diagrams": len(re.findall(r"^```mermaid", text, re.MULTILINE)),
        "signals": terms,
    }


def package_info(root: Path) -> dict[str, Any]:
    package = root / "package.json"
    if not package.is_file():
        return {"present": False, "scripts": {}, "name": None, "package_manager": None}
    try:
        data = json.loads(read_text(package))
    except json.JSONDecodeError:
        return {"present": True, "scripts": {}, "name": None, "package_manager": "invalid-json"}
    manager = None
    for lockfile, name in (
        ("pnpm-lock.yaml", "pnpm"),
        ("yarn.lock", "yarn"),
        ("bun.lock", "bun"),
        ("bun.lockb", "bun"),
        ("package-lock.json", "npm"),
    ):
        if (root / lockfile).exists():
            manager = name
            break
    return {
        "present": True,
        "name": data.get("name"),
        "private": data.get("private", False),
        "scripts": data.get("scripts", {}) if isinstance(data.get("scripts", {}), dict) else {},
        "package_manager": manager,
    }


def git_info(root: Path) -> dict[str, Any]:
    inside = run_git(root, "rev-parse", "--is-inside-work-tree") == "true"
    if not inside:
        return {"is_repository": False, "branch": None, "dirty": None, "remotes": []}
    status = run_git(root, "status", "--short") or ""
    remotes = run_git(root, "remote", "-v") or ""
    remote_names = sorted({line.split()[0] for line in remotes.splitlines() if line.split()})
    return {
        "is_repository": True,
        "branch": run_git(root, "branch", "--show-current"),
        "dirty": bool(status),
        "changed_paths": len(status.splitlines()),
        "remotes": remote_names,
    }


def repository_files(root: Path, all_files: list[Path]) -> dict[str, Any]:
    root_names = sorted(path.name for path in root.iterdir() if path.name != ".git")
    manifests = [name for name in MANIFESTS if (root / name).exists()]
    readme = first_existing(root, README_CANDIDATES)
    license_file = first_existing(root, LICENSE_CANDIDATES)
    community = [name for name in COMMUNITY_FILES if (root / name).is_file()]
    github_dir = root / ".github"
    workflows = []
    if (github_dir / "workflows").is_dir():
        workflows = sorted(str(path.relative_to(root)) for path in (github_dir / "workflows").glob("*") if path.is_file())
    images = sorted(
        str(path)
        for path in all_files
        if path.suffix.lower() in IMAGE_EXTENSIONS and (root / path).stat().st_size < 20_000_000
    )[:20]
    root_generated = sorted(name for name in root_names if name in GENERATED_NAMES or name.endswith((".log", ".sqlite", ".sqlite3")))
    secret_candidates = sorted(
        str(path)
        for path in all_files
        if any(hint in path.name.lower() for hint in SECRET_HINTS)
        and path.name not in {".env.example", ".env.sample", ".env.template"}
    )[:40]
    docs_dirs = [name for name in ("docs", "documentation", "examples", "demo", "screenshots", "assets", "public", "tests", "test") if (root / name).is_dir()]
    return {
        "root_entries": root_names,
        "manifests": manifests,
        "readme": readme_signals(readme, root),
        "license": str(license_file.relative_to(root)) if license_file else None,
        "community_files": community,
        "workflows": workflows,
        "images_or_media": images,
        "docs_or_project_dirs": docs_dirs,
        "root_generated_candidates": root_generated,
        "secret_name_candidates": secret_candidates,
        "env_example": any((root / name).is_file() for name in (".env.example", ".env.sample", ".env.template")),
    }


def compute_gaps(data: dict[str, Any]) -> list[dict[str, str]]:
    files = data["files"]
    readme = files["readme"]
    signals = readme["signals"]
    archetype = data["archetype"]["primary"]
    results: list[dict[str, str]] = []

    if not readme["path"]:
        results.append({"priority": "blocking", "gap": "No root README was found."})
        return results

    if not signals["summary"]:
        results.append({"priority": "blocking", "gap": "README does not yet establish a clear project identity or value proposition in the first viewport."})
    if not signals["setup"]:
        results.append({"priority": "blocking", "gap": "README has no recognizable setup or quickstart path."})

    # Archetype-specific gaps
    if archetype in ("Product / SaaS", "Game / Interactive Graphics", "Mobile Application"):
        if readme["images"] == 0 and not files["images_or_media"]:
            results.append({"priority": "high", "gap": f"Project archetype is '{archetype}' but no visual asset, demo, or UI screenshot exists."})
    elif archetype in ("AI / Agent", "Infrastructure / Backend"):
        if readme["mermaid_diagrams"] == 0 and not signals["stack_or_architecture"]:
            results.append({"priority": "high", "gap": f"Project archetype is '{archetype}' but lacks an architecture flow or Mermaid diagram."})
    elif archetype == "Developer Tool / Library":
        if readme["code_fences"] == 0:
            results.append({"priority": "high", "gap": "Developer tool README lacks copy-pasteable usage code snippets in the first viewport."})

    if not signals["engineering_highlights"]:
        results.append({"priority": "high", "gap": "README lacks technical depth: missing defensible engineering decisions, trade-offs, or Problem-Approach-Why highlights."})
    if not signals["stack_or_architecture"]:
        results.append({"priority": "high", "gap": "README does not organize the tech stack by responsibility (Client, Backend, Data, Infra)."})
    if not signals["testing"]:
        results.append({"priority": "polish", "gap": "README does not document a test, lint, or build verification command."})
    if not signals["limitations_or_status"]:
        results.append({"priority": "polish", "gap": "README does not state project status, maturity, or known limitations."})

    # File and hygiene gaps
    if not files["license"]:
        results.append({"priority": "high", "gap": "No license file was detected; clarify open-source or proprietary terms."})
    if files["secret_name_candidates"]:
        results.append({"priority": "blocking", "gap": "Sensitive-looking filenames detected in repository tree; review before public sharing."})
    if files["root_generated_candidates"]:
        results.append({"priority": "high", "gap": "Generated artifacts appear at repository root; confirm if intentionally tracked."})
    if not files["env_example"] and any(".env" in name for name in files["root_entries"]):
        results.append({"priority": "high", "gap": "Environment file present without a safe .env.example template."})

    return results


def build_report(root: Path) -> dict[str, Any]:
    all_files = relative_files(root)
    git = git_info(root)
    pkg = package_info(root)
    files = repository_files(root, all_files)
    archetype = classify_project(root, files["manifests"], all_files)
    stack = analyze_tech_stack(root, files["manifests"])

    data: dict[str, Any] = {
        "root": str(root),
        "git": git,
        "archetype": archetype,
        "package": pkg,
        "tech_stack": stack,
        "files": files,
    }
    data["gaps"] = compute_gaps(data)
    return data


def markdown_report(data: dict[str, Any]) -> str:
    files = data["files"]
    readme = files["readme"]
    package = data["package"]
    git = data["git"]
    arch = data["archetype"]
    stack = data["tech_stack"]

    lines = [f"# Repository Audit: `{Path(data['root']).name}`", ""]
    lines.append(f"- **Root**: `{data['root']}`")
    lines.append(f"- **Git**: {'Repository' if git['is_repository'] else 'Not a git repository'}" + (f" on branch `{git['branch']}`" if git.get("branch") else ""))
    if git["is_repository"]:
        lines.append(f"- **Worktree**: {'Dirty' if git['dirty'] else 'Clean'} ({git.get('changed_paths', 0)} modified paths)")
        lines.append(f"- **Remotes**: {', '.join(git['remotes']) if git['remotes'] else 'none detected'}")

    lines.append(f"- **Archetype Classification**: **{arch['primary']}** (Score: {arch['primary_score']})")
    if arch.get("secondary"):
        lines.append(f"- **Secondary Archetype**: {arch['secondary']}")
    if arch.get("evidence"):
        lines.append(f"- **Classification Signals**: {'; '.join(arch['evidence'][:3])}")

    lines.append(f"- **Manifests**: {', '.join(files['manifests']) if files['manifests'] else 'none detected'}")
    if package["present"]:
        lines.append(f"- **Package**: `{package.get('name') or 'unnamed'}` ({package.get('package_manager') or 'no lockfile'})")
        if package["scripts"]:
            lines.append(f"- **Scripts**: {', '.join(sorted(package['scripts']))}")

    lines.extend(["", "## Detected Tech Stack Layers", ""])
    for layer, items in stack.items():
        if items:
            lines.append(f"- **{layer.replace('_', ' ').title()}**: {', '.join(items)}")

    lines.extend(["", "## Presentation Evidence", ""])
    lines.append(f"- **README**: `{readme['path'] or 'missing'}` ({readme['bytes']} bytes)")
    lines.append(f"- **Visual Assets**: {len(files['images_or_media'])} images detected (`assets/readme/` or equivalent)")
    lines.append(f"- **Mermaid Diagrams**: {readme['mermaid_diagrams']} in README")
    lines.append(f"- **Code Fences / Headings**: {readme['code_fences']} code fences, {len(readme['headings'])} headings")
    lines.append(f"- **License**: `{files['license'] or 'missing'}`")
    lines.append(f"- **Community Files**: {', '.join(files['community_files']) if files['community_files'] else 'none detected'}")
    lines.append(f"- **CI Workflows**: {', '.join(files['workflows']) if files['workflows'] else 'none detected'}")

    lines.extend(["", "## Prioritized Gaps to Resolve", ""])
    if not data["gaps"]:
        lines.append("No automated gaps detected. Perform manual visual inspection and verify documented reproduction steps.")
    else:
        for item in data["gaps"]:
            lines.append(f"- **[{item['priority'].upper()}]** {item['gap']}")

    lines.extend(["", "---", "*Note: This is a read-only audit. Claims and workflows require verification against actual execution.*", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="repository path (default: current directory)")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 2

    data = build_report(root)
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(markdown_report(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
