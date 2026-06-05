// Multilogin X — Quick profile v3 (OkHttp)
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class QuickProfileV3 {
    private static final MediaType JSON = MediaType.parse("application/json");

    public static void main(String[] args) throws Exception {
        String host = env("MLX_LAUNCHER_HOST", "launcher.mlx.yt");
        String port = env("MLX_LAUNCHER_PORT", "45001");
        String url = String.format("https://%s:%s/api/v3/profile/quick", host, port);

        String json = """
            {
              "browser_type": "mimic",
              "core_version": 124,
              "os_type": "linux",
              "automation": "selenium",
              "is_headless": false,
              "parameters": {
                "flags": { "navigator_masking": "custom", "proxy_masking": "custom" },
                "proxy": { "host": "host.example", "type": "http", "port": 8080 }
              }
            }
            """;

        Request request = new Request.Builder()
            .url(url)
            .post(RequestBody.create(json, JSON))
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
}
