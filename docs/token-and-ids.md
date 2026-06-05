# Tokens, folder ID & profile ID

How to obtain the values for `sdk/.env` without external tooling.

> No MLX license yet? [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)

## Profile UUIDs (Launcher API)

Required for start/stop on **saved profiles**:

| Variable | What it is |
|----------|------------|
| `MLX_FOLDER_ID` | Folder UUID containing the profile |
| `MLX_PROFILE_ID` | Browser profile UUID |

### From Multilogin X desktop app

1. Open **Multilogin X** and select your profile.
2. Open profile **settings** or **details** — copy the profile ID (UUID format).
3. Note the **folder** / group the profile belongs to; folder ID is also a UUID.
4. Paste into `sdk/.env`:

```env
MLX_FOLDER_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MLX_PROFILE_ID=yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy
```

### Launcher host & port

Default in exports: `launcher.mlx.yt:45001`. Check **Multilogin X → Settings → Local API** for your agent address.

```env
MLX_LAUNCHER_HOST=launcher.mlx.yt
MLX_LAUNCHER_PORT=45001
```

## Cloud API bearer token (optional)

For **cloud** endpoints (`https://api.multilogin.com` — profile CRUD, sign-in):

1. Sign in via official MLX cloud API (see [authentication.md](multilogin-api/authentication.md)).
2. Store token in `.env` as `MLX_BEARER_TOKEN` — **never commit**.
3. Tokens expire (~30 min); refresh per Postman docs.

Launcher start/stop/quick calls on the local agent often work **without** cloud token when the desktop app is running.

## Verify setup

```bash
cd sdk/python
pip install -r requirements.txt
python recipes/05_headless_smoke.py
```

## Related

- [`sdk/config.example.env`](../sdk/config.example.env)
- [getting-started.md](getting-started.md)
- [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
