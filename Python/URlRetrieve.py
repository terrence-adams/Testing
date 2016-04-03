from urllib import request

url = "http://www.bellevuecollege.edu"

a = request.urlopen(url)
b = a.read()

print(b)

c = a.info()
print(c)