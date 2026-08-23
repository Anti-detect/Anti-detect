# Python recipes — real-world MLX Launcher flows

Runnable scenarios built on [`mlx_client.py`](../mlx_client.py) and [`mlx_helpers.py`](../mlx_helpers.py).

| Recipe | Use case | Guide |
|--------|----------|-------|
| [`01_saved_profile_lifecycle.py`](01_saved_profile_lifecycle.py) | Start → read CDP port → stop safely | [01](../../../docs/multilogin-api/cookbook/01-saved-profile-lifecycle.md) |
| [`02_playwright_attach.py`](02_playwright_attach.py) | Attach Playwright over CDP | [02](../../../docs/multilogin-api/cookbook/02-playwright-attach.md) |
| [`03_quick_profile_proxy.py`](03_quick_profile_proxy.py) | One-off ephemeral profile + proxy | [03](../../../docs/multilogin-api/cookbook/03-quick-profile-proxy.md) |
| [`04_batch_rotation.py`](04_batch_rotation.py) | Rotate many saved profiles | [04](../../../docs/multilogin-api/cookbook/04-multi-account-rotation.md) |
| [`05_headless_smoke.py`](05_headless_smoke.py) | Headless smoke test | [05](../../../docs/multilogin-api/cookbook/05-headless-smoke-test.md) |
| [`06_error_handling_retry.py`](06_error_handling_retry.py) | Retry transient start failures | [06](../../../docs/multilogin-api/cookbook/06-error-handling-retry.md) |
| [`07_login_flow.py`](07_login_flow.py) | Configurable login | [07](../../../docs/multilogin-api/cookbook/07-login-flow-template.md) |
| [`08_selenium_attach.py`](08_selenium_attach.py) | Selenium WebDriver attach | [08](../../../docs/multilogin-api/cookbook/08-selenium-attach.md) |
| [`09_cookie_warm_export.py`](09_cookie_warm_export.py) | Cookie warm + JSON export | [09](../../../docs/multilogin-api/cookbook/09-cookie-warm-export.md) |
| [`10_scrape_snapshot.py`](10_scrape_snapshot.py) | Logged-in page snapshot | [10](../../../docs/multilogin-api/cookbook/10-scrape-snapshot.md) |
| [`11_import_cookies.py`](11_import_cookies.py) | Import cookies JSON | [11](../../../docs/multilogin-api/cookbook/11-import-cookies.md) |
| [`12_cloud_export_profiles.py`](12_cloud_export_profiles.py) | Cloud search → profiles.json | [12](../../../docs/multilogin-api/cookbook/12-cloud-export-and-workers.md) |
| [`12_parallel_workers.py`](12_parallel_workers.py) | Sharded multi-machine rotation | [12](../../../docs/multilogin-api/cookbook/12-cloud-export-and-workers.md) |

## Setup

```bash
cd sdk/python
pip install -e .
cp ../config.example.env ../.env
mlx doctor
```

## Run

```bash
mlx start
python recipes/02_playwright_attach.py
mlx profiles export -o profiles.json
```

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**

