/**
 * Recipe — Saved profile lifecycle (start → inspect → stop)
 * Usage: node sdk/nodejs/recipes/lifecycle.mjs
 */
const host = process.env.MLX_LAUNCHER_HOST ?? "launcher.mlx.yt";
const port = process.env.MLX_LAUNCHER_PORT ?? "45001";
const folderId = process.env.MLX_FOLDER_ID;
const profileId = process.env.MLX_PROFILE_ID;
const automation = process.env.MLX_AUTOMATION_TYPE ?? "puppeteer";
const headless = process.env.MLX_HEADLESS ?? "false";

if (!folderId || !profileId) {
  console.error("Set MLX_FOLDER_ID and MLX_PROFILE_ID");
  process.exit(1);
}

const startUrl =
  `https://${host}:${port}/api/v2/profile/f/${folderId}/p/${profileId}/start` +
  `?automation_type=${automation}&headless_mode=${headless}`;
const stopUrl = `https://${host}:${port}/api/v1/profile/stop/p/${profileId}`;

try {
  const start = await fetch(startUrl, { headers: { Accept: "application/json" } });
  if (!start.ok) throw new Error(`Start failed: ${start.status}`);
  const json = await start.json();
  console.log("Started:", JSON.stringify(json, null, 2));
  console.log("→ attach automation to data.port, then script stops profile");
} finally {
  const stop = await fetch(stopUrl, { headers: { Accept: "application/json" } });
  if (!stop.ok) throw new Error(`Stop failed: ${stop.status}`);
  console.log(`Stopped profile ${profileId}`);
}
