# Recipe 08 — Selenium attach

## When to use

- Your team already uses **Selenium WebDriver**.
- Legacy test suites that expect `driver.get()` / `find_element`.
- MLX profile started with `automation_type=selenium`.

## Difference from Playwright (Recipe 02)

| | Playwright | Selenium |
|---|------------|----------|
| Start param | `automation_type=puppeteer` | `automation_type=selenium` |
| Attach | `connect_over_cdp(http://127.0.0.1:port)` | `debuggerAddress=127.0.0.1:port` |
| Package | `playwright` | `selenium` |

## Runnable code

[`sdk/python/recipes/08_selenium_attach.py`](../../../sdk/python/recipes/08_selenium_attach.py)

```bash
cd sdk/python
pip install selenium
cp ../config.example.env ../.env
python recipes/08_selenium_attach.py
```

## How attach works

```python
from automation_patterns import connect_selenium_chrome

driver = connect_selenium_chrome(session)  # uses data.port from start response
driver.get("https://example.com")
driver.quit()  # detach only — MLX stop is in profile_session finally
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| SessionNotCreated | ChromeDriver version mismatch — upgrade Selenium 4.6+ |
| Cannot connect | Wrong automation_type — must be `selenium` at start |
| Empty window | Wait 2–3s after start before attach |

## Related

- [Recipe 02 — Playwright](02-playwright-attach.md)
- [Recipe 07 — Login flow](07-login-flow-template.md)

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
