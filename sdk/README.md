# Multilogin X SDK & code library

**The largest open Multilogin X code hub on this profile** — curated from official [Postman API docs](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) and the archived spec in [`docs/multilogin-api/spec/`](../docs/multilogin-api/spec/).

> Unofficial community documentation. For authoritative API behavior, use Multilogin support and the live Postman collection.

## What is inside

| Language | Variants | Folder |
|----------|----------|--------|
| **Python** | `requests`, `http.client`, **`mlx_client`** | [`python/`](python/) |
| **C#** | `HttpClient` | [`csharp/`](csharp/) |
| **Java** | `OkHttp` | [`java/`](java/) |
| **Node.js** | native `fetch` (18+) | [`nodejs/`](nodejs/) |
| **cURL** | shell | [`curl/`](curl/) |

## API surfaces

| Surface | Base | Used for |
|---------|------|----------|
| **Local Launcher** | `https://{MLX_LAUNCHER_HOST}:{MLX_LAUNCHER_PORT}` | Start/stop profiles, quick profiles |
| **Cloud API** | `https://api.multilogin.com` | Auth, workspaces, profile CRUD |

Copy [`config.example.env`](config.example.env) → `.env` and fill IDs from [multilogin-x-id-token-retrieval-tools](https://github.com/multilogin-automation/multilogin-x-id-token-retrieval-tools).

## Launcher endpoints (from saved HTML)

| Method | Path | Operation |
|--------|------|-----------|
| GET | `/api/v2/profile/f/{folder_id}/p/{profile_id}/start` | Start browser profile |
| GET | `/api/v1/profile/stop/p/{profile_id}` | Stop browser profile |
| POST | `/api/v2/profile/quick` | Quick profile v2 |
| POST | `/api/v3/profile/quick` | Quick profile v3 (proxy in body) |

Full reference: [`docs/multilogin-api/`](../docs/multilogin-api/)

## Quick start (Python)

```bash
cd sdk/python
pip install -r requirements.txt
cp ../config.example.env ../.env
# edit MLX_FOLDER_ID, MLX_PROFILE_ID
python requests/start_profile.py
# or use the small client library:
python mlx_client.py
```

### All launcher scripts

| Op | Python | C# | Java | Node | cURL |
|----|--------|----|------|------|------|
| Start | `requests/start_profile.py` | `examples/StartProfile.cs` | `examples/StartProfile.java` | `nodejs/start_profile.mjs` | `curl/start_profile.sh` |
| Stop | `requests/stop_profile.py` | `examples/StopProfile.cs` | `examples/StopProfile.java` | `nodejs/stop_profile.mjs` | `curl/stop_profile.sh` |
| Quick v3 | `requests/quick_profile_v3.py` | `examples/QuickProfileV3.cs` | `examples/QuickProfileV3.java` | — | — |
| Quick v2 | `requests/quick_profile_v2.py` | — | — | — | — |

## Related hubs

- [docs/multilogin-api/README.md](../docs/multilogin-api/README.md) — API index
- [docs/libraries.md](../docs/libraries.md) — full “library sky” map
- [@multilogin-automation](https://github.com/multilogin-automation) — production templates & bots

## Regenerate from HTML

```bash
python scripts/parse-api-html.py
python scripts/extract-api-snippets.py
```

## Pricing

Codes **`SAAS50`** / **`MIN50`**: [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
