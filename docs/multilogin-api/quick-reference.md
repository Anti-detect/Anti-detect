# Multilogin X API — quick reference

One-page cheat sheet (Launcher API from `docs/multilogin-api/spec/` archive).

## Bases

| API | Base |
|-----|------|
| **Local Launcher** | `https://{host}:{port}` — e.g. `launcher.mlx.yt:45001` |
| **Cloud** | `https://api.multilogin.com` |

## Auth

```http
Authorization: Bearer <token>
```

Refresh (~30 min lifetime): `POST /user/refresh_token` (cloud — see live Postman).

## Launcher — start saved profile

```http
GET /api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type=puppeteer&headless_mode=false
```

Response `data.port` → attach Playwright/Selenium.

## Launcher — stop

```http
GET /api/v1/profile/stop/p/{profile_id}
```

## Launcher — quick profile

```http
POST /api/v2/profile/quick
POST /api/v3/profile/quick
Content-Type: application/json
```

v3: `proxy` at root + `parameters.flags` / `parameters.fingerprint`.

## SDK one-liners

```bash
# Python client
cd sdk/python && python mlx_client.py

# cURL
bash sdk/curl/start_profile.sh

# Node 18+
node sdk/nodejs/start_profile.mjs
```

## Categories (full Postman collection)

1. **Launcher** — start/stop/quick  
2. **Profile Management** — CRUD profiles  
3. **Profile Access Management** — sign-in, workspaces  
4. **Browser Profile Data** — unlock profile data  

Re-save full Postman HTML temporarily, run `scripts/archive-postman-html.py` — see [spec/README.md](spec/README.md).

## Links

- [launcher-endpoints.md](launcher-endpoints.md)
- [sdk-matrix.md](sdk-matrix.md)
- [sdk/README.md](../../sdk/README.md)

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**

