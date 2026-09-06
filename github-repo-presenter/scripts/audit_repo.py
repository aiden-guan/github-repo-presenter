#!/usr/bin/env python3
"""Read-only inventory for a portfolio-oriented GitHub repository audit.

The script deliberately reports evidence and likely gaps instead of assigning a
quality score. It uses only the Python standard library and never edits files.
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
    "Podfile",
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
    for path in root.rglob("*"):
        if len(files) >= limit:
            break
        if not path.is_file() or any(part in {".git", "node_modules", ".next", ".turbo"} for part in path.parts):
            continue
        files.append(path.relative_to(root))
    return files


def readme_signals(readme: Path | None, root: Path) -> dict[str, Any]:
    if readme is None:
        return {
            "path": None,
            "bytes": 0,
            "headings": [],
            "images": 0,
            "links": 0,
            "code_fences": 0,
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
        "usage_or_demo": bool(re.search(r"(demo|live demo|try it|usage|deployed|production)", lowered)),
        "stack_or_architecture": bool(re.search(r"(tech stack|built with|architecture|how it works)", lowered)),
        "testing": bool(re.search(r"(test|lint|typecheck|build)", lowered)),
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


def repository_files(root: Path) -> dict[str, Any]:
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
        for path in relative_files(root)
        if path.suffix.lower() in IMAGE_EXTENSIONS and (root / path).stat().st_size < 20_000_000
    )[:20]
    root_generated = sorted(name for name in root_names if name in GENERATED_NAMES or name.endswith((".log", ".sqlite", ".sqlite3")))
    secret_candidates = sorted(
        str(path)
        for path in relative_files(root)
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


def gaps(data: dict[str, Any]) -> list[dict[str, str]]:
    files = data["files"]
    readme = files["readme"]
    signals = readme["signals"]
    results: list[dict[str, str]] = []

    if not readme["path"]:
        results.append({"priority": "blocking", "gap": "No root README was found."})
    else:
        if not signals["summary"]:
            results.append({"priority": "blocking", "gap": "README does not yet establish a clear project identity or overview."})
        if not signals["setup"]:
            results.append({"priority": "blocking", "gap": "README has no recognizable setup or development path."})
        if not signals["usage_or_demo"] and not files["images_or_media"]:
            results.append({"priority": "high", "gap": "No demo/usage proof or local visual asset was detected."})
        if not signals["stack_or_architecture"]:
            results.append({"priority": "high", "gap": "README does not explain the stack or the important engineering decisions."})
        if not signals["testing"]:
            results.append({"priority": "high", "gap": "README does not document a test, lint, typecheck, or build verification path."})
        if not signals["limitations_or_status"]:
            results.append({"priority": "polish", "gap": "README does not state project status, scope, limitations, or roadmap."})
    if not files["license"] and files["community_files"]:
        results.append({"priority": "high", "gap": "Community files exist but no license file was detected; clarify reuse terms."})
    if files["secret_name_candidates"]:
        results.append({"priority": "blocking", "gap": "Sensitive-looking filenames need review before public sharing."})
    if files["root_generated_candidates"]:
        results.append({"priority": "high", "gap": "Generated output or local artifacts appear at the repository root; confirm whether they are intentionally tracked."})
    if not files["env_example"] and any(".env" in name for name in files["root_entries"]):
        results.append({"priority": "high", "gap": "Environment configuration is present without a safe example file."})
    if not files["workflows"]:
        results.append({"priority": "polish", "gap": "No GitHub Actions workflow was detected; add CI only if the project has stable checks and needs it."})
    return results


def build_report(root: Path) -> dict[str, Any]:
    data: dict[str, Any] = {
        "root": str(root),
        "git": git_info(root),
        "package": package_info(root),
        "files": repository_files(root),
    }
    data["gaps"] = gaps(data)
    return data


def markdown_report(data: dict[str, Any]) -> str:
    files = data["files"]
    readme = files["readme"]
    package = data["package"]
    git = data["git"]
    lines = [f"# Repository audit: `{Path(data['root']).name}`", ""]
    lines.append(f"- Root: `{data['root']}`")
    lines.append(f"- Git: {'repository' if git['is_repository'] else 'not detected'}" + (f", branch `{git['branch']}`" if git.get("branch") else ""))
    if git["is_repository"]:
        lines.append(f"- Worktree: {'dirty' if git['dirty'] else 'clean'} ({git.get('changed_paths', 0)} changed paths)")
        lines.append(f"- Remotes: {', '.join(git['remotes']) if git['remotes'] else 'none detected'}")
    lines.append(f"- Manifests: {', '.join(files['manifests']) if files['manifests'] else 'none detected'}")
    if package["present"]:
        lines.append(f"- Package: `{package.get('name') or 'unnamed'}` with {package.get('package_manager') or 'no lockfile detected'}")
        if package["scripts"]:
            lines.append(f"- Package scripts: {', '.join(sorted(package['scripts']))}")
    lines.extend(["", "## Evidence", ""])
    lines.append(f"- README: `{readme['path'] or 'missing'}`")
    lines.append(f"- README images / links / code fences: {readme['images']} / {readme['links']} / {readme['code_fences']}")
    lines.append(f"- License: `{files['license'] or 'missing'}`")
    lines.append(f"- Community files: {', '.join(files['community_files']) if files['community_files'] else 'none detected'}")
    lines.append(f"- Workflows: {', '.join(files['workflows']) if files['workflows'] else 'none detected'}")
    lines.append(f"- Visual assets: {', '.join(files['images_or_media'][:8]) if files['images_or_media'] else 'none detected'}")
    lines.append(f"- Project directories: {', '.join(files['docs_or_project_dirs']) if files['docs_or_project_dirs'] else 'none detected'}")
    lines.extend(["", "## Gaps to review", ""])
    if not data["gaps"]:
        lines.append("No obvious gaps were detected by this inventory. Review the rendered README and verify the claims manually.")
    else:
        for item in data["gaps"]:
            lines.append(f"- **{item['priority']}** — {item['gap']}")
    lines.extend(["", "## Notes", "", "This is a read-only inventory. It does not prove that commands, links, deployments, or GitHub settings work.", ""])
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
