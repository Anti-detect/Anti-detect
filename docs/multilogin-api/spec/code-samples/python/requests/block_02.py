import requests

url = "https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/81b5627a-1212-4016-9467-3dbe4d6f78eb/start?automation_type=puppeteer&headless_mode=false"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
