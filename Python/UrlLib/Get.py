import urllib
from urllib import request
import urllib.parse

url = "http://www.bellevuecollege.edu/directory"
req = urllib.request.urlopen("http://www.bellevuecollege.edu/directory")

values = {"txtQuery" : "Terrence Adams"}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

print(data)
requestOne = urllib.request.Request(url, data)

resp = urllib.request.urlopen(requestOne)

respData = resp.read()
responseFile = open("responseFile.txt","w")
responseFile.write(str(respData))