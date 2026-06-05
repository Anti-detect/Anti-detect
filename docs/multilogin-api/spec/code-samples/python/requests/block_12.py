import requests

url = "https://launcher.mlx.yt:45001/api/v1/profile/stop/p/81b5627a-1212-4016-9467-3dbe4d6f78eb"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
