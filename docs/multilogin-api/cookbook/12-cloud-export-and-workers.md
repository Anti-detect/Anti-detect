# Recipe 12 — Cloud export + parallel workers

## When to use

- **Export:** Build `profiles.json` from cloud search instead of hand-editing UUIDs.
- **Workers:** Split rotation across **multiple machines** (each with its own MLX launcher).

> One launcher should run **one profile at a time**. Parallelism = multiple agents, not multiple starts on the same desktop.

## Part A — Export from cloud

| Step | Tool |
|------|------|
| Set token | `MLX_BEARER_TOKEN` in `sdk/.env` |
| Search | `POST https://api.multilogin.com/profile/search` |
| Export | `python recipes/12_cloud_export_profiles.py` |

Or CLI:

```bash
cd sdk/python
python mlx_cli.py profiles export -o profiles.json
python mlx_cli.py profiles list
```

| Env | Purpose |
|-----|---------|
| `MLX_SEARCH_LIMIT` | Page size (default 100) |
| `MLX_SEARCH_OFFSET` | Pagination offset |
| `MLX_SEARCH_TEXT` | Name filter |
| `MLX_SEARCH_FOLDER=1` | Restrict to `MLX_FOLDER_ID` |

## Part B — Worker sharding

After export (or hand-built `profiles.json`):

```bash
# Machine 1
set MLX_WORKER_ID=0
set MLX_WORKER_COUNT=2
python recipes/12_parallel_workers.py

# Machine 2
set MLX_WORKER_ID=1
set MLX_WORKER_COUNT=2
python recipes/12_parallel_workers.py
```

Optional: `MLX_USE_PLAYWRIGHT=1` for real attach per profile ([Recipe 04](04-multi-account-rotation.md)).

## Runnable code

| Script | Role |
|--------|------|
| [`12_cloud_export_profiles.py`](../../../sdk/python/recipes/12_cloud_export_profiles.py) | Cloud → `profiles.json` |
| [`12_parallel_workers.py`](../../../sdk/python/recipes/12_parallel_workers.py) | Sharded rotation |

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Two workers on one PC starting profiles together | Use `MLX_WORKER_COUNT=1` locally; scale on separate hosts |
| Empty export | Refresh token — `python mlx_cli.py refresh` |
| Missing `folder_id` in search | Filter by folder or update `profile_catalog.py` for your JSON shape |

## Related

- [token-and-ids.md](../../token-and-ids.md)
- [cloud-api.md](../cloud-api.md)
- [Recipe 04 — Rotation](04-multi-account-rotation.md)

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)
