# Python — Multilogin X API

> **Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** · **`MIN50`** (Cloud Real Phone)

Two styles matching Postman exports:

| Style | Folder | Dependency |
|-------|--------|------------|
| **mlx_cli** | [`mlx_cli.py`](mlx_cli.py) | `start` / `stop` / `smoke` / `doctor` one-liners |
| **mlx_client** | [`mlx_client.py`](mlx_client.py) | Launcher API + `profile_session()` |
| **mlx_cloud_client** | [`mlx_cloud_client.py`](mlx_cloud_client.py) | Cloud API + `refresh_token()` |
| **mlx_helpers** | [`mlx_helpers.py`](mlx_helpers.py) | CDP URL, quick v3 payload, retry |
| **recipes** | [`recipes/`](recipes/) | Real-world flows (see cookbook) |
| **automation_patterns** | [`automation_patterns.py`](automation_patterns.py) | Login, Playwright/Selenium attach |
| **requests** | [`requests/`](requests/) | `pip install requests` |
| **http.client** (stdlib) | [`http_client/`](http_client/) | none |

Load `.env` without extra packages: [`mlx_env.py`](mlx_env.py).

## Examples

| Script | API call |
|--------|----------|
| [`requests/start_profile.py`](requests/start_profile.py) | Start saved profile (v2) |
| [`requests/stop_profile.py`](requests/stop_profile.py) | Stop profile (v1) |
| [`requests/quick_profile_v3.py`](requests/quick_profile_v3.py) | Ephemeral quick profile (v3) |
| [`requests/quick_profile_v2.py`](requests/quick_profile_v2.py) | Quick profile v2 |

## Recipes (start here)

| Script | Scenario |
|--------|----------|
| [`recipes/01_saved_profile_lifecycle.py`](recipes/01_saved_profile_lifecycle.py) | Start → CDP port → stop |
| [`recipes/02_playwright_attach.py`](recipes/02_playwright_attach.py) | Playwright over CDP |
| [`recipes/03_quick_profile_proxy.py`](recipes/03_quick_profile_proxy.py) | Ephemeral + proxy |
| [`recipes/04_batch_rotation.py`](recipes/04_batch_rotation.py) | Multi-account rotation |
| [`recipes/05_headless_smoke.py`](recipes/05_headless_smoke.py) | Headless smoke test |
| [`recipes/06_error_handling_retry.py`](recipes/06_error_handling_retry.py) | Retry transient start failures |
| [`recipes/07_login_flow.py`](recipes/07_login_flow.py) | Login flow template |
| [`recipes/08_selenium_attach.py`](recipes/08_selenium_attach.py) | Selenium attach |
| [`recipes/09_cookie_warm_export.py`](recipes/09_cookie_warm_export.py) | Cookie warm + JSON export |
| [`recipes/10_scrape_snapshot.py`](recipes/10_scrape_snapshot.py) | Page snapshot scrape |
| [`recipes/11_import_cookies.py`](recipes/11_import_cookies.py) | Import cookies JSON |
| [`recipes/12_cloud_export_profiles.py`](recipes/12_cloud_export_profiles.py) | Cloud search → `profiles.json` |
| [`recipes/12_parallel_workers.py`](recipes/12_parallel_workers.py) | Sharded multi-machine rotation |

Guides: [docs/multilogin-api/cookbook/](../../docs/multilogin-api/cookbook/)

Install (optional global `mlx` command):

```bash
pip install -e .
mlx doctor
mlx profiles export -o profiles.json
```

CLI without install: `python mlx_cli.py start` · `stop` · `smoke` · `profiles list`  
Pre-flight: `python mlx_cli.py doctor` or `python scripts/mlx-doctor.py`  
Tests: `python -m unittest discover -s sdk/python/tests -v`

More flows: [docs/multilogin-api/cookbook/](../../docs/multilogin-api/cookbook/).

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)

