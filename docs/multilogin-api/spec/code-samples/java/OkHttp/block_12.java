var myHeaders = new Headers();
myHeaders.append("Accept", "application/json");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://launcher.mlx.yt:45001/api/v1/profile/stop/p/81b5627a-1212-4016-9467-3dbe4d6f78eb", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
