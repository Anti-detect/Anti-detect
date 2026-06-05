var myHeaders = new Headers();
myHeaders.append("Accept", "application/json");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/81b5627a-1212-4016-9467-3dbe4d6f78eb/start?automation_type=puppeteer&headless_mode=false", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
