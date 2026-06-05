# Multilogin X API — documentation hub

Central index for **Multilogin X REST API** automation on the Anti-detect profile. Built from:

- Live collection: [Postman Documenter](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
- Archived spec: [`spec/`](spec/) (Postman Save-Page → JSON + code samples)
- Runnable SDK: [`sdk/`](../../sdk/)

> **Disclaimer:** Community-maintained. Not affiliated with Multilogin Inc. Verify endpoints against official docs before production.

## API categories (official overview)

| Category | Purpose |
|----------|---------|
| **Launcher** | Start/stop profiles, quick profiles (local agent) |
| **Profile Management** | Create, update, delete profiles |
| **Profile Access Management** | Sign-in, tokens, workspaces |
| **Browser Profile Data** | Unlock encrypted profile data |

## Guides in this folder

| Doc | Content |
|-----|---------|
| **[cookbook/README.md](cookbook/README.md)** | **Real-world recipes** (lifecycle, Playwright, proxy, rotation) |
| [authentication.md](authentication.md) | Bearer token, refresh, cloud vs launcher |
| [launcher-endpoints.md](launcher-endpoints.md) | Start/stop/quick paths from HTML export |
| [sdk-matrix.md](sdk-matrix.md) | Language × HTTP client matrix |
| [quick-reference.md](quick-reference.md) | One-page cheat sheet |
| [endpoints.generated.md](endpoints.generated.md) | Auto-generated path index |

## Code library

| Language | Entry |
|----------|-------|
| Python | [`sdk/python/`](../../sdk/python/) |
| C# | [`sdk/csharp/`](../../sdk/csharp/) |
| Java | [`sdk/java/`](../../sdk/java/) |

## Automation stacks

| Stack | Where |
|-------|--------|
| Playwright + MLX | [playwright-mlx-integration.md](../playwright-mlx-integration.md) |
| Recipes | [cookbook/](cookbook/README.md) |
| Profile UUIDs | [token-and-ids.md](../token-and-ids.md) |

## Full library map

[docs/libraries.md](../libraries.md)
