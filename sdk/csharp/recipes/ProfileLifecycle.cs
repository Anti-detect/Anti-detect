// Recipe — Saved profile lifecycle (start → use → stop)
// dotnet script sdk/csharp/recipes/ProfileLifecycle.cs
using System;
using System.Net.Http;
using System.Threading.Tasks;

var host = Environment.GetEnvironmentVariable("MLX_LAUNCHER_HOST") ?? "launcher.mlx.yt";
var port = Environment.GetEnvironmentVariable("MLX_LAUNCHER_PORT") ?? "45001";
var folderId = Environment.GetEnvironmentVariable("MLX_FOLDER_ID")
    ?? throw new InvalidOperationException("Set MLX_FOLDER_ID");
var profileId = Environment.GetEnvironmentVariable("MLX_PROFILE_ID")
    ?? throw new InvalidOperationException("Set MLX_PROFILE_ID");
var automation = Environment.GetEnvironmentVariable("MLX_AUTOMATION_TYPE") ?? "puppeteer";
var headless = Environment.GetEnvironmentVariable("MLX_HEADLESS") ?? "false";

var startUrl =
    $"https://{host}:{port}/api/v2/profile/f/{folderId}/p/{profileId}/start" +
    $"?automation_type={automation}&headless_mode={headless}";
var stopUrl = $"https://{host}:{port}/api/v1/profile/stop/p/{profileId}";

using var client = new HttpClient();
try
{
    var start = new HttpRequestMessage(HttpMethod.Get, startUrl);
    start.Headers.Add("Accept", "application/json");
    var startResp = await client.SendAsync(start);
    startResp.EnsureSuccessStatusCode();
    var body = await startResp.Content.ReadAsStringAsync();
    Console.WriteLine($"Started profile {profileId}");
    Console.WriteLine(body);
    Console.WriteLine("→ attach Playwright/Selenium to CDP port from JSON, then stop");
}
finally
{
    var stop = new HttpRequestMessage(HttpMethod.Get, stopUrl);
    stop.Headers.Add("Accept", "application/json");
    var stopResp = await client.SendAsync(stop);
    stopResp.EnsureSuccessStatusCode();
    Console.WriteLine($"Stopped profile {profileId}");
}
