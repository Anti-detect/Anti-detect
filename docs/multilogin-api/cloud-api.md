# Cloud API (Profile Access & refresh)

MLX has two surfaces:

| Surface | Base | This repo |
|---------|------|-----------|
| **Local Launcher** | `https://{host}:{port}` | [`mlx_client.py`](../../sdk/python/mlx_client.py) |
| **Cloud API** | `https://api.multilogin.com` | [`mlx_cloud_client.py`](../../sdk/python/mlx_cloud_client.py) |

Launcher handles start/stop/quick on the desktop agent. Cloud API handles sign-in, token refresh, workspace/profile CRUD (see live Postman).

## Bearer token

```http
Authorization: Bearer <token>
```

Lifetime ~**30 minutes**. Refresh:

```http
POST https://api.multilogin.com/user/refresh_token
```

Exact body fields: [Postman — Profile Access Management](https://documenter.getpostman.com/view/28533318/2s946h9Cv9).

## Python example

```bash
cd sdk/python
pip install -r requirements.txt
# set MLX_BEARER_TOKEN in sdk/.env
python mlx_cloud_client.py
```

```python
from mlx_cloud_client import MlxCloudClient

client = MlxCloudClient()
data = client.refresh_token()
# update MLX_BEARER_TOKEN from response per Postman schema
```

## Profile search (export for rotation)

```http
POST https://api.multilogin.com/profile/search
```

```python
from mlx_cloud_client import MlxCloudClient
from profile_catalog import profiles_from_search_response

client = MlxCloudClient()
result = client.search_profiles(limit=100, search_text="")
profiles = profiles_from_search_response(result)
```

CLI: `python mlx_cli.py profiles list` · `python mlx_cli.py profiles export -o profiles.json`  
Recipe: [cookbook/12](cookbook/12-cloud-export-and-workers.md)

## When you need cloud vs launcher

| Task | API |
|------|-----|
| Start browser locally | Launcher — [cookbook/01](cookbook/01-saved-profile-lifecycle.md) |
| Refresh expired token | Cloud — this doc |
| List profiles for rotation JSON | Cloud — `search_profiles()` / Recipe 12 |
| Create/delete cloud profile | Cloud — Postman Profile Management |

## Related

- [authentication.md](authentication.md)
- [token-and-ids.md](../token-and-ids.md)
