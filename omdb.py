import urllib.request as urlreq
import json

movieName = input('Enter movie name')
url="http://www.omdbapi.com/?apikey=b87f1130&t=" + movieName
try:
    req = urlreq.Request(url)
    req = urlreq.urlopen(req).read()
    json_data = json.loads(req.decode('utf-8'))
    print('Movie released in ' + json_data['Year'])
    print(json_data)
except urllib.request.HTTPError as e:
    print(e.code)
