#!/usr/bin/env bash
set -euo pipefail

HOST="${MLX_LAUNCHER_HOST:-launcher.mlx.yt}"
PORT="${MLX_LAUNCHER_PORT:-45001}"
PROFILE_ID="${MLX_PROFILE_ID:?Set MLX_PROFILE_ID}"

URL="https://${HOST}:${PORT}/api/v1/profile/stop/p/${PROFILE_ID}"

curl -sS -X GET "$URL" -H "Accept: application/json" | jq .
