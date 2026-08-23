# Recipe 03 — Quick profile v3 + proxy

## When to use

- **One-off** browser session (no saved cookies needed).
- Testing a **new residential proxy** before assigning to a saved profile.
- Scraping / signup flows where isolation is more important than persistence.

## v2 vs v3

| Version | Path | Proxy location |
|---------|------|----------------|
| v2 | `POST /api/v2/profile/quick` | Often under `parameters` |
| v3 | `POST /api/v3/profile/quick` | **`proxy` at root body** |

This repo’s helper [`build_quick_v3_payload`](../../../sdk/python/mlx_helpers.py) follows v3 layout.

## Runnable code

**Python:** [`sdk/python/recipes/03_quick_profile_proxy.py`](../../../sdk/python/recipes/03_quick_profile_proxy.py)

Required env in `sdk/.env`:

```env
MLX_PROXY_HOST=gate.provider.example
MLX_PROXY_PORT=10000
MLX_PROXY_USER=optional
MLX_PROXY_PASS=optional
MLX_PROXY_TYPE=http
```

## Notes

- Quick profiles are **ephemeral** — there is no `profile_id` for `/stop` like saved profiles.
- Close via MLX UI or let the session expire per your agent settings.
- Set `proxy_masking: custom` when passing explicit proxy (handled by helper).

## Next

Need persistence? Create a saved profile in MLX cloud UI and switch to [Recipe 01](01-saved-profile-lifecycle.md).

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
