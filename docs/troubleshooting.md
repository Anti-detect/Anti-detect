# Troubleshooting — Multilogin X automation

Symptoms and fixes for **Launcher API**, **cloud API**, and **Playwright/Selenium** flows in this repo.

> **Plans & devices:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`**

---

## Pre-flight

```bash
cd sdk/python
python mlx_cli.py doctor
```

---

## Launcher / local agent

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `Connection refused` on start | MLX agent not running | Open Multilogin X app; check `MLX_LAUNCHER_HOST` / `PORT` |
| `401` / `403` | Wrong or expired local auth | Re-login MLX app; see [authentication.md](multilogin-api/authentication.md) |
| `Profile already running` | Previous session not stopped | `python mlx_cli.py stop` or MLX UI stop |
| Wrong profile starts | UUID typo | [token-and-ids.md](token-and-ids.md) — folder ≠ profile |
| Quick profile won't stop | Ephemeral session | No stop endpoint — close via UI or wait for expiry ([Recipe 03](multilogin-api/cookbook/03-quick-profile-proxy.md)) |

---

## CDP / Playwright / Selenium

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `connect_over_cdp` timeout | Profile still booting | Sleep 2–5s; use [Recipe 06](multilogin-api/cookbook/06-error-handling-retry.md) retry |
| Blank page after attach | Wrong context | Use `browser.contexts[0].pages[0]` ([Recipe 02](multilogin-api/cookbook/02-playwright-attach.md)) |
| Selenium can't connect | Wrong `automation_type` | Start with `selenium`, not `puppeteer` ([Recipe 08](multilogin-api/cookbook/08-selenium-attach.md)) |
| Immediate bot block | Proxy/geo mismatch | [fingerprint-checklist.md](fingerprint-checklist.md) |

---

## Cloud API

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `401` on `profile/search` | Bearer expired (~30 min) | `python mlx_cli.py refresh` — update `MLX_BEARER_TOKEN` |
| Empty `profiles export` | Wrong workspace token or filters | Check `MLX_SEARCH_TEXT`, folder filter |
| Parsed 0 profiles | JSON shape changed | Extend [profile_catalog.py](../sdk/python/profile_catalog.py) or inspect raw `--json` |

---

## Rotation / workers

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Second worker crashes launcher | Two profiles same machine | One profile per launcher — [Recipe 12](multilogin-api/cookbook/12-cloud-export-and-workers.md) |
| Shard empty | `MLX_WORKER_ID` too high | `worker_id` must be `< MLX_WORKER_COUNT` |
| Rotation too slow | Placeholder sleep | Set `MLX_USE_PLAYWRIGHT=1` or custom `run_job()` |

---

## Cloud Real Phone

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Desktop recipe fails on mobile profile | Wrong product lane | Real Phone ≠ desktop launcher — [multilogin-cloud-real-phone.md](multilogin-cloud-real-phone.md) |
| Need more devices | Plan limit | [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`MIN50`** |

---

## Logs & security

- Never commit `sdk/.env` or bearer tokens.
- Redact `profile_id` in public issues.
- [SECURITY.md](../SECURITY.md) for vulnerabilities.

---

## Related

- [faq.md](faq.md)
- [cookbook/06](multilogin-api/cookbook/06-error-handling-retry.md)
- [getting-started.md](getting-started.md)

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** · **`MIN50`**
