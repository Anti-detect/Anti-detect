using System;
using System.Net.Http;
using System.Threading.Tasks;

var host = Environment.GetEnvironmentVariable("MLX_LAUNCHER_HOST") ?? "launcher.mlx.yt";
var port = Environment.GetEnvironmentVariable("MLX_LAUNCHER_PORT") ?? "45001";
var profileId = Environment.GetEnvironmentVariable("MLX_PROFILE_ID")
    ?? throw new InvalidOperationException("Set MLX_PROFILE_ID");

var url = $"https://{host}:{port}/api/v1/profile/stop/p/{profileId}";

using var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, url);
request.Headers.Add("Accept", "application/json");

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
