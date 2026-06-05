# Recipe 02 — Playwright attach over CDP

## When to use

- Production **stealth automation** (anti-detect fingerprint already in MLX profile).
- You must **not** call `chromium.launch()` for the main session — attach to MLX browser instead.

## Flow

1. Start saved profile with `automation_type=puppeteer`.
2. Read `data.port` from JSON response → build `http://127.0.0.1:{port}`.
3. `playwright.chromium.connect_over_cdp(cdp_url)`.
4. Automate on existing context/page.
5. Stop profile via API.

## Runnable code

**Python:** [`sdk/python/recipes/02_playwright_attach.py`](../../../sdk/python/recipes/02_playwright_attach.py)

```bash
cd sdk/python
pip install -r requirements.txt playwright
playwright install chromium
cp ../config.example.env ../.env
python recipes/02_playwright_attach.py
```

Customize the `automate(page)` function for login flows, scraping, or form submission.

## Environment

| Variable | Purpose |
|----------|---------|
| `MLX_FOLDER_ID` | Folder UUID |
| `MLX_PROFILE_ID` | Profile UUID |
| `MLX_SMOKE_URL` | Optional first navigation URL |

## Troubleshooting

| Symptom | Likely cause |
|---------|----------------|
| `connect_over_cdp` timeout | Profile still starting — add short sleep or retry |
| Blank page | Wrong context — use `browser.contexts[0].pages[0]` |
| Immediate block | Proxy/geo mismatch — [fingerprint-checklist.md](../../fingerprint-checklist.md) |

## Next steps

Combine with [Recipe 07 — Login flow](07-login-flow-template.md) or [Recipe 04 — Rotation](04-multi-account-rotation.md).

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)
