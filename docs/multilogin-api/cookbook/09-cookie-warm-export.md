# Recipe 09 — Cookie warm & export

## When to use

- **Cold profiles** before high-risk logins
- **MMO / multi-account** prep — realistic browsing history
- **Backup** cookies after manual session (JSON export)

## Setup

```env
MLX_WARM_URLS=https://example.com,https://www.wikipedia.org
# or
MLX_WARM_URLS_JSON=sdk/python/recipes/warm-urls.example.json
MLX_COOKIES_OUT=cookies_export.json
```

## Runnable code

[`sdk/python/recipes/09_cookie_warm_export.py`](../../../sdk/python/recipes/09_cookie_warm_export.py)

## Flow

```text
start profile → Playwright CDP attach
  → visit each warm URL (human_pause between)
  → context.cookies() → JSON file
stop profile
```

Cookies stay in the MLX profile storage — export is for audit/backup only.

## Related

- [mmo-automation-guide.md](../../mmo-automation-guide.md)
- [Recipe 07 — Login](07-login-flow-template.md)
- [Recipe 11 — Import cookies](11-import-cookies.md)

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
