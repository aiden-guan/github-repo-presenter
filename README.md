# GitHub Repo Presenter

`github-repo-presenter` is a downloadable Codex skill for turning an unfinished or AI-assisted repository into a credible portfolio showcase. It audits the repository, improves the README and supporting docs, surfaces engineering decisions, and verifies what can actually be claimed.

## Install locally

Codex loads user skills from `~/.agents/skills` and follows symlinked skill folders. The simplest copy install is:

```bash
mkdir -p ~/.agents/skills
cp -R github-repo-presenter ~/.agents/skills/github-repo-presenter
```

For a clone-based install:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git ~/github-repo-presenter
mkdir -p ~/.agents/skills
ln -sfn ~/github-repo-presenter/github-repo-presenter ~/.agents/skills/github-repo-presenter
```

For local development, point the symlink at this checkout instead:

```bash
mkdir -p ~/.agents/skills
ln -sfn "/Users/aidenguan/Documents/ChatGPT/Github Skill/github-repo-presenter" ~/.agents/skills/github-repo-presenter
```

If the skill does not appear immediately, restart Codex. You can also invoke `$skill-installer` in Codex and ask it to download the skill from the GitHub repository.

## Use

Invoke it explicitly:

```text
$github-repo-presenter Audit this repository and make it portfolio-ready.
```

It preserves unrelated work, avoids fabricated proof, and distinguishes implemented, locally verified, remotely configured, and unverified work.

The skill includes a read-only inventory script at `github-repo-presenter/scripts/audit_repo.py`, a benchmark study of high-traction repositories, and a GitHub-facing presentation checklist.
