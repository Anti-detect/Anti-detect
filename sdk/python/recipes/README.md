# Python recipes — real-world MLX Launcher flows

Runnable scenarios built on [`mlx_client.py`](../mlx_client.py) and [`mlx_helpers.py`](../mlx_helpers.py).

| Recipe | Use case | Guide |
|--------|----------|-------|
| [`01_saved_profile_lifecycle.py`](01_saved_profile_lifecycle.py) | Start → read CDP port → stop safely | [01-saved-profile-lifecycle.md](../../../docs/multilogin-api/cookbook/01-saved-profile-lifecycle.md) |
| [`02_playwright_attach.py`](02_playwright_attach.py) | Attach Playwright over CDP | [02-playwright-attach.md](../../../docs/multilogin-api/cookbook/02-playwright-attach.md) |
| [`03_quick_profile_proxy.py`](03_quick_profile_proxy.py) | One-off ephemeral profile + proxy | [03-quick-profile-proxy.md](../../../docs/multilogin-api/cookbook/03-quick-profile-proxy.md) |
| [`04_batch_rotation.py`](04_batch_rotation.py) | Rotate many saved profiles | [04-multi-account-rotation.md](../../../docs/multilogin-api/cookbook/04-multi-account-rotation.md) |
| [`05_headless_smoke.py`](05_headless_smoke.py) | Headless smoke test before fleet runs | [05-headless-smoke-test.md](../../../docs/multilogin-api/cookbook/05-headless-smoke-test.md) |
| [`07_login_flow.py`](07_login_flow.py) | Configurable login (selectors JSON + env) | [07-login-flow-template.md](../../../docs/multilogin-api/cookbook/07-login-flow-template.md) |
| [`08_selenium_attach.py`](08_selenium_attach.py) | Selenium WebDriver attach | [08-selenium-attach.md](../../../docs/multilogin-api/cookbook/08-selenium-attach.md) |

## Setup

```bash
cd sdk/python
pip install -r requirements.txt
cp ../config.example.env ../.env
# fill MLX_FOLDER_ID, MLX_PROFILE_ID (and proxy vars for recipe 03)
```

Optional for recipe 02:

```bash
pip install playwright
playwright install chromium
```

## Run

```bash
python recipes/01_saved_profile_lifecycle.py
python recipes/02_playwright_attach.py
```
