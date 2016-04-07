import os
import urllib
from urllib import request



# Open link to the site
url = 'http://www.bellevuecollege.edu'
req = urllib.request.urlopen(url)

req = urllib.request.urlopen(url)
status = req.getcode()
print(status)

header = req.getheaders()
print(header)

#Response Info
x = req.info()
print(x)