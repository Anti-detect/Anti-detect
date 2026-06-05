/**
 * Multilogin X — Start profile (Node.js fetch)
 * Node 18+ (native fetch)
 */
const host = process.env.MLX_LAUNCHER_HOST ?? "launcher.mlx.yt";
const port = process.env.MLX_LAUNCHER_PORT ?? "45001";
const folderId = process.env.MLX_FOLDER_ID;
const profileId = process.env.MLX_PROFILE_ID;
const automation = process.env.MLX_AUTOMATION_TYPE ?? "puppeteer";
const headless = process.env.MLX_HEADLESS ?? "false";

if (!folderId || !profileId) {
  throw new Error("Set MLX_FOLDER_ID and MLX_PROFILE_ID");
}

const url =
  `https://${host}:${port}/api/v2/profile/f/${folderId}/p/${profileId}/start` +
  `?automation_type=${automation}&headless_mode=${headless}`;

const res = await fetch(url, { headers: { Accept: "application/json" } });
if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
console.log(await res.json());
