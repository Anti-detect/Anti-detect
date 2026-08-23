# Recipe 10 — Scrape page snapshot

## When to use

- Monitor a listing or dashboard while logged in via MLX profile
- QA that a page renders correctly under real fingerprint
- Lightweight data pull without full crawler framework

## Setup

```env
MLX_SCRAPE_URL=https://your-target.example/page
MLX_SCRAPE_SELECTOR=main
MLX_SCRAPE_OUT=scrape_snapshot.json
```

## Runnable code

[`sdk/python/recipes/10_scrape_snapshot.py`](../../../sdk/python/recipes/10_scrape_snapshot.py)

## Output shape

```json
{
  "url": "https://...",
  "title": "Page title",
  "text": "First 4000 chars of selector inner text..."
}
```

Extend `scrape_page_snapshot()` in [`automation_patterns.py`](../../../sdk/python/automation_patterns.py) for tables, prices, etc.

## Compliance

Respect robots.txt and platform ToS. Rate-limit requests.

## Related

- [Recipe 02 — Playwright attach](02-playwright-attach.md)

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
