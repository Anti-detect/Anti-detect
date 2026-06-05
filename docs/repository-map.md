# Repository map

Everything in **Anti-detect/Anti-detect** — no external kit repos required.

## Layout

```text
Anti-detect/
├── README.md (+ 9 locale variants)
├── sdk/                          # Runnable MLX Launcher SDK
│   ├── python/                   # mlx_client, recipes, helpers
│   ├── csharp/ java/ nodejs/ curl/
│   └── config.example.env
├── docs/
│   ├── multilogin-api/           # API reference + cookbook + spec/
│   ├── getting-started.md
│   ├── token-and-ids.md
│   ├── architecture.md
│   └── …guides
└── scripts/                      # Archive, catalog, CI helpers
```

## By task

| I want to… | Go to |
|------------|--------|
| Start/stop a profile | `python sdk/python/mlx_cli.py start` · [recipe 01](../sdk/python/recipes/01_saved_profile_lifecycle.py) |
| Playwright automation | [cookbook/02](multilogin-api/cookbook/02-playwright-attach.md) |
| Selenium automation | [cookbook/08](multilogin-api/cookbook/08-selenium-attach.md) |
| Login template | [cookbook/07](multilogin-api/cookbook/07-login-flow-template.md) |
| Quick profile + proxy | [cookbook/03](multilogin-api/cookbook/03-quick-profile-proxy.md) |
| Rotate many accounts | [cookbook/04](multilogin-api/cookbook/04-multi-account-rotation.md) |
| Warm / export cookies | [cookbook/09](multilogin-api/cookbook/09-cookie-warm-export.md) |
| Import cookies JSON | [cookbook/11](multilogin-api/cookbook/11-import-cookies.md) |
| Export profiles from cloud | [cookbook/12](multilogin-api/cookbook/12-cloud-export-and-workers.md) · `mlx profiles export` |
| Scrape logged-in page | [cookbook/10](multilogin-api/cookbook/10-scrape-snapshot.md) |
| Cloud token refresh | [cloud-api.md](multilogin-api/cloud-api.md) |
| Setup doctor | `mlx doctor` |
| Cloud Real Phone | [multilogin-cloud-real-phone.md](multilogin-cloud-real-phone.md) |
| vs GoLogin / AdsPower | [comparison-multilogin-vs-gologin.md](comparison-multilogin-vs-gologin.md) |
| Troubleshooting | [troubleshooting.md](troubleshooting.md) |
| API paths & auth | [multilogin-api/](multilogin-api/README.md) |
| Raw Postman samples | [multilogin-api/spec/](multilogin-api/spec/README.md) |
| Get UUIDs | [token-and-ids.md](token-and-ids.md) |

## SDK languages

| Language | Entry |
|----------|-------|
| Python | [sdk/python/README.md](../sdk/python/README.md) |
| C# | [sdk/csharp/README.md](../sdk/csharp/README.md) |
| Java | [sdk/java/README.md](../sdk/java/README.md) |
| Node | [sdk/nodejs/README.md](../sdk/nodejs/README.md) |
| cURL | [sdk/curl/README.md](../sdk/curl/README.md) |

## Official external sources (reference only)

- [Multilogin X API — Postman](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
- [Multilogin help center](https://help.multilogin.com/en_US/multilogin-x)
- [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
