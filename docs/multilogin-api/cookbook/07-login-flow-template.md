# Recipe 07 — Login flow template

## When to use

- Validate that a **saved MLX profile** can still log in.
- Warm up accounts after cookie import.
- Same login script across many profiles (pair with [Recipe 04](04-multi-account-rotation.md)).

## Setup

1. Copy [`login.example.json`](../../../sdk/python/recipes/login.example.json) → `login.json` and edit selectors for your app.
2. Add to `sdk/.env`:

```env
MLX_LOGIN_USER=your@email.example
MLX_LOGIN_PASS=your-password
MLX_LOGIN_CONFIG=sdk/python/recipes/login.json
```

Never commit real credentials.

## Flow

```text
start profile (puppeteer)
  → Playwright connect_over_cdp
  → goto login_url
  → fill username / password (human_pause between steps)
  → click submit
  → verify URL contains success fragment
stop profile
```

## Runnable code

[`sdk/python/recipes/07_login_flow.py`](../../../sdk/python/recipes/07_login_flow.py)

Shared patterns: [`automation_patterns.py`](../../../sdk/python/automation_patterns.py)

## Selector tips

| Field | Example |
|-------|---------|
| Username | `#email`, `input[name='username']` |
| Password | `#password` |
| Submit | `button[type='submit']`, `[data-testid='login']` |
| Success | `url_contains: "/dashboard"` or `/home` |

## Security

- Use `.env` locally; use CI secrets for automated runs.
- Redact passwords in logs and screenshots.

## Next

Selenium instead of Playwright → [Recipe 08](08-selenium-attach.md)
