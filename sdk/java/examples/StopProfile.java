// Multilogin X — Stop browser profile (OkHttp)
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class StopProfile {
    public static void main(String[] args) throws Exception {
        String host = env("MLX_LAUNCHER_HOST", "launcher.mlx.yt");
        String port = env("MLX_LAUNCHER_PORT", "45001");
        String profileId = require("MLX_PROFILE_ID");

        String url = String.format("https://%s:%s/api/v1/profile/stop/p/%s", host, port, profileId);

        Request request = new Request.Builder()
            .url(url)
            .get()
            .addHeader("Accept", "application/json")
            .build();

        try (Response response = new OkHttpClient().newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new RuntimeException("HTTP " + response.code());
            }
            System.out.println(response.body().string());
        }
    }

    private static String env(String key, String fallback) {
        String v = System.getenv(key);
        return v != null && !v.isBlank() ? v : fallback;
    }

    private static String require(String key) {
        String v = System.getenv(key);
        if (v == null || v.isBlank()) {
            throw new IllegalStateException("Set " + key);
        }
        return v;
    }
}
