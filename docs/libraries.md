# Library sky — Multilogin & anti-detect ecosystem

One map for everything linked from **Anti-detect/Anti-detect**: API SDKs, OSS kits, docs, and automation stacks.

```mermaid
flowchart TB
  H[Anti-detect Hub] --> API[docs/multilogin-api]
  H --> SDK[sdk/ Python C# Java]
  H --> KIT[@multilogin-automation]
  API --> POST[Postman + spec archive]
  SDK --> LAUNCH[Local Launcher API]
  KIT --> TPL[templates Playwright Python]
  KIT --> COOK[cookie robots]
  KIT --> FP[fingerprint OSS]
```

## Tier 1 — API & SDK (this repo)

| Library | Languages | Link |
|---------|-----------|------|
| **MLX API hub** | Docs | [multilogin-api/README.md](multilogin-api/README.md) |
| **API cookbook** | Recipes | [multilogin-api/cookbook/README.md](multilogin-api/cookbook/README.md) |
| **sdk/** | Python, C#, Java, Node, cURL | [sdk/README.md](../sdk/README.md) |
| **python/recipes** | Real flows | [sdk/python/recipes/](../sdk/python/recipes/) |
| **mlx_client** | Python class | [sdk/python/mlx_client.py](../sdk/python/mlx_client.py) |
| **Postman archive** | JSON + code samples | [multilogin-api/spec/README.md](multilogin-api/spec/README.md) |
| Playwright attach | Guide | [playwright-mlx-integration.md](playwright-mlx-integration.md) |
| MMO patterns | Guide | [mmo-automation-guide.md](mmo-automation-guide.md) |

## Tier 2 — @multilogin-automation (code)

| Repo | Stack | Use |
|------|-------|-----|
| multilogin-automation | Python, MLX API | Master hub + `/templates` |
| multilogin-x-getting-started | Onboarding | Install & first profile |
| multilogin-x-id-token-retrieval-tools | Auth | Tokens, IDs |
| multilogin_x_auto_cookie_collector | Python | Cookie warming |
| mlx_cookie_robot | MLX | Cookie robot |
| quick_profile_proxy | Python | Quick profile + proxy |
| mlx_proxy_details | Python | Read proxy metadata |
| MultiLogin | Python | MLX automation fork |
| undetectable-fingerprint-browser | Py/Node | OSS fingerprint |
| CloakBrowser-Manager | Self-hosted | Profile manager |
| openMultiLogin | OSS | Open implementation |
| laravel-multilogin-sdk | PHP | Laravel |
| user-agent-utils | Java/etc. | UA parsing |
| SessionBox | Utility | Multi-login sessions |

Full table: [open-source-catalog.md](open-source-catalog.md)

## Tier 3 — Learning & SEO docs

| Doc | Topic |
|-----|--------|
| [getting-started.md](getting-started.md) | Paths A–E |
| [fingerprint-checklist.md](fingerprint-checklist.md) | Fleet QA |
| [browser-landscape.md](browser-landscape.md) | Market keywords |
| [glossary.md](glossary.md) | Terms EN/VI/ZH/RU |
| [locales.md](locales.md) | 10 README languages |

## Search keywords

`multilogin x api`, `multilogin api python`, `multilogin api csharp`, `multilogin api java`, `browser profile automation`, `anti-detect browser github`, `playwright multilogin`, `mlx launcher api`

## Official sources

- [Postman — Multilogin X API](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
- [Multilogin help](https://help.multilogin.com/en_US/multilogin-x)

## Pricing

**SAAS50** / **MIN50** — [urls.md](urls.md)
