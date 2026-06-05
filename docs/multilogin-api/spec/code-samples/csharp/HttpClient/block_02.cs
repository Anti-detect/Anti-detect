var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/81b5627a-1212-4016-9467-3dbe4d6f78eb/start?automation_type=puppeteer&headless_mode=false");
request.Headers.Add("Accept", "application/json");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
