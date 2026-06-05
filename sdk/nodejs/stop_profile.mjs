const host = process.env.MLX_LAUNCHER_HOST ?? "launcher.mlx.yt";
const port = process.env.MLX_LAUNCHER_PORT ?? "45001";
const profileId = process.env.MLX_PROFILE_ID;

if (!profileId) throw new Error("Set MLX_PROFILE_ID");

const url = `https://${host}:${port}/api/v1/profile/stop/p/${profileId}`;
const res = await fetch(url, { headers: { Accept: "application/json" } });
if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
console.log(await res.json());
