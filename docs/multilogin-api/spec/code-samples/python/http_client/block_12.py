import http.client

conn = http.client.HTTPSConnection("launcher.mlx.yt", 45001)
payload = ''
headers = {
  'Accept': 'application/json'
}
conn.request("GET", "/api/v1/profile/stop/p/81b5627a-1212-4016-9467-3dbe4d6f78eb", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
