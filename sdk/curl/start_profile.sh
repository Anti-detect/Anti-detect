#!/usr/bin/env bash
# Multilogin X — Start profile (cURL)
set -euo pipefail

HOST="${MLX_LAUNCHER_HOST:-launcher.mlx.yt}"
PORT="${MLX_LAUNCHER_PORT:-45001}"
FOLDER_ID="${MLX_FOLDER_ID:?Set MLX_FOLDER_ID}"
PROFILE_ID="${MLX_PROFILE_ID:?Set MLX_PROFILE_ID}"
AUTOMATION="${MLX_AUTOMATION_TYPE:-puppeteer}"
HEADLESS="${MLX_HEADLESS:-false}"

URL="https://${HOST}:${PORT}/api/v2/profile/f/${FOLDER_ID}/p/${PROFILE_ID}/start?automation_type=${AUTOMATION}&headless_mode=${HEADLESS}"

curl -sS -X GET "$URL" -H "Accept: application/json" | jq .
