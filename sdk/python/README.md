# Python — Multilogin X API

Two styles matching Postman exports:

| Style | Folder | Dependency |
|-------|--------|------------|
| **mlx_client** | [`mlx_client.py`](mlx_client.py) | `requests` — reusable class |
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

Production automation: [`multilogin-automation/templates`](https://github.com/multilogin-automation/multilogin-automation/tree/main/templates).
