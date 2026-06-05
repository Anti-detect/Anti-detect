# Recipe 11 — Import cookies JSON

## When to use

- Restore cookies exported from [Recipe 09](09-cookie-warm-export.md).
- Migrate session state between profiles or machines.
- Seed a cold profile before login automation ([Recipe 07](07-login-flow-template.md)).

## Flow

```text
start saved profile
  → attach Playwright over CDP
  → context.add_cookies(JSON)
  → navigate to target URL
  → verify title / logged-in state
stop profile
```

## Input format

Playwright export (`cookies_export.json` from Recipe 09) or `{ "cookies": [ ... ] }`.

## Runnable code

**Python:** [`sdk/python/recipes/11_import_cookies.py`](../../../sdk/python/recipes/11_import_cookies.py)

| Env | Purpose |
|-----|---------|
| `MLX_COOKIES_IN` | Path to cookies JSON (default `cookies_export.json`) |
| `MLX_SMOKE_URL` | Landing URL after import |

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Cookies not applied | Domain/path must match target URL |
| Import before navigation | `add_cookies` then `goto` — order matters |
| Wrong profile | One identity per profile — [Recipe 04](04-multi-account-rotation.md) |

## Next

→ [Recipe 07 — Login flow](07-login-flow-template.md) if cookies alone are not enough.

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)
