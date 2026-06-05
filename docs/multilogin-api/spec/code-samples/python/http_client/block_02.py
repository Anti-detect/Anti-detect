import http.client

conn = http.client.HTTPSConnection("launcher.mlx.yt", 45001)
payload = ''
headers = {
  'Accept': 'application/json'
}
conn.request("GET", "/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/81b5627a-1212-4016-9467-3dbe4d6f78eb/start?automation_type=puppeteer&headless_mode=false", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
