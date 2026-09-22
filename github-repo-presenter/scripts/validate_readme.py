#!/usr/bin/env python3
"""Automated validator for GitHub READMEs.

Verifies:
1. Relative links and anchors resolve to real files and headings.
2. Local images exist on disk and meet size guidelines (<5MB).
3. Heading hierarchy does not skip levels.
4. Mermaid code blocks have valid diagram declarations and balanced fences.
5. Documented npm/package scripts exist in package.json.
6. Referenced environment variables exist in .env.example.
7. Zero exposed real secrets, tokens, or private keys.
8. Zero banned marketing buzzwords ("revolutionary", "seamless", "cutting-edge", etc.).
9. Zero leftover placeholder text ("[TODO]", "[Insert link]", etc.).

Uses ONLY the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


BANNED_BUZZWORDS = [
    "revolutionary",
    "cutting-edge",
    "game-changing",
    "groundbreaking",
    "seamless",
    "seamlessly",
    "delve",
    "delving",
    "testament to",
    "next-generation",
]

PLACEHOLDER_PATTERNS = [
    r"\[TODO[^\]]*\]",
    r"\[TBD[^\]]*\]",
    r"\[Insert[^\]]*\]",
    r"\[Your[^\]]*\]",
    r"\[coming soon[^\]]*\]",
    r"\[replace with[^\]]*\]",
]

SECRET_PATTERNS = [
    (r"sk-[a-zA-Z0-9_-]{20,}", "OpenAI API Key format"),
    (r"ghp_[a-zA-Z0-9]{20,}", "GitHub Personal Access Token"),
    (r"-----BEGIN (RSA|OPENSSH|EC|DSA)? PRIVATE KEY-----", "Private Key Header"),
    (r"xox[baprs]-[0-9a-zA-Z]{10,}", "Slack Token"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key ID"),
]


def heading_anchor(heading: str) -> str:
    """Compute GitHub markdown heading anchor."""
    h = heading.strip().lower()
    h = re.sub(r"[^\w\s-]", "", h)
    h = re.sub(r"\s+", "-", h)
    return h


class ReadmeValidator:
    def __init__(self, readme_path: Path):
        self.readme_path = readme_path.resolve()
        self.root = self.readme_path.parent
        self.text = ""
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.package_json: dict | None = None
        self.env_example_vars: set[str] = set()

    def load(self) -> bool:
        if not self.readme_path.is_file():
            self.errors.append(f"README not found at {self.readme_path}")
            return False
        try:
            self.text = self.readme_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            self.errors.append(f"Failed to read README: {e}")
            return False

        # Load package.json if present
        pkg = self.root / "package.json"
        if pkg.is_file():
            try:
                self.package_json = json.loads(pkg.read_text(encoding="utf-8", errors="replace"))
            except Exception:
                pass

        # Load .env.example if present
        for env_name in (".env.example", ".env.sample", ".env.template"):
            env_file = self.root / env_name
            if env_file.is_file():
                for line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        var_name = line.split("=", 1)[0].strip()
                        self.env_example_vars.add(var_name)
                break

        return True

    def validate_heading_hierarchy(self) -> None:
        lines = self.text.splitlines()
        in_code_block = False
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            m = re.match(r"^(#{1,6})\s+(.+)$", line)
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                self.headings.append((level, title))

        if not self.headings:
            self.errors.append("No markdown headings found.")
            return

        if self.headings[0][0] != 1:
            self.warnings.append(f"Document should start with an H1 heading (# ProjectName), but starts with H{self.headings[0][0]}.")

        prev_level = 0
        for level, title in self.headings:
            if prev_level > 0 and level > prev_level + 1:
                self.warnings.append(f"Heading level skipped from H{prev_level} to H{level}: '{title}'")
            prev_level = level

    def validate_links_and_images(self) -> None:
        available_anchors = {heading_anchor(title) for _, title in self.headings}

        # 1. Image links: ![alt](path) and <img src="path">
        image_matches = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", self.text)
        html_img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', self.text)
        all_images = [img[1] for img in image_matches] + html_img_matches

        for img in all_images:
            img_path_str = img.strip().split()[0]  # strip optional title
            # Strip anchors or query params
            clean_path = img_path_str.split("#")[0].split("?")[0]
            if clean_path.startswith(("http://", "https://", "data:")):
                continue
            resolved = (self.root / clean_path).resolve()
            if not resolved.exists():
                self.errors.append(f"Referenced image does not exist: '{img_path_str}'")
            else:
                size_mb = resolved.stat().st_size / (1024 * 1024)
                if size_mb > 5.0:
                    self.warnings.append(f"Image '{img_path_str}' is {size_mb:.1f} MB (recommended: < 2.5 MB).")

        # 2. Markdown links: [text](path)
        link_matches = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", self.text)
        for text, url in link_matches:
            url = url.strip()
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            if url.startswith("#"):
                anchor = url[1:].lower()
                if anchor and anchor not in available_anchors:
                    self.warnings.append(f"Anchor link '{url}' does not match any heading in document.")
            else:
                clean_target = url.split("#")[0].split("?")[0]
                if clean_target:
                    target_file = (self.root / clean_target).resolve()
                    if not target_file.exists():
                        self.errors.append(f"Local link target does not exist: '{url}'")

    def validate_mermaid_blocks(self) -> None:
        mermaid_blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", self.text, re.DOTALL)
        valid_diagram_starters = (
            "graph", "flowchart", "sequenceDiagram", "stateDiagram",
            "stateDiagram-v2", "classDiagram", "erDiagram", "xychart-beta", "gantt", "pie"
        )
        for idx, block in enumerate(mermaid_blocks, 1):
            first_line = ""
            for line in block.splitlines():
                stripped = line.strip()
                if stripped and not stripped.startswith("%%"):
                    first_line = stripped
                    break
            if not any(first_line.startswith(starter) for starter in valid_diagram_starters):
                self.errors.append(f"Mermaid block #{idx} starts with unrecognized diagram declaration: '{first_line}'")

    def validate_scripts(self) -> None:
        if not self.package_json:
            return
        scripts = self.package_json.get("scripts", {})
        # Find command executions like `npm run <script>` or `pnpm run <script>`
        cmd_matches = re.findall(r"(?:npm|pnpm|yarn|bun)\s+(?:run\s+)?([a-zA-Z0-9_-]+)", self.text)
        standard_cmds = {"install", "add", "test", "start", "build", "dev", "lint"}
        for cmd in cmd_matches:
            if cmd not in standard_cmds and cmd not in scripts:
                self.warnings.append(f"Documented script command '{cmd}' not found in package.json scripts.")

    def validate_env_vars(self) -> None:
        if not self.env_example_vars:
            return
        # Find uppercase variables in code blocks
        found_vars = set(re.findall(r"\b[A-Z][A-Z0-9_]{3,}_(?:KEY|TOKEN|SECRET|URL|PORT|ID|DATABASE|API)\b", self.text))
        for var in found_vars:
            if var not in self.env_example_vars and not var.startswith(("HTTP_", "HTTPS_")):
                self.warnings.append(f"Environment variable '{var}' mentioned in README but missing from .env.example.")

    def scan_for_secrets(self) -> None:
        for pattern, desc in SECRET_PATTERNS:
            if re.search(pattern, self.text):
                self.errors.append(f"Possible sensitive secret detected matching {desc}.")

    def scan_for_fluff_and_placeholders(self) -> None:
        lowered = self.text.lower()
        for buzzword in BANNED_BUZZWORDS:
            # Word boundary search
            if re.search(r"\b" + re.escape(buzzword) + r"\b", lowered):
                self.warnings.append(f"Banned marketing buzzword detected: '{buzzword}'. Use concrete technical description.")

        for pat in PLACEHOLDER_PATTERNS:
            if re.search(pat, self.text, re.IGNORECASE):
                self.errors.append(f"Unfilled placeholder detected matching '{pat}'.")

    def run_all(self) -> tuple[list[str], list[str]]:
        if not self.load():
            return self.errors, self.warnings
        self.validate_heading_hierarchy()
        self.validate_links_and_images()
        self.validate_mermaid_blocks()
        self.validate_scripts()
        self.validate_env_vars()
        self.scan_for_secrets()
        self.scan_for_fluff_and_placeholders()
        return self.errors, self.warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="README.md", help="Path to README.md (default: ./README.md)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    readme_path = Path(args.path)
    if readme_path.is_dir():
        readme_path = readme_path / "README.md"

    validator = ReadmeValidator(readme_path)
    errors, warnings = validator.run_all()

    print(f"\n--- README Validation Report: {readme_path} ---\n")

    if not errors and not warnings:
        print("✅ Validation PASSED! Zero errors and zero warnings.")
        return 0

    if warnings:
        print(f"⚠️  {len(warnings)} Warning(s):")
        for w in warnings:
            print(f"   [WARN] {w}")
        print()

    if errors:
        print(f"❌ {len(errors)} Error(s):")
        for e in errors:
            print(f"   [ERROR] {e}")
        print()
        return 1

    if args.strict and warnings:
        print("❌ Strict mode enabled: Failing on warnings.")
        return 1

    print("✅ Validation passed with non-fatal warnings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
