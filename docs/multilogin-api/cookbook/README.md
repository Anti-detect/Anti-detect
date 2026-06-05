# MLX API cookbook — real-world recipes

Practical guides for **Multilogin X Local Launcher API**. Each recipe explains *when* to use it, *what can go wrong*, and links to runnable code.

> Not affiliated with Multilogin Inc. Test on staging before production fleets.

## Recipe index

| # | Scenario | Best for | Code |
|---|----------|----------|------|
| 01 | [Saved profile lifecycle](01-saved-profile-lifecycle.md) | Persistent logins, daily bots | Python [`01_saved_profile_lifecycle.py`](../../../sdk/python/recipes/01_saved_profile_lifecycle.py) |
| 02 | [Playwright attach over CDP](02-playwright-attach.md) | Stealth UI automation | Python [`02_playwright_attach.py`](../../../sdk/python/recipes/02_playwright_attach.py) |
| 03 | [Quick profile + proxy](03-quick-profile-proxy.md) | One-off runs, proxy QA | Python [`03_quick_profile_proxy.py`](../../../sdk/python/recipes/03_quick_profile_proxy.py) |
| 04 | [Multi-account rotation](04-multi-account-rotation.md) | MMO / multi-shop isolation | Python [`04_batch_rotation.py`](../../../sdk/python/recipes/04_batch_rotation.py) |
| 05 | [Headless smoke test](05-headless-smoke-test.md) | CI / pre-flight checks | Python [`05_headless_smoke.py`](../../../sdk/python/recipes/05_headless_smoke.py) |
| 06 | [Error handling & retry](06-error-handling-retry.md) | Launcher warming, busy profiles | [`mlx_helpers.retry`](../../../sdk/python/mlx_helpers.py) |

## Decision tree

```text
Need cookies from yesterday?
  ├─ YES → Recipe 01/02 (saved profile start/stop)
  └─ NO  → Recipe 03 (quick profile v3)

Many accounts, same script?
  └─ Recipe 04 (rotation JSON + sequential sessions)

Shipping to production?
  └─ Recipe 05 smoke → then scale
```

## Prerequisites

1. Multilogin X running locally (launcher reachable).
2. `MLX_FOLDER_ID` + `MLX_PROFILE_ID` from [id-token tools](https://github.com/multilogin-automation/multilogin-x-id-token-retrieval-tools).
3. Copy [`sdk/config.example.env`](../../../sdk/config.example.env) → `sdk/.env`.

## Related

- [launcher-endpoints.md](../launcher-endpoints.md) — raw paths
- [playwright-mlx-integration.md](../../playwright-mlx-integration.md) — architecture
- [mmo-automation-guide.md](../../mmo-automation-guide.md) — operational rules
