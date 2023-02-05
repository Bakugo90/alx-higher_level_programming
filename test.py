

from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()