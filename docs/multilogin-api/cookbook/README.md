# MLX API cookbook — real-world recipes

Practical guides for **Multilogin X Local Launcher API**. Each recipe explains *when* to use it, *what can go wrong*, and links to runnable code.

> **Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)  
> Not affiliated with Multilogin Inc. Test on staging before production fleets.

## Recipe index

| # | Scenario | Best for | Code |
|---|----------|----------|------|
| 01 | [Saved profile lifecycle](01-saved-profile-lifecycle.md) | Persistent logins, daily bots | Python [`01_saved_profile_lifecycle.py`](../../../sdk/python/recipes/01_saved_profile_lifecycle.py) |
| 02 | [Playwright attach over CDP](02-playwright-attach.md) | Stealth UI automation | Python [`02_playwright_attach.py`](../../../sdk/python/recipes/02_playwright_attach.py) |
| 03 | [Quick profile + proxy](03-quick-profile-proxy.md) | One-off runs, proxy QA | Python [`03_quick_profile_proxy.py`](../../../sdk/python/recipes/03_quick_profile_proxy.py) |
| 04 | [Multi-account rotation](04-multi-account-rotation.md) | MMO / multi-shop isolation | Python [`04_batch_rotation.py`](../../../sdk/python/recipes/04_batch_rotation.py) |
| 05 | [Headless smoke test](05-headless-smoke-test.md) | CI / pre-flight checks | Python [`05_headless_smoke.py`](../../../sdk/python/recipes/05_headless_smoke.py) |
| 06 | [Error handling & retry](06-error-handling-retry.md) | Launcher warming, busy profiles | [`mlx_helpers.retry`](../../../sdk/python/mlx_helpers.py) |
| 07 | [Login flow template](07-login-flow-template.md) | Account warm-up, re-login QA | [`07_login_flow.py`](../../../sdk/python/recipes/07_login_flow.py) |
| 08 | [Selenium attach](08-selenium-attach.md) | WebDriver teams | [`08_selenium_attach.py`](../../../sdk/python/recipes/08_selenium_attach.py) |
| 09 | [Cookie warm & export](09-cookie-warm-export.md) | Cold profiles, MMO prep | [`09_cookie_warm_export.py`](../../../sdk/python/recipes/09_cookie_warm_export.py) |
| 10 | [Scrape snapshot](10-scrape-snapshot.md) | Logged-in monitors | [`10_scrape_snapshot.py`](../../../sdk/python/recipes/10_scrape_snapshot.py) |
| 11 | [Import cookies](11-import-cookies.md) | Session restore / migration | [`11_import_cookies.py`](../../../sdk/python/recipes/11_import_cookies.py) |
| 12 | [Cloud export + workers](12-cloud-export-and-workers.md) | Fleet setup, sharded rotation | [`12_cloud_export_profiles.py`](../../../sdk/python/recipes/12_cloud_export_profiles.py), [`12_parallel_workers.py`](../../../sdk/python/recipes/12_parallel_workers.py) |

## Decision tree

```text
Need cookies from yesterday?
  ├─ YES → Recipe 01/02 (saved profile start/stop)
  └─ NO  → Recipe 03 (quick profile v3)

Many accounts, same script?
  └─ Recipe 04 (rotation JSON + sequential sessions)

Shipping to production?
  └─ Recipe 05 smoke → then scale

Need login automation?
  ├─ Playwright → Recipe 07
  └─ Selenium → Recipe 08

Have cookie JSON from another run?
  └─ Recipe 11 (import) ← pairs with Recipe 09 (export)

Building profiles.json from cloud?
  └─ Recipe 12 (export) → Recipe 04 or 12 workers
```

## Prerequisites

1. Multilogin X running locally (launcher reachable).
2. `MLX_FOLDER_ID` + `MLX_PROFILE_ID` from [token-and-ids.md](../../token-and-ids.md).
3. Copy [`sdk/config.example.env`](../../../sdk/config.example.env) → `sdk/.env`.

## Related

- [launcher-endpoints.md](../launcher-endpoints.md) — raw paths

---

**Ready to run recipes in production?** [Get Multilogin X](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — codes **`SAAS50`** · **`MIN50`**

- [playwright-mlx-integration.md](../../playwright-mlx-integration.md) — architecture
- [mmo-automation-guide.md](../../mmo-automation-guide.md) — operational rules
