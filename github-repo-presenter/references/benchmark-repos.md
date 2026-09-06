# Benchmark repositories

This is a pattern library, not a list of templates to copy. The approximate stars and forks below were observed on public GitHub pages on 2026-09-05 and will drift. Re-check current numbers before quoting them in a README or report.

## High-traction examples

| Repository | Approx. traction | Useful presentation pattern |
| --- | --- | --- |
| [vercel/next.js](https://github.com/vercel/next.js) | 142k stars, 31.9k forks | A short product definition followed by Getting Started, Documentation, Community, Contributing, Security, and good-first-issue paths. It makes the next action obvious for different readers. |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 131k stars, 15.2k forks | Strong product identity, links to the hosted app/docs/blog, a concrete feature list, a quick package start, integrations, and named adoption examples. The README shows what the product is before explaining the monorepo. |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 123k stars, 10.1k forks | Very restrained README: clear positioning, a documentation link, contribution guidance, a license, and accurate repository metadata. It demonstrates that a small README can be effective when the product is already legible. |
| [supabase/supabase](https://github.com/supabase/supabase) | 109k stars, 13.7k forks | A one-paragraph product promise, capability bullets, documentation and community routes, and a short “how it works” explanation. The repository surface also exposes contribution, security, and license paths. |
| [dubinc/dub](https://github.com/dubinc/dub) | 24.7k stars, 3.3k forks | Puts real product traction in context—100M+ clicks and 2M+ links monthly—then explains the stack, self-hosting, contribution flow, recommended versions, and common setup issues. Use metrics only when the owner can substantiate them. |
| [formbricks/formbricks](https://github.com/formbricks/formbricks) | 12.3k stars, 2.3k forks | Combines visual proof, a cloud demo, feature bullets, a real stack list, cloud/self-hosting paths, local development, contribution guidance, security, and license details. This is a strong model for a product repo that needs both marketing clarity and engineering depth. |

## What to borrow for a portfolio project

1. Lead with the problem, audience, and result. “A Next.js app” is implementation detail; “a private feedback workspace for small teams” is an identity.
2. Put proof near the top. A screenshot, live demo, short video, or representative terminal output lets a reviewer evaluate the work before reading the code.
3. Give readers a route. A visitor should be able to choose Demo, Quick start, Architecture, Tests, or Source without scanning a wall of text.
4. Make engineering depth legible. Name the consequential decisions and trade-offs, show the data/auth flow when it is non-obvious, and list commands that were actually run.
5. Use traction as context, not decoration. Stars, forks, releases, customers, integrations, and usage metrics are useful only when they are real, dated when appropriate, and attributable.
6. Keep trust surfaces visible. A license, contribution path, security contact, limitations, and status signal help reviewers distinguish a maintained project from a generated folder.
7. Add the portfolio-specific layer large open-source projects often omit: why the project was built, what the author learned, what they would change next, and which parts are intentionally out of scope.

## Anti-patterns to reject

- Copied README language or badges from a popular repository.
- “Production-ready,” “secure,” “scalable,” or “AI-powered” claims without a corresponding implementation and verification path.
- A giant technology list that does not explain the important choices.
- A screenshot that does not exist in the repository or cannot be reproduced from the current code.
- A live-demo link that points at a dead deployment, login wall, or unrelated product.
- Empty community files added only to make the repository checklist look complete.
