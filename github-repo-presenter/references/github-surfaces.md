# GitHub-facing presentation checklist

Use this reference when the user wants more than a local README edit. These are GitHub surfaces the skill can audit and recommend; remote mutation still requires an explicit request and a capable authenticated tool.

## README and repository metadata

- GitHub renders a README from `.github`, the repository root, or `docs`, in that order. Keep the primary visitor README in the root unless there is a strong reason to use another location.
- A repository description should say what the project does in plain language. A homepage should point to the real product, documentation, or demo.
- Topics improve discovery. Use lowercase, meaningful, hyphenated topics; GitHub allows no more than 20 topics and topic names are public even for private repositories.
- Keep README links and images relative when they belong to the repository. That keeps previews useful across branches and forks.

## Community health

For a public project that invites outside use or contribution, consider the files GitHub's community profile surfaces:

- `LICENSE` — only add or change one when the owner has chosen the license;
- `CONTRIBUTING.md` — explain the actual setup, checks, and pull request expectations;
- `CODE_OF_CONDUCT.md` — only when the owner can enforce it;
- `SECURITY.md` — give a real private reporting path and supported-version policy;
- issue forms/templates and pull request templates — only when they will be maintained.

For a personal portfolio repo, a clear README and truthful status may be more appropriate than filling every community-profile slot.

## Social preview

GitHub supports a repository social preview image. Its guidance recommends PNG, JPG, or GIF under 1 MB and at least 640×320 pixels, with 1280×640 pixels recommended for best display. Use a real project identity, strong contrast, and short readable text. Do not use a generated product screenshot that implies functionality the project does not have.

## Security and settings boundary

GitHub's repository best-practice guidance calls out Dependabot alerts, secret scanning, push protection, code scanning, and a `SECURITY.md` policy. The skill should report which local files or workflows exist and which GitHub settings still need owner action. It must not imply that a local README or workflow enabled an account-level security feature.

## Source links

- [About repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
- [Community profiles for public repositories](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)
- [Setting contribution guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [Classifying repositories with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [Customizing a repository social preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
