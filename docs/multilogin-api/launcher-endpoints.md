# Launcher API endpoints

Extracted from Postman archive (`docs/multilogin-api/spec/`) — **Launcher** folder. Your agent host/port may differ; check Multilogin X settings.

## Base URL pattern

```
https://{MLX_LAUNCHER_HOST}:{MLX_PORT}
```

Example from export: `https://launcher.mlx.yt:45001`

## Endpoints in export

### Start saved profile

```http
GET /api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type={type}&headless_mode={bool}
```

| Query | Example |
|-------|---------|
| `automation_type` | `puppeteer`, `selenium`, … |
| `headless_mode` | `true` / `false` |

**Response** includes `data.port` (CDP/debug port) for Playwright/Selenium attach.

SDK: [`sdk/python/requests/start_profile.py`](../../sdk/python/requests/start_profile.py)

---

### Stop profile

```http
GET /api/v1/profile/stop/p/{profile_id}
```

SDK: [`sdk/python/requests/stop_profile.py`](../../sdk/python/requests/stop_profile.py)

---

### Quick profile v2

```http
POST /api/v2/profile/quick
Content-Type: application/json
```

Body: `browser_type`, `os_type`, `parameters.flags`, optional `parameters.fingerprint`, etc.

---

### Quick profile v3

```http
POST /api/v3/profile/quick
Content-Type: application/json
```

v3 places **`proxy`** inside the root body (not only under `parameters`). Fingerprint `Custom` flags require manual values.

SDK: [`sdk/python/requests/quick_profile_v3.py`](../../sdk/python/requests/quick_profile_v3.py)

## Fingerprint flags (quick profile)

Common `parameters.flags` values: `mask`, `custom`, `natural`, `disabled`.  
When set to **`custom`**, supply matching fields under `parameters.fingerprint`.

## Re-export full API

Saved HTML currently includes **Launcher** operations only. To document Profile Management / Auth:

1. Open [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
2. Save each language tab (Python, C#, Java) via browser **Save Page**
3. Run `python scripts/parse-api-html.py`

## Related

- [authentication.md](authentication.md)
- [sdk-matrix.md](sdk-matrix.md)

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**

