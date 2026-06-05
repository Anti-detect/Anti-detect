# Getting started

Onboarding for **anti-detect browser automation** and **Multilogin X** — all paths use code and docs **in this repository**.

## Path A — First MLX profile

1. Install [Multilogin X](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) and create a browser profile in the desktop app.
2. Copy folder/profile UUIDs → [token-and-ids.md](token-and-ids.md).
3. `cp sdk/config.example.env sdk/.env` and paste your IDs.

## Path B — Launcher API (Python)

```bash
cd sdk/python
pip install -r requirements.txt
python recipes/01_saved_profile_lifecycle.py
```

Uses [`mlx_client.py`](../sdk/python/mlx_client.py) — start, read CDP port, stop safely.

## Path C — Playwright / Selenium

| Stack | Recipe | Guide |
|-------|--------|-------|
| Playwright | [`02_playwright_attach.py`](../sdk/python/recipes/02_playwright_attach.py) | [cookbook/02](multilogin-api/cookbook/02-playwright-attach.md) |
| Selenium | [`08_selenium_attach.py`](../sdk/python/recipes/08_selenium_attach.py) | [cookbook/08](multilogin-api/cookbook/08-selenium-attach.md) |
| Login flow | [`07_login_flow.py`](../sdk/python/recipes/07_login_flow.py) | [cookbook/07](multilogin-api/cookbook/07-login-flow-template.md) |

Architecture: [playwright-mlx-integration.md](playwright-mlx-integration.md)

## Path D — Quick profile + proxy

Ephemeral sessions without saved cookies:

[`03_quick_profile_proxy.py`](../sdk/python/recipes/03_quick_profile_proxy.py) · [cookbook/03](multilogin-api/cookbook/03-quick-profile-proxy.md)

## Path E — Multi-account rotation

[`04_batch_rotation.py`](../sdk/python/recipes/04_batch_rotation.py) + `profiles.json` · [mmo-automation-guide.md](mmo-automation-guide.md)

## Pre-flight checklist

- [ ] Python 3.10+ (for Python SDK)
- [ ] MLX agent running; launcher host/port in `.env`
- [ ] Proxy + timezone aligned with profile fingerprint
- [ ] [fingerprint-checklist.md](fingerprint-checklist.md) before scaling

## Troubleshooting

| Symptom | Check |
|---------|--------|
| Connection refused | Multilogin X app / agent not running |
| Wrong UUID | [token-and-ids.md](token-and-ids.md) |
| Playwright can't connect | `automation_type=puppeteer`; wait for CDP port |
| Selenium attach fails | `automation_type=selenium`; ChromeDriver version |

More: [faq.md](faq.md) · [cookbook/06](multilogin-api/cookbook/06-error-handling-retry.md)

## Next steps

- [repository-map.md](repository-map.md) — full repo layout
- [multilogin-api/cookbook/](multilogin-api/cookbook/) — all recipes
- [Main README](../README.md)
