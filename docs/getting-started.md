# Getting started

Onboarding for **anti-detect browser automation** and **Multilogin X** — all paths use code and docs **in this repository**.

> **Multilogin X:** [Get pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)

## Path A — First MLX profile

1. Get [Multilogin X](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — enter **`SAAS50`** or **`MIN50`** at checkout, then create a browser profile.
2. Copy folder/profile UUIDs → [token-and-ids.md](token-and-ids.md).
3. `cp sdk/config.example.env sdk/.env` and paste your IDs.

## Path B — Launcher API (Python)

```bash
cd sdk/python
pip install -r requirements.txt
python mlx_cli.py doctor          # pre-flight
python mlx_cli.py start           # start + print CDP URL
python mlx_cli.py stop            # stop saved profile
python recipes/01_saved_profile_lifecycle.py   # full lifecycle example
```

Uses [`mlx_cli.py`](../sdk/python/mlx_cli.py) for one-liners or [`mlx_client.py`](../sdk/python/mlx_client.py) in your own scripts.

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

## Path F — Cloud Real Phone (mobile)

Real Android devices in the cloud — **`MIN50`** at checkout.

[multilogin-cloud-real-phone.md](multilogin-cloud-real-phone.md) · [mobile-mmo-playbook.md](mobile-mmo-playbook.md)

## Path G — Cloud profile export

```bash
cd sdk/python
pip install -e .
# set MLX_BEARER_TOKEN in sdk/.env
mlx profiles export -o profiles.json
python recipes/12_parallel_workers.py
```

[cloud-api.md](multilogin-api/cloud-api.md) · [cookbook/12](multilogin-api/cookbook/12-cloud-export-and-workers.md)

---

**Fleet growing?** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** · **`MIN50`** (Cloud Real Phone).

---

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

More: [troubleshooting.md](troubleshooting.md) · [faq.md](faq.md) · [cookbook/06](multilogin-api/cookbook/06-error-handling-retry.md)

## Next steps

- [repository-map.md](repository-map.md) — full repo layout
- [multilogin-api/cookbook/](multilogin-api/cookbook/) — all recipes
- [Main README](../README.md)

---

**Checkout:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · promo **`SAAS50`** · **`MIN50`**
