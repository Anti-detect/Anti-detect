// Recipe — Saved profile lifecycle (start → use → stop)
// Compile with OkHttp on classpath; set MLX_FOLDER_ID / MLX_PROFILE_ID env vars.
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class ProfileLifecycle {
    public static void main(String[] args) throws Exception {
        String host = env("MLX_LAUNCHER_HOST", "launcher.mlx.yt");
        String port = env("MLX_LAUNCHER_PORT", "45001");
        String folderId = require("MLX_FOLDER_ID");
        String profileId = require("MLX_PROFILE_ID");
        String automation = env("MLX_AUTOMATION_TYPE", "puppeteer");
        String headless = env("MLX_HEADLESS", "false");

        String startUrl = String.format(
            "https://%s:%s/api/v2/profile/f/%s/p/%s/start?automation_type=%s&headless_mode=%s",
            host, port, folderId, profileId, automation, headless
        );
        String stopUrl = String.format("https://%s:%s/api/v1/profile/stop/p/%s", host, port, profileId);

        OkHttpClient client = new OkHttpClient();
        try {
            Request start = new Request.Builder().url(startUrl).get()
                .addHeader("Accept", "application/json").build();
            try (Response resp = client.newCall(start).execute()) {
                if (!resp.isSuccessful()) throw new RuntimeException("Start HTTP " + resp.code());
                System.out.println("Started: " + resp.body().string());
            }
        } finally {
            Request stop = new Request.Builder().url(stopUrl).get()
                .addHeader("Accept", "application/json").build();
            try (Response resp = client.newCall(stop).execute()) {
                if (!resp.isSuccessful()) throw new RuntimeException("Stop HTTP " + resp.code());
                System.out.println("Stopped profile " + profileId);
            }
        }
    }

    private static String env(String key, String fallback) {
        String v = System.getenv(key);
        return v != null && !v.isBlank() ? v : fallback;
    }

    private static String require(String key) {
        String v = System.getenv(key);
        if (v == null || v.isBlank()) throw new IllegalStateException("Set " + key);
        return v;
    }
}
