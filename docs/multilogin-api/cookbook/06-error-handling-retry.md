# Recipe 06 — Error handling & retry

## When launcher calls fail

| Error pattern | Typical cause | Action |
|---------------|---------------|--------|
| Connection refused | MLX agent not running | Start Multilogin X app |
| Timeout on start | Profile heavy / disk slow | Increase timeout, retry |
| 4xx on start | Wrong UUID or profile busy | Stop stale session, verify IDs |
| Missing `port` in JSON | Start still in progress | Sleep 2–5s, retry |

## Runnable code

**Python:** [`sdk/python/recipes/06_error_handling_retry.py`](../../../sdk/python/recipes/06_error_handling_retry.py)

## Retry helper

[`sdk/python/mlx_helpers.py`](../../../sdk/python/mlx_helpers.py) exports `retry()`:

```python
from mlx_helpers import retry

result = retry(
    lambda: client.start_profile(folder, profile),
    attempts=3,
    delay_seconds=2.0,
    on_retry=lambda n, e: print(f"attempt {n}: {e}"),
)
```

## Always stop in `finally`

```python
with client.profile_session(folder_id, profile_id) as session:
    ...
# stop called automatically
```

Never leave profiles running overnight unless intentional — leaks RAM and blocks the next start.

## Logging hygiene

- Do **not** log bearer tokens or proxy passwords.
- Redact `profile_id` in public bug reports if needed.

## Related

- [authentication.md](../authentication.md) — cloud token refresh (separate from launcher)
- [maintenance.md](../../maintenance.md) — repo CI checks

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
