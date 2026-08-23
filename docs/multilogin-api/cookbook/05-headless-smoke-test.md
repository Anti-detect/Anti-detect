# Recipe 05 — Headless smoke test

## When to use

- Before deploying a **fleet** of bots after MLX/agent update.
- Nightly CI on a dedicated smoke profile.
- Verifying launcher host/port after VPN or firewall change.

## What “pass” means

1. `GET .../start?headless_mode=true` returns HTTP 200.
2. Response JSON contains a parseable debug `port`.
3. `GET .../stop` succeeds in `finally` block.

No need to open a visible browser window.

## Runnable code

**Python:** [`sdk/python/recipes/05_headless_smoke.py`](../../../sdk/python/recipes/05_headless_smoke.py)

Uses `retry()` for transient “agent not ready” errors.

## Optional CI hook

```yaml
- name: MLX launcher smoke (manual / self-hosted)
  run: |
    cd sdk/python
    pip install -r requirements.txt
    python recipes/05_headless_smoke.py
  env:
    MLX_LAUNCHER_HOST: ${{ secrets.MLX_LAUNCHER_HOST }}
    MLX_FOLDER_ID: ${{ secrets.MLX_FOLDER_ID }}
    MLX_PROFILE_ID: ${{ secrets.MLX_SMOKE_PROFILE_ID }}
```

> Requires self-hosted runner with Multilogin X installed — not suitable for vanilla GitHub-hosted runners.

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
