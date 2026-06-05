"""Stop profile using stdlib http.client."""
import os
import json
import http.client

HOST = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
PORT = int(os.getenv("MLX_LAUNCHER_PORT", "45001"))
PROFILE_ID = os.environ["MLX_PROFILE_ID"]
path = f"/api/v1/profile/stop/p/{PROFILE_ID}"

conn = http.client.HTTPSConnection(HOST, PORT, timeout=60)
conn.request("GET", path, headers={"Accept": "application/json"})
res = conn.getresponse()
body = res.read().decode()
if res.status >= 400:
    raise RuntimeError(f"{res.status} {body}")
print(json.loads(body))
