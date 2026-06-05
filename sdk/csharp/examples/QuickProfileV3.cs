using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

var host = Environment.GetEnvironmentVariable("MLX_LAUNCHER_HOST") ?? "launcher.mlx.yt";
var port = Environment.GetEnvironmentVariable("MLX_LAUNCHER_PORT") ?? "45001";
var url = $"https://{host}:{port}/api/v3/profile/quick";

var json = """
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

using var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, url);
request.Headers.Add("Accept", "application/json");
request.Content = new StringContent(json, Encoding.UTF8, "application/json");

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
