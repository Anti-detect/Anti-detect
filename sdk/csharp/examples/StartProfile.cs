// Multilogin X — Start browser profile (HttpClient)
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

var url =
    $"https://{host}:{port}/api/v2/profile/f/{folderId}/p/{profileId}/start" +
    $"?automation_type={automation}&headless_mode={headless}";

using var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, url);
request.Headers.Add("Accept", "application/json");

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
