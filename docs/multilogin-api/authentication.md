# Multilogin X API — authentication

From Postman collection intro (archived in `docs/multilogin-api/spec/`).

## Bearer token

Most requests use **Authorization: Bearer &lt;token&gt;** on:

- **Cloud API:** `https://api.multilogin.com`
- **Local Launcher:** `https://{launcher_host}:{port}` (example export: `launcher.mlx.yt:45001`)

Generate a token by signing in through the Profile Access Management endpoints in the live Postman collection.

## Token lifetime

The regular token lifetime is about **30 minutes**. Refresh with:

```http
POST /user/refresh_token
```

(Cloud API — see live Postman doc for full URL and body.)

## Environment variables

Use [`sdk/config.example.env`](../../sdk/config.example.env):

```bash
MLX_BEARER_TOKEN=your_token_here
MLX_CLOUD_BASE=https://api.multilogin.com
```

Never commit tokens. Prefer OS keychain or CI secrets.

## Related

- [token-and-ids.md](../token-and-ids.md)
- [launcher-endpoints.md](launcher-endpoints.md)

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)

