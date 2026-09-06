#!/usr/bin/env python3
"""Install a GitHub Repo Presenter instruction adapter into another repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


TOOLKIT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_ROOT = TOOLKIT_ROOT / "templates"

ADAPTERS = {
    "agents": (("AGENTS.md", "AGENTS.md"),),
    "claude": (("AGENTS.md", "AGENTS.md"), ("CLAUDE.md", "CLAUDE.md")),
    "cursor": ((".cursor/rules/github-repo-presenter.mdc", ".cursor/rules/github-repo-presenter.mdc"),),
    "copilot": ((".github/copilot-instructions.md", ".github/copilot-instructions.md"),),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install a GitHub Repo Presenter instruction adapter into a target repository."
    )
    parser.add_argument(
        "--target",
        type=Path,
        required=True,
        help="Target repository directory (defaults are intentionally not guessed).",
    )
    parser.add_argument(
        "--adapter",
        choices=("agents", "claude", "cursor", "copilot", "all"),
        required=True,
        help="Instruction convention to install.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing adapter files. Without this flag the command is non-destructive.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned files without writing them.",
    )
    return parser.parse_args()


def selected_files(adapter: str) -> tuple[tuple[str, str], ...]:
    if adapter == "all":
        ordered: list[tuple[str, str]] = []
        seen: set[str] = set()
        for name in ("agents", "claude", "cursor", "copilot"):
            for source, destination in ADAPTERS[name]:
                if destination not in seen:
                    ordered.append((source, destination))
                    seen.add(destination)
        return tuple(ordered)
    return ADAPTERS[adapter]


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()

    if not target.is_dir():
        print(f"error: target is not a directory: {target}", file=sys.stderr)
        return 2

    files = selected_files(args.adapter)
    missing_sources = [source for source, _ in files if not (TEMPLATES_ROOT / source).is_file()]
    if missing_sources:
        print("error: missing toolkit template(s):", file=sys.stderr)
        for source in missing_sources:
            print(f"  {source}", file=sys.stderr)
        return 2

    destinations = [(TEMPLATES_ROOT / source, target / destination) for source, destination in files]
    existing = [destination for _, destination in destinations if destination.exists() or destination.is_symlink()]
    if existing and not args.force:
        print("error: refusing to overwrite existing file(s); use --force only when replacement is intentional:", file=sys.stderr)
        for destination in existing:
            print(f"  {destination}", file=sys.stderr)
        return 2

    for _, destination in destinations:
        print(f"{'would install' if args.dry_run else 'installing'} {destination}")

    if args.dry_run:
        return 0

    for source, destination in destinations:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    print(f"Installed {len(destinations)} adapter file(s) into {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
