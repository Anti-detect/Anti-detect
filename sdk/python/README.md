# Python — Multilogin X API

Two styles matching Postman exports:

| Style | Folder | Dependency |
|-------|--------|------------|
| **mlx_client** | [`mlx_client.py`](mlx_client.py) | `requests` — reusable class + `profile_session()` |
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
| [`recipes/07_login_flow.py`](recipes/07_login_flow.py) | Login flow template |
| [`recipes/08_selenium_attach.py`](recipes/08_selenium_attach.py) | Selenium attach |

Guides: [docs/multilogin-api/cookbook/](../../docs/multilogin-api/cookbook/)

Tests (no MLX agent needed): `python -m unittest sdk/python/tests/test_mlx_helpers.py`

More flows: [docs/multilogin-api/cookbook/](../../docs/multilogin-api/cookbook/).
